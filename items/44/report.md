seq: 5
state: needs-you
date: 2026-11-26T18:42Z
host: login7c
---
Doing: #46 option (d), D29's three post-hoc steps. Full numbers: summary 15.230 (11), figure 176 (175 for (a)-(c)), stats/longpext/stacked46d_*.json. wt_longpext's frozen code is untouched: I only added new scripts.

STEP 1, MEASURED (164 batch-1 draws; window [0, 120 ks]; 3 min on the login node):
- The window arm alone crosses its threshold on 0 / 164.
- (i) R0 (Z1 +1.71, Z3 +0.27):
  - Binaries 0.129 vs no arm 0.161 ((d)-only 0, no-arm-only 3; diff -0.032, 95% -0.075 to 0; p 0.25).
  - Wander 0.297 for both.
  - Isolated 5/7 vs 6/7.
  - All: 36 vs 40 (diff -0.024, 95% -0.049 to -0.006, p 0.125). Stacked-only 0.
- (ii) Add-on (+0.71 on every arm): identical to no arm in every class (40 vs 40, 0 discordant).
- Harness check: "no stacked candidate in the window" means a sub-threshold signal, not a matching fault. Strong injections match within 4/T. Plateau centres can sit about 2 resolution elements off, so near-threshold stacked detections may be slightly undercounted, in (10) too.

STEP 2, SEMI-ANALYTIC (no runs):
- Model: coherent Z1 is a noncentral chi^2 at each draw's real threshold, with the real eta (50% at 1x a50), and retention computed from the actual walks and orbits. The window arm is 4 segment maxima against its real 120 ks threshold.
- Validation: the coherent part matches batch 1 (binaries 0.141 predicted vs 0.151 measured; 1 rad wander 0.18 vs 0.25). The stacked efficiency had to be FITTED (0.75, range 0.70-0.80, from small counts).
- Amplitude (x a50) for 50% / 95%, no arm | (d) R0 (add-on within 0.01):
  - steady: 1.00/1.23 | 1.01/1.24
  - wander 1 rad: 1.43/1.85 | 1.41/1.72
  - wander 3 rad: 2.39/3.80 | 1.76/2.26
  - wander 10 rad: 4.48/7.23 | 2.25/3.59
  - binaries (93): 3.25/13.5 | 1.63/3.02
- Z3 and the orbit arm are left out of the model; measured, they decided 0 and 1 of the 164.
- Where (d) reaches what no arm cannot at plausible amplitude: strong-Doppler binaries (half of B's prior has coherent retention < 0.1; no arm needs more than 4-13x a50) and wander of 3 rad or more. Nowhere for steady pulsars or wander up to 1 rad. B's binary prior is a design prior, not a population estimate.
- Wander in the record: 15.22 (P13, NGC 5907 ULX1; spans up to about 60 ks). The drift is a parabola (residual fdot). After an (f, fdot) refit it is consistent with zero at about 0.1-0.4 rad. That supports wander up to about 0.3 rad; nothing measures it over a day. 3 and 10 rad are far beyond anything measured, so the case for (d) rests on binaries.

STEP 3, PROPOSED, NOT RUN:
- Draws: 64 binary draws (B's prior, new seeds) at each of m = 1.5, 2.0 and 3.0 x a50 in real-eta terms, plus 32 wander draws at 3 rad and m = 2 (report only): 224 draws.
- Arms: Z1 on the injected octave (Z3 dropped), the short orbit arm, and the window arm. Each draw is judged under no arm, (d) R0 and (d) add-on.
- Rule, fixed before any draw: at m = 2.0 for binaries, (d) PAYS under an allocation if (d)-only > no-arm-only with McNemar p < 0.05. The model predicts 0.36 vs 0.80 there.
- Price: about 0.25 h per draw. Quoted 55-110 core-h billed, after a pilot of about 3 core-h (8 draws across both octaves, both span bins and both amplitudes; LESSONS 7). About 20 files.
- Union (K_eff) check, needed only if (d) is adopted: 400 nulls at about 128 ks, about 19 core-h compute, quoted 20-40 billed (from measured null costs).

Jobs: none. Core-h: this step about 0.05 (login node). Since #44 began, about 625.
Files: not read this step.

SETTLED:
- (d) scored post-hoc on batch 1, amplitude estimates made, and a simulation proposed (15.230 (11), fig 176, longpext 279ac5f). Checklist #46 updated.

NEEDS YOU (Alistair):
- #46: run the confirming binary simulation (pilot about 3, then 55-110 core-h), or decide now between (b), (d) (R0 or add-on) and keeping the gap.
- #44 batch 2: still held.

NEXT:
- Holding; nothing started. wt_longpext's code stays frozen at 1cbad1c.
