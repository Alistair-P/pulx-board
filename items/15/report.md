seq: 0
state: needs-you
date: 2026-11-26T17:10Z
host: login7c
---
#15 (intake): batch 1's seed + prep run stopped partway when the previous session ended; your last terminal instruction was not acted on.

Board ID: 15. Your message said "#NN" and "wait NN"; I took NN to be 15, my checklist number (rule 15).

**Your 25 Nov instructions, all of which reached me:**
1. **The five decisions** (seed per batch; SMC X-3; recovery-set QA rule; P13 links; the dropped prep folders): DONE. §15.229 (20), commit 351facf. The fixed recovery set is 3 epochs. The four SMC X-3 prep folders are deleted, and the four NGC 2403 folders are kept.
2. **Keep NGC 2403; delete 0831790101 and 0890710101 after the survey-list check; seed and prep batch 1:**
   - 0831790101 is deleted.
   - 0890710101 is KEPT: a planned survey_list_v2 (margin-band) target uses it.
   - Batch 1 was STARTED 25 Nov 16:33 with logs/intake15/run_batch.py (be203f4).
   - It STOPPED when the previous session ended, at about 19:15. 7 of 32 ObsIDs are prepped, all ok: 0803990101, 0803990201, 0803990501, 0742590301, 0782310101, 0803990301, 0764770401.
   - It died while seeding the 8th, 0742490101. That left a partial ODF_tarballs/0742490101.tar.gz.part (29 MB, not a valid seed; a rerun overwrites it). There is no prep folder for it.
   - 25 ObsIDs are not yet prepped. Nothing is running now.
3. **Download the 14 ODFs with the read-back and completeness check, record source, date and sha256 in INTAKE.md, prep under the file cap; from batch 2 on, seed and prep as a Slurm job priced from batch 1's times:** this reached me, but I did NOT act on it. I ended that turn with no reply and no work. Nothing has been downloaded, and no Slurm script is written. "Leave the running batch as it is" no longer applies, because the run had already stopped.

**Batch 1's measured times, for the Slurm price:**
- prep_events took 9.2–32.4 min per ObsID (median 27.1, 7 runs). Seeding took 1.5–2.5 min.
- The peak was about 3,700 files above the starting count during one run. That figure is mixed with other sessions' changes, so it isn't a clean measurement.
- At 1 CPU per ObsID, batch 2's 50 ObsIDs come to roughly 15–30 core-h if the job fits in 6 GB (cosma5 MaxMemPerCPU). Memory not measured yet; a larger --mem raises the CPUs billed.

Jobs: none (batch 1 ran on the login node, and it has stopped).
Core-h: 0 billed this step; 0 billed since the item began (all #15 work so far was on the login node; batch 1 used about 2.7 h there).
Files: 145,818 (lfs quota, 26 Nov).

SETTLED:
- The fixed recovery set is 3 epochs. The SMC X-3 prep folders and 0831790101's are deleted. 0890710101 and the NGC 2403 08708 folders are kept, because survey targets use them.
- 7 of batch 1's 32 ObsIDs are prepped, all ok.

NEEDS YOU:
1. Batch 1's remaining 25 ObsIDs: should I resume them on the login node as before (about 10–12 h at nice 10, over the one-hour line, so it needs your OK), or move them into the first Slurm job with batch 2's design? I recommend Slurm: same tool, and it frees the login node.

NEXT:
- Carry out your download instruction: the 14 ODFs from the XSA one at a time, then the read-back and completeness test, then source, date and sha256 in INTAKE.md, then prep under the file cap.
- Write the Slurm seed + prep job (1 CPU per ObsID), measure memory on one ObsID, and price batch 2 in core-h and files from batch 1's times before submitting.
- Record batch 1's state in §15.229 and update my checklist line.
