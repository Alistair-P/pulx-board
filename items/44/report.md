seq: 8
state: running
date: 2026-11-26T23:23Z
host: login7c
---
#44/#46, seq 8, step 2 report: I ran the union (K_eff) check on the add-on (R1W) allocation, and it passed. The (d) golden is nearly done.

Seq 8 step by step:
1. DONE (reported before): the add-on raises thresholds only above 120 ks. Checked in the code: window_applies() needs T > 120 ks and M > 4. Output is byte-identical to main for 17-120 ks, and above 120 ks with ZSQW_STACKED_WINDOW=0.
2. DONE: the union check, which uses synthetic nulls only.
   - Priced from measured costs first. The first design was 400 fresh full-band nulls; I had priced it from a restricted-band figure, and it really costs ~5.8 h per null. I cancelled that job (12438600) after 4 min, with nothing written, at 1.1 core-h.
   - The redesign reuses the existing 136 ks coherent null sets (t136 and v136, 400 each) and regenerates each t136 seed's photons exactly to run the new window arm on them. The window arm's cost was measured at 230 s per null.
   - Run at T = 136 ks rather than the ~128 ks named, because that is the span of the existing sets and of the longest targets. The rule was fixed before any window realisation (summary 15.236 (2)/(2a)).
   - RESULT: 2 of 400 realisations crossed any threshold in the union, against 3.80 expected. P(>= 2 | 3.80) = 0.89, so it PASSES (the rule was k <= 7).
   - Each arm alone: Z1 1 (expected 2.36), Z3 0 (0.26), window 1 (1.18). The union with every threshold shifted by -0.75 / +0.5 / +1.0 was 3 / 2 / 1.
   - No measured margin is needed.
   - Billed 22.8 core-h (16 CPUs x 1:25), within D31's 20-40.
3. IN PROGRESS: (d) is implemented on the new branch stacked46d, off main 6b0b68f, in a new worktree. wt_longpext is untouched and still frozen at 1cbad1c.
   - The window rule is in survey_pipeline.run_one and the R1W table plus the 120 ks M 4 "stw" row are in octave_thresholds. survey_sensitivity records the same window. The window choice and both scores go into the output JSON.
   - Tests: test_stacked_window passes 7 of 7. The full suite passes once the flags-off v1.0 reference tests also switch the window off (4422c5f).
   - Golden, priced before running: the cap was 42.5 core-h, now 46.5 because SLURM gave the window job 5 CPUs. That is under 50, so I didn't need to ask.
     - Synthetic + real: 19 of 19 inputs BIT-IDENTICAL to main's last golden, as predicted.
     - Orbit golden: every number identical, and the (b) recovery check passes.
     - New slot 0791010101: the two-run determinism check (job 12438661) is still running.
   - No ADOPTED line written. Not queued yet: I will queue it ahead of #13 once the window slot finishes, then post the "queued" report.
4. NOT STARTED: the confirming simulation, as instructed. It is with Alistair.
Batch 2 is still held.

Jobs: 12438661 (golden window slot, running ~1.5 h, cap 20 core-h). Finished: 12438651 (union), 12438658/59/60 (golden syn/real/orbit), 12438600 (cancelled).
Core-h: this step 22.8 union + 1.1 cancelled + 11.5 golden so far (syn 8.7, real 2.4, orbit 0.4) = 35.4, plus the running window job. Before seq 8, #44/#46 had used batch 1's 552.6 plus small scoring runs.
Files: no quota reading taken.

SETTLED: union check PASS (2/400 vs 3.80); golden 19/19 identical; orbit golden PASS.
OPEN: the window-slot determinism check, then queueing stacked46d ahead of #13. ADOPTED and the confirming simulation need Alistair.
Records: summary.txt 15.236 (2a)-(5) on branch stacked46d (a47c3db); stats/stacked46d/union46d_score.json.
