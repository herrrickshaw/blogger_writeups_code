#!/usr/bin/env python3
"""Source-checking helper #2: query Google Scholar (via `scholarly`) for
existing coverage of a topic. Complements tools/openalex_search.py -- Scholar's
ranking surfaces different (often more recent/popular) results than OpenAlex's
citation-graph ranking, so worth checking both before publishing on a topic.

Needs the dedicated venv: ~/.venvs/masaladeutsch-plagcheck/bin/python3

Usage:
    ~/.venvs/masaladeutsch-plagcheck/bin/python3 tools/scholarly_search.py "ajvar import substitution India"
    ~/.venvs/masaladeutsch-plagcheck/bin/python3 tools/scholarly_search.py "chemical import substitution HSN" -n 5
"""
import argparse, sys
from scholarly import scholarly
from scholarly._proxy_generator import MaxTriesExceededException


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-n", "--limit", type=int, default=5)
    args = ap.parse_args()

    try:
        results = scholarly.search_pubs(args.query)
    except MaxTriesExceededException:
        print(
            "Google Scholar blocked the request (no proxy configured -- this is "
            "scholarly's well-known out-of-the-box limitation, not a bug here). "
            "Use tools/openalex_search.py instead, which works without a proxy; "
            "scholarly.use_proxy() with a working proxy service would fix this "
            "but adds a real external dependency, so it isn't wired in by default.",
            file=sys.stderr,
        )
        sys.exit(1)
    count = 0
    for pub in results:
        if count >= args.limit:
            break
        bib = pub.get("bib", {})
        title = bib.get("title", "(untitled)")
        year = bib.get("pub_year", "?")
        venue = bib.get("venue", "")
        cited = pub.get("num_citations", 0)
        url = pub.get("pub_url", "")
        print(f"- {title} ({year}) -- {venue or 'unknown venue'}, cited {cited}x")
        if url:
            print(f"  {url}")
        count += 1
    if count == 0:
        print("No related works found on Google Scholar for this query.")


if __name__ == "__main__":
    main()
