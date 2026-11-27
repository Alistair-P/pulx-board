seq: 2
state: idle
date: 2026-11-27T09:05Z
host: login7c
---
#37 (a95 inclusion cut): instruction seq 2 (D41) acknowledged. No golden rerun from me; I am waiting on the board for the D12 rerun.

- D41 understood: the merge session reruns the golden on the exact merged tree when it merges a95cut, priced first. My check (15.226 (18): coherent 19/19 bit-identical, orbit 4/4 identical to mcseed's run) stands as the prediction.
- a95cut is still queued READY at 6b015e2, with main 6b0b68f merged in. Main has since moved to 6cd77d3 (quota41b addendum, regionreview). I have not merged that in: the merge session builds its own trial, and the branch is not touched while it is queued. If the merge session wants main merged into a95cut first, the board can say so.
- Not changed: the live list file (84). The ADOPTED line for survey_pipeline.py f9f49373 is the merge session's to write.

Jobs: none.
Core-h: 0 this step. Since the item began: 45.5 + 3.4 + 11.3 billed for the a95 work.
Files: no reading taken.

SETTLED:
- #37 seq 2: D41 acknowledged, no rerun. a95cut stays READY at 6b015e2. Checklist line updated.

NEEDS YOU:
- Nothing.

NEXT:
- On the board's instruction, once a95cut is on main and #38 has rebuilt the production red records (D12): rerun a50 --all --thresholds applied and --list from a fresh worktree off main, and report before rewriting logs/survey_full/obsids_longest_first.txt.
