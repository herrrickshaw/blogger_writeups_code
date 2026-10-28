"""Helpers for the 28 Oct 2026 gazette-verification updates (batch 3)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
SRC = ("read in the Gazette of India&rsquo;s own text via the SansadSaar index of the archive.org Gazette of India collection")
NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;'
        'border-radius:4px"><b>Updated 28 October 2026.</b> {}</div>\n')


def load(slug):
    return (ROOT / "posts" / f"{slug}.html").read_text(encoding="utf-8")


def rep(t, old, new, count=1):
    n = t.count(old)
    assert n == count, f"expected {count} of {old[:90]!r}, found {n}"
    return t.replace(old, new)


def insert_note(t, text):
    h = max(t.find("<h1"), 0)
    a = t.find('<div class="gb-h2"', h)
    b = t.find('<h2', h)
    cands = [x for x in (a, b) if x >= 0]
    a = min(cands)
    for m in re.finditer(r'<div class="warn"', t[h:a]):
        s = h + m.start()
        if re.search(r"<b>Update(d)?[ ,]", t[s:s + 400]):
            a = s
            break
    return t[:a] + NOTE.format(text) + t[a:]


def save(slug, t):
    out = ROOT / "out" / f"update-2026-10-28-{slug}.html"
    out.write_text(t, encoding="utf-8")
    print("wrote", out.name, len(t))

# PM E-DRIVE notification chain, Ministry of Heavy Industries (Gazette of India, Extraordinary)
PMED = ("S.O. 4259(E) of 29 September 2024 (CG-DL-E-30092024-257594), which notified the scheme; S.O. 3626(E) of 7 August 2025 "
        "(CG-DL-E-07082025-265287), which extended it to 31 March 2028 within &#8377;10,900 crore but kept 31 March 2026 for e-2Ws and e-3Ws; "
        "S.O. 1617(E) of 27 March 2026 (CG-DL-E-27032026-271345), which moved the e-2W end date to 31 July 2026 with &#8377;1,772 crore, "
        "kept e-rickshaws and e-carts to 31 March 2028 and recorded the L5 e-3W segment closed on 26 December 2025; S.O. 3191(E) of 17 June 2026 "
        "(CG-DL-E-17062026-273533), which added e-ambulances; and S.O. 4424(E) of 10 August 2026 (CG-DL-E-10082026-275344), which raised the outlay "
        "to &#8377;11,900 crore for 1 April 2024 to 31 March 2028, extended the e-2W incentive (&#8377;2,500 a kWh, capped at &#8377;5,000) to "
        "31 March 2028 with &#8377;2,767 crore, and set 31 December 2027 as the last date for claims")
