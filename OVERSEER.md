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
- First round: every session posts a full state report. Then reconcile each with the
  instructions of 25 Nov (DECISIONS.md, "Sent 25 Nov") and write each item's first plan.
- The file quota rose by about 29,000 between about 20 and 25 Nov. Alistair was asked to run
  filemap.sh v2 twice and check tmp/. Find the cause before #15's batch 2.
- Confirm whether the §15.133 (C) instruction reached #13.
- The dashboard page: build it once the first reports are in.

### Watch list
- #44: job 12424696 (batch 1, last 25 draws). When it ends, check all 164 records and the billed
  total. The quote was about 110 core-h, cap 200. Then #46 is scored.
- #15: the batch 1 prep run on the login node (10–15 h from 25 Nov 16:33); the 14 XSA downloads.
- merge: mcseed should land first. When it does, #37 runs a95cut's golden check.

### Links between items
- #37's list rerun waits for #38 to merge.
- #13 waits for a95cut and #46.
- #46's option decides the stacked rows above 120 ks (§15.133 (C)), and adds a golden slot (0791010101).
- #23 and #24 wait for the tag.

### Last wake
- (none yet)
