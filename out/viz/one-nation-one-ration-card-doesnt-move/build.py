"""Visual-first edition of one-nation-one-ration-card-doesnt-move. Run from the repo root:  python3 out/viz/one-nation-one-ration-card-doesnt-move/build.py"""
import html
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "one-nation-one-ration-card-doesnt-move"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# Every figure below is in the original post (see derived.json for none needed: no new arithmetic is presented as a figure).

R = "&#8377;"

top = top_line([
    ("2.4%", " is the most that interstate use can be of ONORC&rsquo;s monthly transactions (under 0.5 million against over 20 million "
             "within states), so portability moves entitlement, not grain."),
    ("Under 12%", " of the 554.99 lakh tonne NFSA allocation is what ONORC portability delivered, about 64 lakh tonnes in the first 10 months of 2025."),
    (R + "9,000&ndash;10,000 crore", " is this post&rsquo;s own back-of-envelope gap on the 6.35 million tonnes of FCI rice sold to ethanol "
                                    "distillers roughly 40% below acquisition cost; it is not an official total."),
])

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; figures unchanged from the '
           '7 November 2026 update and the 25 October 2026 correction below.</p>\n'
           '<div class="xv-upd"><p><strong>Updated 16 November 2026:</strong> on 1 October 2026 the central pool held 840.8 lakh tonnes of wheat and rice, '
           '2.7 times the 1 October norm of 307.7 lakh tonnes (Department of Food and Public Distribution bulletin, as shown by '
           '<a href="https://tipsheet.markets/economy/rural/food">Tipsheet</a>). Wheat was about 463 lakh tonnes '
           '(<a href="https://www.thehindubusinessline.com/economy/agri-business/indian-millers-bid-higher-rates-to-get-fcis-wheat-offtake-100-in-many-states/article71645756.ece">Hindu BusinessLine, 30 October 2026</a>) '
           'and rice 377.6 lakh tonnes (<a href="https://www.livemint.com/news/governments-paddy-procurement-hit-by-weather-woes-storage-constraints/amp-11793357180974.html">Mint, 30 October 2026</a>). '
           'The 1 April 2026 stock below is an earlier reading.</p></div>\n')

s1 = insight(
    "ONORC use: at most 2.4% of monthly transactions cross a state line",
    bars("Interstate ONORC use is under 0.5 million a month, against over 20 million within states",
         [("Within one state <small>intra-state, monthly</small>", 20), ("Across states <small>interstate, monthly</small>", 0.5)],
         accent="Across states <small>interstate, monthly</small>", vmax=20,
         fmt=lambda v: "over 20 million" if v == 20 else "under 0.5 million",
         sub="ONORC transactions a month, as reported in the abstract of the 2024 IIM Ahmedabad study.",
         source="Tumbe &amp; Jha, Urbanisation (SAGE), April 2024; abstract only, the full text was not read.")
    + numbers(["Measure", "Figure"],
              [["Interstate transactions a month", "under 0.5 million"], ["Intra-state transactions a month", "over 20 million"],
               ["Maharashtra card-holders drawing grain in other states (undated snapshot)", "64,854"],
               ["Other-state card-holders drawing grain in Maharashtra (same snapshot)", "521,696"]]),
    "A beneficiary authenticates by Aadhaar at any Fair Price Shop and draws grain the shop already lifted from its own state&rsquo;s "
    "allocation, so interstate use is at most about 2.4% (0.5 of roughly 20.5 million) and nothing is trucked between states for the transaction.",
    "Read Maharashtra&rsquo;s 8-to-1 net inflow of other-state card-holders as a signal for that state&rsquo;s own allocation planning, "
    "not as a national figure, until dated interstate counts are published.",
    "share")

