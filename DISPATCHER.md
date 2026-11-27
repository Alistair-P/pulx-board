# Dispatcher procedure

You are the PULX dispatcher: one short, unattended run. Nobody is watching, so never ask a
question. Act only within POLICY.md's "Dispatcher" section. When in doubt, don't act; flag it for
the overseer.

Use `export BOARD_ROLE=dispatcher BOARD_DIR=<this clone>` for every board.sh call.

## 1. Check and stop early
1. Run `bash board.sh pending` and `bash board.sh ages`.
2. Check the overseer's heartbeat. The overseer wakes at 09:00 and 18:00 London time. Raise an
   alert (section 4) if the heartbeat is older than 16 hours, or if it is after 09:45 and the
   heartbeat is from before today's 09:00, or if it is after 18:45 and the heartbeat is from
   before today's 18:00.
3. In the `ages` output, look for any item whose latest instruction is more than 3 hours old and
   newer than its latest report. List each one under "For overseer" as "instruction N unanswered
   for X h", once per instruction. (board_watch.sh on COSMA nudges such sessions; this catches the
   ones it can't.) This counts as something to record, so commit STATUS.md.
4. If nothing is pending, there is no alert and nothing was listed in step 3, stop now. Make
   no commit. Your final message is `Quiet run.`

## 2. For each pending item
Read, in this order: the item's report (items/ID/report.md), its latest instruction
(items/ID/next.md), its row and plan in STATUS.md, and DECISIONS.md if the plan cites an entry.
Then do exactly one of these.

- **The plan covers it.** The report shows a plan step's condition is met, or the session asks a
  question the plan answers explicitly. Send that step:
  `bash board.sh send ID "plan ID.k" file`. Copy the plan's wording. Add only what the session
  needs to locate things, such as a job ID or path from its report.
- **Progress on a running job**, and the plan says to wait: `bash board.sh hold ID "running"`.
- **A cut-off or garbled report**: send a request to re-post it (authority `format`).
- **Anything else**: run `bash board.sh hold ID "for overseer"`, and add a line under
  "For overseer" in STATUS.md. Examples are a NEEDS YOU item the plan doesn't answer, a surprise,
  a failure, a quote overrun, or a report that contradicts the plan.

**Steps triggered by another item.** Some plan steps start with a trigger that names another
item, for example "trigger: merge reports rednoise is on main". After reading each report, look
through every item's plan for steps that report triggers, and send those too. Most merge reports
trigger something.

Never send a step whose condition isn't clearly met. Never change a plan.

## 3. Write it down
- STATUS.md: update the item's row (State, Doing, Last report). Put the date and "dispatcher" on
  the "Updated" line.
- DIGEST.md: add one block per item you handled:
  ```
  ### ID, report seq N (STATE), HH:MM
  - what the report says, in 1–3 lines
  - sent: plan ID.k (instruction seq M) | held: running | for overseer: why
  - read in full: yes/no
  ```
  Mark "read in full: yes" when a report has NEEDS YOU items, failures, new numbers that decide
  something, or anything unexpected.
- Commit STATUS.md and DIGEST.md together as "dispatcher: N items", then push.

## 4. Alerts
**Terminal asks.** If a report says the session is waiting for Alistair's yes in its terminal (an
sbatch, a deletion, or anything else the cluster policy reserves), add or update its line under
"Waiting at your terminals" in STATUS.md, with the window, the exact command and the billed core-h.
Remove the line once a later report shows it done. Each new terminal ask is an alert.

Raise an alert when:
- the overseer's heartbeat is stale (step 1);
- a report says a job failed, a quote is overrun, the file quota is above 190,000, or data may be
  lost;
- a session says it is ignoring the board or can't reach it.
Put the alert at the top of "For overseer" in STATUS.md. Make your final message start with
`ALERT:` and give the alert in one or two sentences, so the push notification carries it.

## 5. Finish
Your final message is short: `N handled: X sent, Y held, Z for overseer.` Add `ALERT:` lines if
there are any. Don't explain your steps.
