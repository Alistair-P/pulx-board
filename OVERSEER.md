# Overseer

The overseer is Alistair's long-running management conversation. It wakes at 09:00, 12:00, 15:00,
18:00 and 21:00 London time. Its memory is this file, BRIEF.md and DECISIONS.md, not the
conversation. So any new conversation can take over by reading these three.

## Procedure at each wake
0. **Book the next wake first**, using a one-off scheduled message into this conversation. Book the
   next slot of 09:00, 12:00, 15:00, 18:00 or 21:00; after 21:00, book 09:00 the next day. The
   message text is the one under "Wake message" below.
1. **Sync.** Attach Alistair-P/pulx-board with push access and clone it, or pull an existing clone.
   Then `export BOARD_ROLE=overseer`, and run `bash board.sh beat overseer`.
2. **Read.** This file's notebook, DIGEST.md, STATUS.md ("Needs Alistair", "For overseer"),
   `bash board.sh pending` and `bash board.sh ages`. Check that the dispatcher's recent scheduled
   runs succeeded.
3. **Audit the dispatcher.** List every instruction sent since the last overseer heartbeat
   (`git log --since=<last wake> -- items/*/next.md`). Check each one's authority and content. If
   one is wrong, send a correction at once, and note it here.
4. **Decide.** Read in full every report DIGEST.md marks, plus any still pending. Decide within
   POLICY.md, send instructions, and add a DECISIONS.md entry for each decision, with its reason.
5. **Look across items.** Check the merge-queue order against dependencies, the file-quota trend,
   core-h spent against what was approved, items blocked on each other, and idle sessions with no
   plan.
6. **Rewrite the plans.** In STATUS.md, give every active item a plan of numbered, conditional
   steps the dispatcher can follow. An example: "44.2: when 12424696 has finished and all 164
   records read cleanly, score #46 under §15.230 (9) and report." Each step must be checkable from
   a report alone. Add "otherwise: for overseer" where the outcome could go more than one way.
7. **Escalate.** Put each question for Alistair under "Needs Alistair", with its options, a
   recommendation, the cost and the date raised. For a question that changes the science, first
   get a second look. Give BRIEF.md and the evidence, but not your own view, to a separate
   max-effort agent. Then show both views.
8. **Tidy.** Move DIGEST.md's blocks into the commit message (they stay in git history), leaving the
   template. Update the notebook below, commit and push. Send a push notification only if
   "Needs Alistair" gained an entry.
9. **Evening (21:00 wake only).** Write a "Today" section in STATUS.md: what moved, what is
   running overnight, and what waits on Alistair. Send it as one push notification.

If Alistair is in the conversation, his messages come first. A wake that arrives during his turn
waits until the turn ends.

## Wake message
> ultrathink. Overseer wake. Follow the procedure in OVERSEER.md in Alistair-P/pulx-board: book the
> next wake first, then work through steps 1–9. Alistair may be away, so act within POLICY.md and
> put anything else under Needs Alistair.

## Notebook
Keep this short. Remove items once they're settled.

### Open threads
- merge hasn't posted a board report. When it does, check S1 (quota41b at dfa0244, the order,
  intake15, p14a-calib 5f9a009) and add rule 15 to STANDING_RULES with the RULE15.md text.
- File count 144,058–146,194 on 26 Nov, down from about 162,000 on 25 Nov. Watch it as #15's
  Slurm job runs (about 2,600 files per 32 ObsIDs in batch 1).
- #46: #44 is posting the simulation numbers. Check whether (b) beats no stacked arm above
  120 ks by more than its uncertainty, then update Needs Alistair item 1.
- The dashboard page: build it once the first reports are in.

### Watch list
- #37: a95cut golden check (D11). Expected bit-identical, about 11.5 core-h.
- #15: the 14 downloads, then the first Slurm job (39 ObsIDs, D10).
- Merges: rednoise, quota41b, p14a-calib and the rest; each one triggers plan steps.

### Links between items
- #37's list rerun waits for #38 to merge.
- #13 waits for a95cut and #46.
- #46's option decides the stacked rows above 120 ks (§15.133 (C)), and adds a golden slot (0791010101).
- #23 and #24 wait for the tag.

### Last wake
- 26 Nov 17:30, with Alistair present. First pass: 10 board reports read (#38 earlier). D8–D15
  recorded. Instructions sent to 11, 13, 15, 27, 37, 41, 42 and 44; 25 held. Rule 15e fixed (it
  had stopped #44 posting simulation numbers).
