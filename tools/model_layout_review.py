#!/usr/bin/env python3
"""Ask models outside the Claude family how to structure a post for readability and ad breaks.

Sends each post's outline (headings, section lengths, paragraph lengths, tables, charts,
boxed notes) plus its opening text to Gemini, Mistral and Groq, and asks each, separately,
for structural edits only: where a section is too long, which paragraph should be split,
what belongs in a table or list, whether the post needs a summary up top, and which section
breaks are natural places for an ad. Never facts or numbers.

Report-only, like tools/multi_model_factcheck.py (whose key file and API helpers this reuses):
model output is a suggestion for a human (or a later edit pass) to check, not an edit.

    python3 tools/model_layout_review.py --slug <slug>
    python3 tools/model_layout_review.py --all --limit 20 --sleep 20      # free-tier pacing
    python3 tools/model_layout_review.py --all --panel gemini,mistral --sleep 20
    python3 tools/model_layout_review.py --theme                          # review the theme modules

Writes out/research/model-review/<slug>.json (each model's parsed answer, or its raw text
when it did not return JSON) and rebuilds out/research/model-review/SUMMARY.md, which lists
the suggestions at least two models agree on first.
"""
import argparse
import html
import json
import pathlib
import re
import sys
import time
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import multi_model_factcheck as mm  # noqa: E402

mm.PROMPT = "{text}"  # the helpers format PROMPT with the text; send our prompt as the text
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "research" / "model-review"
SKIP = {"article-index-start-here", "about-author"}

POST_PROMPT = """You are a copy editor for a data-journalism blog read mostly on phones. The blog runs
Google Auto ads, which AdSense places between blocks of the article. Review the STRUCTURE of
the post below. Do not judge or change facts, numbers, sources or the argument. Do not rewrite
prose. Suggest structural edits only.

Reply with JSON only, no prose before or after, in exactly this shape:
{{
  "structure_score": <1-5, 5 = easy to scan on a phone>,
  "summary_up_top": {{"present": true|false, "suggest": "<one sentence on what the opening should tell the reader, or empty>"}},
  "edits": [
    {{"where": "<heading text or 'opening' or 'para N'>",
      "type": "split-section|split-paragraph|add-heading|to-list|to-table|merge|move|shorten-heading|other",
      "why": "<one sentence>",
      "how": "<one concrete instruction>"}}
  ],
  "ad_breaks": {{"good": ["<heading text after whose section an ad fits naturally>"],
                 "avoid": ["<heading or block where an ad would interrupt a sequence, table, chart or argument>"]}}
}}
At most 8 edits, most important first. Use heading text exactly as given in the outline.

OUTLINE:
{outline}

OPENING TEXT (first 400 words):
{opening}
"""

THEME_PROMPT = """You are reviewing the CSS and ad-handling script of a Blogger theme for a data-journalism
blog (long posts, many tables and charts, Google Auto ads, mostly phone readers). An automated audit
of all 376 posts produced the findings below, followed by the theme modules that address them.
Suggest further changes for READABILITY and AD PLACEMENT only. Keep to what a theme can do: CSS
and a small script. Do not suggest hiding, blocking, reloading or resizing ads, or anything else
against AdSense policies.

Reply with JSON only:
{{"changes": [{{"area": "readability|ads|tables|mobile|other", "problem": "<one sentence>",
  "change": "<exact CSS or a precise description>", "risk": "<what could break>"}}],
  "keep": ["<module or rule that should stay as is, and why>"]}}
At most 10 changes, most important first.

AUDIT FINDINGS:
{audit}

THEME MODULES:
{modules}
"""


class Outline(HTMLParser):
    """Collect the block structure of a post: headings, paragraphs, lists, tables, charts, boxes."""
    BOX = re.compile(r"\b(warn|note|callout|card|stat|exhibit|box|panel|kpi|highlight)\b")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.stack, self.buf, self.skip = [], [], [], 0
        self.table = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "svg", "noscript"):
            self.skip += 1
            if tag == "svg":
                self.items.append(("chart", "svg"))
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "p", "li"):
            self.buf = []
            self.stack.append(tag)
        elif tag == "table":
            self.table = [0, 0]
        elif tag == "tr" and self.table is not None:
            self.table[0] += 1
            self.table[1] = 0
        elif tag in ("td", "th") and self.table is not None:
            self.table[1] += 1
        elif tag in ("canvas", "img"):
            self.items.append(("chart", tag))
        elif tag == "div" and self.BOX.search(a.get("class") or ""):
            self.items.append(("box", (a.get("class") or "").split()[0]))

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "noscript"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "table" and self.table is not None:
            self.items.append(("table", f"{self.table[1]} cols x {self.table[0]} rows"))
            self.table = None
        elif self.stack and tag == self.stack[-1]:
            self.stack.pop()
            text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if text and self.table is None:
                self.items.append((tag, text))
            self.buf = []

    def handle_data(self, data):
        if not self.skip and self.stack:
            self.buf.append(data)


