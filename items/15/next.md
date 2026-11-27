seq: 8
from: overseer
authority: overseer: review PNG verdicts (Alistair's review of 0400560301)
date: 2026-11-27T15:00Z
---
#15: Alistair has looked at 0400560301 (NGC4258-J121903.0+471722), and it isn't good, although its PNG says "ALL CHECKS PASS". The target isn't detected by eboxdetect. A brighter neighbour 15" away outshines it to its core, with contamination at 6.4% against a 5% tolerance. It sits on diffuse emission at +323%. So the net 2,252 counts are mostly diffuse excess plus the neighbour's wings, and the count gate passes for the wrong reason.
This repeats instruction 7. If you've done A–F already, only add G and H.
G. The verdict in the PNG banner and in index.tsv. Show FAIL if a check fails. Show REVIEW (in red, with the number of flags) if any of these flags is set: target not detected; a neighbour outshines the ULX inside the aperture; contamination above tolerance; diffuse emission above 100%; aperture shrunk below 60". Show PASS only if there are none. Sort index.tsv worst first, and add a column naming the flags. Don't change any inclusion rule; that's Alistair's (see H).
H. Count how many of batch 1's targets (bare and tags) carry each of those flags, and how many carry "target not detected" together with "neighbour outshines". Post the counts, so Alistair can decide whether any should become hard QA rules.
A–F as in instruction 7: the gallery (stats/region_review_gallery/<obsid>_<name>.png symlinks plus index.tsv, refreshed by draw); the flaring panel in distinct colours with a legend and shaded flare intervals, or dropped; the run_one folder-lookup fix, then the other 31 regions and their PNGs; NGC1313-X2 out of HOLD_SOURCES; the Closed/CalClosed rule in pick() on pickfix; and 0884030101's commands shown to Alistair in this terminal for his yes.
Update your checklist line, and end with the rule-12 report.
