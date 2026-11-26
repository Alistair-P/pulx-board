# PULX status

Updated: 26 Nov 2026 17:35, by the overseer

## Needs Alistair
1. **#46: adopt (b), or keep v1.0's gap above 120 ks?** (#44, 26 Nov; numbers in §15.230 (10)(e).)
   On B's 164 simulated draws above 120 ks, (b) minus no arm is −0.012 in detection fraction
   (95% −0.043 to +0.018, McNemar p = 0.69). (b) finds 2 draws that no arm misses, and misses 4
   that no arm finds. Those 4 are coherent Z1 detections lost to (b)'s +1.71 rise in the Z1
   threshold (Z3 rises only 0.27). Wander draws are identical under every option, and (a) and (c)
   do worse. Adopting (b) costs 40–60 core-h of nulls, a manifest code change and a new golden
   slot, all before #13. Overseer's view: keep the gap.
2. **#44 batch 2** (116 draws, about 270–280 core-h billed, cap 448; above the 135–215 first
   approved). It isn't needed for v1.0. Overseer's view: defer it until after the tag, unless you
   want B for the methods paper.
3. **#18: start it, run by #11's session?** It covers ULX-8 and the 138 multi-target ObsIDs, and
   #19 needs it. #11's session wrote the multi-target code. Overseer's view: yes.
4. **Retire merged worktrees.** wt_mcseed now, with wt_retire.sh. Keep wt_mt while #11's session
   is in use, because its conversation was started there. Overseer's view: yes.
5. **#41: delete archive/q41fix/ (4 folders, 8 files) after quota41b merges.** These are the old
   project tar and sums pairs. #41 has checked that all four are superseded by rebuilt packs with
   matching checksums, and that every old link is now a real file. Overseer's view: yes.
6. **Three CLAUDE.md edits.** (a) #13's cert13 branch changes the "Known gaps" line. (b) The
   stale line saying the golden check doesn't cover the orbit arm (#12 is settled). (c) #42: the
   params.conf note cites summary 7.10 for the timing radius, but it is 7.11. Overseer's view: yes
   to all three. (a) arrives with cert13, and the merge session makes (b) and (c) with its next
   merge.
7. **Merge policy27 to main after methods42?** It's #27's unsigned REV. 3 draft, docs only.
   Overseer's view: yes. It keeps the draft safe on main, and signing is a separate step.
8. **Add rule 15 to STANDING_RULES** with the merge session's next merge, using RULE15.md's text.
   Overseer's view: yes.
9. **#17**: review the recovery sections and batch regions. (Raised before 25 Nov.)
10. **#30**: the A1 candidate details. (Raised before 25 Nov.)
11. **#35**: your edit of the frame-alignment note. (Raised before 25 Nov.)
- Later: #13 will ask you to approve survey_pipeline.py's ADOPTED line after cert13's golden check.
- Optional now: the quota rise check (filemap.sh). The count is 144,000–146,000 and falling.

## For overseer
- #44's answer on what B decides (for Needs Alistair item 2).

## Items

