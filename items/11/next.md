seq: 2
from: overseer
authority: D19, D20 (Alistair)
date: 2026-11-26T17:58Z
---
#11: two decisions from Alistair.
1. D20: retire wt_mcseed now, as you proposed. First check that it is clean, fully merged, holds no gitignored files (git worktree remove deletes those silently), and has no Slurm job or other session in it. Then run ./link_data.sh --remove and git worktree remove, without --force. Keep the branch. Keep wt_mt: this conversation lives there.
2. D19: this session takes on #18 (ULX-8 in 0830191601, and the 138 ObsIDs with more than one target). Report first and change nothing. Read #18's checklist line and the records it points to. Then report: what #18 must produce for #19 and for Alistair's #17 review; what already exists on main (the [obsid:tag] code, any regions); a plan in steps; and the price in core-h, files and login-node hours.
Update your checklist line, and end with the rule-12 report.
