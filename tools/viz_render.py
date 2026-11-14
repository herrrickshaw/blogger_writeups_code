#!/usr/bin/env python3
"""Render a visual-first edition from a small JSON spec: python3 tools/viz_render.py <slug>

The model decides the findings; code does everything mechanical. Input: out/viz/<slug>/spec.json
(created by tools/viz_new.py). Output: out/update-2026-11-15-<slug>.html.

spec = {
  "top": [["66%", " of petrol's energy per litre ..."], ...],            # 1 to 3 bullets: big number, then the rest
  "sections": [                                                          # 3 or 4
    {"h2": "Headline stating the finding",
     "chart": {...},                                                     # one of the chart shapes below
     "means": "One sentence.", "todo": "One sentence.",
     "numbers": {"table": "T3"}   # optional: the chart's data as a collapsed table, from the original's table T3
                                  # or {"head": [...], "rows": [[...]]} typed out
    }],
  "derived": {"190": "570/3", "7": "count: seven countries in the table"},   # numbers you computed, see viz_verify.py
  "fixes": "keep" | "drop"            # default keep: the original's fixes list is kept verbatim and open
  "tables": "all" | "none" | ["T2"]   # original tables kept as collapsed blocks; default all
}

Chart shapes (title states the takeaway, 90 characters or fewer):
  {"type":"bars","title":..,"sub":..,"source":..,"unit":" mg/kg","accent":"label"|["a","b"],"ref":[3,"what the marker is"],
   "from_zero":false,"vmax":null,
   "rows":[["label", 66, "note", "66%"], ["label",[93,95]], ["label",null]]
        # value: number, [low,high] range, or null (none); note and shown-text are optional; negative numbers draw left of zero
   OR "table":{"id":"T2","label":0,"value":2,"note":1,"rows":"top:10"|"0-9"|[0,3,5],"sort":"desc"|"asc"|null}}
        # rows come from the original's table by code: labels and shown values are the original's text, nothing is retyped
  {"type":"line","title":..,"series":{"A":[[2020,5],[2021,6]]},"accent":"A","unit":"%","sub":..,"source":..}   # 2+ points per series, real data only
  {"type":"waterfall","title":..,"start":["2024",100],"steps":[["Gain",12],["Loss",-5]],"end":"2025","unit":"%","accent":"Gain"}
  {"type":"flow","events":[["When","What happened"],["When","What",true]]}   # a sequence; true marks the accented event
"""
import html as _html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402
from viz_frame import body_links, caveat, fixes, related_box, sources_section, split, tables, update_notes  # noqa: E402

DATE = "2026-11-15"
esc = lambda s: _html.escape(str(s), quote=False)


def num(cell):
    """First number in a table cell as float (commas of any grouping removed), or None."""
    m = re.search(r"-?\d[\d,]*(?:\.\d+)?", cell.replace("−", "-").replace("–", "-") if re.match(r"^\s*[−-]\s*\d", cell) else cell)
    if not m:
        return None
    try:
        v = float(m.group(0).replace(",", ""))
    except ValueError:
        return None
    return -v if re.match(r"^\s*[−]\s*\d", cell) else v


def pick_rows(spec, n):
    r = spec.get("rows", "0-9")
    if isinstance(r, list):
        return r
    m = re.fullmatch(r"(\d+)-(\d+)", str(r))
    if m:
        return list(range(int(m.group(1)), min(int(m.group(2)), n - 1) + 1))
    m = re.fullmatch(r"top:(\d+)", str(r))
    if m:
        return list(range(min(int(m.group(1)), n)))
    raise ValueError(f"table rows must be a list, 'a-b' or 'top:N', got {r!r}")


def rows_from_table(spec, T):
    t = T.get(spec["id"])
    if not t:
        raise ValueError(f"no table {spec['id']} in the original (have {sorted(T)})")
    data = t["rows"]
    idx = pick_rows(spec, len(data))
    sig = lambda cell: re.sub(r"[\s~\u2248]+|about|roughly|approximately", " ", re.sub(r"[\d,.\u2212+-]+", "", cell.split("(")[0])).strip().lower()
    units = {sig(data[i][spec["value"]]) for i in idx}
    if len(units) > 1:
        raise ValueError(f"table {spec['id']} column {spec['value']} mixes units across the chosen rows {sorted(units)}: "
                         "bars on one scale must share a unit; pick another column or rows, or type the rows by hand in one unit")
    out = []
    for i in idx:
        row = data[i]
        v = num(row[spec["value"]])
        if v is None:
            raise ValueError(f"table {spec['id']} row {i} column {spec['value']} has no number: {row[spec['value']]!r}")
        out.append((esc(row[spec["label"]]), v, esc(row[spec["note"]]) if spec.get("note") is not None else "", esc(row[spec["value"]])))
    if spec.get("sort") in ("desc", "asc"):
        out.sort(key=lambda r: r[1], reverse=spec["sort"] == "desc")
    return out


def chart(c, T):
    t = c["type"]
    common = dict(sub=c.get("sub", ""), source=c.get("source", ""))
    if t == "bars":
        rows = rows_from_table(c["table"], T) if "table" in c else [tuple(None if x is None else (tuple(x) if isinstance(x, list) else x) for x in r) for r in c["rows"]]
        acc = c.get("accent")
        if isinstance(acc, list):
            acc = set(acc)
        return bars(c["title"], rows, unit=c.get("unit", ""), accent=acc, ref=tuple(c["ref"]) if c.get("ref") else None,
                    vmax=c.get("vmax"), from_zero=c.get("from_zero", False), **common)
    if t == "line":
        return line(c["title"], {k: [tuple(p) for p in v] for k, v in c["series"].items()}, accent=c.get("accent"),
                    unit=c.get("unit", ""), yfmt=(lambda v: f"{v:g}"), **common)
    if t == "waterfall":
        return waterfall(c["title"], tuple(c["start"]), [tuple(s) for s in c["steps"]], c["end"], unit=c.get("unit", ""),
                         accent=c.get("accent"), **common)
    if t == "flow":
        return flow([tuple(e) for e in c["events"]])
    raise ValueError(f"unknown chart type {t!r}")


