# Overseer

The overseer is Alistair's long-running management conversation. It wakes at 09:00 and 18:00
London time (D34, D40), and also works whenever Alistair is chatting in it. Keep routine wakes brief, to
save Alistair's usage. Think hard only on flagged decisions. Its memory is this file, BRIEF.md and DECISIONS.md, not the
conversation. So any new conversation can take over by reading these three.

## Procedure at each wake
0. **Book the next wake first**, using a one-off scheduled message into this conversation. Book the
   next slot of 09:00 or 18:00; after 18:00, book 09:00 the next day. The message text is the one
   under "Wake message" below.
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
9. **Morning (09:00 wake only).** Alistair starts work soon after, so finish promptly. Write an
   "Overnight" section at the top of STATUS.md: what moved since 18:00, what's running, and what
   waits on him today. List every terminal ask by window with its exact command and billed core-h,
   so he can clear them in one sweep. Send it as one push notification.
10. **Evening (18:00 wake only).** Write a "Today" section in STATUS.md: what moved, what is
   running overnight, and what waits on Alistair. Send it as one push notification.

If Alistair is in the conversation, his messages come first. A wake that arrives during his turn
waits until the turn ends.

## Wake message
> Overseer wake. Follow the procedure in OVERSEER.md in Alistair-P/pulx-board: book the next wake
> first, then work through steps 1–10. Keep routine wakes brief, and think hard only on decisions
> that are flagged. Alistair may be away, so act within POLICY.md and put anything else under
> Needs Alistair.

## Notebook
Keep this short. Remove items once they're settled.

### Open threads
- D63: #15's stage-1 report (15.4), then Alistair's scope decision (Needs Alistair 2). 37.3, 38.4,
  #13's final certificate and #18's full tag runs all wait on it.
- #38: silent since 26 Nov 17:06. Its rebuild was done (88/88) but not reported. Less urgent now,
  since its records are rebuilt again after D63.
- Dispatcher (27 Nov): it wrote DIGEST blocks inside the format comment and lost the `-->`. Fixed,
  and DISPATCHER.md now says to append below it. Check the digest at the next wake.
- board_watch.sh (27 Nov): runs on COSMA in tmux window "watch". It nudges a session whose
  instruction has gone unread. Log: ~/pulx-board/.local/watch.log. Check it isn't nudging sessions
  that are mid-task.

### Watch list
- Files: 164,367 (27 Nov 17:57). tmp/ clean-up (about 37,000) runs once testshim-tmp merges.
- Merges follow D64's order; each one triggers plan steps.

### Lessons
- Check POLICY.md before instructing (D13 overrode Alistair's own policy wording; #27 refused it).
- An instruction saying "as in instruction N" fails if N was never seen. Always restate it.
- Establish the pipeline's actual baseline before recommending a method change. The study's first
  comparison used a 20" baseline the survey doesn't use (27 Nov); #15's answers corrected it.
- A science change needs the step-7 second look before it goes to Alistair. D63 went without one.

### Last wake
- 27 Nov 18:00 (scheduled; Alistair active until 17:08). Read merge, #15, #11 and #44. Sent: merge
  (D64 order), #15 (regfix conflict, then D63 stage 1, amended for its answers), #11 (swap waits for
  his yes; tag runs wait for D63), #44 (queue longpext; D39 continues). D64 recorded; the D63
  baseline note added. Needs Alistair: D63 scope, 0150280101 X-2. Next wake 28 Nov 09:00
  (trig_01PuM3oxMMSTPAtPmApRT3rS).
- 27 Nov 09:00. Overnight: 9 merges (main 6cd77d3); a95cut golden PASS; (d) built and checked.
