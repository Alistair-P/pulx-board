seq: 2
state: idle
date: 2026-11-26T17:30Z
host: login7c
---
#42: wrote "Weighted search statistic" on methods42, as the board asked (seq 2, plan 42.1). Committed, queue entry updated; waiting for the next subsection.

Done (seq 2):
- methods42 head 4ff1e7c, on top of 6ad166b. Docs only: docs/methods_section.md, no code, so no suite run.
- The queue entry now names 4ff1e7c. Checklist: 5 of 8 subsections written; 3 TO WRITE (the blind survey, sensitivity, validation).
- The subsection is paper text in four parts:
  - The weighted Z_n^2 and the event phases. Its normalisation gives mean 2n and makes it invariant under w -> cw. The weights that maximise expected Z^2 are p*a(E), with g as the population estimate of a's shape. The energy factor doesn't move a phase, and psi(E) uses p alone.
  - The choice beta = 0.75: the efficiency eta(beta, gamma) on the 85 calibration observations, and the minimax regret (2.3% against 5.4% for beta 1 and 3.4% for beta 0.5). The gate and the production weighted search stay at beta 1, with the reason (15.196, 15.197).
  - Exact folds, and Z_3 from matched frequency derivatives. The injection test (6/21 against 15/21) shows why summing the fdot-maximised spectrum at f, 2f, 3f fails (15.53 (b)).
  - The single-fold null: chi^2_2 confirmed by 1e6 null trials (7.13). Search maxima are never read off a chi^2 table, and the survey subsection gives the measured thresholds.
- Checked against the code: pulse_stack.weighted_z2 (normalisation, w = p a(E)) and n_eff. Two wording points fixed before committing:
  - I had first said g leaves the phase in any energy bin unchanged. g varies within a bin, so the text now says g can't move a pulse whose phase is the same at all energies, and that psi(E) uses p alone.
  - The harmonic test now states its detection criterion: above the 90th percentile of each method's own null.
- No numbers from real-data searches are in this report. Those in the text come from simulations, nulls and injections, or are cited by summary section.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- "Weighted search statistic" written and committed on methods42 (4ff1e7c); queue entry and checklist updated.

NEEDS YOU:
- Nothing.

NEXT:
- #42: the next subsection when the board sends it. In outline order that is "The blind survey". It is the largest of the remaining three: arms, octaves, thresholds, red noise, orbit arm, comb fill, refinement.
