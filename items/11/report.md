seq: 10
state: needs-you
date: 2026-11-27T17:51Z
host: login7c
---
#18 (#11's session): the 2-tag pilot PASSED on every pre-registered check. The X-2 swap job is ready and waits for Alistair's yes in this terminal.

PILOT RESULT (job 12448511; COMPLETED 0:0 in 6:57 on 2 CPUs, about 0.23 core-h of the 8 cap; 15.235 (8)). Checked against the rule written before the run (15.235 (3)):
- rc 0 for both tags, about 3-4 min each.
- Each targets/<tag>/ has pipeline_inputs.json, pn_clean.fits and src_region_events.fits, stamped with the target ID and barycentred at the tag's own position (DE200, frame-aligned).
- No search output of any kind: no weighted-search, HENDRICS or timing file, no QA record, no survey JSON. Checked by file name only; nothing opened (rule 1).
- The pilot summary holds exactly one ANALYSIS_ONLY row per tag and nothing else.
- 0830191401's shared dir/: all 81 files byte-identical before and after.
- In the survey's placeholder mode both tags get a CONFIG entry, and load_observation reads them (19,289 and 10,175 events). In strict mode they get none, as designed.
So an analysis-only tag is ready for survey_sensitivity (D27) with no search output (D28).

PRICE UPDATE: run_analysis alone took about 3-4 min per tag on 2 CPUs, about 0.1-0.15 core-h. Step 1's estimate of 1-3 core-h per tag included the searches. All 166 tags are of order 20-30 core-h (INFERRED), plus the shared epproc for ObsIDs not yet reduced.

SUITE after the guard fix: 793/0/3. targets18 3b851cc queued.

Jobs: none (12448511 done).
Core-h: about 0.23 this step; #18 about 0.23.
Files: +26 per tag (2 tags), pilot logs.

SETTLED:
- #18: 2-tag pilot PASS; 15.235 (8); targets18 3b851cc queued, suite 793/0/3.

NEEDS YOU:
1. Alistair, in this terminal: yes to `sbatch slurm/submit_targets18_ngc1313.sh`, from /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt? It runs the X-2 swap in 0405090101, 0693850501, 0693851201: -f -a on the X-2 bare (overwrites dir/'s loose X-1 products; the originals stay in #41's .tar), then -a on each X-1 tag. One ANALYSIS_ONLY row each goes to production signal_summary.csv. cosma5/durham, 2 CPUs, 12000M, 16 h, cap 32 core-h (expected about 1-2 from the pilot); out/err in stats/targets18/ngc1313/. Recommend yes.
2. Overseer: the full tag runs (166 tags, about 20-30 core-h in all) go batch by batch, inside #15's batches. Each batch needs Alistair's yes in this terminal (cluster policy) and his D26 per-batch approval. Shall I prepare batch 1's tag list and job script next? Recommend yes.

NEXT:
- On yes to 1: submit, wait for its sha256 file, check the 6 targets the same way as the pilot, and report. Nothing started.
