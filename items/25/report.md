seq: 1
state: done
date: 2026-11-26T21:50Z
host: login7c
---
#25 (artefact battery, check (k)): checked the merge record of p14a-calib on main and settled the checklist line, as instruction seq 1 (plan 25.2) asked.

Jobs: none
Core-h: this step 0. Since the item began: section 15.228 < 1 core-h on the login node; the earlier parts' costs are in sections 15.221 and 15.224.
Files: no quota reading taken.

SETTLED
- p14a-calib is on main. The merge record is section 15.228 (merge 1), commit 15285f7 (trial merge 2b03da2), and includes 5f9a009 as its last commit.
- The merged-tree suite passed: 772 passed, 0 failed, 3 skipped. That is main's 765 plus the 7 tests in test_p14a_lattice. test_frame_raw_equiv passes again. The record states that no golden check was needed and no ADOPTED line was written.
- The checklist #25 line is set to settled ([x]). Battery rule set rev3 = rev2 + (k) is on main:
  - 0 of 480 false vetoes at a50.
  - 82 of 82 forgeries caught. The 95% lower bound is 95.6% counting forgeries and 85.8% counting the 24 lattice lines.
  - (d) to review and (k) to a veto candidate are recorded for #27 in section 15.228 (12).
- The merge record's own queue entry is closed.

NEEDS YOU
- Nothing for #25.
- Housekeeping, which is Alistair's to decide under POLICY: the worktree z_sq_weighting_wt_p14a and the branch p14a-calib are no longer needed. Remove them only on his word, with ./link_data.sh --remove first and never --force.

NEXT
- None for #25. The (k) veto vs review choice belongs to #27. This session stops here and keeps waiting on the board under rule 15.
