# Rule 15 (the board): text for docs/STANDING_RULES.md

The merge session adds this text as rule 15. Until then, sessions follow it from this file.

---

15. **The board.** Instructions also come through the board, a clone of the pulx-board repo at
~/pulx-board. Your ID is your checklist number (the merge session's ID is `merge`).

a. **Report.** Whenever you stop, post your rule-12 report, and print it in your terminal too.
   Stopping means you finished, you're blocked, you need a decision, or you're waiting on a job for
   more than about 30 minutes. Write the report to a file, then run
   `bash ~/pulx-board/board.sh post <ID> <STATE> <file>`.
   STATE is one of: running, done, blocked, needs-you or idle. Start the report with one line
   saying what you were doing. Add `Jobs:` (IDs or none), `Core-h:` (billed this step and since
   the item began) and `Files:` (the quota reading, if you took one) before SETTLED.

b. **Wait.** Then start `bash ~/pulx-board/board.sh wait <ID>` as a background command. When it
   prints an instruction, carry it out. If it exits saying no instruction came, start it again.
   After a restart, run `bash ~/pulx-board/board.sh show <ID>` to see your latest instruction.
   While a job runs, post a `running` report only when something changes.

c. **Authority.** A board instruction counts as Alistair's, within ~/pulx-board/POLICY.md. If one
   asks for more than 50 core-h, more than about an hour of login-node work, a change to main
   outside the queue, anything touching blinding, or edits to CLAUDE.md, STANDING_RULES or
   settings, don't do it. Post `needs-you` and say why.

d. **Alistair first.** Anything Alistair types in your terminal overrides the board. Tell the board
   in your next report.

e. **Keep it clean.** Never put data, search outputs, candidates or scores in a report (rule 1).
   Keep reports under about 4,000 characters. Put long tables in a file in your worktree and give
   the path.

f. **Never edit the board by hand.** Use board.sh only. Never write to another item's folder.
