#!/usr/bin/env python3
"""Check IEM companies against PARIVESH: which ones have an Environmental Clearance (EC).

PARIVESH 2.0 (MoEFCC's clearance portal) serves its whole EC register, central
(MoEFCC) and state (SEIAA) proposals alike, from one open JSON endpoint:
    https://parivesh.nic.in/parivesh_api/trackYourProposal/advanceSearchData
        ?majorClearanceType=1&state=&proposalStatus=&pageNo=0&pageSize=200000
(the call herrrickshaw/india-ec-subsector-analysis/scripts/refresh_ec.py uses).
It covers proposals submitted on PARIVESH 2.0, i.e. from 2022. ECs granted
before that sit on the legacy environmentclearance.nic.in site and are NOT
checked here, so an IEM filed in 2005 with no EC match may well have had one.

    python3 tools/iem_parivesh.py fetch     # one GET (~130 MB), saved to cache/
    python3 tools/iem_parivesh.py fetch --from DUMP.json   # or reuse a saved dump
    python3 tools/iem_parivesh.py inspect   # record count, field names, sample values
    python3 tools/iem_parivesh.py match     # writes data/iem/iem_parivesh_ec.csv + summary

Matching is by company name, after removing M/s, Pvt, Ltd and the like and all
punctuation and spaces (the same rule iem_records.py uses to link Part A and
Part B). A match in the same state is "name+state"; elsewhere it is "name".
A name match says the company sought or got an EC for some project from 2022,
not that it is the project in the IEM: check the proposal numbers.

Outputs (data/iem/):
    iem_parivesh_ec.csv          one row per IEM Part A line, with the EC proposals
                                 of the same company (best status first)
    iem_parivesh_ec_summary.md   counts by filing year and Part B status, and the
                                 companies with an EC granted but no Part B
"""
import argparse
import collections
import csv
import datetime
import gzip
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import iem_records as m  # noqa: E402

URL = "https://parivesh.nic.in/parivesh_api/trackYourProposal/advanceSearchData"
CACHE = ROOT / "cache"
OUT = ROOT / "data" / "iem"

# Field names are not documented; these are guesses tried in order, and any key
# containing the hint word is used if none match. Override with --field.
FIELDS = {
    "name": (["proponentName", "nameOfProponent", "nameOfUserAgency", "userAgencyName", "companyName", "proponent",
              "organisationName", "organizationName", "applicantName"], ("proponent", "company", "agency", "organi", "applicant")),
    "state": (["stateName", "state", "projectState"], ("state",)),
    "status": (["proposalStatus", "status", "currentStatus"], ("status",)),
    "proposal_no": (["proposalNo", "proposal_no", "proposalNumber", "singleWindowNumber"], ("proposalno", "proposalnum")),
    "project": (["projectName", "proposalName", "nameOfProject", "project_name"], ("projectname", "proposalname")),
    "date": (["dateOfSubmission", "submissionDate", "proposalDate", "createdOn", "dateOfIssue"], ("date",)),
    "sector": (["sectorName", "sector", "activityName"], ("sector",)),
}


def latest_cache():
    files = sorted(CACHE.glob("parivesh_ec_*.json.gz"))
    if not files:
        sys.exit("no cache/parivesh_ec_*.json.gz; run: python3 tools/iem_parivesh.py fetch")
    return files[-1]


def fetch(args):
    CACHE.mkdir(exist_ok=True)
    if args.src:
        raw = pathlib.Path(args.src).expanduser().read_bytes()
        body = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
        out = CACHE / f"parivesh_ec_{datetime.date.today():%Y-%m-%d}.json.gz"
        out.write_bytes(gzip.compress(body))
        print(f"{len(body):,} bytes from {args.src} -> {out}")
        print(f"{len(records(json.loads(body))):,} proposals")
        return
    url = URL + "?" + args.query
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "Mozilla/5.0 (masaladeutsch-archive iem_parivesh.py)"})
    print("GET", url)
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            body = r.read()
    except urllib.error.HTTPError as e:
        # advanceSearchData was withdrawn from the open API (404 on 2026-11-14). Fall back to a saved dump
        # (`fetch --from DUMP.json`), or the anonymous central-only dashboard route; see
        # herrrickshaw/india-ec-subsector-analysis data/library/SOURCES.md.
        sys.exit(f"HTTP {e.code} from {url}: endpoint withdrawn. Use `fetch --from DUMP.json` or see SOURCES.md.")
    out = CACHE / f"parivesh_ec_{datetime.date.today():%Y-%m-%d}.json.gz"
    out.write_bytes(gzip.compress(body))
    print(f"{len(body):,} bytes -> {out}")
    recs = records(json.loads(body))
    print(f"{len(recs):,} proposals")


