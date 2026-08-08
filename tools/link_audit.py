#!/usr/bin/env python3
"""Check every link in the archived posts and the theme, and report the dead ones.

    python3 tools/link_audit.py              # full check, human-readable
    python3 tools/link_audit.py --internal   # blogspot + relative links only (fast)
    python3 tools/link_audit.py --json out.json

Exit codes
    0  nothing broken
    1  dead links found
    2  could not run the check at all

Three classes of link, checked differently:

  relative  Always broken. A post body lives at blogspot.com/YYYY/MM/slug.html, so
            "charts/foo.html" resolves under that path and cannot exist. These are
            leftovers from local report bundles and are reported without a request.

  internal  blogspot.com URLs. A 404 here usually means a burned slug: Blogger
            never releases a slug, so a republished post gets a suffix and the
            original address dies. Fix by repointing, or with a custom redirect
            in Blogger's Settings -> Errors and redirects.

  external  Everything else. Only 404 and 410 count as dead. A 403, 429, 999,
            timeout or DNS failure means we could not get an answer — the host is
            blocking scripted requests, throttling us, or unreachable from this
            network. Those are listed as UNVERIFIABLE and never fail the run.
            Where the check runs from changes the answer: many Indian government
            portals refuse foreign datacentre IPs outright, so the same audit
            reports 391/399 OK from India and 156/399 from a GitHub runner.
            Open one in a browser before "fixing" it.
"""
import argparse
import collections
import concurrent.futures as cf
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
BLOG_HOST = "masaladeutsch.blogspot.com"
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "en-IN,en;q=0.9",
}
# Only these mean the target is actually gone. Everything else non-200 means we
# could not get an answer, which is a different claim.
#
# Learned from running this in CI: from a GitHub runner in a US datacentre, 243
# of 399 external links came back non-200 — 99 URLError, 89x 429, 55x 403 — and
# not one was a 404. The same links returned 391/399 OK from an Indian
# connection. Many Indian government portals simply refuse foreign datacentre
# IPs. A checker that calls those "dead" would have the maintainer chasing 243
# phantom failures every week.
DEAD_CODES = {404, 410}
HREF = re.compile(r'href=["\']([^"\'>]+)["\']')
SKIP_PREFIX = ("mailto:", "#", "javascript:", "data:", "tel:")


def collect():
    """url -> set of files it appears in."""
    links = collections.defaultdict(set)
    files = sorted(glob.glob(str(ROOT / "posts" / "*.html")))
    theme = ROOT / "theme" / "theme.xml"
    if theme.exists():
        files.append(str(theme))
    if not files:
        print("no posts/ or theme/ to audit", file=sys.stderr)
        sys.exit(2)
    for f in files:
        s = Path(f).read_text(encoding="utf-8", errors="replace")
        for m in HREF.finditer(s):
            u = m.group(1).strip()
            if u.startswith(SKIP_PREFIX):
                continue
            # "${d.src}" and friends are template literals inside chart JS, not links.
            if "${" in u or "{{" in u:
                continue
            links[u].add(os.path.basename(f))
    return links


def classify(u):
    if not u.startswith("http"):
        return "relative"
    return "internal" if BLOG_HOST in u else "external"


def check(u, timeout=30):
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(u, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            # A transient throttle deserves one retry; a 404 does not.
            if e.code in (429, 503) and attempt == 1:
                time.sleep(4)
                continue
            return e.code, None
        except Exception as e:  # DNS, TLS, timeout
            if attempt == 1:
                time.sleep(2)
                continue
            return f"ERR {type(e).__name__}", None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--internal", action="store_true",
                    help="skip external links (fast; use when only the blog changed)")
    ap.add_argument("--json", metavar="PATH", help="write the full result set here")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--timeout", type=int, default=30,
                    help="per-request seconds; lower in CI where many hosts hang")
    args = ap.parse_args()

    links = collect()
    buckets = collections.defaultdict(list)
    for u in links:
        buckets[classify(u)].append(u)

    dead, unverifiable, results = [], [], {}

    # Relative links need no request — they cannot resolve under a post path.
    for u in sorted(buckets["relative"]):
        dead.append((u, "relative", "cannot resolve under a blogspot post path"))
        results[u] = "relative"

    todo = sorted(buckets["internal"])
    if not args.internal:
        todo += sorted(buckets["external"])

    with cf.ThreadPoolExecutor(args.workers) as ex:
        for u, (code, final) in zip(todo, ex.map(lambda x: check(x, args.timeout), todo)):
            results[u] = code
            if code == 200:
                continue
            if code in DEAD_CODES:
                dead.append((u, classify(u), code))
            else:
                # 403 / 429 / 999 / timeouts / DNS failures: blocked, throttled
                # or unreachable from here. Says nothing about the link.
                unverifiable.append((u, code))

    checked = len(todo) + len(buckets["relative"])
    print(f"links found {len(links)}  |  checked {checked}  "
          f"|  relative {len(buckets['relative'])}  internal {len(buckets['internal'])}  "
          f"external {len(buckets['external'])}"
          + ("  (external skipped)" if args.internal else ""))
    print(f"DEAD {len(dead)}  |  unverifiable {len(unverifiable)}\n")

    if dead:
        print("DEAD LINKS")
        for u, kind, why in sorted(dead, key=lambda x: (x[1], str(x[0]))):
            print(f"  [{kind}/{why}] {u}")
            for src in sorted(links[u]):
                print(f"        in {src}")
        print()
    if unverifiable:
        print("UNVERIFIABLE (host blocks scripted requests — check in a browser "
              "before changing anything)")
        for u, code in sorted(unverifiable):
            print(f"  [{code}] {u}")
        print()

    if args.json:
        Path(args.json).write_text(json.dumps({
            "results": {k: str(v) for k, v in results.items()},
            "dead": [{"url": u, "kind": k, "why": str(w),
                      "sources": sorted(links[u])} for u, k, w in dead],
            "unverifiable": [{"url": u, "code": str(c)} for u, c in unverifiable],
        }, indent=1), encoding="utf-8")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
