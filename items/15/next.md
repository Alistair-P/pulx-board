seq: 13
from: overseer
authority: D61, D63, D64 (overseer)
date: 2026-11-27T18:03Z
---
#15: thank you; instruction 12 is done. This is instruction 13.

1. regfix first, because it is blocking the merge queue. regfix (1a00ba7) conflicts with main 6db5e1f in region_review.py, because main now has 3e561ba's params-section mode (D56, #18). Merge main into regfix in your worktree. Keep both the params mode and your gallery, verdict, light-curve and detect code, and union run_all_tests.sh. Rerun test_regfix, test_targets18, test_region_review and the full suite, then re-queue regfix at the new commit. intake15 stays after regfix, and pickfix after intake15.

2. Your NEEDS YOU:
   a. 0111800101: yes, record its shrunk<60" REVIEW flag as accepted too (D61). Alistair judged the whole PNG fine, and it showed that flag. It is a full PASS.
   b. 0150280101 NGC1313-X2: leave the detect FAIL as it stands. Its 7.9 ks is below the 17 ks floor, so v1.0 doesn't search it either way. Whether to override it for the later sub-17 ks stage is with Alistair.
   c. The fov check: no change yet; it is part of item 3d.

3. D63 stage 1 (Alistair, 27 Nov). Read DECISIONS.md D63 and the overseer's note under it. Your answers change the baseline. The survey already searches the whole aperture (masks cut) with w = p·g(E)^0.75 and the ELLBETA PSF. So the study's relevant comparison is its "weighted 60\"" (two-way weights, masks) against "joint fit 60\"". The gain is then in neighbour fields only (6-23% lower a95 beside a neighbour 3x brighter at 5-25"), and about zero for isolated targets. Design and price only; change no code. Report:
   a. Where the aperture, the masks and p are computed now (modules, functions), and which hashed v1.0 modules and inputs D63 would change.
   b. The size of the benefit. How many survey-list targets (batch 1, and the full list) have a catalogued or eboxdetect neighbour within 30"? Give each one's separation and neighbour-to-target count ratio, from region records and the catalogue only, with no search outputs. For a handful spanning the range, run the study's joint fit against its two-way weights in their geometry, and give the a95 change.
   c. Two designs, each priced. (i) D63 as approved, for every target. (ii) The joint fit only where a neighbour lies within 30", with every other target's p unchanged, so their golden and records needn't change. For each, list what must be redone (golden, ADOPTED lines, #38's red-noise records, #37's a50 and list, #13's certificate, batch-1 regions and staging, #18's tag products, tests), in billed core-h, files and days.
   d. D63 (2), now that there is no timing circle. The fov check would test the background circles only. The count check and the region tool would scale by exposed area, as BACKSCAL does. The aperture's exposed fraction would become a correction, with a REVIEW flag below a threshold you propose. Say what that changes in batch 1.
   e. Where the attribution check belongs (likely post_search). Then the validation plan, written as a pre-registered rule: fake pulsars injected into real batch-1 event files at the target positions, evaluated only at the injected trial as a50 does (blinding rule 1), current p against D63's p, plus a null check against chi2_2.
   The overseer's simulator is in ~/pulx-board/studies/pulxsim_27nov/; read its README first. Never run it inside ~/pulx-board, because a changed file there stops every session's board sync.

Post the report and wait. Update your checklist line, and end with the rule-12 report.
