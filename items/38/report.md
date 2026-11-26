seq: 0
state: done
date: 2026-11-26T17:03Z
host: login7c
---
#38 (red-noise usability): finished Alistair's 25 Nov instructions; the branch is queued for merge.

25 Nov instructions, both reached me (in the terminal):
1. Finish now: all DONE.
   - Figure 174 rendered, looked at and indexed.
   - RESULT part 2 written (§15.232 (12)-(15)).
   - TODO red-rows line marked resolved.
   - Suite 744/0/3, commit c84bbaf.
   - main (2513b12, mcseed) merged into the branch per Alistair's 20 Nov merge order. The one conflict, docs/LESSONS.md, was resolved by keeping both entries. Merged-tree suite 748/0/3, merge commit 8828681, 0 behind main.
   - QUEUED: checklist.py queue add rednoise 38.
2. a50 sensitivity folder fix: DONE (c84bbaf).
   - a50.py uses the folder only if it is named (ZSQW_A50_SENS_DIR or --sens-dir) or is the current set (logs/survey_sensitivity_current_a95). Otherwise it refuses.
   - The folder and a hash of its JSONs are recorded in a50_thresholds.json and a50.json.
   - Two new tests.
3. Checklist line updated (queued).

Results (aggregates only; §15.232 (12)-(13)):
- 0 of 704 observation-octaves change verdict.
- Scratch inclusion a95 moves by a factor of 0.995-1.006 against production; none crosses 0.25.

Orbit golden: re-frozen on this branch. --orbit-compare passes with an EMPTY GOLD_ORBIT_ACCEPT. This covers the re-freeze the merge session was holding.

Jobs: none.
Core-h: 0 billed this step; about 2.7 since the item began.
Files: 144,058 (quota 200,000).

SETTLED:
- #38: one-sided red-noise gate; a50 reads records built by survey_axis, refusing stale ones; a50 sensitivity folder named or the current set, and recorded; fig 174. §15.232, commit 8828681. QUEUED.

NEEDS YOU:
1. Keep the one CLAUDE.md line I added on 25 Nov under rule 9 (where a50 takes its sensitivity folder from)? POLICY now makes CLAUDE.md edits Alistair-only. Recommend yes.

NEXT:
- After the merge session merges #38: rebuild production records from main (a50.py --build-red --all, about 3 core-h, priced from job 12379547), then a50 --all --thresholds applied and survey_pipeline --list before the list freezes. Nothing started.
