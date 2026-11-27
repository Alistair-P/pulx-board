#!/usr/bin/env bash
# board_watch.sh: nudges a PULX session whose board instruction has gone unread.
#
# A session hears the board through its background "board.sh wait". That wait doesn't survive a
# resumed or restarted conversation, so a session can keep working but stop hearing the board.
# This script runs outside Claude, in its own tmux window. Every few minutes it pulls the board,
# and for each tmux window named after a board ID (merge, 11, 38, ...) it checks three things:
#   1. an instruction is waiting: next.md's seq is above the seq that session last read, and it
#      has waited at least WATCH_GRACE minutes (the session's own wait checks every 3 minutes);
#   2. Claude is running in that window (directly or through a wrapper such as claude-b);
#   3. Claude is idle: not working, and no permission question on screen.
# Then it types one line into that window, asking the session to read the board. It nudges the
# same instruction at most 3 times, at least 30 minutes apart, then logs that Alistair is needed.
# It never types into a window showing a permission question or a busy session.
#
# Usage: bash ~/pulx-board/board_watch.sh [--once] [--dry-run]
#   start it:  tmux new-window -d -t pulx -n watch 'bash ~/pulx-board/board_watch.sh'
#   --once      one pass, then exit;   --dry-run   say what it would type, type nothing
# Environment: BOARD_DIR (default: this script's folder), ZSQW_TMUX (session, default pulx),
#   WATCH_EVERY (seconds between passes, default 300), WATCH_GRACE (minutes, default 10).
set -u
B=${BOARD_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}
SESS=${ZSQW_TMUX:-pulx}
EVERY=${WATCH_EVERY:-300}
GRACE=${WATCH_GRACE:-10}
MAXNUDGE=3
GAP=1800
once=0; dry=0
for a in "$@"; do
    case $a in --once) once=1 ;; --dry-run) dry=1 ;; *) echo "unknown option $a"; exit 1 ;; esac
done
LOG=$B/.local/watch.log
mkdir -p "$B/.local"
log() { printf '%s %s\n' "$(date '+%d %b %H:%M')" "$*" | tee -a "$LOG"; }
note() {  # note <id> <seq> <key> <message>: log a repeating condition at most once an hour
    local f=$B/.local/watchnote_$1 last key=$2:$3 t ok=0
    if [[ -f $f ]]; then read -r last t < "$f"; [[ $last == "$key" ]] && (( $(date +%s) - t < 3600 )) && ok=1; fi
    (( ok )) && return 0
    echo "$key $(date +%s)" > "$f"
    log "$4"
}

seq_of() {  # seq_of <rev> <path>
    local s
    s=$(git -C "$B" show "$1:$2" 2>/dev/null | sed -n '1,8s/^seq: *\([0-9][0-9]*\).*/\1/p' | head -n 1)
    echo "${s:-0}"
}

pane_has_claude() {  # is Claude running anywhere under this window's shell (directly or via a wrapper)?
    local root
    root=$(tmux display-message -p -t "$1" '#{pane_pid}' 2>/dev/null) || return 1
    [[ -n $root ]] || return 1
    ps -e -o pid=,ppid=,comm=,args= 2>/dev/null | awk -v r="$root" '
        { pid = $1; ppid = $2; comm = $3; $1 = $2 = $3 = ""; P[pid] = ppid; C[pid] = comm; A[pid] = $0 }
        END {
            for (p in P) {
                q = p; d = 0
                while (q != r && (q in P) && d < 64) { q = P[q]; d++ }
                if (q != r) continue
                if (C[p] == "claude" || C[p] == "claude-b" || (C[p] == "node" && A[p] ~ /claude/)) found = 1
            }
            exit !found
        }'
}

pass() {
    tmux has-session -t "$SESS" 2>/dev/null || { log "no tmux session '$SESS' on $(hostname -s)"; return; }
    bash "$B/board.sh" sync >/dev/null 2>&1 || log "couldn't pull the board; using the local copy"
    local now id n seen t age screen st sseq scount slast msg
    now=$(date +%s)
    while IFS= read -r id; do
        [[ $id =~ ^[a-z0-9][a-z0-9-]{0,19}$ && -d $B/items/$id ]] || continue
        n=$(seq_of HEAD "items/$id/next.md")
        seen=$(cat "$B/.local/$id.seen" 2>/dev/null || echo 0)
        (( n > seen )) || continue
        t=$(git -C "$B" log -1 --format=%ct HEAD -- "items/$id/next.md" 2>/dev/null)
        age=$(( (now - ${t:-$now}) / 60 ))
        (( age >= GRACE )) || continue
        if ! pane_has_claude "$SESS:$id"; then
            note "$id" "$n" noclaude "$id: instruction $n unread for $age min, but no Claude is running in that window"
            continue
        fi
        screen=$(tmux capture-pane -p -t "$SESS:$id" -S -25 2>/dev/null)
        if grep -qiE 'esc to interrupt' <<<"$screen"; then
            continue            # working; its own wait may still pick the instruction up
        fi
        if grep -qE 'Do you want to|❯ *1\.|[0-9]\. Yes|Yes, and don.t ask' <<<"$screen"; then
            note "$id" "$n" perm "$id: instruction $n unread, but the window shows a permission question; left alone"
            continue
        fi
        st=$B/.local/watch_$id
        sseq=0; scount=0; slast=0
        [[ -f $st ]] && read -r sseq scount slast < "$st"
        if [[ $sseq != "$n" ]]; then scount=0; slast=0; fi
        if (( scount >= MAXNUDGE )); then
            (( scount == MAXNUDGE )) && log "$id: instruction $n still unread after $MAXNUDGE nudges; Alistair needed"
            echo "$n $((MAXNUDGE + 1)) $slast" > "$st"
            continue
        fi
        (( now - slast >= GAP )) || continue
        if [[ $id == merge ]]; then msg="PULX board, merge session:"; else msg="PULX board, item $id:"; fi
        msg+=" board instruction $n is waiting unread. Run bash ~/pulx-board/board.sh show $id and carry it out."
        msg+=" If you were interrupted mid-edit, check for half-finished changes first."
        msg+=" Then start bash ~/pulx-board/board.sh wait $id in the background."
        if (( dry )); then
            log "$id: WOULD NUDGE (instruction $n, unread $age min): $msg"
        else
            tmux send-keys -t "$SESS:$id" -l "$msg"
            sleep 0.5
            tmux send-keys -t "$SESS:$id" Enter
            log "$id: nudged (instruction $n, unread $age min, nudge $((scount + 1)) of $MAXNUDGE)"
            echo "$n $((scount + 1)) $now" > "$st"
        fi
    done < <(tmux list-windows -t "$SESS" -F '#{window_name}' 2>/dev/null)
}

log "board_watch started on $(hostname -s): session $SESS, every $EVERY s, grace $GRACE min$( ((dry)) && echo ', dry run')"
while :; do
    pass
    (( once )) && break
    sleep "$EVERY"
done
