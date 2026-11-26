seq: 8
state: idle
date: 2026-11-26T21:31Z
host: login7c
---
#42: read-only summary of three of Alistair's items, as the board asked (seq 8). Nothing changed. Sources: CHECKLIST.md, main's summary.txt and docs/TODO.md, the board's STATUS/BRIEF. No survey outputs, candidate files or verdicts opened (rule 1).

#30 -- checklist line: "[ ] #30 A1, the NGC 6946 X-1 check :: Needs the user's candidate details."
- Target: NGC 6946 X-1, ObsID 0401360301 (22.5 ks). Summary 15.213 (2)(a) names it "the target of checklist #30's candidate". The orbit-golden design kept it out of the golden set for that reason: running the orbit arm on it would be a survey-octave verdict on a non-PULX target (rule 1).
- What "A1" means: NOT FOUND in main's summary.txt, TODO.md or the board files. The "A1"s there are other things: the 15.131 (A1) 19 ks nulls, and change A1 of the sweep speed-up (15.97 Q). I didn't search candidate or survey files for it, because that would mean reading blinded material.
- Needed from Alistair: the candidate's details (presumably its frequency, fdot and epoch, and where it came from), and what "A1" refers to. Only he holds these.
- Blocked on it: #30 itself (not started). No other checklist line names #30 as a dependency.

#35 -- checklist line: "[ ] #35 Frame-alignment note: the user's edit, and a venue :: Not started."
- The note: docs/research_note_frame_times_DRAFT.md, "DRAFT research note, 1 Nov 2026. Not for circulation", on main since 6447fe1 (summary 15.192). It says frame-centre folding is the stock SAS option (barycentred TIME_RAW, bit for bit), measures the 1/r^2 = sinc^-2(pi f T_int) gain on real pulsations, and covers the three lattice artefacts and their fixes. Sources: 15.57, 15.93, 15.102, 15.137, 15.139 (5), 15.192; figures 1, 2, 52, 53, 93, 135.
- Edit wanted: his edit of the draft, plus a venue (research note or short paper). The records give no specific edits.
- Blocked on it: nothing else on the checklist. The methods paper's "Data and event times" (on methods42) already uses the same content.

#17 -- checklist line: "[ ] #17 The user's review of the flags table :: After #16."
- What he reviews per batch: data/new_obs_flags.tsv, written by new_obs_regions.py --stage (15.141 (3)). One row per observation the region picker ran on, most REVIEW flags first. Columns: obsid, name, decision (staged / below gate / held), ulx_counts_full, recentred (src moved onto the eboxdetect source), n_review, review, warnings. TODO's region-tool flags: approximate exposure map, ULX not detected, chip gaps or CCD crossings, background contamination. Today's table has 41 rows from the earlier region runs.
- Images: per observation and target, stats/new_obs_regions/<obsid>/<target>/regions.png, beside regions_{phys,fk5}.reg, result.json and params_section.conf (23 files per observation).
- Where it sits (15.229 (7), TODO "#16 plan"): per batch, download -> prep_events -> new_obs_regions + flags table (#17) -> staged params sections -> run_analysis -> load check + quota_pack. Batches are at most 50 by the quota cap. After his review, the region cache may be packed from 23 files per observation to 2.
- Time for a 50-ObsID batch: NOT RECORDED anywhere I found. Rough guess, INFERRED and not measured: about 1-3 minutes per ObsID to read its flags row and look at regions.png, longer for flagged rows. So roughly 1-2.5 hours per batch, mostly in the flagged rows at the top of the table.
- Blocked on it: each batch's staging (the sections enter params.conf only after review), and the region-cache packing (quota).

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: no quota reading taken.

SETTLED:
- Read-only report on #30, #35 and #17 posted; nothing changed.

NEEDS YOU:
- Nothing from #42. For Alistair: "A1" in #30 isn't defined in any record I can read without opening blinded material, so its meaning has to come from him with the candidate details.

NEXT:
- #42: wait for a95cut, then the one-line survey-list fill-in.
