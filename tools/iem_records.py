#!/usr/bin/env python3
"""Parse DPIIT's monthly IEM company lists into one searchable record table.

Input: the .md conversions of the DPIIT "List of IEM Filed" (Part A) and
"List of IEM Implemented" (Part B) PDFs that data-library-toolkit produced
(PyMuPDF plain text, pages joined by blank lines), named like
    2014-01-01_to_2014-01-31_IEM_PartA_32341.md
Output (in --out, default data/iem/):
    iem_records.csv                      one row per IEM line item
    iem_web.json + index.html            the searchable page (serve the folder, open index.html)
    iem_partA_to_partB_by_year.md/.csv   year-by-year: how many Part A filings reached Part B
    iem_partA_not_in_partB.csv           Part A lines with no Part B found
    md/PartA/YYYY-MM.md, md/PartB/YYYY-MM.md   readable monthly tables
    parse_report.md                      per-file record counts and checks

DPIIT changed layouts over 2001-2024. With --pdf-dir, each list is read from
its PDF, which keeps the column positions the .md text loses:

  legacy   2001-2018  fixed-column printout ("LIST OF INDUSTRIAL ENTREPRENEURS'
                      MEMORANDUM", "... PRODUCTION MEMORANDUM"). Words are placed
                      in columns by their x position against the header row; the
                      2009-2016 files whose rows are justified to their own width
                      are split at wide gaps instead. Records start at the serial
                      number (Part A restarts per state).
  table    2017-2024  ruled tables, read cell by cell with PyMuPDF find_tables().

Without a PDF the .md text is parsed instead (one parser per layout), which is
weaker: in many files PyMuPDF's plain text puts each cell on its own line or
interleaves columns.

Part A lines are then matched to Part B lines (the Part B cites the Part A
memorandum number and date; failing that, the same company name), and a
year-by-year table shows how many filings reached Part B and after how long.

Model output is not involved: this is deterministic parsing, and every row keeps
the source file and DPIIT document id so it can be checked against the PDF.

    python3 tools/iem_records.py --md-dir ~/Downloads/DPIIT_IEM_lists/md \
        --pdf-dir ~/Downloads/DPIIT_IEM_lists
"""
import argparse
import csv
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

STATES = [
    "ANDAMAN AND NICOBAR ISLANDS", "ANDAMAN & NICOBAR ISLANDS", "ANDAMAN & NICOBAR", "ANDHRA PRADESH",
    "ARUNACHAL PRADESH", "ASSAM", "BIHAR", "CHANDIGARH", "CHHATTISGARH", "CHATTISGARH",
    "CHHATISGARH", "DADRA AND NAGAR HAVELI AND DAMAN AND DIU", "DADRA & NAGAR HAVELI",
    "DADRA AND NAGAR HAVELI", "DAMAN AND DIU", "DAMAN & DIU", "DELHI", "GOA", "GUJARAT", "HARYANA",
    "HIMACHAL PRADESH", "JAMMU AND KASHMIR", "JAMMU & KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA",
    "LADAKH", "LAKSHADWEEP", "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM",
    "NAGALAND", "ODISHA", "ORISSA", "PUDUCHERRY", "PONDICHERRY", "PUNJAB", "RAJASTHAN", "SIKKIM",
    "TAMIL NADU", "TAMILNADU", "TELANGANA", "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "UTTARANCHAL",
    "WEST BENGAL", "NCT OF DELHI",
]
STATES.sort(key=len, reverse=True)
STATE_RE = re.compile(r"(?:^|[\s,(])(" + "|".join(re.escape(s) for s in STATES) + r")\s*\)?\s*,?\s*$")
DATE = r"\d{1,2}/\d{1,2}/\d{4}"
NAME_RE = re.compile(r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})_IEM_Part([AB])_(\d+)")

FIELDS = ["part", "period_from", "period_to", "doc_id", "source_file", "layout", "serial",
          "company", "address", "district", "state", "location", "tehsil", "item", "capacity",
          "unit", "iem_no", "iem_date", "memo_no", "memo_date", "production_date", "proposal_type",
          "investment_cr", "employment", "in_part_b", "b_production_date", "b_doc_id", "lag_years", "a_in_lists"]

SKIP_LINE = re.compile(r"LIST OF INDUSTRIAL|Filed From|Acknowledged From|S\.No\s+Name of|^\s*Address\s|"
                       r"Annual\s+No\.|Capacity\s+Date|^\s*-{10,}\s*$|^\s*Page\s+\d+", re.I)


def norm_state(s):
    s = (s or "").upper().replace("&", "AND").strip(" ,")
    s = re.sub(r"\s+", " ", s)
    fixes = {"CHATTISGARH": "CHHATTISGARH", "CHHATISGARH": "CHHATTISGARH", "ORISSA": "ODISHA",
             "TAMILNADU": "TAMIL NADU", "UTTARANCHAL": "UTTARAKHAND", "PONDICHERRY": "PUDUCHERRY",
             "NCT OF DELHI": "DELHI", "ANDAMAN AND NICOBAR": "ANDAMAN AND NICOBAR ISLANDS"}
    return fixes.get(s, s)


def chunks(line):
    """[(start_col, text)] split on runs of 2+ spaces."""
    return [(m.start(), m.group(0).strip()) for m in re.finditer(r"\S(?:.*?\S)?(?=\s{2,}|\s*$)", line)]


def join_item(parts):
    """Item text wraps at a fixed 25 characters mid-word in the legacy report."""
    out, prev = "", ""
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # a full-width (24-25 char) piece was cut mid-word: glue the next piece on
        out = out + p if prev and len(prev) >= 25 else (out + " " + p).strip()
        prev = p
    return re.sub(r"\s+", " ", out).strip()


# ---------------------------------------------------------------- legacy ---

REC_START = re.compile(r"^\s{0,6}(\d{1,5})\s+\S")
TAIL = re.compile(r"(-?[\d,]*\.?\d+)\s+(\d+)\s*$")
MEMO = re.compile(r"Memorandum No\.?\s*:?\s*(\S+)\s+Date\s*:?\s*(" + DATE + r")?\s*Production Commenced on\s*:?\s*(" + DATE + r")?", re.I)
LOCN = re.compile(r"^\s*LOCATION\s+(.*?)\s+TEHSIL\s*(.*)$")
STATE_HDR = re.compile(r"^\s*STATE\s*:\s*(.+?)\s*$")


