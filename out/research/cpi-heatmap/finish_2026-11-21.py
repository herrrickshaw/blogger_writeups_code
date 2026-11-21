#!/usr/bin/env python3
"""Finish the October 2026 CPI heatmap rebuild for publishing (21 Nov 2026).

    python3 out/research/cpi-heatmap/finish_2026-11-21.py      # from the repo root

Reads out/update-2026-11-10-cpi-inflation-heatmap-india-june-2026.html (build_oct2026.py's October rebuild, with the
14 Nov domain migration and the Phase 1 link already applied) and writes out/post-cpi-inflation-heatmap-india-june-2026.html.
Changes, each asserted to apply exactly once:
  - the <h1> still carried the June title; it now states October's finding (docs/HEADLINE_STYLE.md);
  - the update note is dated 21 November, the day it is published;
  - the "other vegetables" sub-class figure names its two drivers, onion and garlic;
  - the sources line records the 21 November re-check against the MoSPI data service.
Every figure in the post was re-fetched from api.mospi.gov.in on 21 Nov 2026 (base 2024, combined): all 37 state rows for
June, September and October, all 12 divisions, the food group and the 9 item-level figures quoted. None had been revised.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "out/update-2026-11-10-cpi-inflation-heatmap-india-june-2026.html"
OUT = ROOT / "out/post-cpi-inflation-heatmap-india-june-2026.html"
TITLE = "CPI inflation by state in India, October 2026: 11 of 36 states and UTs above 6%"
assert len(TITLE) <= 90, len(TITLE)

s = SRC.read_text(encoding="utf-8")


def one(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)


one(">CPI inflation heatmap for India, June 2026: 13 of 28 states, a 3.4-point spread</h1>", f">{html.escape(TITLE, quote=False)}</h1>")
one("<b>Updated 12 November 2026.</b>", "<b>Updated 21 November 2026.</b>")
one("are up 48.08%, cane and beet sugar", "are up 48.08% (onion 116.22%, garlic 60.74%), cane and beet sugar")
one("combined), fetched 12 November 2026;", "combined), fetched 12 November 2026 and re-checked on 21 November 2026 with no revisions found;")

# nothing may still present the post as a June edition, and no old-domain link may be introduced
text = re.sub(r"<[^>]+>", " ", s)
assert not re.search(r"June 2026:", text), "a June title survives"
assert s.count("masaladeutsch") == SRC.read_text(encoding="utf-8").count("masaladeutsch") == 1   # the GitHub-hosted accordion.js, as live
assert "cpi-wpi-trends-mospi-bulletin" not in s                                                      # Phase 1 link stays repointed
OUT.write_text(s, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), "| title", len(TITLE), "chars")
