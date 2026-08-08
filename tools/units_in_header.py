#!/usr/bin/env python3
"""Enforce one house rule: a table's units live in its header, never in its cells.

    python3 tools/units_in_header.py                 # audit every archived post
    python3 tools/units_in_header.py --file X.html   # audit one file
    python3 tools/units_in_header.py --json out.json

Exit codes
    0  every table clean
    1  at least one table repeats a unit in its cells
    2  nothing to audit

THE RULE
    Put the unit once, in the <th>:        <th>Imports, US$ million</th>
    Leave the cells bare:                  <td>131.6</td>
    Not:                                   <td>$131.6 mn</td>

WHY
    A unit repeated down a column is noise in every row and a transcription risk
    in each one; it also breaks numeric alignment and makes a column impossible
    to sort or copy into a spreadsheet. This was the single most common defect
    found across this blog — up to 91% of cells in one table carried a redundant
    unit.

WHAT COUNTS AS A VIOLATION
    A unit-bearing token appearing in the CELLS of a column when it could sit in
    the header instead. The check is deliberately conservative: it only fires
    when the SAME unit appears in a majority of a column's non-empty cells, so a
    one-off "n/a" or a single footnoted value never trips it. A unit that varies
    row to row — a column of mixed currencies, say — is legitimate and is
    ignored, because it genuinely cannot be hoisted.
"""
import argparse
import collections
import glob
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Units this blog actually uses. Ordered longest-first so "US$ million" is
# matched before "US$".
UNITS = [
    "US$ million", "US$ mn", "US$ bn", "US$ billion", "₹ crore", "₹ lakh",
    "&#8377; crore", "&#8377; lakh", "percentage points", "basis points",
    "MMSCM", "MMBtu", "MMT", "GWh", "TWh", "kWh", "MWh", "MW", "GW",
    "tonnes", "tonne", "lakh", "crore", "million", "billion", "bn", "mn",
    "cr", "qtl", "MT", "ktpa", "mtpa",
    "US$", "USD", "EUR", "JPY", "KRW", "BRL", "INR", "₹", "&#8377;", "$", "€",
    "%", "pp", "bps", "kg", "km", "litres", "litre", "years", "yrs",
]
_UNIT_RE = re.compile(
    "(" + "|".join(re.escape(u) for u in UNITS) + ")", re.IGNORECASE
)
_TABLE = re.compile(r"<table[^>]*>(.*?)</table>", re.S | re.I)
_ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
_CELL = re.compile(r"<(t[dh])[^>]*>(.*?)</\1>", re.S | re.I)


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def units_in(s):
    """Units present in a string, normalised lowercase."""
    return {m.group(1).lower() for m in _UNIT_RE.finditer(s)}


def audit_table(tbl):
    """Return a list of (column_index, unit, hits, total) violations."""
    rows = []
    for r in _ROW.finditer(tbl):
        cells = [(k.lower(), text(v)) for k, v in _CELL.findall(r.group(1))]
        if cells:
            rows.append(cells)
    if len(rows) < 2:
        return [], 0

    header = rows[0] if all(k == "th" for k, _ in rows[0]) else None
    body = rows[1:] if header else rows
    ncol = max(len(r) for r in rows)
    out = []
    for c in range(ncol):
        col = [v for r in body if len(r) > c for _, v in [r[c]] if v and v not in ("—", "-", "–", "n/a")]
        if len(col) < 3:
            continue                      # too few values to call it a pattern
        # The rule is about NUMERIC columns. A prose column that happens to
        # mention rupees is not a repeated unit, and flagging it would train
        # the reader to ignore this check.
        words = [len(v.split()) for v in col]
        if sorted(words)[len(words) // 2] > 4:
            continue
        numericish = sum(1 for v in col if re.search(r"\d", v))
        if numericish / len(col) < 0.8:
            continue
        counts = collections.Counter()
        for v in col:
            for u in units_in(v):
                counts[u] += 1
        for unit, hits in counts.items():
            # Only a unit shared by MOST of the column can be hoisted. A unit
            # that varies row to row is real content, not repetition.
            if hits / len(col) >= 0.5:
                head = text(header[c][1]) if header and len(header) > c else ""
                if unit in units_in(head):
                    continue              # already in the header AND the cells
                out.append((c, head[:36], unit, hits, len(col)))
    return out, len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="audit a single HTML file")
    ap.add_argument("--json", metavar="PATH")
    args = ap.parse_args()

    files = [args.file] if args.file else sorted(glob.glob(str(ROOT / "posts" / "*.html")))
    if not files:
        print("nothing to audit", file=sys.stderr)
        return 2

    findings, tables, dirty = [], 0, 0
    for f in files:
        s = Path(f).read_text(encoding="utf-8", errors="replace")
        for i, m in enumerate(_TABLE.finditer(s), 1):
            tables += 1
            viol, nrows = audit_table(m.group(1))
            if viol:
                dirty += 1
                for c, head, unit, hits, total in viol:
                    findings.append({
                        "file": Path(f).name, "table": i, "column": c,
                        "header": head, "unit": unit,
                        "cells_with_unit": hits, "cells_in_column": total,
                        "share": round(hits / total, 2),
                    })

    print(f"files {len(files)}  tables {tables}  tables with a repeated unit {dirty}")
    print(f"violations {len(findings)}\n")
    for v in sorted(findings, key=lambda x: -x["share"]):
        print(f"  {v['file'][:44]:46} table {v['table']} col {v['column']} "
              f"[{v['header'] or 'no header'}]  {v['unit']!r} in "
              f"{v['cells_with_unit']}/{v['cells_in_column']} cells "
              f"({v['share']:.0%})")
    if args.json:
        Path(args.json).write_text(json.dumps(findings, indent=1), encoding="utf-8")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
