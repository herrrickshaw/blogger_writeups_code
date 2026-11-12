#!/usr/bin/env python3
"""Rebuild the Chapter 29/39 (and 28, 32, 38, 54, 55) trade tables from the raw
TradeStat HTML saved by fetch_tradestat.py. Offline; no network.

Outputs (next to this script):
  chapters_annual.csv   FY, chapter, exports, imports, balance (US$ million)
  chapters_fy27ytd.csv  Apr-to-latest-month 2025 vs 2026, same columns
  results.md            human-readable tables + consistency checks

Balance = exports - imports (negative = deficit).
Run with:  python3 -I build_tables.py
"""
import csv
import glob
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
CHAPTERS = ["28", "29", "32", "38", "39", "54", "55"]
FOCUS = ["29", "39"]


def rows(path):
    h = open(path, encoding="utf-8").read()
    for r in re.findall(r"<tr.*?</tr>", h, re.S):
        yield [html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
               for c in re.findall(r"<t[hd].*?</t[hd]>", r, re.S)]


def num(s):
    s = s.replace(",", "").strip()
    return float(s) if s not in ("", "-") else 0.0


def parse_annual(path):
    """-> ({fy_label: {hs: value}}, {fy_label: grand_total}, header)"""
    hdr = None
    data, tot = {}, {}
    for c in rows(path):
        if c and c[0] == "S.No.":
            hdr = c
            fy_prev = c[3].replace(" ", "")
            fy_cur = c[5].replace(" ", "")
            data = {fy_prev: {}, fy_cur: {}}
            continue
        if hdr and len(c) >= 6 and re.fullmatch(r"\d{2}", c[1]):
            data[fy_prev][c[1]] = num(c[3])
            data[fy_cur][c[1]] = num(c[5])
        elif hdr and c and c[0].startswith("India's Total"):
            tot[fy_prev] = num(c[1])
            tot[fy_cur] = num(c[3])
    return data, tot, hdr


def parse_monthly(path):
    """-> ({'month_prev','month_cur','cum_prev','cum_cur'}: {hs: v}, totals, header)"""
    hdr = None
    keys = ["month_prev", "month_cur", "cum_prev", "cum_cur"]
    data = {k: {} for k in keys}
    tot = {}
    for c in rows(path):
        if c and c[0] in ("S.", "S.No."):
            hdr = [re.sub(r"\s+", " ", x) for x in c]
            continue
        if hdr and len(c) >= 9 and re.fullmatch(r"\d{2}", c[1]):
            for k, i in zip(keys, (3, 4, 6, 7)):
                data[k][c[1]] = num(c[i])
        elif hdr and len(c) >= 8 and c[2].startswith("India's Total"):
            for k, i in zip(keys, (3, 4, 6, 7)):
                tot[k] = num(c[i])
    return data, tot, hdr


