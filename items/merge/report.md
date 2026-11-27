seq: 9
state: running
date: 2026-11-27T17:52Z
host: login7c
---
Merge session: targets18 (#18) merged at the queued commit; starting regfix (#15) next.

targets18 3e561ba -> main 6db5e1f (trial merge 11dbb8b + record). Root tree moved to 6db5e1f.
- The queue entry is BEHIND the branch tip: bc0ef53 (packed-guard fix, 15.235 (7)) and 50836e4 (swap prep) are NOT on main (seq 9: not taken unasked). #18 should queue them as a new entry if wanted.
- Conflicts textual: run_all_tests.sh (union, + test_targets18) and summary.txt (15.235 before 15.236). No lines lost.
- No manifest or orbit-path module changed, so no golden check and no ADOPTED line.
- Suite on the merged tree: 800 passed, 0 failed, 3 skipped.
- Record: 15.235 (merge 1). The pilot slurm script is on main, not submitted.
- validation_check: 0 MISSING; UNINDEXED 175, 176 (#46), 177 (#44).
Inform: #18 (3e561ba on main; bc0ef53 and 50836e4 not, queue them if wanted); #11 (targets18 on main, for its suite rerun); #15 (stack_name and region_review params mode now on main; regfix next).

Jobs: none. Core-h: 0. Files: not taken.

SETTLED:
- #18: targets18 merged at 3e561ba, main 6db5e1f, 15.235 (merge 1), suite 800/0/3.

NEEDS YOU:
- none.

NEXT:
- regfix (#15) at the commit its entry names, then intake15, methods42, testshim-tmp.
