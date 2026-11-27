seq: 6
state: needs-you
date: 2026-11-27T15:06Z
host: login7c
---
#41 (file quota): carried out instruction 6. Unpacked the three NGC 1313 observations for #18 and copied out the 9 idle worktrees. The deletions wait for Alistair in the #41 terminal.

Instruction 6: parts 1 and 2 done. No terminal instruction since the last report.

1. UNPACK DONE for #18 (D47 (a)). #18 can run X-2's regions now:
- 0405090101_NGC1313-X1: 83 files + 1 dir
- 0693850501_NGC1313-X1: 83 + 1
- 0693851201_NGC1313-X1: 82 + 1
That adds 251 inodes. Each tar was checked against its SHA256SUMS first, and each file was sha256-checked as it was extracted, with nothing overwritten. quota_pack.check of the loose files against the sums finds 0 problems on all three. The tar + sums are kept, because removing them would be a deletion. Script: logs/q41/unpack_obs.py; log: logs/q41/unpack.jsonl.

2. COPY-OUT of the 9 worktrees (logs/q41/copyout_worktrees.py; log logs/q41/copyout.jsonl): every gitignored or untracked file found only in the worktree was copied, sha256-checked, never overwriting, nothing deleted. Links and __pycache__ were skipped.
- Copied to the root tree: 103 (a95 1, fig164 1, figs8 1, longp60 9, longpv1 29, lpfig 14, m82decay 43, valstore 5).
- Differing from the root tree's copy, so copied to archive/retired_wt_<name>/: 13 (longpv1 1, lpfig 11, valstore 1).
- Already identical in the root tree: 16. wt_methods had none.
- Re-check: every such file in all nine now has a byte-identical copy in the root tree or its archive folder; 0 missing.
That adds 116 files (~7 MB).

Recorded as 15.223 (16), commit daef6ba on testshim-tmp (queue line refreshed; summary + logs scripts only, so no suite rerun).

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began.
Files: lfs quota 175,025 / 200,000 (27 Nov ~15:40).

SETTLED:
- #41: three NGC 1313 observations unpacked for #18, all checks clean, 251 inodes (15.223 (16), daef6ba).
- #41: copy-out of the 9 idle worktrees, 0 files left only in a worktree (15.223 (16), daef6ba).

NEEDS YOU:
1. (Alistair, #41 terminal) Retire the 9 worktrees plus wt_p14a and wt_regrev (about 16,300 inodes; commands shown there). Recommend yes.
2. (Alistair) Clear tmp/tmp* older than 1 h once testshim-tmp merges (about 37,000). Recommend yes.

NEXT:
- On each yes, run the step, report the files freed, and update the checklist. Nothing has been started.
