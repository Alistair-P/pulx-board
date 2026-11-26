seq: 0
state: idle
date: 2026-11-26T17:11Z
host: login7c
---
#25 (artefact battery, check (k)): calibration finished and accepted; p14a-calib (5f9a009) waiting in the merge queue; first board report.

Jobs: none
Core-h: this step ~0 (one test rerun on the login node). Since the item began: section 15.228 in all < 1 core-h on the login node; the earlier parts' costs are in sections 15.221 and 15.224.
Files: no quota reading taken.

Instructions that reached this session:
- No board instruction: there is no items/25 folder, and none of the 25 Nov entries S1-S7 in DECISIONS.md is addressed to #25.
- One instruction reached me by terminal: "#25: accepted, including your Small Window correction; add the 21-line bound (0.025^(1/21) ~ 84%) to section 15.228 (11); the veto/review choice stays with #27". DONE, with one correction (below).
- Two of the 25 Nov entries touch #25 indirectly:
  - S1 (merge order mcseed, quota41b, intake15, p14a-calib 5f9a009, ...): p14a-calib is still in the queue at 5f9a009, ready.
  - S5 (#27: "record the (k) catch rate as 84-95.6%"): see the difference flagged below.

FLAG, board vs record (the record wins): the 82 caught forgeries come from 24 distinct lattice lines, not 21. Of these, 11 lines are in the first run and 21 in the extension, with 8 in both; 21 is the extension's 67 forgeries alone. So section 15.228 (11) gives a one-sided 95% lower bound of 0.025^(1/24) = 85.8%, with 84% only if the extension alone is counted. The (k) catch rate is therefore about 86-95.6%. BRIEF.md and S5 say 84-95.6%; #27's REV. 3 should take 85.8 from section 15.228 (11).

SETTLED
- Check (k) is ADOPTED as battery rule set rev3 (= rev2 + (k)).
  - False vetoes: 0 of 480 at a50 (95% upper limit 0.77%) and 0 of 960 including 1.3 a50. NGC 7793 P13 (0804670401), the one applicable known pulsar, passes.
  - Forgeries at Z^2 >= 30: 82 of 82 caught, by the 15 in the first run and 67 in the pre-registered extension (section 15.228 (10), recorded before the run). The 95% lower bound is 95.6% counting forgeries and 85.8% counting the 24 lattice lines.
  - Coverage: the forgeries come from 2 Full Frame observations. Large Window and Extended Full Frame cannot forge Z^2 30; Small Window is untested (the user accepted this on 20 Nov).
- Section 15.228 (12) records for #27: (d) -> review (ULX pulses are intermittent); (k) -> veto candidate, with the candidate still listed as a rejected artefact. #27 decides.
- Figure 173 is in the shared store and indexed. The 36 P14a records were re-measured: no verdict changed, and rev2 and rev3 have 0 FAIL.
- Tests: the suite at 76acd5d passes (5f9a009 changes summary text only). test_frame_raw_equiv failed on 20 Nov only because 0693760401 had been packed; it passes after #41's restore (rerun 26 Nov, log in the worktree under stats/p14a_calib/lattice/).
- The checklist #25 line and the queue note are updated.

NEEDS YOU
- Nothing blocking for #25. The (k) veto vs review choice is #27's; this session doesn't decide it.

NEXT
- Merge session: p14a-calib is 9 commits behind main since mcseed (merge 2), so it needs a trial merge. Expected conflicts are append-only: summary.txt, validation/README.md, validation_plots.py and run_all_tests.sh. No manifest or orbit-path module is touched, so no golden check is needed.
- This session waits on the board.
