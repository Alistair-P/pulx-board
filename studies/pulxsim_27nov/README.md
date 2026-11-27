# Labelled-photon study of source selection and weighting (overseer, 27 Nov 2026)

Simulation only. No real data, nothing from COSMA. It is the evidence behind D63 (DECISIONS.md).

## What it does
Each simulated photon carries a label: 0 target, j ≥ 1 neighbour j, −1 flat background, −2 diffuse.
A method turns the photons into weights w_i (0 outside its region). The weighted statistic is
Z²_w = (2/Σw²)|Σ w e^{iφ}|². With the target pulsing as 1 + a cos φ, Z²_w is noncentral χ²₂ with
λ = a²K/2 and K = (Σ_target w)²/Σw². So each realisation's detectability follows from its labels,
with no phases drawn. a50 and a95 are the amplitudes detected 50% and 95% of the time at a 10⁻⁹
single-trial bar (Z² = 41.45). Leakage is the share of a pulsing neighbour's own detectability
(oracle K) that appears in the target's search.

check.py tests both assumptions. Under uniform phases every method gave mean 2.00 and tail rates of
0.84–1.03% at 10⁻² and 0.067–0.103% at 10⁻³ (30,000 draws each). With the target pulsing, direct
phase draws matched the K-based prediction to about 1σ (check.json).

## Methods compared
- **hard 20"**: a 20" circle, unweighted, neighbours masked (radius 10", capped 10" from the target).
- **weighted 20" / 60"**: two-way weights p = s/(s+b). s comes from aperture photometry with an
  on-axis PSF, and b from an annulus. Neighbours are masked.
- **joint fit 60"**: EM on fixed PSF shapes at the catalogue positions (target, every neighbour,
  flat background), with amplitudes free. p is the fitted target probability, three-way, out to 60",
  with no masks (`fit_weights`, `em` in pulxsim.py).
- **oracle**: the true probabilities, as the ceiling.
- Variants: full-circle area scaling (window edge); background map, diffuse model and energy weights
  (diffuse); matched off-axis PSF (off-axis).

## Headline results (a95; "none" = not detectable at a = 1)
| Scenario | hard 20" | weighted 20" | weighted 60" | joint fit 60" | best variant |
|---|---|---|---|---|---|
| Faint, clean (1,500 counts) | 0.653 | 0.515 | 0.512 | 0.512 | + energy 0.462 |
| Bright, clean (40,000) | 0.069 | 0.069 | 0.066 | 0.066 | |
| Window edge (no. 1) | 0.070 | 0.069 | 0.067 | 0.067 | |
| Faint on diffuse (no. 2) | none | 0.853 | 0.850 | 0.850 | + diffuse model + energy 0.761 |
| Fainter neighbour at 25" (no. 3) | 0.061 | 0.061 | 0.057 | 0.057 | |
| Neighbour 3x brighter at 5" | 0.388 | 0.382 | 0.367 | 0.327 | |
| ... at 10" | 0.380 | 0.364 | 0.353 | 0.273 | |
| ... at 15" | 0.309 | 0.286 | 0.292 | 0.243 | |
| ... at 10", PSF and 1.5" position errors | 0.377 | 0.365 | 0.352 | 0.285 | oracle 0.280 |
| Off-axis, bright (no. 5) | 0.073 | 0.073 | 0.067 | 0.067 | matched PSF 0.066 |
| Off-axis, faint | 0.601 | 0.532 | 0.522 | 0.525 | matched PSF 0.516 |
| Target off, neighbour at 14" (no. 4) | none | none | none | none | |

Leakage of a pulsing neighbour into the target's search, hard 20" against joint fit: 85% → 60% at
5", 74% → 23% at 10", 24% → 9% at 15", 32% → 8% with the target off. Full numbers:
`python3 summarise.py` (run from outside this folder).

## Caveats
- The PSF is a King stand-in (rc 5.5", α 1.5, roughly pn at 1.5 keV), not the CCF PSF. The off-axis
  stretch (1.3x/1.1x and 1.6x/1.15x) and the spectra are assumptions.
- The noise is white. New weights change the red-noise records (#38).
- The pipeline already weights by energy (w = p·g(E)^β, β = 0.75). So the energy rows show what
  energy weighting is worth, not a change D63 makes.
- **The pipeline's baseline is "weighted 60"", not "weighted 20"".** #15 found (27 Nov) that the
  weighted search takes the whole aperture (20-100", neighbours masked) with the ELLBETA PSF. So
  D63's gain is the step from "weighted 60"" to "joint fit 60"": 11%, 23%, 17% and 6% lower a95
  beside a neighbour 3x brighter at 5", 10", 15" and 25", and about 0 for isolated targets.

## Running it (read this before running anything)
This folder is inside the board clone. A changed or new file here stops every session's board sync.
So run it from somewhere else, on the login node, nice, one thread:

    mkdir -p /path/outside/the/board && cd /path/outside/the/board
    OMP_NUM_THREADS=1 nice -n 10 python3 ~/pulx-board/studies/pulxsim_27nov/scenarios.py clean_faint brighter_nbr10
    python3 ~/pulx-board/studies/pulxsim_27nov/summarise.py

Results go to ./pulxsim_out (or $PULXSIM_OUT). The scripts refuse to write inside this folder.
Scenario names are in scenarios.py, `S()`. Each takes seconds, except `diffuse` (about 2.5 minutes).
Needs numpy and scipy only.

## Files
- pulxsim.py: the simulator, the methods and the metrics.
- scenarios.py: the scenarios, modelled on the five gallery PNGs Alistair reviewed on 27 Nov.
- check.py, check.json: the null and shortcut checks.
- summarise.py: the table from the result files.
- results/: one JSON per scenario, as run on 27 Nov.
