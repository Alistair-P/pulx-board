seq: 6
state: running
date: 2026-11-27T11:29Z
host: login7c
---
Merge session: a95cut (#37) merged under D42 step 1; starting stacked46d's trial (step 2, stop before ADOPTED / fast-forward).

a95cut 6b015e2 -> main df0a6f9 (trial-a95 merge 9c3ff8a, no conflicts; record commit df0a6f9). Root tree moved to df0a6f9.
- Golden (D41, priced first): against #37's golden tree ed97357 the only manifest/orbit-path module that changed is red_noise_floor.py (rednoise; orbit path). Coherent not rerun: no manifest module differs (survey_pipeline.py f9f49373 in both) and fast_golden never calls red_noise_floor (15.201 (3)). Orbit rerun on the merged tree, pre-registered: GOLD_TAG a95m, GOLD_ORBIT_ACCEPT=survey_pipeline.py, predicted PASS. Job 12440001, 1 CPU, 5 min 23 s: all 4 IDENTICAL, (b) PASS, orbit golden PASS. As predicted.
- Suite on the merged tree: 782 passed, 0 failed, 3 skipped. After the ADOPTED line: test_p14a_drev, test_golden_keys, test_orbit_golden pass again; check_reference passes.
- ADOPTED: survey_pipeline.py f9f49373 appended (Alistair 18 Nov, 15.226 (11)(c); confirmed in this terminal 27 Nov; D42). Live hash = branch = golden commit. Backups archive/ADOPTED.sha256.pre_a95cut_20261127, archive/summary.txt.pre_a95cut_merge_20261127.
- Record: summary 15.226 (merge 2); (16) is merge 1.
- Live list logs/survey_full/obsids_longest_first.txt NOT rewritten (D12).
- validation_check: 0 MISSING; UNINDEXED 175, 176 (stacked46, arrive with stacked46d).
Inform: #37 (a95cut on main; your a50 + --list rerun on #38's red records is next, report before rewriting the list); #38 (a95cut on main, for your red-record rebuild); #42 (a95 cut now on main, methods text can cite 15.226); #13 (a95cut blocker cleared; survey_pipeline.py ADOPTED f9f49373 for the draft certificate; stacked46d still to come).

Jobs: 12440001 (orbit golden, COMPLETED). Core-h: about 0.09 this step. Files: no new data files beyond stats/orbit_golden/check_a95m.

SETTLED:
- #37: a95cut merged, main df0a6f9, 15.226 (merge 2), orbit golden PASS, suite 782/0/3, ADOPTED survey_pipeline.py f9f49373.

NEEDS YOU:
- none now (stacked46d's ADOPTED lines wait for Alistair, per D42).

NEXT:
- stacked46d (#46): trial merge on top of main df0a6f9, suite, golden on the merged tree incl. the 0791010101 window slot; priced first; stop before ADOPTED / fast-forward and report.
