seq: 1
state: done
date: 2026-11-26T18:18Z
host: login7c
---
#13 (B7): wrote the v1.0 certificate draft builder (board seq 1, D15). Committed; cert13 stays unqueued.

Done as instructed: logs/p13/build_cert.py rewritten, validated = false always, no compute. Both CLAUDE.md points left alone. Rule 15e clarification noted.
- Hashes come from survey_pipeline.gate_block(): 23 modules + 9 inputs.
- Per-span threshold tables at 17.5/30/40/60/75/80/100/122/136 ks, read from thresholds_for() and search_config(). The "unusable" list is exactly the tables' empty entries (49), each with the module's reason.
- The 15.234 (1)(a) decision (above 120 ks), the inclusion rule (marked PRE-a95cut on this branch), the orbit block and the long part (span, band, stage (iii) file, LONGP_TOL).
- Per-target entries keyed by target ID: configuration, stacked M, above-120 ks flag, published orbit, long part. They come from survey_list (selection inputs only) and are marked "frozen by #14".
- 'advisory' block (seed rule + weighted_search / aperture_energy_scan hashes) and 'post_search' block (rev3 + battery module hashes).
- --check is the consistency test. It re-derives every table and configuration, compares to 1e-9, and runs the survey gate's own hash check. The fresh draft is CONSISTENT.
- Blockers are tested from the code, not asserted. --stamp refuses while any is open, and even with none open it only says stamping is by hand after your review.
  Now READY: signed margins, clean tree.
  PENDING: a95cut, mcseed, rednoise (#38), #46, the Z1/Z3 = max(transfer, direct) rule above 120 ks, survey_pipeline.py's ADOPTED line, p14a_lattice.py not on main.

Draft: /cosma5/data/durham/dc-paga3/ODFs/z_sq_weighting/stats/survey_thresholds/validated_DRAFT_v1.json. It was built from cert13 at baa7e20, and the file records that.

Tests: new tests/test_build_cert.py, 9/0/0. The first full run failed one existing test: test_template_beta read the old draft's layout. I fixed it to read the same file's hash from the new gate block (backup in archive/). Full rerun: ALL SUITES PASS, 751/0/5.

Jobs: none (login node, nice 10, 1 thread)
Core-h: 0 this step; 0 since the item began
Files: not taken

SETTLED:
- #13 (partial): v1.0 draft builder with --check, blockers and per-target IDs; draft consistent. 15.234 (4), commit baa7e20 (hash gate 9145f0a), cert13 unqueued.

NEEDS YOU:
1. Nothing new. Outstanding from my last report: the ADOPTED line for survey_pipeline.py after the golden check on the rebased branch. Recommend yes, decided then.

NEXT:
- Wait for a95cut and #46 on main. Then: merge main into cert13, rerun build_cert --check and the suite, golden check on the merged tree (~13-25 billed core-h, priced first), ADOPTED line for approval, queue.
- After the merge: rebuild the draft in the root tree, the user reviews it, stamp by hand.
