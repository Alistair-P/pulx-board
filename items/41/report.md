seq: 6
state: done
date: 2026-11-27T19:44Z
host: login7c
---
#41 (file quota): testshim-tmp reached main, so I cleared the leaked tmp/tmp* folders under Alistair's earlier yes. #41 is settled again.

No new board instruction (latest seq 6). Authority for the clean-up: Alistair's "Yes go ahead" in the #41 terminal, conditioned on the merge (seq 5/6).

DONE:
- Before the clean-up the folders had grown from 4,146 (census) to 5,750 while the fix waited to merge.
- Cleared: tmp/tmp* folders older than 1 h, 5,730 of 5,750 holding 50,028 inodes (counted with lfs find before). The 20 newer folders were left alone.
- Also cleared: my 21-inode suite_tmpdir.
- Quota 171,698 -> 121,644.
- Recorded as a dated addendum in 15.223 (15), commit 2818a4f (wt_q41, main + 1; summary only), queued under rule 14.

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began.
Files: lfs quota 121,644 / 200,000 (27 Nov).

SETTLED:
- #41: the tmp/tmp* leak is fixed on main and its backlog cleared (50,028 inodes); quota 121,644 (15.223 (15) addendum, 2818a4f queued).
- #41: checklist line set to settled.

NEEDS YOU:
- none.

NEXT:
- Nothing under #41. The 6 test files that make their own temp folders leave 8 entries per suite run, which is small; I'd only touch them if asked. Waiting on the board; nothing has been started.
