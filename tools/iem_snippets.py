#!/usr/bin/env python3
"""Collect web-search results for the IEM web check (run on the Mac, with your own API key).

Web search inside a Claude session is capped per turn, so the searches for the
30,000-odd queued company/state pairs run here instead, through a search API,
and only the results (title, URL, snippet) are committed. Agents in a session
then classify each pair from the saved results, with no search cap.

Providers (key read from the environment, never written to disk or git):
    brave    BRAVE_API_KEY                     https://api.search.brave.com
    google   GOOGLE_CSE_KEY + GOOGLE_CSE_CX    Programmable Search JSON API
    serpapi  SERPAPI_KEY                       https://serpapi.com

    export BRAVE_API_KEY=...        (in the shell only)
    python3 tools/iem_snippets.py --provider brave --period 2022-24
    python3 tools/iem_snippets.py --provider brave --period 2017-21
    python3 tools/iem_snippets.py --provider brave --period 2009-16 --queries 1
    python3 tools/iem_snippets.py --provider brave --period 2001-08 --queries 1
    python3 tools/iem_snippets.py --estimate              # queries left, by period

Per pair, query 1 looks for the plant: <company> <district> <product> plant;
query 2 (default for 2017-24) looks for the company: <company> CIN GST. It is
resumable: pairs already in results.jsonl or already collected are skipped, so
stop with Ctrl-C and rerun at any time. Output, gzip JSON lines, one per pair:
    data/iem/webcheck/snippets/<period>/<first id of shard>.jsonl.gz   (500 pairs a shard)
"""
import argparse
import collections
import gzip
import json
import os
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import iem_webcheck as wc  # noqa: E402

SNIP = wc.DIR / "snippets"
SHARD = 500
PERIODS = ["2022-24", "2017-21", "2009-16", "2001-08"]


def clean_name(s):
    """Drop address text the PDF parser glued onto a name ('... TIRUPUR 642154 AHP APPAREL PVT LTD')."""
    s = re.sub(r"\s+", " ", (s or "").replace(" ", " ")).strip(" ,.")
    pins = list(re.finditer(r"\b\d{6}\b", s))
    if pins:
        after, before = s[pins[-1].end():].strip(" ,."), s[:pins[0].start()].strip(" ,.")
        s = after if len(after.split()) >= 2 else before or after
    s = re.sub(r"(?i)^m\s*/\s*s\.?\s*", "", s)
    s = re.sub(r"\bl(ND)l(A)\b", r"I\1I\2", s)                      # OCR: lNDlA -> INDIA
    m = re.search(r"(?i)\b(PRIVATE LIMITED|PVT\.? ?LTD|LIMITED|LTD|LLP)\b\.?", s)
    if m:
        s = s[:m.end()]                                                # cut address after the suffix
    else:
        s = re.split(r"(?i)\s(?:FLAT|PLOT|SURVEY|SY\.? ?NO|S\.? ?NO|VILLAGE|DOOR|H\.? ?NO|GAT NO|KHASRA)\b", s)[0]
    return s.strip(" ,.")


def short_item(s):
    s = re.split(r"[;(]", s or "")[0]
    s = re.sub(r"[^A-Za-z0-9 &/-]", " ", s)
    return " ".join(s.split()[:5]).lower()


def queries(r, n):
    name = clean_name(r["company"])
    district = (r["districts"].split(";")[0] or r["state"]).split("(")[0].strip().title()
    q = [f"{name} {district} {short_item(r['items'])} plant"]
    if n > 1:
        q.append(f"{name} CIN GST")
    return q


def get_json(url, headers):
    req = urllib.request.Request(url, headers={"Accept": "application/json", **headers})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** (attempt + 1))
                continue
            raise


