seq: 15
state: needs-you
date: 2026-11-28T16:33Z
host: login7c
---
#44/#46, seq 15, report: longpext checked, main merged in, suite passed and queued. The confirming-simulation pilot is ready and waits for Alistair's yes.

1. DONE: longpext queued (#44).
   - Checked: `git diff 1cbad1c..longpext` touches only docs/LESSONS.md, logs/longpext/* (three scoring scripts), summary.txt, validation/README.md and validation_plots.py, where it only adds the @fig functions for 175-177. No pipeline code.
   - main 57974c9 merged into longpext (45a4aee). The conflicts were text only, in summary.txt, LESSONS group 7 and the README, and both sides were kept:
     - summary sections in order 15.225 to 15.236;
     - the only lines changed against main are the 26 Nov Z3 correction and the LESSONS group count;
     - validation_check: 181 indexed, 0 missing, 0 unindexed.
   - Full suite on the merged tree: ALL SUITES PASS, 829 passed / 0 failed / 3 skipped (logs/longpext/suite_merged_main.log).
   - figidx46's entry now says it depends on longpext: merge longpext first, after which figidx46 adds identical README rows and can be dropped.
2. D39: the rule (15.236 (6), e6c9cb5) was committed before any draw.
   - D63 note added (15.236 (6)(f), 50adc2c): the simulation uses main 57974c9's pre-D63 p. It is synthetic with w = 1, so p does not enter.
   - The pilot (8 draws, 4 CPUs x 1:30, cap 6 core-h billed, expected ~2-4) has been shown to Alistair in the terminal: `sbatch slurm/submit_confirm46d.sh pilot` in wt_confirm46d. NOT submitted: waiting for his yes (D59).
Checklist #46 updated.

Jobs: none.
Core-h: 0, login node only (the suite, at nice 10).
Files: +1 log.
SETTLED: longpext queued; figidx46 depends on it.
OPEN: Alistair's yes for the pilot. Then reprice, then ask him for the full run if it is within 110 core-h billed.