def parse_legacy(text, part):
    lines = text.split("\n")
    recs, cur, state_hdr = [], None, ""
    item_parts, addr_parts = [], []

    def close():
        nonlocal cur
        if cur:
            cur["item"] = join_item(item_parts)
            addr = [a for a in addr_parts if a]
            if addr and re.fullmatch(r"[A-Z]{2}", addr[-1]):
                cur["proposal_type"] = addr.pop()
            cur["address"] = ", ".join(addr)
            recs.append(cur)
        cur = None

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        m = STATE_HDR.match(line)
        if m:
            close(); state_hdr = norm_state(m.group(1)); continue
        if SKIP_LINE.search(line):
            continue
        m = MEMO.search(line)
        if m and cur:
            cur["memo_no"], cur["memo_date"], cur["production_date"] = m.group(1), m.group(2) or "", m.group(3) or ""
            continue
        m = LOCN.match(line)
        if m and cur:
            cur["location"], cur["tehsil"] = m.group(1).strip(" ,"), m.group(2).strip(" ,")
            continue
        if re.match(r"^\s*Telephone\b", line):
            continue
        t = TAIL.search(line)
        if REC_START.match(line) and t and re.search(r"[A-Za-z]", line[:t.start()]):
            close()
            rest = line[:t.start()]
            cs = chunks(rest)
            serial, _, first = cs[0][1].partition(" ")
            name_parts = [first.strip()]
            mid = cs[1:]
            district, item = "", ""
            if len(mid) >= 2:
                name_parts += [c[1] for c in mid[:-2]]
                district, item = mid[-2][1], mid[-1][1]
            elif len(mid) == 1:
                district = mid[0][1]
            cur = {"serial": serial, "company": " ".join(p for p in name_parts if p), "district": district,
                   "state": state_hdr, "capacity": t.group(1), "iem_no": t.group(2),
                   "layout": "legacy", "_cols": [c[0] for c in cs], "_line": 1, "_l1": cs}
            item_parts, addr_parts = [item], []
            continue
        if not cur:
            continue
        cur["_line"] += 1
        cs = chunks(line)
        if not cs:
            continue
        cols = cur["_cols"]
        dist_col = cols[-2] if len(cols) >= 3 else (cols[1] if len(cols) > 1 else 40)
        if cur["_line"] == 2:
            # address | state | item continuation | unit | ack date
            dm = re.search(r"(" + DATE + r")\s*$", line)
            if dm:
                cur["iem_date"] = dm.group(1)
                cs = chunks(line[:dm.start()])
            if cs and cs[0][0] < dist_col - 3:
                addr_parts.append(cs.pop(0)[1])
            if cs:
                sc, st = cs.pop(0)
                cur["state"] = norm_state(st) if STATE_RE.search(" " + st.upper()) else (cur["state"] or norm_state(st))
                fix_columns(cur, item_parts, sc)
            if cs:
                last = cs[-1][1]
                if len(cs) >= 2 or (dm and len(last) <= 14 and not re.search(r"[a-z]", last)):
                    cur["unit"] = cs.pop()[1]
            if cs and not cur.get("unit") and len(cs[-1][1]) > 25:
                # item continuation (25 wide) and unit printed with a single space between them
                col, txt = cs.pop()
                cs.append((col, txt[:25])); cur["unit"] = txt[25:].strip()
            item_parts += [c[1] for c in cs]
            continue
        # later lines: address continuation at the left, item continuation further right
        if cs[0][0] < dist_col - 3:
            addr_parts.append(cs.pop(0)[1])
        item_parts += [c[1] for c in cs if c[0] > dist_col + 5]
    close()
    for r in recs:
        r.pop("_cols", None); r.pop("_line", None); r.pop("_l1", None)
    return recs


def fix_columns(cur, item_parts, state_col):
    """Line 1 is split on runs of 2+ spaces, which fails when a long company name
    runs into the district with one space. Line 2's state sits in the district
    column, so use its start to re-cut line 1."""
    cs = cur.get("_l1") or []
    if len(cs) < 2:
        return
    first_col, first = cs[0]
    if first_col + len(first) > state_col + 2:
        cut = state_col - first_col
        serial, _, _ = first.partition(" ")
        name = first[len(serial):cut].strip()
        spill = first[cut:].strip()
        rest = [c[1] for c in cs[1:]]
        cur["company"] = name
        cur["district"] = spill
        item_parts[:] = [" ".join(rest)] + item_parts[1:] if rest else item_parts


# ----------------------------------------------------------------- tables ---

IEMNO = re.compile(r"^(\d+\s*/\s*[A-Z]{1,3}\s*/\s*SIA\s*/\s*IMO\s*/\s*\d{4})\s*,?\s*$", re.I)
CAP = re.compile(r"^(-?[\d,]*\.?\d+)(?:\s+(.*))?$")


def split_records(lines, hdr_words):
    """Runs of lines between serial-number lines, skipping repeated headers."""
    body = [l.strip() for l in lines]
    body = [l for l in body if l and l not in hdr_words]
    recs, cur = [], None
    expect = 1
    for l in body:
        if re.fullmatch(r"\d{1,5}", l) and int(l) == expect:
            if cur:
                recs.append(cur)
            cur = {"serial": l, "lines": []}
            expect += 1
            continue
        if cur is not None:
            cur["lines"].append(l)
    if cur:
        recs.append(cur)
    return recs


def find_state(lines, start=0):
    """Index of the first line (from start) that ends with a state name."""
    for i in range(start, len(lines)):
        if STATE_RE.search(" " + lines[i].upper()):
            return i
        # state split across two lines, e.g. "MEERUT UTTAR" / "PRADESH"
        if i + 1 < len(lines) and STATE_RE.search(" " + (lines[i] + " " + lines[i + 1]).upper()) and \
                len(lines[i + 1]) <= 14:
            return i + 1
    return -1


def parse_statewise(text, part):
    """Part A 2021-2024: S.No | Company Name and Address | District State | Item | Capacity Unit | IEM No and Date."""
    hdr = {"S.No", "Sr. No.", "Company Name and Address", "District State", "District", "State",
           "Item of Manufacture", "Capacity", "Unit", "Capacity Unit", "IEM Number", "and Date",
           "IEM No and", "Date", "IEM No and Date", "IEM Number and Date"}
    out = []
    for r in split_records(text.split("\n"), hdr):
        L = r["lines"]
        k = next((i for i, l in enumerate(L) if IEMNO.match(l)), -1)
        rec = {"serial": r["serial"], "layout": "statewise"}
        if k >= 0:
            rec["iem_no"] = re.sub(r"\s+", "", IEMNO.match(L[k]).group(1))
            if k + 1 < len(L) and re.fullmatch(DATE, L[k + 1]):
                rec["iem_date"] = L[k + 1]
            L = L[:k]
        # capacity: last numeric line before the IEM number, unit after it
        c = next((i for i in range(len(L) - 1, -1, -1) if CAP.match(L[i]) and not re.fullmatch(r"\d{6}", L[i])), -1)
        if c >= 0:
            m = CAP.match(L[c])
            rec["capacity"] = m.group(1)
            rec["unit"] = " ".join(([m.group(2)] if m.group(2) else []) + L[c + 1:]).strip()
            L = L[:c]
        # address ends at the first line ending in a 6-digit PIN; then district + state, then item
        p = next((i for i, l in enumerate(L) if re.search(r"\b\d{6}\s*$", l)), -1)
        s = find_state(L, p + 1 if p >= 0 else 1)
        if s >= 0:
            head = L[:p + 1] if p >= 0 else L[:max(1, s - 1)]
            ds = " ".join(L[len(head):s + 1])
            rec["item"] = " ".join(L[s + 1:])
            m = STATE_RE.search(" " + ds.upper())
            rec["state"] = norm_state(m.group(1))
            rec["district"] = ds[:m.start(1) - 1].strip(" ,") if m.start(1) > 0 else ""
        else:
            head = L
        rec["company"], rec["address"] = split_company(head)
        out.append(rec)
    return out


def split_company(head):
    """Company name is the text up to the first comma that follows a corporate suffix."""
    s = " ".join(head)
    m = re.search(r"^(.*?\b(?:LIMITED|LTD\.?|LLP|PVT\.?\s*LTD\.?|PRIVATE LIMITED|CORPORATION|COMPANY|INDUSTRIES)\b\.?)\s*[,;]?\s*(.*)$", s, re.I)
    if m:
        return m.group(1).strip(" ,"), m.group(2).strip(" ,")
    name, _, addr = s.partition(",")
    return name.strip(), addr.strip()


