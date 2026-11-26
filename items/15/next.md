seq: 2
from: overseer
authority: D37 (Alistair)
date: 2026-11-26T18:46Z
---
#15: carry on with batch 1 as in your last report. When the last downloads pass the check, record all 14 in INTAKE.md and submit the second array within D10. Then add this for Alistair (D37):
1. Review PNGs. Make one PNG per observation (and per extra target, for #18's [obsid:tag] targets) for his #17 review. Show:
   - a smoothed, log-scaled image, wide enough to show the background region and any diffuse emission around the source;
   - every region: the source aperture (the wide aperture and the 20" timing radius), the background region, masked neighbours, other list targets in the field, and chip gaps or CCD edges;
   - a zoomed panel on the source;
   - a caption with source and background counts, the flags row, and whether each region is automatic or a manual override.
   Write them into the region cache (stats/new_obs_regions/<obsid>/), so they're packed with it after review. Never put them on the board.
2. Region override script. Alistair enters corrected values (centre and radius for the source, background or a mask, plus a reason). The script writes them to a separate overrides file, without editing the automated output. The staging step applies overrides on top of the automated regions, so both stay on record with date and reason. After each override it reruns the checks (inside the field of view, the P30 rule that no listed target sits in a background region, counts) and redraws that observation's PNG.
3. Build both on a branch with tests, queue it, and say how Alistair should view the PNGs and run the script. Price any compute first; it should be login-node work only.
Tell the board when batch 1's PNGs are ready for his review. #18 (#11's session) will reuse these tools for tags. Update your checklist line, and end with the rule-12 report.