def outline(path):
    p = Outline()
    p.feed(pathlib.Path(path).read_text(encoding="utf-8", errors="replace"))
    lines, words, para_n, section_words = [], 0, 0, 0
    sec_line = None
    for kind, val in p.items:
        if kind in ("h1", "h2", "h3", "h4"):
            if sec_line is not None:
                lines[sec_line] += f"  [{section_words} words in paragraphs and lists]"
            section_words = 0
            lines.append(f"{'  ' * (int(kind[1]) - 1)}{kind.upper()}: {val[:120]}")
            sec_line = len(lines) - 1
        elif kind == "p":
            n = len(val.split())
            words += n
            section_words += n
            para_n += 1
            if n >= 120:
                lines.append(f"    para {para_n}: {n} words (long) — {' '.join(val.split()[:12])}...")
        elif kind == "li":
            n = len(val.split())
            words += n
            section_words += n
        else:
            lines.append(f"    [{kind}: {val}]")
    if sec_line is not None:
        lines[sec_line] += f"  [{section_words} words in paragraphs and lists]"
    head = f"{words} words in {para_n} paragraphs; {sum(1 for k, _ in p.items if k == 'table')} tables; " \
           f"{sum(1 for k, _ in p.items if k == 'chart')} charts/images; {sum(1 for k, _ in p.items if k == 'box')} boxed notes"
    # collapse runs of identical lines (e.g. 40 stat boxes) so the outline stays short
    out, last, run = [], None, 0
    for ln in lines:
        if ln == last:
            run += 1
            continue
        if run:
            out.append(f"    (x{run + 1})")
        out.append(ln)
        last, run = ln, 0
    if run:
        out.append(f"    (x{run + 1})")
    return head + "\n" + "\n".join(out)[:9000]


def parse_json(text):
    """The first JSON object in a reply. Tolerates code fences, raw newlines inside strings
    (Mistral sends them) and trailing commas."""
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    body = re.sub(r",(\s*[}\]])", r"\1", m.group(0))
    try:
        return json.loads(body, strict=False)
    except json.JSONDecodeError:
        return None


def panel_keys(panel):
    """Models whose key is in the credentials file; a missing key skips that model with a warning."""
    blob = mm.creds()
    keys = {}
    want = {"gemini": ("Gemini", "GEMINI_API_KEY"), "mistral": ("Mistral", "MISTRAL_API_KEY"), "groq": ("Groq", "GROQ_API_KEY")}
    for p in panel:
        if p not in want:
            sys.exit(f"--panel: unknown model {p!r}; choose from gemini, mistral, groq")
        name, var = want[p]
        k = mm.key_optional(var, blob)
        if not k:
            print(f"! {var} not in {mm.CREDS}; skipping {name}", file=sys.stderr)
            continue
        if p == "gemini":
            keys[name] = (mm.ask_gemini, k, [mm.GEMINI_MODEL] + mm.GEMINI_FALLBACKS)
        elif p == "mistral":
            keys[name] = (mm.ask_mistral, k, [mm.MISTRAL_MODEL] + mm.MISTRAL_FALLBACKS)
        else:
            model = mm.groq_pick_model(k)
            keys[name] = (lambda kk, text, m=None, model=model: mm.ask_groq(kk, m or model, text), k, [model])
    if not keys:
        sys.exit("no model keys found; nothing to do")
    return keys


def ask_all(keys, prompt):
    """Each model's parsed JSON answer, {"raw": text} when it gave no JSON, {"error": text} on failure."""
    res = {}
    for name, (fn, k, models) in keys.items():
        try:
            model, raw = mm.ask_with_fallback(fn, k, prompt, models)
        except Exception as e:  # noqa: BLE001 - one model failing must not stop the run
            model, raw = models[0], f"[{name} network error: {e}]"
        if mm.failed(raw):
            res[name] = {"error": raw[:500], "model": model}
            print(f"  {name} ({model}): FAILED", " ".join(raw.split())[:120])
            continue
        res[name] = parse_json(raw) or {"raw": raw}
        res[name]["model"] = model
        print(f"  {name} ({model}): {'ok' if 'raw' not in res[name] else 'no JSON: ' + raw[:80]}")
    return res


