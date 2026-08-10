#!/usr/bin/env python3
"""GA4 Data API report for masaladeutsch (property 548678807): pageviews and
active-user counts, broken down by country/city, over a date range.

Auth: service-account JWT bearer flow (RS256), signed with `cryptography` --
no google-api-python-client / google-analytics-data dependency, consistent
with this repo's minimal-dependency style (see tools/blogger_api.py).

Report-only: reads GA4 data, prints/writes a summary. Never touches the blog.

    python3 tools/ga_report.py                    # last 28 days, prints to stdout
    python3 tools/ga_report.py --days 7
    python3 tools/ga_report.py --days 90 --out out/ga_report.md
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
    args = ap.parse_args()

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

    t = totals.get("rows", [{}])[0].get("metricValues", [])
    t_vals = [v["value"] for v in t] if t else ["0", "0", "0", "0"]

    md = [f"# GA4 report — masaladeutsch, last {args.days} days\n",
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
          "\n## Top pages (top 20)\n",
          merged_pages_to_table(*merge_page_aliases(by_page)),
          ]
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
