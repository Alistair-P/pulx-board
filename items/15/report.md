seq: 2
state: running
date: 2026-11-26T21:33Z
host: login7c
---
#15 (intake): batch 1's seed + prep is done (instruction seq 1 complete). Starting D37 (seq 2): review PNGs and a region-override script.

**Batch 1:**
- **At prep:** 45 of the 46 ObsIDs attempted (7 login, 1 pilot, 26 in job 12436014, 11 in job 12436619). 3 more have been at prep since 12 Oct. 0693760401 is skipped: it is the processed P13 calibration observation.
- **Downloads (D9):** all 14 COMPLETE on the first attempt. Source, UTC date, bytes, sha256 and listed-file count are in data/survey_list_v1/INTAKE.md (ff2fc21).
- **Billed:** 19.8 core-h in all (pilot 1.0 + 13.2 + 5.6), against the 38–49 priced. Compute tasks took 2.9–21.5 min each, with at most 9.6 GB memory.
- **One failure, 0884030101:**
  - Its ODF has two pn exposures (S001 and the unscheduled U002). The merge failed verification, and the fallback picked S001, which has no EXPOSU extensions; barycen then stopped on a missing TSTART.
  - This is pn-exposure selection in preprocess.sh's resolve_pn_events / pick_pn_events, which is pipeline code, so I haven't touched it.
  - Its folder ODFs/0884030101 is left as it stopped (703 files).
- Recorded in §15.229 (23), commit 8f85d7c.

**D37, plan:**
- **Branch:** a new branch `regionreview` off main, in its own worktree, with tests. #18 can reuse it after merge.
- **review_png.py:** one PNG per (ObsID, target) in stats/new_obs_regions/<obsid>/<name>/review.png. Contents:
  - a smoothed log image wide enough for the background;
  - the aperture and the 20" timing radius, backgrounds A and B, masks, other list targets, and CCD edges and chip gaps from the exposure map;
  - a zoomed panel on the source;
  - a caption with the counts, the flags row, and whether each region is automatic or a manual override.
- **region_override.py:** writes rows (date, ObsID, target, region kind, centre, radius, reason) to a separate overrides file and never edits the automatic output. It reruns the field-of-view, P30 and counts checks, then redraws that PNG.
- **Staging:** new_obs_regions --stage applies the overrides on top of the automatic regions, so both stay on record.
- **Cost:** login-node work only, light, no Slurm.

**Batch 1's regions are needed before its PNGs exist, and they aren't made yet:**
- new_obs_regions.py takes target positions from xmm_pulx_archive.tsv. Batch 1's non-PULX survey targets need a small driver that reads survey_list_v1 instead.
- That driver has to give each new source a params.conf name. I propose `<HOST>-<Jname of the catalogue position>`, which is the same for every observation of one SOURCE_ID. PULX targets keep their existing names (NGC1313-X2, ...).
- I'll time one region run on the login node, then price the batch-1 run, about 46 ObsIDs, before starting it.

Jobs: none running (12435948, 12436014, 12436619 done).
Core-h: 0 this step; 19.8 billed since the item began.
Files: 160,001 (26 Nov).

SETTLED:
- Batch 1 seed + prep: 45 of 46 at prep, 19.8 billed core-h.
- All 14 downloads are complete and recorded in INTAKE.md.

NEEDS YOU:
1. 0884030101: should I propose a fix to pn-exposure selection (a bug fix, so the overseer can approve it), or drop the ObsID from batch 1?
2. The name for new survey sources in params.conf: `<HOST>-<Jname>`, as proposed above? It becomes the stacking key, which must be spelled identically for every observation of a source.

NEXT:
- Build review_png.py and region_override.py with tests on the regionreview branch, trying them on existing region results, then queue the branch.
- Time one batch-1 region run and price the rest. Then make batch 1's regions and PNGs and tell the board when they are ready for Alistair.