def summary():
    rows = []
    for f in sorted(OUT.glob("*.json")):
        if f.name == "theme.json":
            continue
        d = json.loads(f.read_text())
        votes = {}
        for model, ans in d["models"].items():
            edits = ans.get("edits") if isinstance(ans, dict) else None
            for e in edits if isinstance(edits, list) else []:
                if not isinstance(e, dict):
                    continue
                k = (str(e.get("where", "")).strip().lower(), e.get("type", ""))
                votes.setdefault(k, []).append((model, e))
        scores = [a.get("structure_score") for a in d["models"].values() if isinstance(a, dict) and isinstance(a.get("structure_score"), (int, float))]
        agreed = [(k, v) for k, v in votes.items() if len({m for m, _ in v}) >= 2]
        rows.append((min(scores) if scores else 9, d["slug"], scores, agreed))
    lines = ["# Model layout review", "",
             "Structural suggestions from Gemini, Mistral and Groq (tools/model_layout_review.py). "
             "Lowest-scoring posts first; only suggestions two or more models made about the same place are listed. "
             "Model output is a suggestion, not a verified edit.", ""]
    for score, slug, scores, agreed in sorted(rows):
        lines.append(f"## {slug} — scores {scores}")
        for (where, typ), v in agreed:
            lines.append(f"- **{where or '?'}** ({typ}, {', '.join(sorted({m for m, _ in v}))}): {v[0][1].get('how', '')}")
        if not agreed:
            lines.append("- no suggestion shared by two models")
        lines.append("")
    (OUT / "SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT / 'SUMMARY.md'} ({len(rows)} posts)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--slug")
    g.add_argument("--all", action="store_true")
    g.add_argument("--theme", action="store_true", help="review theme/modules.json modules against the theme audit")
    g.add_argument("--summary", action="store_true", help="only rebuild SUMMARY.md")
    g.add_argument("--reparse", action="store_true", help="re-read saved replies that did not parse; no API calls")
    g.add_argument("--probe", action="store_true", help="send a one-line request to each model and report which answer")
    ap.add_argument("--panel", default="gemini,mistral,groq")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0)
    ap.add_argument("--force", action="store_true", help="re-run posts that already have a review")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if a.summary:
        return summary()
    if a.reparse:
        n = 0
        for f in OUT.glob("*.json"):
            d = json.loads(f.read_text())
            for name, ans in d["models"].items():
                parsed = parse_json(ans["raw"]) if isinstance(ans, dict) and "raw" in ans else None
                if parsed:
                    parsed["model"] = ans.get("model")
                    d["models"][name] = parsed
                    n += 1
            f.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"re-parsed {n} replies")
        return summary()
    keys = panel_keys([p.strip().lower() for p in a.panel.split(",") if p.strip()])
    if a.probe:
        res = ask_all(keys, 'Reply with this JSON only: {"ok": true}')
        sys.exit(0 if any(isinstance(v, dict) and v.get("ok") is True for v in res.values()) else 1)

    if a.theme:
        audit = (ROOT / "out" / "research" / "theme-audit-2026-10-26.md").read_text(encoding="utf-8")[:6000]
        mods = json.loads((ROOT / "theme" / "modules.json").read_text())
        text = "\n\n".join(f"--- {m['id']} ({m['kind']}) ---\n" +
                           (json.dumps(m.get("classes")) if m["kind"] == "scope" else (ROOT / m["file"]).read_text(encoding="utf-8"))
                           for m in mods if not m.get("retired"))
        res = ask_all(keys, THEME_PROMPT.format(audit=audit, modules=text[:14000]))
        (OUT / "theme.json").write_text(json.dumps({"models": res}, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {OUT / 'theme.json'}")
        return

    slugs = [a.slug] if a.slug else sorted(p.stem for p in (ROOT / "posts").glob("*.html") if p.stem not in SKIP)
    done = failed = 0
    for slug in slugs:
        dest = OUT / f"{slug}.json"
        if dest.exists() and not a.force and not a.slug:
            continue
        path = ROOT / "posts" / f"{slug}.html"
        if not path.exists():
            sys.exit(f"no such post: {path}")
        print(slug)
        ol = outline(path)
        opening = " ".join(html.unescape(mm.extract_text(path)).split()[:400])
        res = ask_all(keys, POST_PROMPT.format(outline=ol, opening=opening))
        if all("error" in v for v in res.values()):
            failed += 1
            print(f"  every model failed; {slug} not saved, so the next run retries it")
            if failed >= 3 and not done:
                sys.exit("the first posts all failed on every model: check keys and quotas with --probe")
            time.sleep(a.sleep)
            continue
        dest.write_text(json.dumps({"slug": slug, "outline": ol, "models": res}, indent=1, ensure_ascii=False), encoding="utf-8")
        done += 1
        if a.limit and done >= a.limit:
            break
        time.sleep(a.sleep)
    summary()


if __name__ == "__main__":
    main()
