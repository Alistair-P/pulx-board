seq: 8
state: running
date: 2026-11-27T16:10Z
host: login7c
---
Merge session: stacked46d (#46) merged on Alistair's terminal yes (D46, board seq 8); starting targets18 next.

stacked46d 6a030a7 -> main 57974c9 (trial merge 649c935 + record commit). Root tree moved to 57974c9.
- Golden on the merged tree as reported (s46m): coherent 19/19 bit-identical, orbit 4/4 identical, window slot identical to w46d_r1/r2.
- ADOPTED: octave_thresholds.py ab3e3264, survey_pipeline.py 9b8ce8b0 (combined a95cut + (d)). Live hashes equal the golden commit's.
- Window-slot reference frozen: speedup_reference/window_golden/ = real_0791010101.json + SHA256SUMS (json de7f0d74, npz 867832aa; npz stays in stats/fast_golden/otcheck_A3w_w46d_r1) + _meta.json (module hashes). Format recorded in 15.236 (merge 1).
- After the lines: check_reference OK; test_p14a_drev, test_golden_keys, test_orbit_golden, test_stacked_window pass. Merged-tree suite 789/0/3.
- validation_check: 0 MISSING; UNINDEXED 175_stacked46, 176_stacked46d (#46's rows not in validation/README.md), 177_longpext_Bfut (#44).
Inform: #46 (on main; add README rows 175-176; the D39 confirming simulation can run on main's code); #44 (window slot frozen; D39 sim on main; row 177 unindexed); #13 (stacked46d on main: both blockers a95cut and #46 cleared; ADOPTED hashes above for the certificate); #37 (survey_pipeline.py on main is now 9b8ce8b0).

Jobs: none new. Core-h: 0 this step (golden 17.4, reported before). Files: not taken.

SETTLED:
- #46: stacked46d merged, main 57974c9, 15.236 (merge 1), ADOPTED x2, window slot frozen.

NEEDS YOU:
- none.

NEXT:
- targets18 (#18), then regfix (#15), intake15 (0ada393), methods42 (5264663), testshim-tmp (#41), each reported.
