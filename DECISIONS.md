# Decisions

Each entry has a number, a date, who decided, the decision and the reason. Instructions cite
entries by number, for example "D3". Never rewrite an entry; add a new one that replaces it.

## Alistair's answers
Alistair writes answers to "Needs Alistair" items here, or tells the overseer, which records them.
The next overseer wake acts on them.

- 26 Nov 17:06: keep #38's CLAUDE.md line under rule 9 (recorded as D6).
- 26 Nov 17:55: #18 yes, to #11's session (D19). Retire the merged worktrees (D20). Delete
  archive/q41fix/ (D21). The three CLAUDE.md edits (D22). Merge policy27 after methods42 (D23).
  Add rule 15 to STANDING_RULES (D24). #46 and #44 batch 2 are still open; Alistair asked for more
  detail.
- 26 Nov 18:18: Q4 yes (D28). Inclusion works by data a95 after download (D27). Leaning towards
  option (d) for #46, a stacked arm on a 120 ks window, and asking whether a harder test should
  come first. #46 is not yet decided.
- 26 Nov 18:28: Q3 yes (D30). The union (K_eff) check for (d) is approved, 20–40 core-h (D31). No
  stacked calibration for longer segments, so (a), (b) and (c) are out; the choice is between (d)
  and keeping the gap (D32). Alistair leans towards including (d) as justifiable.
- 27 Nov 16:59: "go ahead with the changes" after the labelled-photon study (D63). Read as v1.0,
  since the search layer freezes at the tag (rule 11).
- 27 Nov 16:28: yes to the QA rule (D62). Asked whether approvals can be given remotely, and for ideas
  to improve the source finding.
- 27 Nov about 16:00, in the terminals: yes to (d)'s ADOPTED lines and fast-forward (merge, main
  57974c9); yes to #11's pilot (job 12448511) and the 2 stale folders; yes to #41's 11 retirements and
  the tmp/ clean-up after testshim-tmp.
- 27 Nov 16:08: #17 review of five gallery PNGs (D61). Asked why a neighbour that outshines a target
  should matter (M82 X-2 was found blended with X-1), and whether anything corrects for off-axis sources.
- 27 Nov 16:03: "happy with all decisions": exclude 0400560301's target for this epoch (D60); (d)'s
  merge goes ahead once he says yes in the merge terminal.
- 27 Nov 14:21: he approves every Slurm job himself, in the terminal (D59).
- 27 Nov 14:18: yes to all six terminal asks (each still needs his yes in its own terminal). Job
  tiers (D57). A flat gallery of review PNGs, and a readable flaring panel (D58).
- 27 Nov 12:48: (d)'s ADOPTED lines approved on conditions (D46). Bare slots, names and the
  0693760101 rename (D47). The 16 skipped targets go to a review list (D48). Retire wt_p14a and
  wt_regrev (D49). #18's pilot yes (D50; his yes is also needed in #11's terminal). Option A closed
  (D51). #30's candidate details were given to the overseer in chat; they're kept off the board.
- 26 Nov 18:52: the overseer's morning wake moves to 09:00 (D40).
- 26 Nov 18:50: run #44's confirming simulation on (d)'s merged code (D39).
- 26 Nov 18:45: B futility check after (d) (D36). Review PNGs and a region override tool for #17
  (D37). #30 waits for #42's description.
- 26 Nov 18:41: Alistair confirmed D24 and D22 (b), (c) in the merge terminal.
- 26 Nov 18:35: the leaner schedule (D34). Run the nulls below 17 ks (D35). Go with (d) (D33).

## Standing decisions
- **D1** (≈19 Nov, Alistair): targets with spans under 17 ks are deferred to a later stage with
  15 and 10 ks nulls, not dropped. Reason: no validated thresholds below 17 ks.
- **D2** (Alistair): the long-period part is on in v1.0 (+3.9% compute). Extending it down to
  48–57.5 ks was measured and rejected.
- **D3** (Alistair): the Z1 common factor R = 1.231 (+0.44 in Z²) is adopted (z1-adopt).
- **D4** (25 Nov, Alistair, confirmed by #44): finish #44's batch 1 (about 110 core-h billed, cap
  200). Hold batch 2 until #46 is decided. Reason: #46's rule needs all 164 draws, and B isn't on
  the v1.0 path.
