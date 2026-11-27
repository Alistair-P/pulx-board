seq: 12
state: needs-you
date: 2026-11-27T17:57Z
host: login7c
---
#15 (board seq 12): D61 and D62 are done and item 4 is answered. D62 changed 3 batch 1 verdicts: the 2 the board expected, plus NGC 1313 X-2 in 0150280101, which eboxdetect does not detect. Already done before seq 12 and not redone: item 1 (D60, report f) and item 5 (both reruns, verified, report g).

1. **D62 (regfix 61eeb96):** a new check, "detect", fails when eboxdetect finds no source within 10"; Alistair can override it per observation. "outshines" stays a REVIEW flag and never fails. Each has a test.
   - Batch 1 redrawn (51 targets); 3 verdicts changed:
     - 0400560301: REVIEW → FAIL (detect); still held under D60.
     - 0674210601: FAIL (counts) → FAIL (detect + counts).
     - **Not expected: 0150280101 NGC1313-X2**, the S001 rerun (7.9 ks): REVIEW → FAIL (detect). eboxdetect has no source within 10" of X-2 in that exposure.
2. **D61:** the review tool had no way to record verdicts, only region overrides, so I added one: `data/region_verdicts.tsv` and the command `region_review.py verdict OBSID NAME SCOPE ACTION --reason`. A row can pass a check, accept the REVIEW flags, or confirm the verdict. It is display only; staging does not read it.
   - **0111800101:** fov passed by hand. Its 20" circle is 100% exposed, against 90% required (the 40" aperture is 81%). It still shows REVIEW for "aperture shrunk below 60"", which D61 did not cover.
   - **0670950101:** REVIEW flags accepted, so it is now PASS.
   - **Confirmed as they stand:** 0504780101 FAIL, 0674210601 FAIL, 0763120401 PASS.
   - Gallery: 9 FAIL, 4 REVIEW, 37 PASS, 1 HELD, 3 UNCHECKED (another session's X-2 PNGs).
   - Tests: test_regfix 14/0/0, test_region_review 7/0/0, test_targets18 10/0/0.
3. **Item 4.** Per-target numbers: `/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_intake15/stats/intake15/d61_q3_per_source_20261127.tsv`.
   - **a.**
     - Events searched: timing_radius is empty for every section, so both searches take the whole aperture (masks cut); only the weighted search applies weights. **The 20" circle on the PNGs is just drawn; no search uses it.**
     - PSF: the weights use an off-axis and energy-dependent PSF (the calibration file's ELLBETA model).
     - Energy weighting: yes, through the source and background spectra, and through g(E)^0.75 in the survey.
     - **1 batch 1 target is > 10' off-axis:** 0763120401, 13.8', 100" aperture. 63% of its source counts fall inside 20" (PSF model), 67% measured.
   - **b.**
     - The fov check tests the aperture and every background A and B circle, not the 20" circle.
     - The count check and the region tool scale the background by geometric area, not exposed area. The pipeline's own spectra use SAS's exposed-area scaling (BACKSCAL).
     - **With the fov check on the 20" circle and the background circles instead, all 6 fov FAILs pass and none newly fail.**
   - **c. 0670950101:** "outshines" comes from a PSF-model comparison, not the image. A neighbour 24.8" away (5,723 counts, against the ULX's 46,081) out-brightens the ULX's model profile up to 8" from itself. That is past the cap (24.8" − 20" core − 5" ≈ 0"), so the flag trips even though the ULX dominates its own core. Its 10" mask overlaps the 20" circle. Masked photons are cut and the weights renormalise the PSF, so the loss is 1.0% of the ULX counts inside 20" (2.7% inside the 45" aperture).
   - **d. 0674210601:** the tool's count is a measurement, not a catalogue rate. With the target undetected, it is counts in 20" minus a 60–150" annulus, divided by the 20" enclosed-energy fraction: 5,104 inside the flare GTI, times 2.37 for the full exposure = 12,114. The review tool's net of 858 subtracts background A, which sits on the same diffuse emission as the target; the annulus background is much lower.

Recorded in §15.229 (32) (intake15 e4bcd58).

Jobs: none since 12448507/8. Core-h: 0 (login only). Files: 164,367.

SETTLED:
- D62's detect check is in, and D61's verdicts are recorded and drawn.
- Item 4 is answered, with per-target numbers on COSMA.

NEEDS YOU:
1. 0150280101 NGC1313-X2 now FAILs "detect" (eboxdetect finds nothing within 10" in 7.9 ks). Override, or leave it out?
2. 0111800101: is its remaining "shrunk<60"" REVIEW flag accepted too, i.e. a full PASS?
3. Should the fov check move to the 20" circle and the background circles, given no search uses a 20" circle?

NEXT:
- Record Alistair's answers with `region_review.py verdict`, and change the fov check if told.
- Merge order: targets18 → regfix → intake15 → pickfix.
