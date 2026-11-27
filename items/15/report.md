seq: 7
state: needs-you
date: 2026-11-27T14:46Z
host: login7c
---
#15 (board seq 6 + 7; D53, D54, D55, D58): batch 1's regions are all done and the gallery is ready with 51 PNGs. The flare panel fix (D58 B) is not done: the panel isn't what the request describes, so I'm asking which fix is wanted. Neither rerun has started: both need Alistair's own yes here.

1. **D53 + D55, branch regfix 03a8de3 (off targets18, queued: merge after targets18, before intake15):**
   - The region tool now also finds bare `ODFs/<obsid>/dir` folders.
   - NGC1313-X2 is out of HOLD_SOURCES (released 18 Nov, §15.229 (8)).
   - run_regions uses #18's `stack_name`; all 47 names are unchanged.
   - Tests: test_regfix 7/0/0, test_targets18 10/0/0 (its held-source example is now SMCX3), test_region_review 7/0/0.
   - Correction: the 31 failures came from intake15's older copy of the tool. Main's copy already reads `<obsid>.root`.
2. **Batch 1 regions:** the other 31 all OK, about 1 min each on the login node. 47 of 47 targets have regions; 0150280101 and 0884030101 wait for their re-preps.
3. **D58 A, gallery:** `stats/region_review_gallery/` in the root tree, with one `<obsid>_<name>.png` link per review.png plus index.tsv. `draw` refreshes it.
   - **It holds 51 PNGs:** 47 from batch 1 and 4 of #18's. #18's show "not recorded" until redrawn; I didn't redraw them.
   - **Batch 1:** 38 pass every check and 9 fail one.
     - Counts: 0830191401 M51ULX7 (net 915), 0674210601 NGC0224-J004247.1+411615 (net 858), and 0504780101 NGC0703-J015239.6+361025 (net −1,103: background A sits on brighter diffuse emission than the source).
     - Field of view, with the source 81–87% exposed: Holmberg IX X-1 in 5 ObsIDs, and 0111800101 NGC3031-J095533.0+690034.
4. **D58 B, not done:** the last panel of regions.png (drawn by the ulxregions package) plots 10–12 keV light curves per CCD. Every aperture CCD is thick black, and it has no source, background or monitor curves. Two possible fixes; NEEDS YOU 1.
5. **D54, pickfix ef7f106:**
   - A Closed or CalClosed exposure is never the primary while an open-filter one exists.
   - Tests: 32/0/0 (5 new).
   - Replay: 0150280101 moves S011 → S001 (Thin1) and 0884030101 moves S001 → U002. The other two multi-exposure dirs are unchanged.
6. **Reruns, waiting for Alistair's yes in the terminal:** both run from `/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_pickfix`. Each job: 1 CPU, 18000M (3 billed CPUs), 1 h limit, cosma5, about 1–3 billed core-h, output in logs/pickfix/prep1obs_<id>.out/.err, stop with `scancel <id>`.
   - **0884030101:** `rm ODFs/0884030101/dir/{pn_clean.fits,rateEPICPN.fits,pn_merged_evts.ds,pn_merged_evts.inputs}`, then `sbatch slurm/submit_prep_one.sh 0884030101 0884030101`.
   - **0150280101:** `rm ODFs/0150280101_NGC1313-X2/dir/{prep_events.done,pn_clean.fits,rateEPICPN.fits}`, then `sbatch slurm/submit_prep_one.sh 0150280101 NGC1313-X2`.
   - D57 lets me submit jobs without the board, but the cluster policy still needs Alistair's own yes; the stricter rule applies.

Jobs: none. Core-h: 0 (login only: about 31 min of regions, 47 PNGs). Files: 174,448.

SETTLED:
- Batch 1 regions are complete (47 of 47 targets), with D47 names from the shared `stack_name`.
- The gallery is ready: 51 PNGs, of which 38 of batch 1's 47 pass every check.
- The pickfix closed-filter rule is built, tested and replayed.

NEEDS YOU:
1. D58 B: recolour the existing per-CCD panel in regions.png (redrawing it means rerunning about 50 region builds, about 1 h on the login node), or add a new panel to review.png with source, background A, B and full-field monitor curves, flares shaded (about 30 s per PNG)? Or drop it?
2. Alistair, in the terminal: yes or no to each of the two deletions and two sbatch commands in point 6.

NEXT:
- After the reruns: check the chosen exposure and barycentring, run their regions and PNGs, then mark pickfix ready.
- With 1 answered: build the panel fix and redraw every PNG.
