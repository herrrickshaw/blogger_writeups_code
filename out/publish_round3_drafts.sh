#!/usr/bin/env bash
# Insert the six drafts written after the seven state-policy posts (Andhra Pradesh, Odisha, GCC, semiconductors, Madhya Pradesh, West Bengal).
# Run from the repo root on the Mac after `git pull`.
#   DRY=1 bash out/publish_round3_drafts.sh     previews only (no writes).
#   bash out/publish_round3_drafts.sh           inserts each post as a Blogger DRAFT; publish from Blogger -> Posts afterwards.
#   LIVE=1 bash out/publish_round3_drafts.sh    publishes each post live straight away. Use ONE of the two modes, not both:
#                                               doing a draft run and then a LIVE run (or publishing the drafts and then running LIVE) makes two live copies.
#   SKIP="key1 key2"   skips posts already inserted.
# The two earlier runs of publish_state_policy_drafts.sh left five posts live twice (21 Nov, 09:37 and 09:38 UTC); this script refuses to start while any
# title is live more than once, and the insert command itself refuses a title that is already live.
set -u
FLAG="--draft"; [ "${LIVE:-}" = "1" ] && FLAG=""
[ "${DRY:-}" = "1" ] && FLAG="$FLAG --dry-run"

echo "== checking for duplicate live titles first"
dups=$(python3 tools/blogger_api.py duplicates 2>&1)
echo "$dups" | head -30
if echo "$dups" | grep -q "no duplicate titles"; then
  :   # clean: carry on
elif echo "$dups" | grep -q "DELETE"; then
  echo "STOPPED: live duplicates exist. Review the list above (KEEP = earliest copy, no _digits suffix), then remove the later copies with"
  echo "  python3 tools/blogger_api.py duplicates --delete-newer --yes      (permanently deletes the DELETE lines)"
  exit 1
else
  echo "STOPPED: could not check for duplicates (not authorised? run: python3 tools/blogger_api.py auth). Nothing was written."
  exit 1
fi
echo "== also check Blogger -> Posts (or: python3 tools/blogger_api.py drafts) for drafts with the same titles; draft inserts are not checked against existing drafts."

FILES="ap:out/post-andhra-pradesh-cabinet-10-november-2026.html
odisha:out/post-odisha-cabinet-9-november-2026.html
gcc:out/post-state-gcc-policies-india-2026.html
semi:out/post-state-semiconductor-support-india-2026.html
mp:out/post-madhya-pradesh-parks-18-november-2026.html
wb:out/post-west-bengal-investment-policy-2026.html"
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

cat <<'EOF'

Next (not run by this script):
  # the two update notes on already-published posts: dry-run each first, then without --dry-run
  python3 tools/blogger_api.py update --slug indias-labour-codes-took-six-years-to --file out/update-2026-11-21-indias-labour-codes-took-six-years-to.html \
    --title "India's labour codes: final rules under all four in 5 to 7 of 36 or 37 states and UTs" --dry-run
  python3 tools/blogger_api.py update --slug fourteen-states-reimburse-investors --file out/update-2026-11-21-fourteen-states-reimburse-investors.html --dry-run
  # then record the version levels per post, never with a global --as major:
  python3 tools/snapshot.py --as-slug indias-labour-codes-took-six-years-to=major --as-slug fourteen-states-reimburse-investors=major \
    --note "21 Nov updates: labour codes, SGST note" --push
EOF
