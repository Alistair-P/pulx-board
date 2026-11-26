seq: 0
state: done
date: 2026-11-26T17:13Z
host: login7c
---
#27 (C5, detection policy): applied Alistair's 25 Nov REV. 3 instruction to the draft. Docs only; nothing signed.

Instructions from Alistair (typed in this terminal, 25 Nov) and where each stands:
1. Collate the #27 decisions into docs/DETECTION_POLICY_v1.md, decide nothing, queue as docs only: DONE (a5b7fc2, 15.233 (1)-(3)).
2. Recommendations 1-9 and 11 provisional for REV. 3, item 10 open, (k) catch rate 84-95.6%, nothing signed until
   C1-C4 are in: DONE (101b486, 15.233 (4)).
   - PROVISIONAL (marked in the draft, not in force):
     - O1: N = the IN targets frozen at the v1.0 tag, as a fixed number.
     - O2: blind-part recovery targets count in N.
     - O5 and O12: recompute B5's R and the known-pulsar check at that N before signing.
     - O6: no Z3 or orbit margin; row 5a's sigma quoted beside orbit Tier-1 calls.
     - O7 and O9: a halves failure and a (d) failure both go to REVIEW.
     - O8: REVIEW = Tier 1 withheld pending a written review against criteria fixed at signing.
     - O10: a (k) failure is a veto, with the candidate still listed.
     - O13: sidelobe k = 10, max(k, LONGP_TOL) for long-part candidates.
     - O17: a C1 failure makes the cell Tier-1 ineligible, kept in Tier 2.
   - OPEN until signing: O3, O4, O11, O14, O15, O16.
   - (k) entry: catch rate 84-95.6% at 95% confidence (counting lattice lines or forgeries).
   - Signature section: not signed until C1-C4 (#23-#26) are in; C4 is optional, so "in" = done or declared not done.
   - Item 11: the queue line now says merge policy27 AFTER mcseed and p14a-calib.
3. Session renamed "27": noted.
No board instruction for 27 had arrived; the wait is running.

Jobs: none.
Core-h: 0 this step; 0 since the item began.
Files: no quota reading taken (no data written; backups in archive/, diffs in logs/policy27/).

SETTLED:
- #27: REV. 3 draft with the provisional choices marked; still unsigned, waiting on C1-C4 (15.233 (4), 101b486; queued docs only, after mcseed and p14a-calib).

NEEDS YOU:
1. The REVIEW criteria list (needed by provisional O8) must be written before signing. Recommendation: draft it here once C1 and C2 have defined what their outputs flag, so it can cite them.
2. O3, O4, O11, O14, O15, O16 stay open until signing, as instructed. Recommendation: none until C1-C4 report.

NEXT:
- Once #19 freezes N: recompute B5's R and the 15.160 (3) known-pulsar check by the existing rules, as a summary addendum (O5, O12).
- After C1-C4 are in: REV. 4 for signing, with the REVIEW criteria and the remaining open items.
