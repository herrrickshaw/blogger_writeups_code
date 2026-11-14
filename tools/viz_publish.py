#!/usr/bin/env python3
"""Publish the verified visual editions (out/viz/<slug>/edition.html) to Blogger, a few at a time. Run on the Mac.

    python3 tools/viz_publish.py --dry-run               # show what would be published, write nothing
    python3 tools/viz_publish.py --limit 20              # publish the next 20, oldest-verified first
    python3 tools/viz_publish.py --only slug-a slug-b    # just these

Before each post goes up the edition is passed through the same link repair the live posts got in Phase 3
(links to the 11 folded posts point at the merged posts), then through migrate_links (no old blogspot domain).
An edition that still links to a post that has been retired or moved to draft is held back and listed.
The result is written to out/viz/<slug>/publish.html (NOT edition.html, and not out/update-*.html, so no other publish
script picks it up) and sent with `blogger_api.py update`. Published slugs are recorded in out/viz/published.json, so a run
that stops at Blogger's daily write ceiling (exit code 3) can simply be started again the next day.

Run order on the Mac: git pull; zsh out/gsc_index/phase3_publish.sh (the merged posts must be live first); then this script.
It only reads and writes under out/viz/ and calls blogger_api.py; it never touches posts/ or meta/."""
import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from blogger_api import migrate_links  # noqa: E402

MAP = json.load(open(ROOT / "out/gsc_index/phase3_map.json"))      # folded slug -> surviving slug
RETIRED = set(json.load(open(ROOT / "out/gsc_index/phase1_remove.json"))) | set(MAP)
try:
    RETIRED |= set(json.load(open(ROOT / "out/gsc_index/phase2_map.json")))
except FileNotFoundError:
    pass
MANIFEST = {p["slug"]: p for p in json.load(open(ROOT / "meta/manifest.json"))["posts"].values()}
PUBLISHED = ROOT / "out/viz/published.json"


def href_re(path):
    return r'href="https?://[^/"]+' + re.escape(path) + r'(?:#[^"]*)?"'


def relink(html):
    """Phase 3 link repair on one post: links to a folded post go to the merged post that absorbed it."""
    for folded, target in MAP.items():
        if folded not in MANIFEST or target not in MANIFEST:
            continue
        path = re.sub(r"^https?://[^/]+", "", MANIFEST[folded]["url"])
        url = MANIFEST[target]["url"]
        html = re.sub(href_re(path), f'href="{url}"', html)
    return html


def retired_links(html):
    return sorted({m for m in re.findall(r"/(?:\d{4}/\d\d/)?([a-z0-9-]+)\.html", html) if m in RETIRED})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    done = set(json.load(open(PUBLISHED))) if PUBLISHED.exists() else set()
    slugs = [d.parent.name for d in sorted(ROOT.glob("out/viz/*/.verified"), key=lambda p: p.stat().st_mtime)]
    slugs = [s for s in slugs if s not in done and (not a.only or s in a.only)]
    held, sent = [], 0
    for s in slugs:
        if a.limit and sent >= a.limit:
            break
        html = migrate_links(relink((ROOT / f"out/viz/{s}/edition.html").read_text(encoding="utf-8")))
        bad = [x for x in retired_links(html) if x != s]
        if bad:
            held.append((s, bad))
            continue
        pub = ROOT / f"out/viz/{s}/publish.html"
        pub.write_text(html, encoding="utf-8")
        print(f"== {s}")
        cmd = [sys.executable, str(ROOT / "tools/blogger_api.py"), "update", "--slug", s, "--file", str(pub)]
        if a.dry_run:
            cmd.append("--dry-run")
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode == 3:
            print(f"stopped at the daily write ceiling after {sent} posts; run again tomorrow")
            break
        if r.returncode == 0:
            sent += 1
            if not a.dry_run:
                done.add(s)
                PUBLISHED.write_text(json.dumps(sorted(done), indent=1))
        else:
            print(f"   not published (exit {r.returncode})")
    print(f"\n{sent} {'checked' if a.dry_run else 'published'}; {len(slugs) - sent - len(held)} still waiting")
    if held:
        print("held back, each links to a retired or draft post (repoint the link, then re-run):")
        for s, bad in held:
            print(f"  {s}: {', '.join(bad)}")


if __name__ == "__main__":
    main()