- **D5** (25 Nov, Alistair, confirmed by #15):
  - seeding happens per batch, just before prep;
  - SMC X-3 stays out;
  - 0890710101 leaves the fixed recovery set, and recovery epochs must pass survey QA (§15.229 (20));
  - the four NGC 2403 prep folders are kept for batch 4;
  - 0831790101's prep folder is deleted;
  - 0890710101 stays as a margin-band observation.
- **D6** (26 Nov, Alistair): keep the line #38 added to CLAUDE.md under rule 9 on 25 Nov, saying
  where a50 takes its sensitivity folder from. Reason: it documents #38's new a50 safeguard.
- **D7** (26 Nov, overseer): #38 holds after queueing. Once rednoise is on main, the overseer
  decides whether #38 or #37 rebuilds the production red-noise records and reruns a50 and the
  list. Reason: both had it in their plans, and it must be done once.
- **D8** (26 Nov, overseer): #11 is settled. The multi-target code and both checks are on main.
  ULX-8 (0830191601) goes to #18.
- **D9** (25 Nov, Alistair, via his terminal; confirmed by #15): download batch 1's 14 ODFs from
  the XSA, each checked for read-back and completeness, with its source, date and sha256 in
  INTAKE.md. From batch 2, seeding and prep run as Slurm jobs.
- **D10** (26 Nov, overseer): batch 1's 25 unprepped ObsIDs go into the first Slurm job with the 14
  downloads, not back onto the login node. A submission of up to 50 core-h billed needs no
  further approval, if the file projection stays under run_batch.py's 194,000 stop.
- **D11** (26 Nov, overseer; Alistair approved it on 19 Nov): #37 runs a95cut's golden check now
  that mcseed is on main (cap 42.3 core-h, expected about 11.5).
- **D12** (26 Nov, overseer; replaces D7): once rednoise is on main, #38 rebuilds the production
  red-noise records (about 3 core-h). Then #37 reruns a50 and --list on them, once a95cut is also
  on main, and reports before rewriting the live list. Reason: each step goes to the session
  that knows that code.
- **D13** (26 Nov, overseer; WITHDRAWN by D16): the (k) catch rate is 85.8–95.6%, from
  24 distinct lattice lines (§15.228 (11)). It replaces S5's 84–95.6%.
- **D14** (26 Nov, overseer): rule 15e clarified. Simulations, injections, nulls and tests may be
  reported with numbers. Only results of searches on real data are barred.
- **D15** (26 Nov, overseer): #13 writes the v1.0 build_cert.py draft now (validated = false, no
  compute), then waits for a95cut and #46.
- **D16** (26 Nov, overseer): D13 is withdrawn. The detection policy's content is Alistair's
  (POLICY.md), and his 25 Nov choice of 84–95.6% is in the record: 84% counts the extension's 21
  lines, 85.8% all 24, and 95.6% the 82 forgeries (§15.228 (11)). The draft keeps his wording,
  and O10 spells out both lattice-line figures. #27 was right to refuse.
- **D17** (26 Nov, overseer): the merge session finishes quota41b from its passing trial
  (9a4d34c, suite 744/0/3) without rerunning the suite. The suite ran on exactly that tree.
- **D18** (26 Nov, overseer): the merge order after quota41b is rednoise, intake15, p14a-calib,
  longpext, then methods42. a95cut follows once #37 marks it ready, and policy27 if Alistair
  approves. Reason: rednoise is on the v1.0 path (#38's rebuild, then #37's list rerun), and its
  merged-tree suite has already passed on main 2513b12.
- **D19** (26 Nov, Alistair): start #18 (ULX-8 and the 138 multi-target ObsIDs), run by #11's
  session. It reports first, with scope, plan and price, and changes nothing until then.
- **D20** (26 Nov, Alistair): retire wt_mcseed now. Retire wt_mt once #11's session no longer
  needs it, because its conversation lives there. No --force; check clean, merged, no ignored
  files, no job and no session in it first.
- **D21** (26 Nov, Alistair): delete archive/q41fix/ (4 folders, 8 files) now that quota41b is on
  main (818b683). #41's check of 26 Nov shows all four superseded.
- **D22** (26 Nov, Alistair): three CLAUDE.md edits. (a) #13's "Known gaps" change arrives with
  cert13. (b) Fix the stale line saying the golden check doesn't cover the orbit arm. (c) The
  params.conf note's timing-radius pointer becomes summary 7.11, not 7.10. The merge session
  makes (b) and (c) with its next merge. (#38's D6 line arrives with rednoise.)
- **D23** (26 Nov, Alistair): merge policy27 (#27's unsigned REV. 3 draft, docs only) after
  methods42.
- **D24** (26 Nov, Alistair): the merge session adds rule 15 to docs/STANDING_RULES.md with its
  next merge, using RULE15.md's text from "15." to the end, as it now stands.

- **D25** (26 Nov, overseer): #18 works in wt_mt, on a new branch targets18 off main. That saves
  287 new links, and the session's conversation lives there. Its step 1, the target table (about
  1 h on the login node, no compute), starts now.
- **D26** (26 Nov, overseer): #18's 2-tag pilot (about 6–10 core-h) is approved, once its tooling
  is queued and Alistair has answered the tag QA and analysis-only questions. Full runs (160–490
  core-h over all batches) need Alistair's approval per batch.

- **D27** (26 Nov, Alistair): inclusion is decided by each target's data a95, not the catalogue
  estimate. The catalogue a95 chooses what to download and prep, including a margin band just
  outside 0.25. After prep, a95 is recalculated from the data, and a target is searched only if
  its data a95 meets the cut. The same holds for #18's extra targets ([obsid:tag]).
- **D28** (26 Nov, Alistair): #18's extra targets stop after run_analysis (a new analysis-only
  switch), so no production-search output exists for them before the v1.0 certificate. The P30
  pilot's existing search outputs stay unopened (rule 1).

- **D29** (26 Nov, overseer; Alistair asked whether a harder test should come first): #44 scores
  option (d) on the 164 draws under R0 and as an add-on beside R1 (under 0.3 core-h, post-hoc),
  makes an analytic comparison of no arm and (d) for signals that lose coherence, and proposes
  and prices a small confirming simulation. #46 stays undecided until Alistair has seen these.

- **D30** (26 Nov, Alistair): #18's extra targets get the same QA as bare targets, including
  MIN_COUNTS = 1000 and HOLD_SOURCES, as well as the data-a95 inclusion of D27.
- **D31** (26 Nov, Alistair): #44 runs the union (K_eff) check for option (d), 20–40 core-h billed,
  priced first, after the D29 scoring.
- **D32** (26 Nov, Alistair): no new stacked calibration for longer segments above 120 ks. So (a),
  (b) and (c) are out. #46's choice is between (d), a stacked arm on one 120 ks window with the
  existing calibration, and keeping the gap. Alistair leans towards including (d).

- **D33** (26 Nov, Alistair): #46 adopts option (d), recorded as a post-hoc option. That's a stacked
  arm at M = 4 on one 120 ks window of each observation above 120 ks: the first or last 120 ks,
  whichever the flare monitor scores better, fixed before any search. It uses the existing
  120 ks calibration. Reasons: a robust arm for the 63 longest targets at no new calibration cost,
  and the orbit arm already windows long observations (best 128 ks). The budgeting (R0, or the
  add-on beside R1) is whichever scores better on the 164 draws. If both have 95% intervals
  entirely below zero against no arm, it comes back to Alistair. It's implemented on a new
  branch off main, not in wt_longpext, with a golden slot above 120 ks, before #13. The ADOPTED
  line needs Alistair.
- **D34** (26 Nov, Alistair): to save his usage, the overseer wakes at 12:00 and 18:00 only,
  without "ultrathink" on routine wakes, and the dispatcher runs every two hours from 07:45 to
  21:45.
- **D35** (26 Nov, Alistair): validate spans below 17 ks now, with the 15 and 10 ks nulls (the
  record's estimate is 50–150 core-h; approved up to 150 core-h billed, priced first). #38's session
  takes it after its records rebuild. The new thresholds come into the survey only as a
  separately registered stage after the v1.0 tag, not in v1.0.

- **D36** (26 Nov, Alistair): B gets a futility check on batch 1's existing 164 draws once (d) is
  queued, with the rule written into the record before any look. Rule: if, even with batch 2's 116
  draws falling as favourably as batch 1's 95% upper bound allows, the combined test couldn't reach
  a GO (McNemar p < 0.05 and at least 0.5 extra detections per 1,000 core-h, under both cuts), B
  closes as NO-GO without batch 2. Otherwise batch 2 runs after the tag, with wt_longpext frozen
  until then.
- **D37** (26 Nov, Alistair): for his #17 review, one PNG per observation (and per extra target)
  showing all regions and the surrounding diffuse emission, plus a script to enter corrected
  region values. The corrections go in an override layer that the staging step applies over the
  automated regions, keeping both on record. #15 builds both, with support for #18's tags. #18
  reuses them. PNGs stay on COSMA, in the region cache that is packed after review, never on the
  board.

- **D38** (26 Nov, overseer, applying D33): (d) uses the add-on budgeting beside R1. On the 164
  draws at a50 it was identical to no arm (40 vs 40, 0 discordant), while R0 was worse (−0.024,
  95% −0.049 to −0.006). Analytic (§15.230 (11)): no gain for steady pulsars or wander up to 1 rad,
  but strong-Doppler binaries reach 50%/95% at 1.63/3.02 × a50 against no arm's 3.25/13.5. The
  record supports wander only up to about 0.3 rad, so the case rests on binaries. Condition: the
  +0.71 applies only above 120 ks.

- **D39** (26 Nov, Alistair): run #44's confirming simulation for (d) once (d) is on main, using the
  merged code, so it also tests the implementation end to end. Approved: a pilot of about 3
  core-h, then 55–110 core-h billed, with the decision rule of §15.230 (11) fixed before any draw.
  Ask again if the pilot's price comes out above 110.

- **D40** (26 Nov, Alistair): the overseer wakes at 09:00 and 18:00, replacing 12:00, so the morning
  pass is done when he starts work. The 09:00 wake writes an "Overnight" summary and sends one push
  notification.

- **D41** (27 Nov, overseer): #37 doesn't rerun a95cut's golden. The merge session reruns it on the
  exact merged tree under its own rule, priced first.
- **D42** (27 Nov, overseer): merge order a95cut, then stacked46d. a95cut uses the ADOPTED line
  f9f49373 approved on 18 Nov, if the live hash matches. stacked46d gets a trial merge and a golden
  check on the merged tree, but no ADOPTED line or fast-forward until Alistair approves its lines.
  Reason: both change survey_pipeline.py, so the second needs a combined hash, and adopting
  a95cut's already-approved hash first keeps one approval cycle.
- **D43** (27 Nov, overseer): #15 proposes a fix for 0884030101's pn-exposure selection failure but
  doesn't apply it yet.

- **D44** (27 Nov, overseer): #15 applies its pick_pn_events.py fix for 0884030101 (a bug fix in
  prep, not the search layer), with tests and a header-only replay. The stricter no-EXPOSU option
  goes in only if the replay shows it changes no other ObsID.

- **D45** (27 Nov, overseer): #44 adds the validation figure for B's futility result (B is NO-GO,
  §15.225 (15)(d); batch 2 isn't run, which saves about 270–280 core-h). Option A goes to Alistair.

- **D46** (27 Nov, Alistair): approve the ADOPTED lines for stacked46d, option (d): octave_thresholds.py,
  and survey_pipeline.py at its combined hash on top of a95cut. Conditions: the merge session's
  golden on the merged tree passes as predicted (19/19 coherent bit-identical, orbit identical,
  the 0791010101 slot identical to stacked46d's own run), and the live hashes match. If anything
  differs, it comes back to Alistair.
- **D47** (27 Nov, Alistair):
  - (a) known pulsars take the bare slot in their ObsIDs: P13, and NGC 1313 X-2 (X-1 becomes a tag
    there);
  - (b) a section's name is the host plus the literature name where the survey list gives one
    (e.g. HolmbergIX-X1), otherwise the host plus the Jname (e.g. UGC05336-J095753.3+690348). The
    name is the stacking key and never changes between epochs. The DR14 ID may stay as the
    internal [obsid:tag] key;
  - (c) rename 0693760101's section (named NGC7793P13, but its circle is on NGC 7793 ULX-4) to a
    ULX-4 name, keeping skip = 1 until reviewed.
- **D48** (27 Nov, Alistair): the 16 skipped bare sections that are survey targets go into a review
  list for his #17 review: each with its original skip reason and date, counts, catalogue a95 and a
  review PNG. He decides keep or unskip one by one.
- **D49** (27 Nov, Alistair): retire wt_p14a and wt_regrev, with the usual checks and no --force,
  keeping the branches. Any run records only in those trees are copied to the root tree first.
- **D50** (27 Nov, Alistair): #18's 2-tag pilot goes ahead (2 CPUs, 4 h cap, 8 core-h). The cluster
  policy also needs his own yes in #11's terminal.
- **D51** (27 Nov, Alistair): option A (the long part on the full span above 80 ks) is closed. It is
  recorded as a known limitation, alongside B's NO-GO.

- **D52** (27 Nov, overseer): #41 fixes testshim so each test's tmp_path is removed after the test,
  on a small branch with a test (a bug fix in test infrastructure). It stops a leak of about 15,000
  files a day into tmp/.
- **D53** (27 Nov, overseer): #15 applies its one-line fix to new_obs_regions.run_one's folder lookup
  (glob `<obsid>_*/dir`, else `<obsid>/dir`), then runs the other 31 batch-1 regions and draws
  their PNGs.
- **D54** (27 Nov, overseer): #15 adds the filter rule to pick(): a Closed or CalClosed exposure is
  never the primary while an open-filter one exists. It gets tests and a replay. 0150280101's re-prep
  needs Alistair's sbatch yes.
- **D55** (27 Nov, overseer): NGC1313-X2 comes out of new_obs_regions.HOLD_SOURCES. Alistair released
  it on 18 Nov (§15.229 (8)), and the list wasn't updated.
- **D56** (27 Nov, overseer): D48's keep-or-unskip review is mostly moot. #18 found that survey_list()
  ignores skip, so those sections already reach #19. #18 draws PNGs for the 20 rows with a
  params-section mode of region_review (about 1 h on the login node, no SAS), so Alistair can
  check their regions in his #17 review.

- **D57** (27 Nov, Alistair): job approval tiers. Up to 10 core-h billed, a session submits within its
  item's scope without asking. From 10 to 50 core-h, the overseer approves on the board. Above 50,
  Alistair. The cluster policy (sbatch and deletions need his yes in the terminal) is separate. It
  stays in force until he changes it at its source.
- **D58** (27 Nov, Alistair): one flat gallery folder of review PNGs named `<obsid>_<name>.png`,
  updated whenever PNGs are drawn. The flaring-consistency panel gets distinct colours and a
  legend, or goes.

- **D59** (27 Nov, Alistair): he approves every Slurm job (and every deletion) himself, with his yes in
  the session's terminal, as the cluster policy requires. D57's tiers decide who approves the plan
  and price before that. The dispatcher alerts him for each new terminal ask.

- **D60** (27 Nov, Alistair): NGC4258-J121903.0+471722 is excluded (held) in 0400560301. It isn't
  detected, a brighter neighbour 15" away outshines it to its core, contamination is 6.4%, and the
  diffuse emission is +323%. No region can separate it, so its net counts aren't source counts. The
  only other target with both "not detected" and "outshines" (0674210601) already fails the count
  gate. Whether that combination becomes a hard QA rule is still open.

- **D61** (27 Nov, Alistair, #17 review): 0111800101 NGC3031-J095533.0+690034 passes, overriding its fov
  FAIL. The fail is on the 40" count aperture at the Small Window's edge, not on the 20" timing circle,
  and its counts are far above the gate. #15 records the override after checking the timing circle is
  at least 90% exposed. 0504780101 NGC0703-J015239.6+361025: FAIL agreed. 0670950101
  NGC0891-J022233.5+422027: passes (REVIEW flags seen). 0674210601 NGC0224-J004247.1+411615: FAIL
  stands; it fails on non-detection and the count gate, not on the bright neighbour. 0763120401
  NGC0224-J004545.6+413941: PASS stands; how the pipeline handles off-axis PSFs goes to #15 as a
  question. Principle he raised: a brighter neighbour doesn't stop a detection (its photons act as
  background), so "outshines" stays a REVIEW flag and is never a FAIL on its own.

- **D62** (27 Nov, Alistair): in the region review, "not detected by eboxdetect within 10 arcsec" is a
  FAIL check of its own, which he can override per observation. "outshines" stays a REVIEW flag and
  never fails on its own (D61: a neighbour's photons act as background). In both D60 and 0674210601
  the non-detection is the real problem, because the aperture counts then measure something else.

- **D63** (27 Nov, Alistair): v1.0 changes how target photons are selected and weighted, from the
  overseer's labelled-photon study (simulation; STATUS, Needs Alistair 2). (1) The spatial factor p
  in w = p·g(E)^β comes from a joint fit of the target, its catalogued neighbours and the background
  (fixed PSF shapes at fixed positions, amplitudes free, like emldetect's multi-source fit), so p is a
  three-way probability. Extraction goes out to 60", with no neighbour masks. The energy factor
  g(E)^β is unchanged (#47 owns β). (2) Exposure-aware areas everywhere, with the fov check on the
  timing and background circles only. (3) An attribution check where a fitted neighbour lies within
  30" of a target. In the study, (1) lowered a95 by 15-25% against 20" two-way weights beside a
  neighbour 3x brighter at 5-15", stayed within 2% of the oracle with 1.5" position and PSF-shape
  errors, and lowered a95 by 4% (on-axis) and 8% (off-axis) for bright isolated sources. (2) changed
  K by 0.5%; it is a QA fix. Before ADOPTED: a design and price report (stage 1), then an injection
  validation on real batch-1 event files evaluated only at the injected trial, a null check, the
  golden, and rebuilt red-noise records (#38), a50 and list (#37) and certificate (#13).

## Sent 25 Nov (where each stood on 26 Nov)
- **S1, merge** (mcseed step done, 2513b12; the rest unconfirmed until merge reports): yes to all four. Merge quota41b's head dfa0244 into the trial, run the suite and
  fast-forward. The order is mcseed, then quota41b, intake15, p14a-calib (5f9a009), longpext
  (1cbad1c, relabelled "(merge 1)") and methods42. Treat intake15 as ready. Add the rule-14
  "(merge n)" sentence with the first merge. Report when mcseed lands.
- **S2, #38** (confirmed 26 Nov: both done, queued at 8828681): finish now (figure 174, RESULT part 2, TODO line, suite, commit, queue). Fix the
  a50.py default in code: refuse to run unless the sensitivity folder is given or is the current
  set, record the folder used, and add a test.
- **S3, #15** (reached; not acted on; now D9 and D10): download the 14 batch-1 ODFs from the XSA. Check each tarball is complete against
  its summary file list, and record its source, date and sha256 in INTAKE.md. From batch 2, run
  seeding and prep as Slurm jobs, priced from batch 1's measured times.
- **S4, #13** (reached; all done, 15.234, 9145f0a):
  - §15.133: (C);
  - archive the 19 Oct validated.json;
  - the rev3 hashes are checked by #27 and the battery tools;
  - put an advisory block for mcseed's seed rule and the weighted_search / aperture_energy_scan
    hashes in the gate;
  - write the gate code and tests on cert13, unqueued until a95cut and #46 land.
- **S5, #27** (reached; done, 101b486; catch rate corrected by D13): accept recommendations 1–9 and 11 as provisional for REV. 3, and leave item 10
  open. Record the (k) catch rate as 84–95.6%. Nothing is signed until C1–C4 are in.
- **S6, #47** (no session found on 26 Nov): start the β study. Options (a)–(g), soft-spectrum sources at slopes −θ̄₀/2 and
  −θ̄₀ using real count spectra, and costs, including the false-alarm cost from the measured
  correlation between weightings.
- **S7, Alistair**: run filemap.sh v2 twice and check tmp/ for the quota rise.
