seq: 14
from: overseer
authority: 44.5 (D39, D59)
date: 2026-11-27T16:17Z
---
#44: (d) is on main (stacked46d, main 57974c9; ADOPTED octave_thresholds.py ab3e3264, survey_pipeline.py 9b8ce8b0; window slot frozen in speedup_reference/window_golden/).
1. The merge session's validation_check lists 175_stacked46, 176_stacked46d and 177_longpext_Bfut as unindexed. Add their rows to validation/README.md on a new branch from main (docs only), and queue it.
2. D39: Alistair approves your confirming simulation for (d), on main's merged code. Write the decision rule of 15.230 (11) into the record before any draw, and commit it. Prepare the pilot (about 3 core-h, 8 draws across both octaves, both span bins and both amplitudes), then show Alistair the exact sbatch, directory, resources and billed core-h in this terminal. Submit only on his yes (D59). Reprice from the pilot. If the full run is within 110 core-h billed, ask him in this terminal for it; otherwise post needs-you with the price. Report the result against the rule.
Update your checklist line, and end with the rule-12 report.
