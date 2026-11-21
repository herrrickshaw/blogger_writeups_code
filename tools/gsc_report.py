#!/usr/bin/env python3
"""Search Console report for VertiStrat: clicks/impressions/CTR/position,
broken down by query and by page, over a date range.

Auth: same service-account JWT bearer flow as tools/ga_report.py (RS256,
`cryptography`, no google-api-python-client) -- reuses ga_service_account.json
rather than provisioning a separate OAuth client, since the account just needs
adding as a Search Console user (Settings -> Users and permissions) to get
the `webmasters.readonly` scope working.

Report-only: reads Search Console data, prints/writes a summary. Never
touches the blog.

    python3 tools/gsc_report.py                    # last 28 days, prints to stdout
    python3 tools/gsc_report.py --days 90 --out out/gsc_report.md
    python3 tools/gsc_report.py --site "https://masaladeutsch.blogspot.com/"
"""
import argparse, base64, json, time, urllib.request, urllib.parse, urllib.error, pathlib
from datetime import date, timedelta

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

SECRETS = pathlib.Path.home() / ".config" / "market-secrets"
SA_FILE = SECRETS / "ga_service_account.json"
DEFAULT_SITE = "https://masaladeutsch.blogspot.com/"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"


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


def query(access_token, site_url, body):
    api = f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(site_url, safe='')}/searchAnalytics/query"
    req = urllib.request.Request(
        api, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Search Console API error {e.code}: {e.read().decode()}") from e


def rows_to_table(resp, dim_label, limit=25, sort_key="impressions"):
    header = [dim_label, "Clicks", "Impressions", "CTR", "Position"]
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    rows = sorted(resp.get("rows", []), key=lambda r: r[sort_key], reverse=True)[:limit]
    for row in rows:
        key = row["keys"][0]
        ctr = f"{row['ctr'] * 100:.2f}%"
        pos = f"{row['position']:.1f}"
        lines.append(f"| {key} | {row['clicks']} | {row['impressions']} | {ctr} | {pos} |")
    if not rows:
        lines.append("| *(no data returned)* | | | | |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--site", default=DEFAULT_SITE, help="Search Console property (URL-prefix or sc-domain:...)")
    ap.add_argument("--out", help="write markdown report to this path instead of stdout")
    args = ap.parse_args()

    token = get_access_token()
    end = date.today() - timedelta(days=2)  # GSC data lags ~2 days
    start = end - timedelta(days=args.days)
    date_range = {"startDate": start.isoformat(), "endDate": end.isoformat()}

    # searchAnalytics.query has no documented request-side sort order, so pull
    # more rows than we display and sort client-side rather than trust it.
    totals = query(token, args.site, {**date_range, "dimensions": []})
    by_query = query(token, args.site, {**date_range, "dimensions": ["query"], "rowLimit": 1000})
    by_page = query(token, args.site, {**date_range, "dimensions": ["page"], "rowLimit": 1000})

    t_rows = totals.get("rows", [])
    t = t_rows[0] if t_rows else {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0}

    md = [f"# Search Console report — VertiStrat, {start} to {end}\n",
          f"*Site `{args.site}`, generated via tools/gsc_report.py.*\n",
          "## Totals\n",
          f"- Clicks: **{t['clicks']}**",
          f"- Impressions: **{t['impressions']}**",
          f"- Average CTR: **{t['ctr'] * 100:.2f}%**",
          f"- Average position: **{t['position']:.1f}**\n",
          "## Top queries (top 25 by impressions)\n",
          rows_to_table(by_query, "Query"),
          "\n## Top pages (top 25 by impressions)\n",
          rows_to_table(by_page, "Page"),
          ]
    if t["clicks"] == 0 and t["impressions"] == 0 and not by_query.get("rows"):
        md.append("\n**No data returned for this range.** Either the service "
                   "account hasn't been added as a Search Console user yet "
                   "(Settings -> Users and permissions), the Search Console "
                   "API isn't enabled for this GCP project, or there's "
                   "genuinely zero indexed traffic in this window. This is "
                   "not a script failure if the request succeeded without an "
                   "HTTP error above.")

    out_text = "\n".join(md)
    if args.out:
        pathlib.Path(args.out).write_text(out_text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(out_text)


if __name__ == "__main__":
    main()
