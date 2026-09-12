#!/usr/bin/env python3
"""Data-validation tests for masaladeutsch posts. Report-only: never edits a
post (CLAUDE.md rule 3 -- model output is not verified fact).

Three tests per post, written to out/validation/<slug>.md:

  1. house-rules   the ten STATIC_RULES from consistency-check/checks.py, run
                   on the local file (no network), including a real JS syntax
                   check of every inline <script> via `node --check`.
  2. consistency   an LLM compares every number in the prose against the same
                   number in tables, chart labels and captions, and checks that
                   stated totals/percentages add up.
  3. claims        an LLM extracts each quantitative or dated claim with the
                   source the post attributes it to, tiers the source, and flags
                   claims it cannot reconcile or that look stale for the post
                   date. It cannot browse: "cannot verify offline" is a to-do
                   list for a human, not a verdict.

Tests 2-3 talk to any OpenAI-compatible chat endpoint. Defaults target an
OmniRoute gateway (http://localhost:20128/v1); Gemini's OpenAI-compatible
endpoint works the same way:

  # on a machine running OmniRoute
  LLM_API_KEY=sk-... python3 tools/content_validate.py --recent
  # straight to Gemini
  LLM_API_KEY=$GEMINI_API_KEY python3 tools/content_validate.py --recent \
      --base-url https://generativelanguage.googleapis.com/v1beta/openai \
      --model gemini-2.5-flash

  python3 tools/content_validate.py --slug <slug> [--slug ...]
  python3 tools/content_validate.py --file posts/x.html --skip-llm

Exit code is 1 if any BLOCKER house rule fails, so it can gate a publish.
"""
import argparse
import datetime as dt
import html as htmlmod
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import uuid
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "consistency-check"))
from checks import STATIC_RULES, BLOCKER  # noqa: E402

OUT_DIR = ROOT / "out" / "validation"
RECENT = [
    "the-50-tariff-and-234-one-untangling",
    "indias-battery-storage-boom-is",
    "a-million-wine-market-behind-150-wall",
    "the-solar-panel-recycling-opportunity",
]
PROSE_CAP = 14000
SCRIPT_RE = re.compile(r"<script\b([^>]*)>([\s\S]*?)</script>", re.I)
BLOCK_STRIP_RE = re.compile(r"<(script|style|svg)\b[^>]*>[\s\S]*?</\1>", re.I)
TAG_RE = re.compile(r"<[^>]+>")


# ----------------------------------------------------------------- extraction

def clean(s):
    s = TAG_RE.sub(" ", s)
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def extract(body):
    prose = clean(BLOCK_STRIP_RE.sub(" ", body))
    tables = []
    for t in re.findall(r"<table\b[^>]*>([\s\S]*?)</table>", body, re.I):
        rows = []
        for tr in re.findall(r"<tr\b[^>]*>([\s\S]*?)</tr>", t, re.I):
            cells = [clean(c) for c in re.findall(r"<t[hd]\b[^>]*>([\s\S]*?)</t[hd]>", tr, re.I)]
            if cells:
                rows.append(" | ".join(cells))
        if rows:
            tables.append("\n".join(rows))
    charts = []
    for svg in re.findall(r"<svg\b[^>]*>([\s\S]*?)</svg>", body, re.I):
        labels = [clean(x) for x in re.findall(r"<text\b[^>]*>([\s\S]*?)</text>", svg, re.I)]
        labels = [x for x in labels if x]
        if labels:
            charts.append(" | ".join(labels))
    captions = [clean(c) for c in re.findall(r"<figcaption\b[^>]*>([\s\S]*?)</figcaption>", body, re.I)]
    title = clean(next(iter(re.findall(r"<h1\b[^>]*>([\s\S]*?)</h1>", body, re.I)), ""))
    m = re.search(r"\b(\d{1,2} [A-Z][a-z]+ 20\d\d)\b", prose)
    return {"title": title, "date": m.group(1) if m else "unknown", "prose": prose,
            "tables": tables, "charts": charts, "captions": captions}


