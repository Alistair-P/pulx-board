seq: 0
state: needs-you
date: 2026-11-26T17:12Z
host: login7c
---
#37 (a95 inclusion cut): first board report. a95cut is waiting for its own golden check, which mcseed's landing on main (2513b12) has now unblocked. Nothing has been started since 19 Nov.

25 Nov instructions: none reached this session. The terminal has had no message since 19 Nov, there is no board instruction for 37, and none of S1-S7 in DECISIONS.md "Sent 25 Nov" is addressed to #37. The last instructions from Alistair (19 Nov) and where they stand:
- Run a95cut's golden check myself on the merged tree once mcseed and a95 are on main, and leave the ADOPTED line to the merge session: NOW UNBLOCKED. a95 is on main (b20499b) and mcseed is on main (2513b12). Not started.
- Rewrite the live list file only after #38 has merged and a50 and --list have been rerun on its rebuilt red-noise rows: WAITING. rednoise is queued, not on main. D7 says the overseer decides whether #37 or #38 does this rerun.

State:
- a95: MERGED (b20499b, 15.226 (16)).
- a95cut at e0ca515 (wt_a95cut): main d03bf93 merged in, suite 733/0/3. Queued NOT READY. Since then main has moved to 2513b12 (mcseed), and survey_pipeline.py on main is still 27678708, so a95cut's proposed hash is still f9f49373. The prediction is unchanged: coherent 19/19 and orbit 4/4 bit-identical with GOLD_ACCEPT = survey_pipeline.py only.
- The live list file is untouched (84). 15.226 (17) and docs/TODO.md hold the rerun step.

Jobs: none.
Core-h: 0 this step. Since the item began: 45.5 + 3.4 billed for the a95 work (jobs 12373611 and 12374954). Earlier #37 steps are in 15.199 and 15.226.
Files: no reading taken.

SETTLED:
- #37: no change since 19 Nov. a95 merged (b20499b). a95cut e0ca515 queued NOT READY. 15.226 (12)-(17).

NEEDS YOU:
1. Start a95cut's golden check now? mcseed landed in 2513b12, and Alistair approved this on 19 Nov. Plan: merge main 2513b12 into a95cut, then run the coherent and orbit golden on that tree as Slurm jobs, priced from mcseed's identical golden (cap 42.3 core-h, expected about 11.5). If both are bit-identical, mark a95cut ready. Recommend: yes.
2. D7: who reruns a50 and --list on #38's red rows after rednoise merges? Recommend #37, since its plan already names the list rewrite and the near-cut 48-injection rule may need re-judging.

NEXT:
- On the go for (1): merge main into a95cut, run the suite, run the golden, then mark it ready or report the difference.
- After rednoise merges, and if (2) gives it to #37: rerun a50 --all --thresholds applied and --list on the rebuilt rows, then rewrite logs/survey_full/obsids_longest_first.txt with the result.
