seq: 15
from: overseer
authority: D64 (overseer); D39
date: 2026-11-27T18:03Z
---
#44: this replaces instruction 14 and repeats what is still open.
1. Item 1 (figidx46) is done; thank you. Yes, queue longpext too. B is NO-GO, so the freeze on wt_longpext is lifted. First check that nothing after 1cbad1c touches pipeline code (only summary sections, scoring scripts and validation_plots.py's @fig functions), and that the full suite passes with main merged in. Then queue it, and say in figidx46's entry that it depends on longpext.
2. D39 continues as in instruction 14. The rule (15.236 (6), e6c9cb5) is committed before any draw. The pilot (8 draws, cap 6 core-h) waits for Alistair's yes in this terminal (D59). After the pilot, reprice. If the full run is within 110 core-h billed, ask him in this terminal for it; otherwise post needs-you with the price. Report the result against the rule. D63 (DECISIONS.md) will change p in neighbour fields for every arm alike, so it shouldn't change D39's comparison. Note in the record that D39 used the pre-D63 p.
Update your checklist line, and end with the rule-12 report.
