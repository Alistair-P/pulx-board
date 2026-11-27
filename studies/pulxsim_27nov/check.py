#!/usr/bin/env python3
"""check.py: (1) the null. With uniform phases, each method's Z^2_w should have mean 2 and
tail rates matching chi^2_2. (2) The shortcut. With the target pulsing, the detection rate from
direct phase draws should match the noncentral chi^2 prediction from K = (sum_target w)^2 / sum w^2."""
import json
import os, sys
sys.dont_write_bytecode = True      # keep the board clone clean (no __pycache__)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.environ.get("PULXSIM_OUT", os.path.join(os.getcwd(), "pulxsim_out")))
if os.path.realpath(OUT).startswith(os.path.realpath(HERE)):
    sys.exit("Don't write inside the study folder: it is part of the board clone, and a changed file there "
             "stops every session's board sync. cd somewhere else first, or set PULXSIM_OUT.")
import numpy as np
from scipy.stats import chi2, ncx2
sys.path.insert(0, HERE)
import pulxsim as P

rng = np.random.default_rng(20261127)
sc = P.Scenario("check: brighter neighbour at 15\"", Nt=5000, beta=1.0, nbrs=[(15.0, 0.0, 15000)])
meth = P.methods_for(sc)
NSP, NPH = 20, 1500          # spatial realisations x phase draws each
t2, t3 = chi2.isf(1e-2, 2), chi2.isf(1e-3, 2)


def draw_phases(n, a, rng):
    """phases with density (1 + a cos phi) / 2 pi, by solving phi + a sin phi = 2 pi u (Newton)."""
    u = rng.random(n) * 2 * np.pi
    ph = u.copy()
    for _ in range(30):
        ph -= (ph + a * np.sin(ph) - u) / (1 + a * np.cos(ph))
    return ph


out = {}
for k, fn in meth.items():
    zs_null, det, pred = [], [], []
    a = None
    for s in range(NSP):
        ev = sc.simulate(rng)
        w, _ = fn(ev)
        sel = w > 0
        ws, lab = w[sel], ev[2][sel]
        s2 = (ws * ws).sum()
        K = (ws[lab == 0].sum()) ** 2 / s2
        if a is None:      # amplitude giving about 50% detection for this method
            a = float(np.sqrt(2 * (P.THR - 1.3) / K)) if K > 0 else 1.0
            a = min(a, 1.0)
        for c in range(0, NPH, 250):
            m = min(250, NPH - c)
            ph = rng.random((m, ws.size)) * 2 * np.pi
            C, S = np.cos(ph) @ ws, np.sin(ph) @ ws
            zs_null.append(2 / s2 * (C * C + S * S))
            tgt = lab == 0
            ph2 = rng.random((m, ws.size)) * 2 * np.pi
            ph2[:, tgt] = draw_phases(m * tgt.sum(), a, rng).reshape(m, tgt.sum())
            C, S = np.cos(ph2) @ ws, np.sin(ph2) @ ws
            det.append(2 / s2 * (C * C + S * S) > P.THR)
        pred.append(ncx2.sf(P.THR, 2, a * a * K / 2))
    z = np.concatenate(zs_null)
    d = np.concatenate(det)
    out[k] = {"null_draws": int(z.size), "null_mean": float(z.mean()),
              "rate_1e-2": float((z > t2).mean()), "rate_1e-3": float((z > t3).mean()),
              "amplitude": a, "detect_direct": float(d.mean()), "detect_predicted": float(np.mean(pred)),
              "direct_se": float(np.sqrt(d.mean() * (1 - d.mean()) / d.size))}
    print(k, json.dumps(out[k]))
os.makedirs(OUT, exist_ok=True)
json.dump(out, open(os.path.join(OUT, "check.json"), "w"), indent=1)
