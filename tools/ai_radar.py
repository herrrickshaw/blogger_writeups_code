#!/usr/bin/env python3
"""Find new AI repositories gaining traction on GitHub, for the weekly AI Tracker.

    python3 tools/ai_radar.py                      # last 60 days, ranked by velocity
    python3 tools/ai_radar.py --days 30 --min-stars 1000
    python3 tools/ai_radar.py --json radar.json    # machine-readable
    python3 tools/ai_radar.py --md radar.md        # paste-ready edition brief

WHAT "COMING UP" MEANS HERE
    Not "most stars" — that ranks the same established projects every week and
    the tracker already knows about them. This ranks by **stars per day since
    the repository was created**, which surfaces a three-week-old project pulling
    1,200 stars a day above a two-year-old one sitting on 40,000.

    Age normalisation is the whole point. A repo created inside the window and
    already carrying five figures is the signal; total stars alone is a
    popularity list, not a radar.

WHY SEVERAL QUERIES
    GitHub search matches topics and text, not meaning. "agent", "llm", "mcp"
    and topic:ai each return a different slice and they overlap only partly, so
    the tool runs a set and dedupes by full_name. Missing a query means missing
    a category — the mcp query alone surfaces tooling the topic:ai query never
    returns.

HONEST LIMITS, WHICH THE EDITION SHOULD REPEAT
    A star is a bookmark. It measures attention, not adoption, not revenue, and
    it can be bought. Creation date is not launch date: a project may be
    developed privately for months and made public on day one with an audience
    already waiting, which inflates stars-per-day. And GitHub search is not a
    census — it ranks what it indexes, so absence here is not evidence of
    absence.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Each query is a different slice of the same space. Keep them broad: the
# ranking does the filtering, not the query.
QUERIES = [
    "topic:ai", "topic:llm", "topic:agents", "topic:mcp", "topic:rag",
    "agent", "llm", "mcp", "coding agent", "inference", "ai tool",
]

# Repos already in the tracker. Discovery should surface what is NOT known.
TRACKED = {
    "graphify-labs/graphify", "deusdata/codebase-memory-mcp", "xai-org/grok-build",
    "iofficeai/officecli", "langchain-ai/openwiki", "usestrix/strix",
    "hkuds/vibe-trading", "justvugg/colibri", "madslorentzen/ai-job-search",
    "diegosouzapw/omniroute", "nutlope/hallmark",
}


def gh_search(q, per_page=30):
    out = subprocess.run(
        ["gh", "api", "-X", "GET", "search/repositories",
         "-f", f"q={q}", "-f", "sort=stars", "-f", "order=desc",
         "-f", f"per_page={per_page}"],
        capture_output=True, text=True)
    if out.returncode:
        print(f"  ! query failed: {q}\n    {out.stderr.strip()[:160]}", file=sys.stderr)
        return []
    try:
        return json.loads(out.stdout).get("items", [])
    except json.JSONDecodeError:
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60,
                    help="only repositories created within this many days")
    ap.add_argument("--min-stars", type=int, default=1000)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--json", metavar="PATH")
    ap.add_argument("--md", metavar="PATH")
    ap.add_argument("--include-tracked", action="store_true")
    args = ap.parse_args()

    since = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    today = dt.date.today()
    found = {}
    for term in QUERIES:
        q = f"{term} created:>={since} stars:>{args.min_stars}"
        for it in gh_search(q):
            fn = it["full_name"]
            if fn.lower() in TRACKED and not args.include_tracked:
                continue
            created = it["created_at"][:10]
            age = max((today - dt.date.fromisoformat(created)).days, 1)
            found[fn] = {
                "repo": fn,
                "stars": it["stargazers_count"],
                "created": created,
                "age_days": age,
                "stars_per_day": round(it["stargazers_count"] / age, 1),
                "pushed": it["pushed_at"][:10],
                "language": it.get("language") or "",
                "description": (it.get("description") or "").strip(),
                "url": it["html_url"],
                "matched": found.get(fn, {}).get("matched", []) + [term],
            }
    rows = sorted(found.values(), key=lambda r: -r["stars_per_day"])[:args.top]

    print(f"AI radar — repositories created since {since}, at least "
          f"{args.min_stars:,} stars\n"
          f"{len(found)} distinct candidates from {len(QUERIES)} queries; "
          f"showing top {len(rows)} by stars/day\n")
    print(f"{'stars/day':>10} {'stars':>8} {'age':>5}  {'created':10}  repo")
    for r in rows:
        print(f"{r['stars_per_day']:>10,.1f} {r['stars']:>8,} {r['age_days']:>4}d  "
              f"{r['created']}  {r['repo']}")
        if r["description"]:
            print(f"{'':>27}{r['description'][:96]}")

    if args.json:
        Path(args.json).write_text(json.dumps(rows, indent=1), encoding="utf-8")
        print(f"\nwrote {args.json}")
    if args.md:
        L = [f"# AI radar — {today.isoformat()}", "",
             f"Repositories created since **{since}** with at least "
             f"{args.min_stars:,} stars, ranked by stars per day since creation. "
             f"{len(found)} candidates from {len(QUERIES)} GitHub search queries, "
             "deduplicated; repositories already in the tracker are excluded.", "",
             "| Repo | Stars | Age, days | Stars/day | Created | What it is |",
             "|---|---|---|---|---|---|"]
        for r in rows:
            d = r["description"].replace("|", "\\|")[:110]
            L.append(f"| [{r['repo']}]({r['url']}) | {r['stars']:,} | {r['age_days']} "
                     f"| {r['stars_per_day']:,.1f} | {r['created']} | {d} |")
        L += ["", "**Before publishing any of these:** confirm the repository is what its "
              "description claims, check whether the star curve looks organic, and note "
              "that creation date is not launch date — a project developed privately and "
              "opened with an audience already waiting will show an inflated stars/day.", ""]
        Path(args.md).write_text("\n".join(L), encoding="utf-8")
        print(f"wrote {args.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
