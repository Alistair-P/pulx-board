seq: 0
state: needs-you
date: 2026-11-26T17:15Z
host: login7c
---
Doing: #46, scoring the stacked-arm options above 120 ks on B's complete batch 1, per Alistair's 25 Nov instruction 1 (D4).

Alistair's 25 Nov instructions: 1 batch 1 finished (done) and #46 scored on all 164 (done, now). 2 batch 2 held (holding). 3 LESSONS line (done, 5bb342b).

Result is in summary.txt 15.230 (10) and figure 175 (validation store, 175_stacked46.png). Per rule 15e, no counts here.
- The rule fixed before any draw (15.230 (9)) gives FIRM (b), M capped at 4, over (c), M = 5. It holds at both corners of the threshold brackets and under equal weighting of binaries and wander.
- But (b) does not beat v1.0 without a stacked arm above 120 ks. Taking the arm's false-alarm share back raises the Z1 / Z3 thresholds (+1.7). That loses a few coherent detections near threshold, and (b)'s arm wins back fewer than that. The numbers are small and consistent with no difference. (a) and (c) do no better than (b).
- The expected M = 5 advantage under spin wander did not appear.
- B (#44) is untouched: #46's scorer never reads B's extension arm.

Jobs: none running (12424696 finished: 5/5 COMPLETED, 0 errors).
Core-h: this step 0 (scoring on the login node, minutes). Batch 1 total 552.6. Since #44 began, about 625.
Files: 146,194 (26 Nov).

SETTLED:
- B's batch 1 complete: 164 / 164 records, 552.6 core-h billed (15.225 (14)(i)).
- #46 scored by its pre-registered rule: FIRM (b) among the arms (15.230 (10), figure 175, longpext bd7b04a). Checklist lines #44 and #46 updated.

NEEDS YOU (Alistair; this changes the arms, so it is his call under POLICY):
- #46: adopt (b), or keep v1.0's gap above 120 ks?
  - ADOPT (b): (b)'s nulls (800 fresh at 122 and 136 ks, 40-60 core-h billed; double if the transfer check fails), the code change in manifest modules (M = min(ceil(T / 30 ks), 4)), and a new golden slot for 0791010101 (135.8 ks). All of it lands before #13.
  - KEEP THE GAP: no code and no nulls. #46 closes on this measurement, and v1.0 keeps R1 above 120 ks.
- #44 batch 2 (116 draws, re-projected about 270-280 core-h billed, cap 448): held until #46 is decided (D4). It then needs his go, since it is above the 135-215 first approved.

NEXT:
- On "adopt (b)": price and run the nulls (asking if above 50 core-h), make the code change on a branch, run the golden check, and queue. Before #13.
- On "keep the gap": close #46 in the checklist and summary, and tell #13.
- Then batch 2 on his go, and B scored on all 280 draws.
