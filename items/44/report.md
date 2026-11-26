seq: 4
state: needs-you
date: 2026-11-26T18:12Z
host: login7c
---
Doing: #44/#46, answering overseer seq 4 (which replaces seq 3) from the code and the record. No runs. Holding.

1. TABLE ABOVE 120 ks (as seq 3; 15.230 (10)(f)): v1.0 today uses the NO-ARM table there. octave_thresholds.applied_table takes R1 whenever M is outside RF_M_STACKED 2-4, and above 120 ks M = 5. I checked by calling it: the 122 and 136 ks rows report allocation R1, margin 1.1. B's draws used that table, so my no-arm column is v1.0 as it stands. Keep-the-gap needs no code, no nulls and no golden.
   - R0 (15.125): non-orbit alpha split Z1 0.004275 / stacked 0.004275 / Z3 0.00095, signed margin +1.4.
   - R1 (15.123): stacked arm dropped, its share to Z1 (Z1 0.00855 / Z3 0.00095), margin +1.1.
   - So R1 -> R0 is Z1 +1.71 and Z3 +0.27.

2. OPTION (d): M = 4 on one 120 ks window (first or last 120 ks, chosen from the flare monitor before any search). 15.230 (10)(g), priced only, post-hoc if run.
   - Thresholds: yes, the existing ones. M 4 at 120 ks with 30 ks segments is inside RF_M_STACKED and was validated there (15.97 Add. S, on the conservative edge), so no new stacked nulls. The window choice is phase-blind, so it adds no trials.
   - Caveat as for (a): the union of a windowed stacked arm with full-span Z1 / Z3 has an unmeasured K_eff. Conservative K meanwhile; an optional union check costs 20-40 core-h.
   - Z1 cost: under R0 the SAME +1.71 (Z3 +0.27) as (a)-(c). As an add-on beside R1 instead, +0.71 on every arm.
   - Code (manifest modules): the window rule in survey_pipeline.run_one (recorded in the JSON), the stacked row at 120 ks in octave_thresholds, and the same window in survey_sensitivity. Golden: the real slots are unchanged; add the slot above 120 ks (0791010101).
   - Expected: about (b) or a little less. It keeps 0.88-0.99 of the photons, with 30 ks segments against (b)'s 30-34. To beat no-arm under R0 it would need more than 4 stacked-only detections; (b) had 2.
   - Price to score it on the 164 draws: the draws regenerate from their seeds, and only stack_slide on [0, 120 ks] is new. On these draws (b)'s stacked arm measured 245 s in total, so about 10-15 min on the login node, < 0.3 core-h.

3. DOPPLER SLIDE (pulx_recovery.stack_slide, 15.45): each segment's Z^2 spectrum, already maximised over fdot within that segment, is replaced by a rolling maximum over +-v/c x f_top (v/c = 1.84e-3: a sin i 25.3 lt-s at P_orb 1 d, 15.39). The M results are summed and maximised once.
   - So each segment's peak may sit anywhere within that window of a common frequency, independently. Any drift or wander up to +-v/c is tolerated, but nothing tracks a continuous drift path between segments.
   - There is NO orbit correction: no demodulation and no orbit templates. Orbits are the orbit arm's job (bank, 16 ks segments).

4. WHY THE LONG PART STOPS AT 80 ks (15.225 (1); 15.171 (3), 15.173 (5), 15.178): calibration plus cost.
   - Stage (iii) ran long-part nulls only at M 4 (64 ks) and M 5 (80 ks), and thresholds are looked up by M. 80 ks is the longest span with measured nulls.
   - Spans above 80 ks were left to the short bank for cost: at fixed f the long part grows as ~T^3.7 (templates T^2.8 x per-template wall ~T; 64 -> 128 ks, INFERRED).
   - 57.5 ks is not a measured edge, only the stage-(ii) scorer's midpoint. 0.85 Hz is a cost cap (templates ~ f^3).

Jobs: none. Core-h: 0 this step. Since #44 began, about 625.
Files: not read this step.

SETTLED:
- Option (d) priced and recorded as post-hoc (15.230 (10)(g), longpext 0364fe4).
- The table question answered: keep-the-gap = no change (15.230 (10)(f)).

NEEDS YOU (Alistair):
- #46: adopt (b), keep the gap, or score (d) first (< 0.3 core-h, post-hoc).
- #44 batch 2: now (about 270-280 core-h billed, cap 448), or after the tag with wt_longpext frozen at 1cbad1c's code.

NEXT:
- Holding; nothing started. wt_longpext's code stays frozen at 1cbad1c.
