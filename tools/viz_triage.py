#!/usr/bin/env python3
"""Give every live post a disposition for the visual-first rewrite (docs/VISUAL_STORY_STYLE.md).

    python3 tools/viz_triage.py            # writes out/viz/triage.json and prints the counts

  rewrite     standard frame, 500+ words, enough numbers to chart, nothing interactive  -> leaf agent builds an edition
  done        an edition already passes tools/viz_verify.py
  pending     an unpublished update or Phase 3 merge exists for this post; rewrite after it is published and snapshotted
  frame       a different template (tools/viz_frame.py cannot split it); needs a template fix or hand work
  interactive scripts, canvas or iframes that a rewrite would break; phone layout only (theme module gs-mobile-v1)
  walkthrough "How to use ..." command walkthroughs; code blocks are the content; phone layout only
  light       fewer than 30 distinct numbers; nothing to chart; phone layout only
Order within rewrite: the site's most-read list first, then worst phone score (tools/mobile_audit.js), then newest."""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from viz_frame import numbers, split, visible  # noqa: E402

SKIP = {"article-index-start-here", "about-author", "the-masala-deutsch-shop-books-things"}
BOILER = re.compile(r"googleTranslateElementInit|TranslateElement|google_translate_element|gs-a11y|speechSynthesis|accordion|gs-skip-link|adsbygoogle", re.I)


def interactive(html):
    for m in re.finditer(r"<script\b([^>]*)>(.*?)</script>", html, re.S | re.I):
        attrs, code = m.groups()
        if "src=" in attrs and re.search(r"translate\.google|accordion\.js|adsbygoogle|googlesyndication", attrs):
            continue
        if "src=" in attrs or (code.strip() and not BOILER.search(code)):
            return True
    return bool(re.search(r"<(canvas|iframe)\b", html, re.I))


def pending_posts():
    """Posts whose newest update file differs from the live text by more than 3% (an unpublished rewrite), plus the Phase 3
    merge targets: a visual edition built from the live text would conflict with them. Rewrite these after they are
    published and the next snapshot has run."""
    import glob
    latest = {}
    for f in sorted(glob.glob(str(ROOT / "out/update-*.html"))):
        m = re.match(r"update-(\d{4}-\d\d-\d\d)-(.+)\.html$", pathlib.Path(f).name)
        if m:
            latest[m.group(2)] = f
    hold = set(json.load(open(ROOT / "out/gsc_index/phase3_map.json")).values())
    shingles = lambda w: {" ".join(w[i:i + 5]) for i in range(max(1, len(w) - 4))}
    for s, f in latest.items():
        live = ROOT / f"posts/{s}.html"
        if not live.exists():
            continue
        a, b = visible(open(f, encoding="utf-8", errors="replace").read()).split(), visible(live.read_text(encoding="utf-8")).split()
        if a != b:
            A, B = shingles(a), shingles(b)
            if len(A & B) / max(1, len(A | B)) < 0.97:
                hold.add(s)
    return hold


HOLD = set()


def main():
    global HOLD
    HOLD = pending_posts()
    manifest = json.load(open(ROOT / "meta/manifest.json"))["posts"].values()
    retired = set(json.load(open(ROOT / "out/gsc_index/phase1_remove.json"))) | set(json.load(open(ROOT / "out/gsc_index/phase3_map.json")))
    most_read = re.findall(r"/([a-z0-9-]+)\.html", (pathlib.Path("/home/user/vertistrat-site/src/data/mostRead.ts").read_text() if pathlib.Path("/home/user/vertistrat-site/src/data/mostRead.ts").exists() else ""))
    audit = {}
    r = subprocess.run(["node", str(ROOT / "tools/mobile_audit.js"), "--json", "/tmp/viz_audit.json"], capture_output=True, text=True, cwd=ROOT)
    for x in json.load(open("/tmp/viz_audit.json")):
        audit[pathlib.Path(x["file"]).stem] = 3 * x["smallCharts"] + 2 * x["swipeTables"] + x["longParas"]
    rows = []
    for p in manifest:
        slug = p["slug"]
        if slug in retired or slug in SKIP:
            continue
        html = (ROOT / f"posts/{slug}.html").read_text(encoding="utf-8")
        fr = split(html)
        words = len(visible(fr.body if fr else html).split())
        nums = len([n for n in numbers(visible(fr.body if fr else html)) if not re.fullmatch(r"(19|20)\d\d", n)])
        if (ROOT / f"out/viz/{slug}/.verified").exists():
            d = "done"
        elif slug in HOLD:
            d = "pending"
        elif slug.startswith(("how-to-use", "how-to-")) or re.search(r"-open-source-tools?-|open-source-toolkits?", slug):
            d = "walkthrough"
        elif interactive(html):
            d = "interactive"
        elif not fr:
            d = "frame"
        elif nums < 30:
            d = "light"
        else:
            d = "rewrite"
        rows.append({"slug": slug, "disposition": d, "words": words, "numbers": nums, "phoneScore": audit.get(slug, 0),
                     "mostRead": slug in most_read, "published": p["published"][:10]})
    order = lambda x: (not x["mostRead"], -x["phoneScore"], x["published"] and -int(x["published"].replace("-", "")))
    rows.sort(key=lambda x: (x["disposition"] != "rewrite", order(x)))
    (ROOT / "out/viz").mkdir(parents=True, exist_ok=True)
    (ROOT / "out/viz/triage.json").write_text(json.dumps(rows, indent=1))
    from collections import Counter
    c = Counter(x["disposition"] for x in rows)
    print(f"{len(rows)} live posts: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    rw = [x for x in rows if x["disposition"] == "rewrite"]
    print(f"rewrite candidates: {len(rw)} posts, {sum(x['words'] for x in rw):,} words; median {sorted(x['words'] for x in rw)[len(rw) // 2]:,} words")


if __name__ == "__main__":
    main()
