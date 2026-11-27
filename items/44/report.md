seq: 10
state: idle
date: 2026-11-27T11:48Z
host: login7c
---
#44, seq 10 (D45), report: I added and indexed validation figure 177 for B's futility result.

1. DONE: figure 177 (177_longpext_Bfut.png, in the shared store), rendered and looked at, and indexed in validation/README.md (RECORDED, §15.225 (15)). Commit 2ff74a0 on wt_longpext.
   - Left: B's 100 batch-1 draws, WITH against WITHOUT. They are all on the diagonal: 0 WITH-only and 0 WITHOUT-only.
   - Middle: the combined McNemar p against batch 2's WITH-only count. The best case batch 1 allows is marked per cut: p 0.062 / 0.125, against the bar of 0.05.
   - Right: B's arm alone, statistic over threshold. It is over on 0 of 93 binaries; the highest is 0.99. 64 draws had a candidate near the spin and 29 had none inside the matching window.
   - The caption follows CLAUDE.md: WHAT IS PLOTTED, WHAT IT MEANS, then the source and summary section.
   - validation_check.py: 0 indexed figures missing. The 14 PNGs with no row predate this figure and are not mine to index.
2. Option A: not priced, as instructed; it is with Alistair. wt_longpext's pipeline code is unchanged since 1cbad1c (empty diff). Only summary.txt, validation_plots.py, validation/README.md and logs/ scripts were committed.
3. #46: noted. stacked46d is in the merge session's trial. The confirming simulation (D39) waits for the board's instruction once (d) is on main.
Checklist #44 updated.

Jobs: none.
Core-h: this step 0, login node only (minutes). Since the item began: batch 1 552.6, plus the pilot and C1 runs recorded in 15.225.
Files: +1 PNG in the shared store.

SETTLED: B NO-GO on futility, with its figure (177).
OPEN (with Alistair): option A; #46's ADOPTED lines.
