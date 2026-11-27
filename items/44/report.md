seq: 8
state: idle
date: 2026-11-27T01:04Z
host: login7c
---
#44/#46, seq 8, final report: I finished the (d) golden check and queued branch stacked46d for merge. It is the top line of the merge queue, and #13 is not queued yet, so it lands ahead of #13.

Seq 8 step by step:
1. DONE: the add-on raises thresholds only above 120 ks. Checked in the code; output is byte-identical to main at 120 ks and below, and above 120 ks with the switch off.
2. DONE: the union (K_eff) check passed. 2 of 400 synthetic nulls crossed any threshold, against 3.80 expected (P = 0.89; the rule was k <= 7). It billed 22.8 core-h. Already reported in full.
3. DONE: (d) is implemented on stacked46d, off main 6b0b68f in its own worktree, now at 6a030a7. wt_longpext is untouched and still frozen at 1cbad1c.
   - Golden PASS at 960bfab; the manifest modules have not changed since.
     - 19 of 19 coherent inputs are bit-identical to main's last golden.
     - The orbit golden is identical, and its (b) recovery check passes.
     - New slot 0791010101: two runs in separate processes are IDENTICAL. The window rule's choice is recorded in the slot's output.
   - Golden billed 26.8 core-h in total (cap 46.5).
   - Queued with `checklist.py queue add stacked46d 46`, manifest octave_thresholds.py and survey_pipeline.py.
   - No ADOPTED line written. Proposed hashes: octave_thresholds.py ab3e3264, survey_pipeline.py 1250fa50.
   - On adoption, the merge session also freezes the window-slot reference from stats/fast_golden/otcheck_A3w_w46d_r1 into speedup_reference.
4. NOT STARTED: the confirming simulation; it is with Alistair.
Batch 2 is still held. Checklist line #46 is updated.

Jobs: none running. 12438661 (window slot) finished: 5 CPUs x 3:04, 15.3 core-h.
Core-h: this step 15.3. Since seq 8 on #46 (d): 50.7 = union 22.8 + cancelled first design 1.1 + golden 26.8. That is spread over two pre-priced runs, each under its own cap (40 and 46.5). Before seq 8, #44/#46 had used batch 1's 552.6 plus small scoring runs.
Files: no quota reading taken.

SETTLED: (d) is implemented and tested; union check PASS; golden PASS, including the new slot's two-run determinism check; queued ahead of #13.
NEEDS ALISTAIR (not blocking me):
- the ADOPTED line for the two manifest modules;
- the go or no-go on the confirming simulation;
- batch 2 of #44, which is held (~270-280 core-h re-projected).
Records: summary.txt 15.236 (1)-(5) on branch stacked46d; stats/stacked46d/union46d_score.json; logs/stacked46d/golden_diff_s46d.json.
