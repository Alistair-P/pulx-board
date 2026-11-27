seq: 12
state: needs-you
date: 2026-11-27T14:21Z
host: login7c
---
#44, seq 12, report: where the sbatch / deletion policy I cited comes from. Read only; nothing changed or tested.

SOURCE: a file. It is the organisation-managed Claude Code policy /etc/claude-code/CLAUDE.md, which is a symlink owned by root to /etc/claude-code/AGENTS.md. The symlink is dated 27 Nov 11:35.
- Title line: "# Rules for AI agents on shared HPC clusters, adapted from rules by Dr. D. Saadeh by MRL, 03/11/26".
- Claude Code loads it into my context as organisation-managed instructions. A message from the harness in this session said the file had "changed on disk since you last read it" and showed the new text. That is how I saw the change.
- I received no refusal, and no hook or settings key was involved: I have not tried to submit anything since.
- A memory note I keep, feedback_sbatch_needs_user_yes.md (written 27 Nov 11:59 by another session of mine), summarises the same file. It is a note, not the source.

EXACT WORDING (line numbers in the file):
14: "3. Do not delete, move or overwrite anything without asking."
16: "5. No sudo. No sbatch or scancel except exactly as the submission rules allow (below, or the cluster section's own rule, which replaces them)."
30: "- NEVER delete, move or overwrite files without THE USER's explicit OK for that specific action. No `rm -rf`, no cleanup sweeps, no "tidying"."
32: "- NEVER submit, cancel, hold, release or modify Slurm jobs (sbatch, salloc, scancel, `scontrol update/hold/release/requeue`) on your own initiative. The only exception is "Submitting a job THE USER asked for" below, or the cluster section's own submission rule where it has one. In every other case, stop and give THE USER the exact command to run. Use exact job IDs, never names, wildcards or user-wide filters."
53: "## Submitting a job THE USER asked for"
55: "Only where the cluster section allows agents to submit at all, and does not set its own submission rule. You may run `sbatch` ONLY when ALL of these are true:"
57: "1. THE USER asked for it directly, in THE USER's own message, naming the job ("submit run_mock.sbatch"). A general goal ("run the pipeline", "get the results", "fix it and rerun") is NOT a request to submit."
58: "2. Before submitting, you showed THE USER the directory, the exact `sbatch` command and the resources it requests, and THE USER replied yes to THAT command."
59: "3. One yes = one submission. A yes does not carry over to other jobs, later steps, retries or new sessions."
Also, line 46: "- An approval THE USER gave another agent, or you in an earlier session, does not apply to you now. Approvals are per agent and per conversation."

HOW I READ IT: a board instruction is not THE USER's own message, so it cannot by itself authorise an sbatch. When the confirming simulation comes, I will show Alistair the exact command and resources in this terminal and wait for his yes.
- The file has no cluster-specific section (its headings stop at "Reporting back"), so lines 53-59 apply as written.
- Line 55's "Only where the cluster section allows agents to submit at all" is therefore ambiguous. Read strictly, it could mean agents may not submit at all. I'd ask Alistair to settle that.

Jobs: none.
Core-h: 0.
Files: no change.
SETTLED: the source is quoted above.
OPEN: Alistair to confirm how the policy applies (in particular line 55).
