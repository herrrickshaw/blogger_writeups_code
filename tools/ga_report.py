#!/usr/bin/env python3
"""GA4 Data API report for VertiStrat (property 548678807): pageviews and
active-user counts, broken down by country/city, over a date range.

Also a per-city traffic-quality drill-down (2026-09-21): a raw views/user
ratio flagged Coimbatore/Irugur/Salem as outliers in the 2026-09-10 report
(some 25-35 views per user, vs ~1.3 everywhere else), but that ratio alone
can't tell a handful of very engaged readers apart from a script -- so the
top-by-views cities also get a device/browser mix and average engagement
time per session. A script tends to show one device/browser combo and
near-zero engagement time; real readers don't, whatever their views/user
ratio. See city_quality_to_table().

Auth: service-account JWT bearer flow (RS256), signed with `cryptography` --
no google-api-python-client / google-analytics-data dependency, consistent
with this repo's minimal-dependency style (see tools/blogger_api.py).

Report-only: reads GA4 data, prints/writes a summary. Never touches the blog.

    python3 tools/ga_report.py                    # last 28 days, prints to stdout
    python3 tools/ga_report.py --days 7
    python3 tools/ga_report.py --days 90 --out out/ga_report.md
    python3 tools/ga_report.py --city-quality-n 0  # skip the drill-down (2 fewer API calls)
    python3 tools/ga_report.py --days 7 --owner-cities "Madurai,Mumbai,Hyderabad"

Likely-human section (2026-10-02): splits cities into bot-like (no engaged
session in the range) and human-like, and ranks pages by engaged sessions,
optionally leaving out your own cities. See HUMAN_NOTE.
"""
import argparse, base64, glob, json, re, time, urllib.request, urllib.parse, pathlib

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

SECRETS = pathlib.Path.home() / ".config" / "market-secrets"
SA_FILE = SECRETS / "ga_service_account.json"
PROPERTY_ID = "548678807"
SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
DATA_API = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"
ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE_PATH_RE = re.compile(r"^/\d{4}/\d{2}/([^/]+)\.html$")


def _b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def get_access_token():
    sa = json.loads(SA_FILE.read_text())
    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT"}
    claims = {
        "iss": sa["client_email"],
        "scope": SCOPE,
        "aud": sa["token_uri"],
        "iat": now,
        "exp": now + 3600,
    }
    signing_input = f"{_b64url(json.dumps(header).encode())}.{_b64url(json.dumps(claims).encode())}"
    private_key = serialization.load_pem_private_key(sa["private_key"].encode(), password=None)
    signature = private_key.sign(signing_input.encode(), padding.PKCS1v15(), hashes.SHA256())
    jwt = f"{signing_input}.{_b64url(signature)}"

    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt,
    }).encode()
    req = urllib.request.Request(sa["token_uri"], data=data, method="POST")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())["access_token"]


