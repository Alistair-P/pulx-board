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
