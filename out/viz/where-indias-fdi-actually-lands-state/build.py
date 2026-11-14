"""Visual-first edition of where-indias-fdi-actually-lands-state. Run from the repo root:  python3 out/viz/where-indias-fdi-actually-lands-state/build.py"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "where-indias-fdi-actually-lands-state"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"
OUTLINE = (pathlib.Path(__file__).parent / "outline.md").read_text(encoding="utf-8")


def table(first_header, cols=None):
    """Rows of the outline's pipe table whose header starts with first_header; cols picks columns by index."""
    lines = [ln for ln in OUTLINE.splitlines() if ln.startswith("|")]
    for i, ln in enumerate(lines):
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if cells[0].startswith(first_header):
            rows = []
            for ln2 in lines[i + 1:]:
                c2 = [c.strip() for c in ln2.strip("|").split("|")]
                if len(c2) != len(cells):
                    break
                rows.append(c2)
            idx = cols or range(len(cells))
            return [cells[j] for j in idx], [[r[j] for j in idx] for r in rows]
    raise KeyError(first_header)


def num(s):
    return float(s.replace(",", "").replace("%", ""))


# ---- figures behind the charts, copied from the original's tables ----
dh, drows = table("Rank", [1, 2, 3, 5])
districts = [(r[0], r[1], num(r[2])) for r in drows]                      # name, state, Rs crore, 24 quarters
mh, mrows = table("District", [0, 25, 26])                                 # Maharashtra district rows
mah = [(r[0], num(r[2])) for r in mrows if r[0] in ("Navi Mumbai", "Pune", "Thane", "Nashik", "Raigad", "Aurangabad", "Nagpur", "Satara")]
assert mah[0] == ("Navi Mumbai", 84.56) and len(mah) == 8

top = top_line([
    ("72.6%", " of the &#8377;25,80,189 crore of FDI equity inflow recorded from October 2019 to March 2026 went to four districts: "
              "Navi Mumbai, Bengaluru Urban, Delhi and Ahmedabad."),
    ("84.6%", " of Maharashtra&rsquo;s own total is Navi Mumbai alone, and three districts make up 98.7% of the state, "
              "which is itself 31.7% of the national total."),
    ("30.0%", " of the April&ndash;June 2026 quarter went to Tamil Nadu, its first quarter as the top state, against 7.0% of the total since October 2019."),
])

# ---- section 1: four districts ----
four = ["Navi Mumbai", "Bengaluru Urban", "Delhi", "Ahmedabad"]
s1 = insight(
    "FDI equity by district: four took 72.6% of &#8377;25,80,189 crore, October 2019 to March 2026",
    bars("Four districts hold 72.6% of FDI equity; fifth-ranked Gurugram has &#8377;119,768 crore",
         [(f"{n} <small>{st}</small>", v) for n, st, v in districts[:10]],
         accent=[f"{n} <small>{st}</small>" for n, st, v in districts if n in four],
         sub="FDI equity inflow by district, &#8377; crore, 24 of 26 quarters from October 2019 to March 2026; top 10 districts shown.",
         source="DPIIT, State/District-wise FDI Equity Inflow (Table No.16), as summed in the post. Counted at the recipient company&rsquo;s registered office.")
    + numbers(["Rank", "District", "State", "&#8377; crore"],
              [[str(i + 1), n, st, f"{v:,.0f}"] for i, (n, st, v) in enumerate(districts)], summary="Show the top 20 districts"),
    "Every other district in India, in 28 states and 8 union territories, shares the remaining 27.4%, and DPIIT records inflow at the recipient company&rsquo;s "
    "registered office, which is not necessarily where a factory or data centre is built.",
    "DPIIT should add the state and district where the investment is deployed to its FDI inflow data, so that registered-office districts can be told apart from where assets are built.",
    "districts")

