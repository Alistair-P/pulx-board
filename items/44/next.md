seq: 7
from: overseer
authority: D29, D31, D33 (Alistair)
date: 2026-11-26T18:39Z
---
#44: this repeats instruction 6 and adds Alistair's decision. Don't redo steps you've already done.
D33: Alistair adopts (d) for #46. That's the stacked arm at M = 4 on one 120 ks window of each observation above 120 ks, using the existing 120 ks calibration, recorded as a post-hoc option.
1–3 (D29, as before): score (d) on the 164 draws under R0 and as the add-on beside R1; the analytic wander comparison; propose and price a confirming simulation without running it. Post these first.
4 (D31): price the union (K_eff) check, and run it if it is within 40 core-h billed.
5 (D33): then implement (d) on a NEW branch off current main, in a new worktree. Don't use wt_longpext, which stays frozen at 1cbad1c for B.
- Use the budgeting that scores better in step 1. If both have 95% intervals entirely below zero against no arm, stop and report instead.
- The window is the first or last 120 ks, whichever the flare monitor scores better, fixed before any search and recorded in the output JSON.
- Put the window rule in survey_pipeline.run_one, the 120 ks stacked row in octave_thresholds, and the same window in survey_sensitivity, all with tests.
- Add the golden slot above 120 ks (0791010101) and run the golden check, priced first. Ask if it is above 50 core-h.
- Don't write the ADOPTED line; that needs Alistair. Then queue it, ahead of #13.
Batch 2 stays held. Post a report after steps 1–3, after step 4, and when (d) is queued.
