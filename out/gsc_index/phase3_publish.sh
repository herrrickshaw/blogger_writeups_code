#!/bin/zsh
# Phase 3 (14 Nov 2026): publish 7 merged posts, repoint links to the 11 posts folded into them, publish the
# rebuilt index, then move the folded posts to draft. Run from the repo root on the Mac:
#     zsh out/gsc_index/phase3_publish.sh                  # does it
#     DRY=--dry-run zsh out/gsc_index/phase3_publish.sh    # shows what it would do
# Order matters: every link is repointed before the post it pointed at goes to draft.
set -e
cd "${0:A:h}/../.."
DRY=${DRY:-}
# Resume support (16 Nov 2026): FROM=<slug> skips step 1 and every relink that sorts before that slug (use after a stop);
# SKIP="slug1 slug2" skips those relinks (use when a post is not live). Both are for re-runs only; a first run needs neither.
FROM=${FROM:-}
SKIP=${SKIP:-}
newest() { ls out/update-2026-11-1[45]-$1.html 2>/dev/null | sort | tail -1 }

# 1. The seven merged posts, each with its new title (read from the file's <h1>).
for s in $(python3 -c "import json;print(' '.join(sorted(set(json.load(open('out/gsc_index/phase3_map.json')).values()))))"); do
  [[ -n $FROM ]] && continue
  f=$(newest $s)
  title=$(python3 -c "import re,html,sys;t=open(sys.argv[1]).read();print(html.unescape(re.sub('<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S).group(1))).strip())" $f)
  echo "== merged: $s  ($f)"
  python3 tools/blogger_api.py update --slug $s --file $f --title "$title" $DRY
done

# 2. Every other post whose links to a folded post were repointed (relink3.py output).
for f in out/update-2026-11-15-*.html; do
  s=${f:t:r}; s=${s#update-2026-11-15-}
  python3 -c "import json,sys;sys.exit(0 if sys.argv[1] in set(json.load(open('out/gsc_index/phase3_map.json')).values()) else 1)" $s && continue
  [[ -n $FROM && $s < $FROM ]] && continue
  [[ " $SKIP " == *" $s "* ]] && { echo "== skipped: $s"; continue; }
  echo "== relinked: $s"
  python3 tools/blogger_api.py update --slug $s --file $f $DRY
done

# 3. The rebuilt article index (folded posts removed, new titles).
echo "== index"
python3 tools/blogger_api.py update --slug article-index-start-here --file out/update-2026-11-14-article-index-start-here.html $DRY

# 4. Back to draft (content kept, can be republished): the 11 folded posts.
python3 tools/blogger_api.py revert-draft --file out/gsc_index/phase3_revert_to_draft.txt $DRY
echo "Phase 3 done. Next: python3 tools/snapshot.py && git push -q"
