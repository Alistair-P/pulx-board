#!/usr/bin/env python3
"""scenarios.py NAME...: run the study's scenarios; writes $PULXSIM_OUT/results/<name>.json
(default ./pulxsim_out). Run it from outside this folder."""
import json, time
import os, sys
sys.dont_write_bytecode = True      # keep the board clone clean (no __pycache__)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.environ.get("PULXSIM_OUT", os.path.join(os.getcwd(), "pulxsim_out")))
if os.path.realpath(OUT).startswith(os.path.realpath(HERE)):
    sys.exit("Don't write inside the study folder: it is part of the board clone, and a changed file there "
             "stops every session's board sync. cd somewhere else first, or set PULXSIM_OUT.")
import numpy as np
sys.path.insert(0, HERE)
import pulxsim as P
from pulxsim import Scenario, King, aperture_weights, fit_weights, oracle_weights

def S(name):
    if name == "clean_bright":
        return Scenario("Bright, clean, on-axis", Nt=40000, beta=2.3), (), 40
    if name == "clean_faint":
        return Scenario("Faint, clean, on-axis", Nt=1500, beta=2.3), (), 120
    if name == "clean_faint_E":
        sc = Scenario("Faint, clean, on-axis, with energies", Nt=1500, beta=2.3, energy=True)
        ex = [{"joint fit + energy": lambda ev: fit_weights(sc, ev, energy=True)[:2],
               "oracle, position only": lambda ev: oracle_weights(sc, ev, False)}]
        return sc, ex, 120
    if name == "edge":
        sc = Scenario("Bright, at a window edge (no. 1)", Nt=40000, beta=2.3, nbrs=[(42.0, 42.0, 3000)],
                      planes=[(-1, 0, 15.0), (0, -1, 40.0)])
        ex = [{"weighted 20\" (full-circle scaling)": lambda ev: (aperture_weights(sc, ev, 20, True, aware=False), None),
               "weighted 60\" (full-circle scaling)": lambda ev: (aperture_weights(sc, ev, 60, True, aware=False), None)}]
        return sc, ex, 40
    if name == "diffuse":
        sc = Scenario("Faint, on diffuse emission (no. 2)", Nt=1200, beta=3.1, energy=True, bkg_annulus=(30.0, 60.0),
                      diffuse=dict(x=-80.0, y=-75.0, rb=40.0, beta=0.6, at_src=3.9))
        ex = [{"joint fit + background map": lambda ev: fit_weights(sc, ev, bkg="map")[:2],
               "joint fit + diffuse model": lambda ev: fit_weights(sc, ev, bkg="model+flat")[:2],
               "joint fit + diffuse model + energy": lambda ev: fit_weights(sc, ev, bkg="model+flat", energy=True)[:2],
               "oracle, position only": lambda ev: oracle_weights(sc, ev, False)}]
        return sc, ex, 120
    if name == "fainter_nbr25":
        return Scenario("Fainter neighbour at 25\" (no. 3)", Nt=50000, beta=0.95, nbrs=[(25.0, 0.0, 5000)]), (), 40
    if name.startswith("brighter_nbr"):
        d = float(name[len("brighter_nbr"):])
        return Scenario(f"Brighter neighbour (3x) at {d:g}\" (M82 X-2 style)", Nt=5000, beta=1.0,
                        nbrs=[(d, 0.0, 15000)]), (), 80
    if name.startswith("robust_nbr"):
        # the fit's model is wrong: true PSF broader (rc 6.5", alpha 1.6 against the model's 5.5", 1.5)
        # and both true positions 1.5" off their catalogue positions, in different directions
        d = float(name[len("robust_nbr"):])
        return Scenario(f"Brighter neighbour at {d:g}\", with PSF and position errors", Nt=5000, beta=1.0,
                        nbrs=[(d, 0.0, 15000)], psf_true=King(rc=6.5, alpha=1.6),
                        tgt_off=(0.0, 1.5), nbr_off=[(-1.06, -1.06)]), (), 80
    if name == "target_off":
        return Scenario("Target off, bright neighbour at 14\" (no. 4, D60)", Nt=150, beta=3.0,
                        nbrs=[(0.0, 14.0, 5000)]), (), 80
    if name.startswith("offaxis"):
        sx, sy = (1.3, 1.1) if name.endswith("mod") else (1.6, 1.15)
        tru = King(sx=sx, sy=sy, theta=45.0)
        faint = name.endswith("faint")
        sc = Scenario(f"Off-axis, PSF stretched {sx}x by {sy}x (no. 5)" + (", faint" if faint else ""),
                      Nt=1500 if faint else 40000, beta=1.3, psf_true=tru)
        ex = [{"weighted 20\" (matched PSF)": lambda ev: (aperture_weights(sc, ev, 20, True, psf=tru), None),
               "weighted 60\" (matched PSF)": lambda ev: (aperture_weights(sc, ev, 60, True, psf=tru), None),
               "joint fit 60\" (matched PSF)": lambda ev: fit_weights(sc, ev, psf=tru)[:2]}]
        return sc, ex, (120 if faint else 40)
    raise SystemExit("unknown scenario " + name)

os.makedirs(os.path.join(OUT, "results"), exist_ok=True)
for i, name in enumerate(sys.argv[1:]):
    sc, ex, n = S(name)
    t = time.time()
    res = P.run(sc, n, np.random.default_rng(1000 + i), extra=ex)
    res["seconds"] = round(time.time() - t, 1)
    res["params"] = {"Nt": sc.Nt, "beta": sc.beta, "nbrs": sc.nbrs, "planes": sc.planes, "diffuse": sc.diffuse,
                     "energy": sc.energy, "bkg_annulus": sc.bkg_annulus, "masks": sc.masks,
                     "psf_true": [sc.psf_true.rc, sc.psf_true.al, sc.psf_true.sx, sc.psf_true.sy],
                     "tgt_off": sc.tgt_off, "nbr_off": sc.nbr_off}
    json.dump(res, open(os.path.join(OUT, "results", f"{name}.json"), "w"), indent=1)
    print(name, res["seconds"], "s")
    for k, d in res["methods"].items():
        print(f"   {k:<40} K {d['K_mean']:10.1f}  a50 {d['a50'] if d['a50'] is None else round(d['a50'],4)}  a95 {d['a95'] if d['a95'] is None else round(d['a95'],4)}"
              + (f"  leak {[round(v,3) for v in d['leak_fraction']]}" if 'leak_fraction' in d else ""))
    sys.stdout.flush()
