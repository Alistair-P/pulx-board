seq: 2
state: needs-you
date: 2026-11-26T21:41Z
host: login7c
---
#15 (intake): D37's two tools are built and queued. Batch 1's regions, and so its review PNGs, wait on a naming decision.

**The tools (D37):**
- **Where:** branch `regionreview`, worktree /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_regrev, commit f8cf10b. Queued. test_region_review passes 7/0/0 and is registered in run_all_tests.sh. Login-node only.
- **One script, region_review.py:**
  - `draw` writes stats/new_obs_regions/<obsid>/<name>/review.png with:
    - a smoothed, log-scaled field image, wide enough for every background circle;
    - the wide aperture, the 20" timing radius and the source core;
    - backgrounds A and B, masked neighbours, and the other listed targets (from survey_list_v1 and the PULX archive);
    - CCD outlines, with the chip gaps between them;
    - a 3' zoom on the source;
    - a caption with the counts, the flags row, and whether each region is automatic or an override.
  - `add` records a correction in data/region_overrides.tsv: UTC date, ObsID, name, kind (src / core / bkg / bkg_alt / mask), action (set / add / remove / clear), centre, radius and reason. It refuses a row that cannot apply. It then reruns the field-of-view check (≥ 95% of each circle exposed), the P30 check (no listed target in a background circle) and the counts check (net ≥ 1,000), and redraws the PNG. result.json is never edited.
  - `new_obs_regions --stage` applies the rows on top of the automatic regions and notes each one in the section.
- **How Alistair uses them** (from the worktree above until the branch merges, then from main):
  - **Draw PNGs:** `python3 region_review.py draw <obsid>`, or `draw --all`.
  - **View on COSMA:** `eog` or `display` over X forwarding.
  - **View on his own machine:** `rsync -a --include='*/' --include='review.png' --exclude='*' cosma:/cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/new_obs_regions/ ./regions_review/`
  - **Correct a region:** e.g. `python3 region_review.py add 0764770101 NGC1313-X2 bkg remove --index 3 --reason "on a neighbour"`, or `... mask add --ra 49.59 --dec -66.60 --r 15 --reason "..."` (radius in arcsec).
  - **See what's on record:** `python3 region_review.py list <obsid>`; `check <obsid> <name>` reruns the checks and redraws.
- **First real PNG:** stats/new_obs_regions/0764770101/NGC1313-X2/review.png (all checks pass).

**Batch 1's regions:**
- logs/intake15/run_regions.py runs the region picker unchanged on each ObsID's main (best-a95) target, using its catalogue position from the survey list.
- Measured on 0764770101: 44 s and 0.33 GB per ObsID. The 48 ObsIDs would take about 45 min on the login node and add about 1,000 files.
- Not run yet, because of NEEDS YOU 1–2 below.

Jobs: none.
Core-h: 0 this step; 19.8 billed since the item began.
Files: about 160,000.

SETTLED:
- The D37 tools are on the queued branch `regionreview`, with tests.

NEEDS YOU:
1. **Main target vs. recovery target in the 15 NGC 1313 ObsIDs.** The best-a95 target is X-1 (DR14:201068601010001), so X-2, the blind recovery set's target, would be an [obsid:tag] target for #18. Should batch 1 also make X-2's regions now with the same tool (new_obs_regions --target obsid:tag), so its PNGs come with the batch?
2. **The params.conf name for non-PULX survey targets.** This is the stacking key, spelled once per source. I propose `<HOST>-<Jname>` (e.g. NGC1313-J031819.9-662911). Literature targets would then get coordinate names, e.g. Holmberg IX X-1 → UGC05336-J095753.3+690348. Is that acceptable, or should LIT targets keep a literature-style name such as HolmbergIX-X1? One run of the regions per name, so it should be settled before the run.
3. **0884030101's pn-exposure selection failure** (§15.229 (23)): should I propose a fix to the pn-exposure selection, or drop the ObsID?

NEXT:
- Once 1–2 are answered: run batch 1's regions (about 45 min on the login node), then `draw` for every result, then tell the board the PNGs are ready for Alistair's #17 review.