# ---------------------------------------------------------------- house rules

def node_check(body):
    """1-based indices of inline scripts that fail `node --check`; None if no node."""
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except Exception:
        return None
    bad = []
    for i, (attrs, code) in enumerate(SCRIPT_RE.findall(body), 1):
        if re.search(r"\bsrc\s*=", attrs) or not code.strip():
            continue
        if re.search(r'type\s*=\s*["\'](?!text/javascript|module|application/javascript)', attrs, re.I):
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(code)
            path = f.name
        try:
            r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
            if r.returncode != 0:
                bad.append(i)
        finally:
            os.unlink(path)
    return bad


def run_house_rules(body):
    nc = node_check(body)
    rows = []
    for name, sev, fn in STATIC_RULES:
        try:
            ok, detail = fn(body, node_check=nc)
        except Exception as e:  # a rule crashing is itself a finding
            ok, detail = False, f"rule error: {e}"
        rows.append((name, sev, ok, detail))
    return rows


# ------------------------------------------------------------------- LLM side

class LLM:
    def __init__(self, base_url, api_key, model, timeout):
        self.base = base_url.rstrip("/")
        self.key = api_key
        self.model = model
        self.timeout = timeout

    def _req(self, path, data=None):
        req = urllib.request.Request(self.base + path, method="POST" if data else "GET")
        req.add_header("Content-Type", "application/json")
        if self.key:
            req.add_header("Authorization", f"Bearer {self.key}")
        payload = json.dumps(data).encode() if data else None
        delay = 2.0
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, payload, timeout=self.timeout) as r:
                    return json.loads(r.read().decode())
            except urllib.error.HTTPError as e:
                detail = e.read().decode()[:300]
                if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                    time.sleep(delay)
                    delay *= 2
                    continue
                raise RuntimeError(f"HTTP {e.code}: {detail}")
            except urllib.error.URLError as e:
                raise RuntimeError(f"network: {e.reason}")

    def pick_model(self):
        if self.model:
            return self.model
        models = self._req("/models")
        ids = [m.get("id") for m in models.get("data", []) if m.get("id")]
        if not ids:
            raise RuntimeError("endpoint listed no models; pass --model")
        self.model = ids[0]
        return self.model

    def _one_call(self, system, user, max_tokens):
        # A gateway's prompt/semantic cache will happily replay a stale, truncated
        # completion for an identical (temperature=0) prompt across runs -- bit us
        # once already after fixing the thinking-budget setting. A per-call nonce
        # keeps every request byte-distinct so retries and re-runs can't hit it.
        nonced_user = f"{user}\n\n<!-- cache-bust: {uuid.uuid4()} -->"
        res = self._req("/chat/completions", {
            "model": self.model, "temperature": 0, "max_tokens": max_tokens,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": nonced_user}],
        })
        choice = res["choices"][0]
        return choice["message"].get("content") or "", choice.get("finish_reason")

    def json_chat(self, system, user, max_tokens=4000):
        """Reasoning-model gotcha: on this endpoint, thinking tokens are billed
        against the same max_tokens budget and normally land in a separate
        `reasoning_content` field -- but on a long/complex prompt the model can
        exhaust that budget mid-thought, and a fragment of the in-progress
        reasoning spills into the visible `content` field instead of the final
        JSON. The fix is more budget, not a different prompt, so escalate
        max_tokens (not just the instruction wording) whenever a response looks
        truncated (finish_reason == 'length', or no JSON object was found)."""
        strict = ("\n\nOutput format is mandatory: respond with ONLY a single JSON object, "
                  "starting with { and ending with }. No prose before or after it, no markdown "
                  "code fences, no explanation. If a section would be empty, use an empty array.")
        last_err = None
        budget = max_tokens
        for attempt in range(3):
            sys_prompt = system if attempt == 0 else system + strict
            text, finish_reason = self._one_call(sys_prompt, user, budget)
            text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.S)
            start, end = text.find("{"), text.rfind("}")
            truncated = finish_reason == "length"
            if start < 0 or end < 0:
                last_err = RuntimeError(
                    f"model returned no JSON object (finish_reason={finish_reason}, "
                    f"budget={budget}): {text[:200]!r}")
                budget = int(budget * 2)
                continue
            candidate = text[start:end + 1]
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                try:
                    return json.loads(_escape_newlines_in_strings(candidate))
                except json.JSONDecodeError as e:
                    last_err = RuntimeError(
                        f"unparseable JSON after repair (finish_reason={finish_reason}, "
                        f"{e}): {candidate[:200]!r}")
                    if truncated:
                        budget = int(budget * 2)
                        continue
        raise last_err


