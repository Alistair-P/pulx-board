seq: 9
state: needs-you
date: 2026-11-27T11:41Z
host: login7c
---
#44, seq 9 (D36), report: I ran B's futility check on batch 1. B CLOSES AS NO-GO without batch 2.

Steps:
1. DONE: the rule went into summary 15.225 (15), committed with its scorer logs/longpext/futility_B.py (b500aa9) BEFORE any B record was read.
   - The detection, the McNemar test, the cost bars (N 80 / 66 ObsIDs, C 392.5 / 286.3 core-h) and the both-cuts requirement are all unchanged from the pre-registration.
   - "Most favourable batch 2": WITH-only draws at the one-sided 95% Clopper-Pearson upper bound of batch 1's rate, and WITHOUT-only at the 95% lower bound, rounded in B's favour.
   - Batch 2's size per cut comes from the seeds alone: 107 / 64 binary draws.
2. DONE: scored B's arm on batch 1 (synthetic injections only, on the login node, no new runs).
   - Cut a95: 93 binaries; detected 16.1% without the extension and 16.1% with it.
     - 0 WITH-only, 0 WITHOUT-only: no draw changes either way. B's extension arm alone crosses its threshold on 0 of 93.
     - Isolated controls: 7, 0 discordant.
     - Best case: batch 2 adds 4 WITH-only and 0 against, giving 4 vs 0 of 200, McNemar p 0.0625. The cost bar would pass, but p does not, so GO is unreachable.
   - Cut a95_orb: 63 binaries; 17.5% / 17.5%.
     - 0 / 0 discordant, extension alone 0 of 63; controls 5, 0 discordant.
     - Best case 3 vs 0 of 127, p 0.125. GO unreachable.
   - A GO would need at least 5 WITH-only draws in batch 2 with none against under each cut. Batch 1 gave 0 of 93.
   - VERDICT: NO-GO (futility). Batch 2 (~270-280 core-h) is not run. v1.0 keeps the 57.5-80 ks window.
3. Checklist #44 updated. wt_longpext's code is frozen at 1cbad1c; only summary.txt and logs/ scripts were committed since.

Jobs: none.
Core-h: this step 0, login node only (seconds). Since the item began: batch 1 552.6, plus the earlier pilot and C1 runs recorded in 15.225.
Files: no quota reading taken (+1 json, +1 script).

SETTLED: B is NO-GO on futility (rule fixed first, b500aa9; result 15.225 (15)(d), 33cc0fe; stats/longpext/futility_B.json). C1 NO-GO, C2 closed.
NEEDS ALISTAIR:
- Option A, the long part on the full span. It was never measured, because its bracket on B's draws is 416-991 core-h and was waiting on B. Close A, or price a bracket on batch 1's draws alone?
- No validation figure for this result yet (CLAUDE.md asks for one per result). I can add it on request: login node, minutes.
- #46: stacked46d is still queued ahead of #13, waiting on the ADOPTED line and on the confirming simulation decision.
