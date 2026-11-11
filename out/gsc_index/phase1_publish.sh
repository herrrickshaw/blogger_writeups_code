#!/bin/zsh
# Phase 1 of the indexing recovery (10 Nov 2026): publish the merged posts, then the relinked posts,
# then move the 24 absorbed or dead-end posts back to draft. Run from the repo root on the Mac:
#     zsh out/gsc_index/phase1_publish.sh            # does it
#     DRY=--dry-run zsh out/gsc_index/phase1_publish.sh   # shows what it would do
# Order matters: every live link is repointed before any post it used to point at goes to draft.
set -e
cd "${0:A:h}/../.."
DRY=${DRY:-}

# 1. The nine merged posts (each now carries the posts folded into it). Two take new titles.
TARGETS=(050-is-its-own-category-diving-into chemical-import-substitution-hsn-8-registry
  do-cbse-past-papers-actually-help how-to-use-process-safety-design india-ec-approval-funnel-parivesh-20
  indias-wholesale-prices-next-to lok-sabha-question-registry-1843-scheme top-15-chemicals-for-import
  upi-fees-are-now-legal-petrol-pumps)
for s in $TARGETS; do
  title=$(awk -F'\t' -v s="$s" '$1==s{print $2}' out/gsc_index/phase1_titles.tsv)
  echo "== merged: $s ${title:+(new title)}"
  if [[ -n $title ]]; then
    python3 tools/blogger_api.py update --slug $s --file out/update-2026-11-10-$s.html --title "$title" $DRY
  else
    python3 tools/blogger_api.py update --slug $s --file out/update-2026-11-10-$s.html $DRY
  fi
done

# 2. Every other post whose links were repointed or removed (includes the article index).
for f in out/update-2026-11-10-*.html; do
  s=${${f:t:r}#update-2026-11-10-}
  (( ${TARGETS[(Ie)$s]} )) && continue
  echo "== relinked: $s"
  python3 tools/blogger_api.py update --slug $s --file $f $DRY
done

# 3. Back to draft (content kept, can be republished): 12 absorbed posts + 12 dead ends.
python3 tools/blogger_api.py revert-draft --file out/gsc_index/phase1_revert_to_draft.txt $DRY
echo "Phase 1 done. Next: python3 tools/snapshot.py, commit, push."
