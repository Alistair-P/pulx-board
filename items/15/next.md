seq: 7
from: overseer
authority: D58 (Alistair), plus D53-D55 from instruction 6
date: 2026-11-27T14:19Z
---
#15: this repeats instruction 6 and adds two requests from Alistair (D58).
A. Gallery. Add `region_review.py gallery`. It makes one flat folder, stats/region_review_gallery/ in the root tree, holding a symlink named <obsid>_<name>.png to every review.png (bare targets and [obsid:tag] targets alike), plus index.tsv (obsid, name, checks pass/fail, flags summary, path). Make `draw` refresh the gallery automatically, so #18's PNGs appear there too. Alistair will browse it with eog.
B. The flaring-consistency panel (the last one) is unreadable: all its lines are black. Give each curve a distinct colour and line style, with a legend: source, background A, background B, and the full-field monitor. Shade the flare or GTI intervals. If it still can't show anything useful, drop the panel. Then redraw every existing PNG.
C. (Instruction 6, D53) The folder-lookup fix in new_obs_regions.run_one (glob <obsid>_*/dir, else <obsid>/dir), with a test. Then run the other 31 batch-1 regions and draw their PNGs. Make target_name call #18's new_obs_regions.stack_name.
D. (Instruction 6, D55) Remove NGC1313-X2 from HOLD_SOURCES (released 18 Nov).
E. (Instruction 6, D54) The Closed/CalClosed rule in pick() on pickfix, with tests and the replay. Then prepare 0150280101's re-prep.
F. Alistair has said yes to 0884030101's deletion and rerun. The cluster policy still needs his yes in this terminal, so show him the exact commands here.
Under D57 you may now submit jobs of up to 10 core-h within your item's scope without asking the board, priced first, subject to the cluster policy. Tell the board when the gallery is ready and how many PNGs it holds. Update your checklist line, and end with the rule-12 report.
