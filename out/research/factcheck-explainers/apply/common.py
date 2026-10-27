"""Shared helpers for the 27 Oct 2026 fact-check corrections (groups C and D)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);'
        'padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 27 October 2026.</b> {}</div>\n')


def load(slug):
    return (ROOT / "posts" / f"{slug}.html").read_text(encoding="utf-8")


def rep(t, old, new, count=1):
    n = t.count(old)
    assert n == count, f"expected {count} of {old[:80]!r}, found {n}"
    return t.replace(old, new)


def insert_note(t, text):
    h = max(t.find("<h1"), 0)
    a = t.find('<div class="gb-h2"', h)
    if a < 0:
        a = t.index("<h2", h)
    for m in re.finditer(r'<div class="warn"', t[h:a]):
        s = h + m.start()
        if re.search(r"<b>Update(d)?[ ,]", t[s:s + 400]):
            a = s
            break
    return t[:a] + NOTE.format(text) + t[a:]


def save(slug, t):
    out = ROOT / "out" / f"update-2026-10-27-{slug}.html"
    out.write_text(t, encoding="utf-8")
    print("wrote", out.name, len(t))
