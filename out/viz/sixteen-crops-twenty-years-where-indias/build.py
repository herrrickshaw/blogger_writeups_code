"""Visual-first edition of sixteen-crops-twenty-years-where-indias. Run from the repo root:  python3 out/viz/sixteen-crops-twenty-years-where-indias/build.py"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "sixteen-crops-twenty-years-where-indias"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# Every figure below is one the original post prints (chart labels included); nothing is computed, so derived.json is empty.

top = top_line([
    ("3.8&times;", " maize output in 2025-26 against its 2003-06 average, 55 million tonnes, the fastest-growing cereal."),
    ("0.0%", " annual soybean yield growth over twenty years; every tonne of extra output came from more land."),
    ("2.9&times;", " jowar yield in Andhra Pradesh against the national average, the widest state gap of any crop."),
])

# ---- 1. growth ----
growth_all = [("Moong", 6.1), ("Maize", 5.8), ("Gram", 3.7), ("Cotton", 3.2), ("Sugarcane", 3.2), ("Mustard", 3.0), ("Soybean", 2.9),
              ("Lentil", 2.8), ("Rice", 2.6), ("Wheat", 2.6), ("Urad", 2.6), ("Groundnut", 2.2), ("Tur", 1.8), ("Bajra", 0.8),
              ("Ragi", -0.9), ("Jowar", -2.1)]
pct = lambda v: f"{v:+.1f}%"
s1 = insight(
    "Growth: moong and maize grew about 6% a year over twenty years; jowar and ragi shrank",
    bars("Moong grew 6.1% a year and maize 5.8%, while jowar fell 2.1% and ragi 0.9%",
         [("Moong <small>about half from land, half from yield</small>", 6.1),
          ("Maize <small>area 75 to 126 lakh ha, yield 1,962 to 3,588 kg</small>", 5.8),
          ("Gram", 3.7),
          ("Soybean <small>all from land: area 73 to 129 lakh ha, yield about 1,060 kg</small>", 2.9),
          ("Groundnut <small>area fell, yield nearly doubled</small>", 2.2),
          ("Bajra <small>area fell by a quarter, yield rose</small>", 0.8),
          ("Ragi <small>shrinking, shown as a minimal bar</small>", -0.9),
          ("Jowar <small>area fell from 90 to 39 lakh ha</small>", -2.1)],
         accent=["Moong <small>about half from land, half from yield</small>",
                 "Maize <small>area 75 to 126 lakh ha, yield 1,962 to 3,588 kg</small>"],
         fmt=pct, vmax=6.1,
         sub="Average annual change in production, 2003-06 to 2023-26 (three-year averages), 8 of 16 crops.",
         source="UPAG all-India area, production and yield; this blog&rsquo;s calculations.")
    + numbers(["Crop", "Production growth a year"], [[c, pct(v)] for c, v in growth_all]),
    "Moong and maize grew fastest, roughly half from new land and half from better yields, while soybean grew only by adding land "
    "and jowar and ragi are the only crops to shrink.",
    "Read each crop&rsquo;s growth by its source: land for soybean, yield for groundnut, bajra and urad, and both for maize and moong.",
    "growth")

# ---- 2. yield gap ----
gap = [("Jowar", "Rajasthan", "Andhra Pradesh", 285), ("Ragi", "Karnataka", "Tamil Nadu", 219), ("Maize", "Maharashtra", "West Bengal", 194),
       ("Bajra", "Maharashtra", "Madhya Pradesh", 180), ("Moong", "Karnataka", "Madhya Pradesh", 178), ("Urad", "Rajasthan", "Andhra Pradesh", 172),
       ("Tur", "Andhra Pradesh", "Odisha", 149), ("Gram", "Karnataka", "Gujarat", 149), ("Rice", "Madhya Pradesh", "Punjab", 146),
       ("Wheat", "Gujarat", "Punjab", 141), ("Mustard", "West Bengal", "Haryana", 140), ("Soybean", "Rajasthan", "Gujarat", 138),
       ("Sugarcane", "Uttar Pradesh", "Tamil Nadu", 128), ("Cotton", "Maharashtra", "Gujarat", 126),
       ("Groundnut", "Uttar Pradesh", "Gujarat", 126), ("Lentil", "Jharkhand", "Uttar Pradesh", 105)]
pick = {"Jowar", "Ragi", "Maize", "Bajra", "Rice", "Wheat", "Soybean", "Lentil"}
s2 = insight(
    "Yield gap: Andhra Pradesh&rsquo;s jowar yields 2.9 times the national average",
    bars("The best major state&rsquo;s jowar yield is 285% of the national average; lentil&rsquo;s is 105%",
         [(f"{c} <small>best: {hi}</small>", v) for c, lo, hi, v in gap if c in pick],
         accent="Jowar <small>best: Andhra Pradesh</small>", unit="%", vmax=300, ref=(100, "National yield = 100%"),
         sub="Yield of the strongest state producing at least 3% of the crop, as % of the national yield, 2023-26.",
         source="UPAG state-wise area, production and yield; this blog&rsquo;s calculations.")
    + numbers(["Crop", "Weakest major state", "Strongest, % of national"], [[c, lo, f"{hi} {v}%"] for c, lo, hi, v in gap]),
    "The gaps are widest in rainfed coarse grains and pulses, where a few irrigated pockets coexist with large dryland areas, "
    "and narrowest in lentil, sugarcane and soybean.",
    "Aim yield gains at jowar, maize, moong, urad and bajra, which this analysis finds have the most room to grow output without more land.",
    "gap")

# ---- 3. harvest swings ----
swing = [("Wheat", 4, "-10% (2014-15)"), ("Rice", 4, "-23% (2002-03)"), ("Sugarcane", 8, "-19% (2003-04)"), ("Jowar", 8, "-28% (2018-19)"),
         ("Cotton", 9, "-15% (2018-19)"), ("Maize", 9, "-15% (2009-10)"), ("Lentil", 10, "-24% (2018-19)"), ("Urad", 10, "-32% (2019-20)"),
         ("Bajra", 11, "-43% (2002-03)"), ("Tur", 11, "-26% (2008-09)"), ("Gram", 11, "-23% (2014-15)"), ("Mustard", 12, "-24% (2002-03)"),
         ("Ragi", 16, "-45% (2002-03)"), ("Soybean", 17, "-22% (2002-03)"), ("Moong", 21, "-38% (2004-05)"), ("Groundnut", 22, "-41% (2002-03)")]
sw = {c: (v, w) for c, v, w in swing}
show = ["Wheat", "Rice", "Sugarcane", "Maize", "Soybean", "Moong", "Groundnut"]
s3 = insight(
    "Harvest swings: groundnut and moong change 21 to 22% a year, wheat and rice 4%",
    bars("Rain-fed groundnut and moong swing 21 to 22% in a typical year; wheat and rice swing 4%",
         [(f"{c} <small>worst fall {sw[c][1]}</small>", sw[c][0]) for c in show],
         accent=[f"Moong <small>worst fall {sw['Moong'][1]}</small>", f"Groundnut <small>worst fall {sw['Groundnut'][1]}</small>"],
         unit="%", vmax=22,
         sub="Median absolute change in all-India production from one crop year to the next, 2000-01 to 2025-26.",
         source="UPAG all-India production; this blog&rsquo;s calculations.")
    + numbers(["Crop", "Typical yearly change", "Worst single-year fall"], [[c, f"{v}%", w] for c, v, w in swing]),
    "Largely irrigated wheat and rice change about 4% in a typical year, and the 2002-03 drought gave the worst single-year fall "
    "for six of the sixteen crops, including a 23% drop in rice and a 41% drop in groundnut.",
    "Expect rain-fed oilseeds and pulses to swing by a fifth or more in a typical year, and the irrigated cereals to be the steadiest base for price stability.",
    "swings")

# ---- 4. concentration ----
conc = [("Ragi", "Karnataka", 67), ("Sugarcane", "Uttar Pradesh", 47), ("Groundnut", "Gujarat", 46), ("Mustard", "Rajasthan", 44),
        ("Soybean", "Maharashtra", 43), ("Bajra", "Rajasthan", 42), ("Moong", "Madhya Pradesh", 42), ("Lentil", "Madhya Pradesh", 39),
        ("Jowar", "Maharashtra", 37), ("Tur", "Maharashtra", 33), ("Wheat", "Uttar Pradesh", 30), ("Gram", "Maharashtra", 26),
        ("Cotton", "Maharashtra", 25), ("Urad", "Madhya Pradesh", 21), ("Maize", "Madhya Pradesh", 15), ("Rice", "Uttar Pradesh", 13)]
cs = {c: (s, v) for c, s, v in conc}
cshow = ["Ragi", "Sugarcane", "Groundnut", "Soybean", "Wheat", "Maize", "Rice"]
s4 = insight(
    "Concentration: Karnataka grows 67% of ragi, while no state grows more than 13% of rice",
    bars("Karnataka grows 67% of India&rsquo;s ragi; rice&rsquo;s largest state, Uttar Pradesh, grows 13%",
         [(f"{c} <small>{cs[c][0]}</small>", cs[c][1]) for c in cshow],
         accent=[f"Ragi <small>{cs['Ragi'][0]}</small>", f"Rice <small>{cs['Rice'][0]}</small>"], unit="%", vmax=67,
         sub="Largest producing state&rsquo;s share of national output, 2023-26.",
         source="UPAG state-wise production; this blog&rsquo;s calculations.")
    + numbers(["Crop", "Largest state", "Share of output"], [[c, s, f"{v}%"] for c, s, v in conc]),
    "Rice is grown almost everywhere, with its three largest producers supplying only 35%, while soybean&rsquo;s two leading states, "
    "Maharashtra and Madhya Pradesh, produce 84%.",
    "Read the concentrated crops through their lead states: Karnataka for ragi, Uttar Pradesh for sugarcane, Maharashtra and Madhya Pradesh for soybean.",
    "concentration")

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts with the per-crop figures kept under '
           '&ldquo;Show the numbers&rdquo; and in the crop-by-crop list; the figures are unchanged.</p>\n')

crops = [
    ("Rice", "Output 147 million tonnes in 2023-26, up from 88 million in 2003-06, with a record 154 million in 2025-26; yield rose from 2,055 to 2,909 kg a hectare. Uttar Pradesh grows 13%, and West Bengal&rsquo;s share fell from 17% to 11% as Telangana rose to 12%."),
    ("Wheat", "Output 117 million tonnes, with a record 121 million in 2025-26; yield rose from 2,645 to 3,582 kg a hectare. Madhya Pradesh&rsquo;s share doubled from 10% to 21% while Punjab&rsquo;s fell from 21% to 15% and Uttar Pradesh&rsquo;s from 34% to 30%. Its worst fall since 2000 was 10%, in 2014-15."),
    ("Maize", "Output rose from 15 million tonnes in 2003-06 to a record 55 million in 2025-26, with area up from 75 to 126 lakh hectares and yield from 1,962 to 3,588 kg. Madhya Pradesh grows 15%, Karnataka 13% and Bihar 12%; Bihar&rsquo;s yield is 6,113 kg a hectare."),
    ("Jowar", "Output averaged 4.7 million tonnes in 2023-26, about a third of its 1989-90 record of 12.9 million, as area fell from 90 to 39 lakh hectares. Yield rose from 798 to 1,210 kg a hectare. Maharashtra grows 37%, down from 48%."),
    ("Bajra", "Output rose from 9.2 to 10.9 million tonnes and has not beaten its 2003-04 record of 12.1 million. Area fell from 98 to 72 lakh hectares while yield rose from 934 to 1,511 kg. Rajasthan grows 42% at 1,105 kg a hectare."),
    ("Ragi", "1.9 million tonnes, against a record 3.2 million in 1978-79. Yield has hardly moved, at about 1,430&ndash;1,480 kg a hectare. Karnataka grows two-thirds; Tamil Nadu&rsquo;s yield is 3,240 kg a hectare."),
    ("Gram", "Output doubled from 5.6 to 11.6 million tonnes, with a record 13.5 million in 2021-22; yield rose from 811 to 1,221 kg a hectare and area from 69 to 95 lakh hectares. Madhya Pradesh&rsquo;s share fell from 45% to 20%, Maharashtra&rsquo;s rose from 9% to 26% and Gujarat&rsquo;s from 2% to 13%."),
    ("Tur", "Output rose from 2.5 to 3.5 million tonnes, below the 2016-17 record of 4.9 million; yield rose only from 701 to 823 kg a hectare. Karnataka&rsquo;s share more than doubled to 26% at 597 kg a hectare. Kalaburagi district grows 11% of the crop."),
    ("Moong", "Output more than tripled, from 1.2 to a record 4.5 million tonnes in 2025-26, with area and yield each roughly doubling. Madhya Pradesh grows 42% at 1,212 kg a hectare and Rajasthan 29% at 464 kg. Madhya Pradesh&rsquo;s figures are missing for 2003-06, so its earlier share is not shown."),
    ("Urad", "Output rose from 1.4 to 2.2 million tonnes, almost all from yield, which rose from 423 to 682 kg a hectare on an unchanged area of about 33 lakh hectares. It remains below the 2017-18 record of 3.5 million tonnes. Madhya Pradesh grows 21%, Uttar Pradesh and Andhra Pradesh 17% each."),
    ("Lentil", "Output rose from 1.0 to 1.7 million tonnes, mainly through yield, which reached 1,000 kg a hectare. Madhya Pradesh grows 39%, up from 26%, and Uttar Pradesh 37%, down from 48%."),
    ("Groundnut", "Output reached a record 13.1 million tonnes in 2025-26 even though area fell from 65 to 54 lakh hectares; yield rose from 1,188 to 2,155 kg a hectare. Gujarat grows 46%; Rajasthan&rsquo;s share rose from 6% to 21% while Andhra Pradesh&rsquo;s fell from 17% to 3%."),
    ("Rapeseed and mustard", "Output nearly doubled, from 7.3 to 13.2 million tonnes, with a record 13.8 million in 2025-26. Rajasthan grows 44%, down from 51%; Uttar Pradesh&rsquo;s share rose from 11% to 17%. Haryana&rsquo;s yield is 2,034 kg a hectare."),
    ("Soybean", "Output rose from 7.7 to 13.6 million tonnes, peaking at 15.3 million in 2024-25 and falling to 12.6 million in 2025-26; area rose from 73 to 129 lakh hectares at about 1,060 kg a hectare in both periods. Maharashtra grows 43% and Madhya Pradesh 41%."),
    ("Cotton", "Output averaged 30.4 million bales of 170 kg in 2023-26, against 16.2 million in 2003-06, below the 2019-20 record of 36.1 million and 29.0 million in 2025-26. Lint yield rose from 329 to 435 kg a hectare. Gujarat&rsquo;s yield, 547 kg, is 69% higher than Maharashtra&rsquo;s 323 kg."),
    ("Sugarcane", "Output averaged 469 million tonnes in 2023-26 and reached a record 500 million in 2025-26, with yield up from 64 to 82 tonnes a hectare. Uttar Pradesh grows 47%; Maharashtra&rsquo;s share rose from 11% to 25% while Tamil Nadu&rsquo;s fell from 10% to 3%."),
]
crop_block = ('<details class="xv-n"><summary>Crop by crop: output, yield and leading states</summary><ul>'
              + "".join(f"<li><b>{c}.</b> {t}</li>" for c, t in crops) + "</ul></details>\n")

trust = '''<details class="xv-n"><summary>How much to trust it</summary><ul>
<li>All figures are from the Department of Agriculture&rsquo;s Unified Portal for Agricultural Statistics (UPAG): all-India area, production and yield from 1966-67, state figures from 1997-98 and district figures from 2015-16, with 2025-26 at the third advance estimate.</li>
<li>&ldquo;2003-06&rdquo; means the average of 2003-04 to 2005-06 and &ldquo;2023-26&rdquo; the average of 2023-24 to 2025-26, so one drought or bumper year does not drive the comparisons.</li>
<li>Growth is split into area and yield on a log scale, so the two parts add up exactly.</li>
<li>Cotton production is in bales of 170 kg of lint; UPAG&rsquo;s download labels it lakh tonnes, but the figures only reconcile with its published yield as bales.</li>
<li>State yield gaps compare only states producing at least 3% of a crop.</li>
<li>Telangana appears from 2014, when it was carved out of Andhra Pradesh, so its earlier output sits in Andhra&rsquo;s figures.</li>
<li>District shares use the 2022-23 to 2024-25 average of UPAG district-wise production, 2015-16 to 2024-25.</li>
</ul></details>
'''

adds = '''<details class="xv-n"><summary>What it adds up to</summary><ul>
<li>The fastest growers, maize and moong, are the crops where both land and yield expanded, pulled by new demand from ethanol and poultry feed in maize&rsquo;s case.</li>
<li>The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra.</li>
<li>The crops that matter most for price stability, the irrigated cereals, are also the steadiest harvests, while the rain-fed oilseeds and pulses swing by a fifth or more in a typical year.</li>
<li>Sugarcane, moong and tur have become more concentrated, while jowar and gram have spread out; Uttar Pradesh, Maharashtra and Karnataka now grow 83% of India&rsquo;s cane, against 69% in 2003-06.</li>
<li>This post is AI-assisted analysis of public data, not investment advice.</li>
</ul></details>
'''

extras = trust + adds + crop_block + sources_block(body_links(FR.body))

body = STYLE + top + FR.keep_front + FR.notes + updated + s1 + s2 + s3 + s4 + extras
OUT.write_text(FR.head + FR.lead + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
