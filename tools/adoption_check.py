#!/usr/bin/env python3
"""Counterfactual adoption check on the blog's policy claims, via Gemini + search.

For each claim the blog makes about what India *should* do, ask a grounded model
two things:

  adoption      has it actually been adopted since the post was written?
  counterfactual if it has not, what visibly happened instead?

Output is CLEARLY MARKED as model output with its grounding sources. Nothing here
is a verified figure. The house rule stands: any number that reaches a post must
be re-checked against the primary source (PIB, PPAC, DGH, NITI, MoSPI) first.

    python3 tools/adoption_check.py            # all claims
    python3 tools/adoption_check.py --n 3      # first N, for a cheap trial
"""
import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "adoption_check.md"
MODEL = "gemini-2.5-flash"

# Each claim is a position the blog took, with the post it came from. Written by
# hand: an auto-extracted "recommendation" is usually a sentence fragment that a
# grounded search cannot act on.
CLAIMS = [
    ("rooftop-solar-is-working-household",
     "India's PM Surya Ghar rooftop solar subsidy is capped at 3 kW (Rs 78,000) and "
     "no central scheme subsidises a household battery, while grid-scale BESS gets "
     "VGF support.",
     "Has any central or state scheme since mid-2026 begun subsidising HOUSEHOLD "
     "battery storage in India, or extended the PM Surya Ghar cap beyond 3 kW?"),
    ("indias-oil-fields-are-running-down-3696",
     "India's crude output keeps missing target (28.7 MMT against 31.3 MMT) and "
     "petroleum-product self-sufficiency from indigenous crude has fallen to 11.8%.",
     "Has the Indian government revised its domestic crude production targets "
     "downward, or announced new IOR/EOR or acreage measures, since mid-2026?"),
    ("a-tax-play-grow-ethanol-sgst-revenue",
     "States earn SGST from ethanol blending and a tax-reform 'play' would grow "
     "that revenue.",
     "Have any Indian states changed GST/SGST treatment of ethanol or ethanol "
     "blending since mid-2026?"),
    ("the-cbg-incentive-stack-every-leg-of",
     "The compressed bio-gas (CBG) incentive stack is fragmented across schemes.",
     "Has India consolidated or materially changed CBG/SATAT incentives since "
     "mid-2026?"),
    ("nature-versus-nurture-indias-fertiliser",
     "India's NBS regime leaves urea structurally under-priced relative to DAP and "
     "distorts nutrient balance.",
     "Has India changed urea pricing, the NBS rates, or nutrient-based subsidy "
     "structure since mid-2026?"),
]

PROMPT = """You are auditing whether a policy position published on an Indian
economics blog has since been adopted.

THE BLOG'S POSITION: {claim}

QUESTION: {question}

Answer in exactly this structure, in under 180 words:

ADOPTED: yes / partially / no / unclear
EVIDENCE: what specifically happened, with dates and the issuing body. If nothing
happened, say so plainly — do not pad.
COUNTERFACTUAL: if it was not adopted, what observably happened instead, and what
the blog's position implies would have been different.
CONFIDENCE: high / medium / low, and say what would settle it.

Rules: cite only things you can ground in search results. If you cannot find
evidence, say "no evidence found" rather than reasoning from general knowledge.
Never invent a scheme name, a date or a figure."""


def key():
    env = pathlib.Path(os.path.expanduser("~/.config/market-secrets/credentials.env"))
    m = re.search(r"^GEMINI_API_KEY=(.*)$", env.read_text(), re.M)
    if not m:
        sys.exit("GEMINI_API_KEY not in ~/.config/market-secrets/credentials.env")
    return m.group(1).strip()


def ask(k, prompt, grounded=True):
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.2}}
    if grounded:
        body["tools"] = [{"google_search": {}}]
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={k}",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:200]
        if grounded and ("google_search" in detail or e.code == 400):
            return ask(k, prompt, grounded=False) + ("\n\n_(ungrounded — search tool unavailable)_",)[0:0] or ""
        return f"[API error {e.code}: {detail}]"
    cand = (d.get("candidates") or [{}])[0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    srcs = []
    gm = cand.get("groundingMetadata", {})
    for c in gm.get("groundingChunks", []) or []:
        w = c.get("web", {})
        if w.get("title"):
            srcs.append(w["title"])
    return text.strip(), sorted(set(srcs))[:6]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=0)
    args = ap.parse_args()
    k = key()
    claims = CLAIMS[: args.n] if args.n else CLAIMS

    md = ["# Policy adoption & counterfactual check",
          "",
          f"Model: `{MODEL}` with Google Search grounding. Run 2026-08-06.",
          "",
          "> **These are model outputs, not verified facts.** Grounded answers cite",
          "> search results, which are themselves secondary. Before any figure here",
          "> reaches a post it must be re-checked against the primary source",
          "> (PIB / PPAC / DGH / NITI / MoSPI). Same rule as vendor market estimates.",
          ""]
    for slug, claim, q in claims:
        print(f"… {slug}")
        res = ask(k, PROMPT.format(claim=claim, question=q))
        text, srcs = res if isinstance(res, tuple) else (res, [])
        md += [f"## {slug}", "", f"**Blog position:** {claim}", "",
               f"**Question:** {q}", "", text, ""]
        if srcs:
            md += ["**Grounding sources:** " + "; ".join(srcs), ""]
        else:
            md += ["**Grounding sources:** none returned — treat as ungrounded.", ""]
        md.append("---")
        md.append("")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
