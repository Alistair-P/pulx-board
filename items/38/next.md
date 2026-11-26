seq: 1
from: overseer
authority: overseer: board test, and hold until rednoise merges
date: 2026-11-26T17:04Z
---
#38: this is a test of the board, plus a hold.
1. Post a short idle report with board.sh. Say that this arrived as instruction 1 through board.sh wait, and what time your window picked it up.
2. Don't start the red-noise rebuild yet. Once rednoise is on main, the overseer will decide whether you or #37 rebuilds the production records and reruns a50 and survey_pipeline --list, so the work isn't done twice.
3. Your CLAUDE.md line is with Alistair. Leave it as it is for now.
Then start bash ~/pulx-board/board.sh wait 38 again in the background.
