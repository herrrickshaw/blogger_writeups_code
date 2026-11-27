#!/usr/bin/env python3
"""Keyword graph: which articles a reader should be sent to next.

    python3 tools/keyword_graph.py --report                 # what it found
    python3 tools/keyword_graph.py --json out/knowledge-graph.json
    python3 tools/keyword_graph.py --suggest <slug>         # links for one post (new drafts too: --file)

The older entity graph (tools/index_graph.py) matches ~40 hand-picked nouns, so a new
post about sodium-ion cells or earnings drift matched nothing and got unrelated
neighbours. This graph learns its vocabulary from the articles themselves:

  terms     single words and two-word phrases ("sodium-ion", "earnings drift",
            "high-sulphur grades"). Headings count x4, body text counts once, capped
            at 5 per post, so a table that repeats a phrase 2,000 times cannot
            dominate.
  keywords  each post's highest TF-IDF terms: the handful that make it different
            from the other 530.
  hubs      keywords shared by 3 to 40 posts. These are the "tags" a reader can
            follow from one article to the rest of that subject.
  related   cosine similarity of the TF-IDF vectors, nudged up for shared labels,
            countries, states and named entities. Each link carries the shared
            terms that justify it, so a wrong pairing can be seen and fixed.

A term used by more than 12% of posts is too common to link anything, and a term
used by one post links nothing, so both are dropped from the similarity.
"""
import argparse
import collections
import glob
import html
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Words that carry no subject. Includes this blog's own boilerplate and units.
STOP = set("""
a about above after again against all also am an and any are as at be because been before being below between both
but by can could did do does doing down during each few for from further had has have having he her here hers him his
how i if in into is it its itself just me more most my no nor not now of off on once only or other our out over own
same she should so some such than that the their them then there these they this those through to too under until
up very was we were what when where which while who whom why will with would you your
one two three four five six seven eight nine ten first second third new old per cent percent
india indian indias crore crores lakh lakhs billion million thousand tonnes tonne tons year years fiscal month months
week weeks day days state states data table figure chart source sources article articles post posts blog read note notes
click share tools disclosure disclaimer assistance researched written drawing publicly available government cited
several reached search engine summary rather directly index start updated revised version changed
may june july august september october november december january february march april
fy2022 fy2023 fy2024 fy2025 fy2026 fy2027 rs inr usd vs versus around roughly nearly almost about
said says say according however although though since still yet even much many may might must shall
likely less least well among within without across along per via using used use make made makes
stratsolution vertistrat solutions masaladeutsch
came together actually require caveat caveats keyword rose want archived filed edition counter course how-to
""".split())
KEEP_SHORT = {"ev", "evs", "ai", "gst", "lng", "cbg", "pli", "fdi", "msp", "fci", "wpi", "cpi", "pm", "dgft"}
SEG = re.compile(r"[^a-z0-9\-]+")
HEAD_RE = re.compile(r"<h[1-3][^>]*>(.*?)</h[1-3]>", re.S | re.I)
SF_RE = re.compile(r'class="(?:standfirst|extitle|h2sub|eyebrow)"[^>]*>(.*?)</p>', re.S)

MAX_DF = 0.12    # a term in more than this share of posts is too common to link on
HUB_MIN, HUB_MAX = 3, 40
TOP_KEYWORDS = 10
HUB_STOP = {"see way", "guide", "doubled", "bulletin", "scenario", "scenarios", "ranking", "reform", "digital",
            "pool", "policy analysis", "fuel model", "factory", "volatility", "organic", "mineral", "road", "tender",
            "bigger", "opportunity", "piece set", "dataset analysis", "statistical", "fleet", "pump"}
MIN_LINK = 0.07      # below this a pairing is noise; the two best are kept regardless


def _strip(x):
    return html.unescape(re.sub(r"<[^>]+>", " ", x))


def read_post(path):
    """(heading_text, body_text), both lowercase, scripts/styles/disclaimers removed."""
    s = Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r'class="disclaimer".*?</p>', " ", s, flags=re.S)
    heads = HEAD_RE.findall(s) + SF_RE.findall(s)
    return _strip(" ".join(heads)).lower(), _strip(s).lower()


SURFACE = collections.defaultdict(collections.Counter)   # folded term -> spellings seen


def _norm(w):
    w = w.strip("-")
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is", "as", "os")):
        return w[:-1]
    return w