def numbers_block(n, T):
    if "table" in n:
        t = T[n["table"]]
        return numbers([esc(h) for h in t["head"]], [[esc(c) for c in r] for r in t["rows"]], n.get("summary", "Show the numbers"))
    return numbers(n["head"], n["rows"], n.get("summary", "Show the numbers"))


def lint(spec):
    """Every spec-level problem at once (so a leaf fixes them in one edit): lengths, sentence counts, shapes."""
    errs, plain = [], lambda h: re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", h))).strip()
    one = lambda t: plain(t).endswith(".") and not re.search(r"\.\s+[A-Z]", plain(t))
    if not 1 <= len(spec.get("top", [])) <= 3:
        errs.append("top: needs 1 to 3 bullets of [big number, rest of sentence]")
    for i, b in enumerate(spec.get("top", []), 1):
        if len(b) != 2 or not str(b[0]).strip():
            errs.append(f"top[{i}]: must be [\"big number\", \" rest of the sentence.\"]")
    secs = spec.get("sections", [])
    if not 3 <= len(secs) <= 4:
        errs.append(f"sections: need 3 or 4, have {len(secs)}")
    for i, s in enumerate(secs, 1):
        h = plain(s.get("h2", ""))
        if not h or len(h) > 90:
            errs.append(f"section {i} h2 is {len(h)} characters (1 to 90): {h[:60]!r}")
        c = s.get("chart", {})
        if c.get("type") != "flow":
            t = plain(c.get("title", ""))
            if not t or len(t) > 90:
                errs.append(f"section {i} chart title is {len(t)} characters (1 to 90): {t[:60]!r}")
            if not re.search(r"\d", t) and len(t.split()) < 7:
                errs.append(f"section {i} chart title does not state a finding (add the number or make it a full statement): {t!r}")
        for k in ("means", "todo"):
            if not one(s.get(k, "")):
                errs.append(f"section {i} '{k}' must be exactly one sentence ending in a full stop (no '. Capital' inside): {plain(s.get(k, ''))[:80]!r}")
    return errs


def build(slug):
    d = ROOT / f"out/viz/{slug}"
    spec = json.loads((d / "spec.json").read_text(encoding="utf-8"))
    if not spec.get("top") or not spec.get("sections"):
        sys.exit("spec error: the spec has no 'top' bullets or no 'sections' yet; nothing was written")
    if (d / ".verified").exists() and "--force" not in sys.argv:
        sys.exit("spec error: this post already has a verified edition; pass --force to overwrite it")
    src = (ROOT / f"posts/{slug}.html").read_text(encoding="utf-8")
    fr = split(src)
    if not fr:
        sys.exit("the live post does not have the standard frame")
    problems = lint(spec)
    if problems:
        sys.exit("spec error (all problems at once):\n  - " + "\n  - ".join(problems))
    T = {t["id"]: t for t in tables(fr.body)}
    top = top_line([tuple(b) for b in spec["top"]])
    secs = []
    for s in spec["sections"]:
        body = chart(s["chart"], T) + (numbers_block(s["numbers"], T) if s.get("numbers") else "")
        secs.append(insight(s["h2"], body, s["means"], s["todo"], s.get("anchor", "")))
    extra = ""
    fx = fixes(fr.body) if spec.get("fixes", "keep") == "keep" else None
    if fx:
        extra += f'<h2 class="gb-h2" id="fixes">{esc(fx[0])}</h2>\n{fx[1]}\n'
    cv = caveat(fr.body)
    if cv:
        extra += f'<details class="xv-n"><summary>{esc(cv[0])}</summary>{cv[1]}</details>\n'
    for blk in spec.get("details", []):
        extra += f'<details class="xv-n"><summary>{blk["summary"]}</summary>{blk["html"]}</details>\n'
    keep = spec.get("tables", "all")
    used = {s["chart"]["table"]["id"] for s in spec["sections"] if "table" in s.get("chart", {}) and isinstance(s["chart"].get("table"), dict)}
    for t in T.values():
        if keep == "none" or (isinstance(keep, list) and t["id"] not in keep):
            continue
        title = t["title"] or t["id"]
        extra += numbers_block({"table": t["id"], "summary": f"Table: {title}"}, T)
    extra += sources_block(body_links(fr.body))
    rel = related_box(fr.body)          # only when the live post keeps it in the body (no clean footer): carried over verbatim
    if rel:
        extra += rel + "\n"
    src_sec = sources_section(fr.body)
    if src_sec:
        extra += f'<details class="xv-n"><summary>{esc(src_sec[0])}</summary>{src_sec[1]}</details>\n'

    note = (f'<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as charts; figures unchanged.</p>\n')
    mid = STYLE + top + fr.keep_front + update_notes(fr.body) + note + "".join(secs) + extra
    out = ROOT / f"out/update-{DATE}-{slug}.html"
    out.write_text(fr.head + fr.mid + mid + "\n" + fr.tail, encoding="utf-8")
    (d / "derived.json").write_text(json.dumps(spec.get("derived", {}), indent=1) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    try:
        print("wrote", build(sys.argv[1]).relative_to(ROOT))
    except (KeyError, ValueError) as e:
        sys.exit(f"spec error: {type(e).__name__}: {e}")
