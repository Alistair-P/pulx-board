# PULX status

Updated: 26 Nov 2026 18:40, by the overseer

## Needs Alistair
1. (Decided: B gets a futility check on batch 1 after (d) is queued, D36.) **B (#44 batch 2)** was: decide whether to switch on the long-period orbit part for spans above
   80 ks, on one 80 ks window each (134 targets on 80 ObsIDs). It's a post-tag stage by design and
   can't change v1.0. Batch 2 costs about 270–280 core-h billed (cap 448). A GO would add 120–390
   core-h of survey compute after the tag. C1, the same idea at 40–57.5 ks, found no gain.
   Options: run now, defer to after the tag (wt_longpext frozen until then), or drop. Overseer's
   view: defer, or let #44 propose a futility check on batch 1 first.
2. **#46's confirming simulation** (#44, §15.230 (11)). 224 draws: binaries at 1.5, 2 and 3 × a50, and
   wander at 3 rad. A pilot of about 3 core-h, then 55–110 core-h billed. Its rule is fixed: at
   2 × a50, (d) pays if (d)-only beats no-arm-only with McNemar p < 0.05. The model predicts 0.80
   against 0.36. (d) is adopted either way (D33, D38). This would confirm the binary gain. Overseer's
   view: yes, run on (d)'s merged code, so it also tests the implementation end to end.
3. **#17**: your review of the flags table for each batch, between regions and run_analysis. #15 is
   building one review PNG per observation and a region override script (D37). Batch 1 comes
   after its last 12 ObsIDs are prepped.
4. **#30**: the A1 candidate details. (Raised before 25 Nov.) #42 is reading what's needed.
5. **#35**: your edit of the frame-alignment note. (Raised before 25 Nov.)
- Later: #13 will ask you to approve survey_pipeline.py's ADOPTED line after cert13's golden check.
- Optional now: the quota rise check (filemap.sh). The count is 144,000–146,000 and falling.

## For overseer

## Items

| ID | Item | Folder of its conversation | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree | high | active | intake15 merged (6b0b68f); now p14a-calib; D22/D24 confirmed by Alistair in its terminal | 26 Nov 18:25 |
| 11 | #18 (multi-target), was #11 | wt_mt | medium | active | #18 step 1, target table (D25); wt_mcseed retired | 26 Nov 18:02 |
| 13 | certificate | wt_cert13 | high | waiting | v1.0 draft builder done (baa7e20, suite 751/0/5); waits for a95cut and #46 | 26 Nov 18:18 |
| 15 | survey intake | wt_intake15 | medium | running | second array after downloads; then review PNGs and override tool (D37) | 26 Nov 18:30 |
| 25 | artefact battery rev3 | root tree | medium | waiting | p14a-calib (5f9a009) queued; needs a trial merge | 26 Nov 17:11 |
| 27 | detection policy draft | wt_policy27 | high | waiting | REV. 3 at 101b486, unchanged (D16); waits for C1–C4 | 26 Nov 17:30 |
| 37 | a95 cut | root tree | high | running | golden jobs 12436028/29/30 (D11) | 26 Nov 17:51 |
| 38 | red noise | wt_rednoise | high | active | rebuilding production red-noise records (D12, 38.2 sent 18:05) | 26 Nov 17:06 |
| 41 | quota and packing | root tree | medium | waiting | quota41b on main (818b683); deletion waits for Alistair | 26 Nov 17:12 |
| 42 | methods paper (#43, #45) | root tree | medium | active | "Weighted search statistic" done (4ff1e7c, 5 of 8); writing "The blind survey" | 26 Nov 17:30 |
| 44 | long-period part (#44, #46) | wt_longpext | medium | waiting | #46 scored; batch-2 answer posted; batch 2 held | 26 Nov 17:30 |
| 47 | β study | - | high | not started | no conversation found | - |

## Plans
The dispatcher may send only these steps, when their conditions are clearly met. Anything else
goes to "For overseer". A step that starts with "trigger:" is set off by another item's report.

- **merge**:
  - `merge.1`: after each merge it reports, send: "Carry on with the next entry in the D18 order."
    Also send the plan steps that merge triggers for other items.
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
  - `37.2`: if both golden comparisons are bit-identical and a95cut is marked ready, hold.
    Anything else: for overseer.
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
  - `44.4`: when it reports (d) queued, send: "D36: B's futility check on batch 1. First write this
    rule into §15.225 and commit it, before looking at any B result: if, even with batch 2's 116
    draws falling as favourably as batch 1's 95% upper bound allows, the combined test couldn't
    reach a GO (McNemar p < 0.05 and at least 0.5 extra detections per 1,000 core-h, under both
    cuts), B closes as NO-GO without batch 2. Then score B's arm on batch 1's 164 records (login
    node, no new runs), apply the rule, and report the counts and the verdict. Keep wt_longpext
    frozen. Update your checklist line, and end with the rule-12 report."
  - Anything else: for overseer. wt_longpext's code stays frozen at 1cbad1c until batch 2 is
    decided.
