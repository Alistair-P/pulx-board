seq: 13
state: needs-you
date: 2026-11-27T18:40Z
host: login7c
---
#15 (board seq 13): regfix is re-queued with main merged in, 0111800101 is a full PASS, and D63 stage 1 (design and price only) is written up. Recommendation: the joint fit only in neighbour fields, about 40-100 billed core-h, against about 210-300 for every target.

1. **regfix merged with main 6db5e1f (2052b59, queued at 4a2f274; merges cleanly with main a85b293):**
   - Kept #18's params-section mode (D56) and my gallery, verdict, light-curve and detect code. run_all_tests.sh is the union.
   - Two interaction fixes:
     - The detect check is skipped in params mode, which has no region-tool detection.
     - The gallery also indexes stats/region_review_params, linked as `<obsid>_<name>_params.png`.
   - Tests: test_regfix 15/0/0, test_targets18 11/0/0, test_region_review 7/0/0, full suite ALL SUITES PASS.
   - Re-queued. Order: regfix → intake15 → pickfix.
2. **Decisions recorded:**
   - 0111800101: shrunk<60" accepted (D61) → PASS.
   - 0150280101: the detect FAIL stands.
   - fov: no change yet.
3. **D63 stage 1.** Full report: `/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_intake15/logs/intake15/d63_stage1_20261127.md` (per-target tables in stats/intake15/).
   - **a. Where things are computed now:**
     - Aperture and mask cuts: preprocess.sh. p: radial_weighting.build_classifier_model / build_pulse_arrays_from_events (two-way, ELLBETA, masks taken out of the footprint).
     - None of these is in MANIFEST.sha256, so no ADOPTED line is needed.
     - But radial_weighting, inject_recover, run_template_pipeline and pipeline_config are hashed by the orbit and window golden and by #13's certificate. 8 golden outputs move.
   - **b. Neighbour census:**
     - Catalogue: 56 of 127 targets (252 of 571 rows) have a neighbour within 30", mostly faint, at 20-30". 13 targets have one ≥ 0.3× the target. **Only 2 targets have one ≥ 1× within 15".**
     - Batch 1 eboxdetect: 4 of 51.
     - On 7 real geometries the joint fit lowers a95 against two-way 60" weights by 25% and 21% (neighbours 8.8× and 6.25× at 22"), 12%, 8%, 6% and 1.5%, and 0% (a faint neighbour at 2.9"). It matches the oracle each time.
   - **c. Two designs:**
     - (i) every target: about 210-300 billed core-h, 3-5 days. Golden 26.8, η pass about 171, red-noise 2.6, stage A/gate 8.2, plus preprocess -f for masked fields.
     - (ii) neighbour fields only, with a threshold of ≥ 0.1× within 30": about 40-100 core-h, 2-3 days. The golden is still needed.
     - Risk for (ii): the catalogue blends M82 X-1 into X-2, so selection needs eboxdetect plus known pairs.
     - Landing D63 before the intake list's sensitivity pass removes most of (i)'s extra cost.
   - **d. QA rules (fov on background circles only, exposed areas, aperture correction with REVIEW below 90% exposed):** in batch 1, fov FAILs go 6 → 0 and those same 6 become REVIEW. Count FAILs stay 3; background scaling changes nothing (all background circles are fully exposed).
   - **e. Attribution check:** a new post_search.py, outside the manifest, run only on policy-passing candidates. It folds the target's and the neighbour's weighted photons at the candidate's (f, ḟ). The validation rule is pre-registered in the report:
     - injections into real batch-1 pn_clean at the target, evaluated only at the injected trial: neighbour fields with ratio ≥ 0.1, plus 10 isolated controls;
     - pass: controls change ±2%, bright-neighbour fields improve ≥ 5% (median), none worse by > 5%, leakage falls;
     - null: jitter_null against χ²₂;
     - about 25-50 core-h.

Recorded in §15.229 (33) (intake15 f49d864; corrects the e4bcd58 in the first post of this report).

Jobs: none. Core-h: 0 (login only). Files: 171598.

SETTLED:
- regfix is merged with main and re-queued; 0111800101 is a full PASS.
- D63 stage 1 is designed and priced, with no code changed.

NEEDS YOU:
1. Alistair: D63 scope: (i) every target, about 210-300 core-h, or (ii) neighbour fields with ≥ 0.1× within 30", about 40-100 core-h?
2. D63 (2): the fov and area rules with REVIEW below 90% aperture exposure?

NEXT:
- On a scope answer: build D63 on a branch, then run the pre-registered injection validation, priced again first.
