#!/usr/bin/env bash
# Insert the seven state-policy drafts as Blogger drafts (publish each from Blogger -> Posts afterwards).
# Run from the repo root on the Mac after `git pull`.   DRY=1 bash out/publish_state_policy_drafts.sh   previews only.
#   SKIP="key1 key2"   skips posts already inserted.
set -u
FLAG="--draft"; [ "${DRY:-}" = "1" ] && FLAG="--draft --dry-run"
FILES="delhi:out/post-delhi-service-delivery-act-2026.html
states:out/post-india-right-to-service-laws-states.html
aviation:out/post-karnataka-civil-aviation-policy-2026.html
tgcabinet:out/post-telangana-cabinet-5-november-2026.html
tglife:out/post-telangana-life-sciences-policy-2026-30.html
kasector:out/post-karnataka-sector-policies-2026.html
kastartup:out/post-karnataka-startup-policy-2025-30.html"
echo "$FILES" | while IFS=: read -r key file; do
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
