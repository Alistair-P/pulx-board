seq: 4
from: overseer
authority: D66 (Alistair)
date: 2026-11-27T22:30Z
---
#13: D66 (Alistair, 27 Nov 22:29): apply the max rule. Above 120 ks, the Z1 and Z3 thresholds become max(transfer, direct), at R1W's shares under (d). Code it in octave_thresholds on cert13, with tests. Re-derive the draft, and report each (span, octave) change against the current R1W table. Raising thresholds can only lower (d)'s union-check count; confirm that. Don't run a golden. It runs once, on a combined trial merge of cert13 and #15's D63 branch, after that branch's validation has passed (D65). Re-queue cert13 at the new commit. The survey_pipeline.py and octave_thresholds.py ADOPTED lines go to Alistair after that golden. Update your checklist line, and end with the rule-12 report.
