#!/usr/bin/env bash
# Insert the 25 Nov 2026 committee-report drafts. Run from the repo root on the Mac after `git pull`.
#   DRY=1 bash out/publish_nov25_drafts.sh          preview (no write)
#   bash out/publish_nov25_drafts.sh                inserts each as a Blogger draft (press Publish in Blogger -> Posts)
#   LIVE=1 bash out/publish_nov25_drafts.sh         publishes each straight to the blog
#   SKIP="fra dilrmp dbn policylog arjun"           skips posts already inserted (those five are live since 25 Nov 2026)
# Before running: look in Blogger -> Posts for a draft with the same title; delete it first or you get two copies.
set -u
FLAG="--draft"; [ "${LIVE:-}" = "1" ] && FLAG=""
[ "${DRY:-}" = "1" ] && FLAG="$FLAG --dry-run"
FILES="fra:out/post-forest-rights-act-2026-11.html
dilrmp:out/post-dilrmp-standing-committee-41.html
dbn:out/post-digital-bharat-nidhi-32nd-report.html
policylog:out/post-policy-log-october-2026.html
arjun:out/post-arjun-flour-mills-sales-tax.html
oilpsu:out/post-oil-psu-rnd-committee-2026.html
doingbiz:out/post-commerce-committee-doing-business-2026.html"
echo "$FILES" | while IFS=: read -r key file; do
  [ -f "$file" ] || { echo "missing $file"; continue; }
  case " ${SKIP:-} " in *" $key "*) echo "skip $key"; continue;; esac
  title=$(python3 - "$file" <<'PY'
import re,html,sys
t=open(sys.argv[1],encoding="utf-8").read()
print(re.sub(r"<[^>]+>","",html.unescape(re.search(r"<h1[^>]*>(.*?)</h1>",t,re.S).group(1))).strip())
PY
)
  echo "== $key: $title"
  python3 tools/blogger_api.py insert $FLAG --file "$file" --title "$title" || { echo "STOPPED at $key"; exit 1; }
done
