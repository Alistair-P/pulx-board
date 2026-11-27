seq: 11
state: needs-you
date: 2026-11-27T18:34Z
host: login7c
---
#18 (#11's session): did instruction 11. Batch 1 is prepared, not run; the rest of targets18 is re-queued; the X-2 swap job still waits for Alistair's yes.

QUEUE. The merge session took targets18 at 3e561ba ((merge 1), main 6db5e1f) and closed the line, so the commits after it were not taken. I merged main back into targets18 (90f9e8f; summary conflict only) and queued the rest as a new line at 5d45f76:
- the preprocess.sh packed-guard fix, with its test;
- the NGC 1313 X-2 bare / X-1 tag swap in params.conf (preflight 0 errors);
- two job scripts, neither submitted;
- target_table.py --batch;
- summary 15.235 (7)-(10), including the pilot PASS.
No manifest or orbit module. Suite on the merged branch: 800/0/3, the same as main.

BATCH 1, PREPARED, NOT RUN (15.235 (9)):
- Tag list: stats/targets18/batch1/tags_batch1.csv. 45 tags in 30 ObsIDs of #15's batch 1, all ready on disk.
- Job script: slurm/submit_targets18_batch.sh TAGS.csv. It first checks that every tag is a params.conf section and runs nothing otherwise; then preprocess.sh -a per tag. Cap 2 CPUs x 8 h = 16 core-h; batch 1 about 5-6 core-h (INFERRED from the pilot).
- The region tool was NOT run for batch 1 either, since D63 may change the region products.
- Order per batch, once D63 is settled: regions (login) -> Alistair's #17 review -> merge the sections into params.conf -> his yes to the exact sbatch -> the pilot's checks.

NOTE: D64, which instruction 11 cites, was not in DECISIONS.md when I checked.

Jobs: none.
Core-h: 0 this step; #18 about 0.23.
Files: +1 (tag list).

SETTLED:
- #18: batch 1 prepared (15.235 (9)); the rest of targets18 re-queued at 5d45f76, suite 800/0/3 (15.235 (10)).

NEEDS YOU:
1. Alistair, in this terminal: yes to `sbatch slurm/submit_targets18_ngc1313.sh`, from /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt (the X-2 swap; cosma5/durham, 2 CPUs, 12000M, 16 h, cap 32 core-h, about 1-2 expected)? Recommend yes.
2. Overseer: please record D64 in DECISIONS.md.

NEXT:
- On yes to 1: submit, wait for its sha256 file, check the 6 targets as for the pilot. After D63's stage-1 report and Alistair's scope decision: the batch steps above. Nothing started.
