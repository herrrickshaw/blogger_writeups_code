#!/usr/bin/env python3
"""After the hubs are published and tools/snapshot.py has run: find each hub's live URL by its title and write
out/research/phase2-hubs/hubs_published.json (hub key -> URL). Fails loudly if any hub is missing or ambiguous."""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[3]
M = json.load(open(ROOT / "meta/manifest.json"))["posts"].values()
norm = lambda s: re.sub(r"\W+", " ", html.unescape(s or "")).strip().lower()
by_title = {}
for p in M:
    by_title.setdefault(norm(p.get("title")), []).append(p["url"])
out, missing = {}, []
for f in sorted(ROOT.glob("out/post-hub-*.html")):
    key = f.name[len("post-hub-"):-5]
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", f.read_text(), re.S).group(1)
    urls = by_title.get(norm(re.sub(r"<[^>]+>", "", h1)), [])
    if len(urls) == 1:
        out[key] = urls[0]
    else:
        missing.append((key, len(urls)))
if missing:
    raise SystemExit(f"not found or ambiguous in manifest: {missing} (publish the hubs and run tools/snapshot.py first)")
(ROOT / "out/research/phase2-hubs/hubs_published.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
