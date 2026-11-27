seq: 9
state: needs-you
date: 2026-11-27T15:10Z
host: login7c
---
#15 (board seq 9): done. Every review PNG has the new light-curve panel, and all 51 gallery PNGs are redrawn (#18's 4 included). G and H were already done in seq 8 (report d); their results are repeated below. Only the two reruns remain, waiting for Alistair's yes in the terminal.

1. **B, light-curve panel (regfix ba93f94):**
   - Four curves, each with its own colour and line style and a legend:
     - the source aperture, 0.5–7 keV, masks removed (orange, solid);
     - background A (green, dashed) and background B (purple, dotted), each scaled by area to the aperture;
     - the full-field 10–12 keV monitor, PATTERN 0, the tool's own flare-rate selection (blue, dash-dot, right axis).
   - Flares are shaded where the 100 s monitor rate is above the tool's own threshold, which is drawn as a line.
   - Both axes are log scale, because the backgrounds sit 10–100 times below the source.
   - **Time axis:** every curve comes from the barycentred pn_clean.fits. The tool's flare_rate.fits uses the raw event times, which differ by up to about 500 s, so the flares would sit in the wrong place.
   - regions.png's per-CCD panel is unchanged.
   - **Known artefact:** a bin that only partly overlaps a good-time interval reads low (e.g. 0830191401 at 79 ks).
   - Tests: test_regfix 9/0/0, including a synthetic event file checking the rates, the area scaling and one flare span. test_region_review 7/0/0, test_targets18 10/0/0.
   - **Redrawn:** all 51 gallery PNGs in 2.2 min, no errors.
2. **G (seq 8, regfix d0e20bf):** the verdict banner and index.tsv read FAIL, REVIEW (red, with the flag count and names) or PASS, sorted worst first. The five flags are read from the region tool's own review list. No inclusion rule was changed.
   - **Gallery now:** 9 FAIL, 6 REVIEW, 36 PASS.
   - 0400560301 reads "REVIEW: 5 flags".
3. **H, counts over batch 1** (49 targets: 47 bare, 2 tags):

   | flag | targets |
   |---|---|
   | not_detected | 2 |
   | outshines | 4 |
   | contamination | 3 |
   | diffuse>100% | 7 |
   | shrunk<60" | 7 |
   | any of the five | 8 |
   | not_detected AND outshines | 2 |

   The two that are both undetected and outshone are 0400560301 and 0674210601; both carry all five flags.
4. **Reruns, waiting for Alistair's yes in the terminal** (exact commands in report c): delete the failed files and run sbatch, for 0884030101 and for 0150280101.

Recorded in §15.229 (28)–(29) (intake15 9f11bbb).

Jobs: none. Core-h: 0 (login only). Files: 175,237.

SETTLED:
- B: the light-curve panel is in review.png, and all 51 gallery PNGs are redrawn.
- G: the PNGs and index.tsv show FAIL, REVIEW or PASS.
- H: 8 of the 49 targets carry at least one flag; 2 are both undetected and outshone.

NEEDS YOU:
1. Alistair: should any of the five flags become a hard QA rule?
2. Alistair, in the terminal: yes or no to the two deletions and two sbatch commands (report c).

NEXT:
- After each rerun: check the chosen exposure and barycentring, then run its regions and PNG, then mark pickfix ready.
- Apply any QA rule Alistair sets.
