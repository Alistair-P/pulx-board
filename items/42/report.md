seq: 7
state: idle
date: 2026-11-26T18:26Z
host: login7c
---
#42: built the span-bin table from main's code, as the board asked (seq 7, the correction to 6; "Validation" not redone). Waiting.

Full table with sources and notes (ignored, not committed): /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_methods42/logs/methods42/span_bins.md
Read from main 1399fad. Targets are #15's table, stats/intake15/survey_spans.csv (571 targets on 386 ObsIDs), binned on T_ks. Bin edges follow the code: (lo, hi], with 17-30 = [17, 30].

span ks | targets (ObsIDs) | coherent Z1/Z3 | stacked | orbit short bank | long part | alloc
<17 | 94 (71) | runs, all rows UNUSABLE (valid 17-136 ks) | M1: none | 0.01-1.7 Hz, M 1-2, <=16 ks segs | no | R1
17-30 | 138 (101) | 0.0066-6.8 Hz, full span | M1: none | M2, 8.5-15 ks | no | R1
30-57.5 | 124 (91) | full span | M2, 15-28.75 ks | M2-4, <=16 ks | no | R0
57.5-60 | 16 (7) | full span | M2, 28.75-30 ks | M4 | yes | R0
60-80 | 60 (35) | full span | M3, 20-26.7 ks | M4-5 | yes | R0
80-90 | 8 (5) | full span | M3, 26.7-30 ks | M6 | no | R0
90-120 | 68 (45) | full span | M4, 22.5-30 ks | M6-8 | no | R0
>120 | 63 (31) | full span (max 135.8 ks) | M5: UNUSABLE, share to Z1 | M8 on min(T, 128 ks); 21 targets use best 128 ks window | no | R1

All rows:
- Coherent fmax: 6.8 Hz, capped by the frame Nyquist (1.7 Hz in Extended Full Frame). fmin 0.01 Hz below 17 ks, else 0.0066 Hz.
- Comb fill: octaves topping <= 0.2125 Hz at every span, in the coherent, stacked and orbit arms (comb_gti is passed to orbit_arm) and in refinement.
- Long part: 57.5 < T <= 80 ks only, octaves 0.2125-0.425 and 0.425-0.85 Hz. Its templates join the short bank on the same 16 ks segments, refined in the full-span metric, with stage (iii) thresholds per M.
- Orbit thresholds are measured for M1-M8, all 8 octaves usable.
- Allocation: R0 iff the stacked arm is judged (M 2-4); R1 at M 1 or 5. Margins +1.4 / +1.1.

Orbital periods: short bank P_orb 0.05-0.7 d (a sin i to a Roche-filling He donor). Long part 0.7 d to T/0.21, i.e. 3.2-4.4 d over 57.5-80 ks, a sin i to the 10 Msun ceiling. Published orbits are demodulated instead.

Totals: 571; <17 ks 94 (no usable coherent threshold); 57.5-80 ks 76, where the long part runs; >120 ks 63, where the stacked arm is unusable.

UNCONFIRMED:
1. Whether #15's T_ks equals run_one's span (raw event-time range); a target near a bin edge could move.
2. Which spans the orbit arm's M1 thresholds were measured at, i.e. whether an orbit search under 16 ks is inside its validated range.
3. The cost guard's action per observation (dropping Z3, lowering fmax to no less than 1.7 Hz). It should not fire on this list (max 135.8 ks; memory binds from ~154 ks), but that wasn't checked per observation.

Checked and confirmed on the way: the floor model's low Z1 octaves are valid at 17-136 ks (valid_T_coherent).

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- Span-bin table posted; full version at the path above. No code or doc changed, nothing committed.

NEEDS YOU:
- Nothing.

NEXT:
- #42: wait for the board (the survey-list fill-in once a95cut merges).
