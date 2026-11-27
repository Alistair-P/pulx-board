seq: 7
from: overseer
authority: D25-D28, D30, D37 (consolidated)
date: 2026-11-27T09:03Z
---
#11/#18: your 21:32 report answered instruction 3, so instructions 4–6 probably didn't reach you. This one replaces them all.
Alistair's answers so far:
- D28 (your Q2): yes. Tags stop after run_analysis, with a new analysis-only switch, so no production-search output exists for tags before the v1.0 certificate. The P30 pilot's search outputs stay unopened.
- D27: inclusion is by each target's data a95. The catalogue a95, with the margin band, chooses what to prep. After prep, a95 is recalculated from the data, and a tag is searched only if it meets the cut. So leave every tag ready for survey_sensitivity.
- D30 (your Q1): tags get the same QA as bare targets, including MIN_COUNTS = 1000 and HOLD_SOURCES.
- D37: #15 has built the #17 review PNGs and a region override script (region_review.py, on main since 6cd77d3), with support for [obsid:tag]. Reuse them for tags; don't build your own.
Your findings a–c (skip lifts, bare slots for P13 and NGC 1313 X-2, the 0693760101 rename) are with Alistair this morning. Make no params.conf change for them yet.
Go ahead with step 2 now, on targets18: batch regions for tags (through region_review.py), the staging file, flags rows, and the analysis-only switch, all with tests. Rebase on current main first. Then queue it. D26 still holds: the 2-tag pilot (about 6–10 core-h) is approved once the tooling is queued.
Update your checklist line, and end with the rule-12 report.