def run_report(access_token, body):
    req = urllib.request.Request(
        DATA_API, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GA4 API error {e.code}: {e.read().decode()}") from e


def canonical_path_map():
    """slug -> canonical URL path, from this archive's local post metadata.
    Blogger permalinks are fixed at post-creation time, but if a post's
    `published` date is later edited (as tools/blogger_api.py deliberately
    does, to avoid Blogger silently re-dating a post on every update), the
    URL's year/month prefix can end up not matching the published date --
    and Blogger 301-redirects the "naturally guessed" old-dated URL to the
    real permalink. GA4 tracks pagePath as whatever was actually live at
    the time, so the same post's pageviews end up split across both paths
    in the raw report even though there's only ever been one live URL at
    any given moment (verified: the old path 301s, it's not a duplicate
    post). This map lets the top-pages report merge those back together."""
    m = {}
    for f in glob.glob(str(ROOT / "meta" / "*.json")):
        try:
            meta = json.load(open(f))
        except Exception:
            continue
        slug = meta.get("slug")
        url = meta.get("url")
        if not slug or not url:
            continue
        m[slug] = urllib.parse.urlparse(url).path
    return m


def merge_page_aliases(report):
    """Collapse rows whose pagePath resolves to the same post slug (see
    canonical_path_map) into one row keyed by that post's current canonical
    path, summing the metrics and recording which alias paths were folded
    in. Rows with no slug match (/, /search, etc.) pass through unchanged."""
    canon = canonical_path_map()
    merged = {}   # canonical_path -> {"views": int, "users": int, "aliases": {path: (views, users)}}
    order = []
    for row in report.get("rows", []):
        path = row["dimensionValues"][0]["value"]
        views = int(row["metricValues"][0]["value"])
        users = int(row["metricValues"][1]["value"])
        m = PAGE_PATH_RE.match(path)
        slug = m.group(1) if m else None
        key = canon.get(slug, path)
        if key not in merged:
            merged[key] = {"views": 0, "users": 0, "aliases": {}}
            order.append(key)
        merged[key]["views"] += views
        merged[key]["users"] += users
        if path != key:
            merged[key]["aliases"][path] = (views, users)
    order.sort(key=lambda k: -merged[k]["views"])
    return order, merged


def rows_to_table(report, dim_label, metric_labels):
    header = [dim_label] + metric_labels
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for row in report.get("rows", []):
        dims = [d["value"] for d in row.get("dimensionValues", [])]
        mets = [m["value"] for m in row.get("metricValues", [])]
        lines.append("| " + " | ".join(dims + mets) + " |")
    if not report.get("rows"):
        lines.append("| *(no data returned)* |" + " |" * len(metric_labels))
    return "\n".join(lines)


def in_list_filter(field, values):
    return {"filter": {"fieldName": field, "inListFilter": {"values": values}}}


def top_cities_by_views(by_city, n=12):
    """Cities worth a device/engagement drill-down: the highest page-view
    cities, not just highest-user cities -- an outsized views/user ratio
    (the actual bot-suspicion signal) can hide behind a modest user count,
    the way Coimbatore/Irugur/Salem did in the 2026-09-10 report."""
    rows = [
        (row["dimensionValues"][0]["value"], int(row["metricValues"][1]["value"]))
        for row in by_city.get("rows", [])
    ]
    rows.sort(key=lambda r: -r[1])
    return [name for name, _ in rows[:n] if name and name != "(not set)"]


def device_mix_by_city(token, date_range, cities):
    """city -> ["device/browser: views", ...], sorted by views, so a real
    distributed readership (several device/browser combos) is visually
    distinct from one combo accounting for nearly all of a city's views."""
    if not cities:
        return {}
    report = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "city"}, {"name": "deviceCategory"}, {"name": "browser"}],
        "metrics": [{"name": "activeUsers"}, {"name": "screenPageViews"}],
        "dimensionFilter": in_list_filter("city", cities),
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 300,
    })
    mix = {}
    for row in report.get("rows", []):
        city, device, browser = (d["value"] for d in row["dimensionValues"])
        users, views = (int(m["value"]) for m in row["metricValues"])
        mix.setdefault(city, []).append((f"{device}/{browser}", views, users))
    for city in mix:
        mix[city].sort(key=lambda t: -t[1])
    return mix


def engagement_by_city(token, date_range, cities):
    """city -> sessions/engagedSessions/avg-engagement-seconds/bounceRate.
    A city with many page views but near-zero average engagement time is a
    much stronger bot signal than the raw views/user ratio alone -- a script
    can rack up pageviews in milliseconds; a real reader cannot."""
    if not cities:
        return {}
    report = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "city"}],
        "metrics": [{"name": "sessions"}, {"name": "engagedSessions"},
                    {"name": "userEngagementDuration"}, {"name": "bounceRate"}],
        "dimensionFilter": in_list_filter("city", cities),
        "limit": 100,
    })
    eng = {}
    for row in report.get("rows", []):
        city = row["dimensionValues"][0]["value"]
        sessions, engaged, duration, bounce = (m["value"] for m in row["metricValues"])
        sessions, engaged, duration, bounce = int(sessions), int(engaged), float(duration), float(bounce)
        eng[city] = {
            "sessions": sessions,
            "engaged": engaged,
            "avg_engagement_s": (duration / sessions) if sessions else 0.0,
            "bounce_pct": bounce * 100,
        }
    return eng


