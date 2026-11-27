seq: 8
state: needs-you
date: 2026-11-27T15:05Z
host: login7c
---
#15 (board seq 8): G and H are done. Every review PNG now says FAIL, REVIEW or PASS, and 0400560301 shows "REVIEW: 5 flags" in red. A, C, D, E and F were already done in seq 7. Still open: the flare panel (B, my question in report c) and both reruns, which need Alistair's yes here.

1. **G (regfix d0e20bf, queued after targets18):**
   - The verdict is FAIL if a check fails, else REVIEW if any of the five flags is set, else PASS. It shows as a red or green banner at the top of the PNG.
   - The five flags come from the region tool's own REVIEW list, at its own thresholds:
     - not_detected;
     - outshines;
     - contamination (above 5% at every radius);
     - diffuse>100%;
     - shrunk<60".
   - index.tsv gains verdict and qa_flags columns and is sorted worst first.
   - Display only: no inclusion rule changed.
   - Tests: test_regfix 8/0/0, test_region_review 7/0/0, test_targets18 10/0/0.
   - Redrawn: batch 1's 47 PNGs. The gallery has 51 PNGs: 9 FAIL, 6 REVIEW, 36 PASS.
2. **H, counts over batch 1's targets** (47 ObsIDs, 49 targets: 47 bare and 2 tags, both in 0830191401):

   | flag | targets |
   |---|---|
   | not_detected | 2 |
   | outshines | 4 |
   | contamination | 3 |
   | diffuse>100% | 7 |
   | shrunk<60" | 7 |
   | any of the five | 8 |
   | not_detected AND outshines | 2 |

   - **Both undetected and outshone:** 0400560301 NGC4258-J121903.0+471722 and 0674210601 NGC0224-J004247.1+411615. Both carry all five flags.
   - **The other 6:**
     - 0830191401 M51ULX7: 4 flags, everything except not_detected.
     - 0670950101 NGC0891-J022233.5+422027: outshines, diffuse, shrunk.
     - 0504780101: diffuse, shrunk.
     - 0111800101: shrunk.
     - The two 0830191401 tags: diffuse; and diffuse + shrunk.
3. **For #18:** each of the two 0830191401 tags has two region folders, the old D-id name and the D47 J-name, with the same target ID. Both appear in the gallery.
4. **Still waiting:**
   - B, the flare panel: it plots per-CCD curves, not source, background or monitor curves. My question is in report c.
   - The reruns for 0884030101 and 0150280101 (commands in report c): each deletion and each sbatch needs Alistair's own yes in the terminal.

Recorded in §15.229 (28) (intake15 8782021).

Jobs: none. Core-h: 0 (login only). Files: 174,864.

SETTLED:
- G: the PNGs and index.tsv show FAIL, REVIEW or PASS from the five QA flags.
- H: 8 of the 49 batch 1 targets carry at least one flag; 2 are both undetected and outshone.

NEEDS YOU:
1. Alistair: should any of the five flags become a hard QA rule? (counts above)
2. B: recolour the per-CCD panel in regions.png, add a new source/background/monitor panel to review.png, or drop it? (report c)
3. Alistair, in the terminal: yes or no to the two deletions and two sbatch commands (report c).

NEXT:
- Apply whatever QA rule Alistair sets, and the panel fix once B is answered.
- After each rerun: check the chosen exposure and barycentring, then run its regions and PNG, then mark pickfix ready.