s2 = insight(
    "ONORC scale: about 64 lakh tonnes delivered, under 12% of the 554.99 lakh tonne allocation",
    bars("Portability delivered about 64 lakh tonnes, against a 554.99 lakh tonne yearly allocation",
         [("NFSA foodgrain allocation <small>2025-26</small>", 554.99),
          ("FCI central-pool stock <small>1 April 2026, rice and wheat</small>", 604.02),
          ("Buffer norm <small>1 April 2026</small>", 210.40),
          ("ONORC portability, all of it <small>first 10 months of 2025</small>", 64)],
         accent="ONORC portability, all of it <small>first 10 months of 2025</small>",
         fmt=lambda v: {554.99: "554.99", 604.02: "604.02", 210.4: "210.40", 64: "about 64"}[v], vmax=604.02,
         sub="Lakh tonnes. The periods differ: the ONORC figure covers 10 months of 2025, the allocation is for 2025-26.",
         source="PIB, Department of Food &amp; Public Distribution year-end review 2025 (read via a search-indexed summary); FCI stock figures corroborated across several outlets.")
    + numbers(["Figure", "Value"],
              [["ONORC portability transactions, first 10 months of 2025", "about 32.6 crore"],
               ["Foodgrain delivered through them", "about 64 lakh tonnes"],
               ["NFSA entitlement", "roughly 80 crore people"],
               ["FCI central-pool stock against buffer norm, 1 April 2026", "604.02 against 210.40 lakh tonnes, roughly three times"]]),
    "Counting every ONORC transaction, most of them within a state, portability delivered under 12% of the annual allocation, "
    "while central-pool stock stood at roughly three times its buffer norm.",
    "The Department of Food and Public Distribution should publish monthly ONORC transactions on IM-PDS split into intra-state and inter-state, "
    "with origin and destination states and grain drawn.",
    "scale")

s3 = insight(
    "FCI rice for ethanol: sold at &#8377;2,320 a quintal against a &#8377;3,889.46 acquisition cost",
    bars("FCI sold rice to ethanol distillers roughly 40% below its average acquisition cost",
         [("Average acquisition cost <small>2025-26, per quintal</small>", 3889.46),
          ("Sale price to distillers <small>notified OMSS(D) price, per quintal</small>", 2320),
          ("Gap between the two <small>roughly, per quintal</small>", 1570)],
         accent="Gap between the two <small>roughly, per quintal</small>",
         fmt=lambda v: {3889.46: R + "3,889.46", 2320: R + "2,320", 1570: R + "1,570"}[v], vmax=3889.46,
         sub="Rupees per quintal. Storage and carrying costs are not included on either side.",
         source="Rajya Sabha reply, around 29 July 2026, as reported by six outlets; gap computed by this post.")
    + numbers(["Figure", "Value"],
              [["Rice sold to distillers, June 2025 to June 2026", "6.35 million tonnes"], ["Worth", R + "14,596.78 crore"],
               ["This post&rsquo;s own estimate of the gap", R + "9,000&ndash;10,000 crore"]]),
    "On the 6.35 million tonnes sold, the gap comes to about " + R + "9,000&ndash;10,000 crore, an order-of-magnitude estimate this post "
    "multiplied out itself, and the government&rsquo;s position is that a notified fixed price is not a subsidy.",
    "The Department of Food and Public Distribution should publish each year the gap between FCI&rsquo;s economic cost of rice and the OMSS(D) price "
    "on rice sold to distillers, multiplied by tonnage.",
    "price-gap")

s4 = insight(
    "Broken-rice rule: a projected 80 to 90 lakh tonnes freed against 39 to 44 in use",
    bars("A projected 80&ndash;90 lakh tonnes of broken rice is about double the whole-grain rice used",
         [("Whole-grain FCI rice used for ethanol <small>reported, 2025-26 window</small>", (39, 44)),
          ("Broken rice freed by the June 2026 limit <small>projection, phased to 2027-28</small>", (80, 90))],
         accent="Broken rice freed by the June 2026 limit <small>projection, phased to 2027-28</small>", unit=" lakh tonnes", vmax=90, from_zero=True,
         sub="Lakh tonnes. 39 is reported as used for ethanol by June 2026 and 44.2 as issued; the projection is not yet realised.",
         source="CCEA decision, late June 2026, and a government-modalities announcement, read via search-indexed summaries.")
    + numbers(["Figure", "Value"],
              [["Broken-grain limit, raw rice", "25% to 10%"], ["Broken-grain limit, parboiled rice", "16% to 5%"],
               ["Broken rice projected freed", "8&ndash;9 million tonnes (80&ndash;90 lakh tonnes)"]]),
    "Cutting the broken-grain limit on welfare-scheme rice is projected to free roughly double the whole-grain rice now diverted, "
    "so on paper it could substitute for it, though a single report is the only source for the Food Secretary&rsquo;s plan to stop whole-grain supply.",
    "The Department of Food and Public Distribution should publish the state-wise phase-in of the June 2026 broken-grain specification "
    "and the tonnes of broken rice actually freed each season.",
    "broken-rice")