def city_quality_to_table(cities, by_city_rows, mix, eng, top_combos=3):
    """One row per drill-down city: views, users, sessions, avg engagement
    time, bounce rate, and the top device/browser combos -- everything
    needed to eyeball 'real distributed readership' vs 'one script, one
    device, near-zero engagement time' without leaving this report."""
    views_users = {
        row["dimensionValues"][0]["value"]: (
            int(row["metricValues"][1]["value"]), int(row["metricValues"][0]["value"])
        )
        for row in by_city_rows
    }
    header = ("| City | Page views | Active users | Views/user | Sessions | "
              "Avg engagement | Bounce rate | Top device/browser combos |")
    sep = "|" + "---|" * 8
    lines = [header, sep]
    for city in cities:
        views, users = views_users.get(city, (0, 0))
        vpu = f"{views / users:.1f}" if users else "n/a"
        e = eng.get(city)
        sessions = e["sessions"] if e else "?"
        avg_eng = f"{e['avg_engagement_s']:.0f}s" if e else "?"
        bounce = f"{e['bounce_pct']:.0f}%" if e else "?"
        combos = mix.get(city, [])[:top_combos]
        combo_str = "; ".join(f"{c} ({v})" for c, v, _ in combos) or "n/a"
        if len(mix.get(city, [])) > top_combos:
            combo_str += f"; +{len(mix[city]) - top_combos} more"
        lines.append(f"| {city} | {views} | {users} | {vpu} | {sessions} | "
                      f"{avg_eng} | {bounce} | {combo_str} |")
    if not cities:
        lines.append("| *(no cities with recorded page views in this range)* |" + " |" * 7)
    return "\n".join(lines)


HUMAN_NOTE = (
    "Heuristic, not a bot filter. GA4 already drops crawlers on the IAB "
    "list; what gets through here is headless browsers from datacentre "
    "cities (one desktop/Chrome view, 0s engagement, 100% bounce -- see the "
    "drill-down above). Their signature is that they never produce an "
    "*engaged session* (GA4's definition: lasts over 10s, or has 2+ page "
    "views, or a key event). So: a city with zero engaged sessions in the "
    "range is counted as bot-like in full; any city with at least one "
    "engaged session is counted as human-like, and the engaged-session "
    "count -- not users or views -- is the best single number for real "
    "readers. Cities passed via --owner-cities (your own browsing, until "
    "GA4's internal-traffic filter is active) are reported separately and "
    "left out of the page table.")


def _metric_values(row):
    return [float(m["value"]) for m in row.get("metricValues", [])]


def city_engagement_rows(token, date_range):
    """Every city in the range with users, views, sessions, engaged sessions
    and total engagement seconds -- the raw material for the bot-like vs
    human-like split."""
    report = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "city"}],
        "metrics": [{"name": "activeUsers"}, {"name": "screenPageViews"},
                    {"name": "sessions"}, {"name": "engagedSessions"},
                    {"name": "userEngagementDuration"}],
        "limit": 1000,
    })
    rows = []
    for row in report.get("rows", []):
        users, views, sessions, engaged, duration = _metric_values(row)
        rows.append({"city": row["dimensionValues"][0]["value"],
                     "users": int(users), "views": int(views),
                     "sessions": int(sessions), "engaged": int(engaged),
                     "duration": duration})
    return rows


def classify_cities(rows, owner_cities=()):
    """Split city rows into owner / human-like / bot-like (see HUMAN_NOTE)."""
    owner = {c.casefold() for c in owner_cities}
    classes = {"owner": [], "human": [], "bot": []}
    for r in rows:
        if r["city"].casefold() in owner:
            classes["owner"].append(r)
        elif r["engaged"] > 0:
            classes["human"].append(r)
        else:
            classes["bot"].append(r)
    return classes


