seq: 4
state: idle
date: 2026-11-26T18:02Z
host: login7c
---
#42: wrote "Sensitivity" on methods42, as the board asked (seq 4, plan 42.1), and brought the survey subsection's red-noise rule up to date with main. Committed, queue entry updated; waiting for the last subsection.

Done (seq 4):
- methods42 head 7f48153, on top of 21b26d6. Docs only: docs/methods_section.md, no code, so no suite run.
- The queue entry now names 7f48153. Checklist: 7 of 8 subsections written; 1 TO WRITE (Validation).
- "Sensitivity" is paper text in three parts:
  - The model: lambda = eta a^2 S2_eff / 2 and a_P from the noncentral chi^2 at the applied threshold. a50 and a95 differ only in P; reference octave and minimum over octaves.
  - eta by thinning injection on the survey's own axis, weights, sweep and thresholds: 12 injections, 48 near the cut, the small k correction.
  - Validation: a95 by injection, 1886/2000, exact 95% 0.932-0.953, none rejected per observation (15.226 (12)). Thinning accepted (15.212). What the model leaves out: the spread of efficiency within an octave.
- Correction to "The blind survey" (committed at 21b26d6): it described the red-noise gate as a two-sided KS. Main now has #38's rule (15.232, merged 1399fad): an octave is unusable only on an excess of high values over max(c, 1) x chi^2_2, by a one-sided KS at 0.01 per observation (Bonferroni over octaves). The text now says that and why: a deficit can't raise a false alarm at a threshold that is never lowered. I found it through the CLAUDE.md change on main.
- "Per-photon source probability" pointed to "Sensitivity" for the frame-preserving jitter nulls. Those belong under Validation, so the pointer now says Validation.
- Every number here comes from injections and simulations. No real-data search result is in this report or the text.

Noted:
- methods42 is off d03bf93, and main is now 1399fad (mcseed, quota41b, rednoise merged). The text follows main's current state (15.232). The merge should be textual: docs/methods_section.md and one summary.txt subsection, 15.227 (15).

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- "Sensitivity" written and committed on methods42 (7f48153); the survey subsection's red-noise rule matches main; queue entry and checklist updated.

NEEDS YOU:
- Nothing.

NEXT:
- #42: "Validation" when the board sends it: golden checks, coherent and orbit arms; null calibrations including the jitter nulls; injection recovery. After a95cut merges, the one-line survey-list fill-in.
