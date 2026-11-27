# PULX status

Updated: 27 Nov 2026 19:50, by the dispatcher

## Today (27 Nov, to 18:10)
- **On main:** (d) (stacked46d, 57974c9; ADOPTED ab3e3264 and 9b8ce8b0) and targets18 (6db5e1f).
  Suite 800/0/3.
- **Merge queue:** regfix conflicts with main in region_review.py, so it went back to #15. methods42,
  testshim-tmp, targets18 3b851cc, longpext and figidx46 go first (D64).
- **Review (#17):** D60-D62 recorded and drawn. Gallery: 9 FAIL, 4 REVIEW, 37 PASS, 1 held, 3 unchecked.
  The new detect check also fails 0150280101 X-2 (Needs Alistair 3).
- **Source finding:** the labelled-photon study (studies/pulxsim_27nov) led to D63. #15's answers
  show the survey already weights the whole aperture with the ELLBETA PSF, so D63's gain is in
  neighbour fields only. Stage 1 (design and price, with a neighbour-fields-only option) is with #15.
- **#18:** pilot PASS (0.23 core-h). **#44:** README rows queued (figidx46), D39's rule committed.
  **#41:** 11 worktrees retired. Files 164,367.
- **Overnight:** nothing on Slurm. merge works through D64's order; #15 fixes regfix, then D63 stage
  1; #13 rebases cert13.

## Waiting at your terminals (cluster policy: your yes, in that window, to the exact command)
- **#11**: `sbatch slurm/submit_targets18_ngc1313.sh` from wt_mt
  (/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt; the X-2 swap; 2 CPUs, 16 h, cap 32 core-h,
  about 1-2 expected from the pilot). The pilot passed. Still waiting (report 18:34).
- **#44**: the D39 pilot sbatch from its confirm46d worktree (cap 6 core-h, about 2-4 expected). Then
  the full confirming run, if within 110 core-h.
- **#13**: DEFERRED by Alistair (27 Nov 19:50): no c13 golden until D63 is on main. (The ask was
  `sbatch slurm/submit_golden_c13_{syn,real,orbit,window}.sh` from wt_cert13, about 17.5 billed core-h.)
- Done today: (d) on main; #11's pilot and folders; #15's two reruns; #41's 11 retirements.

## Needs Alistair
1. **Batch 1's #17 review**: the gallery stats/region_review_gallery/ (9 FAIL, 4 REVIEW, 37 PASS, 1 held,
   3 unchecked), with verdicts and light curves. Also #18's 20 D48 PNGs in stats/targets18/d48_review/png/.
2. **D63's scope** (raised 27 Nov). Against the survey's actual weights, the joint fit lowers a95 by
   6-23% beside a neighbour 3x brighter at 5-25", and by about 0 elsewhere. Options: (i) every target
   in v1.0; (ii) only targets with a neighbour within 30", in v1.0; (iii) after the tag, as a
   separately registered stage. #15's stage 1 prices (i) and (ii) and counts the targets affected.
   Overseer's lean: (ii) if it is cheap, otherwise (iii). Decide once stage 1 reports. The overseer
   also offered an independent second look first (OVERSEER.md step 7).
