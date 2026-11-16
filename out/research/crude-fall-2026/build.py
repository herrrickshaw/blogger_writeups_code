"""India and the October-November 2026 crude oil price swing: Brent, the Indian basket, the import bill and oil marketing company losses.
Build from the repo root:  python3 out/research/crude-fall-2026/build.py   (writes out/post-india-crude-basket-fall-november-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-crude-basket-fall-november-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Brent, US$ a barrel ----
# Business Standard, 6 Nov 2026: high of $118 on 30 Oct. Indoen Research, 12 Nov 2026 (settlements): 5 Nov 98.29; 6 Nov 98.32; 9 Nov 92.57; 10 Nov 91.49; 11 Nov 92.84.
# The Secretariat, 11 Nov: 91.88 on 10 Nov (an intraday print) and "approximately 22% from its 30 October high of US$118".
# Moneycontrol and 5paisa, 13 Nov: about $95.6-96.4 intraday after renewed attacks on Saudi facilities (not settlements).
BRENT = [("30 October, high", 118.0), ("5 November", 98.29), ("9 November", 92.57), ("10 November", 91.49), ("11 November", 92.84)]
FALL = 100 * (BRENT[-1][1] / BRENT[0][1] - 1)
assert round(FALL, 1) == -21.3 and round(100 * (98.32 / 118.0 - 1), 1) == -16.7
# Supply side: OPEC crude output +1.38 mb/d to 22.87 mb/d in October (The Secretariat, 11 Nov); JPMorgan estimates a surplus of 1.1 mb/d in September and 1.4 mb/d in October,
# Dated Brent at a discount to futures on 9 Nov (Morgan Stanley), via Indoen Research (secondary). Qatar- and Pakistan-mediated drafts on Hormuz transit corridors (Business Standard, 5 Nov).
# Iran's security chief said on 11 Nov that Hormuz stays shut until Washington meets seven conditions and that no talks are under way (Indoen); the accounts conflict.

# ---- Indian basket, US$ a barrel (PPAC series as quoted by the press) ----
# Hindu BusinessLine, 27 Oct 2026: August 2026 average $90.19; 26 Oct $123.72; October average to 26 Oct $120.46, highest since March 2012 ($123.61).
# The Secretariat, 12 Nov: October average $121.85, September $116.09, October 2025 $65.08 (the Hindu BusinessLine gives September as $116.77).
# Business Standard, 12 Nov: $89.29 on Tuesday 10 Nov, down from an October average of $120. Business Standard, 5 Nov: $105.39 so far in November.
# Indoen Research, 12 Nov: $96.39 on 11 Nov (aggregated price data, not PPAC); Jefferies, 13 Nov: about $97 on a 15-day average.
BASKET = [("October 2025, average", 65.08), ("August 2026, average", 90.19), ("September 2026, average", 116.09), ("October 2026, average", 121.85),
          ("26 October 2026, day", 123.72), ("10 November 2026, day", 89.29)]
DROP = 123.72 - 89.29
assert round(DROP, 2) == 34.43 and round(100 * DROP / 123.72) == 28
assert round(121.85 / 65.08, 2) == 1.87

# ---- Import bill ----
# Ministry of Commerce data as reported: crude oil imports April-September 2026 $90.6 billion, +46.3% on $61.9 billion; volume about 122-123 Mt in both periods;
# September $15.4 billion (+47%), 21.7 Mt (+7%); net oil and gas bill $81.1 billion (+35%).  Business Standard 5-6 Nov; The Secretariat 11 Nov.
CRUDE_H1_25, CRUDE_H1_26 = 61.9, 90.6
RISE = CRUDE_H1_26 - CRUDE_H1_25
assert round(RISE, 1) == 28.7 and round(100 * RISE / CRUDE_H1_25, 1) == 46.4
VOL_MT_H1 = 122.5
BBL_PER_TONNE = 7.33                                           # assumption: a standard crude conversion factor
BBL_YEAR_BN = VOL_MT_H1 * 2 * BBL_PER_TONNE / 1000
assert round(BBL_YEAR_BN, 1) == 1.8
GROSS_PER_10 = 10 * BBL_YEAR_BN                                # US$ billion a year per $10 a barrel, before product exports and other offsets
assert round(GROSS_PER_10) == 18
# Sensitivities quoted: Business Standard, 5 Nov: $10 a barrel = about $15 billion on the current account deficit; The Secretariat: $1 = $1.8-2 billion; Indoen: Rs 8,578 crore (about $0.9 billion) per $1.
INDOEN_PER_1_BN = 8578e7 / 93.69 / 1e9
assert round(INDOEN_PER_1_BN, 2) == 0.92

# ---- Oil marketing companies (OMCs) ----
# Jefferies via ANI, 13 Nov 2026: marketing losses Rs 12 a litre on petrol and Rs 27 on diesel on 15-day average pricing at a basket near $97, against Rs 22 and Rs 28 in October ($120 basket).
# ICRA's Prashant Vasisht via Business Standard, 6 Nov: October under-recoveries Rs 12 a litre on diesel and Rs 9 on petrol, and Rs 230-245 a cylinder on LPG (the petrol and diesel order differs from Jefferies').
# Hindu BusinessLine, 27 Oct: LPG under-recoveries of the three OMCs about Rs 62,000 crore.
# The Secretariat, 11 Nov: Delhi petrol Rs 102.12 and diesel Rs 95.20 on 10 Nov, unchanged since 25 May after four May rises (+Rs 7.35 petrol, +Rs 7.53 diesel; Business Standard gives Rs 7.38 and Rs 7.52);
#   the government cut excise by Rs 10 a litre in March to compensate OMCs.
LOSS = [("Petrol, October", 22), ("Petrol, now (15-day average)", 12), ("Diesel, October", 28), ("Diesel, now (15-day average)", 27)]
assert LOSS[0][1] - LOSS[1][1] == 10 and LOSS[2][1] - LOSS[3][1] == 1

TITLE = "India's crude basket: $120 in October, $89 on 10 November; pump prices frozen"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("$89.29", f" a barrel was the Indian basket on 10 November, $34 (28%) below $123.72 on 26 October; October averaged $120 to $121.85, the highest since March 2012, and Brent fell about {abs(FALL):.0f}% from its $118 high on 30 October to $92.84 on 11 November."),
    ("$90.6 billion", f" was India&rsquo;s crude import bill in April&ndash;September, up 46% on volumes that were flat at about 122&ndash;123 million tonnes, so the whole $28.7 billion rise is price."),
    ("Rs 12 and Rs 27", " a litre are Jefferies&rsquo; estimates of marketing losses on petrol and diesel on a $97 basket (Rs 22 and Rs 28 in October); Delhi pump prices have not changed since May."),
])

s1 = insight(
    f"Brent fell from $118 to $92.84 in 12 days, with supply and talks both cited",
    bars("Brent fell about 21% from its 30 October high to $92.84 on 11 November",
         BRENT, accent="11 November", unit=" $/bbl",
         sub="Brent futures, US$ a barrel; settlements except the 30 October high. It was reported near $96 intraday on 13 November after attacks on Saudi facilities.",
         source="Business Standard, 6 November 2026; Indoen Research, 12 November 2026; Moneycontrol and 5paisa, 13 November 2026.")
    + numbers(["Driver", "What was reported", "Source"],
              [["Politics", "US signals no fresh attacks on Iran while talks continue; Iran says no talks are under way and Hormuz stays shut", "Indoen Research; Business Standard"],
               ["Supply", "OPEC crude output +1.38 million barrels a day to 22.87 million in October", "The Secretariat, 11 November 2026"],
               ["Physical market", "Dated Brent at a discount to futures; JPMorgan surplus estimate 1.1 mb/d in September, 1.4 mb/d in October", "Indoen Research (secondary)"],
               ["Transit", "Qatar- and Pakistan-mediated drafts on commercial transit corridors through Hormuz", "Business Standard, 5 November 2026"]]),
    "The $118 peak on 30 October fell about 21% in 12 days on a mix of political signals and larger OPEC output, and a partial rebound to about $96 on 13 November shows how much of the move is risk premium rather than settled supply.",
    "Refiners and the petroleum ministry should plan on a range rather than the 11 November level, since the sources give both a supply glut and a closed strait as live explanations.",
    "brent")

s2 = insight(
    "The Indian basket averaged $121.85 in October, then fell to $89.29 on 10 November",
    bars("The Indian basket fell $34 in 15 days, from $123.72 on 26 October to $89.29 on 10 November",
         BASKET, accent="10 November 2026, day", unit=" $/bbl",
         sub="Indian basket of crude oil, US$ a barrel; monthly averages and single days as published by PPAC and quoted in the press.",
         source="Hindu BusinessLine, 27 October 2026; The Secretariat, 12 November 2026; Business Standard, 12 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["October 2026 average", "$120 (Business Standard); $120.46 to 26 October (Hindu BusinessLine); $121.85 full month (The Secretariat)", "differences are coverage"],
               ["September 2026 average", "$116.09 (The Secretariat); $116.77 (Hindu BusinessLine)", "unreconciled"],
               ["Level after 10 November", "$96.39 on 11 November (Indoen, aggregated); about $97 on a 15-day average (Jefferies)", "does not match $89.29 for 10 November"],
               ["October against October 2025", f"{121.85 / 65.08:.2f} times", "computed from The Secretariat"]]),
    "The basket fell 28% in 15 days, but October&rsquo;s average of about $120 is already priced into the cargoes bought and the bills paid, so the drop shows in the import figures with a lag.",
    "PPAC should publish the daily basket, the monthly average and the number of days behind it in one table, since press reports of October&rsquo;s average range from $120 to $121.85 and November&rsquo;s level from $89 to $97.",
    "basket")

s3 = insight(
    "Crude imports cost $90.6 billion in April to September, 46% more on flat volumes",
    bars("Crude imports cost $28.7 billion more in April to September on flat volumes",
         [("April to September 2025", CRUDE_H1_25), ("April to September 2026", CRUDE_H1_26)], accent="April to September 2026", unit=" $ billion",
         sub="India&rsquo;s crude oil import bill, US$ billion. Volumes were about 122&ndash;123 million tonnes in both periods.",
         source="Commerce Ministry data as reported by Business Standard, 6 November 2026, and The Secretariat, 11 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Crude import bill, September", "$15.4 billion, +47%, on 21.7 Mt (+7%)", "The Secretariat"],
               ["Net oil and gas bill, April&ndash;September", "$81.1 billion, +35%", "Business Standard"],
               ["Annual imports (computed)", f"about {BBL_YEAR_BN:.1f} billion barrels a year (122.5 Mt per half-year &times; 2 &times; {BBL_PER_TONNE} barrels a tonne, an assumed conversion)", "Computed here"],
               ["Per $1 a barrel", f"about ${BBL_YEAR_BN:.1f} billion a year gross (The Secretariat: $1.8&ndash;2 billion); Indoen Research: Rs 8,578 crore, about ${INDOEN_PER_1_BN:.1f} billion", "sources disagree"],
               ["Per $10 a barrel", "about $15 billion on the current account deficit (Business Standard); $18 billion gross (computed)", "gross is before product exports"],
               ["Record October imports", "5.54 million barrels a day, up 9% on September and on October 2025", "The Secretariat"]]),
    f"Volumes barely moved while the bill rose $28.7 billion, so price explains the whole rise, and at about {BBL_YEAR_BN:.1f} billion barrels a year each $10 a barrel is worth about $15 billion to $18 billion depending on what is netted.",
    "The Commerce Ministry should publish the crude bill with volume, average price and the share of term and spot cargoes each month, so the lag between the basket and the bill can be seen.",
    "bill")

s4 = insight(
    "Marketing losses on petrol fell from Rs 22 to Rs 12 a litre, on diesel from Rs 28 to Rs 27",
    bars("Marketing losses: petrol Rs 22 to Rs 12 a litre, diesel Rs 28 to Rs 27, on a $97 basket",
         LOSS, accent=["Petrol, now (15-day average)", "Diesel, now (15-day average)"], unit=" Rs/litre", fmt=lambda v: f"Rs {v:.0f}",
         sub="Estimated losses on selling petrol and diesel at frozen prices, rupees a litre, on 15-day average pricing. Jefferies figures; ICRA gives different October values.",
         source="Jefferies, as reported by ANI, 13 November 2026; Business Standard, 6 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Delhi pump prices, 10 November", "petrol Rs 102.12, diesel Rs 95.20; unchanged since 25 May", "The Secretariat; Indoen Research"],
               ["May 2026 rises", "four rises: petrol +Rs 7.35 or Rs 7.38, diesel +Rs 7.53 or Rs 7.52", "The Secretariat; Business Standard"],
               ["Excise cut", "Rs 10 a litre in March, to compensate OMCs, not to cut pump prices", "The Secretariat"],
               ["ICRA, October under-recoveries", "diesel Rs 12 and petrol Rs 9 a litre; Rs 230&ndash;245 a cylinder on LPG", "Business Standard, 6 November 2026"],
               ["LPG under-recoveries", "about Rs 62,000 crore for the three OMCs", "Hindu BusinessLine, 27 October 2026"],
               ["HPCL exposure", "refining-to-marketing ratio 51%, against 74% for BPCL and 80% for IOC", "Business Standard, 5 November 2026"]]),
    "A $23 fall in the basket cut the petrol loss by Rs 10 a litre but the diesel loss by only Re 1, and LPG losses remain, so the fall has not yet restored OMC marketing margins on the fuels that are priced below cost.",
    "The petroleum ministry should publish the under-recovery on petrol, diesel and LPG each fortnight with the basket price used, so the Jefferies and ICRA numbers can be compared with an official one.",
    "omc")

assert round(120 - 97) == 23

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>PPAC:</b> publish the daily Indian basket, the monthly average and the days it covers in one table, with the Brent weighting used.</li>
<li><b>Ministry of Commerce and Industry:</b> publish crude import volume, price and the term-spot split each month so the lag between the basket and the import bill is visible.</li>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish fortnightly under-recoveries on petrol, diesel and LPG, with the basket price behind them.</li>
<li><b>Ministry of Finance and the Ministry of Petroleum:</b> state how the March excise cut will be treated as OMC margins recover, since it was introduced to compensate losses.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The Indian basket is the PPAC series of the crude oil India buys, weighted between sour and sweet grades; this blog&rsquo;s earlier piece on the basket explains that Brent has a 61% weight in it. Basket values here are as quoted in press reports of the PPAC series; PPAC&rsquo;s own table was not read.</li>
<li>Brent values are futures settlements as reported by Indoen Research, except the 30 October high and the 13 November intraday readings.</li>
<li>The import-volume conversion (7.33 barrels a tonne) is an assumed factor; the per-barrel sensitivity is gross and does not net product exports, which is one reason the quoted sensitivities differ.</li>
<li>Marketing loss is the gap between the cost-based price and the frozen retail price before taxes and dealer margins as each analyst defines it; Jefferies and ICRA do not use the same basis.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>PPAC&rsquo;s own daily basket was not read; the $89.29 for 10 November is a Business Standard figure attributed to PPAC, and two other sources put the basket near $96&ndash;97 for 11 November and the 15-day average.</li>
<li>Why the pump prices have not changed since May, and whether the Rs 10 excise cut will be reversed: the sources describe the freeze and the cut, not the policy intent beyond compensation.</li>
<li>A Mumbai diesel price site reports no change since 5 September; Delhi sources report none since 25 May. The two are not reconciled here and may reflect state-level changes.</li>
<li>The Brent rebound after 11 November rests on intraday readings reported on 13 November; later settlements were not read.</li>
<li>The petrol and diesel order of ICRA&rsquo;s October figures is reversed against Jefferies&rsquo;; the difference is not explained in the reports.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://indoen.com/news/brents-16-weekly-fall-and-a-weak-physical-market-cut-indias-crude-basket-by-us27-in-two-weeks">Indoen Research, 12 November 2026</a> (Brent settlements; physical market; aggregated basket; secondary); '
    '<a href="https://www.business-standard.com/economy/news/crude-oil-retreat-may-offer-india-macroeconomic-relief-in-h2-of-fy27-126111201233_1.html">Business Standard, 12 November 2026</a> (basket $89.29 on 10 November; October average; WPI); '
    '<a href="https://www.business-standard.com/industry/news/crude-price-cool-off-likely-to-soften-cost-squeeze-on-oil-companies-126110502070_1.html">Business Standard, 5 November 2026</a> (basket in November; OMCs; sensitivity; import bill); '
    '<a href="https://www.business-standard.com/industry/news/oil-set-for-biggest-weekly-drop-may-bring-relief-for-india-s-oil-bill-126110601681_1.html">Business Standard, 6 November 2026</a> (30 October high; ICRA on under-recoveries); '
    '<a href="https://thesecretariat.in/article/crude-oil-prices-fall-india-import-bill-petrol-diesel-prices">The Secretariat, 11 November 2026</a> and '
    '<a href="https://thesecretariat.in/article/will-indias-sweet-spot-for-russian-crude-last">12 November 2026</a> (import bill; basket averages; pump prices; OPEC output); '
    '<a href="https://www.thehindubusinessline.com/economy/oil-import-bill-rises-on-west-asia-conflict/article71632295.ece">The Hindu BusinessLine, 27 October 2026</a> (basket to 26 October; LPG under-recoveries); '
    '<a href="https://www.aninews.in/news/business/omcs-losses-narrow-as-crude-cools-but-still-stand-at-rs-12l-on-petrol-and-rs-27l-on-diesel-jefferies20261113123958">ANI, 13 November 2026</a> (Jefferies marketing losses); '
    '<a href="https://iocl.com/admin/uploads/IOCL_Transcript_Q2_26-27.pdf">Indian Oil Q2 FY27 conference call transcript, 31 October 2026</a> (basket about $120 in October). '
    'Percentage changes, the volume conversion and the sensitivity ratios computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/10/indias-crude-basket-now-counts-russian.html", "India's crude basket: Brent weighted at 61%, while most imported barrels are sour"),
    (f"{B}/2026/08/fuel-pricing-to-crude-cost.html", "Petrol and diesel prices in India: build-up from crude cost to pump, by state"),
    (f"{B}/2026/08/you-cannot-substitute-crude-oil-or-gold.html", "India's import bill: 40% is crude oil and gold, which cannot be substituted"),
    (f"{B}/2026/08/thermal-parity-is-dead-what-85-oil-and.html", "Oil-gas decoupling: $85 oil, a $7 gas ceiling and India's crude-linked formula"),
    (f"{B}/2026/08/the-margin-case-why-lpg-and.html", "Indian refining margins: $4–6 a barrel, with LPG and petrochemicals beating petrol"),
]

build("Energy &middot; Oil", TITLE,
      "Brent fell about 21% from its 30 October high and the Indian basket fell $34 in 15 days; the import bill is up 46% on flat volumes and pump prices have not changed since May.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
