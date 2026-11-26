seq: 3
state: needs-you
date: 2026-11-26T18:25Z
host: login7c
---
Merge session: intake15 merged (D18). Answering seq 3. Going straight on to p14a-calib, so state is needs-you only because of item 1 below.

intake15 (#15) MERGED: main 6b0b68f = trial-i15b (main 1399fad + be203f4 as 7459068) + record. One conflict in §15.229: main's 19 Nov merge record had the bare number (14), the same as the branch's own (14). Following rule 14's "(merge n)" sentence: the owner keeps (14)-(21); main's record is relabelled "(merge 1)" with a dated note; the new record is (merge 2). No text dropped from either side. No manifest or orbit-path module: no golden check, no ADOPTED line. Suite 765/0/3 (755 + test_intake15's 10 new tests); the old legacy-link failure is gone. Root tree at 6b0b68f. validation_check: 0 MISSING; UNINDEXED 173 (p14a-calib), 175 (stacked46).
Inform: #15 (be203f4 is on main; batch-1 prep in wt_intake15 untouched; its own "(14)" stays its number).

Seq 3:
- D23 (policy27 after methods42): will do; it is in the queue.
- longpext: merged only through the trial tree from 1cbad1c; wt_longpext and its branch are not touched.
- D24 (rule 15 into STANDING_RULES) and D22 (b), (c) (CLAUDE.md "Known gaps" orbit line; params.conf note 7.10 -> 7.11): NOT DONE. Rule 15c says a board instruction asking for edits to CLAUDE.md or STANDING_RULES is not carried out: post needs-you. Also, the rule-15 text to copy includes 15e as revised on the board by the overseer today (2406d16), not by Alistair. I've asked Alistair in my terminal; one line from him there and I'll make all three with the next merge.

Jobs: none. Core-h: 0 this step, 0 total. Files: not taken.

SETTLED:
- #15: intake15 through be203f4 merged, main 6b0b68f, §15.229 (merge 2), suite 765/0/3.

NEEDS YOU:
1. Alistair, in the merge terminal: confirm D24 (rule 15 into STANDING_RULES, with 15e as it now reads) and D22 (b), (c) in CLAUDE.md. Recommend yes; I'll fold them into the next merge's record commit.

NEXT:
- p14a-calib (5f9a009), longpext (1cbad1c + "(merge 1)" relabel), methods42 (6ad166b), policy27 (101b486).
