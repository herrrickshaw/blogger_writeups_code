#!/usr/bin/env python3
"""Download chapter-level (HS 2-digit) India export/import tables from TradeStat.

Source: Ministry of Commerce & Industry, Department of Commerce, TradeStat
(DGCI&S data), https://tradestat.commerce.gov.in/

Two reports are used, both "All commodities, 2 digit level, US $ Million":
  * Annual  EIDB  commodity-wise export / import  (/eidb/commodity_wise_export,
    /eidb/commodity_wise_import). Selecting financial year Y returns columns for
    FY(Y-1) and FY(Y), so FY2020-21 .. FY2025-26 come from selections 2021..2025
    (the 2021 selection also carries FY2020-21).
  * Monthly MEIDB commodity-wise export / import (/meidb/commoditywise_export,
    /meidb/commoditywise_import), financial-year basis. Selecting month M of 2026
    returns month and April-to-M cumulative columns for 2025 (R = revised) and
    2026 (A = provisional). The script walks back from the latest calendar month
    until it finds a month whose 2026 cumulative is non-zero.

Every response is saved verbatim under raw/ ; build_tables.py parses only those
files, so the numbers can be rebuilt offline. Polite: one request at a time with
a pause between requests.

Usage:  python3 fetch_tradestat.py [--outdir raw]
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import time

import requests

BASE = "https://tradestat.commerce.gov.in"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
PAUSE = 1.5  # seconds between requests


def token(sess, path):
    r = sess.get(f"{BASE}/{path}", timeout=60)
    r.raise_for_status()
    m = re.search(r'name="_token" value="([^"]+)"', r.text)
    if not m:
        raise RuntimeError(f"no CSRF token on {path}")
    time.sleep(PAUSE)
    return m.group(1)


def post(sess, path, data):
    data = dict(data, _token=token(sess, path))
    r = sess.post(f"{BASE}/{path}", data=data, timeout=180,
                  headers={"Referer": f"{BASE}/{path}"})
    r.raise_for_status()
    time.sleep(PAUSE)
    return r.text


def ch29_cum_2026(html):
    """Return the 2026 Apr-to-month cumulative for HS 29, as float."""
    for row in re.findall(r"<tr.*?</tr>", html, re.S):
        cells = [re.sub(r"<[^>]+>", "", c).strip()
                 for c in re.findall(r"<t[hd].*?</t[hd]>", row, re.S)]
        if len(cells) >= 8 and cells[1] == "29":
            return float(cells[7].replace(",", "") or 0)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=str(pathlib.Path(__file__).with_name("raw")))
    a = ap.parse_args()
    out = pathlib.Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    sess = requests.Session()
    sess.headers["User-Agent"] = UA
    log = {"fetched_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "files": []}

    jobs = []
    for y in range(2021, 2026):
        jobs.append((f"eidb_export_{y}.html", "eidb/commodity_wise_export",
                     {"EidbYearCwe": y, "comType": "all", "EidbComLevelCwe": 2,
                      "Eidb_ReportCwe": 2}))
        jobs.append((f"eidb_import_{y}.html", "eidb/commodity_wise_import",
                     {"Eidb_YearCwi": y, "commodityType": "all",
                      "Eidb_ComLevelCwi": 2, "Eidb_ReportCwi": 2}))
    t0 = time.time()
    for i, (fn, path, data) in enumerate(jobs, 1):
        html = post(sess, path, data)
        (out / fn).write_text(html, encoding="utf-8")
        log["files"].append({"file": fn, "url": f"{BASE}/{path}", "form": data,
                             "bytes": len(html.encode())})
        el = time.time() - t0
        print(f"[{i}/{len(jobs)}] {fn} {len(html):,}B  "
              f"elapsed {el:.0f}s  ~{el / i * (len(jobs) - i):.0f}s left",
              flush=True)

    # monthly: find latest FY2026-27 month with data
    today = dt.date.today()
    latest = None
    for m in range(min(today.month, 12), 3, -1):
        html = post(sess, "meidb/commoditywise_export",
                    {"ddMonth": m, "ddYear": 2026, "comlev": "all",
                     "ddCommodityLevel": 2, "ddReportVal": 1, "ddReportYear": 1})
        v = ch29_cum_2026(html)
        print(f"probe month {m}/2026: HS29 Apr-cum 2026 = {v}", flush=True)
        if v:
            latest = m
            fn = f"meidb_export_2026_{m:02d}.html"
            (out / fn).write_text(html, encoding="utf-8")
            log["files"].append({"file": fn,
                                 "url": f"{BASE}/meidb/commoditywise_export",
                                 "form": {"ddMonth": m, "ddYear": 2026,
                                          "comlev": "all", "ddCommodityLevel": 2,
                                          "ddReportVal": 1, "ddReportYear": 1},
                                 "bytes": len(html.encode())})
            break
    if latest is None:
        sys.exit("no FY2026-27 month with data found")
    form = {"imddMonth": latest, "imddYear": 2026, "comlev": "all",
            "imddCommodityLevel": 2, "imddReportVal": 1, "imddReportYear": 1}
    html = post(sess, "meidb/commoditywise_import", form)
    fn = f"meidb_import_2026_{latest:02d}.html"
    (out / fn).write_text(html, encoding="utf-8")
    log["files"].append({"file": fn, "url": f"{BASE}/meidb/commoditywise_import",
                         "form": form, "bytes": len(html.encode())})
    log["latest_fy27_month"] = latest
    (out / "fetch_log.json").write_text(json.dumps(log, indent=1))
    print("latest FY2026-27 month:", latest)


if __name__ == "__main__":
    main()
