#!/bin/bash
# Regenerates MASALADEUTSCH_ALL_POSTS_SUMMARY.md from the current archive,
# commits+pushes it to GitHub if changed, and syncs a copy to Dropbox.
# Run daily via cron; safe to run manually too.
set -euo pipefail
# Repo root relative to this script (see daily_maintenance_cron.sh).
cd "$(dirname "$0")/.." || exit 1

/opt/homebrew/bin/python3 tools/build_md_summary.py

git add MASALADEUTSCH_ALL_POSTS_SUMMARY.md
if ! git diff --cached --quiet -- MASALADEUTSCH_ALL_POSTS_SUMMARY.md; then
  git commit -m "Update all-posts summary $(date +%Y-%m-%d)"
  git push origin main
  echo "$(date '+%Y-%m-%d %H:%M:%S') committed + pushed summary update"
else
  echo "$(date '+%Y-%m-%d %H:%M:%S') no change in summary, skipped commit"
fi

/opt/homebrew/bin/rclone copy MASALADEUTSCH_ALL_POSTS_SUMMARY.md dropbox:archive/vertistrat-archive/ \
  --stats-one-line -v 2>&1 | tail -5
