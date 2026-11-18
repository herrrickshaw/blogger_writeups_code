#!/usr/bin/env bash
# Combined run order for the November 2026 publishing backlog. Run on the Mac, from the repo root.
#
#   bash out/run_order_nov2026.sh status            # what is pending (reads only)
#   bash out/run_order_nov2026.sh editions          # visual editions, 20 a run, until Blogger's daily ceiling (exit 3)
#   bash out/run_order_nov2026.sh updates           # update files: the 3 stale-post updates + 57 how-to-use access notes
#   bash out/run_order_nov2026.sh drafts            # insert the 21 new posts as Blogger DRAFTS
#   bash out/run_order_nov2026.sh index             # rebuild the article index and publish it  (do this LAST)
# Add DRY=1 to any stage to show what it would do without writing. Every stage can be rerun: finished work is skipped.
# Nothing is published from the cloud; this script is the Mac-side step the repo rules require.
set -u
cd "$(dirname "$0")/.."
DRY_FLAG=""; [[ -n "${DRY:-}" ]] && DRY_FLAG="--dry-run"
stage="${1:-status}"

live() { [[ -f "posts/$1.html" ]]; }

case "$stage" in
status)
  echo "snapshot posts: $(ls posts | wc -l)   editions: $(ls out/viz/*/edition.html | wc -l)   published editions recorded: $( [[ -f out/viz/published.json ]] && python3 -c "import json;j=json.load(open('out/viz/published.json'));print(len(j))" || echo 0 )"
  python3 tools/viz_publish.py --dry-run | tail -8
  echo "-- update files pending (no access note / not applied in the snapshot):"
  for f in out/update-2026-11-16-*.html; do s=${f#out/update-2026-11-16-}; s=${s%.html}
    if [[ "$s" == how-to-use-* ]]; then grep -q 'data-gs-access-note="1"' "posts/$s.html" 2>/dev/null && continue; fi
    live "$s" && echo "   $s"; done | head -80
  echo "-- drafts not yet in the snapshot: run 'drafts' (inserts are refused for a title already live)"
  ;;
editions)
  python3 tools/viz_publish.py $DRY_FLAG --limit "${LIMIT:-20}"
  rc=$?
  [[ $rc -eq 3 ]] && echo "Blogger's daily write ceiling reached. Run this stage again tomorrow."
  exit $rc
  ;;
updates)
  # Never publish an out/update-* file over an edition of the same slug (the edition supersedes it).
  for f in out/update-2026-11-16-*.html; do s=${f#out/update-2026-11-16-}; s=${s%.html}
    live "$s" || { echo "== not live, skipped: $s"; continue; }
    [[ -f "out/viz/$s/edition.html" ]] && { echo "== has an edition, skipped: $s"; continue; }
    if [[ "$s" == how-to-use-* ]]; then grep -q 'data-gs-access-note="1"' "posts/$s.html" 2>/dev/null && { echo "== already has the note: $s"; continue; }; fi
    echo "== update: $s"
    python3 tools/blogger_api.py update --slug "$s" --file "$f" $DRY_FLAG || { echo "STOPPED at $s (rerun later; finished ones are skipped)"; exit 1; }
  done
  ;;
drafts)
  bash out/publish_all_nov2026_drafts.sh
  echo "Now open each draft in Blogger, check it on a phone width, press Publish."
  echo "Then: python3 tools/snapshot.py && git add -A && git commit -m snapshot && git push, and run the 'index' stage."
  ;;
index)
  git pull --no-rebase origin main || exit 1
  python3 tools/index_graph.py --json /tmp/graph.json &&
  python3 tools/build_index_page.py --graph /tmp/graph.json --out /tmp/fresh-index.html &&
  python3 tools/splice_index_injections.py --fresh /tmp/fresh-index.html --out out/article-index-updated.html || exit 1
  python3 tools/blogger_api.py update --slug article-index-start-here --file out/article-index-updated.html $DRY_FLAG
  ;;
*) echo "usage: $0 status|editions|updates|drafts|index"; exit 2 ;;
esac
