seq: 2
from: overseer
authority: 13.2 (overseer; D15, D46)
date: 2026-11-27T16:17Z
---
#13: both blockers are on main. a95cut is df0a6f9, and #46's (d) (stacked46d) is main 57974c9. The ADOPTED lines are octave_thresholds.py ab3e3264 and survey_pipeline.py 9b8ce8b0 (a95cut and (d) combined), so your outstanding ADOPTED item is done. rednoise and p14a-calib are on main too.
Go ahead, on cert13, login node only:
1. Merge main (57974c9 or later) into cert13. Rerun build_cert --check and the full suite. Change the inclusion rule from PRE-a95cut to main's a95cut. Update the above-120 ks entry to D46's (d): the stacked window arm at M=4 and the add-on budgeting. Check that the re-derived tables show both.
2. Golden: list cert13's diff against main, by file. If it touches no module or input in gate_block()'s hash list, don't rerun the golden. Cite the merge session's merged-tree golden on 57974c9 (15.236, merge 1) instead. If it does touch one, price the rerun and ask Alistair in this terminal for his yes to the exact sbatch (D59).
3. Rebuild the draft with --check. List the blockers still open (mcseed, the Z1/Z3 = max(transfer, direct) rule above 120 ks, any others), with what each needs and whose item it is.
4. If the suite passes, queue cert13 for the merge session.
Update your checklist line, and end with the rule-12 report.
