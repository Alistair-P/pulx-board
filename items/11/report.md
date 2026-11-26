seq: 2
state: needs-you
date: 2026-11-26T18:02Z
host: login7c
---
#11/#18: did instruction seq 2 (D19, D20): retired wt_mcseed; scoped #18, report first, nothing changed.

1. D20: wt_mcseed RETIRED. Clean, 0 ahead of main, no job, no other process. 10 real ignored files: 3 already identical in the root tree; 7 were mcseed's run records (golden job outputs, sha256 file, diff json, suite logs), cited by 15.217 (12) and found nowhere else. Copied to the root tree's logs/mcseed/ (cp -n, sha256 checked 7/7), then link_data.sh --remove (287 links), git worktree remove, no --force. Branch mcseed kept. wt_mt kept.

2. #18 SCOPE (MEASURED from #15's intake tables, read-only in wt_intake15/stats/intake15/). 138 ObsIDs carry 323 list targets, so 185 targets beyond the bare one:
- span >= 17 ks: 116 ObsIDs, 162 extra targets:
  - already processed, unpacked: 8 ObsIDs, 15 targets;
  - already processed, packed: 19 ObsIDs, 33 targets;
  - still to process (#15/#16 batches): 89 ObsIDs, 114 targets (78 tarball, 8 none, 3 prep).
- span < 17 ks: 22 ObsIDs, 23 targets, deferred by D1.
15.229 (12) counted 170 tags on a different span basis; step 1 reconciles.
Includes ULX-8 (0830191601, 4 list targets) and NGC 7793 ULX-4 (0693760101, recovery set).

WHAT #18 MUST PRODUCE. For #19 (QA, data-based a95/a50, IN list): every extra target as an [obsid:tag] section with its own products under targets/<tag>/ (pipeline_inputs.json, spectra, expmap, frame-aligned events, barycentred at its own position), so cfg_for / survey_sensitivity run per target. For #17 (Alistair's review): per target the region result (src, aperture, bkg, mask), counts, flags rows in the new_obs_flags format, and the P30 neighbour handling (a listed target inside another's aperture is masked; none in a background circle: preflight ERROR).

ON MAIN ALREADY: [obsid:tag] sections, per-target products and barycentring (preprocess.sh, pipeline_config.tid_of/cfg_for); preflight P30 rules; new_obs_regions.py --target (ONE target, never staged: stage() skips tags); figure 157; tests (test_multitarget 17). MISSING: a batch region run and a staging file for tags, flags rows for tags, and an analysis-only run (a tagged preprocess.sh also runs both production searches, qa_obs and survey_pipeline: the P30 pilot did).

PLAN:
1. Target table (login, ~1 h, no compute): tag, bare choice, span, stage, neighbours inside 65", per ObsID.
2. Tooling on a branch off main (tests, queue): batch --target regions, data/params_new_targets.conf staging (not params.conf), flags rows, an analysis-only switch.
3. Regions for the 27 processed ObsIDs (login). The 19 packed ones need #41 to unpack them in small batches. Then the #17 review.
4. After review: run_analysis per tag on compute, 2-tag pilot first; load check; #41 packs.
5. The 89 new ObsIDs: same steps inside #15/#16's batches, after each bare target's prep and regions.
6. Hand #19 the section list and product check.

PRICE (INFERRED unless marked):
- Compute: run_analysis at 1-3 core-h per tag (15.229 (7)) gives 160-490 billed core-h for all 162. The pilot's 5.5 (MEASURED) included the searches. Pilot about 6-10 core-h, then priced per batch.
- Files: 26 per tag (MEASURED, targets/ULX8), so about 4,200 for 162, plus temporary unpacks. Quota 145,712 (26 Nov).
- Login: about 1-2 h for steps 1-2, then about 3-8 h of region runs spread over the batches.

Jobs: none.
Core-h: 0 this step; #18 0 so far.
Files: 145,712.

SETTLED:
- #11: wt_mcseed retired per D20 (records preserved, branch kept); checklist #11 note updated.

NEEDS YOU:
1. Do MIN_COUNTS = 1000 and HOLD_SOURCES apply to tags as to bare targets? Recommend yes (an inclusion rule: Alistair).
2. Should tags stop after run_analysis (new analysis-only switch), so no production-search or survey output exists before the v1.0 certificate? Recommend yes (touches blinding: Alistair).
3. Approve the 2-tag pilot (about 6-10 core-h) once the tooling is queued? The full 160-490 core-h needs your approval per batch.
4. Work #18 in wt_mt on a new branch targets18 off main (saves 287 new links), instead of a new worktree? Recommend yes.

NEXT:
- On the answers: step 1 (target table, no compute), then step 2's tooling with tests. Nothing started.
