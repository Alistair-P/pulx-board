seq: 1
state: running
date: 2026-11-26T17:51Z
host: login7c
---
#37 (a95 inclusion cut): carrying out instruction seq 1 (D11). The a95cut golden jobs have been submitted and are running.

Done for seq 1:
1. main 2513b12 (mcseed) merged into a95cut in wt_a95cut (7d97027, clean, not a merge to main). Suite on that tree: 737 passed, 0 failed, 3 skipped, the same as main (logs/regen/suite_a95cut_ms.log in the root tree).
2. Pre-registered in 15.226 (18) and committed (ed97357) before submission. Reference: mcseed's merged-tree run (GOLD_TAG ms), because the literal compare against the frozen reference fails on main for main's own reasons (15.217 (12) deviation). main 2513b12 differs from mcseed's run tree only by a test and a LESSONS line.
   - Accept lists were computed on the merged tree. Coherent GOLD_ACCEPT = survey_pipeline.py only: it is the only manifest module matching neither MANIFEST nor ADOPTED. Orbit GOLD_ORBIT_ACCEPT = the same five as mcseed's: four that are byte-identical to main, plus survey_pipeline.py.
   - Both lists were exported before sbatch --export=ALL (the comma split, LESSONS group 7).
   - Prediction: all 19 coherent inputs bit-identical to ms, and the orbit run identical to check_ms on all 4 (run 1 = run 2), because a95cut changes only survey_list(), which no golden input calls.
3. Jobs: 12436028 syn (19 CPUs x 1:45), 12436029 real (4 x 1:30), 12436030 orbit (1 x 3:00). Submitted from the clean HEAD ed97357, all RUNNING. Hashes are in wt_a95cut logs/a95cut/golden/sha256_a9c_12436028.txt.
   If all are bit-identical I mark a95cut ready. If anything differs I stop and report the difference.

D12 noted: after rednoise is on main, #38 rebuilds the red rows. Once a95cut is on main too, I rerun a50 and --list and report before rewriting the live list.

Jobs: 12436028, 12436029, 12436030 (running).
Core-h: this step's cap is 42.3 billed, about 12.5 expected. Since the item began: 45.5 + 3.4 billed for the a95 work, plus this step.
Files: no reading taken.

SETTLED:
- None yet for seq 1. The golden result follows in the next report.

NEEDS YOU:
- Nothing.

NEXT:
- When the jobs finish: run logs/a95cut/golden_diff_a9c.py and the orbit --same check against check_ms, record the result in 15.226 (18), mark a95cut ready or report the difference, then post the result.
