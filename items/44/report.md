seq: 0
state: running
date: 2026-11-26T17:13Z
host: login7c
---
Doing: #44/#46, finishing B's batch 1 (job 12424696) so #46 can be scored. First board report.

My last terminal report (25 Nov) said 12424696 was pending. It has since finished, so this report is up to date, not that one.

Alistair's 25 Nov instructions (typed in my terminal, = D4) all reached me:
1. Finish batch 1, resubmitting shards 1-5 from the same commit with hashes recorded: DONE. 12424696 COMPLETED, all 5 tasks, 0 errors. Code byte-identical to 1cbad1c (logs/longpext/sha256_12424696.txt). Batch 1 now has 164 / 164 records.
   Then score #46 on all 164: NOT YET DONE, next step (the job finished while this session was down).
2. Hold batch 2 until #46 is decided: HELD, nothing submitted.
3. Add a line to docs/LESSONS.md on pilot coverage: DONE. Group 7 bullet, longpext 5bb342b (on the branch; not yet queued).
Earlier (20 Nov): the merge record is relabelled "(merge 1)" and longpext's (12)-(14) stay. This is in the queue note for longpext at 1cbad1c (= S1).

Jobs: 12424696 (finished). None running.
Core-h: this step 77.0 billed. Batch 1 total 552.6 (quoted 270-440 before the overrun, then about 110 more approved: 475.6 + 77.0). Since #44 began: about 625 (C1 pilot 1.9, C1 64.2, B pilot 6.1, batch 1 552.6).
Files: 146,194 (26 Nov).

SETTLED:
- #44/#46 batch 1 complete: 164 / 164 records, 0 errors. Recorded in summary 15.225 (14)(g)-(h). The completion record goes in with the #46 scoring commit.
- Batch 2 held (D4).
- LESSONS group 7 pilot line (5bb342b).

NEEDS YOU:
- Nothing now. Batch 2 (116 draws, re-projected about 270-280 core-h billed, cap 448) waits until #46 is decided, then Alistair's go (above 50 core-h, and above the 135-215 first approved).

NEXT:
- Score #46 by its fixed rule (summary 15.230 (9), logs/longpext/stacked46_score.py) on all 164 draws (login node, minutes). Write 15.230 (10) and the validation figure, and post the outcome, with the result in summary.txt, not here (rule 15e).
  - FIRM (b) or (c): bring that option's nulls (about 20-60 core-h), the code change and the 0791010101 golden slot, before #13.
  - UNRESOLVED: bring both options' nulls first ((b) 40-60, (c) 20-40 core-h).
- Then ask about batch 2. B is scored only on all 280 draws.
