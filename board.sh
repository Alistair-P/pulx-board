#!/usr/bin/env bash
# board.sh: the PULX message board. One folder per checklist item under items/<ID>/.
#   items/<ID>/report.md   the latest rule-12 report. Only that item's session writes it.
#   items/<ID>/next.md     the latest instruction. Only the dispatcher, the overseer or Alistair writes it.
#   items/<ID>/handled     hash of the last report a manager dealt with. Managers only.
# Git history keeps every earlier version. No two writers share a file, so pushes never clash.
#
# Session commands (COSMA):
#   board.sh post ID STATE FILE|-     post your rule-12 report. STATE: running done blocked needs-you idle
#   board.sh wait ID [MINUTES]        wait for a new instruction (default 100 min). Prints it and exits 0.
#                                     Exits 3 if none came; then simply start it again.
#   board.sh show ID                  print your latest instruction (use after a restart)
# Manager commands (dispatcher, overseer):
#   board.sh pending                  items whose latest report hasn't been dealt with
#   board.sh send ID AUTHORITY FILE|- write the next instruction for ID. Needs BOARD_ROLE.
#   board.sh hold ID [NOTE]           mark ID's report dealt with, without sending anything
#   board.sh beat ROLE                record a heartbeat for ROLE (overseer or dispatcher)
#   board.sh ages                     heartbeat ages, and each item's last report and instruction
#   board.sh log ID                   message history for ID
#   board.sh sync                     pull the latest board
#
# Environment: BOARD_DIR (default: this script's folder), BOARD_ROLE (dispatcher|overseer|alistair),
# BOARD_POLL (seconds between checks in wait, default 180), BOARD_COMMIT_TRAILER (text added to commits).
set -u
B=${BOARD_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}
POLL=${BOARD_POLL:-180}
MAXBODY=12000
STATES="running done blocked needs-you idle"

die() { echo "board.sh: $*" >&2; exit 1; }
g() { git -C "$B" "$@"; }
now() { date -u +%Y-%m-%dT%H:%MZ; }
[[ -d $B/.git ]] || die "$B is not the board clone (set BOARD_DIR)"
mkdir -p "$B/.local" || die "cannot write in $B"
LOCKFILE=$B/.git/board.lock

