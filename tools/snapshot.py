#!/usr/bin/env python3
"""Snapshot every published masaladeutsch post into the archive and commit the diff.

Pulls the Blogger public feed (which carries full post bodies), writes one HTML
file plus one JSON sidecar per post, regenerates the manifest, appends a
human-readable entry to CHANGELOG.md, and commits.

    python3 tools/snapshot.py                 # snapshot + commit
    python3 tools/snapshot.py --note "..."    # add a reason to the commit/changelog
    python3 tools/snapshot.py --no-commit     # write files only

Drafts are NOT in the public feed. Blogger has no unauthenticated draft access,
so a drafted post looks identical to a deleted one from here. Anything drafted or
deleted on purpose should be captured into posts/ by hand first (see
tools/capture_draft.md), otherwise the snapshot records it as "removed".
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BLOG = "https://masaladeutsch.blogspot.com"
ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
META = ROOT / "meta"
MANIFEST = META / "manifest.json"
CHANGELOG = ROOT / "CHANGELOG.md"
UA = "Mozilla/5.0 (masaladeutsch-archive snapshot)"
PAGE = 100


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8")


def feed_page(start):
    q = urllib.parse.urlencode(
        {"alt": "json", "max-results": PAGE, "start-index": start}
    )
    return json.loads(fetch(f"{BLOG}/feeds/posts/default?{q}"))["feed"]


def all_entries():
    out, start = [], 1
    while True:
        feed = feed_page(start)
        entries = feed.get("entry", [])
        if not entries:
            break
        out.extend(entries)
        total = int(feed["openSearch$totalResults"]["$t"])
        start += len(entries)
        if start > total:
            break
    return out


def slug_of(url):
    tail = urllib.parse.urlparse(url).path.rsplit("/", 1)[-1]
    return re.sub(r"\.html$", "", tail) or "index"


def parse(entry):
    url = next(l["href"] for l in entry["link"] if l["rel"] == "alternate")
    body = entry.get("content", {}).get("$t", "")
    return {
        "id": entry["id"]["$t"].rsplit(".post-", 1)[-1],
        "title": entry["title"]["$t"],
        "url": url,
        "slug": slug_of(url),
        "published": entry["published"]["$t"],
        "updated": entry["updated"]["$t"],
        "labels": sorted(t["term"] for t in entry.get("category", [])),
        "bytes": len(body),
        "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
    }, body


# Design/template markers this blog's house style depends on. Tracked per post so
# a regression (a lost light-lock, a re-spliced disclaimer) shows up in the diff
# even when the prose is untouched.
MARKERS = {
    "light_lock": lambda b: "gs-light-lock" in b,
    "dark_panel_guard": lambda b: "gs-dark-panel-guard" in b,
    "typo_unify": lambda b: "gs-typo-unify" in b,
    "translate_widget": lambda b: "google_translate_element" in b,
    "index_link": lambda b: "article-index-start-here" in b,
    "ai_disclosure": lambda b: "gs-ai-disclosure" in b,
    "inverted_media_query": lambda b: bool(
        re.search(r"not all and \(prefers-color-scheme", b)
    ),
    "disclaimer_in_script": lambda b: any(
        "AI Disclosure" in s
        for s in re.findall(r"<script\b[^>]*>([\s\S]*?)</script>", b, re.I)
    ),
}


def markers(body):
    return {k: fn(body) for k, fn in MARKERS.items()}


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"posts": {}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", default="", help="why this snapshot was taken")
    ap.add_argument("--no-commit", action="store_true")
    args = ap.parse_args()

    POSTS.mkdir(exist_ok=True)
    META.mkdir(exist_ok=True)

    prev = load_manifest()["posts"]
    entries = all_entries()
    if not entries:
        sys.exit("feed returned no posts — refusing to snapshot (would look like a wipe)")

    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    cur, added, changed = {}, [], []

    for e in entries:
        rec, body = parse(e)
        rec["markers"] = markers(body)
        slug = rec["slug"]
        (POSTS / f"{slug}.html").write_text(body, encoding="utf-8")
        (META / f"{slug}.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        old = prev.get(slug)
        if old is None:
            added.append(rec)
        elif old.get("sha256") != rec["sha256"]:
            delta = {
                k: [old["markers"].get(k), rec["markers"][k]]
                for k in rec["markers"]
                if old.get("markers", {}).get(k) != rec["markers"][k]
            }
            changed.append((rec, old, delta))
        cur[slug] = rec

    removed = [prev[s] for s in prev if s not in cur]
    for r in removed:
        # keep the file: the archive is the point. Only the manifest drops it.
        pass

    MANIFEST.write_text(
        json.dumps(
            {"snapshot": now, "count": len(cur), "posts": dict(sorted(cur.items()))},
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    lines = [f"\n## {now} — {len(cur)} posts live"]
    if args.note:
        lines.append(f"\n{args.note}\n")
    if added:
        lines.append("\n**Added**\n")
        lines += [f"- `{r['slug']}` — {r['title']} ({r['bytes']:,} bytes)" for r in added]
    if changed:
        lines.append("\n**Changed**\n")
        for rec, old, delta in changed:
            d = rec["bytes"] - old["bytes"]
            bit = f"- `{rec['slug']}` — {old['bytes']:,} → {rec['bytes']:,} bytes ({d:+,})"
            if delta:
                bit += "; markers " + ", ".join(
                    f"{k} {a}→{b}" for k, (a, b) in sorted(delta.items())
                )
            lines.append(bit)
    if removed:
        lines.append("\n**No longer published** (drafted or deleted; file kept in `posts/`)\n")
        lines += [f"- `{r['slug']}` — {r['title']}" for r in removed]
    if not (added or changed or removed):
        lines.append("\nNo changes.")
    lines.append("")

    head = "# Change log\n\nOne entry per snapshot. Newest at the bottom.\n"
    prior = CHANGELOG.read_text() if CHANGELOG.exists() else head
    CHANGELOG.write_text(prior + "\n".join(lines), encoding="utf-8")

    print(f"{len(cur)} posts | +{len(added)} added | ~{len(changed)} changed | -{len(removed)} unpublished")
    for r in added:
        print("  + ", r["slug"])
    for rec, old, _ in changed:
        print("  ~ ", rec["slug"], f"{old['bytes']:,}→{rec['bytes']:,}")
    for r in removed:
        print("  - ", r["slug"])

    if args.no_commit:
        return
    msg = f"snapshot {now}: +{len(added)} ~{len(changed)} -{len(removed)}"
    if args.note:
        msg += f"\n\n{args.note}"
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    r = subprocess.run(
        ["git", "commit", "-m", msg], cwd=ROOT, capture_output=True, text=True
    )
    print(r.stdout.strip() or r.stderr.strip())


if __name__ == "__main__":
    main()
