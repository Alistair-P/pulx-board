seq: 11
state: idle
date: 2026-11-27T12:53Z
host: login7c
---
#44, seq 11 (D51), report: I recorded Alistair's closure of option A in summary 15.225 (16). #44 is now fully decided.

1. DONE: 15.225 (16), commits 5dcafb9 and ff1a73a on wt_longpext. A is closed, never measured, with D51's three reasons:
   (a) B's window arm (the same orbit bank, long part included, on an 80 ks window) found nothing on the same kind of draws: 0 WITH-only of 93 binaries, and its arm was never over threshold (15.225 (15), figure 177).
   (b) A needs a new long-part calibration above 80 ks: 600 null realisations at M 6-8, 2,171-5,178 core-h, the largest cost of any option.
   (c) #46's option (d) covers strong-Doppler binaries above 120 ks.
   - It is stated as a known v1.0 limitation alongside B's NO-GO: the long part runs only at 57.5-80 ks. Above that, long binaries are left to the coherent arm, the short orbit bank and, above 120 ks, (d)'s window arm.
   - #44's options: A closed, B NO-GO, C1 NO-GO, C2 closed. D was never taken up, because the re-opening in (12) named A and B only.
2. Checklist #44 is set to settled ([x]).
3. wt_longpext's code is no longer frozen (D51). Nothing changed there apart from summary.txt.
4. WAITING for the board's instruction on #46's confirming simulation (D39) once (d) is on main.
   - Cluster policy changed on 27 Nov: I may run sbatch only when Alistair asks for that job in his own message and says yes to the exact command and resources I show him. A board approval alone is not enough.
   - So when the instruction comes, I will price it and set it up, then ask Alistair in the terminal before submitting.

Jobs: none.
Core-h: this step 0. #44 in total: batch 1 552.6, plus the pilot and C1 runs recorded in 15.225.
Files: no change.

SETTLED: #44 is decided (A closed, B NO-GO, C1 NO-GO, C2 closed); known limitation recorded.
OPEN: #46's confirming simulation, after (d) is on main; its sbatch needs Alistair's direct yes.
