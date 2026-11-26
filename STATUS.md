# PULX status

Updated: 26 Nov 2026 18:05, by the overseer (18:00 wake)

## Needs Alistair
1. **#46: include (d), or keep the gap?** (D32: (a), (b) and (c) are out.) (d) is a stacked arm at
   M = 4 on one 120 ks window, chosen blind from the flare monitor, using the existing 120 ks
   calibration (no new nulls). It can be budgeted under R0 (Z1 +1.71, Z3 +0.27) or as an add-on
   beside R1 (+0.71 on every arm). D29 scoring and the analytic check are running; the K_eff check
   (D31, 20–40 core-h) follows. Alistair leans towards including it. Proposed rule, to fix before
   the results: adopt (d) with the better-scoring budgeting, unless both budgetings' paired
   differences against no arm have 95% intervals entirely below zero.
2. **B (#44 batch 2)**: decide whether to switch on the long-period orbit part for spans above
   80 ks, on one 80 ks window each (134 targets on 80 ObsIDs). It's a post-tag stage by design and
   can't change v1.0. Batch 2 costs about 270–280 core-h billed (cap 448). A GO would add 120–390
   core-h of survey compute after the tag. C1, the same idea at 40–57.5 ks, found no gain.
   Options: run now, defer to after the tag (wt_longpext frozen until then), or drop. Overseer's
   view: defer, or let #44 propose a futility check on batch 1 first.
3. **Confirm in the merge terminal**: rule 15 into STANDING_RULES, with 15e as revised on the board
   on 26 Nov (D24), and the two CLAUDE.md fixes (D22 (b), (c)). The merge session rightly refused
   them from the board (rule 15c). One line from Alistair in its terminal is enough.
4. **#17**: review the recovery sections and batch regions. (Raised before 25 Nov.)
5. **#30**: the A1 candidate details. (Raised before 25 Nov.)
6. **#35**: your edit of the frame-alignment note. (Raised before 25 Nov.)
- Later: #13 will ask you to approve survey_pipeline.py's ADOPTED line after cert13's golden check.
- Optional now: the quota rise check (filemap.sh). The count is 144,000–146,000 and falling.

## For overseer
- #44's D29 results, for #46.

## Items

| ID | Item | Folder of its conversation | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree | high | active | intake15 merged (6b0b68f, suite 765/0/3); now p14a-calib; D22/D24 wait for Alistair's terminal line | 26 Nov 18:25 |
| 11 | #18 (multi-target), was #11 | wt_mt | medium | active | #18 step 1, target table (D25); wt_mcseed retired | 26 Nov 18:02 |
| 13 | certificate | wt_cert13 | high | waiting | v1.0 draft builder done (baa7e20, suite 751/0/5); waits for a95cut and #46 | 26 Nov 18:18 |
| 15 | survey intake | wt_intake15 | medium | running | downloads 3/14; job 12436014 (26 ObsIDs), 38–49 core-h | 26 Nov 17:50 |
| 25 | artefact battery rev3 | root tree | medium | waiting | p14a-calib (5f9a009) queued; needs a trial merge | 26 Nov 17:11 |
| 27 | detection policy draft | wt_policy27 | high | waiting | REV. 3 at 101b486, unchanged (D16); waits for C1–C4 | 26 Nov 17:30 |
| 37 | a95 cut | root tree | high | running | golden jobs 12436028/29/30 (D11) | 26 Nov 17:51 |
| 38 | red noise | wt_rednoise | high | active | rebuilding production red-noise records (D12, 38.2 sent 18:05) | 26 Nov 17:06 |
| 41 | quota and packing | root tree | medium | waiting | quota41b on main (818b683); deletion waits for Alistair | 26 Nov 17:12 |
| 42 | methods paper (#43, #45) | root tree | medium | active | "Weighted search statistic" done (4ff1e7c, 5 of 8); writing "The blind survey" | 26 Nov 17:30 |
| 44 | long-period part (#44, #46) | wt_longpext | medium | waiting | #46 scored; batch-2 answer posted; batch 2 held | 26 Nov 17:30 |
| 47 | β study | - | high | not started | no conversation found | - |

## Plans
The dispatcher may send only these steps, when their conditions are clearly met. Anything else
goes to "For overseer". A step that starts with "trigger:" is set off by another item's report.

- **merge**:
  - `merge.1`: after each merge it reports, send: "Carry on with the next entry in the D18 order."
    Also send the plan steps that merge triggers for other items.
  - Any failed suite, conflict it can't resolve, or golden difference: for overseer.
- **11** (now #18):
  - `11.1`: when it reports the target table done, with no new NEEDS YOU, hold until Alistair has
    answered Needs Alistair items 3 and 4. Then for overseer.
- **13**:
  - `13.1`: when it reports the build_cert.py draft committed, with no new NEEDS YOU, hold. It
    waits for a95cut and #46.
  - `13.2`: trigger: a merge report says a95cut AND #46's outcome are on main (or #46 is closed as
    "keep the gap"). Then for overseer, because the rebase and golden check plan needs checking.
- **15**:
  - `15.1`: while downloads, the memory test or the Slurm job are running, hold.
  - `15.2`: when the first Slurm job has finished with every ObsID ok, and the file count is under
    190,000, send: "Record batch 1's outcome in §15.229. Then price batch 2 (up to N = min(50,
    floor((195,000 − used)/500)) ObsIDs) the same way. If it needs XSA downloads, list them under
    NEEDS YOU and don't download them. If it is at most 50 core-h billed and its file projection
    stays under 194,000, submit the ObsIDs that need no download (D10), and report."
  - Any failed ObsID, a price over 50 core-h, or a file count over 190,000: for overseer.
- **25**:
  - `25.1`: hold idle reports while p14a-calib is queued.
  - `25.2`: trigger: a merge report says p14a-calib is on main. Send: "p14a-calib is on main.
    Check the merged-tree suite result in the merge record, set your checklist line to settled,
    post a done report and stop."
- **27**:
  - `27.1`: hold. It waits for C1–C4, or for #19 to freeze N.
- **37**:
  - `37.1`: while the golden jobs run, hold.
  - `37.2`: if both golden comparisons are bit-identical and a95cut is marked ready, hold.
    Anything else: for overseer.
  - `37.3`: trigger: #38 reports the production red-noise records rebuilt, AND a95cut and rednoise
    are both on main. Send: "D12: rerun a50 --all --thresholds applied and survey_pipeline --list
    on main, using #38's rebuilt records (folder in #38's report). Apply the near-cut rule (48
    injections within ±20% of 0.25); price it first, and ask if it is above 50 core-h billed.
    Report the list changes before rewriting the live list file."