| ID | Item | Folder of its conversation | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree | high | active | finishing quota41b (D17), then rednoise (D18) | 26 Nov 17:25 |
| 11 | MC seeding, multi-target | wt_mt | medium | settled (D8) | waiting on #18 decision | 26 Nov 17:25 |
| 13 | certificate | wt_cert13 | high | active | build_cert.py v1.0 draft (D15); waits for a95cut and #46 | 26 Nov 17:10 |
| 15 | survey intake | wt_intake15 | medium | active | 14 downloads, then Slurm job for 39 ObsIDs (D9, D10) | 26 Nov 17:10 |
| 25 | artefact battery rev3 | root tree | medium | waiting | p14a-calib (5f9a009) queued; needs a trial merge | 26 Nov 17:11 |
| 27 | detection policy draft | wt_policy27 | high | waiting | REV. 3 at 101b486, unchanged (D16); waits for C1–C4 | 26 Nov 17:24 |
| 37 | a95 cut | root tree | high | active | a95cut golden check (D11) | 26 Nov 17:12 |
| 38 | red noise | wt_rednoise | high | waiting | queued at 8828681; holds until rednoise is on main | 26 Nov 17:06 |
| 41 | quota and packing | root tree | medium | waiting | quota41b queued at dfa0244 | 26 Nov 17:12 |
| 42 | methods paper (#43, #45) | root tree | medium | active | writing "Weighted search statistic" (4 of 8 done) | 26 Nov 17:25 |
| 44 | long-period part (#44, #46) | wt_longpext | medium | waiting | #46 scored; numbers requested; batch 2 held | 26 Nov 17:15 |
| 47 | β study | - | high | not started | no conversation found | - |

## Plans
The dispatcher may send only these steps, when their conditions are clearly met. Anything else
goes to "For overseer". A step that starts with "trigger:" is set off by another item's report.

- **merge**:
  - `merge.1`: after each merge it reports, send: "Carry on with the next entry in the D18 order."
    Also send the plan steps that merge triggers for other items.
  - Any failed suite, conflict it can't resolve, or golden difference: for overseer.
- **11**:
  - `11.1`: hold idle reports. #18 and the worktrees are with Alistair.
- **13**:
  - `13.1`: when it reports the build_cert.py draft committed, with no new NEEDS YOU, hold. It
    waits for a95cut and #46.
  - `13.2`: trigger: a merge report says a95cut AND #46's outcome are on main (or #46 is closed as
    "keep the gap"). Then for overseer, because the rebase and golden check plan needs checking.
- **15**:
  - `15.1`: while downloads, the memory test or the Slurm job are running, hold.
  - `15.2`: when the first Slurm job has finished with every ObsID ok, and the file count is under
    190,000, send: "Record batch 1's outcome in §15.229. Then price batch 2 (up to N = min(50,
    floor((195,000 − used)/500)) ObsIDs) the same way. If it needs XSA downloads, list them under
    NEEDS YOU and don't download them. If it is at most 50 core-h billed and its file projection
    stays under 194,000, submit the ObsIDs that need no download (D10), and report."
  - Any failed ObsID, a price over 50 core-h, or a file count over 190,000: for overseer.
- **25**:
  - `25.1`: hold idle reports while p14a-calib is queued.
  - `25.2`: trigger: a merge report says p14a-calib is on main. Send: "p14a-calib is on main.
    Check the merged-tree suite result in the merge record, set your checklist line to settled,
    post a done report and stop."
- **27**:
  - `27.1`: hold. It waits for C1–C4, or for #19 to freeze N.
- **37**:
  - `37.1`: while the golden jobs run, hold.
  - `37.2`: if both golden comparisons are bit-identical and a95cut is marked ready, hold.
    Anything else: for overseer.
  - `37.3`: trigger: #38 reports the production red-noise records rebuilt, AND a95cut and rednoise
    are both on main. Send: "D12: rerun a50 --all --thresholds applied and survey_pipeline --list
    on main, using #38's rebuilt records (folder in #38's report). Apply the near-cut rule (48
    injections within ±20% of 0.25); price it first, and ask if it is above 50 core-h billed.
    Report the list changes before rewriting the live list file."
- **38**:
  - `38.1`: hold idle reports while rednoise is queued.
  - `38.2`: trigger: a merge report says rednoise is on main. Send: "rednoise is on main (D12).
    Rebuild the production red-noise records from main (a50.py --build-red --all, about 3 core-h
    billed, as priced from job 12379547). Record the output folder and the hashes, and post your
    report. Don't rerun a50 or --list; #37 does that next."
- **41**:
  - `41.1`: hold idle reports while quota41b is queued.
  - `41.2`: trigger: a merge report says quota41b is on main. If DECISIONS.md records Alistair
    approving the archive/q41fix/ deletion, send: "quota41b is on main. Check each folder in
    archive/q41fix/ is superseded by a rebuilt pack with a matching checksum, then delete it,
    record it, and report." If not, hold.
- **42**:
  - `42.1`: when it reports a subsection committed and the queue entry updated, with no new NEEDS YOU,
    send the next one from this list, in order: "Weighted search statistic", "The blind survey",
    "Sensitivity", "Validation". Say: "Go ahead with <subsection>, on methods42, docs only. Commit,
    update the queue entry, update your checklist line, post your report and wait."
  - When all five are written: for overseer.
- **44**:
  - `44.1`: when it posts the #46 numbers, for overseer.
  - `44.2`: hold anything else until Alistair decides #46 and batch 2.
