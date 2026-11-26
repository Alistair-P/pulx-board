seq: 5
from: overseer
authority: D29 (overseer; Alistair asked for a harder test)
date: 2026-11-26T18:22Z
---
#44: thank you. Alistair is leaning towards (d), and asked whether a harder test should come first, with signals that the coherent search loses but a windowed arm could catch. D29: three cheap steps, recorded as post-hoc. Don't change wt_longpext's frozen code; a separate scoring script in logs/ is fine.
1. Score (d) on the same 164 draws (your price: under 0.3 core-h) under both allocations: (i) R0 (Z1 +1.71, Z3 +0.27), and (ii) the add-on beside R1 (+0.71 on every arm). For each, give detection fractions for binaries, wander and isolated, the paired difference against no arm with its 95% interval and McNemar p, and the stacked-only and no-arm-only counts.
2. Analytic only, no runs: for random-walk phase wander of total rms 1, 3 and 10 rad over the span, and for the binary population, estimate the amplitude (as a multiple of each target's a50) at which no arm (R1) and (d), under each allocation, reach 50% and 95% detection. Use the real thresholds and η. Say where, if anywhere, (d) detects signals that no arm cannot reach at any plausible amplitude. If the record holds any measurement of ULX pulsars' timing noise or wander over about a day, say which wander levels it supports.
3. Propose, but don't run, a small simulation to confirm step 2 where (d) looks best: draws, amplitudes, wander levels, a decision rule fixed in advance, and a price in core-h. Also give the price of the optional union (K_eff) check.
Post one report with all three. Keep holding batch 2, and keep wt_longpext frozen at 1cbad1c.
