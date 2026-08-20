#!/usr/bin/env python3
"""Source-checking helper #2: query Google Scholar (via `scholarly`) for
existing coverage of a topic. Complements tools/openalex_search.py -- Scholar's
ranking surfaces different (often more recent/popular) results than OpenAlex's
citation-graph ranking, so worth checking both before publishing on a topic.

Routed through rotating free proxies (scholarly's ProxyGenerator.FreeProxies)
since Google blocks unproxied scrapers outright. Three real bugs had to be
worked around: httpx 0.28 removed Client(proxies=...) (pinned httpx<0.28 in
requirements-plagcheck.txt), and scholarly's own _fp_coroutine calls
FreeProxy.get_proxy_list() two different ways -- one correct, one missing the
required `repeat` arg on every free-proxy version on PyPI, and it's the one
that fires once the first proxy batch is exhausted, i.e. exactly when
rotation is needed. Monkeypatched below rather than pinned around, since no
free-proxy version actually avoids it. Even with all that fixed, Scholar-via-
free-proxy is inherently flaky (most public proxies are dead or already
blocked) -- this retries a few times, then gives up and tells you to use
openalex_search.py, which has no such problem.

Needs the dedicated venv: ~/.venvs/masaladeutsch-plagcheck/bin/python3

Usage:
    ~/.venvs/masaladeutsch-plagcheck/bin/python3 tools/scholarly_search.py "ajvar import substitution India"
    ~/.venvs/masaladeutsch-plagcheck/bin/python3 tools/scholarly_search.py "chemical import substitution HSN" -n 5
"""
import argparse, sys
from scholarly import scholarly, ProxyGenerator

# Monkeypatch: scholarly._proxy_generator.ProxyGenerator._fp_coroutine has two
# call sites for FreeProxy.get_proxy_list() -- one passes repeat=False (correct
# for free-proxy>=1.1.0), the other (used only once the first proxy batch is
# exhausted, i.e. exactly when rotation is needed most) calls it with no args
# at all and crashes with TypeError on every free-proxy version currently on
# PyPI. Giving get_proxy_list a default fixes both call sites without needing
# to patch scholarly itself.
from fp.fp import FreeProxy
_orig_get_proxy_list = FreeProxy.get_proxy_list
def _get_proxy_list_patched(self, repeat=False):
    return _orig_get_proxy_list(self, repeat)
FreeProxy.get_proxy_list = _get_proxy_list_patched

MAX_ATTEMPTS = 3


def setup_proxy():
    pg = ProxyGenerator()
    if not pg.FreeProxies():
        return None
    scholarly.use_proxy(pg)
    return pg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-n", "--limit", type=int, default=5)
    args = ap.parse_args()

    pg = setup_proxy()
    if pg is None:
        print("Could not initialize any free proxy -- try again shortly.", file=sys.stderr)
        sys.exit(1)

    results = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            results = scholarly.search_pubs(args.query)
            break
        except Exception as e:
            print(f"attempt {attempt + 1}/{MAX_ATTEMPTS} failed ({type(e).__name__}), rotating proxy...", file=sys.stderr)
            setup_proxy()

    if results is None:
        print(
            f"Google Scholar unreachable after {MAX_ATTEMPTS} proxy rotations -- free public "
            "proxies are inherently unreliable for this (most are dead or already "
            "Scholar-blocked). Use tools/openalex_search.py instead, which works "
            "without a proxy. A paid proxy service (scholarly's ScraperAPI/Luminati "
            "backends) would be more reliable but needs its own account/API key.",
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