def parse_breakup2019(text, part):
    """Part A 2017-2021: Sl. No | Company Name and Address | Item | District State | Capacity Unit | IEM No and Date,
    then 'Place(Tehsil) : ...'. Some files add an investment (Rs crore) and employment column."""
    hdr = {"Sl.", "No", "Sl. No", "Company Name", "and Address", "Company Name and Address", "Item of Manufacture",
           "District", "State", "Capaci", "ty", "Capacity", "Unit", "IEM No", "and", "Date", "(Investment in Rs Crore)"}
    out = []
    for r in split_records(text.split("\n"), hdr):
        L = r["lines"]
        rec = {"serial": r["serial"], "layout": "breakup"}
        tz = next((i for i, l in enumerate(L) if l.startswith("Place(Tehsil)")), -1)
        if tz >= 0:
            rec["tehsil"] = " ".join(L[tz:]).split(":", 1)[-1].strip(" ,")
            L = L[:tz]
        # IEM number, day and "Month YYYY" (often split mid-word) close the record
        tail = " ".join(L[-4:]) if len(L) >= 4 else " ".join(L)
        m = re.search(r"\b(\d{1,5})\s+(\d{1,2})\s+([A-Za-z]+\s*[a-z]*)\s+(\d{4})\s*$", " ".join(L))
        if m:
            rec["iem_no"] = m.group(1)
            rec["iem_date"] = f"{m.group(2)} {m.group(3).replace(' ', '')} {m.group(4)}"
            # drop the consumed tail lines
            consumed = len(m.group(0).split())
            words = 0
            while L and words < consumed:
                words += len(L[-1].split()); L = L[:-1]
        c = next((i for i in range(len(L) - 1, -1, -1) if CAP.match(L[i]) and not re.fullmatch(r"\d{6}", L[i])), -1)
        if c >= 0:
            m2 = CAP.match(L[c]); rec["capacity"] = m2.group(1)
            rec["unit"] = " ".join(([m2.group(2)] if m2.group(2) else []) + L[c + 1:]).strip()
            L = L[:c]
        s = find_state(L, 1)
        # the address ends with "STATE-PIN"; the district/state cell is the LAST state-ending run
        s_last = -1
        i = 0
        while True:
            j = find_state(L, i)
            if j < 0:
                break
            s_last, i = j, j + 1
        a = next((i for i, l in enumerate(L) if re.search(r"-\s*\d{6}\s*$|\b\d{6}\s*$", l)), -1)
        if s_last >= 0 and s_last > a:
            # district/state run: walk back from s_last over short lines
            d0 = s_last
            while d0 - 1 > a and len(L[d0 - 1]) <= 22 and not re.search(r"\d", L[d0 - 1]) and d0 - 1 > a + 1:
                d0 -= 1
            ds = " ".join(L[d0:s_last + 1])
            m3 = STATE_RE.search(" " + ds.upper())
            rec["state"] = norm_state(m3.group(1))
            rec["district"] = ds[:max(0, m3.start(1) - 1)].strip(" ,")
            rec["item"] = " ".join(L[a + 1:d0])
            head = L[:a + 1]
        else:
            head = L
        rec["company"], rec["address"] = split_company(head)
        out.append(rec)
    return out


def parse_partb_table(text, part):
    """Part B 2018-2024: Sr. No | Name Of Undertaking / Address | Location | Item | Actual Capacity |
    Ack No./Date | Mem No | Mem Date | Production Commenced On."""
    hdr = {"Sr. No.", "Sr.", "No.", "Name Of Undertaking / Address", "Name Of Undertaking /", "Address",
           "Location", "Item Of Manufacture", "Actual Capacity", "Ack No./Date", "Mem No", "Mem Date",
           "Production Commenced On", "Production", "Commenced On"}
    out = []
    for r in split_records(text.split("\n"), hdr):
        L = r["lines"]
        rec = {"serial": r["serial"], "layout": "partb-table"}
        dates = [i for i, l in enumerate(L) if re.search(DATE + r"\s*$", l)]
        # trailing cells: "ack date" | memo no | memo date | production date
        if len(dates) >= 3:
            pdx, mdx = dates[-1], dates[-2]
            rec["production_date"] = re.search(DATE, L[pdx]).group(0)
            rec["memo_date"] = re.search(DATE, L[mdx]).group(0)
            between = " ".join(L[dates[-3] + 1:mdx]).strip()
            rec["memo_no"] = between
            am = re.search(r"(\d+)\s+(" + DATE + r")", " ".join(L[dates[-3] - 1:dates[-3] + 1]))
            if am:
                rec["iem_no"], rec["iem_date"] = am.group(1), am.group(2)
            L = L[:dates[-3] + 1]
            # strip the ack cell (number + date) from the end
            while L and (re.search(DATE + r"\s*$", L[-1]) or re.fullmatch(r"\d{1,6}", L[-1])):
                L = L[:-1]
                if not L or not re.fullmatch(r"\d{1,6}", L[-1]):
                    break
        c = next((i for i in range(len(L) - 1, -1, -1) if CAP.match(L[i]) and not re.fullmatch(r"\d{6}", L[i])), -1)
        if c >= 0:
            m2 = CAP.match(L[c]); rec["capacity"] = m2.group(1)
            rec["unit"] = " ".join(([m2.group(2)] if m2.group(2) else []) + L[c + 1:]).strip()
            L = L[:c]
        s = next((i for i, l in enumerate(L) if re.search(r",\s*(" + "|".join(re.escape(x) for x in STATES) + r")\s*$", l.upper())), -1)
        if s < 0:
            s = find_state(L, 1)
        if s >= 0:
            loc = L[s]
            if not STATE_RE.search(" " + loc.upper()) and s > 0:
                loc = L[s - 1] + " " + loc; s -= 1
            m3 = re.search(r"^(.*?)\s*,\s*(.+)$", loc)
            if m3:
                rec["district"], rec["state"] = m3.group(1).strip(), norm_state(m3.group(2))
            else:
                m4 = STATE_RE.search(" " + loc.upper())
                if m4:
                    rec["state"] = norm_state(m4.group(1)); rec["district"] = loc[:max(0, m4.start(1) - 1)].strip(" ,")
            rec["item"] = " ".join(L[s + 1:])
            head = L[:s]
        else:
            head = L
        rec["company"], rec["address"] = split_company(head)
        out.append(rec)
    return out


# ------------------------------------------------ PDF word positions (legacy) ---
# The 2001-2018 reports are fixed-column printouts. In many of them PyMuPDF's
# plain text puts every cell on its own line (or moves a page's item column to
# the end of the page), so the .md text cannot say which column a line came
# from. The PDF's word coordinates can: the header row ("Name of Undertaking",
# "Location", "Item of Manufacture", "Proposed", "Ack.") gives the column
# edges, and each word is placed by its x position.

CAP_RE = re.compile(r"^-?[\d,]*\.\d{1,3}$")
WRAP_OFFSET = 10000
LEGEND = re.compile(r"\b[A-Z]{2}\s*:\s*(MANUFACTURE OF|ESTABLISHMENT|EFFECTING|CARRY|CHANGE|GENERAL)|OF A NEW UNDERTAKING")
PTYPE = {"NU", "SE", "NA", "CO", "GM", "EX", "MN", "DV"}


def page_lines(page, tol=2.5):
    words = sorted(page.get_text("words"), key=lambda w: (w[1], w[0]))
    lines = []
    for w in words:
        if lines and abs(w[1] - lines[-1][0]) <= tol:
            lines[-1][1].append(w)
        else:
            lines.append([w[1], [w]])
    return [(y, sorted(ws, key=lambda w: w[0])) for y, ws in lines]