3. **0150280101 NGC1313-X2** fails the new detect check (nothing within 10" in 7.9 ks). It is below
   the 17 ks floor, so v1.0 doesn't search it either way. Recommend leaving it out, with no
   override. Raised 27 Nov.
4. **#30**: starts later, in a COSMA session. 0200670401's section has timing = 0, so as it stands
   that ObsID isn't searched.
5. **#35**: your edit of docs/research_note_frame_times_DRAFT.md, plus a venue.

## For overseer
- **Alistair's answer (27 Nov 19:50, live in the dispatcher session), on #13's golden:** "Let's wait
  until D63 is in then." Read as: no c13 golden now, on cert13 or on the merged tree; the golden runs
  once D63 is on main. Please record it in DECISIONS.md and tell #13 (it is waiting on the board) and
  the merge session (cert13 stays queued and isn't merged until then). His other #13 items, the
  Z1/Z3 max rule and the ADOPTED line, are still open.
- #15 (report 18:40, plan 15.4): regfix merged with main, re-queued at 4a2f274; D63 stage 1 report at
  wt_intake15/logs/intake15/d63_stage1_20261127.md. Scope (i) every target about 210-300 core-h,
  (ii) neighbour fields (>= 0.1x within 30") about 40-100 core-h; also asks Alistair about D63 (2)'s
  fov/area rules (REVIEW below 90% exposed). Needs Alistair 2 can now be decided.
- #13 (report 18:24, plan 13.3): cert13 rebased and queued at 173fd0e, suite 820/0/5, draft --check
  CONSISTENT. NEEDS YOU for Alistair: the golden (above), the Z1/Z3 max(transfer, direct) rule above
  120 ks under (d) (retire or apply; recommends apply), and the survey_pipeline.py ADOPTED line.
- #11 (report 18:34, 11.3): batch 1 tag list and script prepared, not submitted. Asked the overseer to
  record D64 (it is in DECISIONS.md now, 18:10). The swap sbatch is still at Alistair's terminal.
- merge (report 19:30): targets18 5d45f76 on main 6dd6232, suite 802/0/3; regfix next. merge.1's
  wording (D42 order: a95cut, stacked46d) is out of date now that D64 sets the order, so it was not
  sent; the session carries on under instruction 10. Please revise merge.1.
- #41 (report 19:44): tmp/ backlog cleared (50,028 inodes), quota 121,644; addendum 2818a4f queued.
  Held under 41.2.
- #38 hasn't posted its rebuild report (instruction 3, sent 26 Nov 18:01). It did the rebuild (88/88)
  but was interrupted while recording it. Alistair has the paste line. #37's list rerun waits on it.

## Items

| ID | Item | Folder of its conversation | Effort | State | Doing | Last report |
|---|---|---|---|---|---|---|
| merge | merge session | root tree | high | active | targets18 5d45f76 merged (main 6dd6232, 802/0/3); regfix next, then intake15, pickfix | 27 Nov 19:30 |
| 11 | #18 (multi-target), was #11 | wt_mt | medium | needs-you | batch 1 prepared, not run; targets18 on main (6dd6232); swap sbatch at Alistair's terminal; tag runs wait for D63 | 27 Nov 18:34 |
| 13 | certificate | wt_cert13 | high | needs-you | cert13 rebased, queued at 173fd0e (820/0/5); golden sbatch, max rule and ADOPTED with Alistair | 27 Nov 18:24 |
| 15 | survey intake | wt_intake15 | medium | needs-you | regfix re-queued (4a2f274); D63 stage 1 reported, scope with Alistair | 27 Nov 18:40 |
| 25 | artefact battery rev3 | root tree | medium | settled | p14a-calib on main (15285f7) | 26 Nov 21:50 |
| 27 | detection policy draft | wt_policy27 | high | waiting | policy27 on main (077a2eb); waits for C1–C4 | 26 Nov 17:30 |
| 37 | a95 cut | root tree | high | waiting | D41 acknowledged; a95cut READY at 6b015e2; waits for 37.3 triggers | 27 Nov 09:05 |
| 38 | red noise | wt_rednoise | high | ? | rebuild instruction 3 (18:01) not yet picked up; needs a nudge | 26 Nov 17:06 |
| 41 | quota and packing | root tree | medium | settled | tmp/ cleared, quota 121,644; addendum 2818a4f queued | 27 Nov 19:44 |
| 42 | methods paper (#43, #45) | root tree | medium | waiting | coverage questions answered; 2 OPEN markers left | 27 Nov 12:55 |
| 44 | long-period part (#44, #46) | wt_longpext | medium | needs-you | figidx46 queued; told to queue longpext; D39 pilot at Alistair's terminal | 27 Nov 17:53 |
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
  - `11.2`: its swap-job report: if all 6 targets check out as the pilot did, hold; otherwise for
    overseer.
  - `11.3`: its batch-1 tag list and script prepared, not submitted: hold. The tag runs wait for
    D63's stage 1 (15.4) and Alistair's scope decision.
- **13**:
  - `13.1`: when it reports the build_cert.py draft committed, with no new NEEDS YOU, hold. It
    waits for a95cut and #46.
  - `13.2`: sent 27 Nov 16:20.
  - `13.3`: its rebase report: for overseer. The final certificate waits for D63 on main.
- **15**:
  - `15.1`: while downloads, the memory test or the Slurm job are running, hold.
  - `15.2`: when the first Slurm job has finished with every ObsID ok, and the file count is under
    190,000, send: "Record batch 1's outcome in §15.229. Then price batch 2 (up to N = min(50,
    floor((195,000 − used)/500)) ObsIDs) the same way. If it needs XSA downloads, list them under
    NEEDS YOU and don't download them. If it is at most 50 core-h billed and its file projection
    stays under 194,000, prepare the job for the ObsIDs that need no download (D10), and ask
    Alistair for his yes in your terminal (D59)."
  - Any failed ObsID, a price over 50 core-h, or a file count over 190,000: for overseer.
  - `15.3`: when its report answers instruction 12 (items 1-4), with no NEEDS YOU beyond the two
    reruns, send: "D63 (Alistair, 27 Nov; read DECISIONS.md D63 in full): v1.0 changes how target
    photons are selected and weighted. (1) The spatial factor p in w = p·g(E)^β comes from a joint fit
    of the target, its catalogued neighbours within about 2' and the background: fixed PSF shapes at
    fixed positions, amplitudes free (EM on the photons, like emldetect's multi-source fit). p is then
    the photon's fitted target probability, three-way. Extraction goes out to 60", with no neighbour
    masks. g(E)^β is unchanged. (2) Exposure-aware areas everywhere; the fov check tests the timing
    and background circles only. (3) An attribution check where a fitted neighbour lies within 30".
    Stage 1 is design and price only; change no code. Building on your answers to 12/4a, report:
    where selection and p are computed now (modules, functions); which hashed v1.0 modules and inputs
    change; what must be redone (golden, ADOPTED lines, #38's red-noise records, #37's a50 and list,
    #13's certificate, batch-1 regions and staging, tests); the PSF model to use (the CCF's, by
    off-axis angle and energy); where (3) belongs (likely post_search); the implementation split
    between the region tool and the search code; and the validation plan, written as a pre-registered
    rule: fake pulsars injected into real batch-1 event files at the target positions, evaluated only
    at the injected trial as a50 does (blinding rule 1), current p against D63's p, plus a null check
    against chi2_2. Price every step in billed core-h and files. The overseer's simulator is in
    ~/pulx-board/studies/pulxsim_27nov/ (read its README first). Reuse its EM fit (em, fit_weights)
    and its scenarios as test cases where useful. Never run it inside ~/pulx-board: a changed file
    there stops every session's board sync. Post the report and wait. Update your checklist line,
    and end with the rule-12 report."
    (Sent 27 Nov 18:10 as instruction 13, amended for #15's answers, with the regfix fix first.)
  - `15.4`: its regfix re-queue report, with no new NEEDS YOU: hold. Its D63 design report: for
    overseer.
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
    are both on main, AND a merge report says D63's weights are on main (D63 changes a50, so it is
    run once, after D63). Send: "D12: rerun a50 --all --thresholds applied and survey_pipeline --list
    on main, using #38's rebuilt records (folder in #38's report). Apply the near-cut rule (48
    injections within ±20% of 0.25); price it first, and ask if it is above 50 core-h billed.
    Report the list changes before rewriting the live list file."
- **38**:
  - `38.2`: sent 18:05 (rednoise is on main, 1399fad).
  - `38.3`: while the rebuild job runs, hold. That report is one of 37.3's triggers.
  - `38.4`: hold until a merge report says D63's weights are on main (the records and nulls depend
    on the weights); then for overseer, who sends the rebuild for D63 together with this text: "D35:
    Alistair approves validating spans below 17 ks. Take it as a new item, and add a checklist line
    if none exists. Report first, then run. 1. From the record (D1, the floor configuration, and
    the random-field model's validated range of 17–136 ks), say what it needs: which spans (15 and
    10 ks nulls were planned), which arms (coherent Z1/Z3, and whether the orbit arm's M1
    thresholds are validated below 16 ks), and how the thresholds would be fitted and checked.
    2. Price the nulls in billed core-h and files, from measured times. 3. If the price is at most
    150 core-h billed, prepare the job and ask Alistair for his yes in your terminal (D59); otherwise
    post needs-you with the price. The new thresholds
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
  - `44.5`: sent 27 Nov 16:20. Its reports while the pilot or full run go: hold. Results: for overseer
    (who checks whether D63's weights could change the conclusion).
    Text sent: "D39: Alistair approves your
    confirming simulation for (d), on main's merged code. Write the decision rule of §15.230 (11)
    into the record before any draw, and commit it. Run the pilot (about 3 core-h, 8 draws across both
    octaves, both span bins and both amplitudes) and reprice from it. Each sbatch needs Alistair's
    yes in your terminal (D59). If the full run is within 110 core-h billed, ask him for it there;
    otherwise post needs-you with the price. Report the result
    against the rule. Update your checklist line, and end with the rule-12 report." If B's futility
    check (44.4) is still running, send this after it reports.
  - `44.6`: its report that longpext is queued: hold.
  - `44.4`: done (B NO-GO). Text kept for the record: "D36: B's futility check on batch 1. First write this
    rule into §15.225 and commit it, before looking at any B result: if, even with batch 2's 116
    draws falling as favourably as batch 1's 95% upper bound allows, the combined test couldn't
    reach a GO (McNemar p < 0.05 and at least 0.5 extra detections per 1,000 core-h, under both
    cuts), B closes as NO-GO without batch 2. Then score B's arm on batch 1's 164 records (login
    node, no new runs), apply the rule, and report the counts and the verdict. Keep wt_longpext
    frozen. Update your checklist line, and end with the rule-12 report."
  - Anything else: for overseer. wt_longpext's code stays frozen at 1cbad1c until batch 2 is
    decided.
