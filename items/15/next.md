seq: 6
from: overseer
authority: D53, D54, D55
date: 2026-11-27T14:10Z
---
#15: thank you. Three fixes are approved, all bug fixes in tooling. Price any compute first.
1. D53: apply the one-line folder-lookup fix to new_obs_regions.run_one (glob <obsid>_*/dir, else <obsid>/dir), with a test. Then run the other 31 batch-1 regions (about 30 min on the login node), draw their PNGs, and tell the board how many are ready. Make target_name call #18's shared new_obs_regions.stack_name, so both sessions use one naming rule.
2. D55: remove NGC1313-X2 from new_obs_regions.HOLD_SOURCES. Alistair released it on 18 Nov (§15.229 (8)).
3. D54: add the filter rule to pick() on pickfix, with tests and the replay: a Closed or CalClosed exposure is never the primary while an open-filter one exists. Then prepare 0150280101's re-prep command.
The cluster policy now needs Alistair's own yes in this terminal for every sbatch and every deletion. So for 0884030101 (deleting the 4 failed files, then its sbatch) and 0150280101's re-prep, show him the exact commands here and wait for his yes.
Update your checklist line, and end with the rule-12 report.
