seq: 4
state: done
date: 2026-11-28T16:36Z
host: login7c
---
#13 — reply to board seq 4 (D66). Login node only. No golden, no compute. cert13 at 325eb1b, RE-QUEUED.

1. MAX RULE CODED (commit 6849f7c). The rule is in octave_thresholds, a MANIFEST module. It acts only in the R1W table: spans of 120–136 ks with the window arm on.
- Where: every usable Z1/Z3 octave at or above 0.053 Hz.
- Threshold = max(transfer, direct) + R1's margin of 1.1.
- The direct value is 15.133's t136 fit, evaluated at the same design alpha as the transfer.
- Each row records direct_rule; each covered arm records z?_transfer, z?_direct and z?_rule.
- If the fit's Z1 or Z3 validation is false, the code refuses (SystemExit).
- Unchanged: spans ≤120 ks, the window-off path, and octaves below 0.053 Hz (the t136 nulls predate the torque floor).
The fit parameters are frozen in a NEW file, stats/thresholds_15.106/rf_direct_136ks.json, holding A, p and c for 14 arm-octaves plus the sha256 of the source files. It is a gated certificate input, so the gate now has 10 inputs. Reproduced first: at R0's alpha it gives fit.json's design values exactly. The 136 ks fit also covers 120–136 ks, as candidate.json's scope did. At 122 ks that errs on the conservative side, because 136 ks has more cells.

2. CHANGES vs the current R1W table, applied values, red scale 1 (0 means the transfer was already larger):
- 122 ks Z1: 0.053 +2.26, 0.106 +0.80, 0.2125 +1.16, 0.425 0, 0.85 +0.54, 1.7 +0.30, 3.4 0
- 122 ks Z3: +1.39, +1.69, +1.43, +2.15, +0.59, +1.03, +1.56 (same octaves)
- 136 ks Z1: +1.71, +0.22, +0.50, 0, 0, 0, 0
- 136 ks Z3: +1.00, +1.20, +0.86, +1.61, +0.002, +0.40, +1.00
No threshold falls anywhere.

3. UNION CHECK — CONFIRMED. Every covered threshold is at or above its transfer, so the union count can only stay the same or fall. I re-scored #46's own 400 null realisations from their records, with no new realisations: old 2 (Z1 1, Z3 0, window 1), which matches 15.236 (5); new 2 (Z1 1, Z3 0, window 1). The new crossings are a subset of the old ones, so the PASS stands.

4. TESTS. tests/test_direct_max.py (new, registered): 7/0/0. It covers:
- the rule equals max(transfer, direct), with the direct value recomputed independently;
- thresholds only rise;
- no change at ≤120 ks or with the window off;
- the frozen file equals fit.json;
- a failed validation is refused;
- the file is gated and recorded in the survey JSON.
tests/test_stacked_window.py: the share-rescale check now reads the transfer component (7/0/0).
build_cert now records and checks the rule.
Full suite: 827 passed, 0 failed, 5 skipped.

5. DRAFT rebuilt at 325eb1b: --check CONSISTENT. Every blocker is READY except the ADOPTED lines for survey_pipeline.py and octave_thresholds.py. Those go to Alistair after D65's one golden.

6. RE-QUEUED cert13 for the combined trial merge with #15's D63 branch. The golden accept list must name both modules. Note: the queue line's auto "manifest:" field still says only survey_pipeline.py; queue set can't change it, so its golden field names both. The slurm/submit_golden_c13_*.sh scripts are superseded by D65; do not submit them.
Checklist #13 updated.

Permissions: I set the new JSON read-only (444) by mistake, then put it back to 644 at once. No other permission change.

Jobs: none. Core-h: 0.
Files: octave_thresholds.py, survey_pipeline.py, logs/p13/build_cert.py, tests/test_direct_max.py, tests/test_stacked_window.py, run_all_tests.sh, summary.txt 15.234 (6); new stats/thresholds_15.106/rf_direct_136ks.json; draft stats/survey_thresholds/validated_DRAFT_v1.json; backups archive/*.pre_cert13max_20261128.

SETTLED: D66 coded and tested; union count 2 → 2, PASS stands; cert13 re-queued at 325eb1b; suite 827/0/5.
NEEDS YOU: nothing new. The ADOPTED lines (survey_pipeline.py, octave_thresholds.py) come after the one golden (D65).
NEXT: wait on the board for the combined trial merge.
