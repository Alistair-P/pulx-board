seq: 1
state: running
date: 2026-11-26T18:30Z
host: login7c
---
#15 (intake): job 12436014 finished. All 26 ObsIDs are seeded and prepped ok. The second array waits for the last 3 downloads.

- **Job 12436014:** 26 of 26 COMPLETED, every per-task result "ok".
  - Per ObsID: 3.6–21.5 min (seed + prep).
  - Peak memory (MaxRSS): at most 9.6 GB across the array; the pilot peaked at 13.7 GB.
  - Results: stats/intake15/batch1_slurm/, logs in logs/intake15/slurm/.
- **Billed:** 13.2 core-h (elapsed × 3 CPUs). That is well under the 38–49 priced for all 38 ObsIDs; the compute nodes ran 2–3 times faster than batch 1's login times.
- **Batch 1 now:** 34 of its 36 non-download ObsIDs are at prep (7 login + pilot + 26 Slurm), and the other 2 were already prepped (since 12 Oct).
- **Downloads (D9):** 11 of 14 are in, all COMPLETE against their summary lists. My previous report said "3 of 14 done"; at that moment it was 2. 0884030101 is downloading now, then 0400560301 and 0028740201.
- **Second array:** the 12 ObsIDs from the downloads, with the same script, --mem and throttle, submitted once the last download passes. Expected about 6–10 billed core-h, so the whole first job comes to about 20–25 against the D10 price of ≤ 49.

Jobs: 12435948 (pilot, done), 12436014 (done), second array not yet submitted.
Core-h: 14.2 billed so far (pilot 1.0 + job 13.2); the same since the item began.
Files: 155,292 (26 Nov, after the job).

SETTLED:
- Batch 1's seed + prep on Slurm works: 27 of 27 ok, including the pilot.
- The 11 downloads so far are complete and checked.

NEEDS YOU:
- None.

NEXT:
- When the downloads finish: record all 14 (source, date, sha256) in INTAKE.md and submit the second array.
- When it ends: record batch 1 in §15.229, post the report, and propose batch 2's job and price.
