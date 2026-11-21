"""MAJOR revision of 21 November 2026 (first anniversary) to the published post 'India's labour codes: law since 21 November 2025, rules in about a third of states'
(slug indias-labour-codes-took-six-years-to, version 3.0.0 on the blog): new title, lead sentence, headline tile and chart, and a dated update block above the earlier ones.
Build from the repo root:  python3 out/research/labour-codes-update-2026-11-21/build.py            (writes out/update-2026-11-21-indias-labour-codes-took-six-years-to.html)
                           python3 out/research/labour-codes-update-2026-11-21/build.py --check    (arithmetic and asserts only)
posts/ is read, never written (CLAUDE.md rule 1). The output is the published post with exactly four replacements (title, lead sentence, tile, chart) and one inserted block. The builder
then undoes all five and asserts that the result is byte-identical to posts/, so nothing else in the post has moved. Version level: MAJOR (a headline figure and the title's claim changed).
Every count is from the tracker named beside it, or computed with an assert. No tracker is an official count; the state gazettes were not read.
Search excerpts only (none of these pages was read in full): Praans Consultech tracker (9 and 21 Nov 2026), ComplianceTalks tracker (reviewed 6 Nov, published 11 Nov), HR Calcy tracker
(30 Oct), KSMG tracker (6 Oct), Labour Codes Library (checked 1 Nov), Adullam Consulting (13 Nov), Sankhla Knowledge, Labour Code Advisor and Praans (Punjab),
Business Standard (20 Nov, page text fetched but only its opening paragraphs were returned)."""
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "posts/indias-labour-codes-took-six-years-to.html"
META = ROOT / "meta/indias-labour-codes-took-six-years-to.json"
OUT = ROOT / "out/update-2026-11-21-indias-labour-codes-took-six-years-to.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. the source post is the published one
step(1, "source post matches the snapshot sidecar")
orig = SRC.read_text(encoding="utf-8")
meta = json.loads(META.read_text())
assert hashlib.sha256(orig.encode()).hexdigest() == meta["sha256"], "posts/ file differs from its sidecar"
assert len(orig) == meta["bytes"]                                    # the sidecar's "bytes" is the character count; the sha256 above covers the UTF-8 bytes
ANCHOR = '<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 27 October 2026.</b>'
assert orig.count(ANCHOR) == 1                                      # insertion point: above the newest existing update block
assert "Updated 21 November 2026" not in orig

