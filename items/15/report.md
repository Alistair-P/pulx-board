seq: 5
state: needs-you
date: 2026-11-27T13:16Z
host: login7c
---
#15 (board seq 4 + 5; D44, D47): naming is in, the pick fix is built and queued, but two parts are stuck. Only 12 of batch 1's 43 region runs worked, and the 0884030101 rerun is blocked by the new cluster policy.

1. **D47 naming** (logs/intake15/run_regions.py):
   - A known pulsar takes the bare slot.
   - Names: the existing PULX name (NGC1313-X2, M51ULX7, ...); else the survey list's literature name (HolmbergIX-X1, Circinus-ULX5, NGC4395-ULX1); else `<HOST>-<Jname>`.
2. **Batch 1 regions:** 43 run on the login node.
   - **12 OK:** all NGC 1313 X-2, 8 min in total.
   - **31 failed instantly:** `new_obs_regions.run_one` finds a prep folder only as `ODFs/<obsid>_*/dir`, but run_batch prepped every non-pulsar ObsID as `ODFs/<obsid>`. **Proposed one-line fix, not applied (tool code):** glob `<obsid>_*/dir`, else `<obsid>/dir`. With approval, the 31 take about 30 min on the login node.
   - **Review PNGs:** 16 drawn (these 12, plus 3 earlier X-2 results and 0830191401 M51ULX7), in stats/new_obs_regions/<obsid>/<name>/review.png. 15 pass every check. 0830191401 fails the count check: net 915 < 1,000. **They're ready for Alistair's review.**
3. **D44, pickfix 8b03189** (off main; queued NOT READY; merge after intake15):
   - Header times count only if TSTART > 0. The GTI live time now ranks before the header span. A file with no EXPOSU tables is never the primary.
   - test_pick_pn_events: 27/0/0, including 6 new tests.
   - **Header replay** (old vs new vs strict) on every listed ObsID whose folder has ≥ 2 pn event lists, 4 in all: only 0884030101 changes (S001 → U002 alone). The strict option changes nothing, so it's kept as D44 allows. It doesn't fix 0884030101: S001 has 8 of its 12 EXPOSU tables. My (25)(c) said it had none, which was wrong; I've corrected it with a dated pointer.
   - **Not replayed:** the other §15.84 multi-exposure ObsIDs, whose event lists are inside #41's packs, which rule 1 keeps closed.
4. **0884030101 rerun: BLOCKED by cluster policy** (updated 27 Nov). sbatch needs Alistair's own yes to the exact command, and removing files needs his OK; board approval isn't enough for either. Prepared:
   - Delete the failed run's derived files: pn_clean.fits (built from S001), rateEPICPN.fits, and the rejected pn_merged_evts.ds (558 MB) with its .inputs.
   - Then from `/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_pickfix`: `sbatch slurm/submit_prep_one.sh 0884030101 0884030101`
     - Resources: 1 CPU, --mem 18000M (3 billed CPUs), 1 h limit, partition cosma5, venv via bashrc. About 1 billed core-h.
     - Output: logs/pickfix/prep1obs_<jobid>.out / .err. Stop with `scancel <jobid>`.
5. **NEW, pre-existing:** 0150280101's batch 1 prep used S011, a 7.6 ks **CalClosed** exposure (filter shut, no source photons), instead of the 6.7 ks Thin1 S001. pick() ranks by length alone; the filter gate exists only in the merge set. **Proposed:** a Closed or CalClosed exposure is never the primary while an open-filter one exists; then re-prep 0150280101. I left it out of the region run.

Recorded in §15.229 (26) (intake15 f962fa1, queued; test_intake15 16/0/0).

Jobs: none of mine (12445111 and 12445113 belong to other sessions).
Core-h: 0 (login only: about 8 min of regions plus header reads).
Files: 168,635.

SETTLED:
- D47 naming is implemented.
- 16 review PNGs are ready for Alistair's #17 review.
- pickfix is built, tested and replayed; only 0884030101 changes.

NEEDS YOU:
1. Approve the one-line fix to run_one's folder lookup, so the other 31 batch 1 ObsIDs get regions.
2. For Alistair himself (cluster policy): OK to delete the 4 failed files in ODFs/0884030101/dir, and yes to the sbatch command above.
3. Approve the CalClosed rule for pick() (a filter-closed exposure is never the primary while an open one exists), then re-prep 0150280101.

NEXT:
- With 1: run the 31 regions (about 30 min, login node), draw their PNGs, then tell the board.
- With 2: rerun 0884030101, check it used U002 and barycen succeeded, then mark pickfix ready.
- With 3: add the rule to pickfix with tests, re-replay, and prepare 0150280101's re-prep for Alistair's yes.