def header_cols(lines):
    """Column x positions from the 'S.No Name of Undertaking ... Location ... Item ... Ack.' row."""
    for i, (y, ws) in enumerate(lines[:-1]):
        # Feb-Apr 2017: a portrait printout wraps each report line in two, so the header
        # reads 'S.No Name of Undertaking/ Location' over 'Item of Manufacture Proposed Ack.'
        t, t2 = [w[4] for w in ws], [w[4] for w in lines[i + 1][1]]
        if "Location" in t and "Item" not in t and "Item" in t2 and ("Ack." in t2 or "Ack" in t2):
            x, x2 = {w[4]: w[0] for w in ws}, {w[4]: w[0] for w in lines[i + 1][1]}
            off = WRAP_OFFSET
            cols = {"sno": ws[0][0], "name": x.get("Name", ws[0][0] + 20), "loc": x["Location"],
                    "item": off + x2["Item"], "prop": off + x2.get("Proposed", x2["Item"] + 200),
                    "ack": off + (x2.get("Ack.") or x2.get("Ack")), "wrap": x2["Item"]}
            end = lines[i + 1][0]
            for y2, ws2 in lines[i + 2:i + 6]:
                if any(w[4] in ("Date", "No./", "Capacity", "Address", "Annual") for w in ws2) and y2 - end < 30:
                    end = y2
            return cols, end
    for i, (y, ws) in enumerate(lines):
        t = [w[4] for w in ws]
        if "Location" in t and "Item" in t:
            x = {w[4]: w[0] for w in ws}
            cols = {"sno": ws[0][0], "name": x.get("Name", ws[0][0] + 20), "loc": x["Location"], "item": x["Item"],
                    "prop": x.get("Proposed"), "ack": x.get("Ack.") or x.get("Ack")}
            end = y
            for y2, ws2 in lines[i + 1:i + 6]:  # 'Address  Annual No./' and 'Capacity Date' rows
                if any(w[4] in ("Date", "No./", "Capacity", "Address", "Annual") for w in ws2) and y2 - end < 25:
                    end = y2
                    for w in ws2:
                        if w[4] == "Date" and not cols["ack"]:
                            cols["ack"] = w[0]
                        if w[4] == "Annual" and not cols["prop"]:
                            cols["prop"] = w[0]
            if not cols["prop"] or not cols["ack"]:
                return None, None
            return cols, end
    return None, None


