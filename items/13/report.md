seq: 0
state: done
date: 2026-11-26T17:10Z
host: login7c
---
#13 (B7): recorded the user's 25 Nov decisions, retired the 19 Oct stamp, wrote the hash gate and its test on cert13.

The user's 25 Nov instructions (typed in this terminal; all five reached me) and where each stands:
1. 15.133 -> option (C): #46 decides the stacked rows above 120 ks; Z1/Z3 there use max(transfer, direct fit). RECORDED, 15.234 (1)(a). Takes effect with #46's code, before the stamp.
2. 19 Oct validated.json moved to archive/ now: DONE. Now at archive/validated_survey_thresholds.json.pre_cert13_20261125 (sha256 a7df2b1f..., checked after the move). Main's code refuses results runs and --collect; --unvalidated-diagnostic unaffected. No running job reads that path. 15.234 (2).
3. rev3 battery hashes checked by #27 / battery tools, not the survey gate: DONE in code. A 'post_search' block the gate ignores; verify_hashes() is there for those tools to call. 15.234 (1)(c).
4. mcseed seed rule + weighted_search / aperture_energy_scan hashes in an 'advisory' block: DONE in code. The gate prints the block and never checks it. 15.234 (1)(d).
5. Checklist line updated: DONE (set again today with the commit).
Then: gate code + tests/test_certificate.py on cert13: DONE, 9145f0a. UNQUEUED until a95cut and #46 land, as instructed.

The gate (survey_pipeline): a certificate must have a 'gate' block {modules, inputs}. It must cover 23 modules (the manifest's 8 + the other files the survey imports) and 9 input files whose paths are read from the code (rf models per configuration, margins, orbit + long-part thresholds, both frozen bank records, QA thresholds, template). Every hash must match, or the run refuses and names the file. ZSQW_CERT overrides the path; each results JSON records the certificate's sha256.

Note for the board: in my own branch I edited CLAUDE.md's "Known gaps" line and added a LESSONS group 7 entry (rule 9). It reaches main only through the queue.

"What has gone wrong" (asked in the terminal): nothing failed. The full suite PASSED. Its last step was still running when the user asked, so it hadn't been committed or reported yet. It is now.

Jobs: none (suite on the login node, nice 10, 1 thread)
Core-h: 0 this step; 0 since the item began
Files: not taken

SETTLED:
- #13 (partial): 15.133 -> (C) recorded, old stamp archived, hash gate + tests/test_certificate.py written. test_certificate 9 passed / 2 skipped (they wait for the stamp); full suite 742/0/5, ALL SUITES PASS (log is in logs/cert13/suite_1.log, untracked). 15.234, commit 9145f0a (branch cert13; survey_pipeline.py is now ba03e88a...).

NEEDS YOU:
1. When cert13 is rebased after a95cut and #46, approve the ADOPTED.sha256 line for survey_pipeline.py after its golden check (golden predicted bit-identical, GOLD_ACCEPT=survey_pipeline.py; ~13-25 billed core-h). Recommend yes, decided then.
2. CLAUDE.md "Known gaps" still says the golden check doesn't exercise the orbit arm (#12), which is stale since #12 settled. Fix it at the next merge? Recommend yes (not my item, so not edited).

NEXT:
- Rewrite logs/p13/build_cert.py for v1.0: use gate_block(); add the 15.234 decisions, the a95 cut, the long part, per-target IDs, per-span threshold tables for a consistency test, and the advisory and post_search blocks. Draft only (validated = false).
- After a95cut and #46 are on main: rebase cert13, golden on the merged tree, ADOPTED line (your approval), queue; stamp after the merge.
