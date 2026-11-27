seq: 9
state: needs-you
date: 2026-11-27T14:44Z
host: login7c
---
#18 (#11's session): did instruction 9 (D56). The 20 review PNGs are drawn and the mode that draws them is queued. Three actions wait for Alistair's yes in this terminal.

DONE (targets18 3e561ba, queued; suite 793/0/3; 15.235 (6)):
- region_review.py has a params-section mode: `python3 region_review.py params TID [...] --out DIR`. It draws a params.conf section's HAND-SET regions through the unchanged draw(), with no SAS. It builds a 4" counts image from the loose pn_clean.fits, plus an exposure stand-in from where the events fall. So its fov check uses event occupancy, not an exposure map; every PNG says so in its Flags line. The caption says the regions are hand-set and that no region-tool counts exist. It writes only to --out, never to the region tool's store.
- Interface note for #15: this is your module. I added a subcommand and one caption branch, read only when a result has `regions_from`. Automatic results draw exactly as before; test_region_review is still 7/0/0.
- PNGs: all 20 rows, 46 s on the login node, 0 errors, 0 failing checks. They are at /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/targets18/d48_review/png/<obsid>/<name>/review.png, beside the list (review_list.tsv, 20 rows). I looked at three (P13, M82 X-2, ULX-4); the regions are on the source.
- For the #17 review: in 0693760101, background circle A2 sits just outside P13's catalogue position. It passes the P30 check, and P13 looks faint in that epoch.

WAITING FOR ALISTAIR'S YES IN THIS TERMINAL (cluster policy):
a. The pilot (D50). From /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt: `sbatch slurm/submit_targets18_pilot.sh`. Resources: cosma5/durham, 2 CPUs, 12000M, 4 h, cap 8 core-h. Output and error go to stats/targets18/pilot/ (root tree).
b. Deleting my two stale pilot region folders (old names, before D47):
   rm -r /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/new_obs_regions/0830191401/NGC5194-D201128402010003 /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/new_obs_regions/0830191401/NGC5195-D201128402010012
c. The NGC 1313 X-2 swap in 0405090101, 0693850501 and 0693851201 (D47 (a); the overseer recommends overwriting). Order: #41 unpacks the three; then I run the region tool for X-2 and show the params.conf before and after; then, after Alistair's yes, preprocess.sh -f -a on the X-2 bare (overwrites dir/'s X-1 products) and -a on the new X-1 tag. I will show the exact commands once they are unpacked.

Jobs: none.
Core-h: 0 this step; #18 0.
Files: about +80 (20 x result.json, review.png, img.fits, exp.fits).

SETTLED:
- #18: D56 review PNGs for the 20 rows; region_review params mode; targets18 3e561ba queued; 15.235 (6).

NEEDS YOU:
1. Alistair, in this terminal: yes to (a), the pilot sbatch? Recommend yes.
2. Alistair, in this terminal: yes to (b), deleting the two stale folders? Recommend yes.
3. Overseer: ask #41 to unpack 0405090101, 0693850501 and 0693851201 for (c)? Recommend yes.

NEXT:
- On (a): submit, wait for the sha256 file, check the pre-registered PASS rule. On (b): delete, then confirm with ls. On (c): the X-2 regions and the params.conf before/after. Nothing started.
