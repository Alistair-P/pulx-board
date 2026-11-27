seq: 9
state: done
date: 2026-11-27T11:58Z
host: login7c
---
#42: filled in the survey-list cut in the methods text "The blind survey", as board seq 9 asked (a95cut on main, df0a6f9).

- docs/methods_section.md, survey list: the OPEN marker is replaced with the cut. An observation is in only if its a95 for a template-shaped pulse in the reference octave (0.85-1.7 Hz, defined in "Sensitivity") is below 0.25. The cut uses the sensitivity calculation alone, never a search output, and any widening would be a separately registered stage (15.226's user quote). Added 15.226 to the subsection's source comment, noting it replaces 15.155 (8)'s a50 <= 0.4. No counts or list contents are given.
- Commit 5264663 on methods42 sits on 0d0d550, which is already merged (2644692). Main's methods_section.md is identical to 0d0d550, so there is no conflict. Queued again as methods42 (#42): docs only, no manifest, golden not needed. Checklist #42 is updated.
- Backup: archive/methods_section.md.pre_methods42f_20261127.
- Suite not run: docs only, no code changed (rule 6).
- I checked for half-finished edits after the interruption: the worktree was clean at 0d0d550 before this change.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: one docs file edited, one backup; no quota reading taken.

SETTLED:
- The survey-list cut (a95 < 0.25, 15.226) is in the methods text; methods42 5264663 is queued.

NEEDS YOU:
- Nothing from #42. For Alistair: #30 still needs the meaning of "A1" and the candidate details.

NEXT:
- #42: two OPEN markers are left. The #23 jitter-null result goes in when it lands; the v1.0 known-pulsar recovery is decided at submission. Waiting on the board.
