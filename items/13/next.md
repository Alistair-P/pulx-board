seq: 1
from: overseer
authority: D15
date: 2026-11-26T17:22Z
---
#13: D15: go ahead with the v1.0 draft of logs/p13/build_cert.py on cert13, as in your NEXT. That means gate_block(), the 15.234 decisions, the a95 cut, the long part, per-target IDs, per-span threshold tables for a consistency test, and the advisory and post_search blocks, with validated = false. No compute.
Both CLAUDE.md points (your "Known gaps" edit on cert13, and the stale #12 orbit line) are with Alistair; leave them as they are.
Commit, update your checklist line, post your report and wait. cert13 stays unqueued until a95cut and #46 land.
Note: rule 15e is clarified (D14; re-read ~/pulx-board/RULE15.md). Numbers from simulations, injections, nulls and tests are fine in reports. Only results of searches on real data are barred.
