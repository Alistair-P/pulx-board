# PULX status

Updated: 26 Nov 2026 17:10, by the overseer

## Needs Alistair
1. **#17**: review the recovery sections and batch regions. (Raised before 25 Nov.)
2. **#30**: the A1 candidate details. (Raised before 25 Nov.)
3. **#35**: your edit of the frame-alignment note. (Raised before 25 Nov.)
4. **Quota**: run filemap.sh v2 twice, an hour apart, and check tmp/, to find the rise of about
   29,000 files. (Raised 25 Nov. Less urgent: #38 read 144,058 on 26 Nov, down from about 162,000.)

## For overseer
- Every session's first board report: reconcile it with DECISIONS.md "Sent 25 Nov" and write its
  first plan.

## Items
Rows marked "(chat)" are as last known on 25 Nov, until that session's first board report.

| ID | Item | Worktree | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree (resumed) | high | active | merge queue; mcseed is on main (2513b12, per #38) | 25 Nov (chat) |
| 11 | MC seeding (mcseed), then #18 | wt_mcseed | medium | waiting | mcseed READY in the queue | 25 Nov (chat) |
| 13 | certificate | wt_cert13 | high | active | gate code and tests, unqueued | 25 Nov (chat) |
| 15 | survey intake | wt_intake15 | medium | running | batch 1 prep, 32 ObsIDs, login node | 25 Nov (chat) |
| 25 | artefact battery rev3 | wt_p14a | medium | waiting | p14a-calib (5f9a009) queued | 25 Nov (chat) |
| 27 | detection policy draft | wt_policy27 | high | active | DETECTION_POLICY_v1 REV. 3 | 25 Nov (chat) |
| 37 | a95 cut | wt_a95cut | high | waiting | a95cut golden check after mcseed | 25 Nov (chat) |
| 38 | red noise | wt_rednoise | high | waiting | queued at 8828681 (suite 748/0/3); holding (D7) | 26 Nov 17:06 (board, seq 1) |
| 41 | quota and packing | wt_q41 | medium | occasional | packing as batches finish | 25 Nov (chat) |
| 42 | methods paper (#43, #45) | wt_methods42 | medium | active | writing | 25 Nov (chat) |
| 44 | long-period part (#44, #46) | wt_longpext | medium | running | job 12424696, last 25 draws of batch 1 | 25 Nov (chat) |
| 47 | β study | wt_beta47 | high | not started | no conversation found on 26 Nov | - |

## Plans
Until the overseer writes an item's plan, the dispatcher sends nothing for it, and every report
goes to the overseer.

- **All items**: `ID.0`. Hold every report "for overseer".
- **38**:
  - `38.1`: while rednoise is queued and not yet on main, hold any `idle` or `waiting` report.
  - `38.2`: when a report says rednoise is on main, send nothing; for overseer (D7).
