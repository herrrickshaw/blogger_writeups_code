#!/usr/bin/env bash
# Update drafts of the 25 Nov 2026 sweep (slices A and B; slice C found nothing). Run from the repo root on the Mac after fetching the files.
#   DRY=1 bash out/publish_sweep_2026_11_25.sh        preview, no write
#   bash out/publish_sweep_2026_11_25.sh              the twelve additive updates (an update block is added, nothing removed)
#   WITH_REWRITES=1 bash out/publish_sweep_2026_11_25.sh   also the three drafts that rewrite existing text (quantum, paprika oleoresin, wine); read them first
#   SKIP="key ..."                                    skip posts already updated
# The sweep session removed the live accordion <script> tag from every draft. Publishing as-is would drop that tag
# from the live posts, so by default this script puts the tag back before updating. Set KEEP_STRIPPED=1 to publish the drafts exactly as written.
set -u
DRYFLAG=""; [ "${DRY:-}" = "1" ] && DRYFLAG="--dry-run"
TAG='<div id="gs-idx"></div><script defer="defer" src="https://herrrickshaw.github.io/masaladeutsch/accordion.js"></script>'
ADD="punjab:379-kilos-hectare-in-punjab-44-in
alimco:alimco-jaipur-foot-and-bionic-gap-in
ahidf:ahidf-has-sanctioned-19751-crore-in
dap:india-raised-dap-subsidy-18-this-kharif
maize:ethanol-plants-that-trade-maize-to
namrup:thirty-one-years-of-asking-parliament
rooftop:rooftop-solar-is-working-household
reactor:the-reactor-nobody-names-how-coal
corsia:under-corsias-own-numbers-corn-ethanol
health2:indias-two-tracks-of-health-cover-and
oop:most-of-what-indians-pay-for-health-is
idbi:idbi-banks-rescuers-put-in-54000-crore"
REW="quantum:indias-military-quantum-plan-has-four
paprika:india-sells-world-about-third-of-its
wine:a-million-wine-market-behind-150-wall"
LIST="$ADD"; [ "${WITH_REWRITES:-}" = "1" ] && LIST="$ADD
$REW"
echo "$LIST" | while IFS=: read -r key slug; do
  case " ${SKIP:-} " in *" $key "*) echo "skip $key"; continue;; esac
  f="out/update-2026-11-25-$slug.html"; [ -f "$f" ] || { echo "missing $f"; continue; }
  use="$f"
  if [ "${KEEP_STRIPPED:-}" != "1" ] && ! grep -q "accordion.js" "$f"; then
    use="/tmp/sweep-$slug.html"
    python3 - "$f" "$use" "$TAG" <<'PY'
import sys
src,dst,tag=sys.argv[1:4]
t=open(src,encoding="utf-8").read()
a='<div id="gs-idx"></div>'
assert t.count(a)==1, "gs-idx stub not found exactly once"
open(dst,"w",encoding="utf-8").write(t.replace(a,tag))
PY
  fi
  echo "== $key: $slug"
  python3 tools/blogger_api.py update --slug "$slug" --file "$use" $DRYFLAG || { echo "STOPPED at $key"; exit 1; }
done
