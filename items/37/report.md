seq: 1
state: needs-you
date: 2026-11-26T21:31Z
host: login7c
---
#37 (a95 inclusion cut): instruction seq 1 (D11) is finished. a95cut's golden check passed as pre-registered, and a95cut is queued READY.

Result (15.226 (18); jobs from wt_a95cut at ed97357, main 2513b12 + a95cut):
- Jobs 12436028 syn (0:27), 12436029 real (0:36) and 12436030 orbit (0:11) all COMPLETED 0:0. 11.3 core-h billed (cap 42.3).
- check_reference: only survey_pipeline.py differs from the manifest (accepted).
- Coherent: all 19 inputs BIT-IDENTICAL to mcseed's merged-tree run (ms). As predicted.
- Orbit: run 1 = run 2 on all 4, and all 4 IDENTICAL to check_ms. As predicted. --orbit-compare against the frozen reference shows the same 'result' differences on the three real cases as main's ms and mtm runs (15.217 (12) deviation, main's own). Recovery (b) PASS.

Caveat for the merge session and the overseer: main moved during the run (quota41b, rednoise, intake15; now 6b0b68f).
- I merged 6b0b68f into a95cut (head 6b015e2). The one conflict was a docs/TODO.md line, resolved by keeping main's RESOLVED red-rows line and appending D12's who-does-what.
- survey_pipeline.py on main is still 27678708, so the hash to adopt is still f9f49373.
- Suite on the new tree: 765 passed, 0 failed, 3 skipped, the same as main.
- The golden check was NOT rerun on this tree. rednoise changed red_noise_floor.py (an orbit-path module) and re-froze the orbit reference, so the tree the merge session will build differs from the one checked. a95cut itself still changes only survey_list(), which no golden input calls.

Queue: a95cut READY at 6b015e2. Its note says not to rewrite the live list at this merge (D12). The ADOPTED line for survey_pipeline.py f9f49373 is the merge session's to write (approved by Alistair 18 Nov).

Jobs: none running.
Core-h: 11.3 this step. Since the item began: 45.5 + 3.4 + 11.3 billed for the a95 work (earlier #37 steps are in 15.199 and 15.226).
Files: no reading taken.

SETTLED:
- #37 seq 1: a95cut golden PASS (coherent 19/19 bit-identical, orbit 4/4 identical to mcseed's run; jobs 12436028-30, 11.3 core-h). main 6b0b68f merged in, suite 765/0/3, queued READY. 15.226 (18), commits ed97357, 697569a, 5f65d66 and 6b015e2.

NEEDS YOU:
1. Rerun a95cut's golden on main 6b0b68f + a95cut before it merges, comparing against rednoise's merged-tree golden (about 11 core-h, 3 jobs, same scripts)? Recommend yes only if the merge session's rule asks for the golden on the exact merged tree. The change is off the golden path, and the merge session will run the suite on its trial anyway.

NEXT:
- After a95cut is on main and #38 has rebuilt the production red records (D12): rerun a50 --all --thresholds applied and --list from a fresh worktree off main, and report the list before rewriting logs/survey_full/obsids_longest_first.txt.
