# Digest since the last overseer wake

The dispatcher adds one block per item it handles. The overseer clears this file at each wake
(the blocks stay in git history).

<!-- block format:
### ID, report seq N (STATE), HH:MM
- what the report says, in 1-3 lines
- sent: plan ID.k (instruction seq M) | held: running | for overseer: why
- read in full: yes/no
-->

### 11, report seq 11 (needs-you), 18:34
- Batch 1 tag list and job script prepared, not submitted; rest of targets18 re-queued at 5d45f76 (now on main). Swap sbatch still at Alistair's terminal. Asked overseer to record D64 (already recorded 18:10).
- for overseer: NEEDS YOU to overseer (11.3 otherwise holds)
- read in full: yes

### 13, report seq 2 (needs-you), 18:24
- cert13 merged with main 6db5e1f, queued 173fd0e, suite 820/0/5, draft --check CONSISTENT. Touches survey_pipeline.py, so asks for the c13 golden (~17.5 core-h) or to rely on merge's golden.
- for overseer: plan 13.3; Alistair: golden sbatch, Z1/Z3 max rule, ADOPTED line
- read in full: yes

### 15, report seq 13 (needs-you), 18:40
- regfix merged with main, re-queued 4a2f274. D63 stage 1: (i) all targets ~210-300 core-h, (ii) neighbour fields ~40-100 core-h; validation rule pre-registered. Files 171,598.
- for overseer: plan 15.4 (D63 design report); Alistair: scope and fov/area rules
- read in full: yes

### 41, report seq 6 (done), 19:44
- testshim-tmp on main, so tmp/ backlog cleared under Alistair's earlier yes: 50,028 inodes, quota 121,644. Addendum 2818a4f queued. Settled.
- held: 41.2
- read in full: no

### merge, report seq 10 (running), 19:30
- targets18 5d45f76 merged, main 6dd6232, suite 802/0/3, no golden needed. regfix next.
- for overseer: merge.1's text names the old D42 order, so not sent; session continues under instruction 10
- read in full: no

### merge, report seq 10 (idle), 21:23
- pickfix ef7f106 merged (main 30f1961) and #41 addendum 2818a4f merged (main e68c2fb); suite 829/0/3. No ready entries: figidx46 waits for longpext, cert13 for its golden.
- for overseer: merge.1 out of date; session unaware of Alistair's cert13 golden deferral; #44 instruction 15 unanswered 3.7 h
- read in full: no