def _escape_newlines_in_strings(s):
    """Some models emit literal newlines inside JSON string values, which
    json.loads rejects. Walk the text tracking string/escape state and turn
    raw \\n / \\r into their escaped form only while inside a string literal
    -- whitespace between tokens is left alone."""
    out = []
    in_string = False
    escaped = False
    for ch in s:
        if in_string:
            if escaped:
                out.append(ch)
                escaped = False
            elif ch == "\\":
                out.append(ch)
                escaped = True
            elif ch == '"':
                out.append(ch)
                in_string = False
            elif ch == "\n":
                out.append("\\n")
            elif ch == "\r":
                out.append("\\r")
            else:
                out.append(ch)
        else:
            out.append(ch)
            if ch == '"':
                in_string = True
    return "".join(out)


SYSTEM = ("You are a meticulous data-validation reviewer for a data journalism blog "
          "about the Indian economy. You only report what the supplied text supports. "
          "You cannot browse. Respond with a single JSON object and nothing else.")


def evidence(ex, prose_cap=None):
    cap = PROSE_CAP if prose_cap is None else prose_cap
    parts = [f"POST TITLE: {ex['title']}", f"POST DATE (as printed): {ex['date']}",
             "PROSE:", ex["prose"][:cap]]
    if len(ex["prose"]) > cap:
        parts.append(f"[prose truncated at {cap} chars]")
    for i, t in enumerate(ex["tables"], 1):
        parts += [f"TABLE {i}:", t]
    for i, c in enumerate(ex["charts"], 1):
        parts += [f"CHART {i} TEXT LABELS:", c]
    for i, c in enumerate(ex["captions"], 1):
        parts += [f"CAPTION {i}:", c]
    return "\n".join(parts)


def test_consistency(llm, ex, prose_cap=None):
    user = evidence(ex, prose_cap) + """

TASK: Internal consistency audit. Find every place where the same quantity is
stated with different values in different parts of the post (prose vs table vs
chart labels vs captions), and every arithmetic claim that does not hold
(components that do not sum to the stated total, a percentage that does not
match the two numbers it is computed from, a "x-fold" or "x times" claim that
the underlying numbers do not support, a date range whose length is misstated).
Ignore differences that are only rounding (e.g. 12.5% vs ~13%) or unit
restatements that are equivalent. Return:
{"mismatches":[{"quantity":"...","location_a":"...","value_a":"...",
  "location_b":"...","value_b":"...","severity":"high|medium|low","note":"..."}],
 "arithmetic":[{"claim":"...","computed":"...","severity":"high|medium|low","note":"..."}],
 "summary":"one or two sentences"}"""
    return llm.json_chat(SYSTEM, user, max_tokens=8000)


