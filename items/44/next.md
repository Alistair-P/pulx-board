seq: 8
from: overseer
authority: D33 (budgeting by score), D31
date: 2026-11-26T18:47Z
---
#44: thank you, that's clear. This replaces instruction 7 and repeats what's still needed.
Under D33, the budgeting is the better-scoring one: the ADD-ON beside R1. It scored identical to no arm (40 vs 40, 0 discordant), while R0's 95% interval is entirely below zero.
1. Before coding, confirm from the code that the add-on's +0.71 applies only to observations above 120 ks, where (d) runs. If it would raise thresholds at any other span, stop and report.
2. (D31) Run the union (K_eff) check: 400 nulls at about 128 ks, quoted 20–40 core-h billed. Price it from measured costs first, and run it if it is within 40.
3. (D33) Implement (d) with the add-on, on a NEW branch off current main, in a new worktree. Don't use wt_longpext, which stays frozen at 1cbad1c.
   - The window is the first or last 120 ks, whichever the flare monitor scores better, fixed before any search and recorded in the output JSON.
   - Put the window rule in survey_pipeline.run_one, the 120 ks stacked row and the add-on allocation in octave_thresholds, and the same window in survey_sensitivity, all with tests.
   - Add the golden slot above 120 ks (0791010101) and run the golden check, priced first. Ask if it is above 50 core-h.
   - Don't write the ADOPTED line; that needs Alistair. Queue it ahead of #13.
4. Your confirming simulation (pilot about 3, then 55–110 core-h) is with Alistair. Don't start it.
Batch 2 stays held. Post a report after step 2, and when (d) is queued.
