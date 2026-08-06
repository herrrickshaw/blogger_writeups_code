#!/usr/bin/env python3
"""Deterministic audit of every archived post: adoption, charts, readability.

No model involved — these are all measurable, and measuring beats asking.

  adoption   did the normalisation take, and do the house-style elements exist
  charts     does every inline script parse (a SyntaxError = a blank chart)
  readability words/sentence, long-sentence share, table and number density

    python3 tools/audit_blog.py            # summary + worst offenders
    python3 tools/audit_blog.py --csv out/audit.csv
"""
import argparse
import html as htmlmod
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
MANIFEST = ROOT / "meta" / "manifest.json"

DROP = re.compile(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", re.I)
TAG = re.compile(r"<[^>]+>")
SCRIPTS = re.compile(r"<script\b[^>]*>([\s\S]*?)</script>", re.I)


def visible(h):
    return re.sub(r"\s+", " ", htmlmod.unescape(TAG.sub(" ", DROP.sub(" ", h)))).strip()


def readability(text):
    """Plain, defensible metrics. Deliberately not a single opaque score."""
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 1]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    if not sents or not words:
        return None
    wps = [len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s)) for s in sents]
    long_sents = sum(1 for n in wps if n > 34)
    # syllable proxy: vowel groups. Crude but consistent across posts.
    syll = sum(max(1, len(re.findall(r"[aeiouy]+", w.lower()))) for w in words)
    flesch = 206.835 - 1.015 * (len(words) / len(sents)) - 84.6 * (syll / len(words))
    return {
        "words": len(words),
        "sentences": len(sents),
        "words_per_sentence": round(len(words) / len(sents), 1),
        "long_sentence_pct": round(100 * long_sents / len(sents), 1),
        "flesch": round(flesch, 1),
    }


def node_check(scripts):
    """Parse each inline script in Node. Blogger's CSP makes in-page checks lie."""
    if not shutil.which("node") or not scripts:
        return None
    broken = 0
    for s in scripts:
        if not s.strip():
            continue
        r = subprocess.run(["node", "--check", "-"], input=s,
                           capture_output=True, text=True)
        broken += (r.returncode != 0)
    return broken


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    args = ap.parse_args()

    man = json.loads(MANIFEST.read_text())["posts"]
    rows = []
    for rec in sorted(man.values(), key=lambda r: r["slug"]):
        f = POSTS / f"{rec['slug']}.html"
        if not f.exists():
            continue
        src = f.read_text(encoding="utf-8", errors="replace")
        scripts = SCRIPTS.findall(src)
        text = visible(src)
        rd = readability(text) or {}
        rows.append({
            "slug": rec["slug"],
            "version": rec.get("version", "?"),
            # adoption of the normalisation
            "layers": sum(bool(re.search(p, src)) for p in
                          ("BW-OVERRIDE", "gs-light-lock", "gs-dark-panel-guard",
                           r"not all and \(prefers-color-scheme")),
            # house-style elements
            "translate": int("google_translate_element" in src),
            "index_link": int("article-index-start-here" in src),
            "disclosure": int("gs-ai-disclosure" in src),
            "revision_line": int("gs-revision-v1" in src),
            # charts
            "scripts": len([s for s in scripts if s.strip()]),
            "broken_js": node_check(scripts),
            "tables": len(re.findall(r"<table", src, re.I)),
            "units_in_cells": len(re.findall(r"<td[^>]*>[^<]*(?:₹|%|crore|lakh|MMT|GWh)", src, re.I)),
            **rd,
        })

    n = len(rows)
    def pct(k, want=1):
        return round(100 * sum(1 for r in rows if r.get(k) == want) / n)

    print(f"=== {n} posts ===\n")
    print("ADOPTION (normalisation + house style)")
    print(f"  zero conflicting CSS layers   {sum(1 for r in rows if r['layers']==0):>3}/{n}  ({pct('layers',0)}%)")
    for k, label in (("translate", "translate widget"), ("index_link", "index backlink"),
                     ("disclosure", "AI disclosure"), ("revision_line", "revision line")):
        print(f"  {label:<28} {sum(r[k] for r in rows):>3}/{n}  ({pct(k)}%)")

    broken = [r for r in rows if r["broken_js"]]
    print(f"\nCHARTS / SCRIPTS")
    print(f"  posts with inline scripts     {sum(1 for r in rows if r['scripts']):>3}/{n}")
    print(f"  posts with a broken script    {len(broken):>3}/{n}"
          + ("  <-- blank charts" if broken else "  (none)"))
    for r in broken:
        print(f"      {r['slug']}  {r['broken_js']} of {r['scripts']}")

    rd = [r for r in rows if r.get("flesch") is not None]
    rd.sort(key=lambda r: r["flesch"])
    avg = lambda k: round(sum(r[k] for r in rd) / len(rd), 1)
    print(f"\nREADABILITY (mean over {len(rd)} posts)")
    print(f"  words per sentence            {avg('words_per_sentence')}")
    print(f"  long sentences (>34 words)    {avg('long_sentence_pct')}%")
    print(f"  Flesch reading ease           {avg('flesch')}   (30-50 = difficult, typical of policy prose)")
    print("\n  hardest to read:")
    for r in rd[:5]:
        print(f"    {r['flesch']:>6}  {r['words_per_sentence']:>5} w/sent  {r['slug']}")
    print("  easiest:")
    for r in rd[-3:]:
        print(f"    {r['flesch']:>6}  {r['words_per_sentence']:>5} w/sent  {r['slug']}")

    dirty = sorted((r for r in rows if r["tables"]), key=lambda r: -r["units_in_cells"])[:5]
    print("\n  units repeated in table cells (should be in the header):")
    for r in dirty:
        print(f"    {r['units_in_cells']:>4} cells  {r['slug']}")

    if args.csv:
        import csv
        p = pathlib.Path(args.csv); p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
        print(f"\nwrote {p}")


if __name__ == "__main__":
    sys.exit(main())
