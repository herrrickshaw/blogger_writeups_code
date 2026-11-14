"""Visual-first edition of guar-gum-indias-35-billion-export-peak. Run from the repo root:  python3 out/viz/guar-gum-indias-35-billion-export-peak/build.py"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "guar-gum-indias-35-billion-export-peak"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# Numbers computed from the original's numbers go in derived.json ({"190": "570/3"}), never typed in silently.

top = top_line([
    ("&#8377;21,287 crore", " was India&rsquo;s guar gum export value in 2012-13 (about $3.5 billion), up from &#8377;121 crore in 2003-04. "
                            "The 2024-25 figure of $550.12 million is roughly 84% below that peak."),
    ("Roughly 90%", " of guar gum exports still go to oil and shale-gas extraction, per APEDA, the same end use behind the 2014-15 crash."),
    ("72%", " of guar production comes from Rajasthan on APEDA&rsquo;s live data, which supersedes the earlier 70% to nearly 80% range."),
])

EXP = {"2003-04": 20.2, "2012-13": 3500, "2016-17": 467, "2020-21": 260, "2023-24": 541.65, "2024-25": 550.12}
LAB = {20.2: "~$20.2M", 3500: "~$3.5B", 467: "~$467M", 260: "~$260M", 541.65: "$541.65M", 550.12: "$550.12M"}
assert round((1 - 550.12 / 3500) * 100) == 84          # the original's "roughly 84% below the 2012-13 peak"

s1 = insight(
    "Guar gum exports: about $3.5 billion at the 2012-13 peak, $550.12 million in 2024-25",
    bars("Exports peaked near $3.5 billion in 2012-13 and are roughly 84% below that now",
         [("2003-04 <small>baseline, pre-fracking boom; &#8377;121 crore</small>", EXP["2003-04"]),
          ("2012-13 <small>peak, India&rsquo;s number 1 agri-export; &#8377;21,287 crore</small>", EXP["2012-13"]),
          ("2016-17 <small>post-crash</small>", EXP["2016-17"]),
          ("2020-21 <small>&#8377;1,949 crore</small>", EXP["2020-21"]),
          ("2023-24 <small>417,674 MT, per APEDA</small>", EXP["2023-24"]),
          ("2024-25 <small>474,519.44 MT, per APEDA (DGCIS)</small>", EXP["2024-25"])],
         accent="2012-13 <small>peak, India&rsquo;s number 1 agri-export; &#8377;21,287 crore</small>", fmt=lambda v: LAB[v], vmax=3500,
         sub="Export value, US dollars. Dollar figures are approximate: conversions vary by source year and exchange rate.",
         source="APEDA export data and contemporaneous market reporting; the 2024-25 row was checked against APEDA&rsquo;s GuarGum page (DGCIS-sourced).")
    + numbers(["Year", "Export value", "Context"],
              [["2003-04", "&#8377;121 crore (~$20.2M)", "Baseline, pre-fracking-boom"],
               ["2012-13", "&#8377;21,287 crore (~$3.5B)", "Peak, India&rsquo;s number 1 agri-export item that year"],
               ["2016-17", "~$467 million", "Post-crash, US rig count and oil prices had collapsed"],
               ["2020-21", "&#8377;1,949 crore (~$260M)", "Still well below pre-boom-adjusted trend"],
               ["2023-24", "$541.65 million (417,674 MT)", "Partial recovery, +2.67% YoY by volume, per APEDA"],
               ["2024-25 (FY25)", "$550.12 million (474,519.44 MT)", "Latest full year, per APEDA&rsquo;s live data (DGCIS-sourced)"]]),
    "US shale fracking demand lifted exports from about $20.2 million to about $3.5 billion, and the data supports calling India a dominant "
    "supplier of a demand-volatile commodity, not cleanly a growing export market.",
    "APEDA should publish one consistent annual export series from 2003-04 in rupees, dollars and tonnes, taken from DGCIS data.",
    "exports")

s2 = insight(
    "Buyers: roughly 90% of guar gum is exported, and roughly 90% of that goes to oil and gas",
    bars("About 90% of exports still go to oil and shale gas, the buyers behind the 2014-15 crash",
         [("Guar gum processed in India that is exported <small>roughly</small>", 90),
          ("Exports going to oil and shale-gas extraction <small>roughly</small>", 90),
          ("India&rsquo;s share of world guar produce", 80)],
         accent="Exports going to oil and shale-gas extraction <small>roughly</small>", unit="%", vmax=100, from_zero=True,
         sub="Share, %, as stated on APEDA&rsquo;s GuarGum page.",
         source="APEDA (apeda.gov.in/GuarGum), DGCIS-sourced."),
    "Thirteen years after the bust the industry has not pivoted to food, pharma or textiles at scale, so the partial recovery is a recovery of fracking demand specifically.",
    "APEDA should publish the end-use breakdown behind its 90% statement year by year, so diversification can be checked rather than assumed.",
    "dependency")

s3 = insight(
    "Guar seed: about &#8377;3,000 a quintal in 2007, &#8377;30,000 in March 2012, &#8377;4,200 in January 2015",
    bars("Seed prices rose tenfold in five years, then fell to &#8377;4,200 a quintal by January 2015",
         [("2007 <small>approximate</small>", 3000), ("March 2012 <small>peak</small>", 30000), ("January 2015", 4200),
          ("2024 <small>approximate</small>", 5300), ("April 2026", 4776)],
         accent="March 2012 <small>peak</small>", unit="", fmt=lambda v: f"&#8377;{v:,.0f}",
         sub="&#8377; per quintal, at the five dates the post documents. It is not a continuous price series.",
         source="Points: 2007 about 3,000; March 2012 30,000; January 2015 4,200; 2024 about 5,300; April 2026 4,776. Not a monthly index.")
    + numbers(["Date", "Guar seed, &#8377;/quintal"],
              [["2007", "~3,000"], ["Mar 2012", "30,000"], ["Jan 2015", "4,200"], ["2024", "~5,300"], ["Apr 2026", "4,776"]]),
    "Guar gum itself followed the same shape at higher values, peaking around $11,135 a tonne in 2012, so the April 2026 seed price of &#8377;4,776 sits far below the 2012 peak.",
    "The Rajasthan Agriculture Department should publish district-wise guar sowing area, yield and farm-gate price each kharif season, so the farmer side of the cycle can be tracked.",
    "seed-price")

s4 = insight(
    "Where guar is grown: Rajasthan 72%, Haryana about 12%, Gujarat about 11% of production",
    bars("Rajasthan alone grows 72% of India&rsquo;s guar, on APEDA&rsquo;s live data",
         [("Rajasthan", 72), ("Haryana <small>roughly</small>", 12), ("Gujarat <small>roughly</small>", 11)],
         accent="Rajasthan", unit="%", vmax=100, from_zero=True,
         sub="Share of national guar production, %. Total sowing area about 29 lakh hectares (2,902,732 ha).",
         source="APEDA and state-government data."),
    "Guar is rainfed on 300-400mm a year and fixes its own nitrogen, which fits the arid northwest, but no guar-specific central scheme or formal wasteland-programme listing was found.",
    "The Department of Land Resources should state publicly whether guar is an eligible species under the wasteland and watershed programmes it administers.",
    "geography")

fixes = '''<h2 class="gb-h2" id="fix">Four fixes</h2>
<ol>
<li><b>APEDA:</b> publish one annual guar gum export series from 2003-04 in rupees, dollars and tonnes, from DGCIS data.</li>
<li><b>APEDA:</b> publish the year-by-year end-use breakdown behind the 90% oil and shale-gas statement.</li>
<li><b>Department of Land Resources:</b> state whether guar is an eligible species under wasteland and watershed programmes.</li>
<li><b>Rajasthan Agriculture Department:</b> publish district-wise guar sowing area, yield and farm-gate price each kharif season.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; the figures are unchanged from the original post.</p>\n')

procs = '''<details class="xv-n"><summary>Who processes it: the major Indian suppliers</summary>
<ul>
<li><b>Hindustan Gums &amp; Chemicals Ltd:</b> joint venture of Solvay (USA) and the M.P. Birla Group (India); 60+ years in the industry.</li>
<li><b>Vikas WSP Ltd:</b> listed on NSE/BSE since 1995; ~46,200 MT/year guar gum powder capacity plus a 100% export-oriented guar polymers unit (~39,900 TPA).</li>
<li><b>India Glycols Ltd, Rama Gum Industries (India) Ltd, Jai Bharat Gums &amp; Chemicals Ltd, Lucid Group (Lucid Colloids), Neelkanth Polymers:</b> guar processors and derivative makers.</li>
<li><b>Dabur India Ltd:</b> FMCG major with a guar-gum-adjacent interest, not a pure-play processor.</li>
</ul>
<p>This list is not exhaustive, and installed-capacity figures beyond Vikas WSP&rsquo;s own were not independently verified. Most of these firms sit in or around Rajasthan, close to the growing regions.</p></details>
'''

agro = '''<details class="xv-n"><summary>Why guar fits low-fertility, arid land</summary>
<p>Guar is a rainfed summer legume needing only 300-400mm of annual rainfall, with no supplemental irrigation in most seasons. It fixes nitrogen with Rhizobium bacteria, so a well-nodulated crop often needs no added nitrogen fertiliser and improves soil for a following wheat rotation. Intercropping guar, cowpea or pearl millet with peach, or turmeric with papaya, has been found viable for rehabilitating marginal land in Punjab and Himachal Pradesh&rsquo;s Shiwalik hill region.</p>
<p>The National Wasteland Development Board (1985) and the Integrated Wasteland Development Programme prioritise nitrogen-fixing, drought-tolerant species. The post could not confirm that guar is enrolled by name under IWDP or a similar programme.</p></details>
'''

caveat = '''<details class="xv-n"><summary>What this piece does not establish</summary>
<p>Export-value figures across 2003-2024 are compiled from multiple APEDA-sourced and secondary reports spanning different years and currency-conversion conventions; treat the dollar figures as directionally accurate rather than exactly reconciled to one methodology. Rajasthan&rsquo;s share has been cited as both &ldquo;around 70%&rdquo; and &ldquo;nearly 80%&rdquo;; APEDA&rsquo;s live data resolves this at 72%. No dedicated central scheme incentivising guar cultivation on wasteland was found; the policy fit is an agronomic-criteria match, not confirmation of a guar-specific programme. The seed-price chart uses five documented points, not a continuous AGMARKNET or NCDEX series.</p></details>
'''

extras = procs + agro + caveat + sources_block(body_links(FR.body))

body = STYLE + top + FR.keep_front + FR.notes + "\n" + updated + s1 + s2 + s3 + s4 + fixes + extras
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
