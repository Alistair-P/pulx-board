seq: 4
from: overseer
authority: overseer: questions for Alistair's #46 and B decisions
date: 2026-11-26T18:09Z
---
#44: this replaces instruction 3 and includes it. Answer from the record, with no new runs. Post one short report and keep holding.
1. (From instruction 3.) In your no-arm column, Z1 is at the lower threshold and (b) is at +1.71, but keep-the-gap says "v1.0 keeps R1 above 120 ks". Above 120 ks, which Z1/Z3 table does v1.0 use today: the no-arm table, or one that still reserves the stacked arm's false-alarm share? If the second, what would switching to the no-arm table above 120 ks take (code, nulls, golden), and is it inside #46's scope? Define R0 and R1 in one line each.
2. Alistair's idea, a new option (d): run the stacked arm at M = 4 on one 120 ks window of each observation above 120 ks. The window would be the first or last 120 ks, whichever is less affected by flaring, chosen from the flare monitor before any search. Would (d) use the existing calibrated 120 ks stacked thresholds with no new nulls? What would it need (code, golden)? Would it pay the same +1.71 Z1 cost as (a)–(c)? And what would it cost, in core-h, to score (d) on the same 164 draws? Price only, and record it as a post-hoc option if it's ever run.
3. In a few lines, confirm what the stacked arm's "Doppler slide" does: does it follow a frequency drift between segments, and does the stacked arm do any orbit correction?
4. In a few lines, why does the long-period orbit part stop at 80 ks: cost scaling, calibration, or something else? Cite the section.
Keep wt_longpext's code frozen at 1cbad1c (don't merge main into it) until batch 2 is decided.
