#!/usr/bin/env python3
"""Rebuild the article index from what is live, already in its post-Phase-1 shape.

    python3 out/gsc_index/rebuild_index.py            # from the repo root

Runs tools/index_graph.py, then leaves out the posts Phase 1 sends back to draft
(phase1_revert_to_draft.txt, and any related links to them), applies the new titles in
phase1_titles.tsv, and builds with tools/build_index_page.py inside the existing page shell
(out/idx-shell-head.html, out/idx-shell-tail.html). Every link uses blog.vertistratsolution.com.

Writes the same body to two places, so the order of publishing does not matter:
  out/update-2026-11-14-article-index-start-here.html   publish now
  out/update-2026-11-10-article-index-start-here.html   what phase1_publish.sh republishes later
"""
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from blogger_api import migrate_links  # noqa: E402

G = ROOT / "out/gsc_index"
revert = {l.strip() for l in (G / "phase1_revert_to_draft.txt").read_text().splitlines()
          if l.strip() and not l.startswith("#")}
titles = dict(l.split("\t", 1) for l in (G / "phase1_titles.tsv").read_text().splitlines() if "\t" in l)
# house-style titles (docs/HEADLINE_STYLE.md), applied before the next snapshot catches up
RT = ROOT / "out/retitle/titles.tsv"
if RT.exists():
    titles.update(dict(l.split("\t", 1) for l in RT.read_text(encoding="utf-8").splitlines() if "\t" in l))

with tempfile.TemporaryDirectory() as td:
    graph = pathlib.Path(td) / "graph.json"
    subprocess.run([sys.executable, str(ROOT / "tools/index_graph.py"), "--json", str(graph)], check=True)
    g = json.loads(graph.read_text())
    dropped = [s for s in g if s in revert]
    for s in dropped:
        del g[s]
    for s, p in g.items():
        if s in titles:
            p["title"] = titles[s].strip()
        if isinstance(p.get("related"), list):
            p["related"] = [r for r in p["related"] if r.get("slug") not in revert]
    graph.write_text(json.dumps(g))
    out = pathlib.Path(td) / "index.html"
    subprocess.run([sys.executable, str(ROOT / "tools/build_index_page.py"), "--graph", str(graph), "--out", str(out),
                    "--shell-head", str(ROOT / "out/idx-shell-head.html"),
                    "--shell-tail", str(ROOT / "out/idx-shell-tail.html")], check=True)
    body = migrate_links(out.read_text(encoding="utf-8"))

assert "masaladeutsch.blogspot.com" not in body
for d in ("2026-11-14", "2026-11-10"):
    (ROOT / f"out/update-{d}-article-index-start-here.html").write_text(body, encoding="utf-8")
print(f"left out {len(dropped)} Phase 1 draft posts; retitled {sum(s in g for s in titles)}; "
      f"{body.count('blog.vertistratsolution.com'):,} links on the new domain")
