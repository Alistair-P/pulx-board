seq: 1
state: running
date: 2026-11-26T17:50Z
host: login7c
---
#15 (intake): carrying out D9/D10. Batch 1's downloads are under way, and its first Slurm seed + prep job is submitted.

**D9, downloads:**
- logs/intake15/download_odfs.sh fetches the 14 ODFs one at a time on the login node.
- A file goes into ODF_tarballs only if tar reads it back AND logs/intake15/check_xsa_tar.py finds the ODF complete against its own summary file list.
- The checker reuses seed_odf's completeness test. The XSA puts the summary beside a <rev>_<obsid>.TAR that holds the rest of the ODF, and the checker counts both. test_intake15 passes 16/0/0.
- Progress: 3 of 14 done, all complete. Source, UTC date, bytes and sha256 are recorded per file in stats/intake15/downloads_batch1.tsv. They go into INTAKE.md when all 14 are in.

**D10, the Slurm job:**
- slurm/submit_intake_prep.sh runs one ObsID per array task on 1 CPU, through run_batch.py --only. Each task writes its own result files, uses an ObsID-specific SAS_RAND_SEED, and applies the 194,000 file stop.
- The stale 0742490101 .part file is removed.
- Pilot: job 12435948 seeded and prepped 0742490101 (100 ks) ok, in 20.3 min, with a peak memory (MaxRSS) of 13.7 GB. So --mem is 18000M, which bills 3 CPUs at cosma5's 6,000 MB per CPU.
- Price, from batch 1's 8 measured runs (0.20–0.34 min per ks): 38 ObsIDs (24 unprepped + 14 downloads) come to 12.8–16.3 task-h, which is 38–49 billed core-h. Files: about +3,100 after, with a peak of about +8,000 at 8 concurrent, starting from 149,805. Both are within D10, so it's submitted.
- Submitted: job 12436014, an array of the 26 ready ObsIDs (24 seed + prep, plus 2 downloads already complete), at most 8 running at once.
- The 12 ObsIDs whose downloads are still running go in a second array once each passes the check. That array is inside the same price.
- Batch 1's state is recorded in §15.229 (22), commit e8cea7e.

Jobs: 12435948 (pilot, done), 12436014 (running).
Core-h: about 1.0 billed this step so far (pilot: 20 min × 3 CPUs); up to 49 for the whole job; since the item began, the same (everything earlier ran on the login node).
Files: 149,805 (26 Nov, before the job).

SETTLED:
- 8 of batch 1's 32 non-download ObsIDs are prepped: 7 from the login run and 1 from the pilot.
- The completeness check works on the XSA layout, and every download so far is complete.
- The first Slurm job is submitted within D10.

NEEDS YOU:
- None.

NEXT:
- Submit the second array for the 12 remaining downloads once they pass the check, and record all 14 in INTAKE.md.
- When the job finishes: collect the per-task results, record billed core-h, the file count and any failures in §15.229, and post the report.
