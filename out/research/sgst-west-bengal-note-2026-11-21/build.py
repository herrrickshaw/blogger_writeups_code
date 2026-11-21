"""Update of 21 November 2026 to the published post 'SGST reimbursement: 14 states offer it to investors as a subsidy, not a GST refund'
(slug fourteen-states-reimburse-investors, version 2.0.0 on the blog): West Bengal is no longer an exception.
Build from the repo root:  python3 out/research/sgst-west-bengal-note-2026-11-21/build.py            (writes out/update-2026-11-21-fourteen-states-reimburse-investors.html)
                           python3 out/research/sgst-west-bengal-note-2026-11-21/build.py --check    (arithmetic and asserts only)
posts/ is read, never written (CLAUDE.md rule 1). The output is the published post with one dated update block inserted above the 7 November block and one sentence added to the
sources paragraph; the builder then removes both insertions and asserts that what is left is byte-identical to posts/, so the original text is provably unchanged.
Sources: the West Bengal Industrial Development Corporation launch booklet for the Investment Promotion Policy, 2026 (official; text excerpts), the Kolkata Gazette text of the 2025 Act
(official copy on sarthac.gov.in; excerpt), KPMG Flash News 6 Nov 2026, Khaitan & Co note of 18 Nov 2026, Business Standard 5 Nov 2026, The Hindu 6 Nov 2026, Fox Mandal 30 Apr 2025 and
Indian Express 16 Sep 2025 (secondary). The Policy and the Scheme themselves were not found; the booklet says they prevail over it."""
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "posts/fourteen-states-reimburse-investors.html"
META = ROOT / "meta/fourteen-states-reimburse-investors.json"
OUT = ROOT / "out/update-2026-11-21-fourteen-states-reimburse-investors.html"
STEPS = 6


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
step(1, "source post matches the snapshot sidecar")
orig = SRC.read_text(encoding="utf-8")
meta = json.loads(META.read_text())
assert hashlib.sha256(orig.encode()).hexdigest() == meta["sha256"], "posts/ file differs from its sidecar"
assert len(orig) == meta["bytes"]                                    # the sidecar's "bytes" is the character count
BLOCK_ANCHOR = '<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 7 November 2026.</b>'
SRC_ANCHOR = "(search-result text; the drafts themselves were not opened).</p>"
assert orig.count(BLOCK_ANCHOR) == 1 and orig.count(SRC_ANCHOR) == 1
assert "Updated 21 November 2026" not in orig and "Update of 21 November 2026" not in orig
FOURTEEN = ["Tamil Nadu", "Rajasthan", "Punjab", "Odisha", "Maharashtra", "Telangana", "Andhra Pradesh", "Madhya Pradesh", "Haryana", "Chhattisgarh", "Jharkhand", "Himachal Pradesh", "Assam", "Bihar"]
assert len(FOURTEEN) == 14 and len(set(FOURTEEN)) == 14 and "West Bengal" not in FOURTEEN        # the post's own list of fourteen
assert "Karnataka and West Bengal are the clean exceptions" in orig and "Gazette Bill No. 5 of 2025" in orig       # the two statements this note corrects or qualifies

