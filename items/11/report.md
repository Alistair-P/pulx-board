seq: 8
state: needs-you
date: 2026-11-27T13:27Z
host: login7c
---
#18 (#11's session): did instruction 8 (D47, D48, D50). Names, P13 and 0693760101 are done and queued; the NGC 1313 X-2 swap is blocked; D48's list is built without PNGs; and my finding (a) was wrong.

CORRECTION FIRST. Finding (a) said skipped bare sections "never reach #19 unless the skip is lifted". That is wrong. survey_list() reads every params.conf section and never looks at `skip`; preprocess.sh skips a section only in a run given no obsid. D48 was decided on that premise. Lifting a skip changes almost nothing for the survey.

DONE (targets18 b75e098, queued; suite 792/0/3; 15.235 (4)-(5)):
- D47 (b) names: one shared rule, new_obs_regions.stack_name, for #15's bare targets and #18's tags. A known pulsar keeps its name; a "LIT:" list name becomes galaxy plus designation (HolmbergIX-X1); otherwise host plus Jname (UGC05336-J095753.3+690348 style). #15's run_regions.target_name has no literature-name rule yet; it should call stack_name. One list name ends in a Jname (LIT:W26 1eRASS J120242.5+015809), so it falls to host plus Jname.
- D47 (a) P13: no edit needed. In all four ObsIDs the bare section already is P13 (src within 1"). Step 1 missed it because #15's position table lacks those packed rows; the table now matches a bare by its own src.
- D47 (c): [0693760101] renamed NGC7793P13 -> NGC7793-J235747.9-323457, skip = 1 kept. Before and after: logs/targets18/params_0693760101_{before,after}.txt. Not changed (data): its production summary row and stats/NGC7793P13__0693760101.npz still use the P13 name. Harmless: the gate already holds 0693760101 out (15.100).

BLOCKED, D47 (a), NGC 1313 X-2 in 0405090101, 0693850501, 0693851201: their bare is X-1, all three are packed, and dir/ holds X-1's products. A params-only swap would make preprocess.sh pair X-2 with X-1's products silently. It needs: #41 to unpack; an X-2 region run; Alistair's OK to overwrite dir/'s X-1 products (preprocess -f), or to leave X-1 bare there. Also, NGC1313-X2 is still in new_obs_regions.HOLD_SOURCES although Alistair released it on 18 Nov (15.229 (8)), so under D30 it would not be staged. That is #15's code.

D48 LIST: /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/targets18/d48_review/review_list.tsv, 20 rows (the 16 plus the 4 P13 bares that step 1 mis-tagged). Reasons:
- 7: "QPO test only; NOT in the survey sample" (recorded 30 Oct, 15.185).
- 2: no reason, only a production result line.
- 11: no reason anywhere (P13 x9, M51 ULX-7 x2), recorded on or before the 21 Oct snapshot.
No PNGs: region_review needs the region tool's result and SAS cache, which none of the 20 has (14 packed).

PILOT (D50): not submitted; it waits for Alistair's yes in this terminal. Its regions were rerun under the D47 names (both OK, PNGs drawn); new params file stats/targets18/pilot/pilot_params_d47.conf (preflight 0 errors); the script points to it.

Jobs: none.
Core-h: 0 this step; #18 0.
Files: about +20 (regions, PNGs, list).

SETTLED:
- #18: D47 (b) and (c) done, P13 confirmed already bare, D48 list built; targets18 b75e098 queued; 15.235 (4)-(5).

NEEDS YOU:
1. Alistair: the pilot yes, in this terminal. From /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt: sbatch slurm/submit_targets18_pilot.sh. cosma5/durham, 2 CPUs, 12000M, 4 h, cap 8 core-h; out/err in stats/targets18/pilot/. Recommend yes.
2. D48 PNGs: (i) a params-section mode for region_review, drawn from the loose pn_clean (fov check from event occupancy), about 1 h on the login node, no SAS; or (ii) #41 unpacks and SAS runs. Recommend (i).
3. NGC 1313 X-2 in the 3 processed ObsIDs: overwrite X-1's dir/ products after #41 unpacks, or leave X-1 bare there? Recommend overwrite (D47 (a)), after unpacking.
4. OK to delete my two pilot region folders under the old names (stats/new_obs_regions/0830191401/NGC5194-D201128402010003, NGC5195-D201128402010012)? They would be staged under stale names. Recommend yes.
5. Given the correction, is D48's keep/unskip review still wanted? Recommend keep it as a #17 regions check only.

NEXT:
- On a yes: submit the pilot, wait for its sha256 file, check the pre-registered PASS rule. Nothing started.
