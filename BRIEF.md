# PULX brief

What the dispatcher and the overseer need to know. The overseer keeps this current.
Last full revision: 26 Nov 2026 (first board reports read 17:20).

## The project
- Alistair's blind search for pulsations in ultraluminous X-ray sources, using archival XMM-Newton
  data. The code repo is z_sq_weighting on COSMA (Durham HPC), at
  /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting.
- Each checklist item has its own git worktree, z_sq_weighting_wt_<name>, and its own Claude Code
  session in tmux (session `pulx`). The merge session works in wt_merge and is the only one that
  changes main.
- The record lives on COSMA: CHECKLIST.md (via checklist.py), the §15 sections of summary.txt,
  docs/STANDING_RULES.md, docs/LESSONS.md and the merge queue (`checklist.py queue show`).
- Reports follow rule 12: a first line, then Jobs / Core-h / Files, then SETTLED, NEEDS YOU, NEXT.

## Design (v1.0)
- The search layer is separate from the decision layer and is frozen at the v1.0 tag. After the
  tag, only bug fixes may change it (rule 11).
- Photon weights are w = p·g(E)^β with β = 0.75. η(β, γ) is the weight efficiency, and a50 ∝ η^−½.
  The weighted search takes every event in the aperture (20-100"; masks cut). timing_radius is
  empty, so the 20" circle on the review PNGs is only drawn. p uses the CCF's ELLBETA PSF (off-axis
  and energy-dependent), and is two-way (source against background) with neighbours masked.
  HENDRICS is the unweighted cross-check. (#15, 27 Nov.)
- Search arms:
  - coherent Z1/Z3;
  - stacked, with M segments (validated for M = 2–4);
  - orbit short bank (P ≤ 0.7 d);
  - long-period part, for spans of 57.5–80 ks at 0.2125–0.85 Hz, with LONGP_TOL 1e−3 and
    2.4e−8 s⁻¹. It is on in v1.0 and adds 3.9% to compute.
- The floor configuration applies from 17 ks; below that it is pre-floor. There are no validated
  thresholds below 17 ks. So the 94 shorter targets are deferred to a later stage with 15 and
  10 ks nulls, not dropped.
- Thresholds come from the RF tail model, with a union bound (δu = 2 ln R). R0 (§15.125) splits the
  non-orbit α three ways (Z1 0.004275, stacked 0.004275, Z3 0.00095), with a +1.4 margin. R1
  (§15.123) drops the stacked arm and gives its share to Z1 (Z1 0.00855, Z3 0.00095), with a +1.1
  margin. R1 applies wherever M is outside 2–4, including above 120 ks. Going from R1 to R0
  raises Z1 by 1.71 and Z3 by 0.27. The Z1 common factor R = 1.231 (+0.44 in Z²) is adopted (z1-adopt).
- The inclusion cut is a95 < 0.25 (#37). a95 is the 95% point of the same detection curve as a50.
  The k correction is 1.014 with 12 η injections and 1.004 with 48. An a95 within ±20% of 0.25
  gets 48 injections. The on-disk list goes from 84 to 73 under this cut.
- Red-noise usability (#38): a one-sided, excess-only KS test at s = max(c, 1), α = 0.01, with cuts
  of 1.517 (n = 1) and 1.828 (n = 8).
- Artefact battery rev3 (#25) = rev2, plus (d) rebuilt as a halves amplitude test, plus the (k)
  lattice check. Provisional policy: a (d) failure sends a candidate to review, and a (k) failure
  vetoes it. The (k) catch rate is 84–95.6% at 95% confidence, as Alistair chose (D16). 84% counts
  the extension's 21 lattice lines, 85.8% all 24 distinct lines, and 95.6% the 82 forgeries
  (§15.228 (11)).
- MC seeding (mcseed, #11): seeds are crc32(obsid|tag[|offset]). sigma_global is advisory only,
  because MC resolution is 5e−5 against the 5e−8 needed.
- Golden checks compare against ADOPTED.sha256 and MANIFEST. Only Alistair approves ADOPTED lines.

## The survey list (#15)
- 571 targets on 386 ObsIDs pass the catalogue a95 cut. 477 have spans of at least 17 ks.
  138 ObsIDs have more than one target (#18). NGC 7793 ULX-4 is flagged as a known pulsar.
- Intake runs in batches of up to 50 ObsIDs. Seeding happens per batch, just before prep. From
  batch 2, seeding and prep run as Slurm jobs, not on the login node. XSA downloads need an
  approved list.
- The fixed recovery set is 3 epochs: NGC 2403 ULX 0164560901, and NGC 4631 X8 0110900201 and
  0943790101. Recovery epochs must pass the survey's QA, including the 1,000-count minimum. They
  are exempt only from the a95 cut. SMC X-3 stays out (held for pile-up on 12 Oct).

## Rules that matter most here
- Rule 1, blinding: never open search outputs. Nothing on the board may contain them.
- Rule 7: price in billed CPUs (memory counts), in core-h and in files. One output file per task.
- Rule 11: after the tag, only bug fixes in the search layer.
- Rule 12: the report format above.
- Rule 13: a session edits only its own checklist line.
- Rule 14: merges go through the queue. Merge records are labelled "(merge n)".
- Rule 15: the board (RULE15.md).
- Alistair's standing limits:
  - ask before more than 50 core-h or about an hour of work;
  - never use `--force` to remove a worktree;
  - only the merge session changes main;
  - sessions must not scan /cosma5 broadly.

## File quota
- Soft limit 200,000, hard limit 220,000, with a 7-day grace period. Work to 195,000, which keeps
  5,000 headroom.
- #16's batch cap is N = min(50, floor((195,000 − used)/500)). #15's run_batch.py stops at 194,000.
- Readings: 132,874 (#44, about 20 Nov), 162,028–162,141 (25 Nov). The cause of the rise of about
  29,000 is not yet found. #15 projects 170,586 at the end of intake and 176,346 at the end of
  the survey.

## Lessons to apply
- `sbatch --export` splits on commas.
- `git worktree remove` deletes ignored files silently.
- A trailing-slash gitignore pattern doesn't match a symlink.
- A pilot must sample every band and span bin it prices. A 4-draw pilot under-priced #44's batch 1
  by 1.8 times (2.3 times in the low band).
- #41 refuses to pack any folder a link points into. Packing once broke 1,264 P13 links.

## Where things stand (26 Nov, from the first board reports)
- On main: multitarget (1538aa3), mcseed (27ba948; record 2513b12), a95 (b20499b).
- Queued: rednoise (#38, 8828681, merged-tree suite 748/0/3), quota41b, intake15, p14a-calib,
  longpext, methods42, policy27 (docs only). a95cut is NOT READY until its golden check passes.
- #46 is scored: FIRM (b) among the arms, but (b) doesn't beat having no stacked arm above
  120 ks. Alistair decides (b) or keep the gap. Batch 1 is complete: 164/164, 552.6 core-h.
- #15: batch 1 stopped after 7 of 32 prepped. The rest goes to Slurm (D10).
- File count 144,000–146,000.

## Path to the v1.0 tag (as of 25 Nov)
1. Merge queue, in order: mcseed; quota41b at dfa0244; intake15; p14a-calib at 5f9a009; longpext
   at 1cbad1c, relabelling §15.225's "(12) MERGED" as "(merge 1)"; methods42. Then a95cut once
   #37's golden check passes, and rednoise (#38) once it's queued. z1-deeptail (#39) is NOT READY.
2. #37: a95cut's golden check after mcseed lands. Then rerun a50 and the list after #38 merges.
3. #46: score on all 164 batch-1 draws (job 12424696), choosing between 4 and 5 segments. Then that
   option's null runs, its code change and the 0791010101 golden slot.
4. #13, the certificate: gate code and tests on cert13, unqueued until a95cut and #46 land.
5. #14, the tag.
- After the tag: #23 and #24 (real-data jitter nulls, local whitening), #19 (the IN list; it needs
  #17, #18 and #37), and #20 and #21 (the pilot and the full run).
- D63/D66 (27 Nov), in v1.0: a three-way joint-fit p only for targets with a neighbour at 0.1x or
  brighter within 30"; new QA area rules; post_search.py attribution; the Z1/Z3 max rule above
  120 ks. #15 builds and validates, then one combined trial merge with cert13 and one golden (D65).
- Separate study: #47, the β question. It is analytic only. Options (a)–(g), soft-spectrum sources,
  and whether a flat (β = 0) search could run as a separately registered stage after the tag.

## Alistair's own open items
- #17: review of the recovery sections and batch regions.
- #30: the A1 candidate details.
- #35: his edit of the frame-alignment note.
- §15.133: (C) was recommended on 25 Nov. Confirm whether he relayed it to #13.
- #44 batch 2 (about 270–280 core-h billed): decide after #46.
- The COSMA quota request (less urgent now).
