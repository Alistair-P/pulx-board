# Digest since the last overseer wake

The dispatcher adds one block per item it handles. The overseer clears this file at each wake
(the blocks stay in git history).

<!-- block format:

### merge, report seq 3 (running), 21:33
- p14a-calib merged, main 15285f7, §15.228 (merge 1), suite 772/0/3; D22 and D24 done in the same commit. Next: longpext.
- sent: plan merge.1 (instruction seq 4); triggered plan 25.2 to #25
- read in full: no

### 25, triggered by merge seq 3, 21:47
- p14a-calib is on main.
- sent: plan 25.2 (instruction seq 1)
- read in full: no

### 37, report seq 1 (needs-you), 21:31
- a95cut golden PASS (coherent 19/19 bit-identical, orbit 4/4); queued READY at 6b015e2 after merging main 6b0b68f; suite 765/0/3; 11.3 core-h.
- for overseer: asks whether to rerun the golden on the merged tree (rednoise changed an orbit-path module)
- read in full: yes

### 11, report seq 3 (needs-you), 21:32
- #18 step 1 target table done (43d8ccf, 15.235); findings a–e from records.
- for overseer: new NEEDS YOU 2–4 for Alistair (skip lifts, bare slots for P13/X-2, 0693760101 rename)
- read in full: yes

### 15, report seq 2 (needs-you), 21:41
- D37 review-PNG and override tools built and queued (regionreview f8cf10b). Batch 1 regions not run.
- for overseer: NEEDS YOU 1–3 (X-2 tag regions, params.conf naming, 0884030101 fix or drop)
- read in full: yes

### 42, report seq 8 (idle), 21:31
- Read-only summary of #30, #35, #17 for Alistair; "A1" undefined in readable records.
- for overseer: content for Alistair, outside plan 42.1
- read in full: yes

### 44, report seq 7 (running), 21:46
- (d) add-on budgeting on new branch stacked46d (e37a247); union check job 12438600 pending (600 nulls, ~30 core-h, cap 40).
- held: running (44.2); noted for overseer: report cites seq 7, and differs from seq 8 in null count
- read in full: yes