def human_pages(token, date_range, owner_cities=(), n=20):
    """Pages ranked by engaged sessions, owner cities excluded. Same-post URL
    aliases are folded together by slug, as in the top-pages table."""
    body = {
        "dateRanges": date_range,
        "dimensions": [{"name": "pagePath"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "activeUsers"},
                    {"name": "engagedSessions"}, {"name": "userEngagementDuration"}],
        "orderBys": [{"metric": {"metricName": "engagedSessions"}, "desc": True}],
        "limit": 200,
    }
    if owner_cities:
        body["dimensionFilter"] = {"notExpression": in_list_filter("city", list(owner_cities))}
    report = run_report(token, body)
    canon = canonical_path_map()
    merged, order = {}, []
    for row in report.get("rows", []):
        path = row["dimensionValues"][0]["value"]
        views, users, engaged, duration = _metric_values(row)
        m = PAGE_PATH_RE.match(path)
        key = canon.get(m.group(1), path) if m else path
        if key not in merged:
            merged[key] = {"views": 0, "users": 0, "engaged": 0, "duration": 0.0}
            order.append(key)
        agg = merged[key]
        agg["views"] += int(views); agg["users"] += int(users)
        agg["engaged"] += int(engaged); agg["duration"] += duration
    order = [k for k in order if merged[k]["engaged"] > 0]
    order.sort(key=lambda k: (-merged[k]["engaged"], -merged[k]["duration"]))
    return [(k, merged[k]) for k in order[:n]]


def human_breakdown_md(classes, pages, owner_cities=()):
    def tot(rs, key):
        return sum(r[key] for r in rs)

    lines = [HUMAN_NOTE, "",
             "| Class | Cities | Active users | Page views | Sessions | Engaged sessions |",
             "|---|---|---|---|---|---|"]
    labels = [("human", "Human-like"), ("bot", "Bot-like (no engaged session)")]
    if owner_cities:
        labels.insert(0, ("owner", f"Owner cities ({', '.join(owner_cities)})"))
    for key, label in labels:
        rs = classes[key]
        lines.append(f"| {label} | {len(rs)} | {tot(rs, 'users')} | {tot(rs, 'views')} | "
                     f"{tot(rs, 'sessions')} | {tot(rs, 'engaged')} |")

    human = sorted(classes["human"], key=lambda r: (-r["engaged"], -r["duration"]))
    lines += ["", "### Human-like cities (top 20 by engaged sessions)", "",
              "| City | Engaged sessions | Sessions | Active users | Page views | Avg engagement / session |",
              "|---|---|---|---|---|---|"]
    for r in human[:20]:
        avg = r["duration"] / r["sessions"] if r["sessions"] else 0
        lines.append(f"| {r['city']} | {r['engaged']} | {r['sessions']} | {r['users']} | "
                     f"{r['views']} | {avg:.0f}s |")
    if not human:
        lines.append("| *(no city had an engaged session in this range)* | | | | | |")

    lines += ["", "### Pages read by likely humans (top 20 by engaged sessions"
              + (", owner cities excluded" if owner_cities else "") + ")", "",
              "| Page path | Engaged sessions | Page views | Active users | Avg engagement / view |",
              "|---|---|---|---|---|"]
    for path, a in pages:
        avg = a["duration"] / a["views"] if a["views"] else 0
        lines.append(f"| {path} | {a['engaged']} | {a['views']} | {a['users']} | {avg:.0f}s |")
    if not pages:
        lines.append("| *(no page had an engaged session in this range)* | | | | |")
    return "\n".join(lines)


