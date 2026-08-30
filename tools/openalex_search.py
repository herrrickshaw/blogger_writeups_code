#!/usr/bin/env python3
"""Source-checking helper: query OpenAlex (free, no key required) for existing
coverage of a topic before or while drafting a post -- the "has anyone else
already written this" check.

Usage:
    python3 tools/openalex_search.py "ajvar import substitution India"
    python3 tools/openalex_search.py "chemical import substitution HSN" -n 10
"""
import argparse, json, urllib.parse, urllib.request

API = "https://api.openalex.org/works"
CONTACT_EMAIL = "umashankartd1991@gmail.com"  # OpenAlex "polite pool" -- faster, more reliable rate limits


def search(query, limit=5):
    params = {
        "search": query,
        "per-page": limit,
        "sort": "relevance_score:desc",
        "mailto": CONTACT_EMAIL,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.load(resp)
    return data.get("results", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-n", "--limit", type=int, default=5)
    args = ap.parse_args()

    results = search(args.query, args.limit)
    if not results:
        print("No related works found on OpenAlex for this query.")
        return
    for r in results:
        title = r.get("display_name", "(untitled)")
        year = r.get("publication_year", "?")
        cited = r.get("cited_by_count", 0)
        oa = r.get("open_access", {}).get("is_oa")
        doi = r.get("doi", "")
        loc = r.get("primary_location") or {}
        src = (loc.get("source") or {}).get("display_name", "")
        print(f"- {title} ({year}) -- {src or 'unknown venue'}, cited {cited}x{' [OA]' if oa else ''}")
        if doi:
            print(f"  {doi}")


if __name__ == "__main__":
    main()
