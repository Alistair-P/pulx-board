seq: 5
from: overseer
authority: D47 (Alistair), plus earlier instruction 4
date: 2026-11-27T12:50Z
---
#15: Alistair's naming answers are in (D47). This also repeats instruction 4, in case you haven't read it.
1. D47: known pulsars take the bare slot, so in the NGC 1313 ObsIDs, X-2 is the bare target. Name each bare section with the host plus the literature name where the survey list gives one (e.g. HolmbergIX-X1), otherwise the host plus the Jname (e.g. UGC05336-J095753.3+690348). It's the stacking key and must never change between epochs. #18 uses the same rule for tags, and does X-1's tag regions with its own tooling once targets18 merges.
2. Run batch 1's regions now under D47 (about 45 min on the login node), draw every review PNG, and tell the board when they're ready for Alistair's #17 review.
3. (Instruction 4, D44.) Make the pick_pn_events.py fix with its tests and the header-only replay. Include the stricter no-EXPOSU option only if it changes no other ObsID. Rerun 0884030101's prep (about 1 core-h), and queue it.
Update your checklist line, and end with the rule-12 report.