def test_claims(llm, ex, prose_cap=None):
    user = evidence(ex, prose_cap) + """

TASK: Claims ledger. Extract up to 40 of the most load-bearing quantitative or
dated factual claims (figures, percentages, dates, rankings, legal/regulatory
statuses). For each give the source the post itself attributes it to, tier that
source, and assess it against the text only:
  source_tier: primary (government/court/company filing/official release named),
               secondary (press/analyst/industry body named), analyst-estimate,
               or unsourced.
  status: consistent (claim matches how the post describes its source),
          internally_contradicted (another part of the post disagrees),
          stale_risk (presented as current but its own date suggests it may
          have changed by the post date), cannot_verify_offline (fine as
          written, needs a human to check the cited source).
Return:
{"claims":[{"claim":"...","source_as_cited":"...","source_tier":"...",
  "status":"...","note":"..."}],
 "unsourced_count":0,"summary":"one or two sentences"}"""
    return llm.json_chat(SYSTEM, user, max_tokens=10000)


# --------------------------------------------------------------------- report

def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def write_report(slug, ex, rules, cons, claims, meta):
    lines = [f"# Data validation — {slug}", "",
             "> **Tests 2 and 3 are model output, not verified fact.** A flagged claim is a",
             "> prompt to check the cited primary source, never a reason to edit the post",
             "> on its own. Test 1 is deterministic.", "",
             f"Source: `posts/{slug}.html` · title: {ex['title']} · printed date: {ex['date']}",
             f"Run: {meta['when']} · endpoint: {meta['endpoint']} · model: {meta['model']}", "",
             "## 1. House rules (static, deterministic)", "",
             "| rule | severity | result | detail |", "|---|---|---|---|"]
    for name, sev, ok, detail in rules:
        lines.append(f"| {name} | {sev} | {'PASS' if ok else '**FAIL**'} | {md_escape(detail)} |")
    n_fail = sum(1 for r in rules if not r[2])
    lines += ["", f"{len(rules) - n_fail}/{len(rules)} passed.", ""]

    lines += ["## 2. Internal consistency (LLM)", ""]
    if cons is None:
        lines.append(f"_skipped: {meta.get('llm_error') or 'LLM disabled'}_")
    else:
        mm = cons.get("mismatches") or []
        ar = cons.get("arithmetic") or []
        if not mm and not ar:
            lines.append("No mismatches or arithmetic problems reported.")
        if mm:
            lines += ["| quantity | where A | value A | where B | value B | sev | note |",
                      "|---|---|---|---|---|---|---|"]
            for m in mm:
                lines.append("| " + " | ".join(md_escape(m.get(k, "")) for k in
                    ("quantity", "location_a", "value_a", "location_b", "value_b", "severity", "note")) + " |")
            lines.append("")
        if ar:
            lines += ["| arithmetic claim | computed | sev | note |", "|---|---|---|---|"]
            for a in ar:
                lines.append("| " + " | ".join(md_escape(a.get(k, "")) for k in
                    ("claim", "computed", "severity", "note")) + " |")
            lines.append("")
        if cons.get("summary"):
            lines += [f"_{md_escape(cons['summary'])}_", ""]

    lines += ["## 3. Claims ledger (LLM)", ""]
    if claims is None:
        lines.append(f"_skipped: {meta.get('llm_error') or 'LLM disabled'}_")
    else:
        cl = claims.get("claims") or []
        order = {"internally_contradicted": 0, "stale_risk": 1, "cannot_verify_offline": 2, "consistent": 3}
        cl.sort(key=lambda c: order.get(c.get("status", ""), 9))
        counts = {}
        for c in cl:
            counts[c.get("status", "?")] = counts.get(c.get("status", "?"), 0) + 1
        lines.append("Status counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
                     + f" · unsourced (model count): {claims.get('unsourced_count', '?')}")
        lines += ["", "| status | claim | source as cited | tier | note |", "|---|---|---|---|---|"]
        for c in cl:
            st = c.get("status", "")
            st = f"**{st}**" if st in ("internally_contradicted", "stale_risk") else st
            lines.append(f"| {st} | " + " | ".join(md_escape(c.get(k, "")) for k in
                ("claim", "source_as_cited", "source_tier", "note")) + " |")
        if claims.get("summary"):
            lines += ["", f"_{md_escape(claims['summary'])}_"]
    lines.append("")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{slug}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path, n_fail