def records(obj):
    """The largest list of dicts anywhere in the response."""
    best = []
    stack = [obj]
    while stack:
        o = stack.pop()
        if isinstance(o, list):
            if o and all(isinstance(x, dict) for x in o[:50]) and len(o) > len(best):
                best = o
            stack.extend(x for x in o[:50] if isinstance(x, (dict, list)))
        elif isinstance(o, dict):
            stack.extend(v for v in o.values() if isinstance(v, (dict, list)))
    return best


def flat(d, pre=""):
    """Nested dicts become a.b keys; other_property, a JSON string of
    [{"label": ..., "value": ...}] pairs (Activity, Category, ...), becomes op.<label>."""
    out = {}
    if isinstance(d.get("other_property"), str):
        try:
            for p in json.loads(d["other_property"] or "[]"):
                if isinstance(p, dict) and "label" in p:
                    out["op." + str(p["label"])] = p.get("value")
        except ValueError:
            pass
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(flat(v, pre + k + "."))
        elif not isinstance(v, list):
            out[pre + k] = v
    return out


def pick(keys, overrides):
    got = {}
    low = {k.lower().replace("_", "").split(".")[-1]: k for k in keys}
    for f, (names, hints) in FIELDS.items():
        if f in overrides:
            got[f] = overrides[f]
            continue
        k = next((low[n.lower().replace("_", "")] for n in names if n.lower().replace("_", "") in low), None)
        if k is None:
            k = next((orig for lk, orig in low.items() if any(h in lk for h in hints)), None)
        got[f] = k
    return got


def load(args):
    path = latest_cache()
    recs = [flat(r) for r in records(json.loads(gzip.decompress(path.read_bytes())))]
    keys = collections.Counter(k for r in recs[:2000] for k in r)
    overrides = dict(x.split("=", 1) for x in args.field)
    return path, recs, keys, pick(keys, overrides)


def inspect(args):
    path, recs, keys, f = load(args)
    print(f"{path.name}: {len(recs):,} proposals\n\nfields (in first 2,000 records):")
    for k, n in keys.most_common():
        ex = next((str(r[k])[:70] for r in recs[:500] if r.get(k) not in (None, "")), "")
        print(f"  {k:40s} {n:5d}  e.g. {ex}")
    print("\nfields used:", json.dumps(f, indent=1))
    if f["status"]:
        print("\nstatus values:")
        for s, n in collections.Counter(str(r.get(f["status"])) for r in recs).most_common(60):
            print(f"  {n:7,d}  {s}  -> {stage(s)}")


def stage(s):
    s = (s or "").upper()
    for pat, name in (("DELIST", "delisted"), ("REJECT", "rejected"), ("WITHDRAW", "withdrawn"),
                      ("RETURN", "returned"), (r"\bTOR\b|TERMS OF REFERENCE", "tor_granted"),
                      ("GRANT|ISSUED|APPROVED", "granted"), ("CLOSE", "closed")):
        if re.search(pat, s):
            if name == "tor_granted" and not re.search("GRANT|ISSUED|APPROVED", s):
                continue
            return name
    return "in_process"


RANK = {"granted": 0, "tor_granted": 1, "in_process": 2, "returned": 3, "withdrawn": 4,
        "rejected": 5, "closed": 6, "delisted": 7}


def norm_name(s):
    s = (s or "").upper().replace("&", " AND ")
    s = re.sub(r"^\s*M\s*/\s*S\.?\s*", "", s)
    s = re.sub(r"\bM/S\.?\s*", " ", s)
    return m.norm_company(s)


