seq: 3
state: needs-you
date: 2026-11-27T09:12Z
host: login7c
---
#15 (board seq 3): answered the second-array question, wrote region_review.py's summary entry, and diagnosed 0884030101 with a proposed fix (not applied). Batch 1's region run is held.

1. **Second array:** it was submitted and finished. Job 12436619 ran the 12 downloaded ObsIDs, submitted 26 Nov 18:40 UTC, every task COMPLETED (3.0–19.8 min each). It is recorded in §15.229 (23) and report 20261126d; report e left it out, my error. All 14 downloads are in INTAKE.md's batch 1 table, with source, UTC date, bytes and sha256. 11 of the 12 reached prep; the 12th is 0884030101.
2. **region_review.py's summary entry:** written as §15.229 (25)(a), citing D37 and the merge 6cd77d3. It covers what the tool draws, the override rows and their refusal rules, the three checks, how `--stage` applies overrides, and the tests. Because it is on intake15, I queued intake15 (0ada393). There are no manifest modules and no pipeline code on it; test_intake15 passes 16/0/0.
3. **D43, 0884030101 (proposed, not applied; §15.229 (25)(c)):**
   - *What goes wrong:* epproc wrote two pn exposures.
     - S001 is a 1.53 ks exposure with a broken header: TSTART = 0, LIVETIME = 0, ONTIME = 0, and no EXPOSU tables. Its events and GTIs are normal.
     - U002 is the real observation: 97.6 ks LIVETIME, same filter, mode and pointing.
     - `pick_pn_events` skips the zero live times and falls back to TSTOP − TSTART = 803,769 ks, so the 1.5 ks file ranks as "longest". The merge's verification correctly rejected the merge. The fallback then took S001, and barycen stopped on its missing TSTART.
   - *The fix (pick_pn_events.py only):*
     - Header times count only if TSTART > 0; otherwise the time extent comes from the GTI tables.
     - After LIVETIME, ONTIME and EXPOSURE, rank by GTI live time before the header span.
     - Optional, for Alistair: never pick as primary an exposure with no EXPOSU tables.
     - Result here: U002 is the primary, and S001 is skipped by the 5 ks gate.
   - *What it could affect:* only observations with ≥ 2 pn exposures where one exposure has no positive live time or TSTART ≤ 0. Any file with a positive LIVETIME ranks as now. In batch 1 the only other multi-exposure ObsID is 0803990301, ranked on LIVETIME, so it is unchanged.
   - *Tests:*
     - New synthetic cases in test_pick_pn_events.
     - A header-only replay, old vs new, on the multi-exposure ObsIDs named in the prep logs and §15.84 (a list, no scan); only 0884030101 may change.
     - Rerun 0884030101's prep as one Slurm task, about 1 billed core-h.
     - It is not a manifest module, so no golden check is needed.
4. **Batch 1 regions:** held until the board relays Alistair's answers.

Jobs: none running.
Core-h: 0 this step (header reads only); batch 1 total 19.8 billed.
Files: 171,676 (lfs quota; the rise since 160,001 is from other sessions, not from #15).

SETTLED:
- The second array ran and is recorded; all 14 downloads are in INTAKE.md.
- region_review.py's summary entry is written in §15.229 (25)(a), and intake15 0ada393 is queued so it can reach main.
- 0884030101's cause is found: S001's broken header (TSTART = 0) made it rank as the longest exposure.

NEEDS YOU:
1. D43: approve the pick_pn_events fix as proposed, and say whether the stricter option (never pick a primary with no EXPOSU tables) should be included.
2. X-2 regions and non-PULX naming: already with Alistair. I'm holding the region run.

NEXT:
- Once D43 is approved: build the fix on a branch with tests, run the replay, rerun 0884030101 on Slurm, then queue it.
- Once the naming answers arrive: run batch 1's regions and review PNGs, then tell the board.
