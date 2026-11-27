seq: 10
state: done
date: 2026-11-27T12:55Z
host: login7c
---
#42: three coverage questions for Alistair, answered from main's code (board seq 10). Read only; no search output opened.

1. fdot at 1.6-1.75 Hz, spans 17-30 ks (floor configuration; stacked arm absent, M = 1)
- Coherent Z1 (octave 0.85-1.7 Hz): |fdot| <= 2.28e-7 Hz/s, the same across the octave (pulx_recovery.z_range at the octave TOP). Binding term: the orbit ceiling f a (2pi/P)^2 with a sin i 25.3 lt-s and P 1 d. Spin-up f x 1.756e-8 = 3.0e-8 and the torque cap 3.6e-9 don't bind. That is 8 cells at 17 ks and 26 at 30 ks. Above 1.7 Hz, octave 1.7-3.4 is sized at 3.4 Hz (4.6e-7).
- Coherent Z3, fundamental at 1.65 Hz (from the sweep topped at 6.8 Hz): |fdot| <= 3.0e-7 (a third of that sweep's range).
- Orbit short bank (to 1.7 Hz; 17-30 ks gives M = 2, segments 8.5-15 ks): the orbit is modelled by explicit templates, P 0.05-0.7 d, a sin i up to a Roche-filling He donor (1.9-15.2 lt-s). Peak a(2pi/P)^2 = 4.4e-6 c, i.e. up to 7.2e-6 Hz/s at 1.65 Hz. Intrinsic spin-up on top: nudot_max at the octave's LOWER edge (0.85 Hz) = 3.6e-9 Hz/s, wind-limited, L_Edd/(6 pi^2 I nu); the S = 150 supply cap (4.3e-9) and the chirp limit don't bind. Per segment that is one fdot point (cap T_seg^2/8 <= 0.25 cells), plus a semi-coherent grid of +-3.6e-9 between segments. No long part at these spans.

2. Frequency cap by pn mode (frame_times.search_fmax: Nyquist 1/(2 frame time), frame time read from EXPOSU; the survey then takes the largest octave top <= Nyquist):
- Full Frame, 73.35 ms: Nyquist 6.816 Hz, cap 6.8 Hz.
- Large Window, 47.66 ms: 10.49 Hz, cap 6.8.
- Small Window, 5.672 ms: 88.2 Hz, cap 6.8.
- Extended Full Frame, 199.17 ms: 2.510 Hz, survey cap 1.7.
Coverage of 1.65-1.75 Hz:
- Full Frame, Large Window, Small Window: Z1 everywhere (1.65-1.7 in 0.85-1.7, 1.7-1.75 in 1.7-3.4); Z3 everywhere; orbit arm 1.65-1.70 only, since --orbit-fmax is 1.7 in every mode.
- Extended Full Frame: Z1 and orbit 1.65-1.70 only; no Z3 at 1.65 (Z3 fundamentals stop at 0.567 Hz, since they need a sweep topped at 3f).
- Frame-integration loss r^2 at 1.65 Hz: FF 0.96, LW 0.98, EFF 0.70.

3. Pulse mostly in the 2nd harmonic (rough: single-cell chi^2, false-alarm 1e-6 to 1e-9, 50% detection):
- Z1 at f sees only the fundamental, so close to nothing.
- Z1 at 2f sees the harmonic as a sinusoid and reports 2f. It needs ~0.89x the noncentrality of a dedicated Z2 at f (2 vs 4 degrees of freedom).
- Z3 at f captures it but needs ~1.08x Z2's, and Z3 carries 10% of the non-orbit alpha against Z1's 90%, so its threshold is higher.
- So Z1 at 2f is the main route, within ~5% in amplitude of Z2.
- For f = 1.65 Hz, 2f = 3.3 Hz is outside the orbit arm. In FF/LW/SW it is inside the coherent band (r^2 0.84 FF). In EFF it is above Nyquist: not searched, r^2 0.20.

ObsIDs (pn_clean.fits headers):
- 0401360301: PrimeFullWindow, span 22.5 ks.
- 0200670401: PrimeFullWindow, span 19.3 ks.
Both are on #15's target table (stats/intake15/survey_spans.csv). Neither is in logs/survey_full/obsids_longest_first.txt, the frozen pre-a95cut list. survey_list() now gives:
- 0401360301: PENDING, no QA record.
- 0200670401: PENDING, no CONFIG entry; its section is timing = 0, products only.
Both params.conf sections carry skip = 1.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: none changed.

SETTLED:
- Coverage questions 1-3 answered from code; mode, span and list status of both ObsIDs given.

NEEDS YOU:
- Nothing from #42. For Alistair: #30 still needs the meaning of "A1" and the candidate details. survey_list's out-reason "P12 (A1)" may be the referent; not checked further.

NEXT:
- #42: waiting on the board. Two OPEN markers are left (#23 jitter-null result; v1.0 known-pulsar recovery at submission).
