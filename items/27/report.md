seq: 1
state: needs-you
date: 2026-11-26T17:24Z
host: login7c
---
#27 (C5): received overseer instruction seq 1 (D13: change the (k) catch rate from 84-95.6% to 85.8-95.6%). NOT applied; needs Alistair.

Why it is not applied (rule 15c/15d, POLICY.md):
1. Alistair typed in this terminal on 25 Nov: "In the (k) entry, record the catch rate as 84-95.6% (counting lattice lines or forgeries)." Rule 15d: what Alistair types in the terminal overrides the board.
2. POLICY.md puts the detection policy (#27) under "Alistair only"; the overseer may not change its content.
3. The premise is incomplete. §15.228 (11) gives BOTH lower ends for counting lattice lines as units:
   - 85.8% = 0.025^(1/24), all 24 distinct lines (pooled run (9) + extension (10));
   - 84% = 0.025^(1/21), the extension's 21 lines alone.
   95.6% is the Clopper-Pearson lower bound counting the 82 forgeries. These are forgery (simulation) numbers, not real-data search output. So 84% is in the record. It is the more conservative lower end, the one Alistair chose.
Current state of the draft (101b486): the (k) table cell reads "84-95.6% at 95% confidence (counting lattice lines or forgeries)" and cites §15.228 (2)-(4), (11). O10's text spells out the split: 84% from the extension's 21 lines (85.8% over all 24), 95.6% counting each forgery, §15.228 (11). The overseer's other points match the draft already: REVIEW criteria wait for C1/C2, and O3, O4, O11, O14, O15 and O16 are open. No commit made; the queue entry still points at 101b486, the current head.
Rule 15e clarification (D14) read and noted.

Jobs: none.
Core-h: 0 this step; 0 since the item began.
Files: no quota reading taken.

SETTLED:
- #27: REV. 3 draft unchanged at 101b486 (15.233 (4)); queued docs only, after mcseed and p14a-calib.

NEEDS YOU:
1. (k) catch-rate wording: keep Alistair's 84-95.6% (as drafted, with both lattice-line lower ends spelled out in O10) or change it to 85.8-95.6%? Recommendation: keep 84-95.6%. It is the conservative end, it is in §15.228 (11), and Alistair chose it. Only Alistair can change it.
2. REVIEW criteria (O8): still waiting for C1 and C2 (agreed).

NEXT:
- On Alistair's answer, edit the one table cell if he asks, commit, and move the queue entry. Otherwise nothing until #19 freezes N (O5, O12) or C1-C4 report.