# ---- section 2: Maharashtra ----
sh, srows = table("State / UT", [0, 25, 26])
srows = [r for r in srows]
s2 = insight(
    "Maharashtra: 31.7% of national FDI equity, and Navi Mumbai is 84.6% of the state total",
    bars("Navi Mumbai, Pune and Thane make up 98.7% of Maharashtra; the rest are 0.32% or less",
         [(n, v) for n, v in mah], accent=["Navi Mumbai", "Pune", "Thane"], unit="%",
         sub="Share of Maharashtra&rsquo;s own 24-quarter FDI equity total, %; top 8 of Maharashtra&rsquo;s districts shown.",
         source="DPIIT Table No.16, October 2019 to March 2026 (24 quarters), as summed in the post.")
    + numbers(["State / UT", "&#8377; crore, 24 quarters", "% of national"], srows, summary="Show the 18 largest states and union territories"),
    "Maharashtra is the largest state, and its own FDI is more concentrated than the national picture, with Navi Mumbai alone at 84.6% of it.",
    "DPIIT should release the full state and district-wise series as a downloadable CSV updated each quarter, so that users do not have to parse PDFs to check this.",
    "maharashtra")

# ---- section 3: Tamil Nadu ----
s3 = insight(
    "Tamil Nadu: 30.0% of April&ndash;June 2026 FDI equity, 7.0% of the total since October 2019",
    bars("Tamil Nadu led a quarter for the first time, far above its 7.0% share of the whole period",
         [("Tamil Nadu <small>April&ndash;June 2026</small>", 30.0), ("Tamil Nadu <small>since October 2019</small>", 7.0),
          ("Maharashtra <small>April&ndash;June 2026</small>", 21.3), ("Maharashtra <small>since October 2019</small>", 30.8),
          ("Karnataka <small>April&ndash;June 2026</small>", 10.7), ("Karnataka <small>since October 2019</small>", 20.1),
          ("Delhi <small>April&ndash;June 2026</small>", 13.5), ("Delhi <small>since October 2019</small>", 12.9)],
         accent=["Tamil Nadu <small>April&ndash;June 2026</small>", "Tamil Nadu <small>since October 2019</small>"], fmt=lambda v: f"{v:.1f}%",
         sub="Share of FDI equity inflow, %: the April&ndash;June 2026 quarter (&#8377;1,86,661 crore) and October 2019 to June 2026 (state level).",
         source="DPIIT fact sheets to March 2026 and June 2026, Annex C; quarter taken as the difference between the two.")
    + numbers(*(lambda h, r: (h, r))(*table("State / UT, April")), summary="Show the ten states for the quarter"),
    "Tamil Nadu took &#8377;55,900 crore of the quarter&rsquo;s &#8377;1,86,661 crore, against a previous best of &#8377;22,902 crore, though the fact sheet does not name the investments behind it.",
    "DPIIT should release its district series as a CSV updated each quarter, since the fact sheet carries no district table for April&ndash;June 2026.",
    "tamilnadu")

# ---- section 4: reconciliation gap ----
gh, grows = table("State / UT, October 2019 to March 2026")
gap = sorted(((r[0], num(r[3])) for r in grows if r[0] != "All states and UTs"), key=lambda x: -x[1])
big3 = ["Maharashtra", "Karnataka", "Delhi"]
s4 = insight(
    "DPIIT cumulative state table: &#8377;1,45,325 crore above this piece&rsquo;s 24 quarterly tables",
    bars("DPIIT&rsquo;s table is higher in every state shown; Maharashtra, Karnataka and Delhi most",
         [(n, v) for n, v in gap], accent=big3,
         sub="DPIIT Annex C total less the sum of the 24 quarterly tables, October 2019 to March 2026, &#8377; crore; 12 states shown.",
         source="DPIIT Annex C to March 2026 against this piece&rsquo;s sums of 24 quarterly tables.")
    + numbers(gh, grows, summary="Show both totals by state"),
    "DPIIT puts October 2019 to March 2026 at &#8377;27,25,514 crore against &#8377;25,80,189 crore summed here, and the difference holds the two missing 2020 quarters plus any restatement, which these tables cannot separate.",
    "DPIIT should publish the state and district-wise FDI equity tables for January&ndash;March 2020 and April&ndash;June 2020, so that the district series has no hole in it.",
    "gap")

# ---- collapsed detail ----
qh, qrows = table("Quarter")
qtr = numbers(qh, qrows, summary="National FDI equity by quarter, 24 quarters")
qnote = ('<details class="xv-n"><summary>The national trend and the two missing quarters</summary>'
         '<p>The July&ndash;September 2020 spike of &#8377;1,74,793 crore, driven almost entirely by a single Ahmedabad district figure, is the largest quarter of the 24, '
         'and the April&ndash;June 2025 and July&ndash;September 2025 quarters are the strongest sustained pair since 2020-21. '
         'State-wise data is kept from October 2019 only; January&ndash;March 2020 and April&ndash;June 2020 could not be located as standalone tables, '
         'and nothing is estimated for them, so the change shown for July&ndash;September 2020 spans roughly nine months, not three.</p>'
         + qtr.split("</summary>", 1)[1])

