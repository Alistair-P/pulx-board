seq: 0
state: needs-you
date: 2026-11-26T17:25Z
host: login7c
---
Merge session (rule 14, wt_merge): working through the merge queue. Paused after the terminal was lost on 25 Nov: quota41b's trial merge passed the suite, but the record and the fast-forward of main are not done yet.

Alistair's 25 Nov instructions in the terminal, and where each stands:
1. Merge quota41b's head dfa0244 into the trial, run the suite, fast-forward main if clean: PARTLY DONE. Fresh trial branch trial-q41c = main 2513b12 + dfa0244 = 9a4d34c (wt_trial). No conflicts, no manifest or orbit-path module touched, so no golden check. Suite ALL PASS 744/0/3 (737 + test_quota_pack 7; logs/mergeq/suite_merged_quota41b.log in the root tree). NOT YET DONE: §15.223 (merge n) record, fast-forward main, queue done.
2. Order mcseed, quota41b, intake15, p14a-calib, longpext (1cbad1c, "(merge 1)" relabel), methods42: being followed. mcseed DONE; quota41b in progress; the rest not started.
3. Treat intake15 as ready, its suite failure decided by the merged-trial run: received, not started. The entry has since moved to be203f4 (batch-1 prep runs from wt_intake15; merging the commit doesn't touch that tree).
4. Merge p14a-calib at 5f9a009: received, not started.
5. Add the rule-14 "(merge n)" sentence with the first merge: DONE in 2513b12.
6. Tell Alistair once mcseed lands: DONE on 25 Nov in the terminal.

Other state: main 2513b12; root tree detached at 2513b12, no tracked changes. longpext's batch-1 array 12424696 has COMPLETED, so no job imports from wt_longpext; I still merge 1cbad1c per the entry. a95cut (#37) is still marked NOT READY, waiting on its golden check, which can now run on main. New entry policy27 (#27, docs only, DETECTION_POLICY_v1.md rev. 2 draft + §15.233) is not in the agreed order. validation_check after mcseed: 0 MISSING; 173 (p14a-calib) and 174 (rednoise) are unindexed until those branches merge.

Jobs: none (merge session submits none).
Core-h: 0 this step, 0 since the session began (suites run on the login node, nice 10, 1 thread).
Files: not taken.

SETTLED:
- #11: mcseed merged to main 2513b12, record §15.217 (merge 2), suite 737/0/3; rule-14 "(merge n)" sentence added in the same commit. Inform #11 and #37 (a95cut's golden check can run on main).
- #41: quota41b dfa0244 trial-merged as 9a4d34c, suite 744/0/3; not yet on main.

NEEDS YOU:
1. Resume quota41b from the passing trial (record, fast-forward, root tree, validation_check, queue done) without rerunning the suite? Recommend yes: the passing run is on exactly this tree.
2. policy27 (#27, docs only): merge after methods42? Recommend yes. (Merging the detection-policy draft text is Alistair's call under POLICY.md, even though it's unsigned.)
3. RULE15.md says the merge session adds rule 15 to STANDING_RULES; POLICY.md puts STANDING_RULES edits with Alistair only. Add it with the next merge? Recommend yes, once you confirm here or in the terminal.

NEXT:
- quota41b record + fast-forward; then intake15 (be203f4), p14a-calib (5f9a009), longpext (1cbad1c + "(merge 1)" relabel in §15.225), methods42, then policy27 if approved. Each gets a trial merge, the full suite, a fast-forward and a record.
