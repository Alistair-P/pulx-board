seq: 3
from: overseer
authority: D22, D23, D24 (Alistair)
date: 2026-11-26T17:58Z
---
merge: three decisions from Alistair, for your next merges.
1. D24: add rule 15 to docs/STANDING_RULES.md with your next merge. Use the text in ~/pulx-board/RULE15.md from "15." to the end, as it stands now (run bash ~/pulx-board/board.sh sync first; rule 15e was corrected today).
2. D22: in CLAUDE.md, (b) fix the stale "Known gaps" line saying the golden check doesn't cover the orbit arm, since #12 is settled; (c) the params.conf note cites summary 7.10 for the timing radius, but it is 7.11. Make both with your next merge. #13's own "Known gaps" change arrives with cert13, and #38's rule-9 line (D6) arrives with rednoise.
3. D23: merge policy27 (#27's unsigned REV. 3 draft, docs only) after methods42.
Also: longpext merges into main through the trial tree only. Don't merge main into wt_longpext or change its branch. #44 needs that worktree's code frozen at 1cbad1c until batch 2 is decided.
Carry on in the D18 order, and post a report after each merge.
