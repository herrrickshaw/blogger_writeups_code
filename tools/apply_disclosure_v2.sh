#!/usr/bin/env bash
# Apply the reworded AI-disclosure line to every live post, resumably.
#
#   bash tools/apply_disclosure_v2.sh            # live writes
#   bash tools/apply_disclosure_v2.sh --dry-run  # preview only
#
# Reads out/disclosure-v2/post-<slug>.html (generated in the repo) and runs
# blogger_api.py update --slug <slug> for each. Progress is recorded in
# out/disclosure-v2/.done/<slug>, so re-running skips finished posts.
#
# blogger_api.py exit codes: 0 ok | 2 transient (retry) | 3 per-blog daily
# write ceiling reached -> this script STOPS; re-run tomorrow to continue.
# The client itself paces writes (WRITE_GAP_SECONDS); ~256 posts is roughly
# 20 minutes if the ceiling is not hit.
set -u
cd "$(dirname "$0")/.." || exit 1
DIR=out/disclosure-v2
DONE="$DIR/.done"; FAILED="$DIR/.failed.log"
mkdir -p "$DONE"
DRY=""; [ "${1:-}" = "--dry-run" ] && DRY="--dry-run"

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
      echo; echo "Daily write ceiling reached after $ok update(s) this run. Re-run this script tomorrow; it resumes where it stopped."; exit 3
    fi
    if [ $rc -eq 2 ] && [ $attempt -lt 3 ]; then echo "  transient failure, retrying in 30s"; sleep 30; continue; fi
    echo "  FAILED rc=$rc (logged)"; echo "$(date -u +%FT%TZ) $slug rc=$rc" >> "$FAILED"; break
  done
done
echo
echo "Run complete: $ok updated, $skipped already done, $(wc -l < "$FAILED" 2>/dev/null || echo 0) failure line(s) in $FAILED"
[ -z "$DRY" ] && echo "Next: python3 tools/snapshot.py --as patch --note 'AI disclosure reworded sitewide (human-authorship-first, points to Editorial Policy)' --push"
