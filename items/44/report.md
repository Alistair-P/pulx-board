seq: 7
state: running
date: 2026-11-26T21:46Z
host: login7c
---
Doing: #46 option (d) per seq 7 (D29, D31, D33). Steps 1-3 were posted already (my report answering instruction 5; 15.230 (11), figure 176); not redone. Now step 4 (union check) is running, and step 5 has started on a new branch.

BUDGETING (seq 7: "the budgeting that scores better in step 1"): the ADD-ON. Under R0 (d) scored 36 vs 40 against no arm, 95% interval entirely below zero (-0.049 to -0.006). As an add-on it scored 40 vs 40. So the allocation is "R1W":
- The window's share 0.004275 joins R1's non-orbit budget, and all non-orbit shares are multiplied by 0.6897, so the total stays 0.01. The orbit share is unchanged.
- The rf model then gives Z1 +0.77, Z3 +0.83, and the window row +0.86-0.90 over the 120 ks R0 stacked row.

STEP 5 STARTED: branch stacked46d off main 6b0b68f, worktree wt_stacked46d (wt_longpext untouched, frozen at 1cbad1c).
- octave_thresholds: the R1W window table above 120 ks. The window threshold travels as "stw"; the full-span "st" stays NaN, so a caller that doesn't know the window sees v1.0's gap. ZSQW_STACKED_WINDOW=0 restores v1.0.
- Checked: tables at 17-120 ks, and above 120 ks with the switch off, are byte-identical to main's.
- tests/test_stacked_window.py 4/0/0, registered. Commit e37a247. Summary 15.236 (1)-(2), 3290fd8.
- Next: run_one's window rule, survey_sensitivity, the golden slot and its price. These wait until the union job has started, because the job imports from this worktree.

STEP 4, UNION (K_eff) CHECK: pre-registered and SUBMITTED, job 12438600 (pending).
- 600 null realisations at 128 ks: null_calibration.one's coherent arm plus M 4 on the first 120 ks, judged against the implementation's own R1W table.
- Expected 5.70 non-orbit crossings. PASS if k <= 10 (Poisson p >= 0.05); otherwise a measured margin is needed.
- Price: about 30 core-h billed, capped at 40 by --time 2:30 (D31). Hashes in logs/stacked46d/sha256_12438600.txt.

Jobs: 12438600 (pending).
Core-h: this step 0 so far (cap 40). Since #44 began, about 625.
Files: 160,947.

SETTLED:
- Add-on budgeting chosen by step 1. The threshold change is implemented and tested, with byte-identity at 120 ks and below.
- Union check pre-registered and submitted.

NEEDS YOU:
- Nothing now.

NEXT:
- When 12438600 ends: score it and post the step-4 report.
- Meanwhile, once it has started: run_one window rule (first or last 120 ks by sum p^2, recorded in the JSON), survey_sensitivity, tests, then price the golden check (ask if above 50 core-h). Then queue ahead of #13. No ADOPTED line.
