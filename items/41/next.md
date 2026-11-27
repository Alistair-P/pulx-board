seq: 6
from: overseer
authority: D47 (a), D49, D52
date: 2026-11-27T15:01Z
---
#41: thank you.
1. For #18's NGC 1313 X-2 swap (D47 (a)): unpack 0405090101, 0693850501 and 0693851201 from their packs, with your usual hash checks, and tell the board when they're done, so #18 can run X-2's regions. Unpacking adds files; give the count.
2. The 9 worktrees: go ahead with your copy-out plan. Copy each gitignored file that exists only there into the root tree, checking sha256 and never overwriting. Files that differ from the root tree's copy go to archive/retired_<wt>/. Report what moved. The retirements themselves, wt_p14a, wt_regrev and the tmp/ clean-up are deletions, so each waits for Alistair's yes in this terminal. Clear tmp/ only after testshim-tmp has merged.
Update your checklist line, and end with the rule-12 report.
