#!/usr/bin/env python3
"""Index coverage for VertiStrat, per URL, from the Search Console URL Inspection API.

The Search Console "Pages" report has no API, but URL Inspection does: for each
URL it returns Google's verdict, coverage state ("Crawled - currently not
indexed", "Discovered - currently not indexed", "Duplicate, Google chose
different canonical than user", ...), robots/fetch state, last crawl and both
canonicals. This tool inspects every post in meta/manifest.json (plus the
homepage), caches results so a run can resume, reads the sitemaps report, and
writes a summary grouped by reason.

Auth: same service account as tools/gsc_report.py (webmasters.readonly is
enough for URL Inspection and the sitemaps list). Quota: 2,000 inspections a
day and 600 a minute per property, so 500-odd posts fit in one run.

    python3 tools/gsc_index.py                       # inspect everything not inspected today
    python3 tools/gsc_index.py --limit 50            # a small first run
    python3 tools/gsc_index.py --only-not-indexed    # re-inspect only URLs last seen not indexed
    python3 tools/gsc_index.py --summary             # rebuild the summary from the cache only

Outputs: out/gsc_index/inspect.jsonl (append-only cache, one JSON per inspection)
         out/gsc_index/SUMMARY.md, out/gsc_index/not_indexed.csv, out/gsc_index/sitemaps.json
Report-only: never touches the blog.
"""
import argparse, csv, collections, datetime as dt, json, pathlib, sys, time, urllib.error, urllib.parse, urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
DEFAULT_SITE = "https://masaladeutsch.blogspot.com/"

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "gsc_index"
CACHE = OUT / "inspect.jsonl"
INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"


def call(token, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if body is not None else "GET",
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def load_cache():
    rows = {}
    if CACHE.exists():
        for line in CACHE.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                rows[r["url"]] = r          # last inspection wins
    return rows


def urls_from_manifest(site):
    m = json.loads((ROOT / "meta" / "manifest.json").read_text())
    posts = m["posts"].values() if isinstance(m["posts"], dict) else m["posts"]
    urls = [site] + sorted(p["url"] for p in posts if p.get("url"))
    return list(dict.fromkeys(urls))


def flatten(url, res):
    ir = res.get("inspectionResult", {})
    ix = ir.get("indexStatusResult", {})
    return {"url": url, "checked": dt.datetime.now().isoformat(timespec="seconds"),
            "verdict": ix.get("verdict"), "coverage": ix.get("coverageState"),
            "robots": ix.get("robotsTxtState"), "indexing": ix.get("indexingState"),
            "fetch": ix.get("pageFetchState"), "last_crawl": ix.get("lastCrawlTime"),
            "crawled_as": ix.get("crawledAs"), "google_canonical": ix.get("googleCanonical"),
            "user_canonical": ix.get("userCanonical"), "referring": (ix.get("referringUrls") or [])[:3],
            "sitemaps": ix.get("sitemap") or [],
            "mobile": (ir.get("mobileUsabilityResult") or {}).get("verdict"),
            "rich": (ir.get("richResultsResult") or {}).get("verdict")}


def inspect(args, site):
    OUT.mkdir(parents=True, exist_ok=True)
    cache = load_cache()
    today = dt.date.today().isoformat()
    urls = urls_from_manifest(site)
    if args.only_not_indexed:
        urls = [u for u in urls if cache.get(u, {}).get("verdict") != "PASS"]
    todo = [u for u in urls if not cache.get(u, {}).get("checked", "").startswith(today)]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(urls)} URLs; {len(todo)} to inspect now")
    from gsc_report import get_access_token  # needs `cryptography`; only the API path imports it
    token, t0, n = get_access_token(), time.time(), 0
    with CACHE.open("a") as fh:
        for u in todo:
            if time.time() - t0 > 3000:
                token, t0 = get_access_token(), time.time()
            try:
                res = call(token, INSPECT, {"inspectionUrl": u, "siteUrl": site, "languageCode": "en-IN"})
            except urllib.error.HTTPError as e:
                msg = e.read().decode()[:200]
                if e.code == 429 or "quota" in msg.lower():
                    print(f"quota reached after {n}: {msg}"); break
                print(f"  {e.code} {u}: {msg}"); continue
            row = flatten(u, res)
            fh.write(json.dumps(row) + "\n"); fh.flush()
            n += 1
            if n % 25 == 0:
                print(f"  {n} inspected")
            time.sleep(0.15)
    print(f"inspected {n}")
    try:
        sm = call(token, f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(site, safe='')}/sitemaps")
        (OUT / "sitemaps.json").write_text(json.dumps(sm, indent=1))
    except urllib.error.HTTPError as e:
        print(f"sitemaps: {e.code} {e.read().decode()[:200]}")


