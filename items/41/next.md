seq: 4
from: overseer
authority: D49 (Alistair), plus instruction 3
date: 2026-11-27T12:51Z
---
#41: this repeats instruction 3 (the census) and adds a retirement Alistair approved.
1. (Instruction 3.) The file count rose from about 160,000 (26 Nov 21:41) to 172,545 (27 Nov 12:17). Using your usual scoped census (not a broad /cosma5 scan), report the top growth by folder, which item owns each, and what could be packed or removed safely. Delete nothing for the census. Re-project the count to the end of intake (batches 2–5, plus #18's 170 tags at about 26 files each).
2. D49: retire wt_p14a and wt_regrev. Keep the branches. For each:
   - check it's clean and fully merged into main, with no Slurm job and no Claude session in it;
   - copy any run records that exist only there (gitignored files that the summary cites) into the root tree, checking sha256;
   - run ./link_data.sh --remove, then git worktree remove without --force.
   Report the files freed.
Update your checklist line, and end with the rule-12 report.
