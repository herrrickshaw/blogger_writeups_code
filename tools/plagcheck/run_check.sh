#!/bin/bash
# Recurring internal-duplication check across all local post files.
# Three tools, three purposes:
#   JPlag       - structure-aware similarity scan across ALL pairs (fast, holistic)
#   pl-copyfind - WCopyfind/CopyFind-equivalent phrase matcher, run only on the
#                 pairs JPlag flags, to surface the actual matched text
#   copydetect  - winnowing/document-fingerprinting (MOSS-family), a
#                 differently-built third signal over the same corpus
# (Ferret has no reachable current open-source distribution as of Aug 2026 --
# JPlag's text-mode covers the same natural-language duplicate-passage use case.)
set -e
cd "$(dirname "$0")/../.."
REPO=$(pwd)
DATE=$(date +%Y-%m-%d)
JAVA=/opt/homebrew/opt/openjdk/bin/java
PYVENV=~/.venvs/masaladeutsch-plagcheck/bin/python3
OUT="out/plagcheck"
REPORTS="out/plagcheck/reports"
mkdir -p "$REPORTS"

python3 tools/plagcheck/extract_corpus.py "$OUT/txt"

rm -rf "$OUT/jplag-results" "$OUT/jplag-results.jplag"
"$JAVA" -jar tools/plagcheck/bin/jplag-6.3.0.jar "$OUT/txt" -l text -M RUN \
  -r "$OUT/jplag-results" --csv-export --overwrite -m 0.15 \
  > "$OUT/jplag-run.log" 2>&1 || true

node tools/plagcheck/run_copyfind.js "$OUT/jplag-results/results.csv" "$OUT/txt" "$OUT/copyfind-results.json"

"$PYVENV" tools/plagcheck/run_copydetect.py "$OUT/txt" "$OUT/copydetect-results.csv" \
  > "$OUT/copydetect-run.log" 2>&1 || true

python3 tools/plagcheck/build_report.py "$OUT/jplag-results/results.csv" "$OUT/copyfind-results.json" "$OUT/copydetect-results.csv" "$REPORTS/$DATE.md"

echo "report: $REPORTS/$DATE.md"