def summary(site):
    cache = load_cache()
    rows = [r for r in cache.values() if r["url"] in set(urls_from_manifest(site))]
    by = collections.Counter((r.get("verdict") or "?", r.get("coverage") or "?") for r in rows)
    lines = [f"# Index coverage, {dt.date.today().isoformat()}", "",
             f"{len(rows)} URLs inspected (posts in meta/manifest.json plus the homepage).", "",
             "| Verdict | Coverage state | URLs |", "|---|---|---|"]
    lines += [f"| {v} | {c} | {n} |" for (v, c), n in by.most_common()]
    canon = [r for r in rows if r.get("google_canonical") and r.get("user_canonical") and r["google_canonical"] != r["user_canonical"]]
    lines += ["", f"Google chose a different canonical for {len(canon)} URL(s)."]
    lines += [f"- {r['url']} -> {r['google_canonical']}" for r in canon[:40]]
    nosm = [r for r in rows if r.get("verdict") != "PASS" and not r.get("sitemaps")]
    lines += ["", f"Not indexed and not seen in any sitemap: {len(nosm)}"]
    never = [r for r in rows if not r.get("last_crawl")]
    lines += [f"Never crawled: {len(never)}"]
    blocked = collections.Counter((r.get("robots"), r.get("indexing"), r.get("fetch")) for r in rows if r.get("verdict") != "PASS")
    lines += ["", "Not-indexed URLs by (robots, indexing, fetch):"] + [f"- {k}: {n}" for k, n in blocked.most_common()]
    sm = OUT / "sitemaps.json"
    if sm.exists():
        lines += ["", "## Sitemaps", ""]
        for s in json.loads(sm.read_text()).get("sitemap", []):
            cnt = "; ".join(f"{c.get('type')}: {c.get('submitted')} submitted, {c.get('indexed', '?')} indexed" for c in s.get("contents", []))
            lines.append(f"- {s.get('path')} | last read {s.get('lastDownloaded')} | errors {s.get('errors')} warnings {s.get('warnings')} | {cnt}")
    (OUT / "SUMMARY.md").write_text("\n".join(lines) + "\n")
    with (OUT / "not_indexed.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["url", "verdict", "coverage", "last_crawl", "google_canonical", "robots", "indexing", "fetch"])
        for r in sorted(rows, key=lambda r: (r.get("coverage") or "", r["url"])):
            if r.get("verdict") != "PASS":
                w.writerow([r["url"], r.get("verdict"), r.get("coverage"), r.get("last_crawl"), r.get("google_canonical"),
                            r.get("robots"), r.get("indexing"), r.get("fetch")])
    print("\n".join(lines[:20]))
    print(f"\nwrote {OUT}/SUMMARY.md and not_indexed.csv")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--site", default=DEFAULT_SITE)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only-not-indexed", action="store_true")
    ap.add_argument("--summary", action="store_true", help="rebuild the summary from the cache; no API calls")
    a = ap.parse_args()
    try:
        if not a.summary:
            inspect(a, a.site)
    except KeyboardInterrupt:
        print("interrupted; writing the summary from what was inspected")
    except Exception as e:  # keep the cache usable and still write a summary
        print(f"stopped early: {type(e).__name__}: {e}")
    summary(a.site)


if __name__ == "__main__":
    main()
