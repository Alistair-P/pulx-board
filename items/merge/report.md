seq: 10
state: running
date: 2026-11-27T19:30Z
host: login7c
---
Merge session: targets18 (#18, the rest) merged; longpext is not queued yet, so regfix (#15) is next.

targets18 5d45f76 -> main 6dd6232 (trial merge 5298aaf + record). Root tree moved to 6dd6232.
- Merged 5d45f76, the commit its new queue entry names. It contains 3b851cc (seq 10) and bc0ef53 (packed-guard fix). No conflicts.
- No manifest or orbit-path module. params.conf: three new bare NGC 1313 X-2 sections, and the old bare ones renamed to :D201068601010001 (D47 (a)). The sections the golden inputs read are unchanged, so no golden.
- Suite 802/0/3.
- #18's 15.235 (10) sat at the end of the file on its branch, inside 15.236. I moved it unchanged into 15.235 after (merge 1) (number order); a check confirms the moved lines are identical. Record 15.235 (merge 2).
- The batch and ngc1313 slurm scripts are on main, not submitted.
- validation_check: 0 MISSING; 175-177 unindexed (figidx46 waits for longpext).
Inform: #18 (5d45f76 on main; (10) moved into 15.235); #11 (targets18 complete on main).

Jobs: none. Core-h: 0. Files: not taken.

SETTLED:
- #18: targets18 at 5d45f76 merged, main 6dd6232, 15.235 (merge 2), suite 802/0/3.

NEEDS YOU:
- none.

NEXT:
- regfix (#15, re-queued with main merged in), then intake15, pickfix. longpext and figidx46 when #44 queues longpext; cert13 waits for its golden (Alistair's yes, D59).
