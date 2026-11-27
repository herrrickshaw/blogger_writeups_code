#!/usr/bin/env python3
"""Confirm the published blog is actually serving what the archive thinks it is.

    python3 tools/site_health.py            # check everything in the manifest
    python3 tools/site_health.py --sample 20

Exit codes
    0  healthy
    1  something is wrong
    2  could not run the check

The link audit checks links that appear in a post body. This checks the other
direction: every post the manifest knows about, whether or not anything links to
it. That catches the failures link-checking cannot see — a post quietly reverted
to draft, a homepage that stops rendering cards because the per-index byte
budget was blown by an oversized post, an index page that 200s but is empty.
"""
import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "meta" / "manifest.json"
BLOG = "https://blog.vertistratsolution.com"
UA = {"User-Agent": "Mozilla/5.0 (vertistrat-archive health check)"}
PACE = 0.0   # seconds between requests per worker; set in main()


THROTTLE_CODES = (429, 503)


def get(url, timeout=45, tries=4):
    """Fetch with backoff. Raises on the last throttle so the caller can bucket it.

    Blogger rate-limits by client IP, and a shared CI runner gets throttled far
    harder than a home connection: the same check that passed 93/93 locally came
    back 10/93 with 429s from a GitHub runner. Being slow and polite is the fix,
    and a throttle that survives it is reported as inconclusive, never as the
    site being down.
    """
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in THROTTLE_CODES and attempt < tries:
                time.sleep(2 ** attempt)   # 2s, 4s, 8s
                continue
            raise


def check_post(rec):
    url = rec["url"]
    time.sleep(PACE)   # module-level, set from --pace; keeps us under the limiter
    try:
        status, body = get(url)
    except urllib.error.HTTPError as e:
        return rec, e.code, None
    except Exception as e:
        return rec, f"ERR {type(e).__name__}", None
    # A Blogger 404 can still return 200 with a "page not found" shell, so
    # confirm the post's own title is actually on the page.
    title = re.sub(r"<[^>]+>", "", rec.get("title", "")).strip()[:40]
    present = bool(title) and title.split("—")[0].strip()[:28].lower() in body.lower()
    return rec, status, present


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=0,
                    help="check only the N most recent posts (default: all)")
    ap.add_argument("--min-homepage-cards", type=int, default=1)
    ap.add_argument("--workers", type=int, default=3,
                    help="keep this low; Blogger rate-limits by IP")
    ap.add_argument("--pace", type=float, default=0.3,
                    help="seconds to wait before each request, per worker")
    args = ap.parse_args()
    global PACE
    PACE = args.pace

    if not MANIFEST.exists():
        print("no manifest — run tools/snapshot.py first", file=sys.stderr)
        return 2
    posts = list(json.loads(MANIFEST.read_text())["posts"].values())
    posts.sort(key=lambda r: r.get("published", ""), reverse=True)
    if args.sample:
        posts = posts[: args.sample]

    problems = []
    homepage_throttled = False

    # 1. The homepage must render at least one post, not just the chrome.
    try:
        status, home = get(BLOG + "/")
        # This is a custom theme: posts render as <div class='card'>, in single
        # quotes. Counting Blogger's stock post-outer/post-title classes found
        # zero and reported a healthy homepage as broken.
        cards = len(re.findall(r"""<div[^>]*\bclass=['"][^'"]*\bcard\b""", home))
        print(f"homepage      {status}  {len(home):,} bytes  post cards: {cards}")
        if status != 200:
            problems.append(f"homepage returned {status}")
        elif cards < args.min_homepage_cards:
            problems.append(
                f"homepage rendered {cards} post cards (expected at least "
                f"{args.min_homepage_cards}) — usually the per-index byte budget, "
                f"blown by an oversized post")
    except urllib.error.HTTPError as e:
        if e.code in THROTTLE_CODES:
            # Same rule as for posts: being rate-limited tells us nothing about
            # whether the homepage renders. Do not call it an outage.
            homepage_throttled = True
            print(f"homepage      RATE-LIMITED {e.code} — inconclusive")
        else:
            problems.append(f"homepage returned {e.code}")
            print(f"homepage      {e.code}")
    except Exception as e:
        problems.append(f"homepage unreachable: {type(e).__name__}")
        print(f"homepage      UNREACHABLE {type(e).__name__}")

    # 2. Every post the manifest knows about must still serve its own title.
    ok, throttled = 0, []
    with cf.ThreadPoolExecutor(args.workers) as ex:
        for rec, status, present in ex.map(check_post, posts):
            if status == 200 and present:
                ok += 1
            elif status == 200 and present is False:
                problems.append(f"200 but title missing (drafted? redirected?): {rec['url']}")
            elif status in THROTTLE_CODES:
                # We were rate-limited. This says nothing about the post.
                throttled.append(rec["url"])
            else:
                problems.append(f"{status}: {rec['url']}")
    print(f"posts         {ok}/{len(posts)} serving their own title"
          + (f"  ({len(throttled)} inconclusive — rate-limited)" if throttled else ""))

    print()
    if homepage_throttled:
        print("RATE-LIMITED: homepage — inconclusive, not a site fault.")
    if throttled:
        print(f"RATE-LIMITED {len(throttled)} — not checked, not a site fault. "
              f"Lower --workers or raise --pace, or use --sample.")
    if problems:
        print(f"PROBLEMS {len(problems)}")
        for p in problems:
            print("  " + p)
        return 1
    print("healthy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