def search(provider, q):
    if provider == "brave":
        d = get_json("https://api.search.brave.com/res/v1/web/search?" +
                     urllib.parse.urlencode({"q": q, "count": 8, "country": "IN"}),
                     {"X-Subscription-Token": os.environ["BRAVE_API_KEY"]})
        items = (d.get("web") or {}).get("results", [])
        return [{"t": i.get("title", ""), "u": i.get("url", ""),
                 "s": re.sub(r"<[^>]+>", "", i.get("description", ""))} for i in items]
    if provider == "google":
        d = get_json("https://www.googleapis.com/customsearch/v1?" +
                     urllib.parse.urlencode({"key": os.environ["GOOGLE_CSE_KEY"], "cx": os.environ["GOOGLE_CSE_CX"],
                                             "q": q, "num": 8, "gl": "in"}), {})
        return [{"t": i.get("title", ""), "u": i.get("link", ""), "s": i.get("snippet", "")} for i in d.get("items", [])]
    if provider == "serpapi":
        d = get_json("https://serpapi.com/search.json?" +
                     urllib.parse.urlencode({"engine": "google", "q": q, "gl": "in", "num": 8,
                                             "api_key": os.environ["SERPAPI_KEY"]}), {})
        return [{"t": i.get("title", ""), "u": i.get("link", ""), "s": i.get("snippet", "")}
                for i in d.get("organic_results", [])]
    raise SystemExit(f"unknown provider {provider}")


def collected():
    ids = set()
    for f in SNIP.rglob("*.jsonl.gz"):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            ids.update(json.loads(line)["id"] for line in fh)
    return ids


def pending(period):
    skip = wc.done_ids() | collected()
    return [r for r in wc.load_queue() if r["period"] == period and int(r["id"]) not in skip]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", choices=["brave", "google", "serpapi"])
    ap.add_argument("--period", choices=PERIODS)
    ap.add_argument("--queries", type=int, choices=[1, 2], help="per pair; default 2 for 2017-24, 1 before")
    ap.add_argument("--limit", type=int, default=0, help="stop after this many pairs")
    ap.add_argument("--qps", type=float, default=1.0, help="queries per second (Brave free tier: 1)")
    ap.add_argument("--estimate", action="store_true")
    args = ap.parse_args()

    if args.estimate:
        for p in PERIODS:
            n = len(pending(p))
            k = args.queries or (2 if p in ("2022-24", "2017-21") else 1)
            print(f"{p}: {n:,} pairs left x {k} = {n * k:,} queries")
        return
    if not (args.provider and args.period):
        ap.error("--provider and --period are required (or --estimate)")
    nq = args.queries or (2 if args.period in ("2022-24", "2017-21") else 1)
    todo = pending(args.period)
    if args.limit:
        todo = todo[:args.limit]
    print(f"{args.period}: {len(todo):,} pairs, {nq} queries each, via {args.provider}")
    (SNIP / args.period).mkdir(parents=True, exist_ok=True)
    gap, last, done, stats = 1.0 / args.qps, 0.0, 0, collections.Counter()
    for r in todo:
        rid = int(r["id"])
        out = SNIP / args.period / f"{(rid - 1) // SHARD * SHARD + 1:05d}.jsonl.gz"
        rec = {"id": rid, "q": []}
        for q in queries(r, nq):
            time.sleep(max(0.0, last + gap - time.time()))
            last = time.time()
            try:
                res = search(args.provider, q)
            except Exception as e:  # noqa: BLE001 - log and keep going; the pair stays pending
                print(f"  {rid}: {type(e).__name__}: {e}")
                stats["errors"] += 1
                rec = None
                break
            rec["q"].append({"q": q, "r": [{**x, "s": x["s"][:300]} for x in res[:8]]})
        if rec is None:
            if stats["errors"] >= 20 and not done:
                sys.exit("20 errors before any success: check the API key and provider")
            continue
        with gzip.open(out, "at", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        done += 1
        stats["results"] += sum(len(x["r"]) for x in rec["q"])
        if done % 100 == 0:
            print(f"  {done:,}/{len(todo):,} pairs")
    print(f"done {done:,} pairs, {stats['results']:,} results, {stats['errors']} errors -> {SNIP / args.period}")


if __name__ == "__main__":
    main()