# ----------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", action="append", default=[], help="post slug under posts/ (repeatable)")
    ap.add_argument("--file", action="append", default=[], help="path to a post HTML file (repeatable)")
    ap.add_argument("--recent", action="store_true", help=f"the recently published set: {', '.join(RECENT)}")
    ap.add_argument("--base-url", default=os.environ.get("LLM_BASE_URL", "http://localhost:20128/v1"),
                    help="OpenAI-compatible base URL (default: OmniRoute on localhost:20128)")
    ap.add_argument("--api-key", default=os.environ.get("LLM_API_KEY"), help="bearer key (or env LLM_API_KEY)")
    ap.add_argument("--model", default=os.environ.get("LLM_MODEL"), help="model id; default: first from /models")
    ap.add_argument("--skip-llm", action="store_true", help="run only the deterministic house rules")
    ap.add_argument("--max-chars", type=int, default=None,
                    help=f"cap prose sent to the LLM (default {PROSE_CAP}); lower this for a "
                         f"provider with a small prompt-length limit, e.g. --max-chars 3000")
    ap.add_argument("--timeout", type=int, default=180)
    args = ap.parse_args()

    files = [pathlib.Path(f) for f in args.file]
    files += [ROOT / "posts" / f"{s}.html" for s in args.slug]
    if args.recent:
        files += [ROOT / "posts" / f"{s}.html" for s in RECENT]
    if not files:
        ap.error("give --slug, --file or --recent")

    llm, llm_error = None, None
    if not args.skip_llm:
        llm = LLM(args.base_url, args.api_key, args.model, args.timeout)
        try:
            print(f"model: {llm.pick_model()}  via {args.base_url}")
        except Exception as e:
            llm_error = str(e)
            print(f"  ! LLM endpoint unavailable ({llm_error}); running house rules only")
            llm = None

    worst = 0
    summary = []
    for path in files:
        slug = path.stem
        if not path.exists():
            print(f"skip (not found): {path}")
            continue
        body = path.read_text(encoding="utf-8")
        ex = extract(body)
        rules = run_house_rules(body)
        cons = claims = None
        err = llm_error
        if llm:
            for label, fn in (("consistency", test_consistency), ("claims", test_claims)):
                try:
                    res = fn(llm, ex, prose_cap=args.max_chars)
                    if label == "consistency":
                        cons = res
                    else:
                        claims = res
                except Exception as e:
                    err = f"{label}: {e}"
                    print(f"  ! {slug}: {err}")
        meta = {"when": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
                "endpoint": re.sub(r"^(https?://[^/]+).*", r"\1", args.base_url),
                "model": llm.model if llm else "-", "llm_error": err}
        rpt, n_fail = write_report(slug, ex, rules, cons, claims, meta)
        blockers = [r[0] for r in rules if not r[2] and r[1] == BLOCKER]
        worst = max(worst, 1 if blockers else 0)
        n_mm = len((cons or {}).get("mismatches") or []) + len((cons or {}).get("arithmetic") or [])
        flagged = sum(1 for c in (claims or {}).get("claims") or []
                      if c.get("status") in ("internally_contradicted", "stale_risk"))
        summary.append((slug, len(rules) - n_fail, len(rules), blockers, n_mm, flagged))
        print(f"-> {rpt.relative_to(ROOT)}  rules {len(rules) - n_fail}/{len(rules)}"
              f"{'  BLOCKER: ' + ','.join(blockers) if blockers else ''}"
              f"  consistency-findings {n_mm if cons is not None else '-'}"
              f"  flagged-claims {flagged if claims is not None else '-'}")
    sys.exit(worst)


if __name__ == "__main__":
    main()
