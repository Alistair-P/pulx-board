seq: 3
state: running
date: 2026-11-26T21:33Z
host: login7c
---
Merge session: p14a-calib merged (D18), with Alistair's D24 and D22 folded in. Going straight on to longpext.

p14a-calib (#25) third part MERGED: main 15285f7 = trial-p14a3 (main 6b0b68f + 5f9a009 as 2b03da2) + record. Conflicts textual only: run_all_tests.sh (union, + test_p14a_lattice) and validation/README.md (rows 173 and 174 both kept). No manifest or orbit-path module: no golden check, no ADOPTED line. Suite 772/0/3 (765 + 7); test_frame_raw_equiv passes again. Record §15.228 (merge 1). Root tree at 15285f7. validation_check: 0 MISSING; UNINDEXED 175, 176 (stacked46; rows not on main yet).

Alistair confirmed D24 and D22 in the merge terminal (rule 15d), so they're in the same commit:
- rule 15 is in docs/STANDING_RULES.md, taken from RULE15.md at board commit 7b6aa1a with the revised 15e (copy: logs/mergeq/RULE15_as_adopted_20261126.md in the root tree);
- CLAUDE.md: the "Known gaps" line drops the orbit-arm golden gap (dated pointer: #12 settled, §15.213); the params.conf note cites summary 7.11.
Inform: #25 (third part on main); all sessions (rule 15 is now in STANDING_RULES on main; worktrees see it after merging main).

Jobs: none. Core-h: 0 this step, 0 total. Files: not taken.

SETTLED:
- #25: p14a-calib 5f9a009 merged, main 15285f7, §15.228 (merge 1), suite 772/0/3.
- D24, D22 (b), (c): done in 15285f7.

NEEDS YOU:
- none.

NEXT:
- longpext (1cbad1c, with the "(merge 1)" relabel in §15.225; wt_longpext untouched), methods42 (6ad166b), policy27 (101b486).
