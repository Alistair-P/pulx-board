seq: 8
state: running
date: 2026-11-26T21:58Z
host: login7c
---
Doing: #46 option (d) per seq 8. Item 1 is confirmed, the union check was redesigned (one pricing error), and the golden check is submitted.

1. CONFIRMED FROM THE CODE: the add-on applies only above 120 ks. octave_thresholds.window_applies needs M = ceil(T / 30 ks) > 4 AND T > 120 ks. Only then is the R1W table used. Checked: applied_table at 17, 25, 40, 60, 75, 90, 105, 119 and 120 ks is byte-identical to main's, and so is every span with ZSQW_STACKED_WINDOW=0.

2. UNION CHECK, REDESIGNED BEFORE ANY RESULT (15.236 (2a)).
- My first design (600 fresh nulls at 128 ks) was MISPRICED. The 171 s per realisation I used was measured on P6's three low octaves only; a full-band coherent arm at 136 ks costs about 5.8 h per realisation. I cancelled job 12438600 after 4 minutes: 1.1 core-h, nothing written, nothing scored.
- New design: the coherent Z1 / Z3 maxima come from the EXISTING 136 ks null sets (t136, 400 realisations, all octaves; v136 for the three low octaves). The window arm is run new on t136's photons, regenerated exactly.
- Rule, fixed first: expected 3.80 crossings; PASS if k <= 7.
- Price from a MEASURED 230 s per realisation (window arm, full band): about 28 core-h billed, capped at 40. Job 12438651 is running.
- Seq 8 said 400 nulls at about 128 ks. This is 400 at 136 ks, the existing sets' span and the longest targets' (135.8 ks).

3. IMPLEMENTATION on branch stacked46d (wt_stacked46d, off main 6b0b68f; wt_longpext untouched):
- octave_thresholds: the R1W add-on table.
- survey_pipeline.run_one: the window is the first or last 120 ks, whichever has the larger sum p^2. p carries the flare monitor, so a flare lowers it. The window is chosen before any search and recorded in the JSON; the arm runs M 4 on it and is judged on "stw".
- survey_sensitivity: records the same window.
- fast_golden: the new slot real_0791010101, kept outside the 19 frozen inputs.
- tests/test_stacked_window.py 7/0/0. Summary 15.236 (1)-(4).
- GOLDEN, priced and submitted (12438658-61): the three standard parts measured at 12.7 core-h last time; the new slot about 5-12 (inferred); caps 42.5 in total, under 50. Prediction: the 19 inputs and the orbit golden bit-identical, and the new slot identical across its two runs.
- The full suite is running on the login node.

Jobs: 12438651 (union, running), 12438658 / 59 / 60 / 61 (golden, pending).
Core-h: this step 1.1 so far (cancelled job). Caps: 40 (union) + 42.5 (golden). Since #44 began, about 626.
Files: about 161,000.

SETTLED:
- The add-on is confined to spans above 120 ks (checked).
- Union check redesigned and running. (d) implemented with tests; golden check submitted.

NEEDS YOU:
- Nothing now. (The confirming simulation and batch 2 are held, per seq 8.)

NEXT:
- Score the union check and post the step-2 report.
- Compare the golden outputs and finish the suite. Then queue stacked46d ahead of #13, without an ADOPTED line, and post.
