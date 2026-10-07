#!/usr/bin/env python3
"""Look up every IEM company in MCA's Company Master Data: CIN, status, registration date.

MCA publishes its register of companies (CIN, name, status such as Active or
Strike Off, date of registration, registered state, principal business
activity) as RoC-wise CSV files on data.gov.in:
    https://data.gov.in/catalog/company-master-data
Download the CSVs you want (all RoCs for a full check) into one folder, then:

    python3 tools/iem_cin.py --master ~/Downloads/mca_company_master

Columns are found by name (CORPORATE_IDENTIFICATION_NUMBER / CIN, COMPANY_NAME,
COMPANY_STATUS, DATE_OF_REGISTRATION, REGISTERED_STATE, ...), so files with
slightly different headers work. Zauba Corp and similar sites republish this
same MCA data; this reads the source instead of scraping them.

Names are matched after removing M/s, Pvt, Ltd and the like, punctuation and
spaces (the rule iem_records.py uses). Firms and proprietorships have no CIN
and will not match. Where several companies share a normalised name, an Active
one registered in the plant's state is preferred, and the count is kept.

Outputs (data/iem/):
    iem_cin.csv          one row per IEM company name: CIN, status, registration
                         date, registered state, Part A lines, how many reached Part B
    iem_cin_summary.md   company status for filings that reached Part B vs not
"""
import argparse
import collections
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import iem_records as m  # noqa: E402

OUT = ROOT / "data" / "iem"
COLS = {"cin": ("CORPORATEIDENTIFICATIONNUMBER", "CIN", "LLPIN"),
        "name": ("COMPANYNAME", "NAME", "LLPNAME"),
        "status": ("COMPANYSTATUS", "STATUS", "LLPSTATUS"),
        "registered": ("DATEOFREGISTRATION", "DATEOFINCORPORATION", "REGISTRATIONDATE"),
        "reg_state": ("REGISTEREDSTATE", "STATE"),
        "activity": ("PRINCIPALBUSINESSACTIVITYASPERCIN", "PRINCIPALBUSINESSACTIVITY", "INDUSTRIALCLASS"),
        "paid_up": ("PAIDUPCAPITAL", "PAIDUPCAPITALINR")}


def norm_name(s):
    s = (s or "").upper().replace("&", " AND ")
    s = re.sub(r"\bM\s*/\s*S\.?\s*", " ", s)
    return m.norm_company(s)


def colmap(header):
    key = {re.sub(r"[^A-Z]", "", h.upper()): h for h in header}
    out = {}
    for role, names in COLS.items():
        out[role] = next((key[n] for n in names if n in key), None)
    return out


def read_master(folder):
    files = sorted(pathlib.Path(folder).expanduser().rglob("*.csv"))
    if not files:
        sys.exit(f"no .csv files under {folder}; download them from https://data.gov.in/catalog/company-master-data")
    reg = collections.defaultdict(list)
    n = 0
    for f in files:
        raw = f.read_bytes()
        text = raw.decode("utf-8", errors="replace") if b"\x00" not in raw[:1000] else raw.decode("utf-16", errors="replace")
        rd = csv.DictReader(text.splitlines())
        cm = colmap(rd.fieldnames or [])
        if not cm["cin"] or not cm["name"]:
            print(f"  skip {f.name}: no CIN/name column in {rd.fieldnames[:8] if rd.fieldnames else []}")
            continue
        k = 0
        for r in rd:
            nm = norm_name(r.get(cm["name"]))
            if len(nm) < 4:
                continue
            reg[nm].append({role: (r.get(col) or "").strip() if col else "" for role, col in cm.items()})
            k += 1
        n += k
        print(f"  {f.name}: {k:,} companies")
    print(f"{n:,} companies, {len(reg):,} distinct names, from {len(files)} files")
    return reg


def choose(cands, plant_state):
    def score(c):
        return (c["status"].upper() != "ACTIVE", m.norm_state(c["reg_state"]) != plant_state)
    return sorted(cands, key=score)[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--master", required=True, help="folder of MCA Company Master Data CSVs")
    args = ap.parse_args()
    reg = read_master(args.master)

    csv.field_size_limit(10 ** 8)
    A = [r for r in csv.DictReader(open(OUT / "iem_records.csv", encoding="utf-8")) if r["part"] == "A"]
    co = collections.defaultdict(lambda: {"names": collections.Counter(), "states": collections.Counter(),
                                          "lines": 0, "in_b": 0, "years": set()})
    for r in A:
        k = norm_name(r["company"])
        if len(k) < 4:
            continue
        c = co[k]
        c["names"][r["company"].strip()] += 1
        c["states"][m.norm_state(r["state"])] += 1
        c["lines"] += 1
        c["in_b"] += r["in_part_b"] != "no"
        d = m.pdate(r["iem_date"])
        c["years"].add(d.year if d else int(r["period_from"][:4]))

    rows, tally = [], collections.Counter()
    for k, c in co.items():
        cands = reg.get(k, [])
        best = choose(cands, c["states"].most_common(1)[0][0]) if cands else {}
        status = best.get("status", "") or ("not in register" if not cands else "")
        label = status.title() if cands else "Not in register"
        tally[("reached Part B", label)] += c["in_b"]
        tally[("no Part B found", label)] += c["lines"] - c["in_b"]
        rows.append({"company": c["names"].most_common(1)[0][0], "partA_lines": c["lines"], "partA_in_partB": c["in_b"],
                     "filed": f"{min(c['years'])}-{max(c['years'])}", "plant_state": c["states"].most_common(1)[0][0],
                     "cin": best.get("cin", ""), "status": best.get("status", ""), "registered": best.get("registered", ""),
                     "reg_state": best.get("reg_state", ""), "activity": best.get("activity", ""),
                     "same_name_companies": len(cands)})
    rows.sort(key=lambda r: -r["partA_lines"])
    with open(OUT / "iem_cin.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    groups = ("reached Part B", "no Part B found")
    statuses = sorted({s for _, s in tally}, key=lambda s: -sum(tally[(g, s)] for g in groups))
    md = ["# IEM Part A companies in MCA's Company Master Data", "",
          f"{len(co):,} distinct company names from {len(A):,} Part A lines; matched by name with M/s, Pvt, Ltd "
          "and punctuation removed. Firms, proprietorships and names misread from the PDFs will show as not in register. "
          "Counts are Part A lines, by the company's current MCA status.", "",
          "| MCA status | Part A lines that reached Part B | Part A lines with no Part B found |", "|---|---|---|"]
    tot = {g: sum(tally[(g, s)] for s in statuses) for g in groups}
    for s in statuses:
        md.append(f"| {s} | {tally[(groups[0], s)]:,} ({100 * tally[(groups[0], s)] / max(1, tot[groups[0]]):.1f}%) "
                  f"| {tally[(groups[1], s)]:,} ({100 * tally[(groups[1], s)] / max(1, tot[groups[1]]):.1f}%) |")
    md.append(f"| Total | {tot[groups[0]]:,} | {tot[groups[1]]:,} |")
    (OUT / "iem_cin_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    found = sum(1 for r in rows if r["cin"])
    print(f"{found:,} of {len(rows):,} IEM company names found in the register -> {OUT / 'iem_cin.csv'}, iem_cin_summary.md")


if __name__ == "__main__":
    main()
