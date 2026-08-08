#!/usr/bin/env python3
"""Apply the house table standard to archived posts: units in the header, bordered.

    python3 tools/table_standard.py --file posts/x.html --out out/x.html
    python3 tools/table_standard.py --all --outdir out/tablefix   # dry run report
    python3 tools/table_standard.py --all --outdir out/tablefix --write

THE STANDARD (gs-table-v1)
    - Dark header band, white bold text, serif throughout.
    - Every cell bordered; the header does not wrap mid-word.
    - Numeric columns right-aligned and tabular-figured; first column left.
    - The unit appears ONCE, in the <th>. Cells carry bare numbers.
    - The table sits in an overflow-x:auto wrapper and is allowed to exceed it,
      so the scroller actually engages. (A width:100% table never can.)

WHAT THIS SCRIPT WILL NOT DO
    It refuses to touch a cell whose remainder, after the unit is removed, does
    not look like a number, a range, or a dash. That covers "$14.18bn" -> 14.18
    and "-30% to -40%" -> "-30 to -40", and it leaves "about $2bn, mostly gas"
    exactly as it found it. A hoist that mangles one value in three hundred is
    worse than no hoist, so the failures are reported rather than guessed at.
"""
import argparse
import glob
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from units_in_header import audit_table, text as celltext, _TABLE, _ROW, _CELL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MARKER = "gs-table-v1"

STYLE = """/*gs-table-v1 — scoped to .post-body, not .artx: several posts use other
  wrapper classes (.tblwrap among them) and an .artx-scoped rule silently did
  nothing on them. Verified on a canary post before the batch. */
.post-body .tw{overflow-x:auto;margin:1.1rem 0}
/* display:block makes the table its OWN scroller, so it works whether or not
   the post wrapped it in .tw — several posts use .tblwrap or nothing, and a
   width:auto table with no scroller pushes the whole page sideways. */
.post-body table{display:block;overflow-x:auto;max-width:100%;width:max-content;
 min-width:100%;border-collapse:collapse;font-size:.86rem}
.post-body thead th,.post-body tr:first-child th{background:#111;color:#fff;font-weight:700;
 text-align:right;vertical-align:bottom;padding:.6rem .7rem;border:1px solid #111;
 white-space:normal;overflow-wrap:normal;word-break:keep-all;min-width:5.5rem}
.post-body thead th:first-child,.post-body tr:first-child th:first-child{text-align:left}
.post-body td{border:1px solid #d9d9d9;padding:.5rem .7rem;text-align:right;
 font-variant-numeric:tabular-nums;white-space:nowrap;color:#111;background:#fff}
.post-body td:first-child{text-align:left;white-space:normal;min-width:8rem}
.post-body tbody tr:nth-child(even) td{background:#fafafa}
"""

# A value we are willing to strip a unit from.
# Allows "~5.3", "<2", "-30 to -40", "(1.2)". Approximation and comparison
# markers are meaning, not units, and stay in the cell.
_NUMLIKE = re.compile(
    r"^[\s(]*[~≈<>≤≥]?\s*[−–—+-]?[\d,.]+\s*"
    r"(?:to|–|—|-|and|&ndash;|&mdash;)?\s*[~≈]?\s*[−–—+-]?[\d,.]*[\s)%]*$"
)
# A trailing "/something" is part of the unit: "₹2,369/qtl" is rupees per quintal.
_PER = re.compile(r"/\s*[A-Za-z]{1,6}\.?$")


