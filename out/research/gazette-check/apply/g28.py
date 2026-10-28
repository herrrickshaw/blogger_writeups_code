"""Helpers for the 28 Oct 2026 gazette-verification updates (batch 2)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);'
        'padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 28 October 2026.</b> {}</div>\n')
SRC = "read in the Gazette of India&rsquo;s own text via the SansadSaar index of the archive.org Gazette of India collection"


def load(slug):
    return (ROOT / "posts" / f"{slug}.html").read_text(encoding="utf-8")


def rep(t, old, new, count=1):
    n = t.count(old)
    assert n == count, f"expected {count} of {old[:90]!r}, found {n}"
    return t.replace(old, new)


def insert_note(t, text):
    h = t.find("<h1")
    end = min(x for x in (t.find('<div class="gb-h2"', h), t.find("<h2", h)) if x > 0)
    a = end
    for m in re.finditer(r'<div class="(warn|gb-card)"', t[h:end]):
        s = h + m.start()
        if re.search(r"<b>Update(d)?[ ,]", t[s:s + 400]):
            a = s
            break
    return t[:a] + NOTE.format(text) + t[a:]


def save(slug, t):
    out = ROOT / "out" / f"update-2026-10-28-{slug}.html"
    out.write_text(t, encoding="utf-8")
    print("wrote", out.name, len(t))