more = '''<details class="xv-n"><summary>Two different 40% figures, and the other pressures on the same grain</summary>
<ul>
<li><b>Two 40%s:</b> the ESY 2025-26 tender (Tender 22376, 23 September 2025) required FCI surplus rice to be at least 40% of a bidder&rsquo;s grain-based feedstock offer, a sourcing floor. The 40% in the price gap above is a discount, not a rule. The 7 November 2026 note says the ESY 2026-27 tender drops the floor.</li>
<li><b>Sugar side:</b> sugar-based feedstocks got 289 crore litres, 28% of the ESY 2025-26 allocation, against the roughly 54% the NITI Aayog roadmap envisaged. ISMA asks for at least 50%.</li>
<li><b>Economic Survey 2025-26:</b> reportedly flags early warning signals that maize expansion (production growth roughly 8.8% a year, area roughly 6.7%) is displacing pulses and oilseeds in Maharashtra and Karnataka. The Petroleum Ministry told Parliament that E20 has not affected food crop availability.</li>
<li><b>An inflated number:</b> a reported &#8377;1,160 crore of rice diverted in Madhya Pradesh turned out, per FCI, to concern 490 bags worth roughly &#8377;5.63 lakh; the larger figure was the value of rice legitimately issued.</li>
<li><b>Storage plan:</b> the cooperative grain storage plan targets 700 lakh tonnes, and 313 godowns completed so far deliver 1.80 lakh tonnes, roughly a quarter of one percent. It is a farmer-level scheme, not an ethanol-feedstock storage plan.</li>
</ul></details>
'''

doesnt = '''<details class="xv-n"><summary>What does not follow, and what this piece could not establish</summary>
<ul>
<li>None of this shows ONORC is poorly designed or under strain; it was built as an entitlement and settlement system so it would not need to move grain, and the data suggest that is working.</li>
<li>It is not a claim that FCI&rsquo;s ethanol-rice sales are illegal or mismanaged. The government&rsquo;s surplus-only, notified-price framing is a coherent administrative position, even where the arithmetic suggests an implicit transfer.</li>
<li>The Economic Survey describes a risk of future cropping-pattern distortion, not a claim that current food security is compromised.</li>
<li>This piece could not establish whether the cane-cost complaint belongs to ISMA or to the All India Distillers&rsquo; Association, or whether ISMA&rsquo;s position changed over time.</li>
<li>Single or search-indexed-only sourcing: the exact tender-clause wording, the Food Secretary&rsquo;s statement, the ESY 2025-26 feedstock percentages and the Economic Survey growth rates. Advance estimates and the Maharashtra snapshot are directional, not exact.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fix">Five fixes</h2>
<ol>
<li><b>Department of Food and Public Distribution:</b> publish monthly ONORC transactions on IM-PDS, split into intra-state and inter-state, so the inter-state share (at most about 2.4% on the cited abstract) is an official, dated figure.</li>
<li><b>Department of Food and Public Distribution:</b> publish each year the gap between FCI&rsquo;s economic cost of rice and the OMSS(D) price, multiplied by tonnage, so the estimate of &#8377;9,000&ndash;10,000 crore becomes an official figure.</li>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish each tender&rsquo;s allocation by feedstock beside the roadmap&rsquo;s planned split, so 28% sugar-based against roughly 54% is tracked.</li>
<li><b>Department of Food and Public Distribution:</b> publish the state-wise phase-in of the broken-grain specification and the tonnes actually freed, so the projected 8&ndash;9 million tonnes can be checked.</li>
<li><b>Ministry of Cooperation:</b> publish quarterly capacity completed under the grain storage plan against the 700 lakh tonne target.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
<p class="gb-note"><b>Corrected 25 October 2026.</b> Interstate ONORC portability was described as &ldquo;under 1%&rdquo; of transactions; the cited abstract implies roughly 2% or less (at most about 2.4%). The NFSA allocation was given as 554.93 lakh tonnes for FY2024-25; the PIB table gives 554.99 lakh tonnes for 2025-26.</p>
'''

extras = more + doesnt + fixes + sources_block([(html.unescape(u), t) for u, t in body_links(FR.body)])

body = STYLE + top + FR.keep_front + FR.notes + updated + s1 + s2 + s3 + s4 + extras
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
