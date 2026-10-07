#!/usr/bin/env python3
"""Web check of every IEM Part A filing with no Part B: was the plant built anyway?

The check runs as batches of research agents (web search for the company's CIN
and status, website, and news of the plant at the filed district). This script
keeps the queue and the results, so the work can stop and resume across sessions.

    python3 tools/iem_webcheck.py queue                 # data/iem/webcheck/queue.csv
    python3 tools/iem_webcheck.py batches --period 2022-24 --size 25 > batches.json
    python3 tools/iem_webcheck.py snipbatches --period 2022-24 --out DIR   # from saved search results
    python3 tools/iem_webcheck.py ingest JOURNAL.jsonl  # agent results -> results.jsonl
    python3 tools/iem_webcheck.py summary               # data/iem/webcheck/summary.md

Unit: a (company, plant state) pair among Part A lines with no Part B found,
names normalised as in iem_records.py. Periods: 2001-08, 2009-16, 2017-21,
2022-24 (filing year of the earliest line). Pairs already checked in the
40-filing sample (iem_noB_sample_webcheck_2026-10-07.csv) are carried over.

Classifications: built, under_construction_or_announced, dropped_or_failed,
company_active_no_project_evidence, not_found. Results are research leads from
web search, not verified facts; each row keeps its evidence and source URLs.
"""
import argparse
import collections
import csv
import json
import pathlib
import random
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import iem_records as m  # noqa: E402

DIR = ROOT / "data" / "iem" / "webcheck"
QUEUE = DIR / "queue.csv"
RESULTS = DIR / "results.jsonl"
SAMPLE = ROOT / "data" / "iem" / "iem_noB_sample_webcheck_2026-10-07.csv"
CLASSES = ["built", "under_construction_or_announced", "dropped_or_failed",
           "company_active_no_project_evidence", "not_found"]


def period(y):
    return "2001-08" if y <= 2008 else "2009-16" if y <= 2016 else "2017-21" if y <= 2021 else "2022-24"


def key(company, state):
    return m.norm_company(company) + "|" + m.norm_state(state)


def queue(args):
    csv.field_size_limit(10 ** 8)
    A = [r for r in csv.DictReader(open(ROOT / "data/iem/iem_records.csv", encoding="utf-8"))
         if r["part"] == "A" and r["in_part_b"] == "no"]
    pairs = collections.defaultdict(list)
    for r in A:
        if len(m.norm_company(r["company"])) < 4:
            continue
        pairs[key(r["company"], r["state"])].append(r)
    rows = []
    for k, ls in pairs.items():
        def yr(r):
            d = m.pdate(r["iem_date"])
            return d.year if d else int(r["period_from"][:4])
        ls.sort(key=yr)
        f = ls[0]
        rows.append({"key": k, "period": period(yr(f)), "first_year": yr(f), "last_year": yr(ls[-1]),
                     "company": f["company"].strip(" ,."), "state": f["state"],
                     "districts": "; ".join(sorted({r["district"] for r in ls if r["district"]}))[:80],
                     "iem_no": f["iem_no"], "iem_date": f["iem_date"],
                     "items": "; ".join(sorted({r["item"][:50] for r in ls if r["item"]}))[:140],
                     "lines": len(ls)})
    order = {"2022-24": 0, "2017-21": 1, "2009-16": 2, "2001-08": 3}
    random.seed(20261007)
    random.shuffle(rows)
    rows.sort(key=lambda r: order[r["period"]])
    for i, r in enumerate(rows, 1):
        r["id"] = i
    DIR.mkdir(parents=True, exist_ok=True)
    with open(QUEUE, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id"] + [k for k in rows[0] if k != "id"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows):,} pairs -> {QUEUE}", collections.Counter(r["period"] for r in rows))


def load_queue():
    return list(csv.DictReader(open(QUEUE, encoding="utf-8")))


def done_ids():
    ids = set()
    if RESULTS.exists():
        for line in open(RESULTS, encoding="utf-8"):
            ids.add(int(json.loads(line)["id"]))
    return ids


def batches(args):
    q = [r for r in load_queue() if r["period"] == args.period and int(r["id"]) not in done_ids()]
    if args.limit:
        q = q[:args.limit]
    out = []
    for i in range(0, len(q), args.size):
        chunk = q[i:i + args.size]
        out.append({"batch": f"{args.period}-{int(chunk[0]['id']):05d}",
                    "rows": "\n".join(f"{r['id']} | {r['company']} | {r['state']} | {r['districts']} | "
                                      f"IEM {r['iem_no']} of {r['iem_date']} | {r['items']}" for r in chunk)})
    json.dump(out, sys.stdout)
    print(f"\n{len(q):,} pairs in {len(out)} batches", file=sys.stderr)


