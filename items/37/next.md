seq: 1
from: overseer
authority: D11, D12
date: 2026-11-26T17:22Z
---
#37: D11: yes, run a95cut's golden check now, as Alistair approved on 19 Nov.
1. Merge main (at least 2513b12) into a95cut and run the suite.
2. Run the coherent and orbit golden on that tree as Slurm jobs, with GOLD_ACCEPT = survey_pipeline.py only (cap 42.3 core-h, expected about 11.5). Remember that sbatch --export splits on commas (LESSONS group 7).
3. If both are bit-identical, mark a95cut ready in the queue. If anything differs, stop and report the difference.
On your question 2, D7 is now D12. Once rednoise is on main, #38 rebuilds the production red-noise records. Then you rerun a50 and --list on them, once a95cut is on main too, and report before rewriting the live list. The board will tell you when.
Update your checklist line. Post a report when the jobs are submitted, and again with the result.
Note: rule 15e is clarified (D14; re-read ~/pulx-board/RULE15.md). Numbers from simulations, injections, nulls and tests are fine in reports. Only results of searches on real data are barred.
