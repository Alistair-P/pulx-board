seq: 3
state: needs-you
date: 2026-11-26T18:01Z
host: login7c
---
Doing: #46, answering the overseer's table question (seq 3) from the code and the record. No new runs. Holding.

1. v1.0 today uses the NO-ARM table above 120 ks.
   - In octave_thresholds.applied_table (main's 20857320, the same as 1cbad1c), R1 applies whenever the stacked arm cannot be judged: r1 = (ALLOCATION == "R1") or M outside RF_M_STACKED 2-4. Above 120 ks M = 5, so those rows are R1.
   - I checked this by calling it: the 122 and 136 ks rows report allocation R1, margin 1.1.
   - B's draws took their coherent thresholds from survey_pipeline.thresholds_for(T), which is that same table. So my no-arm column IS v1.0 as it stands, and keep-the-gap scores exactly as that column. It does not score like (b) without (b)'s stacked-only draws.
2. Nothing is needed to switch. Keep-the-gap means no code, no nulls and no golden. One optional cosmetic edit: the UNUSABLE reason text for M 5 says "MEASURE it (C3)"; under keep-the-gap it could say "no stacked arm above 120 ks (#46)". That is a manifest-module edit, not needed, and only offered.
3. R0 and R1:
   - R0 (15.125): the non-orbit alpha is split into coherent Z1 0.004275, stacked 0.004275 and Z3 0.00095, with a signed margin of +1.4.
   - R1 (15.123): the stacked arm is dropped and its share goes to Z1 (Z1 0.00855, Z3 0.00095), with a signed margin of +1.1.
   - So R1 -> R0 is Z1 +1.71 (share halved, plus margin +0.3) and Z3 +0.27 (margin only).

Recorded: summary 15.230 (10)(f), longpext 3696fd4. That is a summary-only commit; the code stays frozen at 1cbad1c and nothing from main is merged in.

Jobs: none. Core-h: 0 this step. Since #44 began, about 625.
Files: not read this step.

SETTLED:
- v1.0 already uses R1 above 120 ks, so keep-the-gap needs no change (15.230 (10)(f)).

NEEDS YOU (Alistair):
- #46: adopt (b) (nulls 40-60 core-h, code, golden slot 0791010101, before #13), or keep the gap (no change; #46 closes).
- #44 batch 2: now (about 270-280 core-h billed, cap 448), or after the tag with wt_longpext frozen at 1cbad1c's code.

NEXT:
- Holding; nothing started. wt_longpext's code stays frozen at 1cbad1c until batch 2 is decided.
