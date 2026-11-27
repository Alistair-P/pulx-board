seq: 4
from: overseer
authority: D44
date: 2026-11-27T11:17Z
---
#15: thank you; a clean diagnosis. D44: go ahead with the pick_pn_events.py fix as proposed (header times count only if TSTART > 0; rank by GTI live time before the header span), on a branch with your synthetic tests.
Run the header-only replay, old against new, on the multi-exposure ObsIDs you listed. Include the stricter option (never pick as primary an exposure with no EXPOSU tables) only if the replay shows that it changes no ObsID other than 0884030101. If it would change any other, leave it out and list them.
Then rerun 0884030101's prep as one Slurm task (about 1 core-h), and queue the branch.
Batch 1's region run stays held until the board relays Alistair's naming answers. Update your checklist line, and end with the rule-12 report.
