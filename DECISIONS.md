# Decisions

Each entry has a number, a date, who decided, the decision and the reason. Instructions cite
entries by number, for example "D3". Never rewrite an entry; add a new one that replaces it.

## Alistair's answers
Alistair writes answers to "Needs Alistair" items here, or tells the overseer, which records them.
The next overseer wake acts on them.

- 26 Nov 17:06: keep #38's CLAUDE.md line under rule 9 (recorded as D6).

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
- **D13** (26 Nov, overseer; correction from the record): the (k) catch rate is 85.8–95.6%, from
  24 distinct lattice lines (§15.228 (11)). It replaces S5's 84–95.6%.
- **D14** (26 Nov, overseer): rule 15e clarified. Simulations, injections, nulls and tests may be
  reported with numbers. Only results of searches on real data are barred.
- **D15** (26 Nov, overseer): #13 writes the v1.0 build_cert.py draft now (validated = false, no
  compute), then waits for a95cut and #46.

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
