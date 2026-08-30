#!/bin/bash
# Daily maintenance: regenerate the all-posts .md summary (commit+push to
# GitHub, sync to Dropbox), run the LanguageTool grammar/usage sweep, and
# pull a GA4 traffic snapshot.
#
# The language audit and GA4 report are both REPORT-ONLY, same contract as
# tools/multi_model_factcheck.py: nothing here edits or publishes a post, or
# changes any GA/Blogger setting. Ask "check the language audit results" or
# "check the GA report" to have them read back. Nothing here auto-applies a
# suggested language fix -- a manual pass on 2026-08-10 found roughly 85% of
# LanguageTool's own suggestions were false positives, so unattended
# auto-apply would silently introduce real errors into live posts.
set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
export GH_TOKEN="$(cat "$HOME/.config/gh_cron_token" 2>/dev/null)"
# Repo root relative to this script, so the chain is not tied to one machine.
# (The absolute python3 below stays: cron runs with a minimal PATH.)
cd "$(dirname "$0")/.." || exit 1

echo "=== $(date '+%Y-%m-%d %H:%M:%S') summary regeneration ==="
/bin/bash tools/update_summary_cron.sh

echo "=== $(date '+%Y-%m-%d %H:%M:%S') language audit (report-only, no publish) ==="
/opt/homebrew/bin/python3 tools/language_audit.py
echo "$(date '+%Y-%m-%d %H:%M:%S') language audit complete -- see out/language_audit/_summary_latest.md"
# Pushed to GitHub, same reasoning as the GA4 report below: a cloud routine
# has no access to this machine's disk, so cross-referencing traffic against
# flagged posts needs both reports available in the repo.
git add out/language_audit/
if ! git diff --cached --quiet -- out/language_audit/; then
  git commit -m "Language audit snapshot $(date +%Y-%m-%d)"
  git push origin main
  echo "$(date '+%Y-%m-%d %H:%M:%S') language audit committed + pushed"
fi

echo "=== $(date '+%Y-%m-%d %H:%M:%S') GA4 traffic report (report-only) ==="
mkdir -p out/ga_report
today=$(date +%Y-%m-%d)
if /opt/homebrew/bin/python3 tools/ga_report.py --days 28 --out "out/ga_report/${today}.md"; then
  cp "out/ga_report/${today}.md" out/ga_report/latest.md
  echo "$(date '+%Y-%m-%d %H:%M:%S') GA4 report complete -- see out/ga_report/latest.md"
  # Pushed to GitHub (unlike the language audit, which stays local-only) so a
  # cloud routine with no access to this machine's disk can read the latest
  # snapshot straight from the repo.
  git add out/ga_report/
  if ! git diff --cached --quiet -- out/ga_report/; then
    git commit -m "GA4 report snapshot ${today}"
    git push origin main
    echo "$(date '+%Y-%m-%d %H:%M:%S') GA4 report committed + pushed"
  fi
else
  echo "$(date '+%Y-%m-%d %H:%M:%S') GA4 report FAILED -- see output above (previous latest.md left untouched)"
fi