def snipbatches(args):
    """Turn collected search results (tools/iem_snippets.py) into batch files for classifier agents."""
    import gzip
    q = {int(r["id"]): r for r in load_queue()}
    done = done_ids()
    recs = []
    for f in sorted((DIR / "snippets" / args.period).glob("*.jsonl.gz")):
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            recs += [json.loads(line) for line in fh]
    recs = sorted((r for r in recs if r["id"] not in done), key=lambda r: r["id"])
    out = pathlib.Path(args.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    names = []
    for i in range(0, len(recs), args.size):
        chunk = recs[i:i + args.size]
        name = f"s{args.period}-{chunk[0]['id']:05d}"
        lines = []
        for rec in chunk:
            r = q[rec["id"]]
            lines.append(f"=== {r['id']} | {r['company']} | {r['state']} | {r['districts']} | "
                         f"IEM {r['iem_no']} of {r['iem_date']} | {r['items']}")
            for qq in rec["q"]:
                lines.append(f"  search: {qq['q']}")
                for x in qq["r"] or []:
                    lines.append(f"   - {x['t']} | {x['u']} | {x['s']}")
                if not qq["r"]:
                    lines.append("   (no results)")
        (out / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        names.append(name)
    json.dump(names, sys.stdout)
    print(f"\n{len(recs):,} pairs with search results in {len(names)} batches -> {out}", file=sys.stderr)


def ingest(args):
    """Pull the validated rows out of a workflow journal (or any JSONL whose
    records hold {"rows": [...]} somewhere) and append new ids to results.jsonl."""
    valid = {int(r["id"]) for r in load_queue()}
    have = done_ids()
    new, verdicts = {}, {}

    def walk(o):
        if isinstance(o, dict):
            if "id" in o and "verdict" in o:
                try:
                    verdicts[int(o["id"])] = o
                except (TypeError, ValueError):
                    pass
                return
            if "id" in o and "classification" in o:
                try:
                    i = int(o["id"])
                except (TypeError, ValueError):
                    return
                ev = str(o.get("evidence", ""))
                unchecked = ev.upper().startswith("UNCHECKED") or re.search(
                    r"(?i)budget|exhaust|prior knowledge|not verified this session", ev)
                if i in valid and i not in have and o["classification"] in CLASSES and not unchecked:
                    new[i] = o
                return
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str) and o[:1] in "[{" and '"classification"' in o:
            try:
                walk(json.loads(o))
            except ValueError:
                pass

    for path in args.journal:
        for line in open(path, encoding="utf-8"):
            try:
                walk(json.loads(line))
            except ValueError:
                continue
    with open(RESULTS, "a", encoding="utf-8") as fh:
        for i in sorted(new):
            row = {"id": i, **{k: v for k, v in new[i].items() if k != "id"}}
            v = verdicts.get(i)
            if v:
                row.update({"verdict": v["verdict"], "verify_note": v.get("verify_note", ""),
                            "verify_sources": v.get("verify_sources", [])})
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{len(new):,} new results ({sum(1 for i in new if i in verdicts):,} with a second-agent verdict); "
          f"{len(have) + len(new):,} of {len(valid):,} pairs done")


def summary(args):
    q = {int(r["id"]): r for r in load_queue()}
    res = [json.loads(line) for line in open(RESULTS, encoding="utf-8")] if RESULTS.exists() else []
    by = collections.defaultdict(collections.Counter)
    for r in res:
        by[q[int(r["id"])]["period"]][r["classification"]] += 1
    tot = collections.Counter(r["period"] for r in q.values())
    md = ["# IEM filings with no Part B: web check", "",
          "Unit: a company and plant state with Part A filings but no Part B found in DPIIT's lists "
          "(January 2001 to August 2024). Each was checked by web search for the company's CIN and status, "
          "website, and news of the plant at the filed district. Results are research leads from search "
          "snippets, not verified facts; see results.jsonl for evidence and sources.", "",
          "| Filed | Pairs | Checked | " + " | ".join(c.replace("_", " ") for c in CLASSES) + " |",
          "|---|---|---|" + "---|" * len(CLASSES)]
    for p in ("2022-24", "2017-21", "2009-16", "2001-08"):
        c = by[p]
        n = sum(c.values())
        cells = " | ".join(f"{c[k]:,} ({100 * c[k] / n:.0f}%)" if n else "&ndash;" for k in CLASSES)
        md.append(f"| {p} | {tot[p]:,} | {n:,} | {cells} |")
    (DIR / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("queue").set_defaults(fn=queue)
    b = sub.add_parser("batches")
    b.add_argument("--period", required=True, choices=["2022-24", "2017-21", "2009-16", "2001-08"])
    b.add_argument("--size", type=int, default=25)
    b.add_argument("--limit", type=int, default=0)
    b.set_defaults(fn=batches)
    sb = sub.add_parser("snipbatches")
    sb.add_argument("--period", required=True, choices=["2022-24", "2017-21", "2009-16", "2001-08"])
    sb.add_argument("--size", type=int, default=25)
    sb.add_argument("--out", required=True)
    sb.set_defaults(fn=snipbatches)
    i = sub.add_parser("ingest")
    i.add_argument("journal", nargs="+")
    i.set_defaults(fn=ingest)
    sub.add_parser("summary").set_defaults(fn=summary)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
