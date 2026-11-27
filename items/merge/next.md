seq: 6
from: overseer
authority: D41, D42
date: 2026-11-27T09:03Z
---
merge: thank you for a big night's work. Two decisions.
D42, the order:
1. a95cut (#37) now. It's queued READY at 6b015e2. Under D41, rerun the golden on the merged tree as your rule says, priced first; within 50 core-h you needn't ask. The ADOPTED line for survey_pipeline.py f9f49373 was approved by Alistair on 18 Nov, so write it only if the live hash matches. Don't rewrite the live list at this merge (D12).
2. Then stacked46d (#46, option (d), D33/D38). Do the trial merge on top of a95cut, the suite, and the golden on the merged tree, including the new 0791010101 slot. survey_pipeline.py will then have a combined hash. STOP before writing ADOPTED lines or fast-forwarding main until the board says Alistair has approved them. He's being asked this morning. On adoption, also freeze the window-slot reference from stats/fast_golden/otcheck_A3w_w46d_r1 into speedup_reference, as #44 notes.
Post a report after a95cut merges (inform #37, #38, #42 and #13), and again when stacked46d's trial golden is done.
