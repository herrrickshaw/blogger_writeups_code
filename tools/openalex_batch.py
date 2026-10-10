#!/usr/bin/env python3
"""Run a list of literature queries against OpenAlex and write one markdown file.

The API key is read from the environment and is never written anywhere:

    export OPENALEX_API_KEY=...            # your key, in your shell only
    python3 tools/openalex_batch.py out/research/limonene_openalex_queries.txt \
        --out out/research/limonene_openalex_results.md -n 15

One query per line; blank lines and lines starting with # are skipped. Output has,
for each query, the top works by relevance with year, venue, citation count, DOI,
open-access flag and the abstract (rebuilt from OpenAlex's inverted index).
Nothing here is verified fact: it is a reading list. Check the paper itself.
"""
import argparse, json, os, sys, time, urllib.parse, urllib.request

API = "https://api.openalex.org/works"
FIELDS = ("display_name,publication_year,doi,cited_by_count,open_access,"
          "primary_location,abstract_inverted_index,type")


def abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def search(q, n, key):
    params = {"search": q, "per-page": n, "sort": "relevance_score:desc", "select": FIELDS}
    if key:
        params["api_key"] = key
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r).get("results", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("--out", required=True)
    ap.add_argument("-n", "--limit", type=int, default=15)
    ap.add_argument("--min-year", type=int, default=0)
    a = ap.parse_args()
    key = os.environ.get("OPENALEX_API_KEY", "")
    if not key:
        print("OPENALEX_API_KEY is not set; running without a key (lower limits).", file=sys.stderr)
    qs = [l.strip() for l in open(a.queries, encoding="utf-8") if l.strip() and not l.startswith("#")]
    out = ["# OpenAlex results", "", f"Queries: {len(qs)}. Reading list only, not verified.", ""]
    for q in qs:
        out += [f"## {q}", ""]
        try:
            res = search(q, a.limit, key)
        except Exception as e:           # report and carry on
            out += [f"_Query failed: {e}_", ""]
            continue
        for r in res:
            y = r.get("publication_year") or 0
            if y < a.min_year:
                continue
            loc = r.get("primary_location") or {}
            venue = (loc.get("source") or {}).get("display_name") or "unknown venue"
            oa = " [OA]" if (r.get("open_access") or {}).get("is_oa") else ""
            out.append(f"- **{r.get('display_name')}** ({y}), {venue}, cited {r.get('cited_by_count', 0)}x{oa}  ")
            if r.get("doi"):
                out.append(f"  {r['doi']}  ")
            ab = abstract(r.get("abstract_inverted_index"))
            if ab:
                out.append(f"  > {ab[:700]}{'...' if len(ab) > 700 else ''}")
        out.append("")
        time.sleep(0.2)
    open(a.out, "w", encoding="utf-8").write("\n".join(out))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
