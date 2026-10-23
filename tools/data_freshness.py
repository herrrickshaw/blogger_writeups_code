#!/usr/bin/env python3
"""Find figures in published posts that a newer official release has probably superseded.

tools/multi_model_factcheck.py already asks Gemini and Mistral for an "OUTDATED
DATA" section, but an ungrounded model cannot know which 2026 releases exist, so
most of those flags are "maybe check for a newer figure" and some cite releases
that do not exist. This tool splits the job:

  1. Gemini and Mistral each read the post and return a structured inventory of
     its data points: the quote, the value, the period it refers to (normalised
     to an end date), the publisher and series, and how often that series is
     released. Extraction is something these models do well.
  2. This script, not the model, decides staleness: from the period end, the
     release frequency and a typical publication lag, it counts how many newer
     releases have probably come out by today.

Report-only, same contract as the fact-checker: a stale-looking figure is a
prompt to fetch the newer release from the primary source, never an edit.

    python3 tools/data_freshness.py --slug <slug>
    python3 tools/data_freshness.py --all --sleep 20            # resumable; skips posts already done at the same text
    python3 tools/data_freshness.py --all --panel gemini        # one model only (e.g. Mistral quota-capped)
    python3 tools/data_freshness.py --summary                   # out/freshness/SUMMARY.md + worklist.csv
    python3 tools/data_freshness.py --summary --today 2026-10-23
"""
import argparse
import csv
import datetime as dt
import glob
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import multi_model_factcheck as mmf  # noqa: E402  (credentials, text extraction, model names, fallbacks)

ROOT = mmf.ROOT
OUT_DIR = ROOT / "out" / "freshness"
FREQS = ("daily", "weekly", "monthly", "quarterly", "half-yearly", "annual", "multi-year", "live", "one-off")
# Typical gap between the end of a period and the official release, in days, and
# the length of one period. Deliberately generous: a figure is only called stale
# once the next release is very likely out (monthly WPI/CPI/IIP/trade come out
# 12-45 days after the month; quarterly GDP and DPIIT FDI 60-90 days after the
# quarter; most financial-year totals - trade, production, FDI, scheme data - by
# August, though ASI, annual reports and agricultural finals take 12-18 months, so
# an annual flag on those can be early).
LAG = {"daily": 7, "weekly": 14, "monthly": 45, "quarterly": 100, "half-yearly": 120,
       "annual": 150, "multi-year": 365}
PERIOD = {"daily": 1, "weekly": 7, "monthly": 30.4, "quarterly": 91.3, "half-yearly": 182.6,
          "annual": 365.25, "multi-year": 365.25 * 5}
LIVE_STALE_DAYS = 60   # a live counter or dashboard reading older than this is worth re-reading

PROMPT = """You are building a data inventory for an India-focused economics blog post,
so its author can see which figures need refreshing. Read the article below and
list its quantitative data points: statistics from an official or published
series (prices, volumes, output, trade, capacity, budget and scheme figures,
survey results, counts from a dashboard or portal, market data).

For each data point give:
- "quote": the exact words from the article containing the figure (max 30 words)
- "value": the figure as written, with unit
- "period": the period the figure refers to, as written ("May 2026", "FY2024-25",
  "as on 31 Aug 2026", "2023", "Apr-Jun 2026")
- "period_end": that period's last day as YYYY-MM-DD (FY2024-25 -> 2025-03-31,
  May 2026 -> 2026-05-31, calendar 2023 -> 2023-12-31, a dated reading -> that date);
  null if the article gives no period
- "publisher": who publishes the series (e.g. "MoSPI", "RBI", "PPAC", "DGCI&S", "DPIIT", "CEA", "PIB / ministry")
- "series": the series or table name, as specific as the article allows
- "frequency": how often the publisher releases this series, one of:
  daily, weekly, monthly, quarterly, half-yearly, annual, multi-year, live, one-off
  ("live" = a dashboard or counter that changes continuously; "one-off" = a single
  study, report, deal, judgment, census-style event, or a figure that is fixed
  history and will not be revised or extended)
- "headline": true if the figure is in the title, the opening paragraphs, a
  headline stat box or a main chart/table; otherwise false

Rules: list at most 40 data points, headline ones first. Skip pure arithmetic the
article derives itself, historical figures for long-closed periods that the
article uses as history (e.g. a 2010 value in a time series), and figures with
no source. Do not judge whether a figure is outdated and do not add figures that
are not in the article. Return JSON only, in exactly this shape:
{{"data_points": [{{"quote": "...", "value": "...", "period": "...", "period_end": "YYYY-MM-DD", "publisher": "...", "series": "...", "frequency": "monthly", "headline": true}}]}}

ARTICLE TEXT:
{text}"""