def match(args):
    path, recs, keys, f = load(args)
    if not f["name"]:
        sys.exit("could not find the proponent/company field; run inspect and pass --field name=<key>")
    print(f"{path.name}: {len(recs):,} proposals; fields {f}")
    ec = collections.defaultdict(list)
    for r in recs:
        n = norm_name(str(r.get(f["name"]) or ""))
        if len(n) < 4:
            continue
        ec[n].append({"proposal_no": str(r.get(f["proposal_no"]) or ""),
                      "state": m.norm_state(str(r.get(f["state"]) or "")),
                      "status": str(r.get(f["status"]) or ""),
                      "stage": stage(str(r.get(f["status"]) or "")),
                      "project": str(r.get(f["project"]) or "")[:120],
                      "date": str(r.get(f["date"]) or "")[:10],
                      "sector": str(r.get(f["sector"]) or ""),
                      "proponent": str(r.get(f["name"]) or "")})
    print(f"{len(ec):,} distinct proponent names")

    csv.field_size_limit(10 ** 8)
    rows = list(csv.DictReader(open(OUT / "iem_records.csv", encoding="utf-8")))
    A = [r for r in rows if r["part"] == "A"]
    out_rows, stats = [], collections.Counter()
    by_year = collections.defaultdict(collections.Counter)
    no_b_granted = collections.defaultdict(lambda: {"lines": 0, "proposals": set(), "years": set(), "states": set()})
    for r in A:
        props = ec.get(norm_name(r["company"]), [])
        st = m.norm_state(r["state"])
        same = [p for p in props if p["state"] == st] if st else []
        use, kind = (same, "name+state") if same else (props, "name" if props else "")
        use = sorted(use, key=lambda p: (RANK[p["stage"]], p["date"]))
        best = use[0]["stage"] if use else ""
        d = m.pdate(r["iem_date"])
        y = d.year if d else int(r["period_from"][:4])
        b = "yes" if r["in_part_b"] != "no" else "no"
        by_year[y][(b, kind, best == "granted")] += 1
        stats[(kind, best)] += 1
        if b == "no" and kind == "name+state" and best == "granted":
            k = (r["company"].strip(), st)
            no_b_granted[k]["lines"] += 1
            no_b_granted[k]["years"].add(y)
            no_b_granted[k]["proposals"].update(p["proposal_no"] for p in use if p["stage"] == "granted")
        out_rows.append({"iem_no": r["iem_no"], "iem_date": r["iem_date"], "company": r["company"],
                         "item": r["item"], "district": r["district"], "state": r["state"],
                         "in_part_b": r["in_part_b"], "ec_match": kind, "ec_best_stage": best,
                         "ec_granted": sum(p["stage"] == "granted" for p in use),
                         "ec_proposals": len(use),
                         "ec_list": " | ".join(f"{p['proposal_no']} {p['stage']} {p['date']} {p['state']}: {p['project']}"
                                               for p in use[:5])})
    with open(OUT / "iem_parivesh_ec.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0]))
        w.writeheader()
        w.writerows(out_rows)

    md = [f"# IEM Part A companies on PARIVESH (EC register, {path.stem[12:22]})", "",
          f"PARIVESH 2.0 EC register: {len(recs):,} proposals, {len(ec):,} proponent names. "
          "It holds proposals submitted from 2022; earlier ECs (legacy environmentclearance.nic.in) are not checked.",
          "Matched by company name with M/s, Pvt, Ltd and punctuation removed; `name+state` = an EC proposal "
          "from the same company in the plant's state. A match is the company, not necessarily the same project.", "",
          "| Filed in | Part A lines | Company has EC granted (same state) | of which no Part B | Any EC proposal (same state) |",
          "|---|---|---|---|---|"]
    for y in sorted(by_year):
        c = by_year[y]
        tot = sum(c.values())
        g = sum(n for (b, k, gr), n in c.items() if k == "name+state" and gr)
        g_nob = sum(n for (b, k, gr), n in c.items() if k == "name+state" and gr and b == "no")
        anyp = sum(n for (b, k, gr), n in c.items() if k == "name+state")
        md.append(f"| {y} | {tot:,} | {g:,} | {g_nob:,} | {anyp:,} |")
    md += ["", "## Companies with an EC granted in the plant's state but no Part B found", "",
           "| Company | State | Part A lines | Filed | EC proposals granted |", "|---|---|---|---|---|"]
    for (co, st), v in sorted(no_b_granted.items(), key=lambda kv: (-max(kv[1]["years"]), kv[0])):
        yrs = sorted(v["years"])
        md.append(f"| {co} | {st.title()} | {v['lines']} | {yrs[0]}{'–' + str(yrs[-1]) if len(yrs) > 1 else ''} "
                  f"| {', '.join(sorted(v['proposals'])[:4])}{' …' if len(v['proposals']) > 4 else ''} |")
    (OUT / "iem_parivesh_ec_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    n_any = sum(n for (k, b), n in stats.items() if k)
    n_g = sum(n for (k, b), n in stats.items() if k == "name+state" and b == "granted")
    print(f"Part A lines: {len(A):,}; company on PARIVESH: {n_any:,}; EC granted in same state: {n_g:,}; "
          f"companies with EC granted, same state, no Part B: {len(no_b_granted):,}")
    print("->", OUT / "iem_parivesh_ec.csv", "and iem_parivesh_ec_summary.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["fetch", "inspect", "match"])
    ap.add_argument("--query", default="majorClearanceType=1&state=&proposalStatus=&pageNo=0&pageSize=200000",
                    help="query string for advanceSearchData")
    ap.add_argument("--from", dest="src", help="fetch: use a saved advanceSearchData JSON dump (.json or .json.gz) instead")
    ap.add_argument("--field", action="append", default=[], metavar="ROLE=KEY",
                    help="override a field, e.g. --field name=proponentName (roles: " + ", ".join(FIELDS) + ")")
    args = ap.parse_args()
    {"fetch": fetch, "inspect": inspect, "match": match}[args.cmd](args)


if __name__ == "__main__":
    main()
