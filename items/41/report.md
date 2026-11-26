seq: 1
state: idle
date: 2026-11-26T17:26Z
host: login7c
---
#41 (file quota): acted on overseer instruction seq 1. I ran the superseded check for archive/q41fix/ ahead of the deletion decision and am waiting on the board for quota41b's merge.

Instruction seq 1: received. No 25 Nov instruction was meant for #41 (noted). Rule 15e clarification read.

CHECK (read-only, login, about 10 min): every folder in archive/q41fix/ is superseded by a rebuilt pack with matching checksums. For each of the 4 folders:
- the archived tar + sums pair matches its recorded old sha256;
- the live pair matches its recorded new sha256;
- quota_pack.check on the live pack finds 0 problems;
- the member names are the same;
- every unchanged FILE entry is identical;
- every old LINK entry (252 / 280 / 268 / 200) is now a FILE, with 0 LINK entries left;
- a full extract test of the live tar finds 0 problems.
Details: /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_q41/logs/q41/q41fix_superseded_20261126.txt. The archive holds 8 files in all. Nothing was deleted.

Jobs: none.
Core-h: 0 this step; 0 since the item began.
Files: lfs quota 146,121 / 200,000 (26 Nov, before this check; the check writes no files).

SETTLED:
- #41: archive/q41fix/ is confirmed superseded by the rebuilt packs, all checks pass (logs/q41/q41fix_superseded_20261126.txt; data check, not committed).
- #41: earlier items unchanged: 15.223 (13)-(14), quota41b queued at dfa0244, suite 740/0/3.

NEEDS YOU:
1. (Alistair) Delete archive/q41fix/ (4 folders, 8 files) once quota41b merges? Recommend yes: the check above passes on all four.

NEXT:
- Wait on the board. When told, delete archive/q41fix/, and record it as a dated addendum in 15.223 (14) once quota41b has merged. Nothing has been started.
