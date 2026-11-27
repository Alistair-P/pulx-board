# Who may decide what

There are three levels. When you are unsure which level a decision belongs to, pass it up one level.

## Dispatcher (hourly scheduled run)

It may:
1. Send a step that is written in the item's plan in STATUS.md, when the report shows the plan's
   condition is met. Copy the step's wording. Its authority is the plan step, for example `plan 44.2`.
2. Re-send the current instruction if a session says it lost it (authority `resend`).
3. Ask a session to re-post a report that is cut off, garbled or missing the rule-12 sections
   (authority `format`).
4. Do nothing (`board.sh hold`) when a session reports progress and its plan says to wait.

It may not do anything else. It never answers a NEEDS YOU item unless the plan answers it
explicitly. Everything else goes under "For overseer" in STATUS.md, untouched.

## Overseer (management conversation, every three hours)

It may do these, each with a DECISIONS.md entry that gives the reason:
1. Choose between options a session offers, when the choice is technical and doesn't change the
   science. That covers implementation, order of work, tooling, tests and docs.
2. Approve compute up to 50 core-h billed, and up to about an hour of login-node work, per step,
   within what the item is already meant to do.
3. Order the merge queue within the agreed order, and tell a session to queue or not.
4. Approve fixes for bugs. After the v1.0 tag, only bug fixes may touch the search layer (rule 11).
5. Write and revise plans, and correct or withdraw any dispatcher instruction.
6. Apply the file-quota rules, including the #16 batch cap.
7. Answer a session's NEEDS YOU items that fall inside these limits.

## Alistair only ("Needs Alistair")

- More than 50 core-h billed, or more than about an hour of login-node work, in one step. Also any
  run that would exceed the price he approved.
- Anything that changes the science. That covers thresholds, β or the weights, the arms, sample and
  inclusion cuts, validation and decision rules, ADOPTED lines, and the detection policy (#27).
- Anything touching blinding (rule 1) or unblinding.
- Changes to main outside the merge queue, and tagging v1.0.
- Edits to CLAUDE.md, STANDING_RULES, settings or permissions in z_sq_weighting. Even when
  DECISIONS.md records his approval, Alistair confirms these in that session's own terminal,
  because rule 15c makes a session refuse them from the board.
- Deleting data, ODFs, worktrees or branches. Downloads from the XSA beyond a list he approved.
- Starting a new checklist item or session.
- Anything a session addresses to Alistair by name, and his own items.

## Jobs and deletions (cluster policy, 27 Nov)
On COSMA, every `sbatch` and every deletion now needs Alistair's own yes in that session's terminal,
for the exact command shown. A board instruction can approve a job's price and scope. The session
then prepares the exact command and asks him in its terminal. The overseer lists these waiting asks
under "Waiting at your terminals" in STATUS.md. Never ask a session to get around this.

## Every instruction
- Names its authority. Covers one item. Plain text, under about 4,000 characters.
- Refers to files by their COSMA path; never pastes data.
- Never asks for anything rule 15 lets a session refuse.
- A session sees only its latest instruction. If you send one before the previous one was
  answered, the new one must repeat everything still needed from the previous one.
- Ends with "Update your checklist line, and end with the rule-12 report." when work is asked for.
