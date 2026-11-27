# PULX board

This repo is the message board for Alistair's PULX survey. The survey itself runs on COSMA, in the
z_sq_weighting repo. This repo holds messages and status, plus the overseer's simulation studies in
studies/ (code and simulated results only, added at Alistair's request on 27 Nov).

## What must never be here
- Data, event files, ODFs, or anything from /cosma5.
- Anything from a search on real data: candidates, scores, statistics or counts (blinding, rule 1).
  Results of simulations, injections, nulls and tests are fine, with their numbers.
- Secrets, keys, tokens or personal details.
A report that would need any of these points to a file path on COSMA instead.

## Who writes what
| File | Written by |
|---|---|
| items/ID/report.md | that item's COSMA session only, through `board.sh post` |
| items/ID/next.md | the dispatcher, the overseer or Alistair, through `board.sh send` |
| items/ID/handled | managers, through `board.sh send` or `board.sh hold` |
| heartbeat/* | `board.sh beat` |
| STATUS.md, DIGEST.md | the dispatcher and the overseer |
| BRIEF.md, POLICY.md, DISPATCHER.md, OVERSEER.md, DECISIONS.md, RULE15.md | the overseer (Alistair's answers go in DECISIONS.md too) |
| board.sh, CLAUDE.md, .claude/ | the overseer, with Alistair's agreement |
| studies/* | the overseer. Sessions read them and run them only from outside the board clone |

Use `board.sh` for every message. Never edit report.md or next.md by hand.

## The three levels
- **Dispatcher**: an hourly scheduled run. It follows DISPATCHER.md and acts only on written plans.
- **Overseer**: Alistair's long-running management conversation, woken every three hours. It follows OVERSEER.md.
- **Alistair**: decides everything POLICY.md reserves for him. His word overrides the board.

## Sources of truth
CHECKLIST.md, summary.txt §15 and docs/STANDING_RULES.md on COSMA are the record. The board only
carries messages. If the board and the record disagree, the record wins; flag the difference.

## Commits
Small commits, one purpose each. If a push is rejected, `git pull --rebase` and push again. If a
rebase conflicts on STATUS.md or DIGEST.md, take the remote version and redo your own edits on top.
