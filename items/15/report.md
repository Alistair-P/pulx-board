seq: 14
state: needs-you
date: 2026-11-28T16:45Z
host: login7c
---
#15 (board seq 14, D66): D63 stage 2 is built and tested on branch d63 (f6f01a0, off main e68c2fb). It is NOT queued: the validation runs first, then the merge goes in with cert13 under one golden (D65). Before the validation run can be built and priced finally, Alistair needs to decide two points (NEEDS YOU 1, 3).

1. **Selection rule** (written in new_obs_regions.py before it was applied):
   - A target is selected if (a) its region tool's eboxdetect list has a source within 30" at ≥ 0.1× the target count, or (b) it is in KNOWN_PAIRS (M82 X-2 ↔ X-1, which 4XMM merges into one source).
   - For a selected target: extraction to max(60", current aperture); masks inside that radius dropped; eboxdetect sources within the radius + 10" fitted jointly, plus the known partner.
   - **22 selected of 106** (data/d63_selection.tsv, with each target's reason):
     - 0400560301 (14.6", ×0.26; held under D60);
     - 0670950101 (24.8", ×0.12);
     - 0674210601 (13.7", ×0.72);
     - 0884030101 (26.9", ×0.14);
     - 0795712601 NGC5907-ULX1 (28.9", ×3.9);
     - 0935191301 SMC X-3 (29.9", ×0.76; held);
     - the 16 XMM M82-X2 epochs (known pair).
2. **Code:**
   - **Joint fit** (`radial_weighting.joint_neighbour_fit`):
     - Fixed shapes: each neighbour gets the CCF ELLBETA PSF at its own off-axis angle, on the target's footprint.
     - The target and neighbour amplitudes are fitted by EM, with the existing background (flare component included) held fixed.
     - The result is a three-way p.
   - **Wiring:** params `joint_nbrs` → preprocess.sh → pipeline_inputs.json (written only when set) → `_model_kw`, which every production path uses. **Unselected targets: p is bit-identical** (tested on 0110900201).
   - **QA rules (2):**
     - fov tests the background circles only;
     - counts use exposed areas, with the gate on net / f_ap;
     - REVIEW when the aperture is below 90% exposed;
     - the region tool reports exposed areas, but its background placement is unchanged.
   - **post_search.py:** target-weighted against neighbour-weighted Z₁² at the candidate's exact (f, ḟ). Ratio 2 is PROVISIONAL until the validation fixes it. It refuses to run without `--policy-passed`.
3. **Tests:**
   - test_d63 11/0/0. The synthetic field recovers both amplitudes (S within 6%, N within 4%), and the target's detectability K rises. The real-data identity test passes.
   - Related suites and **the full suite: 840/0/3**.
4. **Validation set** (stage-1 rule, unchanged): 4 neighbour fields (0400560301, 0670950101, 0674210601, 0884030101) + 10 seeded controls. **Problems:**
   - (i) The criterion "ratio ≥ 1 within 25" improves ≥ 5%" has no member in batch 1, so it cannot be tested as written.
   - (ii) 0150280101, which Alistair excluded, is among the controls.
   - (iii) Controls are unselected, so their p is identical by construction.
5. **Fresh price (INFERRED):**
   - Batch 1 is at prep only, so each of the 18 sections (4 neighbour fields × 2 variants + 10 controls) needs preprocess -a for its spectra, exposure map and inputs: 1–3 billed core-h each, 18–54.
   - Injection and jitter-null harness: about 5–10.
   - **Total about 25–65 billed core-h, about 1 day, about 500–900 files.**
   - The harness still has to be written. Each sbatch needs Alistair's yes in the terminal.
6. **M82 caveat:** the M82-X2 sections centre `src` on the X-1+X-2 blend (X-1 is 3.4" from it in 0112290201). The joint fit there also needs src moved to X-2's own position, which is a params.conf change I have not made.

Recorded in §15.229 (34) on d63.

Jobs: none. Core-h: 0 (login only). Files: 125,488.

SETTLED:
- D63 stage 2 is built and tested on d63 f6f01a0 (suite 840/0/3); 22 targets selected, each with its reason.
- 0150280101 stays out (D66 (4)).

NEEDS YOU:
1. Alistair: the "ratio ≥ 1 within 25"" criterion has no batch-1 member. Add M82 X-2 epochs (or NGC 5907 0795712601) to the validation, or drop the criterion? It must be decided before anything runs.
2. Alistair: should 0150280101 be replaced in the controls by the next ObsID in seed order?
3. Alistair: should the M82-X2 sections' src be moved to X-2's own Chandra position (a params.conf change)?
4. Approve writing the validation harness, then the run at about 25–65 billed core-h (each sbatch shown here for Alistair's yes).

NEXT:
- With 1–3 answered: write the harness and the validation params file, price it again on a pilot, and show the sbatch commands here.
