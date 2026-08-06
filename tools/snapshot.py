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
import html
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
    "revision_line": lambda b: "gs-revision-v1" in b,
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


def marker_delta(old, rec):
    return {
        k: [old.get("markers", {}).get(k), rec["markers"][k]]
        for k in rec["markers"]
        if old.get("markers", {}).get(k) != rec["markers"][k]
    }


# ---------------------------------------------------------------- versioning
#
# Semver (semver.org) applied to prose. The "public API" of a post is what a
# reader could act on — its figures and its claims:
#
#   MAJOR  a figure or a conclusion changed. Someone who acted on the previous
#          version could now be wrong. This is the incompatible change.
#   MINOR  material new content, backward compatible — a new section, table or
#          chart. Nothing previously stated stopped being true.
#   PATCH  nothing the reader relies on moved: styling, markup, a design fix, a
#          typo, a reworded sentence.
#
# Existing posts start at 1.0.0, not 0.1.0: they are published and stable, and
# semver reserves 0.y.z for "anything MAY change at any time".
FIRST_VERSION = "1.0.0"

_DROP = re.compile(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", re.I)
# The revision line and the revision-history block are *about* the version, so
# they must not feed back into classifying it — their dates and version numbers
# would otherwise read as "figures changed" and force a spurious MAJOR bump.
_REVLINE = re.compile(r"<p\b[^>]*data-gs-revision-v1[^>]*>[\s\S]*?</p>", re.I)
_REVBLOCK = re.compile(r"<div\b[^>]*id=[\"']changelog[\"'][^>]*>[\s\S]*?</div>", re.I)
_TAG = re.compile(r"<[^>]+>")
_NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
_HEAD = re.compile(r"<h[1-4][^>]*>([\s\S]*?)</h[1-4]>", re.I)


def visible_text(html_str):
    s = _REVLINE.sub(" ", html_str)
    s = _REVBLOCK.sub(" ", s)
    s = _DROP.sub(" ", s)
    s = _TAG.sub(" ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def headings(html_str):
    html_str = _REVBLOCK.sub(" ", html_str)
    return [re.sub(r"\s+", " ", _TAG.sub("", h)).strip() for h in _HEAD.findall(html_str)]


def classify(old_body, new_body):
    """Return (level, reason). Heuristic — override with --as when it is wrong."""
    if old_body is None:
        return None, "no previous body on disk"
    ot, nt = visible_text(old_body), visible_text(new_body)
    if ot == nt:
        return "patch", "visible text identical; only markup/styling changed"

    on, nn = sorted(_NUM.findall(ot)), sorted(_NUM.findall(nt))
    if on != nn:
        added, removed = len(set(nn) - set(on)), len(set(on) - set(nn))
        return "major", f"figures changed (+{added}/-{removed} distinct numbers)"

    oh, nh = headings(old_body), headings(new_body)
    gone = [h for h in oh if h not in nh]
    if gone:
        return "major", f"section(s) removed: {', '.join(gone[:3])}"

    fresh = [h for h in nh if h not in oh]
    if fresh:
        return "minor", f"section(s) added: {', '.join(fresh[:3])}"
    if len(nt) > len(ot) * 1.02:
        return "minor", f"prose grew {len(ot):,}→{len(nt):,} chars with no new figures"
    return "patch", "wording changed; no figures, sections or claims moved"


def bump(version, level):
    major, minor, patch = (int(x) for x in version.split("."))
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"posts": {}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", default="", help="why this snapshot was taken")
    ap.add_argument("--no-commit", action="store_true")
    ap.add_argument("--push", action="store_true", help="push to origin after committing")
    ap.add_argument(
        "--as",
        dest="force_level",
        choices=["major", "minor", "patch"],
        help="override the auto-classified semver level for every change this run",
    )
    args = ap.parse_args()

    POSTS.mkdir(exist_ok=True)
    META.mkdir(exist_ok=True)

    prev = load_manifest()["posts"]
    entries = all_entries()
    if not entries:
        sys.exit("feed returned no posts — refusing to snapshot (would look like a wipe)")

    # Key by post id, never by slug. Slugs are derived from the URL and are not a
    # safe primary key: two feed entries reducing to the same slug would silently
    # overwrite each other and report a phantom size change.
    seen_ids = {}
    for e in entries:
        pid = e["id"]["$t"].rsplit(".post-", 1)[-1]
        if pid in seen_ids:
            print(f"warning: feed returned post {pid} twice — ignoring the duplicate")
            continue
        seen_ids[pid] = e
    entries = list(seen_ids.values())

    now = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    cur, added, changed, moved, bumped = {}, [], [], [], []
    slug_owner = {}

    for e in entries:
        rec, body = parse(e)
        rec["markers"] = markers(body)
        slug = rec["slug"]
        if slug in slug_owner:
            # Two live posts sharing a slug: disambiguate on disk by id so neither
            # file is lost, and say so loudly.
            print(f"warning: slug {slug!r} used by posts {slug_owner[slug]} and {rec['id']}")
            slug = f"{slug}--{rec['id']}"
            rec["slug"] = slug
        slug_owner[slug] = rec["id"]

        old = prev.get(rec["id"])
        # Read the previous body from its OLD path before anything is overwritten;
        # a moved post lives under a different filename.
        old_path = POSTS / f"{(old or {}).get('slug', slug)}.html"
        old_body = old_path.read_text(encoding="utf-8") if old and old_path.exists() else None

        (POSTS / f"{slug}.html").write_text(body, encoding="utf-8")
        (META / f"{slug}.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        if old is None:
            rec["version"] = FIRST_VERSION
            rec["version_history"] = [
                {"version": FIRST_VERSION, "date": now, "level": "initial",
                 "reason": "first snapshot", "note": args.note or ""}
            ]
            added.append(rec)
        else:
            rec["version"] = old.get("version", FIRST_VERSION)
            rec["version_history"] = list(old.get("version_history", []))
            if not rec["version_history"]:
                # Post predates versioning: record the baseline so history is
                # never empty and v1.0.0 has a date attached.
                rec["version_history"].append(
                    {"version": rec["version"], "date": now, "level": "baseline",
                     "reason": "version tracking introduced", "note": ""}
                )
            url_moved = old.get("url") != rec["url"]
            body_changed = old.get("sha256") != rec["sha256"]

            if url_moved:
                # Same post, new address. Blogger reserves slugs permanently, so
                # a moved post leaves a dead URL behind — always log it, even
                # when not one byte of the body changed.
                moved.append((rec, old))
            if body_changed:
                changed.append((rec, old, marker_delta(old, rec)))

            if body_changed or url_moved:
                level, reason = classify(old_body, body)
                if not body_changed:
                    level, reason = "patch", "moved to a new URL; body unchanged"
                if level is None:
                    level = "patch"
                    reason = "previous body missing from posts/ — defaulted to patch"
                if args.force_level:
                    level = args.force_level
                    reason = f"forced via --as {level} ({reason})"
                rec["version"] = bump(rec["version"], level)
                rec["version_history"].append(
                    {
                        "version": rec["version"],
                        "date": now,
                        "level": level,
                        "reason": reason,
                        "bytes": [old.get("bytes"), rec["bytes"]],
                        "url_changed": [old.get("url"), rec["url"]] if url_moved else None,
                        "markers_changed": marker_delta(old, rec) or None,
                        "note": args.note or "",
                    }
                )
                bumped.append((rec, old, level, reason))
        cur[rec["id"]] = rec

    removed = [prev[k] for k in prev if k not in cur]
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
        lines += [
            f"- `{r['slug']}` **v{r['version']}** — {r['title']} ({r['bytes']:,} bytes)"
            for r in added
        ]
    if bumped:
        lines.append("\n**Versions**\n")
        for rec, old, level, reason in bumped:
            lines.append(
                f"- `{rec['slug']}` **{old.get('version', FIRST_VERSION)} → "
                f"{rec['version']}** ({level.upper()}) — {reason}"
            )
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
    if moved:
        lines.append("\n**Moved** (old URL is now dead — Blogger never releases a slug)\n")
        for rec, old in moved:
            lines.append(f"- `{rec['title'][:60]}` — `{old['slug']}` → `{rec['slug']}`")
    if removed:
        lines.append("\n**No longer published** (drafted or deleted; file kept in `posts/`)\n")
        lines += [f"- `{r['slug']}` — {r['title']}" for r in removed]
    if not (added or changed or removed or moved or bumped):
        lines.append("\nNo changes.")
    lines.append("")

    head = "# Change log\n\nOne entry per snapshot. Newest at the bottom.\n"
    prior = CHANGELOG.read_text() if CHANGELOG.exists() else head
    CHANGELOG.write_text(prior + "\n".join(lines), encoding="utf-8")

    print(
        f"{len(cur)} posts | +{len(added)} added | ~{len(changed)} changed | "
        f"->{len(moved)} moved | -{len(removed)} unpublished"
    )
    for rec, old, level, reason in bumped:
        print(f"  v {rec['slug']}: {old.get('version', FIRST_VERSION)} -> "
              f"{rec['version']} ({level}) — {reason}")
    for rec, old in moved:
        print("  ->", old["slug"], "=>", rec["slug"])
    for r in added:
        print("  + ", r["slug"])
    for rec, old, _ in changed:
        print("  ~ ", rec["slug"], f"{old['bytes']:,}→{rec['bytes']:,}")
    for r in removed:
        print("  - ", r["slug"])

    if args.no_commit:
        return
    msg = (
        f"snapshot {now}: +{len(added)} ~{len(changed)} "
        f"->{len(moved)} -{len(removed)}"
        + (f" | v{len(bumped)} bumped" if bumped else "")
    )
    if args.note:
        msg += f"\n\n{args.note}"
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    r = subprocess.run(
        ["git", "commit", "-m", msg], cwd=ROOT, capture_output=True, text=True
    )
    print(r.stdout.strip() or r.stderr.strip())

    if args.push:
        p = subprocess.run(
            ["git", "push", "origin", "HEAD"], cwd=ROOT, capture_output=True, text=True
        )
        print(p.stderr.strip() or p.stdout.strip())


if __name__ == "__main__":
    main()
