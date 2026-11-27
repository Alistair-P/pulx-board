# Digest since the last overseer wake

The dispatcher adds one block per item it handles. The overseer clears this file at each wake
(the blocks stay in git history).

<!-- block format:

### 15, report seq 3 (needs-you), 09:12
- Second array (job 12436619) ran, all tasks completed; 14 downloads in INTAKE.md. region_review.py summary written (§15.229 (25)(a)); intake15 queued 0ada393.
- D43: 0884030101 diagnosed (S001 broken header, TSTART = 0); pick_pn_events.py fix proposed, not applied. Asks approval, plus whether to add the stricter no-EXPOSU option. Files 171,676.
- for overseer: NEEDS YOU D43 not covered by the plan
- read in full: yes

### 37, report seq 2 (idle), 09:05
- D41 acknowledged; no golden rerun. a95cut stays READY at 6b015e2 (main not merged in; the board can ask).
- held: waiting (37.2)
- read in full: no

### 11, report seq 8 (needs-you), 13:27
- D47 (b)/(c) done, targets18 b75e098 queued; finding (a) was wrong (survey_list ignores skip). X-2 swap blocked; D48 list 20 rows, no PNGs.
- for overseer: 5 NEEDS YOU not covered by 11.1; pilot waits for Alistair's terminal yes
- read in full: yes

### 15, report seq 5 (needs-you), 13:16
- D47 naming in. 31 of 43 region runs failed (folder-lookup bug, fix proposed); 16 PNGs ready. pickfix 8b03189 queued NOT READY; 0884030101 rerun needs Alistair's yes. CalClosed pick found in 0150280101.
- for overseer: failures and 3 NEEDS YOU not covered by the plan
- read in full: yes

### 41, report seq 4 (needs-you), 13:41
- Census done; files 169,781; projected peak ~199,700 without tmp cleanup and the testshim fix. D49 checks pass; removal waits for Alistair's OK.
- for overseer: 4 NEEDS YOU; no plan step
- read in full: yes

### 42, report seq 10 (done), 12:55
- Answered the overseer's three coverage questions and the two ObsIDs' mode, span and list status.
- for overseer: answers are for Alistair; no plan step
- read in full: yes

### 44, report seq 11 (idle), 12:53
- D51 recorded in 15.225 (16); #44 settled. Waits for 44.5; says sbatch now needs Alistair's own yes.
- for overseer: the policy change contradicts 44.5's "submit it"
- read in full: yes

### 15, report seq 9 (needs-you), 15:10
- Instruction 9 done: light-curve panel added, all 51 PNGs redrawn; verdicts 9 FAIL, 6 REVIEW, 36 PASS; 8 of 49 targets flagged.
- for overseer: asks whether any flag becomes a hard QA rule (Alistair); 2 reruns still wait at his terminal
- read in full: yes

### 41, report seq 6 (needs-you), 15:06
- Instruction 6 done: three NGC 1313 observations unpacked for #18 (+251 inodes); 9 worktrees copied out (+116 files). Files 175,025.
- for overseer: retirements now wait at Alistair's #41 terminal (new terminal ask); #18 not yet told X-2 can run
- read in full: yes
