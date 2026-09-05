#!/usr/bin/env bash
# Apply a directory of prepared post bodies to the live blog, resumably.
#
#   bash tools/apply_batch.sh out/<batch-dir>            # live writes
#   bash tools/apply_batch.sh out/<batch-dir> --dry-run  # preview only
#
# Each <batch-dir>/post-<slug>.html is pushed with blogger_api.py update
# --slug <slug>. Progress is recorded in <batch-dir>/.done/<slug>, so a
# re-run skips finished posts. Generalises apply_disclosure_v2.sh, which
# is the same loop pinned to out/disclosure-v2.
#
# blogger_api.py exit codes: 0 ok | 2 transient (retried up to 3x) | 3 the
# per-blog daily write ceiling -> this script STOPS; re-run tomorrow.
set -u
cd "$(dirname "$0")/.." || exit 1
DIR="${1:?usage: apply_batch.sh out/<batch-dir> [--dry-run]}"
DONE="$DIR/.done"; FAILED="$DIR/.failed.log"
mkdir -p "$DONE"
DRY=""; [ "${2:-}" = "--dry-run" ] && DRY="--dry-run"

total=$(ls "$DIR"/post-*.html | wc -l | tr -d ' '); n=0; ok=0; skipped=0
for f in "$DIR"/post-*.html; do
  slug=$(basename "$f" .html); slug=${slug#post-}
  n=$((n+1))
  if [ -z "$DRY" ] && [ -e "$DONE/$slug" ]; then skipped=$((skipped+1)); continue; fi
  attempt=0
  while :; do
    attempt=$((attempt+1))
    printf '[%3d/%3d] %s ' "$n" "$total" "$slug"
    python3 tools/blogger_api.py update --slug "$slug" --file "$f" $DRY
    rc=$?
    if [ $rc -eq 0 ]; then [ -z "$DRY" ] && touch "$DONE/$slug"; ok=$((ok+1)); break; fi
    if [ $rc -eq 3 ]; then
      echo; echo "Daily write ceiling reached after $ok update(s) this run. Re-run tomorrow; it resumes where it stopped."; exit 3
    fi
    if [ $rc -eq 2 ] && [ $attempt -lt 3 ]; then echo "  transient failure, retrying in 30s"; sleep 30; continue; fi
    echo "  FAILED rc=$rc (logged)"; echo "$(date -u +%FT%TZ) $slug rc=$rc" >> "$FAILED"; break
  done
done
echo
echo "Run complete: $ok updated, $skipped already done, $( [ -f "$FAILED" ] && wc -l < "$FAILED" || echo 0) failure line(s) in $FAILED"
