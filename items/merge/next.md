seq: 7
from: overseer
authority: D42, D46 (Alistair)
date: 2026-11-27T12:50Z
---
merge: this repeats D42 step 2 and adds Alistair's approval.
1. Carry on with stacked46d (#46, option (d)): trial merge on top of main df0a6f9, suite, and golden on the merged tree, including the 0791010101 window slot, priced first.
2. D46: Alistair approves both ADOPTED lines (octave_thresholds.py, and survey_pipeline.py at its combined hash), on two conditions. The merged-tree golden must pass as predicted: 19/19 coherent bit-identical, orbit identical, and the 0791010101 slot identical to stacked46d's own run. And the live hashes must match. If both hold, write the lines, freeze the window-slot reference from stats/fast_golden/otcheck_A3w_w46d_r1 into speedup_reference, and fast-forward main. If anything differs, stop and report.
3. Then, in this order: targets18 (#18, 992696d), intake15 (0ada393), methods42 (5264663).
Post a report after each merge, naming the sessions to inform.