- **38**:
  - `38.2`: sent 18:05 (rednoise is on main, 1399fad).
  - `38.3`: while the rebuild job runs, hold. When it reports the records rebuilt, with folder and
    hashes, hold. That report is one of 37.3's triggers.
  - A failed rebuild, or a cost above 10 core-h: for overseer.
- **41**:
  - `41.1`: hold idle reports while quota41b is queued.
  - `41.2`: done (D21, 18:05). #41 is settled once its addendum 26cca25 merges; hold its reports.
- **42**:
  - `42.1`: when it reports a subsection committed and the queue entry updated, with no new NEEDS YOU,
    send the next one from this list, in order: "Weighted search statistic", "The blind survey",
    "Sensitivity", "Validation". Say: "Go ahead with <subsection>, on methods42, docs only. Commit,
    update the queue entry, update your checklist line, post your report and wait."
  - When "Validation" is written: for overseer.
  - `42.2`: trigger: a merge report says a95cut is on main. Send: "a95cut is on main. Fill in the
    survey-list cut in 'The blind survey' (a95 < 0.25), commit, update the queue entry and report."
- **44**:
  - `44.1`: its answer on the Z1/Z3 table above 120 ks: for overseer.
  - `44.2`: hold anything else until Alistair decides #46 and batch 2. wt_longpext's code stays
    frozen at 1cbad1c until batch 2 is decided.
