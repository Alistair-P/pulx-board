seq: 10
state: needs-you
date: 2026-11-27T16:14Z
host: login7c
---
#15: both reruns worked. Alistair said yes in the terminal. 0884030101 now uses U002 and 0150280101 uses S001, both with the barycentre correction and frame alignment verified. Their regions and PNGs are done, and pickfix is marked READY.

1. **Deleted (Alistair's OK):**
   - 0884030101's failed-run files: pn_clean.fits, rateEPICPN.fits, pn_merged_evts.ds (558 MB) and its .inputs.
   - 0150280101's files built from S011: prep_events.done, pn_clean.fits, rateEPICPN.fits.
2. **Jobs** (submitted from wt_pickfix at ef7f106; 1 CPU, 18000M = 3 billed CPUs):
   - 12448507, 0884030101: COMPLETED, exit 0, 1:47. U002 chosen (Thin1, about 110 ks ONTIME), no merge. barycen OK. 5,657,800 events aligned; TIMESYS TDB, DE200.
   - 12448508, 0150280101: COMPLETED, exit 0, 0:30. S001 chosen (Thin1, about 7.9 ks), barycen OK. 3,886,591 events aligned; TDB.
3. **Regions** (regfix tool, login node):
   - 0150280101 NGC1313-X2: OK. Its PNG is REVIEW (not_detected); its checks pass.
   - 0884030101 NGC3621-J111815.2-324841: OK. Its PNG is REVIEW (outshines, shrunk<60"); its checks pass.
   - Batch 1 now has regions for all 49 ObsIDs.
4. **Gallery: 54 PNGs** (9 FAIL, 5 REVIEW, 36 PASS, 3 UNCHECKED, 1 HELD).
   - #18 removed its two duplicate tag folders.
   - 3 new NGC1313-X2 PNGs (0405090101, 0693850501, 0693851201) were drawn by another session at 16:07–16:09 with main's tool, which writes no review.json. They show UNCHECKED until redrawn with regfix's region_review.
5. **pickfix ef7f106: READY** (merge after intake15).

Recorded in §15.229 (31) (intake15 72b1959).

Jobs: 12448507 and 12448508, both COMPLETED. Core-h: 0.11 billed. Files: 157,398.

SETTLED:
- The 0884030101 and 0150280101 reruns are verified end to end, with regions and PNGs; pickfix is READY.

NEEDS YOU:
1. Alistair: should "not detected AND outshines" become a hard QA rule? (2 batch 1 targets, as counted earlier; 0884030101 is outshone but detected.)
2. When should --stage write the real staging tables: after the #17 review, or now?

NEXT:
- Apply any QA rule Alistair sets; run --stage when told.
- Merge order for the merge session: targets18 → regfix → intake15 → pickfix.
