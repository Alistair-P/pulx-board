# Digest since the last overseer wake

The dispatcher adds one block per item it handles. The overseer clears this file at each wake
(the blocks stay in git history).

<!-- block format:
### ID, report seq N (STATE), HH:MM
- what the report says, in 1-3 lines
- sent: plan ID.k (instruction seq M) | held: running | for overseer: why
- read in full: yes/no
-->
