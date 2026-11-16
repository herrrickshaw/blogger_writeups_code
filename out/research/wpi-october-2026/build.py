"""India's WPI for October 2026 (base 2022-23): the 12.29% reading, the fuel and power rise, and the gap with retail prices.
Build from the repo root:  python3 out/research/wpi-october-2026/build.py   (writes out/post-india-wholesale-inflation-october-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-wholesale-inflation-october-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Ministry of Commerce and Industry (DPIIT / Office of the Economic Adviser), WPI for October 2026, base 2022-23, provisional, released 16 Nov 2026 ----
# Read through: DD News, "Wholesale price inflation rises to 12.29% in October" (https://ddnews.gov.in/en/wholesale-price-inflation-rises-to-12-29-in-october/),
# PTI via The Tribune and Mathrubhumi (16 Nov), Kotak Neo (16 Nov), PNB Economic Intelligence Cell "Macro Insights" 16 Nov 2026 (group table citing the Office of
# Economic Adviser). The Ministry's own PDF (eaindustry.nic.in) was not opened: the cached copy was the May 2026 release on the old 2011-12 base.
WPI = {"August": 9.92, "September": 11.39, "October": 12.29}
CUM_APR_OCT = 10.14                                                  # cumulative April-October 2026-27 (DD News)
GROUPS = {  # name: (weight %, Aug, Sep, Oct inflation %, Sep index, Oct index)    weights and August from PNB; indices from DD News / Tribune
    "Primary articles": (22.76, 7.12, 8.67, 9.24, 120.3, 120.6),
    "Fuel and power": (14.11, 23.16, 25.85, 32.84, 110.5, 115.7),
    "Manufactured products": (63.13, 8.47, 9.76, 9.54, 110.2, 110.2)}
ALL_IDX_SEP, ALL_IDX_OCT = 112.5, 113.3
assert round(sum(g[0] for g in GROUPS.values()), 2) == 100.00
assert [WPI[m] for m in WPI] == sorted(WPI.values())
# Weighted index check: all-commodities index = sum of weight x group index (Laspeyres); it reproduces 113.3 and 112.5 within rounding.
assert abs(sum(w * i1 / 100 for w, *_, i0, i1 in GROUPS.values()) - ALL_IDX_OCT) < 0.1
assert abs(sum(w * i0 / 100 for w, _, _, _, i0, i1 in GROUPS.values()) - ALL_IDX_SEP) < 0.1
# Contribution to the year-on-year rise in points: weight x (October 2026 index less implied October 2025 index), implied index = index / (1 + inflation).
def prior(idx, infl): return idx / (1 + infl / 100)
ALL_PRIOR = prior(ALL_IDX_OCT, WPI["October"])
CONT = {k: w * (i1 - prior(i1, o)) / 100 for k, (w, _, _, o, _, i1) in GROUPS.items()}
TOTAL_RISE = ALL_IDX_OCT - ALL_PRIOR
assert abs(sum(CONT.values()) - TOTAL_RISE) < 0.1                    # shares add up to the all-commodities rise within index rounding
SHARE = {k: 100 * v / sum(CONT.values()) for k, v in CONT.items()}
assert round(SHARE["Fuel and power"]) in (32, 33) and round(SHARE["Manufactured products"]) in (48, 49) and round(SHARE["Primary articles"]) in (18, 19)
FUEL_SHARE = round(SHARE["Fuel and power"], 1)

MOM = {k: w * (i1 - i0) / 100 for k, (w, _, _, _, i0, i1) in GROUPS.items()}              # points added to the all-commodities index, September to October
assert round(ALL_IDX_OCT - ALL_IDX_SEP, 1) == 0.8 and 0.85 < MOM['Fuel and power'] / (ALL_IDX_OCT - ALL_IDX_SEP) < 0.95
# Fuel and power components, September -> October inflation %
FUEL = [("Crude petroleum and natural gas", 57.32, 70.80), ("Mineral oils", 40.02, 45.57), ("Coal and lignite", 9.31, 10.49), ("Electricity", -0.43, 8.06)]
# Primary articles and manufactured items, October inflation % (September in brackets in the table)
OTHER = [("Chemicals and chemical products", 16.74, 17.53), ("Basic metals", 16.96, 17.21), ("Rubber and plastic products", 13.47, 13.90), ("Textiles", 13.85, 13.67),
         ("Minerals", 9.51, 12.64), ("Non-food articles", 10.28, 11.69), ("Food products (manufactured)", 9.44, 9.24), ("Food articles", 8.14, 8.26)]
FOOD_IDX_WPI = 8.58                                                  # WPI Food Index (weight 24.99%), September 8.66

# ---- MoSPI CPI, October 2026 (see out/research/cpi-october-2026/build.py): same-month retail comparators ----
CPI_ALL, CPI_FOOD, CPI_FUELS, CPI_PTE = 6.09, 8.94, 3.71, 7.52       # CPI general; CFPI; 04.5 Electricity, gas and other fuels; 07.2 Operation of personal transport equipment
assert round(WPI["October"] - CPI_ALL, 2) == 6.20

# Single secondary report: Indoen Research, 12 Nov 2026: Delhi petrol Rs 102.12 and diesel Rs 95.20 a litre as of 10 Nov, "unchanged for weeks".
PETROL, DIESEL = 102.12, 95.20

TITLE = "India's wholesale inflation: 12.29% in October 2026, fuel and power up 32.84%"
assert 55 <= len(TITLE) <= 80, len(TITLE)

top = top_line([
    ("12.29%", " was India&rsquo;s wholesale price inflation in October 2026, up from 11.39% in September and 9.92% in August; April to October averages 10.14%."),
    ("32.84%", f" was inflation in fuel and power, which has 14.11% of the weight and about {FUEL_SHARE:.0f}% of the year&rsquo;s rise; crude petroleum and natural gas rose 70.80% and mineral oils 45.57%."),
    ("6.2 points", f" separate wholesale inflation (12.29%) from retail inflation (6.09%); the retail index for electricity, gas and other fuels rose {CPI_FUELS}%, against 32.84% wholesale."),
])

s1 = insight(
    "Wholesale inflation: 9.92% in August, 11.39% in September, 12.29% in October",
    bars("Wholesale inflation rose for a third month, to 12.29% from 9.92% in August",
         [("August", WPI["August"]), ("September", WPI["September"]), ("October", WPI["October"]), ("April to October, cumulative", CUM_APR_OCT)],
         accent="October", unit="%",
         sub="Year-on-year change in the all-commodities WPI (base 2022-23), per cent. October is provisional.",
         source="Ministry of Commerce and Industry release of 16 November 2026, as published by DD News and PTI; PNB Macro Insights.")
    + numbers(["Group", "Weight (%)", "August", "September", "October"],
              [[k, f"{w:.2f}", f"{a:.2f}", f"{s:.2f}", f"{o:.2f}"] for k, (w, a, s, o, _, _) in GROUPS.items()] +
              [["All commodities", "100.00", "9.92", "11.39", "12.29"], ["WPI Food Index", "24.99", "6.41", "8.66", "8.58"]]),
    "October is the highest reading in the 2022-23-based series according to PTI, the all-commodities index rose 0.71% in the month to 113.3, and the 12.29% was above the 12.1% median of a Reuters poll reported by Kotak Neo.",
    "The November reading, due in mid-December, is the next test; PTI quoted economists who expect cooling global energy prices to lower it.",
    "trend")

s2 = insight(
    "Fuel and power rose 32.84%, led by crude petroleum and natural gas at 70.80%",
    bars("Crude and gas prices rose 70.80% in a year, mineral oils 45.57%, coal 10.49%",
         [(n, o) for n, _, o in FUEL], accent="Crude petroleum and natural gas", unit="%", ref=(12.29, "all-commodities WPI inflation, 12.29%"),
         sub="Year-on-year change in the WPI, October 2026, per cent. Electricity was &minus;0.43% in September.",
         source="Ministry of Commerce and Industry, release of 16 November 2026, as published by DD News.")
    + numbers(["Item", "September (%)", "October (%)"], [[n, f"{s:.2f}", f"{o:.2f}"] for n, s, o in FUEL] +
              [["Fuel and power, whole group", "25.85", "32.84"], ["Fuel and power, April to October", "&ndash;", "26.37"]]),
    "Electricity moved from &minus;0.43% in September to 8.06% and the fuel and power index rose 4.71% in one month, so the group with 14.11% of the weight supplied about nine-tenths of the 0.8-point monthly rise in the index.",
    "Power distributors and the petroleum ministry should publish monthly pass-through tables from wholesale fuel and power prices to tariffs and pump prices, so the 32.84% can be traced to households and firms.",
    "fuel")

s3 = insight(
    f"Fuel and power has 14.11% of the weight and about {FUEL_SHARE:.0f}% of the year&rsquo;s rise",
    bars(f"Fuel and power: 14.11% of the weight, about {FUEL_SHARE:.0f}% of the 12.4-point rise",
         [("Fuel and power", SHARE["Fuel and power"], "weight 14.11%"), ("Primary articles", SHARE["Primary articles"], "weight 22.76%"),
          ("Manufactured products", SHARE["Manufactured products"], "weight 63.13%")],
         accent="Fuel and power", unit="%",
         sub="Share of the year-on-year rise in the all-commodities index, per cent: weight times the change in each group index. Computed by this blog from published indices, so approximate.",
         source="Group indices and inflation rates from the Ministry of Commerce and Industry release, via DD News and PNB Macro Insights; shares computed here.")
    + numbers(["Group", "Index, October 2026", "Implied October 2025", "Weight (%)", "Points of the rise", "Share of rise (%)"],
              [[k, f"{i1:.1f}", f"{prior(i1, o):.1f}", f"{w:.2f}", f"{CONT[k]:.2f}", f"{SHARE[k]:.1f}"] for k, (w, _, _, o, _, i1) in GROUPS.items()] +
              [["All commodities", f"{ALL_IDX_OCT}", f"{ALL_PRIOR:.1f}", "100.00", f"{TOTAL_RISE:.2f}", "100.0"]]),
    f"Manufactured products, with 63.13% of the weight, supply about {SHARE['Manufactured products']:.0f}% of the rise, with chemicals at 17.53% and basic metals at 17.21%, so fuel is the largest single push but not the whole of it.",
    "DPIIT should add a contribution-to-inflation table by group and item to its monthly release, so readers do not have to rebuild it from rounded indices.",
    "contribution")

s4 = insight(
    "Wholesale fuel and power is up 32.84%, retail electricity, gas and fuels 3.71%",
    bars("Wholesale fuel inflation is 32.84%, the retail fuels index 3.71%; food is close at both",
         [("WPI mineral oils", 45.57), ("WPI fuel and power", 32.84), ("CPI electricity, gas and other fuels", CPI_FUELS), ("CPI operation of personal transport equipment", CPI_PTE),
          ("WPI Food Index", FOOD_IDX_WPI), ("CPI food", CPI_FOOD), ("WPI all commodities", 12.29), ("CPI all items", CPI_ALL)],
         accent="CPI electricity, gas and other fuels", unit="%",
         sub="Year-on-year inflation, October 2026, per cent. The two indices have different baskets and weights, so the comparison shows direction and size, not an exact pass-through.",
         source="Ministry of Commerce and Industry (WPI, 16 November 2026); MoSPI (CPI, 12 November 2026).")
    + numbers(["Measure", "Value", "Source"],
              [["WPI minus CPI, all items", "6.20 points", "Computed here"],
               ["Delhi petrol and diesel, 10 November", f"Rs {PETROL} and Rs {DIESEL} a litre, reported unchanged for weeks", "Indoen Research, 12 November 2026 (single report)"],
               ["CPI operation of personal transport equipment", "7.52% (petrol, diesel, vehicle running costs)", "MoSPI, group 07.2"]]),
    "Wholesale food and retail food are within 0.4 points of each other, but wholesale fuel is about nine times the retail fuels index, so the energy rise has so far reached the CPI only in part.",
    "The petroleum ministry and PPAC should publish oil marketing companies&rsquo; monthly marketing margins on petrol, diesel and LPG, so the gap between wholesale and pump prices can be sized instead of inferred.",
    "retail")

assert round(32.84 / CPI_FUELS, 1) == 8.9 and abs(CPI_FOOD - FOOD_IDX_WPI) < 0.4

mfr = '''<details class="xv-n"><summary>Manufactured products and primary articles, October 2026</summary><div class="gb-tblwrap"><table class="gb-table"><thead><tr><th>Item</th><th>September (%)</th><th>October (%)</th></tr></thead><tbody>''' + "".join(
    f"<tr><td>{n}</td><td>{s:.2f}</td><td>{o:.2f}</td></tr>" for n, s, o in OTHER) + '''</tbody></table></div></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>DPIIT:</b> publish each group&rsquo;s and item&rsquo;s contribution to the year-on-year change with every monthly WPI release.</li>
<li><b>DPIIT and MoSPI:</b> publish a concordance between WPI items and CPI items, starting with petrol, diesel, LPG, electricity, onion and edible oils.</li>
<li><b>Ministry of Petroleum and PPAC:</b> publish oil marketing companies&rsquo; monthly marketing margins, so that frozen pump prices and rising wholesale prices can be reconciled.</li>
<li><b>DPIIT:</b> publish a bridge between the 2011-12 and 2022-23 WPI series for 2025-26 and 2026-27, since earlier releases this year were on the old base.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>WPI figures are the Ministry of Commerce and Industry&rsquo;s provisional October 2026 release (base 2022-23), read through DD News, PTI and the PNB Economic Intelligence Cell. WPI inflation is the year-on-year change in the index.</li>
<li>The all-commodities index is the weighted sum of the three group indices; the group shares of the rise are weight times the change in each group index, with the October 2025 index inferred from the October 2026 index and the published inflation rate. The inferred indices are rounded, so the shares are approximate.</li>
<li>Retail figures are MoSPI&rsquo;s CPI for October 2026 (base 2024=100): general 6.09%, food 8.94%, electricity, gas and other fuels 3.71%, operation of personal transport equipment 7.52%.</li>
<li>WPI and CPI cover different goods at different stages with different weights, so the gap is a guide to where price pressure sits, not a measure of pass-through.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The Ministry&rsquo;s own release: the DPIIT page read here still held the May 2026 release (old 2011-12 base), so every WPI figure rests on press and bank reproductions of the October release. Item weights below the three groups are not given.</li>
<li>Pump-price history: the report that Delhi petrol and diesel prices are unchanged for weeks is a single source, and PPAC&rsquo;s own price series was not read.</li>
<li>Whether the series change affects comparisons: releases earlier in 2026 were on base 2011-12, so figures such as April&rsquo;s 8.3% are not on the same basis as October&rsquo;s 12.29%.</li>
<li>Causes: the release names mineral oils, crude petroleum and natural gas, electricity, food articles, basic metals, chemicals and others as drivers, but not their order. The West Asia conflict is cited in trade coverage of the energy rise, not in the release.</li>
<li>October values are provisional and are revised after ten weeks.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + mfr + fixes + method + gaps

SOURCES = (
    '<a href="https://ddnews.gov.in/en/wholesale-price-inflation-rises-to-12-29-in-october/">DD News, Wholesale price inflation rises to 12.29% in October, 16 November 2026</a> (the Ministry of Commerce and Industry release as published: group and item inflation, indices, cumulative rate); '
    '<a href="https://www.tribuneindia.com/news/wholesale-inflation-rises-to-12-29-in-october-on-higher-fuel-power-prices">The Tribune (PTI), 16 November 2026</a>; '
    '<a href="https://english.mathrubhumi.com/news/money/wpi-inflation-october-series-high-fuel-power-prices-ptiewb5qc4q">Mathrubhumi (PTI), 16 November 2026</a> (highest in the new series; economists on November); '
    '<a href="https://www.kotakneo.com/news/personal-finance/india-wholesale-inflation-rises-in-october-2026/">Kotak Neo, 16 November 2026</a> (Reuters poll median 12.1%; August final 9.92%); '
    '<a href="https://pnb.bank.in/downloadprocess.aspx?fid=CDsK1BVfPeAPDu/iZQRl/A==">PNB Economic Intelligence Cell, Macro Insights, 16 November 2026</a> (group weights; August to October inflation by group, citing the Office of Economic Adviser); '
    '<a href="https://www.fortuneindia.com/economy/wpiinflation-rises-to-1229-in-october-as-fuel-prices-surge/170468">Fortune India, 16 November 2026</a>; '
    '<a href="https://www.mospi.gov.in/uploads/latestreleasesfiles/1794480048335-Press%20Release%20of%20CPI%20for%20October%202026%20.pdf">MoSPI, CPI press release for October 2026, 12 November 2026</a> (retail comparators); '
    '<a href="https://indoen.com/news/brents-16-weekly-fall-and-a-weak-physical-market-cut-indias-crude-basket-by-us27-in-two-weeks">Indoen Research, 12 November 2026</a> (single report: Delhi pump prices). '
    'Group shares of the rise, the 6.2-point gap and the fuel ratio computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/08/indias-wholesale-prices-next-to.html", "India's wholesale prices, 14 years: the 2021–24 rise and fall was global in shape"),
    (f"{B}/2026/08/imported-fertiliser-fuel-prices-diesel.html", "Imported fertiliser and fuel prices in India: diesel, CPI and WPI, FY2012–FY2026"),
    (f"{B}/2026/08/fuel-pricing-to-crude-cost.html", "Petrol and diesel prices in India: build-up from crude cost to pump, by state"),
    (f"{B}/2026/10/every-litre-of-petrol-pays-5-for-roads.html", "Road and Infrastructure Cess: ₹5 a litre on petrol, ₹2 on diesel, none on EVs"),
    (f"{B}/2026/08/cpi-inflation-heatmap-india-june-2026.html", "CPI inflation heatmap for India, June 2026: 13 of 28 states, a 3.4-point spread"),
]

build("Prices &middot; Inflation", TITLE,
      "Wholesale prices rose 12.29% in October 2026, driven by fuel and power at 32.84%; retail inflation, at 6.09%, has so far taken on only a part of the energy rise.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
