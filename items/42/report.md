seq: 3
state: idle
date: 2026-11-26T17:50Z
host: login7c
---
#42: wrote "The blind survey" on methods42, as the board asked (seq 3, plan 42.1). Committed, queue entry updated; waiting for the next subsection.

Done (seq 3):
- methods42 head 21b26d6, on top of 4ff1e7c. Docs only: docs/methods_section.md, no code, so no suite run.
- The queue entry now names 21b26d6. Checklist: 6 of 8 subsections written; 2 TO WRITE (Sensitivity, Validation).
- The subsection is paper text in eight parts:
  - Band and octaves, 6.8 Hz down to 0.0066 Hz, with per-octave fdot ranges: orbit, spin-up and the torque cap below about 0.05 Hz.
  - The span switch at 17 ks.
  - The three arms: coherent Z1/Z3; stacked, M = ceil(T/30 ks) with the Doppler slide; orbit, 0.05-0.7 d with the frozen 16 ks bank to 1.7 Hz, plus the long-period part at 57.5-80 ks with its frequency-tolerance caveat. Published orbits demodulated with their GTIs.
  - The comb fill, gap form, below 0.2125 Hz.
  - Refinement (top 20 per octave per arm) and ranking.
  - Thresholds: the alpha split, the random-field model and its validated ranges, UNUSABLE outside them, margins +1.4 / +1.1, the orbit arm's measured thresholds, the red-noise scale with its KS gate.
  - Eccentric orbits, the text that was in the stub.
  - The survey list.
- Current values were taken from the code, not from pipeline_description section 11, which is partly stale (it predates P11, the random-field thresholds and the orbit-arm changes). Checked: pulx_recovery, survey_pipeline, octave_thresholds, orbit_search, comb_fill, slurm/submit_survey_full.sh. Sources are listed in the comment after the subsection.
- Fixed before committing:
  - "settings fixed before any survey output was examined" is now "fixed and validated before it is run for results". The step-1 JSONs exist, kept only for comparison.
  - "up to three arms", since the stacked arm needs M >= 2.
  - The span-carrying of A now names its fitted power-law correction.
  - The eccentricity loss is written with x, the projected semi-major axis.

OPEN in the text, marked in place:
- The survey-list cut. Main has a50 <= 0.4 (15.155 (8)); #37's a95 < 0.25 is queued, not merged. I'll fill it in once a95cut lands; it's a one-line edit.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- "The blind survey" written and committed on methods42 (21b26d6); queue entry and checklist updated.

NEEDS YOU:
- Nothing.

NEXT:
- #42: "Sensitivity" when the board sends it, then "Validation". After a95cut merges, the one-line survey-list fill-in.
