seq: 10
state: needs-you
date: 2026-11-27T16:07Z
host: login7c
---
#15 (board seq 10, D60): done. NGC4258-J121903.0+471722 in 0400560301 is now held for this epoch with the D60 reason: never staged, and shown as HELD in its PNG and index row. Still open: the hard-QA-rule question and the two reruns, both with Alistair.

1. **The hold (regfix 1a00ba7):**
   - new `new_obs_regions.HOLD_TARGETS`, keyed by (target ID, name), holds one target in one epoch. HOLD_SOURCES still holds a source in every epoch.
   - `stage()` lists it in params_new_obs_held.tsv with the D60 reason, marks it "held" in new_obs_flags.tsv, and writes no params section.
   - I also fixed the staging header, which still said NGC 1313 X-2 is held.
2. **Display:**
   - The PNG banner reads "HELD, NOT STAGED (D60)" in orange, and the caption gives the full reason.
   - index.tsv has a new `held` column, and held rows sort last.
   - Gallery: 9 FAIL, 5 REVIEW, 36 PASS, 1 HELD (51 PNGs).
3. **Tests:** test_regfix 11/0/0. That includes a run of stage() on a temporary tree, which held the target and staged nothing for it, and a check that another epoch of the same source is not held. test_region_review 7/0/0, test_targets18 10/0/0.
4. **--stage was NOT run on the real staging tables.** They are tracked in git, and a run would stage about 40 batch 1 sections ahead of Alistair's #17 review. Instead I ran stage() with its outputs sent to a scratch folder: 0400560301 came out held with the D60 reason and staged nowhere. Because the hold is in the code, every later --stage will hold it.
5. 0674210601 already fails the count gate (net 858), so nothing more is needed there.
6. **Reruns:** 0884030101 and 0150280101 still wait for Alistair's yes in the terminal (commands in report c).

Recorded in §15.229 (30) (intake15 007c54f).

Jobs: none. Core-h: 0 (login only). Files: 175,686.

SETTLED:
- D60: 0400560301's NGC4258-J121903.0+471722 is held for this epoch with its reason, never staged, and shown as HELD.

NEEDS YOU:
1. Alistair: should "not detected AND outshines" (2 targets in batch 1) become a hard QA rule?
2. Alistair, in the terminal: yes or no to the two deletions and two sbatch commands (report c).
3. When should --stage write the real staging tables: after the #17 review, or now?

NEXT:
- After each rerun: check the chosen exposure and barycentring, then run its regions and PNG, then mark pickfix ready.
- Apply any QA rule Alistair sets; run --stage when told.