def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": mmf.UA, **headers})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=180).read()), None
    except urllib.error.HTTPError as e:
        return None, f"[API error {e.code}: {e.read().decode()[:300]}]"
    except (urllib.error.URLError, OSError) as e:
        return None, f"[network error: {e}]"


def ask_gemini(k, text, model):
    d, err = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={k}",
                   {"contents": [{"parts": [{"text": PROMPT.format(text=text)}]}],
                    "generationConfig": {"temperature": 0.0, "responseMimeType": "application/json"}}, {})
    if err:
        return "Gemini " + err
    cand = (d.get("candidates") or [{}])[0]
    return "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", [])).strip() or "[empty response]"


def ask_mistral(k, text, model):
    d, err = _post(mmf.MISTRAL_URL,
                   {"model": model, "temperature": 0.0, "response_format": {"type": "json_object"},
                    "messages": [{"role": "user", "content": PROMPT.format(text=text)}]},
                   {"Authorization": f"Bearer {k}"})
    if err:
        return "Mistral " + err
    try:
        return d["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        return f"[Mistral unexpected response: {json.dumps(d)[:300]}]"


def parse(out):
    """The model's JSON as a list of data points, or None if it isn't usable JSON."""
    s = re.sub(r"^```(?:json)?\s*|\s*```$", "", out.strip())
    try:
        d = json.loads(s)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", s, re.S)
        try:
            d = json.loads(m.group(0)) if m else None
        except json.JSONDecodeError:
            return None
    pts = d.get("data_points") if isinstance(d, dict) else d if isinstance(d, list) else None
    if not isinstance(pts, list):
        return None
    return [p for p in pts if isinstance(p, dict) and p.get("value")]


def failed(out):
    return out.startswith(("Gemini [", "Mistral [", "[")) and ("error" in out or "unexpected" in out or "empty" in out)


# A model that answered 429 is skipped until its cooldown ends, so each post
# does not spend a call on it first. A daily quota ("exceeded your current
# quota", RESOURCE_EXHAUSTED) is out for the rest of the run; a per-minute rate
# limit for ten minutes. 2026-10-23: gemini-flash-latest was out of daily quota
# and mistral-small/-medium rate-limited, so every post made three dead calls.
COOLDOWN = {}
DAILY = re.compile(r"exceeded your current quota|RESOURCE_EXHAUSTED|per day", re.I)


def ask_with_fallback(fn, k, text, models):
    """Each model in turn on any failure or unusable JSON; one paced retry of the list."""
    out, m = "", models[0]
    for attempt in range(2):
        live = [x for x in models if COOLDOWN.get(x, 0) <= time.time()] or models
        for m in live:
            out = fn(k, text, m)
            if not failed(out) and parse(out) is not None:
                return m, out
            if "API error 429" in out:
                COOLDOWN[m] = time.time() + (24 * 3600 if DAILY.search(out) else 600)
                print(f"    {m}: 429, skipped for " + ("this run" if DAILY.search(out) else "10 min"))
            if mmf.TERMINAL.search(out) and "404" not in out:
                return m, out
        if attempt == 0:
            time.sleep(45)
    return m, out


def done(slug, sha, panel):
    p = OUT_DIR / f"{slug}.json"
    if not p.exists():
        return False
    r = json.loads(p.read_text(encoding="utf-8"))
    if r.get("skipped"):
        return r.get("text_sha1") == sha
    return r.get("text_sha1") == sha and all(r.get("models", {}).get(x, {}).get("ok") for x in panel)


def run_one(path, keys, panel):
    slug = pathlib.Path(path).stem
    text = mmf.extract_text(path)
    sha = mmf.text_sha(text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rec = {"slug": slug, "text_sha1": sha, "chars": len(text),
           "checked": dt.datetime.now().isoformat(timespec="seconds"), "models": {}}
    print(f"… {slug}  ({len(text)} chars)")
    if len(text) > mmf.MAX_CHARS:
        rec["skipped"] = f"too large: {len(text):,} chars > {mmf.MAX_CHARS:,}"
        (OUT_DIR / f"{slug}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False), encoding="utf-8")
        print("  -> skipped, too large")
        return False
    prior = OUT_DIR / f"{slug}.json"
    if prior.exists():   # keep a model's clean answer from an earlier run at the same text
        old = json.loads(prior.read_text(encoding="utf-8"))
        if old.get("text_sha1") == sha:
            rec["models"] = {k: v for k, v in old.get("models", {}).items() if v.get("ok")}
    for name in panel:
        if rec["models"].get(name, {}).get("ok"):
            continue
        if name == "gemini":
            m, out = ask_with_fallback(ask_gemini, keys["gemini"], text, [mmf.GEMINI_MODEL] + mmf.GEMINI_FALLBACKS)
        else:
            m, out = ask_with_fallback(ask_mistral, keys["mistral"], text, [mmf.MISTRAL_MODEL] + mmf.MISTRAL_FALLBACKS)
        pts = None if failed(out) else parse(out)
        rec["models"][name] = {"model": m, "ok": pts is not None, "data_points": pts or [],
                               **({} if pts is not None else {"error": out[:400]})}
        print(f"  {name:8} {m:26} " + (f"{len(pts)} data points" if pts is not None else out[:100]))
        time.sleep(1)
    (OUT_DIR / f"{slug}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False), encoding="utf-8")
    return not any(v["ok"] for v in rec["models"].values())


# ------------------------------------------------------------------ staleness
def releases_behind(p, today):
    """(releases probably published since this figure's period, reason) or (None, reason)."""
    f = str(p.get("frequency") or "").lower().strip()
    if f not in FREQS:
        return None, "unknown frequency"
    if f == "one-off":
        return None, "one-off"
    try:
        end = dt.date.fromisoformat(str(p.get("period_end"))[:10])
    except ValueError:
        return None, "no period"
    if end > today:
        return None, "period ends after today"
    age = (today - end).days
    if f == "live":
        return (1 if age > LIVE_STALE_DAYS else 0), f"live reading {age} days old"
    # the k-th later period ends k*PERIOD after this one and is out LAG days after that
    n = int((age - LAG[f]) // PERIOD[f]) if age >= LAG[f] else 0
    return n, f"{f}, period ended {end}"


def key_of(p):
    """Loose identity for matching the same data point across models."""
    nums = re.findall(r"\d[\d,.]*", str(p.get("value", "")))
    return (nums[0].replace(",", "").rstrip(".") if nums else str(p.get("value"))[:20].lower(),
            str(p.get("period_end"))[:7])


def summary(today, out_md, out_csv):
    rows, pending, skipped = [], [], []
    for f in sorted(OUT_DIR.glob("*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))
        if r.get("skipped"):
            skipped.append((r["slug"], r["skipped"]))
            continue
        good = {n: v for n, v in r.get("models", {}).items() if v.get("ok")}
        if not good:
            pending.append(r["slug"])
            continue
        seen = {}
        for name, v in good.items():
            for p in v["data_points"]:
                k = key_of(p)
                if k in seen:
                    seen[k]["models"].add(name)
                    continue
                n, why = releases_behind(p, today)
                seen[k] = {"slug": r["slug"], "models": {name}, "behind": n, "why": why, **p}
        rows += list(seen.values())
    # Score each post on its FRONTIER, not on every figure. A post's 2000-01 or
    # 2016-17 value is history in a time series, not a stale figure; what matters
    # is the newest period it has for each publisher and release frequency. If
    # that newest period is current, the post is current for that source (this
    # also covers posts whose "Updated" note already carries the newer figure).
    # Tested 2026-10-23 on the FDI sector post: per-figure scoring flagged 24
    # historical values; the frontier (June 2026, quarterly) is current.
    pub = lambda x: re.sub(r"\W+", " ", re.sub(r"\(.*?\)", "", str(x.get("publisher") or "?"))).strip().lower()
    groups = {}
    for x in rows:
        if x["behind"] is None:
            continue
        groups.setdefault((x["slug"], pub(x), x.get("frequency")), []).append(x)
    stale = []
    for (slug, _, _), xs in groups.items():
        front = max(str(x.get("period_end")) for x in xs)
        top = [x for x in xs if str(x.get("period_end")) == front]
        if not top[0]["behind"]:
            continue
        lead = max(top, key=lambda x: (bool(x.get("headline")), len(x["models"])))
        stale.append({**lead, "models": set().union(*(x["models"] for x in top)),
                      "headline": any(x.get("headline") for x in top), "n_points": len(xs)})
    refreshed = sum(1 for x in rows if x["behind"]) - sum(x["n_points"] for x in stale)
    stale.sort(key=lambda x: (-bool(x.get("headline")), -x["behind"], -len(x["models"]), x["slug"]))
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["slug", "headline", "releases_behind", "models", "frequency", "period", "period_end",
                    "publisher", "series", "value", "quote"])
        for x in stale:
            w.writerow([x["slug"], bool(x.get("headline")), x["behind"], "+".join(sorted(x["models"])),
                        x.get("frequency"), x.get("period"), x.get("period_end"), x.get("publisher"),
                        x.get("series"), x.get("value"), x.get("quote")])
    by_post = {}
    for x in stale:
        by_post.setdefault(x["slug"], []).append(x)
    score = lambda xs: sum((3 if x.get("headline") else 1) * min(x["behind"], 6) for x in xs)
    ranked = sorted(by_post.items(), key=lambda kv: -score(kv[1]))
    series = {}
    for x in stale:
        s = f'{x.get("publisher") or "?"}: {x.get("series") or "?"}'
        series.setdefault(s, set()).add(x["slug"])
    md = [f"# Data freshness worklist, as of {today}", "",
          "> **Model extraction, script judgement, not verified fact.** Gemini/Mistral listed each post's data",
          "> points; this script counted how many newer releases have *probably* come out, from the period end,",
          "> release frequency and a typical lag. Fetch the newer release from the primary source before changing",
          "> anything (house rule: PIB / MoSPI / RBI / DGCI&S / PPAC / ministry originals).", "",
          f"{len(rows)} data points from {len({x['slug'] for x in rows})} posts; "
          f"{len(stale)} probably superseded ({sum(1 for x in stale if x.get('headline'))} headline) "
          f"across {len(by_post)} posts, counted once per publisher and release frequency at the post's newest "
          f"period ({refreshed} older figures not listed because the post already has a newer one from that source). {len(pending)} posts have no clean model answer yet; "
          f"{len(skipped)} skipped as too large. Full list: `{pathlib.Path(out_csv).relative_to(ROOT)}`.", "",
          "## Series behind in the most posts", "",
          "| Publisher / series | Posts |", "|---|---|"]
    for s, slugs in sorted(series.items(), key=lambda kv: -len(kv[1]))[:30]:
        md.append(f"| {s} | {len(slugs)} |")
    md += ["", "## Posts ranked by stale data (headline figures weighted x3)", ""]
    for slug, xs in ranked:
        md.append(f"### {slug}  (score {score(xs)})")
        for x in sorted(xs, key=lambda x: (-bool(x.get("headline")), -x["behind"])):
            md.append(f'- {"**H** " if x.get("headline") else ""}{x.get("value")} — {x.get("period")} '
                      f'({x.get("publisher")}: {x.get("series")}; {x.get("frequency")}) — '
                      f'~{x["behind"]} newer release(s), {x["n_points"]} figure(s) from this source [{"+".join(sorted(x["models"]))}]')
        md.append("")
    if pending:
        md += ["## No clean model answer yet", "", ", ".join(pending), ""]
    if skipped:
        md += ["## Skipped (too large)", ""] + [f"- {s}: {why}" for s, why in skipped] + [""]
    pathlib.Path(out_md).write_text("\n".join(md), encoding="utf-8")
    print(f"{len(rows)} data points, {len(stale)} probably superseded in {len(by_post)} posts, "
          f"{len(pending)} pending -> {pathlib.Path(out_md).relative_to(ROOT)}, {pathlib.Path(out_csv).relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--slug")
    g.add_argument("--file")
    g.add_argument("--all", action="store_true")
    g.add_argument("--summary", action="store_true")
    ap.add_argument("--panel", default="gemini,mistral", help="gemini, mistral or both (default both)")
    ap.add_argument("--sleep", type=float, default=0, help="seconds between posts (~20 suits the free tiers)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true", help="re-run posts already done at the same text")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD for --summary (default: today)")
    args = ap.parse_args()

    if args.summary:
        today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
        return summary(today, OUT_DIR / "SUMMARY.md", OUT_DIR / "worklist.csv")

    panel = tuple(p.strip().lower() for p in args.panel.split(",") if p.strip())
    if not panel or set(panel) - {"gemini", "mistral"}:
        sys.exit("--panel: choose gemini, mistral or gemini,mistral")
    blob = mmf.creds()
    keys = {n: mmf.key({"gemini": "GEMINI_API_KEY", "mistral": "MISTRAL_API_KEY"}[n], blob) for n in panel}

    if args.all:
        files = [f for f in sorted(glob.glob(str(ROOT / "posts" / "*.html")))
                 if pathlib.Path(f).stem not in mmf.SKIP_SLUGS]
        if not args.force:
            before = len(files)
            files = [f for f in files
                     if not done(pathlib.Path(f).stem, mmf.text_sha(mmf.extract_text(f)), panel)]
            print(f"resuming: {before - len(files)} already done, {len(files)} remaining")
        if args.limit:
            files = files[:args.limit]
    else:
        files = [args.file or str(ROOT / "posts" / f"{args.slug}.html")]

    fails = 0
    for i, f in enumerate(files):
        all_failed = run_one(f, keys, panel)
        fails = fails + 1 if all_failed else 0
        if args.all and fails >= 2:
            print(f"stopping early: 2 posts in a row failed on every model (likely a quota wall). "
                  f"{len(files) - i - 1} left; re-run --all later, done posts are skipped.")
            break
        if args.sleep and i < len(files) - 1:
            time.sleep(args.sleep)


if __name__ == "__main__":
    main()
