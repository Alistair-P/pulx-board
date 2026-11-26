seq: 0
state: running
date: 2026-11-26T17:02Z
host: login7c
---
#38 (red-noise usability): finishing Alistair's 25 Nov instructions; merging main into the branch before queueing.

25 Nov instructions, all reached me (in the terminal):
1. Finish now. Figure 174 rendered, looked at and indexed: DONE. RESULT part 2 (§15.232 (12)-(15)): DONE. TODO red-rows line marked resolved: DONE. Suite 744/0/3: DONE. Commit c84bbaf: DONE. Queue: NOT YET. main moved 9 commits (mcseed, 2513b12). Per Alistair's 20 Nov merge order I am merging main into the branch first. The one conflict was docs/LESSONS.md (both sides added a group-7 entry; both kept). Neither module mcseed changed (weighted_search, aperture_energy_scan) is on the manifest or orbit-golden path. The merged-tree suite is running on the login node at nice 10. When it passes: commit the merge, then checklist.py queue add rednoise 38.
2. a50 sensitivity folder: DONE in c84bbaf. a50.py uses the folder only if it is named (ZSQW_A50_SENS_DIR or --sens-dir) or is the current set (CURRENT_SENS_DIR = logs/survey_sensitivity_current_a95, found in this tree or the root tree). Otherwise it refuses, and an empty name is refused too. The folder plus a hash of its JSONs goes into a50_thresholds.json, and per row into a50.json. Two new tests (test_a50_thresholds 14/0/0). Check: with no folder named it chose the current set and reproduced the scratch a50.csv bit for bit.
3. Checklist line updated.

Results (aggregates only; details in summary.txt §15.232 (12)-(13), table in logs/rednoise/flip_report.json):
- Red-noise records: 88/88 built by the survey's own code.
- Flip report: 0 of 704 observation-octaves change verdict between the old and new test, so there are no efficiency runs to price.
- Scratch a50 against the production table: inclusion a95 moves by a factor of 0.995-1.006 and none crosses 0.25.
- The first scratch run read the stale default sensitivity folder. I discarded it and recorded the mistake; it is what prompted fix 2.

Jobs: none (records build 12379547 done).
Core-h: about 2.7 billed since the item began (pilot 12378288 0.12, build 12379547 2.6); about 1 h of login-node work today (scratch a50, suites).
Files: 144,058 (quota 200,000).

SETTLED:
- #38: one-sided red-noise gate; a50 reads records built by survey_axis; a50 sensitivity folder named or the current set, and recorded. 0/704 verdict flips, no a95 crossing of 0.25. §15.232 (12)-(15), commit c84bbaf. Merge of main not yet committed.

NEEDS YOU:
1. On 25 Nov I edited CLAUDE.md (one line on the red-noise item: where a50 takes its sensitivity folder from), under rule 9. POLICY now makes CLAUDE.md edits Alistair-only. Keep the line? Recommend yes; it records a50's new default for every session.

NEXT:
- When the merged-tree suite passes: commit the merge, run checklist.py queue add rednoise 38, and post done.
- After the merge session merges #38: rebuild production records from main (about 3 core-h), then a50 --all --thresholds applied and survey_pipeline --list, before the list freezes.