def calibrate(cols, lines):
    """Some 2009-2016 PDFs print the header in a narrower font than the rows, so
    the header's x positions do not line up with the data, and each data line is
    justified to its own width. If the acknowledgement numbers on record lines sit
    well away from the 'Ack.' heading, switch to gap-based cell splitting."""
    if cols.get("wrap"):
        return cols
    firsts, lasts = [], []
    for _, ws in lines:
        if len(ws) >= 4 and re.fullmatch(r"\d{1,5}", ws[0][4]) and re.fullmatch(r"\d{1,6}", ws[-1][4]) \
                and ws[0][0] < cols["name"] + 15 and re.search(r"[A-Za-z]", ws[1][4]):
            firsts.append(ws[0][0]); lasts.append(ws[-1][0])
    if len(lasts) < 2:
        return cols
    firsts.sort(); lasts.sort()
    s_obs, a_obs = firsts[len(firsts) // 2], lasts[len(lasts) // 2]
    if abs(a_obs - cols["ack"]) <= 30 or cols["ack"] <= cols["sno"]:
        return cols
    return dict(cols, runs=True)


def zones(ws, cols, idx=0):
    """Assign a printed line's words to the five columns: name/address, district/state,
    item, capacity/unit, acknowledgement no./date."""
    z = {0: [], 1: [], 2: [], 3: [], 4: []}
    if cols.get("wrap"):
        # the wrapped half-line has no stable columns: read it by content
        b = [w for w in ws if w[0] >= WRAP_OFFSET]
        has_cap = any(CAP_RE.match(w[4]) for w in b)
        words = [w for w in b if not (re.fullmatch(DATE, w[4]) or CAP_RE.match(w[4])
                                      or (has_cap and re.fullmatch(r"\d{1,6}", w[4])))]
        for w in ws:
            if w[0] < WRAP_OFFSET:
                z[0 if w[0] < cols["loc"] - 15 else 1].append(w)
            elif re.fullmatch(DATE, w[4]) or (has_cap and re.fullmatch(r"\d{1,6}", w[4])):
                z[4].append(w)
            elif CAP_RE.match(w[4]):
                z[3].append(w)
            elif idx == 1 and (w is words[-1] or len(" ".join(x[4] for x in words)) <= 12):
                z[3].append(w)
            else:
                z[2].append(w)
        return z
    if not cols.get("runs"):
        for w in ws:
            x = w[0]
            if x < cols["loc"] - 15:
                k = 0
            elif x < cols["item"] - 15:
                k = 1
            elif x >= cols["ack"] - 8:
                k = 4
            elif CAP_RE.match(w[4]):
                k = 3
            elif x >= cols["prop"] - 3:
                k = 3
            else:
                k = 2
            z[k].append(w)
        return z
    # Justified rows: each printed line is stretched to its own width, so columns
    # have no fixed x. Split the line into runs of words at wide gaps and read the
    # runs in column order instead.
    rest = []
    for w in ws:
        if w[0] > cols["name"] + 25 and (re.fullmatch(DATE, w[4]) or CAP_RE.match(w[4])):
            z[3 if CAP_RE.match(w[4]) else 4].append(w)
        else:
            rest.append(w)
    if idx == 0 and len(rest) > 2 and re.fullmatch(r"\d{1,6}", rest[-1][4]):
        z[4].append(rest.pop())
    runs = []
    for w in rest:
        if runs and w[0] - runs[-1][-1][2] <= 12:
            runs[-1].append(w)
        else:
            runs.append([w])
    if runs and runs[0][0][0] < cols["name"] + 25:
        z[0] += runs.pop(0)
    text = lambda r: " ".join(w[4] for w in r)
    if idx == 0:
        if runs and (len(runs) >= 2 or runs[0][0][0] < cols["item"] or STATE_RE.search(" " + text(runs[0]).upper())):
            z[1] += runs.pop(0)
        for r in runs:
            z[2] += r
    elif idx == 1:
        if runs and STATE_RE.search(" " + text(runs[0]).upper()):
            z[1] += runs.pop(0)
        if len(runs) >= 2:
            z[3] += runs.pop()
        elif runs and z[4] and len(text(runs[0])) > 26:
            # 25-character item cell and the unit printed with a single space between them
            r = runs.pop()
            cut = 0
            for i, w in enumerate(r):
                if len(text(r[:i + 1])) >= 25:
                    cut = i + 1
                    break
            z[2] += r[:cut]; z[3] += r[cut:]
        elif runs and z[4] and runs[0][0][0] > cols["prop"]:
            z[3] += runs.pop()
        for r in runs:
            z[2] += r
    else:
        for r in runs:
            z[2] += r
    return z


def unwrap_lines(lines, bx, hdr_end):
    """Re-join a wrapped printout: a line starting at the item column (x near bx) is
    the second half of the line above it, so shift its words right and merge."""
    out = []
    for y, ws in lines:
        if (hdr_end is None or y > hdr_end + 1) and ws[0][0] <= bx + 6 and out and not out[-1][2]:
            py, pws, _ = out[-1]
            out[-1] = (py, pws + [(w[0] + WRAP_OFFSET, w[1], w[2] + WRAP_OFFSET) + tuple(w[3:]) for w in ws], True)
        else:
            out.append((y, list(ws), False))
    return [(y, ws) for y, ws, _ in out]


def parse_pdf_words(pdf_path, part):
    import fitz
    fitz.TOOLS.mupdf_display_errors(False)
    doc = fitz.open(str(pdf_path))
    recs, cur, cols, state_hdr, last = [], None, None, "", 0

    def close():
        nonlocal cur
        if cur:
            b = cur.pop("_b")
            cur.pop("_i", None)
            cur["item"] = join_item(b["item"])
            addr = b["addr"]
            cur["company"] = b["name"]
            cur["address"] = ", ".join(a.strip(" ,") for a in addr if a.strip(" ,"))
            z1 = [z for z in b["z1"] if z]
            if z1:
                if STATE_RE.search(" " + z1[0].upper()) and len(z1) == 1:
                    cur["state"] = norm_state(z1[0])
                else:
                    cur["district"] = z1[0]
                    rest = " ".join(z1[1:])
                    if rest:
                        m = STATE_RE.search(" " + rest.upper())
                        cur["state"] = norm_state(m.group(1)) if m else norm_state(rest)
            if not cur.get("state"):
                cur["state"] = state_hdr
                for a in reversed(addr[-3:]):
                    m = STATE_RE.search(" " + re.sub(r"[\d\-.]+", " ", a.upper()).strip())
                    if m:
                        cur["state"] = norm_state(m.group(1)); break
            cur["unit"] = " ".join(b["unit"]).strip()
            recs.append(cur)
        cur = None

    for page in doc:
        lines = page_lines(page)
        c2, hdr_end = header_cols(lines)
        if c2:
            cols = calibrate(c2, [l for l in lines if l[0] > hdr_end + 1])
        if not cols:
            continue
        if cols.get("wrap"):
            lines = unwrap_lines(lines, cols["wrap"], hdr_end)
        for y, ws in lines:
            if hdr_end is not None and y <= hdr_end + 1:
                text = " ".join(w[4] for w in ws)
                m = STATE_HDR.match(text)
                if m:
                    close(); state_hdr = norm_state(m.group(1))
                continue
            text = " ".join(w[4] for w in ws)
            m = STATE_HDR.match(text)
            if m:
                close(); state_hdr = norm_state(m.group(1)); continue
            if LEGEND.search(text):
                continue
            if re.fullmatch(r"[-\s\u00ad]+", text) or re.match(r"^Page\s+\d+", text):
                continue
            m = re.search(r"Memorandum No\.?\s*:?\s*(\S+)?", text, re.I)
            if m and cur:
                if m.group(1) and not m.group(1).startswith("Date"):
                    cur["memo_no"] = m.group(1)
                d = re.search(r"Date\s*:?\s*(" + DATE + ")", text)
                if d:
                    cur["memo_date"] = d.group(1)
                p = re.search(r"Commenced on\s*:?\s*(" + DATE + ")", text)
                if p:
                    cur["production_date"] = p.group(1)
                continue
            if cur and re.match(r"^Date\s*:", text):
                d = re.search(DATE, text)
                cur["memo_date"] = d.group(0) if d else ""
                p = re.search(r"Commenced on\s*:?\s*(" + DATE + ")", text)
                if p:
                    cur["production_date"] = p.group(1)
                continue
            if cur and re.match(r"^Production Commenced", text):
                p = re.search(DATE, text)
                cur["production_date"] = p.group(0) if p else ""
                continue
            m = re.search(r"ACTUAL INVESTMENT.*?\)\s*(\S+)?.*?Employment\s*(\S+)?", text, re.I)
            if m and cur:
                cur["investment_cr"], cur["employment"] = m.group(1) or "", m.group(2) or ""
                continue
            m = re.match(r"^LOCATION\b\s*(.*?)(?:\s+TEHSIL\b\s*(.*))?$", text)
            if m and cur:
                cur["location"], cur["tehsil"] = (m.group(1) or "").strip(" ,"), (m.group(2) or "").strip(" ,")
                continue
            if cur and re.match(r"^TEHSIL\b", text):
                cur["tehsil"] = text[6:].strip(" ,")
                continue
            if re.match(r"^(Telephone|Fax)\b", text):
                continue
            first, start = ws[0], False
            if re.fullmatch(r"\d{1,5}", first[4]) and first[0] < cols["name"] - 2 and len(ws) > 1:
                n = int(first[4])
                start = n == last + 1 or n == 1 or (cur is None and n > last)
            z = zones(ws, cols, 0 if start or not cur else cur["_i"] + 1)
            if start:
                close()
                last = n
                cur = {"serial": first[4], "layout": "pdf-legacy", "_i": 0,
                       "_b": {"name": " ".join(w[4] for w in z[0][1:]), "addr": [], "z1": [], "item": [],
                              "unit": []}}
                z[0] = []
            elif cur:
                cur["_i"] += 1
            if not cur:
                continue
            b = cur["_b"]
            t0 = " ".join(w[4] for w in z[0])
            if t0:
                if t0 in PTYPE:
                    cur["proposal_type"] = t0
                else:
                    b["addr"].append(t0)
            if z[1]:
                b["z1"].append(" ".join(w[4] for w in z[1]))
            if z[2]:
                b["item"].append(" ".join(w[4] for w in z[2]))
            for w in z[3]:
                if CAP_RE.match(w[4]) and not cur.get("capacity"):
                    cur["capacity"] = w[4]
                elif not CAP_RE.match(w[4]):
                    b["unit"].append(w[4])
            for w in z[4]:
                if re.fullmatch(DATE, w[4]):
                    cur.setdefault("iem_date", w[4])
                elif re.fullmatch(r"\d+", w[4]) and not cur.get("iem_no"):
                    cur["iem_no"] = w[4]
        # a page break does not end a record: legacy records run over pages
    close()
    return recs


# ------------------------------------------------------- PDF tables (2017+) ---
# PyMuPDF's plain text interleaves cells from different columns in several of
# the 2020-2024 ruled-table PDFs (e.g. 2023 Part B), so for table-era files the
# cells are read straight from the PDF with page.find_tables() when the PDF is
# available (--pdf-dir), and the .md heuristics above are only the fallback.

COLMAP = [("serial", r"^(s\.?\s*no|sr\.?|sl\.?)"), ("company", r"company|undertaking"),
          ("location", r"^location"), ("district", r"district"), ("item", r"item"),
          ("investment_cr", r"invest"), ("employment", r"employ"),
          ("capacity", r"capaci"), ("iem", r"iem ?n|ack ?n|part-b ?n"),
          ("memo_no", r"mem no|part-a no"), ("memo_date", r"mem date|part-a date"),
          ("production_date", r"production|commenced")]
MONTHS = "january february march april may june july august september october november december".split()


def header_map(row):
    m = {}
    for i, c in enumerate(row):
        c = re.sub(r"\s+", " ", (c or "")).strip().lower()
        if not c:
            continue
        cz = c.replace(" ", "")  # narrow header cells wrap mid-word: 'IE/M/No/an/d/Da/te'
        for key, pat in COLMAP:
            if key not in m and (re.search(pat, c) or re.search(pat, cz)):
                m[key] = i
                break
    return m if "company" in m and ("item" in m or "capacity" in m) else None


def clean(c):
    return re.sub(r"\s+", " ", (c or "").replace("\n", " ")).strip()


def split_iem_cell(s):
    """'49/N/SIA/IMO/2024, 23/01/2024' | '42 18/01/2019' | '26 08 Januar y 2019' -> (no, date)."""
    s = re.sub(r"\s*/\s*", "/", clean(s))
    s = re.sub(r"(?<=[A-Z])\s+(?=[A-Z]*/)", "", s)  # '910/N/SIA/IM O/2022' wrapped inside the cell
    m = re.search(r"(\d+\s*/\s*[A-Z]+\s*/\s*SIA\s*/\s*IMO\s*/\s*\d{4}|\d+\s*/\s*IIM\s*/\s*P\s*R\s*O\s*D\s*/\s*\d{4}"
                  r"|\d+\s*/\s*\d{4}|\d+)\s*,?\s*("
                  + DATE + r"|\d{1,2}-\d{1,2}-\d{4})", s)
    if m:
        return re.sub(r"\s+", "", m.group(1)), m.group(2)
    m = re.search(r"^(\d+)\s+(\d{1,2})\s+([A-Za-z ]+?)\s*(\d{4})$", s)
    if m:
        mon = m.group(3).replace(" ", "")
        mi = next((i + 1 for i, x in enumerate(MONTHS) if x.startswith(mon.lower()[:3])), None)
        return m.group(1), (f"{int(m.group(2)):02d}/{mi:02d}/{m.group(4)}" if mi else f"{m.group(2)} {mon} {m.group(4)}")
    return s, ""


STATES_C = sorted({re.sub(r"[^A-Z]", "", s): s for s in STATES}.items(), key=lambda kv: -len(kv[0]))


def unwrap(cell):
    """Join a narrow cell's lines, gluing a line that fills the cell width to the next
    when the break falls inside a word ('UTTARAKHAN' + 'D')."""
    lines = [l.strip() for l in (cell or "").split("\n") if l.strip()]
    if not lines:
        return ""
    width = max(len(l) for l in lines)
    out = lines[0]
    for prev, nxt in zip(lines, lines[1:]):
        glue = len(prev) >= width - 1 and prev[-1].isalpha() and nxt[0].isalpha()
        out += ("" if glue else " ") + nxt
    return re.sub(r"\s+", " ", out).strip()


def split_place(cell):
    """'MEDAK\nTELANGANA' -> ('MEDAK', 'TELANGANA'); tolerates '(UT)' and words broken
    across lines ('UTTARAKHAN D') by matching the state with spaces removed."""
    cell = re.sub(r"\(\s*UT\s*\)", "", unwrap(cell), flags=re.I).strip(" ,")
    m = STATE_RE.search(" " + cell.upper())
    if m:
        return cell[:max(0, m.start(1) - 1)].strip(" ,"), norm_state(m.group(1))
    comp = re.sub(r"[^A-Z]", "", cell.upper())
    for sc, name in STATES_C:
        if comp.endswith(sc):
            n, i = len(sc), len(cell)
            while n and i:
                i -= 1
                if cell[i].isalpha():
                    n -= 1
            return cell[:i].strip(" ,-"), norm_state(name)
    return cell, ""


def split_iem_raw(raw):
    """IEM number and date from a table cell, also when a narrow cell wrapped them
    one fragment per line: '94/9/24/Ma/y/20/19' -> ('949', '24/05/2019')."""
    no, dt = split_iem_cell(raw)
    if dt:
        return no, dt
    lines = [l.strip() for l in (raw or "").split("\n") if l.strip()]
    i = next((k for k, l in enumerate(lines) if re.search(r"[A-Za-z]", l)), None)
    if i is not None and i >= 2:
        num, day = "".join(lines[:i - 1]), lines[i - 1]
        mon = "".join(l for l in lines[i:] if re.fullmatch(r"[A-Za-z]+", l))
        yr = "".join(l for l in lines[i:] if re.fullmatch(r"\d+", l))
        mi = next((k + 1 for k, x in enumerate(MONTHS) if mon and x.startswith(mon.lower()[:3])), None)
        if num.isdigit() and day.isdigit() and len(yr) == 4 and mi:
            return num, f"{int(day):02d}/{mi:02d}/{yr}"
    return no, dt


def parse_pdf_tables(pdf_path, part):
    import fitz  # PyMuPDF, already a data-library-toolkit dependency
    fitz.TOOLS.mupdf_display_errors(False)
    doc = fitz.open(str(pdf_path))
    out, cmap, cur, blocks, cmap_x, ncols = [], None, None, False, {}, 0

    def col_centres(tab):
        """x centre of each column, from the row with the most separate cells
        (title and header rows often span several columns)."""
        if not tab.rows:
            return {}
        best = max(tab.rows, key=lambda r: sum(1 for c in r.cells if c))
        return {i: (c[0] + c[2]) / 2 for i, c in enumerate(best.cells) if c}

    def remap(tab):
        """Column positions shift between pages (a 14-column table on page 1, 10 on
        page 2), so map each field to the column nearest to where its heading was."""
        xs = col_centres(tab)
        return {k: min(xs, key=lambda i: abs(xs[i] - x)) for k, x in cmap_x.items()} if xs else cmap

    for page in doc:
        for tab in page.find_tables().tables:
            rows = tab.extract()
            if cmap_x and tab.col_count != ncols and not any(header_map(r) for r in rows[:8]):
                cmap = remap(tab)
            # Some 2018 Part B tables give one row per printed line: the header runs over
            # several rows and the serial sits mid-record, with blank rows between records.
            # Merge the header rows, then read each blank-separated block as one record.
            lead = []
            for row in rows[:6]:
                if not any((c or "").strip() for c in row) or any(re.fullmatch(r"\d{1,5}", (c or "").strip()) for c in row):
                    break
                lead.append(row)
            if len(lead) > 1:
                merged = ["\n".join((r[i] or "") for r in lead if i < len(r)) for i in range(max(map(len, lead)))]
                hm = header_map(merged)
                single = max((len(header_map(r) or {}) for r in lead), default=0)
                if hm and len(hm) > single:
                    cmap, blocks = hm, True
                    xs = col_centres(tab)
                    cmap_x, ncols = {k: xs[i] for k, i in hm.items() if i in xs}, tab.col_count
                    rows = rows[len(lead):]
            if blocks and cmap:
                group = []
                for row in rows + [[""]]:
                    if any((c or "").strip() for c in row):
                        group.append(row)
                        continue
                    if group:
                        cells = {key: "\n".join((g[i] or "") for g in group if i < len(g)).strip("\n")
                                 for key, i in cmap.items()}
                        ser = (re.findall(r"\d+", cells.get("serial", "")) or [""])[0]
                        if ser:
                            out.append({"serial": ser, "layout": "pdf-table", "_raw": cells})
                        elif out:  # a record split by a page break
                            for key, v in cells.items():
                                if v.strip() and key != "serial":
                                    out[-1]["_raw"][key] = (out[-1]["_raw"].get(key, "") + "\n" + v).strip("\n")
                    group = []
                continue
            for row in rows:
                hm = header_map(row)
                if hm:
                    cmap, blocks = hm, False
                    xs = col_centres(tab)
                    cmap_x, ncols = {k: xs[i] for k, i in hm.items() if i in xs}, tab.col_count
                    continue
                if not cmap:
                    continue
                used = set(cmap.values())

                def raw(k):
                    """The cell under heading k; when merged header cells sit one column off
                    the data (2022 Part A), take the unclaimed neighbouring cell instead."""
                    if k not in cmap:
                        return ""
                    i = cmap[k]
                    for j in (i, i + 1, i - 1):
                        if 0 <= j < len(row) and (j == i or j not in used) and (row[j] or "").strip():
                            return row[j]
                    return ""
                ser = re.sub(r"\s+", "", raw("serial"))  # '1\n0' is serial 10 in a narrow column
                if re.fullmatch(r"\d{1,5}", ser):
                    cur = {"serial": ser, "layout": "pdf-table", "_raw": {k: raw(k) for k in cmap}}
                    out.append(cur)
                elif cur is not None:
                    for k in cmap:  # continuation row: a cell carried over a page, or the Place(Tehsil) line
                        v = raw(k)
                        if v.strip() and k != "serial":
                            cur["_raw"][k] = (cur["_raw"].get(k, "") + "\n" + v).strip("\n")
    for r in out:
        rc = r.pop("_raw")
        c = {k: clean(v) for k, v in rc.items()}
        r["_place"] = rc.get("district") or rc.get("location", "")
        r["_iem"] = rc.get("iem", "")
        comp = c.get("company", "")
        tz = re.search(r"Place\s*\(Tehsil\)\s*:?\s*(.*)$", comp)
        if tz:
            r["tehsil"] = tz.group(1).strip(" ,()"); comp = comp[:tz.start()].strip()
        pt = re.search(r",\s*(NU|SE|NA|CO|GM)\s*$", comp)
        if pt:
            r["proposal_type"] = pt.group(1); comp = comp[:pt.start()]
        r["company"], r["address"] = split_company([comp])
        r["district"], r["state"] = split_place(r.pop("_place", "") or c.get("district") or c.get("location", ""))
        r["item"] = c.get("item", "")
        cap = c.get("capacity", "")
        cap = re.sub(r"(\d)\s*\.\s*(\d)", r"\1.\2", cap)
        # a capacity wrapped inside its cell ('2351000.0' / '0 CASES') comes back as '2351000.0 0 CASES'
        m = re.match(r"^(-?\d[\d,. ]*?\d|\d)(?:\s+|$)(\D.*)?$", cap)
        if m:
            r["capacity"], r["unit"] = re.sub(r"\s+", "", m.group(1)), (m.group(2) or "").strip()
        else:
            r["unit"] = cap
        r["iem_no"], r["iem_date"] = split_iem_raw(r.pop("_iem", ""))
        for k in ("memo_no", "memo_date", "production_date", "investment_cr", "employment"):
            if c.get(k):
                r[k] = c[k]
    return out


def detect(text):
    head = text[:4000]
    if re.search(r"Filed From|Acknowledged From|S\.No\s+Name of Undertaking", text[:30000]):
        return "legacy"
    if "Name Of Undertaking" in head or "Production Commenced" in head:
        return "partb-table"
    if "Place(Tehsil)" in text[:20000] or ("DETAILED BREAK-UP" in head.upper() and "STATE WISE" not in head.upper()):
        return "breakup"
    if "STATE WISE" in head.upper():
        return "statewise"
    return "unknown"


PARSERS = {"legacy": parse_legacy, "statewise": parse_statewise, "breakup": parse_breakup2019,
           "partb-table": parse_partb_table}


def parse_file(path, pdf_index=None):
    m = NAME_RE.search(path.name)
    if not m:
        return [], {"file": path.name, "layout": "unnamed", "records": 0}
    fr, to, part, doc = m.groups()
    text = path.read_text(encoding="utf-8", errors="replace")
    layout = detect(text)
    pdf = (pdf_index or {}).get(path.stem)
    try:
        recs = []
        if pdf:
            first, second = (parse_pdf_words, parse_pdf_tables) if layout == "legacy" else (parse_pdf_tables, parse_pdf_words)
            # some 2018 Part B lists carry the legacy title over a ruled table: try the other reader
            recs = first(pdf, part) or second(pdf, part)
            if recs:
                layout = recs[0]["layout"]
        md_layout = detect(text)
        try:
            md_recs = PARSERS[md_layout](text, part) if md_layout in PARSERS else []
        except Exception:  # the .md reading is only a cross-check here
            md_recs = [] if recs else None
            if md_recs is None:
                raise
        # a table whose rows find_tables() merged (Dec 2021) yields far fewer records
        # than the text does; keep whichever reading found the list's records
        if len(recs) < 0.5 * len(md_recs):
            recs, layout = md_recs, md_layout
    except Exception as e:  # one bad file must not stop the run; it shows up in parse_report.md
        print(f"  ! {path.name}: {type(e).__name__}: {e}", file=sys.stderr)
        recs, layout = [], layout + " (error)"
    for r in recs:
        r.update({"part": part, "period_from": fr, "period_to": to, "doc_id": doc, "source_file": path.name})
        for k in FIELDS:
            r.setdefault(k, "")
            if isinstance(r[k], str):
                r[k] = re.sub(r"\s+", " ", r[k]).strip()
    serials = [int(r["serial"]) for r in recs if str(r["serial"]).isdigit()]
    info = {"file": path.name, "part": part, "period": f"{fr}..{to}", "layout": layout, "records": len(recs),
            "max_serial": max(serials) if serials else 0,
            "missing_company": sum(1 for r in recs if not r["company"]),
            "missing_item": sum(1 for r in recs if not r["item"]),
            "missing_state": sum(1 for r in recs if not r["state"]),
            "missing_iem_no": sum(1 for r in recs if not r["iem_no"])}
    return recs, info


def num_year(no, date):
    """(number, year) key: '911/N/SIA/IMO/2022' -> (911, 2022); 'IEM NO.823/20 19' -> (823, 2019);
    '1122' + '13/03/1996' -> (1122, 1996)."""
    s = re.sub(r"\s+", "", no or "")
    s = re.sub(r"^(IEM)?(NO)?[.:]*", "", s, flags=re.I)
    m = re.match(r"(\d+)", s)
    if not m:
        return None
    y = re.search(r"/(\d{4})$", s) or re.search(r"(\d{4})\s*$", date or "")
    return (int(m.group(1)), int(y.group(1))) if y else None


def dedupe(recs):
    """Monthly and financial-year lists overlap, and a few months were posted twice
    under different document ids: keep the first copy of each line item."""
    seen, out = set(), []
    for r in recs:
        k = (r["part"], r["iem_no"], r["iem_date"], r["memo_no"], re.sub(r"\W", "", r["company"].upper())[:25],
             re.sub(r"\W", "", r["item"].upper())[:25])
        if k in seen:
            continue
        seen.add(k); out.append(r)
    return out


def pdate(s):
    m = re.search(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})", s or "")
    if not m:
        return None
    try:
        import datetime
        return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


