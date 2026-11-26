seq: 0
state: idle
date: 2026-11-26T17:20Z
host: login7c
---
#42 (methods paper; also closed #43 and #45): idle since 20 Nov, after writing "Data and event times" and rewording the M82 X-2 paragraph. Branch methods42 is queued; waiting for the next instruction.

25 Nov instructions (DECISIONS.md "Sent 25 Nov"):
- None of S1-S7 is addressed to #42, and no instruction reached this session between 20 and 26 Nov, on the board or in my terminal.
- S1 (merge) sets the queue order and puts methods42 last. On 26 Nov, 54d5a13 is not yet on main, which fits that order. Nothing for me to do.
- S2-S7 belong to other items.

State of #42:
- Branch methods42 at 54d5a13 (worktree wt_methods42, off main d03bf93). Queued on 20 Nov: manifest none, golden not needed, docs/methods_section.md and summary.txt only, no code, so no suite run.
- Written (3 of 8): "Data and event times" (new 20 Nov), the population energy template, and the M82 X-2 exploratory paragraph.
- M82 X-2 paragraph: reworded 20 Nov, at Alistair's request, to present it as a demonstration of what the weighted fold makes possible with XMM. Bachetti et al. 2022 Section III and Appendix F checked for why they left XMM out: weak pulsations below 3 keV, and background from M82 X-1 and the galaxy.
- Wording point: those folds weight by p_i alone (position and energy), not by the g(E) template, so the text says "p_i", not "energy-weighted". Recorded in summary 15.227 (15).
- TO WRITE (5): per-photon source probability, weighted search statistic, the blind survey, sensitivity, validation.
- #45 settled 19 Nov and merged (b3bf465, 1741eaa); wt_m82lr retired, branch kept.

Jobs: none.
Core-h: 0 this step; #42 has used none (#45 used about 12, settled).
Files: no quota reading taken.

SETTLED:
- #45 merged and settled; worktree retired, run outputs kept in the root tree's logs/m82lr/.
- #42 is still in progress, not settled: 3 of 8 subsections written, methods42 (54d5a13) queued.

NEEDS YOU:
- Nothing.

NEXT:
- #42: write "Per-photon source probability" from summary 15.194, 7.10 and the params.conf notes in CLAUDE.md, in wt_methods42 on top of 54d5a13. I'll start it when the board or Alistair says to go.
