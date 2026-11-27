# PULX status

Updated: 27 Nov 2026 13:50, by the dispatcher

## Overnight (to 27 Nov 09:05)
- **Merges:** 9 branches merged overnight. main is at 6cd77d3, with the suite at 782/0/3. Rule 15 is in
  STANDING_RULES, and the CLAUDE.md fixes are in.
- **a95cut (#37):** golden PASS (coherent 19/19 bit-identical, orbit 4/4). It's merging now, with a
  golden rerun on the merged tree.
- **(d) (#44/#46):** built on stacked46d. Union check PASS (2 of 400 nulls against 3.8 expected).
  Golden PASS, including the new 0791010101 slot. 50.7 core-h. It merges after a95cut and needs
  your ADOPTED approval (item 1).
- **B:** the futility check on batch 1 has started (D36).
- **#15:** the review tools (region_review.py) are on main. Batch 1's regions wait on your naming
  answers (item 2).
- **#18:** target table done: 170 new tags on 122 ObsIDs. Step 2's tooling is starting.
- **#25 and #41:** settled. **#42:** all 8 methods subsections drafted.
- **#38:** hasn't picked up its rebuild instruction (sent 18:01). It needs a nudge (item 4).
- **Files:** about 160,000.

## Waiting at your terminals (cluster policy: your yes, in that window, to the exact command)
All six are approved by Alistair on the board (27 Nov 14:18). Each session shows the command and waits.
- #11: the pilot's sbatch (8 core-h).
- #41: retire wt_p14a and wt_regrev; clear old tmp/tmp* folders (about 37,000 files); retire 9 idle,
  merged worktrees (13,401 files).
- #15: delete 0884030101's 4 failed files, then its sbatch (about 1 core-h).
- #11: overwrite X-1's products with X-2's in 3 NGC 1313 ObsIDs (after #41 unpacks); delete 2 stale
  pilot folders.

## Needs Alistair
1. **Batch 1's #17 review**: the gallery stats/region_review_gallery/ (D58), once #15 has built it.
2. **The cluster policy**: where it comes from (#44 is quoting it). If it's your own setting, you
   can relax it to match D57's tiers.
3. **#30**: starts later, in a COSMA session. 0200670401's section has timing = 0, so as it stands
   that ObsID isn't searched.
4. **#35**: your edit of docs/research_note_frame_times_DRAFT.md, plus a venue.

## For overseer
- **Cluster policy change (27 Nov), reported by #11, #15, #41 and #44:** sessions now run sbatch only on
  Alistair's own yes to the exact command in their terminal, and delete files only on his OK there.
  Board approval isn't enough. This contradicts the "submit" wording in plans 15.2, 38.4 and 44.5.
- **#11 (seq 8, needs-you):** correction: finding (a) was wrong; survey_list() ignores `skip`, so D48's
  premise fails. D47 (b)/(c) done, targets18 b75e098 queued (suite 792/0/3). NGC 1313 X-2 swap blocked
  (packed, X-1's products in dir/; X2 still in HOLD_SOURCES). D48 list: 20 rows, no PNGs
  (stats/targets18/d48_review/review_list.tsv). Pilot waits for Alistair's yes. 5 NEEDS YOU.
- **#15 (seq 5, needs-you):** 31 of batch 1's 43 region runs failed instantly (run_one folder-lookup bug;
  one-line fix proposed). 16 PNGs ready for #17 (0830191401 fails the count check). pickfix 8b03189
  queued NOT READY; doesn't fix 0884030101, whose rerun needs Alistair's yes and delete OK. New:
  0150280101 prepped from a CalClosed exposure; rule proposed. 3 NEEDS YOU.
- **#41 (seq 4, needs-you):** census done (logs/q41/quota_census_20261127.md). Files 169,781. Projected
  peak ~199,700 during a 50-obs batch, over the 195,000 line, unless tmp/tmp* is cleared and the
  testshim leak fixed. D49 checks pass; removal waits for Alistair's OK in the #41 terminal. 4 NEEDS YOU.
- **#42 (seq 10, done):** the three coverage answers and the two ObsIDs' modes and spans are in its
  report, for Alistair. #30 still needs "A1" and the candidate details.
- **#44 (seq 11, idle):** D51 recorded (15.225 (16)); #44 settled. Waits for 44.5; it will ask Alistair
  for the sbatch yes itself (policy change above).
- Silent since their last instructions: merge (last report 23:52; instructions 5 and 6 unread),
  #11 (21:32; instruction 7), #44 (01:04; instruction 9) and #38 (17:06; instruction 3). Alistair
  asked to check those windows at 11:15.
- #41's quota census (asked 11:20): 171,676 files, up about 11,700 overnight.
- (d)'s ADOPTED approval, then tell the merge session (D42).

## Items

| ID | Item | Folder of its conversation | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree | high | active | a95cut merged (df0a6f9, ADOPTED f9f49373); stacked46d trial running | 27 Nov 11:29 |
| 11 | #18 (multi-target), was #11 | wt_mt | medium | needs-you | targets18 b75e098 queued; finding (a) corrected; X-2 swap blocked; pilot needs Alistair's yes | 27 Nov 13:27 |
| 13 | certificate | wt_cert13 | high | waiting | draft builder done; waits for a95cut and (d) | 26 Nov 18:18 |
| 15 | survey intake | wt_intake15 | medium | needs-you | D47 names in; 12/43 regions OK, 31 need a lookup fix; pickfix 8b03189 queued NOT READY; 0884030101 rerun needs Alistair | 27 Nov 13:16 |
| 25 | artefact battery rev3 | root tree | medium | settled | p14a-calib on main (15285f7) | 26 Nov 21:50 |
| 27 | detection policy draft | wt_policy27 | high | waiting | policy27 on main (077a2eb); waits for C1–C4 | 26 Nov 17:30 |
| 37 | a95 cut | root tree | high | waiting | D41 acknowledged; a95cut READY at 6b015e2; waits for 37.3 triggers | 27 Nov 09:05 |
| 38 | red noise | wt_rednoise | high | ? | rebuild instruction 3 (18:01) not yet picked up; needs a nudge | 26 Nov 17:06 |
| 41 | quota and packing | root tree | medium | needs-you | census done (169,781); D49 removal waits for Alistair's OK | 27 Nov 13:41 |
| 42 | methods paper (#43, #45) | root tree | medium | waiting | coverage questions answered; 2 OPEN markers left | 27 Nov 12:55 |
| 44 | long-period part (#44, #46) | wt_longpext | medium | waiting | #44 settled (A closed, D51); waits for 44.5 | 27 Nov 12:53 |
| 47 | β study | - | high | not started | no conversation found | - |

## Plans
The dispatcher may send only these steps, when their conditions are clearly met. Anything else
goes to "For overseer". A step that starts with "trigger:" is set off by another item's report.

- **merge**:
  - `merge.1`: after each merge it reports, send: "Carry on with the next entry in the D42 order
    (a95cut, then stacked46d's trial and golden, stopping before ADOPTED and the fast-forward unless
    DECISIONS.md records Alistair's approval)." Also send the plan steps that merge triggers for
    other items.
  - Any failed suite, conflict it can't resolve, or golden difference: for overseer.
- **11** (now #18):
  - `11.1`: when it reports the target table done, with no new NEEDS YOU, hold until Alistair has
    answered Needs Alistair items 3 and 4. Then for overseer.
- **13**:
  - `13.1`: when it reports the build_cert.py draft committed, with no new NEEDS YOU, hold. It
    waits for a95cut and #46.
  - `13.2`: trigger: a merge report says a95cut AND #46's (d) branch are on main. Then for
    overseer, because the rebase and golden check plan needs checking.
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
  - `37.2`: done (golden PASS; D41). Hold until 37.3's triggers are met.
  - `37.3`: trigger: #38 reports the production red-noise records rebuilt, AND a95cut and rednoise
    are both on main. Send: "D12: rerun a50 --all --thresholds applied and survey_pipeline --list
    on main, using #38's rebuilt records (folder in #38's report). Apply the near-cut rule (48
    injections within ±20% of 0.25); price it first, and ask if it is above 50 core-h billed.
    Report the list changes before rewriting the live list file."
- **38**:
  - `38.2`: sent 18:05 (rednoise is on main, 1399fad).
  - `38.3`: while the rebuild job runs, hold. That report is one of 37.3's triggers.
  - `38.4`: when it reports the production records rebuilt, with folder and hashes, send: "D35:
    Alistair approves validating spans below 17 ks. Take it as a new item, and add a checklist line
    if none exists. Report first, then run. 1. From the record (D1, the floor configuration, and
    the random-field model's validated range of 17–136 ks), say what it needs: which spans (15 and
    10 ks nulls were planned), which arms (coherent Z1/Z3, and whether the orbit arm's M1
    thresholds are validated below 16 ks), and how the thresholds would be fitted and checked.
    2. Price the nulls in billed core-h and files, from measured times. 3. If the price is at most
    150 core-h billed, submit them; otherwise post needs-you with the price. The new thresholds
    are not adopted into v1.0. They come in as a separately registered stage after the tag. Update
    your checklist line, and end with the rule-12 report."
  - A failed rebuild, or a cost above 10 core-h: for overseer.
- **41**:
  - `41.1`: hold idle reports while quota41b is queued.
  - `41.2`: done (D21, 18:05). #41 is settled once its addendum 26cca25 merges; hold its reports.
- **42**:
  - `42.1`: when it reports a subsection committed and the queue entry updated, with no new NEEDS YOU,
    send the next one from this list, in order: "Weighted search statistic", "The blind survey",
    "Sensitivity", "Validation". Say: "Go ahead with <subsection>, on methods42, docs only. Commit,
    update the queue entry, update your checklist line, post your report and wait."
  - When "Validation" is written: for overseer.
  - `42.2`: trigger: a merge report says a95cut is on main. Send: "a95cut is on main. Fill in the
    survey-list cut in 'The blind survey' (a95 < 0.25), commit, update the queue entry and report."
- **44**:
  - `44.1`: its D29 report (scores, analytic check, proposed simulation): for overseer.
  - `44.2`: while the K_eff check or the golden check runs, hold.
  - `44.3`: when it reports (d) queued with the golden check passed, hold. The ADOPTED line goes
    to Alistair, and 13.2 waits for it to merge.
  - `44.5`: trigger: a merge report says (d)'s branch is on main. Send: "D39: Alistair approves your
    confirming simulation for (d), on main's merged code. Write the decision rule of §15.230 (11)
    into the record before any draw, and commit it. Run the pilot (about 3 core-h, 8 draws across both
    octaves, both span bins and both amplitudes) and reprice from it. If the full run is within
    110 core-h billed, submit it; otherwise post needs-you with the price. Report the result
    against the rule. Update your checklist line, and end with the rule-12 report." If B's futility
    check (44.4) is still running, send this after it reports.
  - `44.4`: when it reports (d) queued, send: "D36: B's futility check on batch 1. First write this
    rule into §15.225 and commit it, before looking at any B result: if, even with batch 2's 116
    draws falling as favourably as batch 1's 95% upper bound allows, the combined test couldn't
    reach a GO (McNemar p < 0.05 and at least 0.5 extra detections per 1,000 core-h, under both
    cuts), B closes as NO-GO without batch 2. Then score B's arm on batch 1's 164 records (login
    node, no new runs), apply the rule, and report the counts and the verdict. Keep wt_longpext
    frozen. Update your checklist line, and end with the rule-12 report."
  - Anything else: for overseer. wt_longpext's code stays frozen at 1cbad1c until batch 2 is
    decided.