mid_cities = numbers(*table("Maharashtra district", [0, 1, 2, 3]), summary="Maharashtra&rsquo;s smaller districts: first 12 quarters against last 12")
movers = ('<details class="xv-n"><summary>What moved underneath the big numbers</summary>'
          '<p>Kolhapur fell 98.7% on one &#8377;112.5 crore quarter that never repeated, Parbhani&rsquo;s entire &#8377;244 crore landed in April&ndash;June 2025, '
          'and Aurangabad and Nagpur rose while Nashik and Satara fell, though every figure is small beside the Navi Mumbai, Pune and Thane core.</p>'
          + mid_cities.split("</summary>", 1)[1])

cal21 = ('<details class="xv-n"><summary>Calendar 2021 districts, a separate DPIIT table</summary>'
         '<p>The post&rsquo;s earlier chart ranked districts for January&ndash;December 2021 from DPIIT Table No. 9, a different base from the 24-quarter totals above, so the two are not combined.</p>'
         '<div class="gb-tblwrap"><table class="gb-table"><thead><tr><th>District, Jan&ndash;Dec 2021</th><th>&#8377; crore</th></tr></thead><tbody>'
         '<tr><td>Bangalore (Urban)</td><td>135,822</td></tr><tr><td>New Mumbai</td><td>74,397</td></tr><tr><td>Delhi</td><td>56,465</td></tr>'
         '<tr><td>Gurgaon (Gurugram)</td><td>18,141</td></tr><tr><td>Kancheepuram</td><td>12,057</td></tr></tbody></table></div></details>\n')

verified = ('<details class="xv-n"><summary>How the figures were verified</summary>'
            '<p>The dataset was supplied directly, because dpiit.gov.in could not be reached, and was parsed from DPIIT&rsquo;s own PDFs. '
            'Every figure checked from three quarters read directly matched exactly, and summing its quarters into fiscal years reproduced five independently sourced years: '
            'FY2021-22 $58.77bn, FY2022-23 $46.03bn, FY2023-24 $44.42bn, FY2024-25 $50.02bn and FY2025-26 $58.85bn.</p>'
            '<p>This piece did not re-read all 24 source PDFs, and relies on the dataset&rsquo;s own account of its parser checks, '
            'which put agreement with DPIIT&rsquo;s printed totals at 0.00&ndash;0.03%.</p></details>\n')

caveat = ('<details class="xv-n"><summary>What this does not establish</summary><ul>'
          '<li>DPIIT attributes inflow to the recipient company&rsquo;s registered office, so a holding company in Navi Mumbai or Bengaluru Urban can direct capital deployed anywhere; this dataset cannot separate that from local investment.</li>'
          '<li>The January&ndash;June 2020 gap means no comparison across it is a clean three-month step.</li>'
          '<li>The Ahmedabad July&ndash;September 2020 spike and the Parbhani and Kolhapur swings are reported as facts, not explained, and no transaction behind any of them is identified.</li>'
          '<li>This is equity inflow only; total FDI, which also includes re-invested earnings and other capital, is larger and differently distributed, and is not broken down by state or district here.</li>'
          '</ul></details>\n')

fixes = '''<h2 class="gb-h2" id="fix">Four fixes</h2>
<ol>
<li><b>DPIIT:</b> publish the state and district-wise FDI equity tables for January&ndash;March 2020 and April&ndash;June 2020.</li>
<li><b>DPIIT:</b> release the full state and district-wise series as a downloadable CSV file updated each quarter, instead of 3,320 rows locked in PDFs.</li>
<li><b>DPIIT:</b> add the state and district where the investment is deployed, alongside the recipient company&rsquo;s registered office.</li>
<li><b>DPIIT and the Reserve Bank of India:</b> publish a state-wise breakdown of total FDI, including reinvested earnings and other capital, not only equity inflows.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; the figures are unchanged, '
           'and the district series still ends in March 2026.</p>\n')

extras = qnote + movers + cal21 + verified + caveat + fixes + sources_block(body_links(FR.body))

body = STYLE + top + FR.keep_front + FR.notes + updated + s1 + s2 + s3 + s4 + extras
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