locked() {  # run a command while holding the board lock, so sessions sharing one clone take turns
    ( flock -w 300 9 || { echo "board.sh: lock busy for 5 min" >&2; exit 1; }; "$@" ) 9>"$LOCKFILE"
}
checkid() { [[ ${1:-} =~ ^[a-z0-9][a-z0-9-]{0,19}$ ]] || die "bad item ID '${1:-}' (use the checklist number, or merge)"; }
seq_of() {  # seq_of <git rev> <path>  -> the seq: header of that file at that revision, else 0
    local s
    s=$(g show "$1:$2" 2>/dev/null | sed -n '1,8s/^seq: *\([0-9][0-9]*\).*/\1/p' | head -n 1)
    echo "${s:-0}"
}
field_of() {  # field_of <file> <name>   (prints - if the file or field is missing)
    local v=""
    [[ -f $1 ]] && v=$(sed -n "1,8s/^$2: *//p" "$1" | head -n 1)
    echo "${v:--}"
}
readbody() {  # readbody FILE|-  -> body on stdout
    local src=$1 body
    if [[ $src == - ]]; then body=$(cat); else [[ -f $src ]] || die "no such file: $src"; body=$(cat -- "$src"); fi
    [[ -n ${body//[[:space:]]/} ]] || die "the message is empty"
    (( ${#body} <= MAXBODY )) || die "message is ${#body} characters (limit $MAXBODY). Put long tables in a file and give its path."
    printf '%s\n' "$body"
}
pull() { g pull -q --rebase origin main 2>&1 | grep -v '^$' >&2; return "${PIPESTATUS[0]}"; }
commit() {  # commit "message"   (adds identity if the clone has none, and the optional trailer)
    local msg=$1 id=()
    [[ -n $(g config user.email) ]] || id=(-c "user.name=pulx-${BOARD_ROLE:-session}" -c "user.email=pulx-${BOARD_ROLE:-session}@users.noreply.github.com")
    [[ -n ${BOARD_COMMIT_TRAILER:-} ]] && msg=$(printf '%s\n\n%s' "$msg" "$BOARD_COMMIT_TRAILER")
    g ${id[@]+"${id[@]}"} commit -q -m "$msg"
}
push() {  # push, rebasing on top of anyone who pushed first
    local i
    for i in 1 2 3 4 5 6 7 8; do
        g push -q origin HEAD:main 2>/dev/null && return 0
        if ! pull; then
            g rebase --abort 2>/dev/null
            die "someone changed the same file at the same moment. Your commit is kept locally; run: git -C $B status"
        fi
        sleep $(( (RANDOM % 4) + 1 ))
    done
    die "push failed 8 times (network?). Your commit is kept locally; the next board.sh command will push it."
}

do_post() {
    local id=$1 state=$2 src=$3 body seq f
    checkid "$id"
    [[ " $STATES " == *" $state "* ]] || die "STATE must be one of: $STATES"
    body=$(readbody "$src") || exit 1
    pull || die "cannot reach GitHub"
    seq=$(cat "$B/.local/$id.seen" 2>/dev/null || echo 0)
    f=$B/items/$id/report.md
    mkdir -p "$B/items/$id"
    { printf 'seq: %s\nstate: %s\ndate: %s\nhost: %s\n---\n' "$seq" "$state" "$(now)" "$(hostname -s)"
      printf '%s\n' "$body"; } > "$f"
    g add "items/$id/report.md"
    commit "$id: report ($state, answers seq $seq)"
    push
    echo "Posted $id's report ($state, answers instruction $seq)."
    echo "Next: start 'bash $B/board.sh wait $id' as a background command."
}

do_wait_fetch() { g fetch -q origin main 2>/dev/null; }
do_wait_take() { pull; }
do_wait() {
    local id=$1 mins=${2:-100} seen n start fails=0
    checkid "$id"
    [[ $mins =~ ^[0-9]+$ ]] || die "MINUTES must be a whole number"
    seen=$(cat "$B/.local/$id.seen" 2>/dev/null || echo 0)
    start=$SECONDS
    while :; do
        if locked do_wait_fetch; then fails=0; else
            fails=$((fails + 1)); (( fails == 3 )) && echo "board.sh: can't reach GitHub (3 tries); still trying" >&2
        fi
        n=$(seq_of origin/main "items/$id/next.md")
        if (( n > seen )); then
            locked do_wait_take || true
            echo "New instruction for $id (seq $n):"
            echo
            cat "$B/items/$id/next.md"
            echo "$n" > "$B/.local/$id.seen"
            echo
            echo "When you stop, post your report: bash $B/board.sh post $id STATE FILE"
            exit 0
        fi
        if (( SECONDS - start >= mins * 60 )); then
            echo "No new instruction for $id in $mins min. Start 'bash $B/board.sh wait $id' again."
            exit 3
        fi
        sleep "$POLL"
    done
}

do_show() {
    local id=$1 f n
    checkid "$id"
    pull || echo "board.sh: can't reach GitHub; showing the local copy" >&2
    f=$B/items/$id/next.md
    if [[ -f $f ]]; then
        n=$(seq_of HEAD "items/$id/next.md"); cat "$f"; echo "$n" > "$B/.local/$id.seen"
    else
        echo "(no instruction for $id yet)"
    fi
}

do_pending() {
    local d id r h done_h n=0
    pull || die "cannot reach GitHub"
    for d in "$B"/items/*/; do
        id=$(basename "$d"); r=$d/report.md
        [[ -f $r ]] || continue
        h=$(g hash-object "$r")
        done_h=$(head -n 1 "$d/handled" 2>/dev/null)
        [[ $h == "$done_h" ]] && continue
        printf '%-6s %-9s answers seq %-3s (latest instruction seq %s)  reported %s\n' "$id" \
            "$(field_of "$r" state)" "$(field_of "$r" seq)" "$(seq_of HEAD "items/$id/next.md")" "$(field_of "$r" date)"
        n=$((n + 1))
    done
    echo "$n pending"
}

mark_handled() {  # mark_handled ID -> stages items/ID/handled if there is a report
    local id=$1 r=$B/items/$1/report.md
    [[ -f $r ]] || return 0
    g hash-object "$r" > "$B/items/$id/handled"
    g add "items/$id/handled"
}

do_send() {
    local id=$1 auth=$2 src=$3 body rs ns new role=${BOARD_ROLE:-}
    checkid "$id"
    [[ $role =~ ^(dispatcher|overseer|alistair)$ ]] || die "set BOARD_ROLE to dispatcher, overseer or alistair"
    [[ -n ${auth//[[:space:]]/} ]] || die "AUTHORITY is required (a plan step such as 'plan 44.2', a DECISIONS entry such as 'D7', or 'Alistair')"
    body=$(readbody "$src") || exit 1
    pull || die "cannot reach GitHub"
    rs=$(seq_of HEAD "items/$id/report.md"); ns=$(seq_of HEAD "items/$id/next.md")
    new=$(( (rs > ns ? rs : ns) + 1 ))
    mkdir -p "$B/items/$id"
    { printf 'seq: %s\nfrom: %s\nauthority: %s\ndate: %s\n---\n' "$new" "$role" "$auth" "$(now)"
      printf '%s\n' "$body"; } > "$B/items/$id/next.md"
    g add "items/$id/next.md"
    mark_handled "$id"
    commit "$id: instruction seq $new ($role; $auth)"
    push
    echo "Sent $id instruction $new."
}

do_hold() {
    local id=$1 note=${2:-no instruction needed}
    checkid "$id"
    pull || die "cannot reach GitHub"
    [[ -f $B/items/$id/report.md ]] || die "$id has no report"
    mark_handled "$id"
    if g diff --cached --quiet; then echo "$id was already marked as dealt with."; return 0; fi
    commit "$id: report dealt with, nothing sent (${BOARD_ROLE:-?}: $note)"
    push
    echo "Marked $id's report as dealt with."
}

do_beat() {
    local role=$1
    [[ $role =~ ^(overseer|dispatcher)$ ]] || die "ROLE must be overseer or dispatcher"
    pull || die "cannot reach GitHub"
    mkdir -p "$B/heartbeat"
    printf '%s %s\n' "$(date -u +%s)" "$(now)" > "$B/heartbeat/$role"
    g add "heartbeat/$role"
    commit "heartbeat: $role"
    push
    echo "Heartbeat recorded for $role."
}

do_ages() {
    local f t d id
    pull || echo "board.sh: can't reach GitHub; local copy" >&2
    for f in "$B"/heartbeat/*; do
        [[ -f $f ]] || continue
        read -r t _ < "$f"
        printf 'heartbeat %-10s %s h ago\n' "$(basename "$f")" "$(awk -v a="$(date -u +%s)" -v b="$t" 'BEGIN{printf "%.1f", (a-b)/3600}')"
    done
    for d in "$B"/items/*/; do
        [[ -d $d ]] || continue
        id=$(basename "$d")
        printf '%-6s report: %-9s %-17s  instruction: seq %-3s %s\n' "$id" \
            "$(field_of "$d/report.md" state)" "$(field_of "$d/report.md" date)" \
            "$(field_of "$d/next.md" seq)" "$(field_of "$d/next.md" date)"
    done
}

cmd=${1:-}; shift || true
case $cmd in
    post)    (( $# == 3 )) || die "usage: board.sh post ID STATE FILE|-"; locked do_post "$@" ;;
    wait)    (( $# >= 1 )) || die "usage: board.sh wait ID [MINUTES]"; do_wait "$@" ;;
    show)    (( $# == 1 )) || die "usage: board.sh show ID"; locked do_show "$1" ;;
    pending) locked do_pending ;;
    send)    (( $# == 3 )) || die "usage: board.sh send ID AUTHORITY FILE|-"; locked do_send "$@" ;;
    hold)    (( $# >= 1 )) || die "usage: board.sh hold ID [NOTE]"; locked do_hold "$1" "${2:-}" ;;
    beat)    (( $# == 1 )) || die "usage: board.sh beat ROLE"; locked do_beat "$1" ;;
    ages)    locked do_ages ;;
    log)     (( $# == 1 )) || die "usage: board.sh log ID"; checkid "$1"; g log --date=format:'%d %b %H:%M' --format='%h %ad  %s' -- "items/$1" | head -n 30 ;;
    sync)    locked pull && echo "Board up to date." ;;
    *)       sed -n '2,25p' "${BASH_SOURCE[0]}"; exit 1 ;;
esac
