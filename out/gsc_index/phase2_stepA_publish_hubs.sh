#!/bin/zsh
# Phase 2, step A (12 Nov 2026): publish the nine hub posts. Nothing is reverted or relinked yet.
#     DRY=--dry-run zsh out/gsc_index/phase2_stepA_publish_hubs.sh   # preview
#     zsh out/gsc_index/phase2_stepA_publish_hubs.sh                 # publish
# Then: python3 tools/snapshot.py, commit, push. Step B (link repair + reverting the 50 guides) is built from that snapshot.
set -e
cd "${0:A:h}/../.."
DRY=${DRY:-}
for f in out/post-hub-*.html; do
  title=$(python3 -c 'import html,re,sys;t=open(sys.argv[1]).read();print(html.unescape(re.sub(r"<[^>]+>","",re.search(r"<h1[^>]*>(.*?)</h1>",t,re.S).group(1))).strip())' $f)
  echo "== $f"
  echo "   $title"
  python3 tools/blogger_api.py insert --file $f --title "$title" $DRY
done
echo "Step A done. Next: python3 tools/snapshot.py, commit, push."
