seq: 3
state: needs-you
date: 2026-11-26T21:32Z
host: login7c
---
#18 (this is #11's session): did instruction seq 3 (D25): step 1, the target table. Done; step 2 waits for Alistair.

DONE. Branch targets18 off main 1399fad, in wt_mt. logs/targets18/target_table.py reads only #15's intake tables and the params.conf section headers, nothing from any search. It writes target_table.csv, obsid_table.csv and inputs_sha256.txt to /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/targets18/. Test test_targets18 3/0/0, registered. Suite 758/0/3. Commit 43d8ccf, record 15.235. About 45 min of login-node work, 1 thread.

TABLE (MEASURED). 145 ObsIDs, 330 list targets:
- the 138 multi-target ObsIDs;
- 6 processed ObsIDs whose single list target is not their bare section;
- 0693760101 (finding c).
Roles:
- new tags: 170 on 122 ObsIDs. This equals 15.229 (12)'s 170 (114 + 56), so the two counts agree. By stage: tarball 98, packed 41, analysis 15, none 9, prep 7. By #15 batch: 1 45, 2 23, 3 32, 4 12, 5 2, already processed 56.
- bare-planned 89, bare-existing 25, existing tag 1 (ULX8).
- deferred by D1: 45 (the 22 ObsIDs under 17 ks).
Proposals for step 2:
- An existing bare section is kept.
- In a new ObsID a known pulsar takes the bare slot, else the best catalogue a95. This moves M51 ULX-7 into the bare slot of 0830191401.
- Tags are "D" + the DR14 SRCID; ULX8 is kept.

FINDINGS (from records; none acted on):
a. 24 ObsIDs in scope have a bare section with skip = 1. In 16 of them that skipped bare is a list target, so those 16 never reach #19 unless the skip is lifted.
b. 7 known pulsars come out as tags under a skipped bare section that is another source: P13 in 0748390901, 0781800101, 0804670301, 0804670401; NGC 1313 X-2 in 0405090101, 0693850501, 0693851201. ORBITS is keyed by source name, so a tag may still be demodulated; step 2 checks that.
c. 0693760101: [0693760101] is named NGC7793P13 and skip = 1, but its source circle is on NGC 7793 ULX-4 (0.3" from the published position, 2.5' from P13). Unskipped as it stands, stage B would stack ULX-4 with P13.
d. 36 new tags have another list target inside 65". 169 of the 170 have a 4XMM-DR14 detection inside 65". v1.0 masks listed neighbours only.
e. 1 new tag has catalogue counts under 1000.

Jobs: none.
Core-h: 0 this step; #18 0.
Files: not re-read (145,712 earlier today; this step added 3 files in the root tree, plus 2 tracked files).

SETTLED:
- #18 step 1: target table built and recorded; 15.235, commit 43d8ccf on targets18 (not queued: step 2 joins it).

NEEDS YOU:
1. Earlier questions 1 and 2 (count and hold rules for tags; an analysis-only switch) are still with Alistair, and step 2 waits on them.
2. Finding a: should the 16 skipped bare sections that are list targets have their skip lifted for v1.0? Recommend Alistair decides at #17/#19 (an inclusion question). #18 makes no change to them.
3. Finding b: should P13 and NGC 1313 X-2 take the bare slot in those 7 ObsIDs, in place of the skipped other source? Recommend yes (recovery set; ORBITS, OVERRIDES and the gate read the bare). Alistair's call.
4. Finding c: should 0693760101's section be renamed to a ULX-4 name? Recommend yes, before anything unskips it. A params.conf fix, Alistair's call.

NEXT:
- When Alistair has answered: step 2's tooling on targets18, with tests (batch regions for tags, a staging file, flags rows, analysis-only switch if approved), then the queue, then the 2-tag pilot (D26). Nothing started.
