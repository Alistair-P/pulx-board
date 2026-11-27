seq: 7
state: needs-you
date: 2026-11-27T12:17Z
host: login7c
---
#18 (#11's session): did instruction 7: step 2's tooling is built, tested and queued; the 2-tag pilot is ready but NOT submitted, because the cluster policy now needs Alistair's own yes to the exact sbatch command.

RESTART CHECK. The edit to preprocess.sh cut off on 26 Nov never ran: no backup existed, and the file matched HEAD. Nothing to restore; redone cleanly.

STEP 2 (15.235 (2); targets18 rebased on main df0a6f9; queued at 992696d):
- Analysis-only switch (D28): `preprocess.sh -a`, or `analysis_only = 1` in a section, stops right after run_analysis. No HENDRICS or weighted search, no qa_obs, no survey run. It writes one ANALYSIS_ONLY row to the summary, because the survey's CONFIG is built only from summary rows, and D27 needs every tag ready for survey_sensitivity. Only the survey's placeholder mode reads that row; every other reader drops it. A later real search is not mistaken for already done.
- Staging (D30, D37): tag results go to data/params_new_targets.conf (not params.conf), through the same HOLD_SOURCES and MIN_COUNTS gates and the same region_review overrides as bare targets. Every section has analysis_only = 1. Tags also get rows in the flags, low-count and held tables, keyed by target ID.
- Batch: `new_obs_regions.py --targets FILE` runs the region tool per tag and draws each #17 review PNG. The target table writes FILE: 170 tags, 46 ready on disk today.
- Names: a known pulsar keeps its name; any other source is <host>-<tag>, the same in every epoch.
- Tests: test_targets18 9/0/0. Suite 791/0/3. Neither changed file is a manifest or orbit module, so no golden.
Interface note for #15: new_obs_regions.stage() now also writes tag rows into new_obs_flags.tsv, params_new_obs_lowcounts.tsv and params_new_obs_held.tsv.

PILOT (15.235 (3), pre-registered before anything ran).
- Deviation: the planned ObsID 0830191601 was packed by #41 on 19 Nov, after the inventory the table read. 14 of the 22 "ready" tags were packed since. The `ready` column now checks the disk itself. The pilot moved to 0830191401: tags D201128402010003 and D201128402010012 (prep stage, unpacked).
- Done on the login node, about 1 min: both regions OK, both review PNGs drawn (no failing check), preflight 0 errors, shared directory hashed beforehand (81 files).
- Job script: slurm/submit_targets18_pilot.sh. 2 CPUs x 4 h cap = 8 core-h. It writes a pilot summary, never production signal_summary.csv.
- New in this pilot: a tag run where the bare target hasn't had run_analysis yet.

Jobs: none.
Core-h: 0 this step; #18 0.
Files: lfs quota 172,545 (27 Nov; up from 145,712 on 26 Nov, mostly #15's batch 1). The pilot adds about 26 per tag.

SETTLED:
- #18 step 2: tooling queued (targets18 992696d); 15.235 (2)-(3).

NEEDS YOU:
1. Alistair: submit the pilot? This needs your own yes in the terminal, per the cluster policy. Exact command, from /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt:
   sbatch slurm/submit_targets18_pilot.sh
   Resources: cosma5, account durham, 1 task, 2 CPUs, 12000M, 4:00:00 (cap 8 core-h). No modules or conda; the venv comes from bashrc.
   Output and error: stats/targets18/pilot/t18pilot_<jobid>.out and .err in the root tree. Stop it with: scancel <jobid>.
   Recommend yes.
2. Findings a-c (skip lifts, bare slots for P13 and X-2, the 0693760101 rename) are still with Alistair. No params.conf change until then.

NEXT:
- If submitted: wait for the job's sha256 file before touching wt_mt; then check the pre-registered PASS rule on the login node and report. Nothing started.
