#!/usr/bin/env python3
"""Roll the per-post reports in out/factcheck/ into one ranked worklist.

tools/multi_model_factcheck.py writes one report per post with each model's
FACTUAL ERRORS / INTERPRETATION ERRORS / OUTDATED DATA bullets. Reading 300+
of those is not a workflow, so this collects every bullet and ranks them:

  1. flags BOTH panel models raised on the same post (they share a number or
     a run of quoted words) -- the likeliest real problems;
  2. single-model flags marked [confidence: high];
  3. outdated-data flags, grouped by post -- the "needs a newer figure" list;
  4. posts with no clean answer yet (API errors), so the next run knows.

Report-only, same contract as the checker: model output is a prompt to check a
primary source, never a verdict, and nothing here edits a post.

    python3 tools/factcheck_summary.py                       # Gemini + Mistral
    python3 tools/factcheck_summary.py --models gemini,mistral,groq
    python3 tools/factcheck_summary.py --out out/factcheck/SUMMARY.md
"""
import argparse
import glob
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FC = ROOT / "out" / "factcheck"
CATS = {"FACTUAL ERRORS": "factual", "INTERPRETATION ERRORS": "interpretation",
        "OUTDATED DATA": "outdated"}
NUM = re.compile(r"\d[\d,]*\.?\d*")


def failed(text):
    return "API error" in text or "network error" in text or "[empty response]" in text


def parse_section(body):
    """{category: [(bullet text, confidence)]} for one model's answer."""
    out = {c: [] for c in CATS.values()}
    cur = None
    for line in body.splitlines():
        s = line.strip().strip("*").strip()
        head = s.rstrip(":").upper()
        if head in CATS:
            cur = CATS[head]
            continue
        if cur and re.match(r"^[-*•]\s+", line.strip()):
            item = re.sub(r"^[-*•]\s+", "", line.strip())
            if re.fullmatch(r"\(?none found\)?\.?", item, re.I):
                continue
            m = re.search(r"\[confidence:\s*(high|medium|low)\]", item, re.I)
            conf = m.group(1).lower() if m else "unstated"
            out[cur].append((item, conf))
    return out


def keys(item):
    """Tokens two models' flags must share to count as the same claim."""
    # Years and one- or two-digit numbers ("10", "2026") match unrelated claims;
    # keep only figures distinctive enough to identify one claim: decimals, or
    # three-plus digits that are not a calendar year.
    nums = set()
    for n in NUM.findall(item):
        n = n.rstrip(".,")
        digits = re.sub(r"\D", "", n)
        if re.fullmatch(r"(19|20)\d\d", n):
            continue
        if "." in n or len(digits) >= 3:
            nums.add(n.replace(",", ""))
    quote = re.search(r"[\"“'‘](.{12,}?)[\"”'’]", item)
    words = set()
    if quote:
        w = re.findall(r"[a-z]{4,}", quote.group(1).lower())
        words = {" ".join(w[i:i + 3]) for i in range(max(0, len(w) - 2))}
    return nums, words


def same_claim(a, b):
    na, wa = keys(a)
    nb, wb = keys(b)
    return bool(na & nb) or bool(wa & wb)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default="gemini,mistral")
    ap.add_argument("--out", default=str(FC / "SUMMARY.md"))
    args = ap.parse_args()
    models = [m.strip().lower() for m in args.models.split(",") if m.strip()]

    posts, pending, too_large = {}, [], []
    for f in sorted(glob.glob(str(FC / "*.md"))):
        slug = pathlib.Path(f).stem
        if slug.upper() == "SUMMARY":
            continue
        text = pathlib.Path(f).read_text(encoding="utf-8")
        if "SKIPPED: too large" in text:
            too_large.append(slug)
            continue
        got = {}
        for sec in re.split(r"^## ", text, flags=re.M)[1:]:
            name = sec.split(None, 1)[0].lower()
            if name in models and not failed(sec):
                got[name] = parse_section(sec)
        if len(got) < len(models):
            pending.append((slug, sorted(set(models) - set(got))))
        if got:
            posts[slug] = got

    agreed, high, outdated, rows = [], [], {}, []
    for slug, got in posts.items():
        counts = {c: 0 for c in CATS.values()}
        n_agree = n_high = 0
        names = list(got)
        for name, cats in got.items():
            for cat, items in cats.items():
                counts[cat] += len(items)
                for item, conf in items:
                    others = [(o, oi) for o in names if o != name
                              for oi, _ in got[o].get(cat, []) if same_claim(item, oi)]
                    if cat == "outdated":
                        outdated.setdefault(slug, []).append((name, item))
                    if others:
                        if name == names[0]:  # record each agreed pair once
                            agreed.append((slug, cat, name, item, others))
                            n_agree += 1
                    elif conf == "high":
                        high.append((slug, cat, name, item))
                        n_high += 1
        rows.append((n_agree, n_high, slug, counts))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))

    md = ["# Fact-check summary", "",
          "> **Model output, not verified fact.** Each line below is a prompt to check the",
          "> primary source before anything in a post changes. The models' training data",
          "> stops before many of these posts were written, so \"unverifiable\" is common",
          "> and is not itself a finding.", "",
          f"Panel: {', '.join(m.capitalize() for m in models)}. "
          f"Posts with at least one clean answer: {len(posts)}. "
          f"Posts missing a clean answer from some panel model: {len(pending)}. "
          f"Too large to send: {len(too_large)}.", "",
          "## Posts ranked by agreed and high-confidence flags", "",
          "| Post | Agreed | High (single model) | Factual | Interpretation | Outdated |",
          "|---|---|---|---|---|---|"]
    for n_agree, n_high, slug, c in rows:
        if n_agree or n_high or c["outdated"]:
            md.append(f"| {slug} | {n_agree} | {n_high} | {c['factual']} | "
                      f"{c['interpretation']} | {c['outdated']} |")
    md += ["", "## 1. Flagged by both models", ""]
    for slug, cat, name, item, others in agreed:
        md.append(f"- **{slug}** ({cat}) — {name.capitalize()}: {item}")
        for o, oi in others[:2]:
            md.append(f"  - {o.capitalize()}: {oi}")
    md += ["", "## 2. High-confidence, one model only", ""]
    md += [f"- **{s}** ({c}) — {n.capitalize()}: {i}" for s, c, n, i in high]
    md += ["", "## 3. Outdated data to re-check, by post", ""]
    for slug in sorted(outdated):
        md.append(f"- **{slug}**")
        md += [f"  - {n.capitalize()}: {i}" for n, i in outdated[slug]]
    md += ["", "## 4. Not yet checked cleanly", ""]
    md += [f"- {s} — no clean answer from {', '.join(m.capitalize() for m in miss)}"
           for s, miss in pending]
    if too_large:
        md += ["", "Too large to send in one request: " + ", ".join(too_large)]
    pathlib.Path(args.out).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(posts)} posts summarised, {len(agreed)} agreed flags, {len(high)} high-confidence "
          f"single-model flags, {sum(len(v) for v in outdated.values())} outdated-data flags, "
          f"{len(pending)} posts pending -> {args.out}")


if __name__ == "__main__":
    main()
