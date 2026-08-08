#!/bin/bash
# Daily: give any newly published post the site-index footer stub.
# Safe to run any time -- inject_site_index.py skips posts already carrying
# the gs-idx marker, so a day with no new posts writes nothing at all.
# Credentials stay in ~/.config/market-secrets (never in the repo or CI).
LOG="$HOME/Library/Logs/masaladeutsch-inject.log"
{
  echo "=== $(date '+%Y-%m-%d %H:%M:%S') inject_site_index"
  /usr/bin/python3 "$HOME/masaladeutsch-archive/tools/inject_site_index.py" --apply
  echo "exit=$?"
} >> "$LOG" 2>&1
