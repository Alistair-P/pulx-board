seq: 1
from: overseer
authority: D9, D10
date: 2026-11-26T17:22Z
---
#15: D9 and D10.
1. Download batch 1's 14 ODFs from the XSA, one at a time on the login node, as Alistair approved on 25 Nov. Check each tarball reads back and is complete against its summary file list. Record its source, date and sha256 in INTAKE.md.
2. Write the Slurm seed + prep job, 1 CPU per ObsID. Measure memory on one ObsID first and set --mem from that (rule 7: memory counts towards billed CPUs).
3. Price the first job: batch 1's 25 unprepped ObsIDs plus the 14 downloads, in billed core-h and files, from batch 1's measured times. Remove the stale ODF_tarballs/0742490101.tar.gz.part before the job seeds that ObsID.
4. If the job is at most 50 core-h billed and its file projection stays under 194,000, submit it (D10). Otherwise post needs-you with the price.
Record batch 1's state in §15.229 and update your checklist line. Post a report when the job is submitted, and again when it finishes.
Note: rule 15e is clarified (D14; re-read ~/pulx-board/RULE15.md). Numbers from simulations, injections, nulls and tests are fine in reports. Only results of searches on real data are barred.
