seq: 5
state: idle
date: 2026-11-26T18:14Z
host: login7c
---
#42: wrote "Validation", the last subsection, on methods42, as the board asked (seq 5, plan 42.1). All 8 subsections are now drafted. Committed, queue entry updated; waiting.

Done (seq 5):
- methods42 head 0d0d550 (b39de95 plus one wording fix), on top of 7f48153. Docs only: docs/methods_section.md, no code, so no suite run.
- The queue entry now names 0d0d550. Checklist: all 8 drafted, still [~] because of the OPEN markers below.
- "Validation" is paper text in three parts:
  - Golden checks: the manifest; the 19-input reference (10 noise, 2 injection, 4 real) compared bit for bit or against pre-written predictions; the orbit golden's four inputs, determinism, the synthetic recovery within 3 lattice steps, and the empty accept list.
  - Null calibrations: synthetic w = 1 sets fitted and validated at 20/40/75/136 ks, 1,000 photons, stacked M 2-4; M 5 failed, so unusable. Torque-floor and orbit null sets. Then what synthetic nulls leave out and how each piece is covered: the weighted chi^2_2 check, the red-noise excess test, and the frame-preserving jitter nulls (own CCD's live frames +-K, p_i recomputed, 0.2% retention gate, count window on dropout combs).
  - Injection recovery: the orbit arm's 360 injections; the ceiling injections (0.94 at 20 and 0.90 at 30 Msun, relative to 10); M51 ULX-7 blind recovery by the long part, which failed the frequency-accuracy rule (kept as a recorded deviation); a95 by injection; the design-stage known-pulsar recovery (15.53 (d)).
  The pulsar recoveries cited are known-pulsar validation results from the summary, not survey output.
- Fixed before committing: the ceiling injections concern the long-period part, ceiling 10 Msun, with efficiencies stated relative to it. The golden set's "repeat" is a determinism re-run, not a property of the real inputs.

Three OPEN markers in the text, each saying what fills it:
1. Survey-list cut (The blind survey): fill in when #37's a95cut lands (the board will send it).
2. Jitter-null result (Validation): #23 (C1) has not run. The tool is described; its calibration result is pending.
3. Known-pulsar recovery in the v1.0 configuration (Validation): the only end-to-end recovery recorded is 15.53 (d), which predates the adopted weights, thresholds and orbit arm. Either cite a v1.0 recovery (the artefact battery #25 or survey dry runs, if they record one) or say it wasn't repeated. That choice is for Alistair or the overseer, at submission.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- "Validation" written and committed on methods42 (0d0d550). All 8 methods subsections are drafted; queue entry and checklist updated.

NEEDS YOU:
- Nothing now. OPEN marker 3 needs a decision before submission, not before the merge.

NEXT:
- #42: the survey-list fill-in when a95cut merges. Then whatever the board sends: a read-through, the #23 result, or marker 3.