SUFFIX = re.compile(r"\b(PVT|PRIVATE|LTD|LIMITED|CO|COMPANY|THE|M/S|INDIA|P|L|INC|LLP|UNIT\b.*)\b")


def norm_company(s):
    s = re.sub(r"[^A-Z0-9 ]", " ", (s or "").upper())
    return re.sub(r"\s+", "", SUFFIX.sub(" ", s))


def match_parts(recs):
    """Part B (production started) lines cite the Part A memorandum they implement
    ('Memorandum No.: 1122 Date: 13/03/1996', or the Part-A No/Date columns).
    Mark every Part A line whose (number, year) appears in a Part B line; failing
    that, a Part B line from the same company (name without PVT/LTD etc.) dated
    after the filing counts as a weaker, name-only match."""
    b_by, b_name = {}, {}
    for r in recs:
        if r["part"] != "B":
            continue
        k = num_year(r["memo_no"], r["memo_date"])
        if k:
            b_by.setdefault(k, r)
    a_keys = {num_year(r["iem_no"], r["iem_date"]) for r in recs if r["part"] == "A"}
    for r in recs:
        # name-only matching uses just the Part B lines whose cited memorandum is
        # not in the Part A lists; the rest already belong to a numbered filing
        n = norm_company(r["company"])
        if r["part"] == "B" and len(n) >= 6 and num_year(r["memo_no"], r["memo_date"]) not in a_keys:
            b_name.setdefault(n, []).append(r)
    for r in recs:
        if r["part"] == "A":
            b, how = b_by.get(num_year(r["iem_no"], r["iem_date"])), "memo"
            ad = pdate(r["iem_date"]) or pdate(r["period_from"][8:10] + "/" + r["period_from"][5:7] + "/" + r["period_from"][:4])
            if not b and ad:
                later = [x for x in b_name.get(norm_company(r["company"]), [])
                         if (pdate(x["production_date"]) or pdate(x["iem_date"]) or ad) >= ad]
                b, how = (later[0], "name") if later else (None, "")
            r["in_part_b"] = how if b else "no"
            r["b_production_date"] = (b["production_date"] or b["iem_date"]) if b else ""
            r["b_doc_id"] = b["doc_id"] if b else ""
            bd = pdate(r["b_production_date"])
            r["lag_years"] = f"{(bd - ad).days / 365.25:.1f}" if b and bd and ad else ""
        else:
            k = num_year(r["memo_no"], r["memo_date"])
            r["a_in_lists"] = "yes" if k in a_keys else "no"
    return recs