def merged_pages_to_table(order, merged):
    lines = ["| Page path | Page views | Active users |", "|---|---|---|"]
    footnotes = []
    for key in order:
        row = merged[key]
        note = ""
        if row["aliases"]:
            n = len(footnotes) + 1
            note = f" [{n}]"
            alias_desc = "; ".join(f"`{p}` ({v} views/{u} users)"
                                    for p, (v, u) in row["aliases"].items())
            footnotes.append(f"[{n}]: same post, folded in from a pre-redirect URL "
                              f"still present in GA4's history (301 confirmed working) "
                              f"-- {alias_desc}")
        lines.append(f"| {key}{note} | {row['views']} | {row['users']} |")
    if not order:
        lines.append("| *(no data returned)* | | |")
    if footnotes:
        lines.append("")
        lines.extend(footnotes)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--out", help="write markdown report to this path instead of stdout")
    ap.add_argument("--city-quality-n", type=int, default=12,
                     help="how many top-by-views cities get the device/engagement "
                          "drill-down (0 disables the section)")
    ap.add_argument("--owner-cities", default="",
                     help="comma-separated cities to treat as your own browsing in the "
                          "likely-human section, e.g. 'Madurai,Mumbai,Hyderabad' -- a "
                          "stopgap until GA4's internal-traffic filter is active")
    ap.add_argument("--no-human", action="store_true",
                     help="skip the likely-human section (2 fewer API calls)")
    args = ap.parse_args()
    owner_cities = [c.strip() for c in args.owner_cities.split(",") if c.strip()]

    token = get_access_token()
    date_range = [{"startDate": f"{args.days}daysAgo", "endDate": "today"}]

    totals = run_report(token, {
        "dateRanges": date_range,
        "metrics": [{"name": "activeUsers"}, {"name": "totalUsers"},
                    {"name": "screenPageViews"}, {"name": "sessions"}],
    })
    by_country = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "country"}],
        "metrics": [{"name": "activeUsers"}, {"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "activeUsers"}, "desc": True}],
        "limit": 30,
    })
    by_city = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "city"}],
        "metrics": [{"name": "activeUsers"}, {"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "activeUsers"}, "desc": True}],
        "limit": 30,
    })
    by_page = run_report(token, {
        "dateRanges": date_range,
        "dimensions": [{"name": "pagePath"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "activeUsers"}],
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 20,
    })

    drill_cities = top_cities_by_views(by_city, n=args.city_quality_n) if args.city_quality_n else []
    device_mix = device_mix_by_city(token, date_range, drill_cities)
    engagement = engagement_by_city(token, date_range, drill_cities)

    t = totals.get("rows", [{}])[0].get("metricValues", [])
    t_vals = [v["value"] for v in t] if t else ["0", "0", "0", "0"]

    md = [f"# GA4 report — VertiStrat, last {args.days} days\n",
          f"*Property {PROPERTY_ID}, generated via tools/ga_report.py.*\n",
          "## Totals\n",
          f"- Active users: **{t_vals[0]}**",
          f"- Total users: **{t_vals[1]}**",
          f"- Page views: **{t_vals[2]}**",
          f"- Sessions: **{t_vals[3]}**\n",
          "## Views by country (top 30)\n",
          rows_to_table(by_country, "Country", ["Active users", "Page views"]),
          "\n## Views by city (top 30)\n",
          rows_to_table(by_city, "City", ["Active users", "Page views"]),
          f"\n## City traffic-quality check (top {len(drill_cities)} by page views)\n",
          "Device/browser variety and engagement time are stronger bot signals than "
          "views/user alone: a script racks up pageviews in milliseconds on one "
          "device/browser combo, a real reader does not. `n/a` for views/user means "
          "the API returned page views with no matching active-user row for that city "
          "(sampling/rounding at low volume, not necessarily bot traffic by itself).\n",
          city_quality_to_table(drill_cities, by_city.get("rows", []), device_mix, engagement),
          "\n## Top pages (top 20)\n",
          merged_pages_to_table(*merge_page_aliases(by_page)),
          ]
    if not args.no_human:
        try:
            classes = classify_cities(city_engagement_rows(token, date_range), owner_cities)
            pages = human_pages(token, date_range, owner_cities)
            md += ["\n## Likely human readership\n", human_breakdown_md(classes, pages, owner_cities)]
        except RuntimeError as e:   # never lose the rest of the report to this section
            md += ["\n## Likely human readership\n", f"*Skipped: {e}*"]
    if t_vals[0] == "0" and not by_country.get("rows"):
        md.append("\n**No data returned for this range.** Either the GA4 "
                   "measurement ID isn't actually installed on the blog's "
                   "Blogger theme (Settings → Google Analytics Property "
                   "ID), or there's genuinely zero recorded traffic in this "
                   "window. This is not a script/auth failure if the request "
                   "itself succeeded without an HTTP error above.")

    out_text = "\n".join(md)
    if args.out:
        pathlib.Path(args.out).write_text(out_text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(out_text)


if __name__ == "__main__":
    main()
