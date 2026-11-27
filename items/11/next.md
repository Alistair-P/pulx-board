seq: 8
from: overseer
authority: D47, D48, D50 (Alistair)
date: 2026-11-27T12:50Z
---
#11/#18: Alistair's answers.
1. D50: the pilot goes ahead. He'll give his yes to the exact sbatch command in this terminal, as the cluster policy needs. Then carry on as in your NEXT.
2. D47 (a): known pulsars take the bare slot. That's P13 in its 4 ObsIDs and NGC 1313 X-2 in its 3 (findings b), plus the NGC 1313 ObsIDs where X-1 becomes a tag.
3. D47 (b), names: a section's name is the host plus the literature name where the survey list gives one (e.g. HolmbergIX-X1), otherwise the host plus the Jname (e.g. UGC05336-J095753.3+690348). The name is the stacking key and must never change between epochs. Keep the DR14 ID as the internal [obsid:tag] key. Change targets18's naming to match. #15 uses the same rule for bare targets.
4. D47 (c): rename 0693760101's section to a NGC 7793 ULX-4 name, keeping skip = 1.
5. D48: for finding a, build a review list of the 16 skipped bare sections that are survey targets. For each: ObsID, section, target, the original skip reason and its date (from the record), counts, catalogue a95, and a review PNG drawn with region_review.py. Put it on COSMA, never on the board. Tell the board where it is and how many rows it has.
Make items 2–4 as params.conf edits on a branch, each listed with before and after, and queue it.
Update your checklist line, and end with the rule-12 report.
