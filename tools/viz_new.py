#!/usr/bin/env python3
"""Scaffold a visual-first edition for one post.

    python3 tools/viz_new.py <slug>

Writes out/viz/<slug>/outline.md (what the model needs to read: the argument and the figures, with the parts that
code keeps verbatim collapsed to one line and tables listed compactly with row numbers) and spec.json (empty).
Then fill spec.json (shape: top of tools/viz_render.py) and run  python3 tools/viz_go.py <slug>  until it prints PASS."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from viz_frame import body_links, caveat, fixes, outline, split, tables, update_notes  # noqa: E402

MAXROWS = 25


def table_text(t):
    n = len(t["rows"])
    cols = " | ".join(f"c{i} {h}" for i, h in enumerate(t["head"]))
    rows = list(enumerate(t["rows"]))
    if n > MAXROWS:
        rows = rows[:MAXROWS - 5] + [(None, None)] + rows[-4:]
    lines = [f'[{t["id"]} "{t["title"][:70]}" {n} rows; use rows by number in a chart "table" spec]', f"  cols: {cols}"]
    for i, r in rows:
        lines.append("  ..." if i is None else f"  r{i}: " + " | ".join(r))
    return "\n".join(lines)


def make_outline(fr):
    b = fr.body
    n = update_notes(b)
    if n:
        b = b.replace(n, '<p>[kept verbatim: dated update notes]</p>')
    fx = fixes(b)
    if fx:
        b = b.replace(fx[1], f"<p>[kept verbatim, open: {fx[0]}; {len(re.findall('<li', fx[1]))} items]</p>", 1)
    cv = caveat(b)
    if cv:
        b = b.replace(cv[1], f"<p>[kept verbatim, collapsed: {cv[0]}]</p>", 1)
    T = tables(fr.body)
    seen = iter(T)
    def sub(m):
        rows = len(re.findall(r"<tr\b", m.group(0)))
        if rows < 2:
            return m.group(0)
        return f"<p>@@{next(seen)['id']}@@</p>"
    b = re.sub(r"<table\b.*?</table>", sub, b, flags=re.S)
    text = outline(b)
    byid = {t["id"]: t for t in T}
    text = re.sub(r"@@(T\d+)@@", lambda m: "\n" + table_text(byid[m.group(1)]) + "\n", text)
    return text, T


def main(slug):
    fr = split((ROOT / f"posts/{slug}.html").read_text(encoding="utf-8"))
    if not fr:
        sys.exit(f"{slug}: not a standard frame")
    d = ROOT / f"out/viz/{slug}"
    d.mkdir(parents=True, exist_ok=True)
    text, T = make_outline(fr)
    (d / "outline.md").write_text(text + "\n", encoding="utf-8")
    if not (d / "spec.json").exists():
        (d / "spec.json").write_text(json.dumps({"top": [], "sections": [], "derived": {}}, indent=1) + "\n")
    print(f"out/viz/{slug}/outline.md {len(text.split()):,} words, {len(T)} tables, {len(body_links(fr.body))} body links kept by code")


if __name__ == "__main__":
    main(sys.argv[1])
