#!/usr/bin/env bash
# AI tools edition 05 (new post) and the update to edition 04 (existing post). Run from the repo root on the Mac after `git pull`.
#   DRY=1 bash out/publish_edition05.sh      preview, no write
#   bash out/publish_edition05.sh            1) insert edition 05 as a Blogger draft, 2) update edition 04 in place
#   LIVE=1 bash out/publish_edition05.sh     publish edition 05 live instead of a draft
# Check Blogger -> Posts for an existing draft of the edition 05 title first, or you get two copies.
set -u
DRYFLAG=""; [ "${DRY:-}" = "1" ] && DRYFLAG="--dry-run"
DRAFT="--draft"; [ "${LIVE:-}" = "1" ] && DRAFT=""
TITLE=$(python3 - <<'PY'
import re,html
t=open("out/post-ai-tools-edition-05.html",encoding="utf-8").read()
print(re.sub(r"<[^>]+>","",html.unescape(re.search(r"<h1[^>]*>(.*?)</h1>",t,re.S).group(1))).strip())
PY
)
echo "== edition 05: $TITLE"
python3 tools/blogger_api.py insert $DRAFT $DRYFLAG --file out/post-ai-tools-edition-05.html --title "$TITLE" || { echo "STOPPED at edition 05"; exit 1; }
echo "== edition 04 update"
python3 tools/blogger_api.py update --slug ai-tools-edition-04-deepseek-put-its --file out/update-2026-11-25-ai-tools-edition-04.html $DRYFLAG || { echo "STOPPED at edition 04 update"; exit 1; }