def cohort_table(recs):
    """Per filing year: distinct Part A memoranda, how many turn up in a later
    Part B list, and after how long."""
    iems = {}
    for r in recs:
        if r["part"] != "A":
            continue
        k = num_year(r["iem_no"], r["iem_date"]) or (r["doc_id"], r["serial"], r["company"])
        prev = iems.get(k)
        if not prev or (prev["in_part_b"] == "no" and r["in_part_b"] != "no"):
            iems[k] = r
    rows = defaultdict(lambda: Counter())
    lags = defaultdict(list)
    for r in iems.values():
        d = pdate(r["iem_date"])
        y = d.year if d else int(r["period_from"][:4])
        c = rows[y]
        c["filed"] += 1
        c[r["in_part_b"]] += 1
        if r["lag_years"]:
            lg = max(0.0, float(r["lag_years"]))
            lags[y].append(lg)
            c["lag" + (str(int(lg)) if lg < 5 else "5+")] += 1
    out = []
    for y in sorted(rows):
        c = rows[y]
        found = c["memo"] + c["name"]
        ls = sorted(lags[y])
        out.append({"year": y, "filed": c["filed"], "in_b_memo": c["memo"], "in_b_name_only": c["name"],
                    "in_b_total": found, "pct_in_b": f"{100 * found / c['filed']:.1f}" if c["filed"] else "",
                    "median_lag_years": f"{ls[len(ls) // 2]:.1f}" if ls else "",
                    **{f"lag_{k}": c["lag" + k] for k in ("0", "1", "2", "3", "4", "5+")}})
    return out


