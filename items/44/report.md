seq: 14
state: needs-you
date: 2026-11-27T17:53Z
host: login7c
---
#44/#46, seq 14, interim report: item 1 is done. For item 2, the rule is committed and the pilot is ready; it is waiting for Alistair's yes in the terminal (D59).

1. DONE: branch figidx46 off main 57974c9 (docs only, worktree wt_figidx46, commit 46f1efd) adds README rows for figures 175, 176 and 177. validation_check: 181 indexed, 181 PNGs, 0 missing, 0 unindexed. Queued (`checklist.py queue add figidx46 46`).
   - NOTE for the merge session: the summary sections these rows cite are on branch longpext only, not on main: 15.230 (10)(e)-(11) and 15.225 (15)-(16). So are the @fig functions for 175-177 in validation_plots.py and the scoring scripts. That is 15 commits after 1cbad1c, with no pipeline code. Should longpext be queued too?
2. IN PROGRESS: the confirming simulation (D39), on main's merged code. Branch confirm46d off main 57974c9, in a new worktree.
   - Rule and design written into summary 15.236 (6) and committed (e6c9cb5) BEFORE any draw. It is 15.230 (11)(d)'s design:
     - 64 binaries above 120 ks, each at m = 1.5 / 2.0 / 3.0 x a50, plus 32 wander draws at 3 rad = 224 searches.
     - Arms: Z1 on the injected octave, the v1.0 orbit arm, and the (d) window arm as run_one runs it.
     - Allocations: no arm (R1), add-on (R1W as adopted) and R0.
     - (d) PAYS at m = 2.0, separately per allocation, iff d-only > no-arm-only and the exact two-sided McNemar p < 0.05.
     - Two deviations, both recorded: (i) two-sided, the stricter reading; (ii) the add-on leaves the orbit share unchanged, as main implements it (step 1's post-hoc add-on had raised the orbit arm too).
   - Pilot: 8 binary draws covering octave x span bin x m 1.5 / 3.0. 1 task x 4 CPUs, cap 1:30 = 6 core-h; expected ~2-4 billed. Hashes in logs/stacked46d/sha256_confirm46d_pilot.txt.
   - NOT SUBMITTED. The exact sbatch, directory, resources and billed core-h are shown to Alistair in the terminal now. It will be submitted only on his yes.

Jobs: none.
Core-h: 0 this step.
Files: +4.
OPEN: Alistair's yes for the pilot. Then reprice; if the full run is within 110 core-h billed, ask him in the terminal for it.