# ---- 2. dates
step(2, "dates and weekday checks")
for d, wd in [(D(2025, 11, 21), "Friday"), (D(2026, 5, 8), "Friday"), (D(2026, 9, 24), "Thursday"), (D(2026, 10, 31), "Saturday"), (D(2026, 11, 3), "Tuesday"),
              (D(2026, 11, 5), "Thursday"), (D(2026, 11, 8), "Sunday"), (D(2026, 11, 21), "Saturday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 11, 21) - D(2025, 11, 21)).days == 365               # first anniversary
assert (D(2026, 11, 21) - D(2026, 10, 31)).days == 21                # days since the Centre's target date
assert (D(2026, 10, 31) - D(2026, 9, 24)).days == 37                 # from the Labour Secretary's statement to the target
assert (D(2026, 5, 8) - D(2025, 11, 21)).days == 168                 # codes in force to Central Rules
assert D(2026, 5, 8).replace(month=11) == D(2026, 11, 8)             # six months after the Central Rules: the Form I update date given by ComplianceTalks (about 8 November)

# ---- 3. tracker counts: each must add up to its own total
step(3, "tracker totals and ranges")
TR = [  # name, date label, jurisdictions, all four, at least one, draft or none
    ("KSMG tracker", "reviewed 6 Oct", 36, 5, 11, 25),
    ("HR Calcy tracker", "30 Oct", 36, 6, 11, 25),
    ("ComplianceTalks tracker", "reviewed 6 Nov", 36, 6, 13, 23),
    ("Praans Consultech tracker", "9 Nov", 37, 7, 13, 24),
    ("Praans Consultech tracker", "21 Nov", 37, 7, 16, 21),
]
for n, d, tot, four, some, rest in TR:
    assert some + rest == tot, (n, d)                              # at least one code, plus none or draft only, is every jurisdiction
    assert four <= some, (n, d)
assert [t[3] for t in TR] == [5, 6, 6, 7, 7]
assert 6 + 5 == 11 and 6 + 7 == 13 and 7 + 6 == 13 and 7 + 9 == 16                  # all four plus some-but-not-all, as the trackers print them
assert 34 + 83 + 27 == 144 == 36 * 4                                # Labour Codes Library: rule sets (state and code pairs), 1 Nov
assert 28 + 8 == 36                                                 # 28 states and 8 union territories: the 36 of most trackers; Praans counts 37
ISF = (37, 6, 10)                                                   # Indian Staffing Federation via Business Standard, 20 Nov: by October, all four, 'around 10' at least one
ALL4 = [t[3] for t in TR] + [6, ISF[1]]                             # plus the Library's six and the ISF's six
ONE = [t[4] for t in TR] + [ISF[2]]
assert (min(ALL4), max(ALL4)) == (5, 7) and (min(ONE), max(ONE)) == (10, 16)
pct = lambda a, b: round(100 * a / b, 1)
SHARE_ALL4 = [pct(a, b) for a, b in [(5, 36), (6, 36), (6, 36), (7, 37), (7, 37), (6, 37)]]
SHARE_ONE = [pct(a, b) for a, b in [(11, 36), (11, 36), (13, 36), (13, 37), (16, 37), (10, 37)]]
assert (min(SHARE_ALL4), max(SHARE_ALL4)) == (13.9, 18.9)
assert (min(SHARE_ONE), max(SHARE_ONE)) == (27.0, 43.2)             # the old title's 'about a third' holds for at least one code, not for all four
# the share with no final rules under any code, from the same trackers: draft only, or none (ISF: 37 less about 10)
NONE = [pct(r, t) for _, _, t, _, _, r in TR] + [pct(37 - 10, 37)]
assert (min(NONE), max(NONE)) == (56.8, 73.0)                       # most jurisdictions have no final rules under any code: the chart title's claim
assert min(NONE) > 50

# ---- 4. the post's 9 July list of 11 states, against the later trackers
step(4, "the 9 July list of 11 against later trackers")
JULY = ["Madhya Pradesh", "Uttar Pradesh", "Gujarat", "Karnataka", "Haryana", "Uttarakhand", "Jharkhand", "Odisha", "Bihar", "Chhattisgarh", "Assam"]
DRAFT_LATER = ["Madhya Pradesh", "Karnataka", "Haryana", "Jharkhand", "Chhattisgarh", "Assam"]          # draft only: ComplianceTalks table, HR Calcy list
ALL4_LATER = ["Uttar Pradesh", "Gujarat", "Bihar"]                                                      # final under all four: ComplianceTalks, HR Calcy
PARTIAL_LATER = ["Uttarakhand"]                                                                         # final under some (two) codes: ComplianceTalks, HR Calcy
NOT_SEEN = ["Odisha"]                                                                                   # not among the final states in any later tracker excerpt read
assert len(JULY) == 11 and len(set(JULY)) == 11
assert sorted(DRAFT_LATER + ALL4_LATER + PARTIAL_LATER + NOT_SEEN) == sorted(JULY)
assert len(DRAFT_LATER) == 6 and len(ALL4_LATER) == 3
MARCH = ["Gujarat", "Arunachal Pradesh", "Haryana", "Madhya Pradesh", "Karnataka", "Maharashtra"]       # the post's March 2026 list of six
assert len(MARCH) == 6 and [m for m in MARCH if m in DRAFT_LATER + ["Maharashtra"]] == ["Haryana", "Madhya Pradesh", "Karnataka", "Maharashtra"]   # four of the six are draft in the later trackers (Maharashtra: one code final)

# ---- 5. central figures (Business Standard 20 Nov)
step(5, "central figures")
assert round(25_000 / 15_000, 4) == 1.6667 and f"{100 * (25_000 - 15_000) / 15_000:.1f}" == "66.7"        # EPFO wage ceiling Rs 15,000 to Rs 25,000

# ---- 6. the four replacements
step(6, "title, lead sentence, tile and chart")
TITLE_OLD = "India's labour codes: law since 21 November 2025, rules in about a third of states"
TITLE_NEW = "India's labour codes: final rules under all four in 5 to 7 of 36 or 37 states and UTs"
assert 55 <= len(TITLE_NEW) <= 90, len(TITLE_NEW)                   # headline style: at most 90 characters, plain, no idiom, no first or second person
assert not any(w in TITLE_NEW.lower().split() for w in ("you", "your", "we", "our"))
LEAD_OLD = "as of the most recent count, barely a third of India's states had notified their own."
LEAD_NEW = "as of November 2026, trackers count final state rules under all four codes in 5 to 7 of 36 or 37 states and union territories (UTs)."
TILE_OLD = '<div class="stat"><b>~11 of 28</b><span>states with final rules notified, per the most recent single-date tracker found</span></div>'
TILE_NEW = ('<div class="stat"><b>5&ndash;7 of 36&ndash;37</b><span>states and UTs with final state rules under all four codes, and 10&ndash;16 under at least one, '
            'per trackers read 6 Oct to 21 Nov 2026</span></div>')
m = re.search(r'<figure class="gb-figure" style="margin:1\.5rem 0 1\.75rem;text-align:center">\n<svg role="img".*?</figure>', orig, flags=re.S)
assert m and orig.count(m.group(0)) == 1 and "Nine Months In, Most States Aren't Done" in m.group(0)
FIG_OLD = m.group(0)
U = 390 / 36                                                        # pixels per jurisdiction: 36 fills the 390-pixel bar
w = lambda n: round(n * U, 1)
assert (w(36), w(10), w(16), w(5), w(7)) == (390.0, 108.3, 173.3, 54.2, 75.8)
LBL = "font-family=\"-apple-system,'Segoe UI',sans-serif\""
FIG_NEW = f'''<figure class="gb-figure" style="margin:1.5rem 0 1.75rem;text-align:center">
<svg role="img" aria-label="Bar chart: of 36 states and union territories, 10 to 16 have final rules under at least one labour code and 5 to 7 under all four" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto" viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, 'Times New Roman', serif">
<rect x="0" y="0" width="700" height="320" fill="#f8f9fa" />
<text x="30" y="34" font-size="19" font-weight="700" fill="#212529">A year in, most states and UTs have no final rules</text>
<text x="30" y="54" font-size="12.5" fill="#495057" {LBL}>36 states and union territories; range across the trackers read, 6 Oct to 21 Nov 2026</text>

<text x="240" y="96" font-size="13" fill="#212529" text-anchor="end" {LBL}>All states and UTs</text>
<rect x="250" y="80" width="{w(36)}" height="28" fill="#212529" />
<text x="647" y="99" font-size="13.5" fill="#212529" font-weight="700">36</text>
<text x="250" y="122" font-size="10.5" fill="#868e96" {LBL}>28 states and 8 union territories; one tracker counts 37</text>

<text x="240" y="166" font-size="13" fill="#212529" text-anchor="end" {LBL}>Final under at least one code</text>
<rect x="250" y="150" width="{w(16)}" height="28" fill="#6b3fa0" opacity="0.3" />
<rect x="250" y="150" width="{w(10)}" height="28" fill="#6b3fa0" opacity="0.55" />
<text x="{250 + w(16) + 7}" y="169" font-size="13.5" fill="#212529" font-weight="700">10&ndash;16</text>
<text x="250" y="192" font-size="10.5" fill="#868e96" {LBL}>27% to 43%; the lighter part is the spread between trackers</text>

<text x="240" y="236" font-size="13" fill="#212529" text-anchor="end" {LBL}>Final under all four codes</text>
<rect x="250" y="220" width="{w(7)}" height="28" fill="#6b3fa0" opacity="0.3" />
<rect x="250" y="220" width="{w(5)}" height="28" fill="#6b3fa0" />
<text x="{250 + w(7) + 7}" y="239" font-size="13.5" fill="#212529" font-weight="700">5&ndash;7</text>
<text x="250" y="262" font-size="10.5" fill="#868e96" {LBL}>14% to 19%</text>

<text x="30" y="300" font-size="10" fill="#868e96" {LBL}>Source: private trackers (KSMG, HR Calcy, ComplianceTalks, Praans, ISF); not an official count.</text>
</svg>
<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,'Segoe UI',sans-serif;margin-top:.5rem">One year after the codes came into force, trackers put final state rules under all four codes in 5 to 7 of 36 or 37 states and union territories, and under at least one code in 10 to 16. Between 57% and 73% have no final rules under any code.</figcaption>
</figure>'''
assert f"{250 + w(16) + 7:.1f}" == "430.3" and f"{250 + w(7) + 7:.1f}" == "332.8"            # label positions clear the bars; the right edge is 640
assert 250 + w(36) <= 640 and 250 + w(16) + 7 + 40 <= 700
REPL = [(TITLE_OLD, TITLE_NEW), (LEAD_OLD, LEAD_NEW), (TILE_OLD, TILE_NEW), (FIG_OLD, FIG_NEW)]
for a, b in REPL:
    assert orig.count(a) == 1, a[:60]
if "--check" in sys.argv:
    print("consistency checks passed (sidecar hash, dates, tracker totals and ranges, July list, central figures, replacements)", flush=True)
    sys.exit(0)

P = '<p style="margin:.7em 0">'
UL = '<ul style="margin:.4em 0 .8em;padding-left:1.3em">'


def li(*parts):
    return "<li>" + " ".join(parts) + "</li>"


step(7, "writing the update block")
counts = UL + "".join([
    li("<b>Labour Secretary, via Business Standard (24 Sep):</b> ten states with final rules, unnamed."),
    li("<b>KSMG (reviewed 6 Oct):</b> 36 jurisdictions, 5 with all four codes, 11 with at least one."),
    li("<b>HR Calcy (30 Oct):</b> 36, 6 with all four, 11 with at least one."),
    li("<b>Labour Codes Library (1 Nov):</b> 36, 6 with all four; by rule set, 34 of 144 final, 83 draft only, 27 none found."),
    li("<b>ComplianceTalks (reviewed 6 Nov):</b> 36, 6 with all four, 13 with at least one."),
    li("<b>Praans Consultech (9 Nov):</b> 37, 7 with all four, 13 with at least one."),
    li("<b>Praans Consultech (21 Nov):</b> 37, 7 with all four, 16 with at least one, 21 with none."),
    li("<b>Indian Staffing Federation, via Business Standard (20 Nov, data to October):</b> 37, 6 with all four, about 10 with at least one."),
]) + "</ul>"
dispute = UL + "".join([
    li("<b>Ladakh:</b> final under all four codes, August to September 2026 (HR Calcy, ComplianceTalks, KSMG); draft only, with April 2026 entries (Labour Codes Library, 1 Nov)."),
    li("<b>Lakshadweep:</b> all four final (Labour Codes Library); wages only (ComplianceTalks); three codes (HR Calcy, KSMG)."),
    li("<b>Mizoram:</b> all four final (Labour Codes Library); social security and OSH (HR Calcy); one code (KSMG)."),
    li("<b>Uttar Pradesh:</b> all four final, 31 Aug to 17 Sep 2026 (ComplianceTalks, HR Calcy, Adullam); three codes (KSMG, 6 Oct)."),
    li("<b>Punjab, OSH rules:</b> final, gazette of 3 Nov 2026 (Sankhla Knowledge, Labour Code Advisor); draft (Praans, verified 14 Nov)."),
    li("<b>Karnataka and Haryana:</b> final in a mid-2026 source and draft in an end-October source, both cited by Adullam."),
]) + "</ul>"

block = (
    '<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
    + P + "<b>Updated 21 November 2026, one year after the codes came into force.</b> The title, the lead sentence, the headline tile and the chart of this post were revised. "
    "The title read &lsquo;India&rsquo;s labour codes: law since 21 November 2025, rules in about a third of states&rsquo;; the tile read &lsquo;~11 of 28 states with final rules notified, "
    "per the most recent single-date tracker found&rsquo;; the lead said that &lsquo;barely a third of India&rsquo;s states&rsquo; had notified rules; and the chart showed 28, 17 and 11.</p>"
    + P + "Trackers read between 6 October and 21 November put 5 to 7 states and union territories at final rules under all four codes, and 10 to 16 at final rules under at least one, "
    "out of 36 or 37 jurisdictions. That is 14% to 19% for all four codes and 27% to 43% for at least one (computed), and 57% to 73% with none. "
    "The old title held for at least one code and not for all four.</p>"
    + P + "No tracker read is an official count, and none shows the Centre&rsquo;s 31 October target as met, 21 days after the date.</p>"
    + P + "<b>Counts by tracker.</b></p>" + counts
    + P + "<b>Correction to this post&rsquo;s own count.</b> The 9 July 2026 list of 11 states below does not match later trackers. Six of the 11 (Madhya Pradesh, Karnataka, Haryana, Jharkhand, "
    "Chhattisgarh and Assam) are draft only in the November trackers; Uttar Pradesh, Gujarat and Bihar are final under all four codes; Uttarakhand is final under two.</p>"
    + P + "Odisha does not appear as final in any later tracker read. Four of the six states in the March 2026 list (Haryana, Madhya Pradesh, Karnataka and Maharashtra) are also draft, or final under one code only. "
    "The text of this post below still gives the 9 July count and the Parliament-reply count of 17 as dated snapshots; both are superseded by the counts above. "
    "The trackers count 36 jurisdictions (28 states and 8 union territories), or 37, not 28.</p>"
    + P + "<b>Where trackers disagree on named states.</b></p>" + dispute
    + P + "<b>Since 22 October.</b> Punjab&rsquo;s Code on Wages and Social Security rules were notified on 31 October 2026 and published on 5 November, when they came into force. "
    "Maharashtra&rsquo;s Wage Rules also came into force on 5 November, with its other three codes still at draft.</p>"
    + P + "At the Centre, the new EPF scheme was notified in June, and in September the EPFO wage ceiling rose from Rs 15,000 to Rs 25,000 a month, up 66.7%, which Business Standard estimates brings "
    "5.1 million more workers under social security. Establishments registered under the earlier central laws had until about 8 November, six months after the Central Rules, to update their particulars on the Shram Suvidha portal.</p>"
    + P + "Where a state has no final rules, the Ministry&rsquo;s FAQ of 30 December 2025, as quoted by the Labour Codes Library, says the old rules continue to the extent they are in line with the codes; "
    "that is the Ministry&rsquo;s explanation, not the law.</p>"
    + P + "<b>What would fix the counting problem.</b></p>"
    "<ol style=\"margin:.4em 0 .8em;padding-left:1.3em\"><li>The Ministry of Labour and Employment should publish one dated list, by state and code, of final and draft rules with gazette references, updated at least monthly.</li>"
    "<li>The Ministry should say whether the 31 October target was met and name the ten states cited on 24 September.</li>"
    "<li>Each state labour department should publish final rules in its gazette with a stated commencement date and keep a code-wise status page on its website.</li>"
    "<li>The Ministry should notify the transitional position for jurisdictions without final rules, now set out only in an FAQ.</li></ol>"
    + P + "<i>These are proposals from this blog, not recommendations any agency has adopted.</i></p>"
    + P + "<b>Not established.</b> No official consolidated list was found; the state gazettes were not read, and every count above is from a private tracker or a news report. "
    "The ten states the Labour Secretary cited were not named. The reason Praans counts 37 jurisdictions and the others 36 was not found.</p>"
    + P + 'Sources: <a href="https://www.praansconsultech.com/labour-codes">Praans Consultech tracker</a>, <a href="https://compliancetalks.in/2026/11/11/labour-codes-state-rules-status-2026">ComplianceTalks</a>, '
    '<a href="https://www.hrcalcy.in/p/labour-code-state-rules-tracker.html">HR Calcy</a>, <a href="https://ksmg.co/explainers/labour-codes/labour-code-state-rules-tracker">KSMG</a>, '
    '<a href="https://labour-codes-by-vivek.github.io/states/">Labour Codes Library</a>, <a href="https://www.adullamcorp.com/en/board/hr-legal/28">Adullam Consulting</a>, '
    '<a href="https://www.business-standard.com/industry/news/labour-codes-first-year-marked-by-state-level-delays-regulatory-gaps-126112001298_1.html">Business Standard, 20 November 2026</a>, '
    '<a href="https://sankhlaco.com/library/punjab-code-on-wages-rules-2026-final">Sankhla Knowledge</a>, <a href="https://labourcodesadvisor.com/notifications/punjab">Labour Code Advisor</a>, '
    '<a href="https://www.praansconsultech.com/labour-codes/punjab/punjab-code-on-wages-rules-2026">Praans, Punjab</a>. All secondary; page text was not read in full. '
    "<i>Earlier updates follow. Apart from the title, lead sentence, tile and chart, the text of this post is unchanged.</i></p></div>\n"
)
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in (block + FIG_NEW + TILE_NEW + LEAD_NEW + TITLE_NEW).lower(), banned
assert not re.search(r"\b(we|our|you|your)\b", re.sub(r"<[^>]+>", " ", block + LEAD_NEW + TILE_NEW).lower().replace("this blog", "")), "first or second person"

step(8, "assembling and proving that nothing else changed")
new = orig
for a, b in REPL:
    new = new.replace(a, b, 1)
new = new.replace(ANCHOR, block + ANCHOR, 1)
assert new.count("Updated 21 November 2026") == 1
restored = new.replace(block, "", 1)
for a, b in reversed(REPL):
    assert restored.count(b) == 1, b[:60]
    restored = restored.replace(b, a, 1)
assert restored == orig                                              # undo all five edits: byte-identical to the published post
assert TITLE_OLD not in new and TILE_OLD not in new and LEAD_OLD not in new and "Nine Months In" not in new     # the old headline claims survive only as quoted history in the block
assert new.count(TITLE_NEW) == 1 and new.count(TILE_NEW) == 1 and new.count(LEAD_NEW) == 1
OUT.write_text(new, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), f"({len(new) - len(orig)} characters net; title, lead, tile and chart replaced; all else unchanged)")
step(9, "complete")
