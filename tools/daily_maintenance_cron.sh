#!/bin/bash
# Daily maintenance: regenerate the all-posts .md summary (commit+push to
# GitHub, sync to Dropbox), then run the LanguageTool grammar/usage sweep.
#
# The language audit is REPORT-ONLY, same contract as
# tools/multi_model_factcheck.py: it never edits or publishes a post. It
# writes one markdown report per flagged post to out/language_audit/, plus a
# dated summary, for a human to review -- ask "check the language audit
# results" to have them read back. Nothing here auto-applies a suggested fix;
# a manual pass on 2026-08-10 found roughly 85% of LanguageTool's own
# suggestions were false positives, so unattended auto-apply would silently
# introduce real errors into live posts.
set -uo pipefail
cd /Users/umashankar/masaladeutsch-archive

echo "=== $(date '+%Y-%m-%d %H:%M:%S') summary regeneration ==="
/bin/bash tools/update_summary_cron.sh

echo "=== $(date '+%Y-%m-%d %H:%M:%S') language audit (report-only, no publish) ==="
/opt/homebrew/bin/python3 tools/language_audit.py
echo "$(date '+%Y-%m-%d %H:%M:%S') language audit complete -- see out/language_audit/_summary_latest.md"
