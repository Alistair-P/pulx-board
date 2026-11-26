seq: 1
state: needs-you
date: 2026-11-26T17:26Z
host: login7c
---
Doing: #46, posting the numbers for Alistair's decision (overseer seq 1, D14). Simulated draws only. Full table: summary 15.230 (10)(e), figure 175, stats/longpext/stacked46_numbers.txt (wt_longpext).

Data: B's batch 1, 164 synthetic draws above 120 ks at each target's own catalogue a50: 93 binaries, 64 spin-wander, 7 isolated. Intervals are Jeffreys 68%. Paired differences use 4,000 bootstrap resamples.

THRESHOLD SHIFTS (every option against no arm, measured from the recorded tables):
- Z1 +1.71, Z3 +0.27. CORRECTION: I said "Z1 / Z3 +1.7" before. Z3 moves only 0.27 (15.230 (5) corrected).
- (b) and (c) share the same Z1 / Z3 table.
- Stacked thresholds: (b) median 121.7, bracket +-1.46; (c) median 138.5, bracket -2.17 to 0.

DETECTION FRACTION, binaries (n 93) | wander (n 64):
- No stacked arm above 120 ks (v1.0): 0.161 [0.127, 0.203] | 0.297 [0.244, 0.356]
- (a) 80 ks window: 0.129 [0.098, 0.168] | 0.297 [0.244, 0.356]
- (b) M capped at 4: 0.151 [0.117, 0.191] at nominal and at its low edge; 0.140 [0.108, 0.179] at its high edge | 0.297 at both
- (c) M = 5: 0.129 [0.098, 0.168] at both edges | 0.297 at both
- Isolated (n 7): 6 with no arm, 5 under every option.
- No arm and (a) have no bracket. Only (b)'s binary count moves inside the brackets.
- All four options detect the same wander draws: 15/16 at 0.3 rad, 4/16 at 1 rad, 0 at 3 and 10 rad.

PAIRED DIFFERENCE, (b) minus no arm:
- All 164, nominal and (b) low edge: -0.012 (b-only 2, no-arm-only 4); 68% -0.031 to 0.000; 95% -0.043 to +0.018; McNemar p 0.69.
- All 164, (b) high edge: -0.018 (1 vs 4); 68% -0.031 to -0.006; 95% -0.043 to +0.006; p 0.38.
- Binaries: -0.011 (2 vs 3; 95% -0.065 to +0.032); at the high edge -0.022 (1 vs 3).
- Wander: 0 (0 vs 0).
- All four no-arm-only draws are coherent Z1 detections between the R1 and R0 thresholds.

Jobs: none. Core-h: this step 0 (login node, minutes). Since #44 began, about 625.
Files: not read this step (146,194 on 26 Nov).

SETTLED:
- #46 decision numbers recorded: 15.230 (10)(e), longpext 6ffba25.
- Z3 shift corrected to +0.27 in 15.230 (5) and in figure 175's caption, re-rendered.

NEEDS YOU (Alistair; changes the arms):
- #46: adopt (b) (nulls 40-60 core-h billed, double if the transfer check fails; code in manifest modules; golden slot 0791010101; before #13), or keep v1.0's gap above 120 ks (no code, no nulls; #46 closes).
- #44 batch 2 (about 270-280 core-h billed, cap 448): held until #46 is decided (D4), then his go.

NEXT:
- Nothing started (per seq 1). On Alistair's #46 answer: the adopt-(b) or keep-the-gap steps in my previous report. Then batch 2 on his go.
