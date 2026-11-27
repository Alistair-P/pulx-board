seq: 11
state: done
date: 2026-11-27T14:29Z
host: login7c
---
#42: frame-lattice questions for Alistair (board seq 11), from main's code, 15.224, 15.228, 15.97 R and the frame-times note. Read only; no search output opened. Lines are f = (j/m) f_frame.

1. Z3 fundamentals in v1.0. Each sweep topped at hi gives Z3 fundamentals in [hi/6, hi/3], and harmonics are read only up to hi (pulx_recovery: fsw, z_n_fft_harmonic).
- FF, LW, SW (top 6.8 Hz): fmin to 2.267 Hz.
- EFF (top 1.7 Hz): fmin to 0.567 Hz.
- fmin is 0.0066 Hz (floor) or 0.01 Hz (pre-floor).
- So no mode tests a Z3 fundamental at f_frame/3 = 4.544 Hz. Z1 does search 4.544 Hz (FF octave 3.4-6.8).
- FF's Z3 top, 2.267 Hz, sits 0.2% below f_frame/6 = 2.272 Hz.

2. Lattice lines inside the bands (bands from code; f_frame from 15.224 (9)):
- m = 1 (every frame same phase, Z ~ N) and m = 2: no arm reads either, at any harmonic, in any mode.
  - FF: f_frame 13.63 and f_frame/2 6.816, both above 6.8.
  - LW: 20.98 and 10.49.
  - EFF: 5.02 and 2.51, both above 1.7.
  - SW: 176 Hz.
- Lowest order read by Z1, Z3's harmonics and stacked:
  - FF: m = 3, 4.544 Hz (Z1 directly; also Z3's 3rd harmonic of 1.515 Hz). m = 4, 3.408; m = 5, 2.726 / 5.452; m = 6, 2.272; denser above.
  - EFF: m = 3, 1.674 Hz.
  - LW: m = 4, 5.246 (m = 3 is 6.99, outside).
  - SW: m = 26, 6.78.
  - Every octave holds lines with m >= 3 (15.224 (9): m ~ 1000-2000 in FF's lowest octave).
- An exact fold stays at chi^2_2 noise at every m (15.228 (0)); only a binned fold forges, strongest at m = 32j +- 1.
- Orbit arm: trial orbits (a sin i >= 1.9 lt-s) demodulate the times, which breaks the lattice (15.93).
- #25's 24 lines (15.228 (11)) are SIMULATED forgeries, not survey candidates. They were made from real FF event times on 0941150101 and 0693760101, thinned and folded with a 32-bin histogram. Statistic: Z1 at the forgery's own f (h = 1). All 24 are inside the FF Z1 band, and none is a Z3 harmonic:
  - m = 31: k 1-13 (0.440-5.717 Hz)
  - m = 33: k 1, 2, 4, 5, 7, 8, 10 (0.413-4.131 Hz)
  - m = 63: k 1 (0.216 Hz); m = 65: k 2 (0.419 Hz)
  - 0693760101 adds m = 31 k 1 and m = 33 k 1.
  - (k) caught all 82 forgeries that reached Z^2 >= 30.

3. f_frame/3 in Z3 in earlier versions: 15.97 ADDENDUM R (11 Oct 2026, readout_check.py, job 12130688), a DIAGNOSTIC check prompted by the user's question about Z3 harmonics near 4.5 Hz. Neither calibration nor threshold validation.
- Its 48 null simulations (40 ks, 0.85-6.8 Hz, continuous and frame-snapped) give only the chance rate near readout lines (m <= 6), and nothing over threshold.
- Its real-data part I don't quote (15e). As a design point it records that the one line is the frame rate itself, entering a Z3 read through a 6.816 Hz fundamental whose 2nd harmonic is 13.63 Hz, and that the survey's Z3 never reads a harmonic above 6.8 Hz.
- I found no section recording a measured f_frame/3 Z3 line; 4.5 Hz appears only in the question.

4. Check (k) (p14a_lattice, 15.228 (1), (8)):
- Applies only to a raw frame-centred fold (no orbit) with TIME_RAND present.
- Candidate f within 1/T + B f of k/(mD), with gcd(k, m) = 1 and 2 <= m <= M_MAX = ceil(sqrt(2N/30)), N the photons folded; lowest m first. m = 1 is check (a)'s.
- D is the source CCD's frame-table time, already barycentred. B = 1.25e-4 is the Doppler bound; in practice it absorbs the table-D bias of -6.0 to -6.6e-5 (15.228 (9)).
- Harmonics: the candidate's own f only, a Z1 fold. Check (a) covers f, 2f, 3f only against m = 1 frame-rate lines and aliases.
- Rule: p_k = ncx2.cdf(Z2_rand; 2, rho max(Z^2 - 2, 0)), with rho = sinc^2(f L D) and L the mode's live fraction. FAIL if p_k < 0.01.
- INFERRED gap: a Z3 candidate whose 2nd or 3rd harmonic sits on an m >= 2 line is not windowed at h > 1. Exact folds make this a guard, not a live failure.

Jobs: none.
Core-h: 0 this step; 0 since #42 began.
Files: none changed.

SETTLED:
- Lattice questions 1-4 answered from code and record.

NEEDS YOU:
- Nothing from #42. For Alistair: whether (k) should also window Z3 candidates at h = 2, 3 (#27's call).

NEXT:
- #42: waiting on the board.
