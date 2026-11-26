seq: 1
state: idle
date: 2026-11-26T17:25Z
host: login7c
---
#42: wrote "Per-photon source probability" on methods42, as the board asked (seq 1, overseer). Committed, queue entry updated; waiting for the next subsection.

Done (seq 1):
- methods42 head 6ad166b, on top of 54d5a13. Docs only: docs/methods_section.md, no code, so no suite run.
- The queue entry now names 6ad166b. Checklist: 4 of 8 subsections written, 4 TO WRITE (weighted search statistic, blind survey, sensitivity, validation).
- The subsection is paper text in four parts:
  - p_i and its ingredients: S, B, s(E) from the small region rescaled by the King encircled-energy ratio, the 2-D off-axis PSF on the live footprint, flat f_bkg.
  - The two-component flare background: a 10-12 keV full-field monitor, per-CCD live time, low-live bins counted as quiet, 3/4 sigma split; why time-scrambled nulls are invalid.
  - The wide 60-70" aperture, and the 20" radius for the HENDRICS arm.
  - What p_i buys, from the ablation (15.220).
  Sources are listed in the comment after it.
- Every code detail was checked against radial_weighting.py and run_template_pipeline.py, not only the summary. One correction came of it: in the two-component model, bins under 30% live count as quiescent rather than being held at the mean (that is the single-phi path, 15.194).

For Alistair or the overseer (no action needed now):
- Stale CLAUDE.md pointer: the params.conf note cites "summary 7.10" for the timing radius, but it is 7.11. 7.10 is the blind-seed zoom window. The subsection cites 7.11. I didn't edit CLAUDE.md (rule 15c).
- methods42 is off main d03bf93, and main may have moved since. Docs-only, so the merge should be textual.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- "Per-photon source probability" written and committed on methods42 (6ad166b); queue entry and checklist updated.

NEEDS YOU:
- Nothing.

NEXT:
- #42: the next subsection when the board sends it. In outline order that is "Weighted search statistic".