def main():
    checks = []
    ann = {"export": {}, "import": {}}
    ann_tot = {"export": {}, "import": {}}
    # Annual: later selections override earlier for the overlapping year
    # (a selection's "previous year" column carries the later revision).
    for flow in ("export", "import"):
        for path in sorted(glob.glob(os.path.join(RAW, f"eidb_{flow}_*.html"))):
            d, t, hdr = parse_annual(path)
            if not hdr:
                sys.exit(f"no table in {path}")
            for fy, vals in d.items():
                prev = ann[flow].get(fy)
                if prev is not None:
                    diffs = {hs: (prev.get(hs, 0), vals.get(hs, 0))
                             for hs in CHAPTERS
                             if abs(prev.get(hs, 0) - vals.get(hs, 0)) > 0.005}
                    checks.append((f"{flow} {fy}: earlier vs later selection",
                                   "identical for focus chapters" if not diffs
                                   else f"revised: {diffs}"))
                ann[flow][fy] = vals
                ann_tot[flow][fy] = t.get(fy)
            # chapter sum vs grand total
            for fy, vals in d.items():
                s = sum(vals.values())
                g = t.get(fy)
                if g:
                    checks.append((f"{flow} {fy} sum of 2-digit chapters vs "
                                   f"India total ({os.path.basename(path)})",
                                   f"{s:,.2f} vs {g:,.2f} (diff {s - g:+.2f})"))
    fys = sorted(set(ann["export"]) & set(ann["import"]))

    mfiles = {f: sorted(glob.glob(os.path.join(RAW, f"meidb_{f}_2026_*.html")))[-1]
              for f in ("export", "import")}
    mon, mtot, mhdr = {}, {}, {}
    for f, p in mfiles.items():
        mon[f], mtot[f], mhdr[f] = parse_monthly(p)
    # cross-check: monthly report's 2025 cumulative must not exceed FY2025-26 annual
    for f in ("export", "import"):
        for hs in FOCUS:
            checks.append((f"{f} HS{hs}: Apr-Aug 2025 (monthly report) as share "
                           f"of FY2025-26 annual",
                           f"{mon[f]['cum_prev'][hs] / ann[f]['2025-2026'][hs]:.1%}"))

    # ---- write CSVs
    with open(os.path.join(HERE, "chapters_annual.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["fy", "hs2", "exports_usd_mn", "imports_usd_mn",
                    "balance_usd_mn"])
        for fy in fys:
            for hs in CHAPTERS + ["29+39"]:
                hsl = hs.split("+")
                e = sum(ann["export"][fy][h] for h in hsl)
                i = sum(ann["import"][fy][h] for h in hsl)
                w.writerow([fy, hs, f"{e:.2f}", f"{i:.2f}", f"{e - i:.2f}"])
    with open(os.path.join(HERE, "chapters_fy27ytd.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["period", "hs2", "exports_usd_mn", "imports_usd_mn",
                    "balance_usd_mn"])
        for k, lab in (("cum_prev", "Apr-Aug 2025 (FY2025-26 YTD, revised)"),
                       ("cum_cur", "Apr-Aug 2026 (FY2026-27 YTD, provisional)")):
            for hs in CHAPTERS + ["29+39"]:
                hsl = hs.split("+")
                e = sum(mon["export"][k][h] for h in hsl)
                i = sum(mon["import"][k][h] for h in hsl)
                w.writerow([lab, hs, f"{e:.2f}", f"{i:.2f}", f"{e - i:.2f}"])

    # ---- results.md
    L = ["# TradeStat chapter-level trade, HS 29 & 39 (plus 28, 32, 38, 54, 55)",
         "", "US$ million. Balance = exports − imports (negative = deficit).",
         "Built by `build_tables.py` from raw/ (see README.md for sources).", ""]
    for hs in ["29", "39", "29+39"] + [c for c in CHAPTERS if c not in FOCUS]:
        hsl = hs.split("+")
        L += [f"## HS {hs}", "",
              "| FY | Exports | Imports | Balance |", "|---|---:|---:|---:|"]
        for fy in fys:
            e = sum(ann["export"][fy][h] for h in hsl)
            i = sum(ann["import"][fy][h] for h in hsl)
            L.append(f"| {fy} | {e:,.1f} | {i:,.1f} | {e - i:,.1f} |")
        for k, lab in (("cum_prev", "Apr–Aug 2025"), ("cum_cur", "Apr–Aug 2026")):
            e = sum(mon["export"][k][h] for h in hsl)
            i = sum(mon["import"][k][h] for h in hsl)
            L.append(f"| {lab} | {e:,.1f} | {i:,.1f} | {e - i:,.1f} |")
        L.append("")
    L += ["## Monthly report column headers (status flags as published)", ""]
    for f in ("export", "import"):
        L.append(f"- {f}: `{' | '.join(mhdr[f][3:9])}`")
    L += ["", "## Consistency checks", ""]
    L += [f"- {a}: {b}" for a, b in checks]
    open(os.path.join(HERE, "results.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
