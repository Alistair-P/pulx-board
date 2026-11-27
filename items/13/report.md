seq: 2
state: needs-you
date: 2026-11-27T18:24Z
host: login7c
---
#13 — reply to board seq 2. Login node only, no compute. cert13 at 173fd0e, QUEUED.

1. MERGE + CHECK. main 57974c9 merged in (712b4ca), then the newer main 6db5e1f (targets18, 9631241). Conflicts were text only:
- summary.txt and run_all_tests.sh: both sides kept.
- CLAUDE.md "Known gaps": both clauses kept, mine (the gate) and main's (#12 closed, D22 (b)). That line stays Alistair's.
build_cert.py now:
- inclusion = main's a95_template_ref < 0.25 (the PRE-a95cut fallback removed);
- above_120ks = (C) then #46's (d): stacked arm at M 4 on the first or last 120 ks by sum p², full-span M 5 not run, add-on R1W budgeting (non-orbit shares ×0.6897, Z1/Z3 at R1 +1.1, window row stw at R0's 120 ks K_eff +1.4), union check 2 vs 3.80.
Re-derived tables show both parts:
- 122 and 136 ks: all 10 octaves R1W, margin 1.1, stw finite at M 4, st NaN.
- ≤120 ks: unchanged R0/R1, no window key.
New tests cover this, and --check now catches a changed stw or window M. test_build_cert 11/0/0. Suite 820/0/5 = main's 800/0/3, every suite count unchanged, + test_certificate 9/0/2 + test_build_cert 11/0/0.

2. GOLDEN. cert13 vs main, by file: CLAUDE.md, docs/LESSONS.md, logs/p13/build_cert.py, run_all_tests.sh, summary.txt, survey_pipeline.py, tests/test_build_cert.py, tests/test_certificate.py, tests/test_survey_pipeline.py, tests/test_template_beta.py; in commit 173fd0e also slurm/submit_golden_c13_*.sh (new scripts, mode 755 like s46d's).
survey_pipeline.py is in gate_block()'s list (a manifest module), so the 15.236 (merge 1) golden does not cover it. The change is gate code only, outside run_one: prediction = every output identical to s46m.
Scripts are written, NOT submitted: slurm/submit_golden_c13_{syn,real,orbit,window}.sh, GOLD_TAG c13, accept lists as s46m.
Price measured at s46m: syn 19 CPU × 0:28 = 8.9, real 4 × 0:36 = 2.4, orbit 0.2, window 2 × 3:02 = 6.1. Total ~17.5 billed core-h (range 15–25), caps 34.5.

3. DRAFT rebuilt at 173fd0e, --check CONSISTENT. Contents: 23 modules + 9 inputs, 9 span tables, 49 unusable (span, arm, octave) entries, 73 IN targets.
READY: a95cut, mcseed (on main since 15.217 (12)), rednoise, #46, rev3 battery, signed margins, clean tree.
PENDING:
(i) 15.234 (1)(a) Z1/Z3 = max(transfer, direct) above 120 ks is not in the code under (d). The direct fit (design values) sits above the transfer at:
- Z1: 0.053 Hz +1.71, 0.106 Hz +0.22, 0.2125 Hz +0.50
- Z3: 0.053 Hz +1.00, 0.106 Hz +1.20, 0.2125 Hz +0.86, 0.425 Hz +1.61, 1.7 Hz +0.40, 3.4 Hz +1.00
(d)'s union check passed on the transfer-only R1W table (Z1 1 vs 2.36, Z3 0 vs 0.26), but on the same t136 nulls the direct fit came from. candidate.json is R0 +1.4, so it no longer compares directly. Owner: Alistair (decision). If applied: #13 or #46 code in octave_thresholds (manifest), with golden and ADOPTED.
(ii) survey_pipeline.py ADOPTED line for cert13's file. Owner: Alistair, after one golden.

4. QUEUED cert13 (#13) for the merge session. Golden NOT RUN, ADOPTED needed. The stamp waits on (i), not this merge. Checklist #13 updated.

Jobs: none. Core-h: 0.
Files: logs/p13/build_cert.py, tests/test_build_cert.py, summary.txt 15.234 (5), run_all_tests.sh, CLAUDE.md (merge), slurm/submit_golden_c13_*.sh; draft stats/survey_thresholds/validated_DRAFT_v1.json; backups archive/*.pre_cert13_20261127.

SETTLED: merge, inclusion, (d) in the draft, suite 820/0/5, queued.
NEEDS YOU (Alistair):
1. Golden: yes to `cd wt_cert13 && sbatch slurm/submit_golden_c13_syn.sh; sbatch ..._real.sh; sbatch ..._orbit.sh; sbatch ..._window.sh` (~17.5 core-h)? Or let the merge session's merged-tree golden be the only one. Recommend: one golden only, the merge session's, since it runs anyway.
2. The max rule (i): retire it under (d), or apply it at R1W's shares? Recommend: apply it (it's the user's 25 Nov rule and costs ≤ +1.7 in Z²), unless you treat (d)'s union check as superseding it.
3. ADOPTED line for survey_pipeline.py after that golden.
NEXT: wait on the board.
