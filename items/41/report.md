seq: 2
state: done
date: 2026-11-26T18:05Z
host: login7c
---
#41 (file quota): carried out overseer instruction seq 2 (D21, plan 41.2): reran the superseded check, deleted archive/q41fix/, and recorded it.

Instruction seq 2: done in full. No terminal instruction from Alistair since the last report.

- CHECK, rerun before deleting (MEASURED). Script logs/q41/q41fix_check.py; log /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_q41/logs/q41/q41fix_check_20261126.log. All 4 folders pass every check:
  - the archived tar + sums match their recorded old sha256, and the live pair matches its recorded new sha256;
  - quota_pack.check on the live pack is clean, and the member names are the same;
  - unchanged FILE entries are identical;
  - every old LINK entry (252 / 280 / 268 / 200) is a FILE in the live pack, with no LINK left;
  - the full extract test is clean;
  - each archive folder held only its tar + sums pair.
- DELETED: the 4 folders in z_sq_weighting/archive/q41fix/ (8 files) and the empty parent: 13 inodes. Nothing outside #41 referred to them (git grep on main: only summary.txt). The rebuilt packs in ODFs/<folder>/ are now the only copies.
- RECORDED as a dated addendum in 15.223 (14), with the check's log path: commit 26cca25 on quota41b, which was fast-forwarded to main 1399fad, so the branch is 1 commit ahead. Queued again under rule 14. Summary text + a read-only check script only, so no suite run. Backup: archive/summary.txt.pre_q41fixdel_20261126; diff: logs/q41/summary_q41fixdel.diff.

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began (login only: the check took about 10 min, nice 10).
Files: lfs quota 155,162 before the delete; 154,548 a minute after. The delete itself removes 13 inodes; the rest of the movement comes from other sessions' jobs (12 in squeue).

SETTLED:
- #41: archive/q41fix/ deleted (13 inodes) after the rerun check passed on all four folders (15.223 (14) addendum, commit 26cca25, queued).
- #41: checklist line set to settled.

NEEDS YOU:
- none.

NEXT:
- Nothing left under #41 once 26cca25 merges. I'll wait on the board. Nothing has been started.
