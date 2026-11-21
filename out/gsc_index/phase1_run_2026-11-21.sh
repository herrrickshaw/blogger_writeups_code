#!/usr/bin/env bash
# Phase 1 as run on 21 Nov 2026 (bash; phase1_publish.sh is the 10 Nov zsh original). Run from the repo root:
#     DRY=--dry-run bash out/gsc_index/phase1_run_2026-11-21.sh     # shows what it would do
#     bash out/gsc_index/phase1_run_2026-11-21.sh                   # does it
# Differences from phase1_publish.sh, found by diffing every draft against the live post on 21 Nov:
#   - merged targets already identical to live are skipped (050-..., chemical-import-substitution-hsn-8-registry,
#     do-cbse-past-papers-actually-help, how-to-use-process-safety-design);
#   - lpgs-missing-number-7308-commission-and is skipped: its 10 Nov draft is older than the live post (a later merge)
#     and the live post links to nothing Phase 1 reverts;
#   - cpi-inflation-heatmap-india-june-2026 is published from a link-only patch of the live body, not its 10 Nov
#     draft, which also carries an unpublished October 2026 data refresh;
#   - two posts published after the plan get link-only patches (phase1_patch_2026-11-21.py);
#   - before any revert, every live post (or the draft about to replace it) is checked for links to the reverted posts.
set -euo pipefail
cd "$(dirname "$0")/../.."
DRY=${DRY:-}
export BLOGGER_ACCESS_TOKEN=${BLOGGER_ACCESS_TOKEN:-proxy-injected}
API="python3 tools/blogger_api.py"
SKIP=" 050-is-its-own-category-diving-into chemical-import-substitution-hsn-8-registry do-cbse-past-papers-actually-help how-to-use-process-safety-design lpgs-missing-number-7308-commission-and cpi-inflation-heatmap-india-june-2026 "
title_of() { awk -F'\t' -v s="$1" '$1==s{print $2}' out/gsc_index/phase1_titles.tsv; }

python3 out/gsc_index/phase1_patch_2026-11-21.py

# 1-2. merged targets and relinked posts from the 10 Nov drafts
for f in out/update-2026-11-10-*.html; do
  s=$(basename "$f" .html); s=${s#update-2026-11-10-}
  [[ $SKIP == *" $s "* ]] && { echo "== skip: $s"; continue; }
  if cmp -s "$f" "posts/$s.html"; then echo "== already live: $s"; continue; fi
  t=$(title_of "$s")
  echo "== publish: $s${t:+ (title from phase1_titles.tsv)}"
  if [[ -n $t ]]; then $API update --slug "$s" --file "$f" --title "$t" $DRY; else $API update --slug "$s" --file "$f" $DRY; fi
done

# 2b. PARIVESH link fixes (12 Nov) and 3. the 21 Nov link-only patches
for f in out/update-2026-11-12-india-forest-wildlife-crz-clearances.html out/update-2026-11-12-india-trade-sector-policy.html \
         out/update-2026-11-21-cpi-inflation-heatmap-india-june-2026.html out/update-2026-11-21-indias-petrochemical-import-tree-from.html \
         out/update-2026-11-21-seven-open-source-tools-for-stock.html; do
  s=$(basename "$f" .html); s=${s#update-2026-11-1[0-9]-}; s=${s#update-2026-11-2[0-9]-}
  echo "== link fix: $s"
  $API update --slug "$s" --file "$f" $DRY
done

# 4. nothing that stays live may link to a post about to go to draft
python3 - <<'EOF'
import glob, json, os, re
rev = [l.strip() for l in open("out/gsc_index/phase1_revert_to_draft.txt") if l.strip() and not l.startswith("#")]
skip = {"050-is-its-own-category-diving-into", "chemical-import-substitution-hsn-8-registry", "do-cbse-past-papers-actually-help",
        "how-to-use-process-safety-design", "lpgs-missing-number-7308-commission-and", "cpi-inflation-heatmap-india-june-2026"}
src = {}
for f in glob.glob("out/update-2026-11-10-*.html"):
    s = f.split("update-2026-11-10-")[1][:-5]
    if s not in skip: src[s] = f
for f in glob.glob("out/update-2026-11-12-*.html") + glob.glob("out/update-2026-11-21-*.html"):
    src[re.sub(r"^update-2026-11-\d\d-", "", os.path.basename(f))[:-5]] = f
bad = {}
for f in glob.glob("posts/*.html"):
    s = os.path.basename(f)[:-5]
    if s in rev: continue
    body = open(src.get(s, f), encoding="utf-8").read()
    hits = [r for r in rev if re.search(r"/\d{4}/\d{2}/" + re.escape(r) + r"\.html", body)]
    if hits: bad[s] = hits
assert not bad, f"still linking to posts about to go to draft: {bad}"
print(f"link check: no post that stays live links to the {len(rev)} posts going to draft")
EOF

# 5. back to draft (content kept; republish with publish-draft)
$API revert-draft --file out/gsc_index/phase1_revert_to_draft.txt $DRY
echo "Phase 1 ${DRY:+(dry run) }done. Next: python3 tools/snapshot.py, commit, push."
