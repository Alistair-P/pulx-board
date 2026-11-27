seq: 5
state: needs-you
date: 2026-11-27T14:40Z
host: login7c
---
#41 (file quota): carried out instruction 5 (D52): fixed the testshim tmp_path leak on branch testshim-tmp and queued it. The deletion commands are shown to Alistair in the #41 terminal, waiting for his yes.

Instruction 5: the fix is done and queued. The deletions wait for Alistair (cluster policy). No terminal instruction since the last report.

FIX (15.223 (15), commit 436eb0d, off main df0a6f9, 0 behind):
- testshim/run_suite.py removes each run's tmp_path / tmpdir in a finally block, after pass, fail or skip. ZSQW_KEEP_TMP=1 keeps them.
- tests/test_testshim_tmp.py (2 tests) is registered in run_all_tests.sh.
- Suite 784/0/3. The first full run gave 783/1/3: the 1 was test_provenance's not-a-repository test, because my private TMPDIR sat inside the worktree. A rerun with TMPDIR outside any repository passed 3/0/0.
- A full suite run now leaves 8 top-level entries (21 inodes) in TMPDIR, from 6 test files that make their own temp dirs (not changed here).

DELETIONS (shown to Alistair):
1. D49 wt_p14a, wt_regrev: checks passed (26 Nov census). 2,917 inodes.
2. tmp/tmp* older than 1 h: ~37,000 inodes. Recommended after testshim-tmp merges, since sessions keep leaking until then.
3. The 9 idle merged worktrees: NOT ready as is. All are clean, merged, with no job and no process inside, but 8 of them hold gitignored files that exist only there:
   a95 1, fig164 1, figs8 1, longp60 9, longpv1 29, lpfig 14, m82decay 43, valstore 5. Some are cited by the summary.
   lpfig 11, valstore 1 and longpv1 1 also differ from the root tree's copies. wt_methods has none.
   Each needs a copy-out step first (copy into the root tree with a sha256 check, never overwriting; files that differ go to archive/retired_<wt>/).

Jobs: none of #41's.
Core-h: 0 this step; 0 since the item began. Login: one full suite at nice 10.
Files: lfs quota 173,589 / 200,000 (27 Nov, after the suite).

SETTLED:
- #41: the testshim tmp_path leak is fixed and queued (15.223 (15), 436eb0d, testshim-tmp, suite 784/0/3).

NEEDS YOU:
1. (Alistair) Yes to the D49 removal of wt_p14a and wt_regrev? Recommend yes.
2. (Alistair) Yes to clearing tmp/tmp* folders older than 1 h, once testshim-tmp merges? Recommend yes.
3. (Alistair) Approve a copy-out plan for the 9 worktrees before retiring them (wt_methods needs none)? Recommend yes.

NEXT:
- On each yes, run that step, report the files freed, and update the checklist. Nothing has been started.