step(2, "dates and weekday checks")
for d, wd in [(D(2025, 4, 2), "Wednesday"), (D(2025, 11, 7), "Friday"), (D(2026, 5, 9), "Saturday"), (D(2026, 11, 5), "Thursday"), (D(2026, 11, 18), "Wednesday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 5, 9) - D(2025, 4, 2)).days == 402                   # from the Act's gazette to the date the new policy is deemed in force
assert (D(2026, 11, 5) - D(2026, 5, 9)).days == 180                  # deemed in force 180 days before it was unveiled
assert 14 + 1 == 15

step(3, "ceilings and the booklet's worked example")
EX_FCI = 200                                                         # Rs crore of plant and machinery, the booklet's example
assert EX_FCI * 120 / 100 == 240 and EX_FCI * 20 / 100 == 40 and 240 / 40 == 6.0
assert 100 / 15 < 10 and 120 / 20 == 6.0                             # the ceiling can be drawn in 6.7 or 6 years at the annual limits, inside the 10-year window
assert 5_000 * 10 == 50_000                                          # the estimated backlog is ten times the Budget provision (Business Standard, 5 and 12 November 2026)
if "--check" in sys.argv:
    print("consistency checks passed (sidecar hash, anchors, the post's own list of fourteen, dates, ceilings)", flush=True)
    sys.exit(0)

P = '<p style="margin:.7em 0">'
UL = '<ul style="margin:.4em 0 .8em;padding-left:1.3em">'

step(4, "writing the update block")
block = (
    '<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
    + P + "<b>Updated 21 November 2026.</b> West Bengal is no longer an exception. The West Bengal Investment Promotion Policy, 2026, deemed in force from 9 May 2026 and unveiled on Thursday "
    "5 November, gives manufacturing units SGST-linked assistance of 100% of net SGST for up to 10 years. Service units get 100% of net SGST for 5 years, up to Rs 10 crore a year.</p>"
    + P + "That makes West Bengal a fifteenth state in this comparison, so the count of fourteen, the title and the paragraph below on states that &ldquo;don&rsquo;t play this game&rdquo; are out of date for West Bengal.</p>"
    + P + "<b>How the 100% works.</b></p>"
    + UL
    + "<li>Net SGST is the SGST paid in cash after input tax credit. Tax discharged with IGST credit, tax under dispute and tax later refunded do not count, so a unit that buys mostly from other states receives less.</li>"
    "<li>The 100% sits inside a ceiling on all assistance together: 100% of Eligible FCI for a regular unit, 110% for a thrust-sector unit or a unit in a priority area, and 120% for both. Eligible FCI is audited spending on plant and machinery from 9 May 2026.</li>"
    "<li>A yearly limit of 15% of Eligible FCI, or 20% for a priority-area or thrust-sector unit, also applies. The booklet&rsquo;s own example is a Rs 200 crore thrust-sector unit in a priority area, which can receive up to Rs 240 crore in total and at most Rs 40 crore a year.</li>"
    "</ul>"
    + P + "<b>The 2025 revocation.</b> The post says West Bengal revoked every state industrial incentive scheme in 2025 by &ldquo;Gazette Bill No. 5 of 2025&rdquo;. The instrument is the Revocation of West Bengal Incentive Schemes and Obligations "
    "in the Nature of Grants and Incentives Act, 2025, published in the Kolkata Gazette, Extraordinary, on 2 April 2025; the bill number was not checked. A law-firm summary says its Schedule covers schemes from 1993 to 2021. "
    "The post&rsquo;s description otherwise stands.</p>"
    + P + "<b>What the new policy does not settle.</b> It applies to investment from 9 May 2026 and does not address claims under the withdrawn schemes, according to a Khaitan &amp; Co note of 18 November. "
    "Business Standard reports a backlog estimated at Rs 50,000 crore, ten times the Rs 5,000 crore set aside for 2026-27, and the Chief Minister saying the state may look at it when its finances improve.</p>"
    + P + "Several industrial houses challenged the Act in the Calcutta High Court, with a hearing set for 7 November 2025; the outcome was not found.</p>"
    + P + "<b>The post&rsquo;s question of announced against paid.</b> Terms are fixed at the Certificate of Intent and sanctioned assistance is to be paid from a dedicated Assured Incentive Fund, which the booklet presents as an answer to the 2025 withdrawal. "
    "A claim needs a Certificate of Eligibility, issued after production starts, so no payment under the policy had been reported by 21 November 2026.</p>"
    + P + "<b>Not re-checked.</b> Only West Bengal was updated here. The other rows, including Karnataka, the post&rsquo;s other exception, were not re-checked, and the policy text itself was not found: "
    "the booklet summarises it and says the Policy and the West Bengal Investment Promotion Scheme, 2026 prevail. <i>The original text below is unchanged.</i></p></div>\n"
)
src_add = (
    ' Update of 21 November 2026: West Bengal from the <a href="https://wbidc.com/assets/pdf/WBIP_2026_Launch_Booklet.pdf">launch booklet of the West Bengal Industrial Development Corporation</a> (official; text excerpts), '
    '<a href="https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2026/11/KPMG-Flash-News-West-Bengal-Investment-Promotion-Policy-2026.pdf">KPMG Flash News, 6 November 2026</a>, '
    '<a href="https://www.khaitanco.com/sites/default/files/2026-11/Ergo_West%20Bengal%20Investment%20Scheme_18%20November%202026.pdf">Khaitan &amp; Co, 18 November 2026</a>, '
    '<a href="https://www.business-standard.com/india-news/west-bengal-unveils-new-investment-policy-offers-up-to-120-assistance-126110502088_1.html">Business Standard, 5 November 2026</a>, '
    '<a href="https://sarthac.gov.in/view-act-rule-file?file_id=3475">the Act of 2 April 2025 as published in the Kolkata Gazette</a> (official copy; excerpt), '
    '<a href="https://foxmandal.in/news/bengal-to-scrap-old-industrial-incentives-eyes-modern-approach/">Fox Mandal, 30 April 2025</a> and '
    '<a href="https://indianexpress.com/article/cities/kolkata/industry-majors-calcutta-hc-challenge-bengal-decision-10253586">Indian Express, 16 September 2025</a> (secondary; search-result text, not read in full).'
)
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in (block + src_add).lower(), banned
assert not re.search(r"\b(we|our|you|your)\b", re.sub(r"<[^>]+>", " ", block + src_add).lower().replace("this blog", "")), "first or second person"

step(5, "assembling and proving the original is unchanged")
new = orig.replace(BLOCK_ANCHOR, block + BLOCK_ANCHOR).replace(SRC_ANCHOR, SRC_ANCHOR[:-4] + src_add + "</p>")
assert new.count("Updated 21 November 2026") == 1 and new.count("Update of 21 November 2026") == 1
restored = new.replace(block, "", 1).replace(src_add, "", 1)
assert restored == orig                                              # remove both insertions: byte-identical to the published post
OUT.write_text(new, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), f"({len(new) - len(orig)} characters added; original text unchanged)")
step(6, "complete")
