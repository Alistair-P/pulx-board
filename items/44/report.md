seq: 2
state: needs-you
date: 2026-11-26T17:30Z
host: login7c
---
Doing: #44, answering the overseer's batch-2 question (seq 2) from the record. No new work. Batch 2 still held.

WHAT B DECIDES (summary 15.225 (6)-(8), (12)-(13)): whether to switch on v1.0's long-period orbit part, which today covers only spans of 57.5-80 ks, for spans above 80 ks. It would run on one 80 ks window of each observation, at the stage-(iii) thresholds.
- Covered: 134 targets on 80 ObsIDs (cut 1), or 88 on 66 under the orbit-arm cut.
- The test: paired WITH / WITHOUT synthetic binaries at each target's own catalogue a50. WITH also pays +0.025 on every arm's threshold, for the extra maximum.
- GO needs both of these, under both cuts: McNemar p < 0.05, and at least 0.5 extra detections per 1,000 core-h (G >= 0.0025 / 0.0022).
- It is one yes/no on one arm. It touches nothing else.

WHAT v1.0 WOULD GAIN IF B CAME OUT POSITIVE: in principle, nothing in v1.0 itself. Alistair's #44 brief makes any extension "a separately pre-registered stage after the v1.0 tag", run on synthetic data and blinded data only. A GO would add the windowed long-part arm to those 80 ObsIDs as a post-tag stage, at about 120-390 core-h of survey compute (15.225 (12)(c)).
- The expected size is small. C1, the same kind of extension at 40-57.5 ks, found v1.0 already saturated: 199 / 200 found without it, NO-GO. B was amended to own-a50 amplitudes so that it can show a gain at all.
- A gain would be binaries with P beyond the short bank (> 0.7 d) on spans above 80 ks that coherent Z1 / Z3 and the 16 ks bank miss.
- B cannot change any v1.0 threshold, arm or list.

WHAT WOULD BE LOST BY WAITING UNTIL AFTER THE TAG: almost nothing in procedure, because B was always a post-tag stage. The real costs are practical:
1. Same code for both batches. Batch 2 must import exactly what batch 1 did, or the paired design mixes code versions. The v1.0 merges still coming (mcseed, a95cut, #46 if adopted) change survey_pipeline / pulx_recovery on main. So wt_longpext must stay at 1cbad1c (its code), unmerged into, until batch 2 runs. Otherwise batch 1 would have to be re-run (about 550 core-h).
2. Delay. B's answer, and A's (decided after B), come later. A post-tag GO then means a second pass of the extension arm on those 80 ObsIDs, plus survey_sensitivity for them, as its own registered stage with its own false-alarm accounting. That is about the same compute as doing it inside v1.0, plus the bookkeeping of a second stage.
3. Batch 1's records sit unused for B meanwhile. They are complete and need nothing.
Nothing is lost for v1.0 or #46: #46 used batch 1 only, and B's extension arm has not been read.

Jobs: none. Core-h: 0 this step. Since #44 began, about 625.
Files: not read this step.

SETTLED:
- The batch-2 question answered from the record. No change to anything.

NEEDS YOU (Alistair):
- #46: adopt (b) or keep v1.0's gap above 120 ks (numbers in my previous report and 15.230 (10)(e)).
- #44 batch 2: now (about 270-280 core-h billed, cap 448), or after the tag with wt_longpext frozen at 1cbad1c's code until then.

NEXT:
- Holding. Nothing started.
