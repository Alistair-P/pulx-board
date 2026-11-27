seq: 4
state: needs-you
date: 2026-11-27T13:41Z
host: login7c
---
#41 (file quota): carried out instruction 4 (repeats 3): ran the scoped census and the D49 checks. Stopped before removing the worktrees, because the cluster policy needs Alistair's OK in this terminal for each deletion.

Instruction 4: part 1 done; part 2 (D49) checked, removal pending that OK. No terminal instruction since the last report.

CENSUS (counts only): one streamed lfs find per scoped folder (worktrees, root-tree folders, tmp/), ctime after 26 Nov 21:41. A broad lfs find of the user dir was refused by the safety classifier; scope therefore excludes the legacy tree and ODF_tarballs.
In scope: 118,481 entries, 18,747 new since 21:41. The quota now reads 169,781 (172,545 at 12:17; other sessions' churn).
Top growth by folder:
- tmp/tmp* (test temp folders): 15,255 new (37,076 total, 4,146 folders). Owner: all sessions' test runs. Cause: testshim/run_suite.py makes tmp_path with tempfile.mkdtemp() and never removes it; TMPDIR = /cosma5/data/durham/dc-paga3/tmp; ~/.bashrc only clears entries older than 7 days.
- wt_pickfix: +1,406, a new worktree (#15, D43/D44, 27 Nov 11:23).
- tmp/claude-22935: +840 (Claude task output).
- .git: +410.
- stats/new_obs_regions: +320 (#15).
- stats/fast_golden: +88.
- worktrees mt / stacked46d / trial / rednoise / merge: +69 / 51 / 48 / 44 / 34.
- ODFs: 0 since 21:41. #15's batch 1 (12,137 in ODFs) was made 26 Nov 18:20-19:01.
Safe to pack or remove (nothing done):
(a) tmp/tmp* folders older than about 1 h: up to 37,076 files.
(b) A one-line testshim fix to clean tmp_path after each test, which stops the leak.
(c) 9 more worktrees that are merged, clean, without jobs and idle since <= 19 Nov: 13,401 files (list in the file below).
(d) Pack #15's batch 1 when its prep ends: about 2,700 files.
PROJECTION to end of intake (INFERRED, #15's plan constants: 18 files per packed obs, +1 per download, 26 per tag, peak ~500 per obs in a batch):
- as things stand: 169,781 - 2,700 + 3,224 (batches 2-5: 176 obs, 56 downloads) + 4,420 (170 tags) = ~174,700, with a peak of ~199,700 during a 50-obs batch. That is over the 195,000 safe line.
- with (a) + (b): ~137,600 (peak ~162,600);
- also with (c) + D49: ~121,300.
Tables and method: /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_q41/logs/q41/quota_census_20261127.md (+ .tsv).

D49 (wt_p14a, wt_regrev): both clean, fully merged, no Slurm job, no process with cwd inside, idle since 20 Nov / 26 Nov 21:38. Run records that exist only there: none (the one ignored non-link file in wt_p14a is identical in the root tree, same sha256). The two hold 1,518 + 1,399 = 2,917 inodes. NOT removed yet.

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began. Login: about 40 min of lfs find at nice 10.
Files: 169,781 / 200,000 (27 Nov ~14:00).

SETTLED:
- #41: scoped census and projection done (logs/q41/quota_census_20261127.md; data, not committed).
- #41: D49 pre-checks pass on both worktrees.

NEEDS YOU:
1. (Alistair, in the #41 terminal) Say yes to retire wt_p14a and wt_regrev with: cd <wt> && ./link_data.sh --remove && cd .. && git -C z_sq_weighting worktree remove <wt> (no --force). Recommend yes: the checks pass.
2. Clear tmp/tmp* folders older than 1 h (up to ~37,000 files)? Recommend yes, after (3).
3. Fix testshim to delete each tmp_path after its test (a bug that leaks files; it touches test infrastructure only). Recommend yes, as a small #41 branch with a test.
4. Retire the 9 idle merged worktrees in (c), after a session check on each? Recommend yes; 13,401 files.

NEXT:
- On yes to 1: remove the two worktrees, report the files freed, update the checklist. Nothing has been started.
