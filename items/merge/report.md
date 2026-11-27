seq: 9
state: blocked
date: 2026-11-27T17:52Z
host: login7c
---
Merge session: regfix (#15) at 1a00ba7 does not merge cleanly onto main 6db5e1f: a CODE conflict in region_review.py. I aborted the trial merge and stopped; the queue order is held.

- What conflicts: regfix is off targets18 b75e098, before 3e561ba's region_review params-section mode (D56, #18), which is now on main. Three hunks in region_review.py: the usage docstring (params line vs gallery text), the block after draw() (params_section / result_from_section / params_review vs gallery / verdict / light-curve code), and the CLI (the "params" subparser and handler vs the "gallery" subparser and handler, both before the same parse_args). Also run_all_tests.sh (a test list, which I could union).
- Both sides look additive, but this is code, and my rules cover only summary sections, test lists, README rows and figures. So it goes back to the owner.
- Proposed fix: #15 merges main 6db5e1f into regfix in its worktree, resolves region_review.py (keeping both the params mode and the gallery/verdict/light-curve), reruns test_regfix, test_targets18, test_region_review and the suite, and re-queues regfix at the new commit.
- intake15's entry says merge AFTER regfix (run_regions calls stack_name), so it waits too.
- methods42 (5264663, docs only) and testshim-tmp (#41, daef6ba) do not depend on regfix. May I take them now, ahead of regfix and intake15? That reorders within the agreed order, so I'm asking first.
- Nothing changed on main since 6db5e1f. Trial branch trial-rf is left at main, unused.

Jobs: none. Core-h: 0. Files: not taken.

SETTLED:
- none new (targets18 reported earlier, main 6db5e1f).

NEEDS YOU:
- Overseer: (a) send regfix back to #15 to merge main and re-queue; (b) say whether I may merge methods42 and testshim-tmp before regfix and intake15.

NEXT:
- On (b) yes: methods42, then testshim-tmp. Then regfix (re-queued), then intake15.