def strip_unit(value, units):
    """Remove every unit in `units` from a cell.

    Returns (bare_value, extra_suffix) or (None, None) if what is left does not
    look like a number. Stripping the whole unit signature at once is what makes
    "₹9,743 cr" work — one token at a time never gets there.
    """
    out = value
    per = ""
    m = _PER.search(out)
    if m:
        per = m.group(0).replace(" ", "")
        out = out[:m.start()]
    for u in sorted(units, key=len, reverse=True):
        out = re.sub(re.escape(u), " ", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip().strip(",").strip()
    if not out or not _NUMLIKE.match(out):
        return None, None
    return out, per


def hoist(table_html):
    """Return (new_table_html, moved, refused)."""
    viol, _ = audit_table(table_html)
    if not viol:
        return table_html, [], []
    rows = list(_ROW.finditer(table_html))
    if not rows:
        return table_html, [], []
    moved, refused = [], []
    new = table_html

    # Group violations by column so a column's whole unit signature is hoisted
    # together — "₹" and "crore" are one unit, not two findings.
    bycol = {}
    for col, head, unit, hits, total in viol:
        bycol.setdefault(col, [head, set()])[1].add(unit)

    for col, (head, unitset) in bycol.items():
        unit = " ".join(_pretty(u) for u in sorted(unitset, key=len, reverse=True))
        # Verify every body cell in the column can be stripped before changing any.
        plan = []
        ok = True
        for ri, r in enumerate(rows):
            cells = _CELL.findall(r.group(1))
            if ri == 0 and all(k.lower() == "th" for k, _ in cells):
                continue
            if len(cells) <= col:
                continue
            kind, raw = cells[col]
            v = celltext(raw)
            if not v or v in ("—", "-", "–", "n/a", "&mdash;"):
                continue
            if not any(u.lower() in v.lower() for u in unitset):
                continue
            stripped, per = strip_unit(v, unitset)
            if stripped is None:
                refused.append((head or f"col {col}", unit, v))
                ok = False
                break
            plan.append((raw, v, stripped, per))
        if not ok or not plan:
            continue

        pers = {p for _, _, _, p in plan if p}
        if len(pers) == 1:
            unit = unit + pers.pop()
        elif pers:
            continue          # mixed denominators cannot be hoisted
        for raw, before, after, _p in plan:
            new = new.replace(f">{raw}<", f">{after}<", 1)
        # Put the unit in the header, once.
        hdr_cells = _CELL.findall(rows[0].group(1))
        if len(hdr_cells) > col:
            k, hraw = hdr_cells[col]
            htxt = celltext(hraw)
            label = _pretty(unit)
            if label.lower() not in htxt.lower():
                new = new.replace(f">{hraw}<", f">{htxt}, {label}<", 1)
        moved.append((head or f"col {col}", unit, len(plan)))
    return new, moved, refused


_PRETTY = {"%": "%", "$": "US$", "₹": "₹", "&#8377;": "₹", "€": "€",
           "bn": "bn", "mn": "mn", "crore": "crore", "lakh": "lakh",
           "km": "km", "kg": "kg", "mmt": "MMT", "gwh": "GWh", "mw": "MW",
           "cr": "crore", "qtl": "quintal", "mt": "MT"}


def _pretty(u):
    return _PRETTY.get(u.lower(), u)


def ensure_style(doc):
    """Inject the standard table CSS once, at the end of the first <style>."""
    if MARKER in doc:
        return doc, False
    i = doc.find("</style>")
    if i < 0:
        return doc, False
    return doc[:i] + "\n" + STYLE + doc[i:], True


def process(path, write_to=None):
    doc = Path(path).read_text(encoding="utf-8", errors="replace")
    before_text = _visible(doc)
    total_moved, total_refused = [], []
    out = doc
    for m in list(_TABLE.finditer(doc)):
        new_tbl, moved, refused = hoist(m.group(1))
        total_moved += moved
        total_refused += refused
        if new_tbl != m.group(1):
            out = out.replace(m.group(1), new_tbl, 1)
    out, styled = ensure_style(out)

    # Guard: the only visible text that may change is inside tables.
    if _visible_nontable(out) != _visible_nontable(doc):
        return None, total_moved, total_refused, "REFUSED: non-table text changed"
    if write_to:
        Path(write_to).write_text(out, encoding="utf-8")
    return out, total_moved, total_refused, ("styled" if styled else "style already present")


def _visible(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def _visible_nontable(s):
    s = re.sub(r"<table[^>]*>.*?</table>", " TABLE ", s, flags=re.S | re.I)
    return _visible(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--outdir")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    files = [args.file] if args.file else sorted(glob.glob(str(ROOT / "posts" / "*.html")))
    if args.outdir:
        Path(args.outdir).mkdir(parents=True, exist_ok=True)

    tot_m = tot_r = changed = 0
    for f in files:
        dest = args.out or (str(Path(args.outdir) / Path(f).name) if args.outdir else None)
        out, moved, refused, note = process(f, dest if (args.write or args.out) else None)
        if out is None:
            print(f"  {Path(f).name[:46]:48} {note}")
            continue
        if moved or refused:
            print(f"  {Path(f).name[:46]:48} moved {len(moved):2}  refused {len(refused):2}  {note}")
            for h, u, n in moved:
                print(f"        + [{h[:30]}] '{u}' -> header ({n} cells)")
            for h, u, v in refused[:3]:
                print(f"        ! [{h[:30]}] '{u}' left alone, cell was {v[:40]!r}")
        tot_m += len(moved); tot_r += len(refused)
        if moved:
            changed += 1
    print(f"\n  posts changed {changed} | units hoisted {tot_m} | cells refused {tot_r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
