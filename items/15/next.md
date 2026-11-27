seq: 14
from: overseer
authority: D66 (Alistair)
date: 2026-11-27T22:30Z
---
#15: thank you for the stage-1 report. D66 (Alistair, 27 Nov 22:29) answers both of your questions, and two more. All four are yes:
1. D63 scope (ii). The joint fit applies only to targets with a neighbour at 0.1x the target's counts or brighter within 30". Every other target keeps its current p, aperture and masks. Select from eboxdetect plus a known-pairs list (M82 X-1/X-2, and any others you know of). Write the selection rule down before applying it, and list the result per target with its reason.
2. D63 (2), the QA rules. The fov check tests the background circles only. The count check and the region tool scale by exposed area. The aperture's exposed fraction becomes a correction, with REVIEW below 90%.
3. The attribution check: post_search.py as you designed it (outside the manifest; policy-passing candidates only).
4. 0150280101 NGC1313-X2 stays out. Record it as Alistair's decision.
Stage 2, now. Build all of this on a new branch from main (e68c2fb or later), with tests, in the pipeline's own code. For selected targets, extract out to 60", or to the current aperture where that is larger. Then report the branch, the selected-target list with reasons, the test results and a fresh price for the validation run, before running it. The validation follows the rule pre-registered in your stage-1 report, unchanged. Each sbatch needs Alistair's yes in this terminal (D59). Don't queue the branch until the validation has passed. The merge session will then merge it together with cert13, under one golden (D65).
Update your checklist line, and end with the rule-12 report.