def write_web(all_recs, out, cohort=None):
    """Compact column-wise JSON for iem_search.html: repeated strings (state,
    district, unit, file) are stored once in a lookup table."""
    cols = ["part", "company", "district", "state", "location", "item", "capacity", "unit", "iem_no", "iem_date",
            "memo_no", "memo_date", "production_date", "proposal_type", "in_part_b", "b_production_date",
            "lag_years", "period_from", "doc_id"]
    dict_cols = {"part", "district", "state", "unit", "proposal_type", "in_part_b", "period_from", "doc_id"}
    data, lookups = {c: [] for c in cols}, {c: {} for c in dict_cols}
    for r in all_recs:
        for c in cols:
            v = r.get(c, "")
            if c in dict_cols:
                v = lookups[c].setdefault(v, len(lookups[c]))
            data[c].append(v)
    payload = {"cols": cols, "lookups": {c: list(d) for c, d in lookups.items()}, "data": data,
               "n": len(all_recs), "cohort": cohort or []}
    (out / "iem_web.json").write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                                      encoding="utf-8")


def write_cohort(rows, all_recs, out):
    cols = list(rows[0]) if rows else []
    with open(out / "iem_partA_to_partB_by_year.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(rows)
    md = ["# Did Part A filings reach Part B?", "",
          "One row per filing year: distinct Part A memoranda, and how many later appear in a DPIIT Part B",
          "(production commenced) list. `memo` = the Part B line cites this memorandum's number and year;",
          "`name only` = a Part B line from the same company, dated after the filing, with no number match.",
          "Recent years are right-censored: the Part B lists stop in 2024, so late filings had little time.", "",
          "| Year | Filed | In B (memo) | In B (name only) | % in B | Median lag (yrs) | <1 yr | 1 | 2 | 3 | 4 | 5+ |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['year']} | {r['filed']} | {r['in_b_memo']} | {r['in_b_name_only']} | {r['pct_in_b']} | "
                  f"{r['median_lag_years']} | {r['lag_0']} | {r['lag_1']} | {r['lag_2']} | {r['lag_3']} | "
                  f"{r['lag_4']} | {r['lag_5+']} |")
    (out / "iem_partA_to_partB_by_year.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    pend = [r for r in all_recs if r["part"] == "A" and r["in_part_b"] == "no"]
    with open(out / "iem_partA_not_in_partB.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader(); w.writerows(pend)


def write_outputs(all_recs, infos, out):
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "iem_records.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader(); w.writerows(all_recs)
    by = defaultdict(list)
    for r in all_recs:
        by[(r["part"], r["period_from"][:7], r["period_to"][:7])].append(r)
    for (part, ym, ym2), rs in by.items():
        d = out / "md" / f"Part{part}"
        d.mkdir(parents=True, exist_ok=True)
        name = ym if ym == ym2 else f"{ym}_to_{ym2}"
        title = "filed (Part A)" if part == "A" else "implemented (Part B)"
        lines = [f"# IEMs {title}, {ym if ym == ym2 else ym + ' to ' + ym2}", "",
                 f"Source: DPIIT monthly list, document {', '.join(sorted({r['doc_id'] for r in rs}))}. "
                 f"{len(rs)} records, parsed by tools/iem_records.py.", "",
                 "| # | Company | District | State | Item | Capacity | Unit | IEM no. | Date | "
                 + ("Part B found |" if part == "A" else "Production from |"),
                 "|---|---|---|---|---|---|---|---|---|---|"]
        for r in rs:
            cells = [r["serial"], r["company"], r["district"], r["state"], r["item"], r["capacity"], r["unit"],
                     r["iem_no"] or r["memo_no"], r["iem_date"] or r["production_date"],
                     ({"memo": "yes", "name": "name match", "no": "no"}.get(r.get("in_part_b"), "")
                      + (f" ({r['b_production_date']})" if r.get("b_production_date") else ""))
                     if part == "A" else r["production_date"]]
            lines.append("| " + " | ".join(str(c).replace("|", "/") for c in cells) + " |")
        (d / f"{name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    rep = ["# IEM parse report", "", f"{len(all_recs)} records from {len(infos)} files.", "",
           "Layouts: " + ", ".join(f"{k} {v}" for k, v in Counter(i['layout'] for i in infos).items()), "",
           "Check: `records` should equal `max_serial` (legacy Part A restarts serials per state, so there it "
           "may exceed it). Rows with gaps are listed first.", "",
           "| File | Layout | Records | Max serial | No company | No item | No state | No IEM no. |",
           "|---|---|---|---|---|---|---|---|"]
    infos.sort(key=lambda i: (i["records"] >= i["max_serial"] and i["records"] > 0, i["file"]))
    for i in infos:
        rep.append(f"| {i['file']} | {i['layout']} | {i['records']} | {i.get('max_serial', 0)} | "
                   f"{i.get('missing_company', 0)} | {i.get('missing_item', 0)} | {i.get('missing_state', 0)} | "
                   f"{i.get('missing_iem_no', 0)} |")
    (out / "parse_report.md").write_text("\n".join(rep) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md-dir", required=True, help="folder holding the PartA/PartB .md conversions (searched recursively)")
    ap.add_argument("--pdf-dir", help="folder holding the source PDFs (searched recursively); table-era files are "
                    "then read from the PDF's ruled tables instead of the .md text")
    ap.add_argument("--out", default=str(pathlib.Path(__file__).resolve().parent.parent / "data" / "iem"))
    args = ap.parse_args()
    files = sorted(p for p in pathlib.Path(args.md_dir).expanduser().rglob("*.md") if NAME_RE.search(p.name))
    if not files:
        sys.exit(f"no IEM .md files found under {args.md_dir}")
    pdf_index = {}
    if args.pdf_dir:
        pdf_index = {p.stem: p for p in pathlib.Path(args.pdf_dir).expanduser().rglob("*.pdf")}
    all_recs, infos = [], []
    for p in files:
        recs, info = parse_file(p, pdf_index)
        all_recs += recs; infos.append(info)
    n_raw = len(all_recs)
    all_recs = match_parts(dedupe(all_recs))
    for r in all_recs:
        for k in FIELDS:
            r.setdefault(k, "")
    write_outputs(all_recs, infos, pathlib.Path(args.out))
    out = pathlib.Path(args.out)
    cohort = cohort_table(all_recs)
    write_web(all_recs, out, cohort)
    write_cohort(cohort, all_recs, out)
    page = pathlib.Path(__file__).resolve().parent / "iem_search.html"
    if page.exists():
        # the template is the page body; give the standalone copy its own document skeleton
        (out / "index.html").write_text(
            '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
            + page.read_text(encoding="utf-8") + "\n</body>\n</html>\n", encoding="utf-8")
    a = [r for r in all_recs if r["part"] == "A"]
    print(f"{n_raw} lines parsed, {len(all_recs)} after removing duplicates, from {len(files)} files -> {args.out}")
    print(f"Part A lines: {len(a)}; found in a Part B list: {sum(r['in_part_b'] == 'memo' for r in a)} by "
          f"memorandum number, {sum(r['in_part_b'] == 'name' for r in a)} by company name only")
    print(Counter(i["layout"] for i in infos))


if __name__ == "__main__":
    main()
