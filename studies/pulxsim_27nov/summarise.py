#!/usr/bin/env python3
"""summarise.py: one table of a50/a95, K and leakage per scenario and method, from results/*.json."""
import json, glob, os, sys
sys.dont_write_bytecode = True
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.abspath(os.environ.get("PULXSIM_OUT", os.path.join(os.getcwd(), "pulxsim_out")))
src = out if os.path.isdir(os.path.join(out, "results")) else here   # your reruns, else the committed results
order = ["clean_faint", "clean_faint_E", "clean_bright", "edge", "diffuse", "fainter_nbr25", "brighter_nbr5", "brighter_nbr10",
         "brighter_nbr15", "brighter_nbr25", "robust_nbr10", "robust_nbr15", "target_off", "offaxis_mod", "offaxis_strong", "offaxis_strong_faint"]
fmt = lambda v: "none <= 1" if v is None else f"{v:.3f}"
for name in order:
    p = f"{src}/results/{name}.json"
    if not os.path.exists(p):
        continue
    r = json.load(open(p))
    print(f"\n## {r['scenario']}  ({name}, {r['nreal']} realisations, {r['seconds']} s)")
    if "neighbour_own_K" in r:
        print(f"   neighbour's own oracle K: {[round(v, 1) for v in r['neighbour_own_K']]}")
    base = r["methods"]["hard 20\""]["a95"]
    for k, d in r["methods"].items():
        rel = "" if (d["a95"] is None or base is None) else f"  a95/hard20 {d['a95'] / base:.3f}"
        leak = f"  leak {[round(v, 3) for v in d['leak_fraction']]}" if "leak_fraction" in d else ""
        print(f"   {k:<40} target photons {d['target_photons_in_region']:9.0f}  K {d['K_mean']:9.1f} (sd {d['K_sd']:6.1f})"
              f"  a50 {fmt(d['a50'])}  a95 {fmt(d['a95'])}{rel}{leak}")
