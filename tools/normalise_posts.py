#!/usr/bin/env python3
"""Strip the conflicting colour layers this project added to post bodies.

Measured on the live page: disabling the BW-override, the light-lock and the
dark-panel guard takes the mineral-oil post from 795/1403 low-contrast nodes to
0/1403. Each post's original CSS was internally consistent — it declared dark
panels and white text together. The three added layers contradicted it and each
other. This removes them.

Also removes `@media not all and (prefers-color-scheme: dark)` blocks, which are
a genuine bug: the query reads as "when not dark" but applies in LIGHT mode.

Kept: the post's own design CSS, gs-typo-unify, structure, scripts, the
translate widget, the index link and the AI disclosure.

    python3 tools/normalise_posts.py                 # dry run, writes out/normalised/
    python3 tools/normalise_posts.py --slug <slug>   # one post

Nothing is uploaded. Apply with tools/blogger_api.py.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
OUT = ROOT / "out" / "normalised"
MANIFEST = ROOT / "meta" / "manifest.json"

# Marker -> human name. A <style> element containing any of these is removed
# whole; these blocks contain nothing but the layer they name.
LAYER_MARKERS = [
    ("BW-OVERRIDE", "BW-override"),
    ("gs-light-lock", "light-lock"),
    ("gs-dark-panel-guard", "dark-panel guard"),
]
INVERTED = "@media not all and (prefers-color-scheme"


def drop_style_blocks(src):
    """Remove whole <style> elements that exist only to carry an added layer."""
    removed = []

    def repl(m):
        inner = m.group(1)
        for marker, name in LAYER_MARKERS:
            if marker in inner:
                removed.append(name)
                return ""
        return m.group(0)

    out = re.sub(r"<style[^>]*>([\s\S]*?)</style>", repl, src)
    return out, removed


def drop_inverted(src):
    """Remove inverted media-query blocks, matching braces properly."""
    n = 0
    while True:
        i = src.find(INVERTED)
        if i < 0:
            break
        o = src.find("{", i)
        if o < 0:
            break
        depth, j = 0, o
        while j < len(src):
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        src = src[:i] + src[j:]
        n += 1
        if n > 12:
            break
    return src, n


def tidy(src):
    """Collapse the empty <style></style> and blank runs a removal leaves."""
    src = re.sub(r"<style[^>]*>\s*</style>", "", src)
    return re.sub(r"\n{3,}", "\n\n", src)


def normalise(src):
    out, layers = drop_style_blocks(src)
    out, n_inv = drop_inverted(out)
    out = tidy(out)
    if n_inv:
        layers.append(f"inverted-MQ x{n_inv}")
    return out, layers


def guard_ok(before, after):
    """Refuse a normalisation that damages anything other than the layers.

    Scripts, the disclosure, the translate widget and the index link must all
    survive intact, and the visible text must be byte-identical — this pass is
    CSS-only by definition.
    """
    def vis(h):
        h = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", " ", h, flags=re.I)
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

    checks = {
        "scripts kept": len(re.findall(r"<script\b", before, re.I))
                        == len(re.findall(r"<script\b", after, re.I)),
        "disclosure kept": ("gs-ai-disclosure" in before) == ("gs-ai-disclosure" in after),
        "translate kept": ("google_translate_element" in before)
                          == ("google_translate_element" in after),
        "index link kept": ("article-index-start-here" in before)
                           == ("article-index-start-here" in after),
        "visible text unchanged": vis(before) == vis(after),
        "smaller": len(after) <= len(before),
    }
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="only this post")
    args = ap.parse_args()

    man = json.loads(MANIFEST.read_text())["posts"]
    OUT.mkdir(parents=True, exist_ok=True)
    rows, skipped, refused = [], 0, []

    for rec in sorted(man.values(), key=lambda r: r["slug"]):
        if args.slug and rec["slug"] != args.slug:
            continue
        f = POSTS / f"{rec['slug']}.html"
        if not f.exists():
            continue
        before = f.read_text(encoding="utf-8")
        after, layers = normalise(before)
        if not layers:
            skipped += 1
            continue
        checks = guard_ok(before, after)
        if not all(checks.values()):
            refused.append((rec["slug"], [k for k, v in checks.items() if not v]))
            continue
        (OUT / f"{rec['slug']}.html").write_text(after, encoding="utf-8")
        rows.append((rec["slug"], layers, len(before), len(after)))

    print(f"{len(rows)} posts would change · {skipped} already clean · {len(refused)} refused\n")
    for slug, layers, b, a in rows:
        print(f"  {slug:<46} -{b-a:>6,}b   {', '.join(layers)}")
    if refused:
        print("\nREFUSED (guard tripped — inspect by hand):")
        for slug, why in refused:
            print(f"  {slug:<46} {', '.join(why)}")
    print(f"\nbodies written to {OUT}")
    print("apply with: python3 tools/blogger_api.py update --slug <slug> "
          f"--file {OUT}/<slug>.html")
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