def show(term):
    """Readable spelling of a folded term: the form the articles use most."""
    return " ".join((SURFACE[w].most_common(1)[0][0] if SURFACE.get(w) else w) for w in term.split(" "))


def _ok(w):
    if w in STOP or len(w) > 24 or w.isdigit() or re.fullmatch(r"[\d\-.]+", w):
        return False
    if re.fullmatch(r"fy\d+(-\d+)?|q[1-4]|h[12]", w):
        return False
    return len(w) >= 3 or w in KEEP_SHORT


def terms(text):
    """Counter of unigrams and adjacent-word phrases; a stop word breaks a phrase."""
    out = collections.Counter()
    for seg in re.split(r"[.;:()\[\]|\n\r\t,!?—–\"“”]+", text):
        prev = None
        for raw in SEG.split(seg):
            if not raw:
                continue
            w = _norm(raw)
            if not _ok(w):
                prev = None
                continue
            SURFACE[w][raw.strip("-")] += 1
            out[w] += 1
            if prev:
                out[f"{prev} {w}"] += 1
            prev = w
    return out


def weigh(head, body):
    h, b = terms(head), terms(body)
    return {t: h.get(t, 0) * 4 + min(b.get(t, 0), 5) for t in set(h) | set(b)}


def compute(docs, top_related=5):
    """docs: slug -> {head, body, labels?, countries?, states?, entities?, title?}.
    Returns {"posts": {slug: {keywords, related}}, "hubs": {keyword: [slugs]}}."""
    n = len(docs)
    hb = {s: (terms(d["head"]), terms(d["body"])) for s, d in docs.items()}
    w = {s: {t: h.get(t, 0) * 4 + min(b.get(t, 0), 5) for t in set(h) | set(b)} for s, (h, b) in hb.items()}
    df = collections.Counter(t for v in w.values() for t in v)
    cap = max(int(MAX_DF * n), 6)
    use = {t for t, c in df.items() if 2 <= c <= cap}
    idf = {t: math.log(n / df[t]) for t in use}
    vec, norm = {}, {}
    for s, v in w.items():
        # phrases count a little more than their parts: they are more specific
        x = {t: c * idf[t] * (1.25 if " " in t else 1.0) for t, c in v.items() if t in use}
        nm = math.sqrt(sum(a * a for a in x.values())) or 1.0
        vec[s], norm[s] = x, nm

    def keywords(s):
        ranked = sorted(vec[s].items(), key=lambda kv: (-kv[1], kv[0]))
        out, words = [], set()
        for t, _ in ranked:
            parts = set(t.split())
            # a single word already inside a chosen phrase adds nothing
            if " " not in t and any(t in set(k.split()) for k in out if " " in k):
                continue
            if " " in t and all(p in words for p in parts):
                continue
            out.append(t)
            words |= parts
            if len(out) >= TOP_KEYWORDS:
                break
        return out

    kws = {s: keywords(s) for s in docs}
    # A hub is a subject, not a stray phrase: the term must sit in the headings of at
    # least two posts (body-only phrases such as "caveat size" are template wording).
    in_head = collections.defaultdict(set)
    for s, (h, _) in hb.items():
        for t in h:
            if t in use and (" " in t or len(t) >= 4 or t in KEEP_SHORT):
                in_head[t].add(s)
    hubs = {}
    for t, hs in in_head.items():
        kw_posts = {s for s, ks in kws.items() if t in ks}
        # in headings of 2+ posts AND either a defining keyword of 2+ posts or developed in the
        # body (median 3+ mentions): this drops title filler ("bigger", "guide") that heads many
        # posts but defines none
        bodies = sorted(hb[s][1].get(t, 0) for s in hs)
        deep = len(hs) >= 3 and bodies[len(bodies) // 2] >= 3     # headline word the text really develops
        if t in HUB_STOP or len(hs) < 2 or (len(kw_posts) < 2 and not deep):
            continue
        members = hs | kw_posts
        if HUB_MIN <= len(members) <= HUB_MAX:
            hubs[t] = sorted(members)
    # a word whose membership equals a phrase containing it is the same hub: keep the phrase
    for t in [t for t in hubs if " " not in t]:
        if any(" " in u and t in u.split() and set(hubs[u]) >= set(hubs[t]) for u in hubs):
            del hubs[t]

    inv = collections.defaultdict(list)
    for s, x in vec.items():
        for t in x:
            inv[t].append(s)

    res = {}
    for s in docs:
        acc = collections.defaultdict(float)
        share = collections.defaultdict(list)
        for t, a in vec[s].items():
            for o in inv[t]:
                if o == s:
                    continue
                c = a * vec[o][t]
                acc[o] += c
                share[o].append((c, t))
        d = docs[s]
        cand = []
        for o, dot in acc.items():
            sc = dot / (norm[s] * norm[o])
            e = docs[o]
            lab = set(d.get("labels") or []) & set(e.get("labels") or [])
            geo = (set(d.get("countries") or []) | set(d.get("states") or [])) & \
                  (set(e.get("countries") or []) | set(e.get("states") or []))
            ent = set(d.get("entities") or []) & set(e.get("entities") or [])
            sc += 0.03 * min(len(lab), 2) + 0.02 * min(len(geo), 2) + 0.03 * min(len(ent), 3)
            cand.append((sc, o))
        cand.sort(key=lambda x: (-x[0], x[1]))
        rel = []
        keep = [c for c in cand[:top_related] if c[0] >= MIN_LINK]
        keep += [c for c in cand[len(keep):3] if c[0] >= 0.04]       # weaker, but never leave a post with one link
        keep = keep or cand[:2]
        for sc, o in keep:
            # phrases first, then words not already inside a listed phrase
            sh, seen = [], set()
            for _, t in sorted(share[o], key=lambda x: (" " not in x[1], -x[0], x[1])):
                if " " not in t and t in seen:
                    continue
                sh.append(t)
                seen |= set(t.split())
                if len(sh) >= 4:
                    break
            rel.append({"slug": o, "score": round(sc, 4), "shared": [show(t) for t in sh]})
        res[s] = {"keywords": [show(k) for k in kws[s]], "related": rel}
    return {"posts": res, "hubs": {show(k): v for k, v in hubs.items()}}


def load_docs(root=ROOT, extra=None):
    manifest = json.loads((root / "meta" / "manifest.json").read_text())["posts"]
    by_slug = {r["slug"]: r for r in manifest.values()}
    docs = {}
    for f in sorted(glob.glob(str(root / "posts" / "*.html"))):
        slug = Path(f).stem
        rec = by_slug.get(slug)
        if not rec:
            continue
        head, body = read_post(f)
        docs[slug] = {"head": head, "body": body, "title": rec["title"], "url": rec["url"],
                      "labels": [l for l in (rec.get("labels") or []) if l]}
    for slug, d in (extra or {}).items():
        docs[slug] = d
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--suggest", metavar="SLUG")
    ap.add_argument("--file", help="a draft HTML file to suggest links for (with --suggest NAME)")
    args = ap.parse_args()
    extra = None
    if args.file:
        h, b = read_post(args.file)
        extra = {args.suggest or "draft": {"head": h, "body": b, "title": args.suggest or "draft", "labels": []}}
    docs = load_docs(extra=extra)
    g = compute(docs)
    if args.json:
        Path(args.json).write_text(json.dumps({
            "posts": {s: {"title": docs[s].get("title"), "url": docs[s].get("url"), **v}
                      for s, v in g["posts"].items()},
            "hubs": g["hubs"]}, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {args.json} ({len(g['posts'])} posts, {len(g['hubs'])} keyword hubs)")
    if args.suggest:
        r = g["posts"].get(args.suggest)
        if not r:
            sys.exit(f"no post {args.suggest!r}")
        print("keywords:", ", ".join(r["keywords"]))
        for x in r["related"]:
            print(f"  {x['score']:.3f}  {docs[x['slug']]['title'][:80]}\n         via {', '.join(x['shared'])}  ({x['slug']})")
    if args.report:
        inbound = collections.Counter(x["slug"] for v in g["posts"].values() for x in v["related"])
        orphans = [s for s in g["posts"] if inbound[s] == 0]
        print(f"posts {len(docs)}; keyword hubs {len(g['hubs'])}; posts nobody links to {len(orphans)}")
        print("\nlargest hubs:")
        for k, v in sorted(g["hubs"].items(), key=lambda kv: -len(kv[1]))[:30]:
            print(f"  {len(v):3}  {k}")
        thin = [s for s, v in g["posts"].items() if len(v["related"]) < 3]
        print(f"\nposts with fewer than 3 related: {len(thin)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
