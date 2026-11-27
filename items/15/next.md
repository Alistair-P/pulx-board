seq: 12
from: overseer
authority: D60, D61, D62 (Alistair)
date: 2026-11-27T16:31Z
---
#15: this replaces instruction 11 and repeats it in full, with one addition (item 3, D62) and two extra questions in 4a. If you have already done parts of 11, don't redo them; say which in your report.

1. D60 (Alistair): exclude NGC4258-J121903.0+471722 in 0400560301 for this epoch. Hold it in the staging tables (not staged), with that reason and D60 cited, so it never enters params.conf from this run. Its PNG and index row should show it as held.

2. D61, Alistair's #17 review of five gallery PNGs:
   - 0111800101 NGC3031-J095533.0+690034: pass, overriding the fov FAIL. That fail is on the 40" count aperture at the Small Window's edge. First measure the exposed fraction of the 20" timing circle. If it is at least 90%, record the pass as an override citing D61. If not, don't override; report it.
   - 0504780101 NGC0703-J015239.6+361025: FAIL stands.
   - 0670950101 NGC0891-J022233.5+422027: pass (he has seen the REVIEW flags).
   - 0674210601 NGC0224-J004247.1+411615: FAIL stands.
   - 0763120401 NGC0224-J004545.6+413941: PASS stands.
   Record these the way the review tool takes verdict overrides (say which), and redraw those PNGs and index rows.

3. D62 (Alistair): in the review tool, "not detected by eboxdetect within 10 arcsec" becomes a FAIL check of its own, which Alistair can override per observation. "outshines" stays a REVIEW flag and never fails on its own. Add a test for each. Redo batch 1's verdicts and report which change. Expected: 0400560301 goes from REVIEW to FAIL (consistent with D60), 0674210601 gains a second fail reason, and nothing else. Commit on regfix and refresh its queue entry.

4. Report on these from the code and batch 1's records, on the login node. No code changes beyond item 3.
   a. Which events does the search take: those in the 20" timing circle, or the aperture's with weights? Is the timing radius 20" for every target, whatever the off-axis angle? Do the per-photon weights use an off-axis and energy-dependent PSF, or an on-axis one? Do they also weight by energy (source spectrum against background spectrum)? For 0763120401, give its off-axis angle and the fraction of its source counts inside 20". Say how many batch-1 targets are more than 10' off-axis, with the same fraction for each.
   b. Which circles does the fov check test? Does background scaling use the exposed area or the full circle area? How many batch-1 fov FAILs would change if fov tested only the timing circle and the background circles, with the aperture's exposed fraction used as a correction?
   c. 0670950101: what is its "outshines" flag based on? On the image the ULX dominates at its core. Its capped east mask overlaps the 20" timing circle; say how the weights handle that.
   d. 0674210601: the tool's own ULX count is far above the aperture net count. Say where the tool's figure comes from (a catalogue rate times exposure, or a measurement).
   Put per-source numbers in a file on COSMA and give its path. The board report carries only the answers and numbers of targets.

5. The two reruns (0884030101, 0150280101) still wait for Alistair's yes in this terminal. Update your checklist line, and end with the rule-12 report.
