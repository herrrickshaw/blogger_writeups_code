#!/usr/bin/env python3
"""Link-only patches needed to run Phase 1 on 21 Nov 2026, eleven days after it was planned.

    python3 out/gsc_index/phase1_patch_2026-11-21.py      # from the repo root

Writes out/update-2026-11-21-<slug>.html for three live posts that link to posts Phase 1 sends to draft:
  cpi-inflation-heatmap-india-june-2026  -- its Phase 1 draft (out/update-2026-11-10-...) also carries an unpublished
                                            October 2026 data refresh, out of Phase 1's scope; this patch changes the
                                            one link only, on the live body.
  indias-petrochemical-import-tree-from  -- published after the plan (14 Nov), not covered by it.
  seven-open-source-tools-for-stock      -- published after the plan (14 Nov), not covered by it.
Each link is repointed to the post that absorbed the reverted one (phase1_remove.json). In "Related" lists its text
becomes that post's current title, as the Phase 1 relinks do; an inline link inside a sentence (KEEP_TEXT) keeps its
words, which still describe the absorbing post. Nothing else in the body changes.
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
B = "https://blog.vertistratsolution.com"
absorbed = json.loads((ROOT / "out/gsc_index/phase1_remove.json").read_text())
PATCH = {"cpi-inflation-heatmap-india-june-2026": ["cpi-wpi-trends-mospi-bulletin"],
         "indias-petrochemical-import-tree-from": ["chemical-import-substitution-analysis"],
         "seven-open-source-tools-for-stock": ["below-250-is-where-real-junk-lives"]}
KEEP_TEXT = {"cpi-inflation-heatmap-india-june-2026"}   # "The companion CPI &amp; WPI trend piece tracks ..."

for slug, olds in PATCH.items():
    body = (ROOT / f"posts/{slug}.html").read_text(encoding="utf-8")
    new = body
    for old in olds:
        tgt = absorbed[old]
        assert tgt, f"{old} has no merge target"
        m = json.loads((ROOT / f"meta/{tgt}.json").read_text())
        url, title = m["url"], html.escape(m["title"], quote=False)
        pat = re.compile(r'(<a\b[^>]*href=")' + re.escape(B) + r'/\d{4}/\d{2}/' + re.escape(old) + r'\.html("[^>]*>)(.*?)(</a>)', re.S)
        new, n = pat.subn(lambda g: g[1] + url + g[2] + (g[3] if slug in KEEP_TEXT else title) + g[4], new)
        assert n >= 1, (slug, old)
        assert old not in new, (slug, old, "still referenced")
        print(f"{slug}: {old} -> {tgt} ({n} link{'s' if n > 1 else ''})")
    # everything outside the changed <a> elements must be byte-identical
    strip = lambda s: re.sub(r'<a\b[^>]*>.*?</a>', '<a/>', s, flags=re.S)
    assert strip(new) == strip(body), slug
    (ROOT / f"out/update-2026-11-21-{slug}.html").write_text(new, encoding="utf-8")
