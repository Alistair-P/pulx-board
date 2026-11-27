seq: 6
state: idle
date: 2026-11-27T16:14Z
host: login7c
---
#41 (file quota): retired the 11 worktrees on Alistair's yes. The tmp/ clean-up is approved and waits for testshim-tmp to merge.

Alistair, in the #41 terminal (rule 15d): "Yes go ahead". That answers both open items: the retirement of the 9 worktrees + wt_p14a + wt_regrev, and the tmp/tmp* clean-up.

DONE: wt_p14a, wt_regrev, wt_a95, wt_fig164, wt_figs8, wt_longp60, wt_longpv1, wt_lpfig, wt_m82decay, wt_methods, wt_valstore.
- Re-checked first: no process, no job, no tracked change, all merged.
- Each: link_data.sh --remove, then git worktree remove without --force. wt_longpv1 predates link_data.sh, so I used the root tree's copy there; its 10 untracked entries were all links into the root tree.
- All 11 branches kept.
- Quota 174,274 -> 157,359 (about 16,300 of it from these worktrees, the rest other sessions).
- Recorded as a dated addendum in 15.223 (16), commit 84b86f9 on testshim-tmp (queue line refreshed).

WAITING: clearing tmp/tmp* folders older than 1 h (about 37,000) runs as soon as testshim-tmp is on main, per seq 5/6. I check main each time the board wait cycles.

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began.
Files: lfs quota 157,359 / 200,000 (27 Nov, after the retirement).

SETTLED:
- #41: 11 idle merged worktrees retired, branches kept, quota 157,359 (15.223 (16) addendum, 84b86f9).

NEEDS YOU:
- none.

NEXT:
- When testshim-tmp merges: clear tmp/tmp* older than 1 h and my 21-inode suite_tmpdir, report the files freed, and update the checklist. Nothing has been started.
