seq: 10
state: idle
date: 2026-11-27T21:23Z
host: login7c
---
Merge session: pickfix (#15) and the testshim-tmp addendum (#41) merged. The queue is now empty of ready entries: idle.

- pickfix ef7f106 -> main 30f1961 (trial ba58ceb). No conflicts; pick_pn_events.py is not a manifest or orbit-path module and is not on a golden path. Suite 829/0/3 (test_pick_pn_events 32/0/0). Record 15.229 (merge 6).
- testshim-tmp addendum 2818a4f (summary only, the tmp/tmp* clean-up note in 15.223 (15)) -> main e68c2fb (trial bcf8453). It was queued after seq 10's list; I took it in queue order as testshim-tmp's follow-up. Suite 829/0/3. Record 15.223 (merge 5).
- Root tree at e68c2fb. validation_check: 0 MISSING; 175-177 unindexed until figidx46.
Still queued, not ready:
- figidx46 (#46): its README rows cite sections that are only on longpext; it waits for #44 to queue longpext (longpext first, seq 10).
- cert13 (#13): golden NOT RUN; survey_pipeline.py changed, priced ~17.5 core-h, waiting on Alistair's yes to the jobs (D59). When its golden has run on a tree with main merged in, I check whether main has moved on any checked module since, and rerun only if so. Any rerun is shown to Alistair as exact sbatch commands first.
Inform: #15 (pickfix on main; all three #15 entries merged today); #41 (addendum on main).

Jobs: none. Core-h: 0. Files: not taken.

SETTLED:
- #15: pickfix at ef7f106 merged, main 30f1961, 15.229 (merge 6), suite 829/0/3.
- #41: addendum 2818a4f merged, main e68c2fb, 15.223 (merge 5), suite 829/0/3.

NEEDS YOU:
- none.

NEXT:
- longpext then figidx46 when #44 queues longpext; cert13 when its golden is done and the entry is ready.
