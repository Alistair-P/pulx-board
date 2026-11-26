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
