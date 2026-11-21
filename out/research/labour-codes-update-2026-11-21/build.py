"""Update of 21 November 2026 (first anniversary) to the published post 'India's labour codes: law since 21 November 2025, rules in about a third of states'
(slug indias-labour-codes-took-six-years-to, version 3.0.0 on the blog).
Build from the repo root:  python3 out/research/labour-codes-update-2026-11-21/build.py            (writes out/update-2026-11-21-indias-labour-codes-took-six-years-to.html)
                           python3 out/research/labour-codes-update-2026-11-21/build.py --check    (arithmetic and asserts only)
posts/ is read, never written (CLAUDE.md rule 1). The output is the published post with one dated update block inserted above the earlier update blocks; the builder then removes the
block again and asserts that what is left is byte-identical to posts/, so the original text is provably unchanged. Same pattern as out/update-2026-10-27-*.html.
Every count below is from the tracker named beside it, or computed with an assert. No tracker is an official count; the state gazettes were not read.
Search excerpts only (none of these pages was read in full): Praans Consultech tracker (9 and 21 Nov 2026), ComplianceTalks tracker (reviewed 6 Nov, published 11 Nov), HR Calcy tracker
(30 Oct), KSMG tracker (6 Oct), Labour Codes Library (checked 1 Nov), Adullam Consulting (13 Nov), Sankhla Knowledge and Labour Code Advisor and TeamLease RegTech and Praans (Punjab),
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
STEPS = 7


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. the source post is the published one
step(1, "source post matches the snapshot sidecar")
orig = SRC.read_text()
meta = json.loads(META.read_text())
assert hashlib.sha256(orig.encode()).hexdigest() == meta["sha256"], "posts/ file differs from its sidecar"
assert len(orig) == meta["bytes"]                                   # the sidecar's "bytes" is the character count (23,596); the UTF-8 length is 23,598 and the sha256 above covers it
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
assert (min(SHARE_ONE), max(SHARE_ONE)) == (27.0, 43.2)             # 'about a third' (the post's title) holds for at least one code, not for all four

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
if "--check" in sys.argv:
    print("consistency checks passed (sidecar hash, dates, tracker totals and ranges, July list, central figures)", flush=True)
    sys.exit(0)


P = '<p style="margin:.7em 0">'
UL = '<ul style="margin:.4em 0 .8em;padding-left:1.3em">'


def li(*parts):
    return "<li>" + " ".join(parts) + "</li>"


step(6, "writing the update block")
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
    + P + "<b>Updated 21 November 2026, one year after the codes came into force.</b> "
    "Trackers read between 6 October and 21 November put 5 to 7 states and union territories at final rules under all four codes, and 10 to 16 at final rules under at least one, "
    "out of 36 or 37 jurisdictions.</p>"
    + P + "That is 14% to 19% for all four codes and 27% to 43% for at least one (computed). This post&rsquo;s title, &lsquo;rules in about a third of states&rsquo;, "
    "holds for at least one code and not for all four. No tracker read is an official count, and none shows the Centre&rsquo;s 31 October target as met, 21 days after the date.</p>"
    + P + "<b>Counts by tracker.</b></p>" + counts
    + P + "<b>Correction to this post&rsquo;s own count.</b> The 9 July 2026 list of 11 states below does not match later trackers. Six of the 11 (Madhya Pradesh, Karnataka, Haryana, Jharkhand, "
    "Chhattisgarh and Assam) are draft only in the November trackers; Uttar Pradesh, Gujarat and Bihar are final under all four codes; Uttarakhand is final under two.</p>"
    + P + "Odisha does not appear as final in any later tracker read. Four of the six states in the March 2026 list (Haryana, Madhya Pradesh, Karnataka and Maharashtra) are also draft, or final under one code only. "
    "The headline figure of about 11 of 28 states should be read as superseded. The trackers count 36 jurisdictions (28 states and 8 union territories), or 37, not 28.</p>"
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
    "<i>Earlier updates follow; the original text is unchanged.</i></p></div>\n"
)
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in block.lower(), banned
assert not re.search(r"\b(we|our|you|your)\b", re.sub(r"<[^>]+>", " ", block).lower().replace("this blog", "")), "first or second person in the block"

step(7, "assembling and proving the original is unchanged")
new = orig.replace(ANCHOR, block + ANCHOR)
assert new.count("Updated 21 November 2026") == 1
assert new.replace(block, "", 1) == orig                              # remove the block: byte-identical to the published post
OUT.write_text(new)
print("wrote", OUT.relative_to(ROOT), f"({len(new) - len(orig)} characters added; original text unchanged)")
