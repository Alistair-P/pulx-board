seq: 10
state: running
date: 2026-11-27T16:12Z
host: login7c
---
#18 (#11's session): did instruction 10 and Alistair's terminal yes. The pilot is running, the stale folders are deleted, and the X-2 swap is prepared; it waits for Alistair's yes to the exact sbatch.

ALISTAIR'S YES, IN THIS TERMINAL (27 Nov): "Go for the pilot sbatch (8 core-h), deleting the 2 stale pilot folders, and later the X-2 swap commands".
- Pilot: job 12448511, submitted from wt_mt at bc0ef53 (clean tree), running on m5002 since 16:10; cap 8 core-h. Before-hashes of 0830191401's shared dir/ taken first (81 files).
- Deleted: the two pre-D47 pilot region folders, after checking their contents. The D47-named results stay.

BUG FOUND AND FIXED (bc0ef53, 15.235 (7)). preprocess.sh's #41 guard (kept in #11's merge) stopped whenever <folder>.tar and SHA256SUMS.txt existed. But a pack restored as the guard's own message says ("tar -xf") keeps both files, so the guard refused every restored observation, including these three. It now stops only when the pack is there AND no epproc event list is loose. test_multitarget 17/0/0, including the restored case.

X-2 SWAP, PREPARED (targets18 50836e4):
- Regions: the region tool ran for NGC 1313 X-2 in 0405090101, 0693850501 and 0693851201, all OK, with review PNGs drawn (so they appear in the gallery). In 0405090101 the aperture is on X-2, and X-1 is about 3' away, in no background circle.
- params.conf: [obsid] becomes X-2 (the tool's section, analysis_only = 1). X-1's section moves unchanged to [obsid:D201068601010001]; its name stays NGC1313-X1 (the stacking key) and it gains analysis_only = 1. Before and after for each: logs/targets18/ngc1313/params_<obsid>_{before,after}.txt. Preflight on the six sections: 0 errors.
- Run script: slurm/submit_targets18_ngc1313.sh. For each ObsID: preprocess.sh -f -a <obsid> (X-2; overwrites dir/'s loose X-1 products, whose originals stay in #41's hash-checked .tar), then -a <obsid>:D201068601010001 (X-1 tag). It never runs the tag after a failed bare. It writes one ANALYSIS_ONLY row per target to production signal_summary.csv. Cap: 2 CPUs x 16 h = 32 core-h.

Jobs: 12448511 (pilot), running.
Core-h: up to 8 this step (pilot); #18 up to 8.
Files: about +30 (3 region results and PNGs, pilot logs).
Full suite: rerun in progress after the guard fix. The result goes in the next report.

SETTLED:
- #18: pilot submitted (12448511) and stale folders deleted, both on Alistair's yes; guard bug fixed; X-2 swap prepared (targets18 50836e4); 15.235 (7).

NEEDS YOU:
1. Alistair, in this terminal: yes to `sbatch slurm/submit_targets18_ngc1313.sh`, from /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting_wt_mt (cosma5/durham, 2 CPUs, 12000M, 16 h, cap 32 core-h; out/err in stats/targets18/ngc1313/)? Recommend yes, but only after the pilot passes its PASS rule.

NEXT:
- When the pilot ends: check the pre-registered PASS rule (15.235 (3)) and report. Then, on Alistair's yes, submit the swap job. Nothing else started.
