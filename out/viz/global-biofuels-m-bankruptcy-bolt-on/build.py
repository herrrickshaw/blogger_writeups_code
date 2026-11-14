"""Visual-first edition of global-biofuels-m-bankruptcy-bolt-on. Run from the repo root:  python3 out/viz/global-biofuels-m-bankruptcy-bolt-on/build.py"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, flow, insight, line, numbers, sources_block, top_line, waterfall  # noqa: E402,F401
from viz_frame import body_links, split  # noqa: E402

SLUG = "global-biofuels-m-bankruptcy-bolt-on"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
FR = split(SRC)
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# Numbers computed from the original's numbers go in derived.json ({"190": "570/3"}), never typed in silently.

top = top_line([
    ("$2.1 billion", " in total potential claims when Global Clean Energy Holdings filed Chapter 11 on 19 April 2025; "
                     "senior lenders took 100% of new common equity and public shareholders received nothing."),
    ("$34 million", " is the final second draw on Montana Renewables&rsquo; US Department of Energy loan, cut in September 2026 "
                    "from up to $658 million; the SAF target fell from about 300 to about 200 million gallons a year."),
    ("$190 million", " in cash bought one 120 million-gallon-per-year ethanol plant from Green Plains: "
                     "ethanol deals are single plants, not company mergers."),
])

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; deal sizes, dates and parties are unchanged '
           'from the 7 November update. Values are shown in the currency each deal was quoted in and are never put on one axis.</p>\n')

s1 = insight(
    "Global Clean Energy: lenders took 100% of new common equity and shareholders got nothing",
    bars("Lenders took all new common equity and 44.4% of preferred; CTCI took 55.6%",
         [("Senior lenders led by Orion <small>new common equity</small>", 100),
          ("Senior lenders led by Orion <small>new preferred equity</small>", 44.4),
          ("CTCI <small>new preferred equity, in partial satisfaction of its claim</small>", 55.6),
          ("Public shareholders <small>new equity</small>", None)],
         accent="Senior lenders led by Orion <small>new common equity</small>", unit="%", vmax=100,
         sub="Share of the new equity after the Chapter 11 filing of 19 April 2025 in the Southern District of Texas.",
         source="Original post, section 1. Claims of about $1.1 billion secured debt and $958.5 million from CTCI Americas.")
    + numbers(["Item", "Figure"],
              [["Total potential claims", "roughly $2.1 billion"], ["Secured debt", "about $1.1 billion"],
               ["Claims of CTCI Americas, the engineering contractor", "$958.5 million"],
               ["Backing before the filing: revolving credit claims, term loans, CTCI&rsquo;s claims", "100%, 96%, 100%"]])
    + '<details class="xv-n"><summary>Why the post reads this as the renewable-diesel risk profile</summary>'
      '<p>A Bakersfield, California refinery converted to renewable diesel raised over $2 billion, was delayed more than three years, '
      'lost its offtake partner (ExxonMobil exited) and ended up handing 100% of its common equity to lenders.</p></details>\n',
    "A refinery that raised over $2 billion to convert to renewable diesel ended with lenders and its contractor holding all the new equity, "
    "which the post treats as the risk profile of the whole renewable-diesel build-out.",
    "The California Air Resources Board should publish monthly renewable-diesel and sustainable-aviation-fuel output by facility, "
    "so that distress shows up in official data before it shows up as a restructuring.",
    "bust")

s2 = insight(
    "Montana Renewables: second DOE draw cut from up to $658 million to a final $34 million",
    bars("Montana Renewables&rsquo; second DOE draw fell from up to $658 million to a final $34 million",
         [("First drawdown <small>approximately, February 2025</small>", 782),
          ("Calumet equity investment <small>alongside the first drawdown</small>", 150),
          ("Second draw as first planned <small>up to</small>", 658),
          ("Second draw as amended <small>final, September 2026</small>", 34)],
         accent="Second draw as amended <small>final, September 2026</small>", fmt=lambda v: f"${v:g} million",
         sub="US dollars, million. The loan guarantee is $1.44 billion.",
         source="Original post, section 2 and the 7 November 2026 update."),
    "The segment&rsquo;s largest capital event funded a first drawdown of approximately $782 million, but the amendment cut the SAF target "
    "to about 200 million gallons a year from about 300 and left the rest of the expansion to Montana Renewables&rsquo; own earnings.",
    "The US Department of Energy&rsquo;s Loan Programs Office should publish, for each loan guarantee, the amount committed, drawn to date "
    "and the date of each drawdown.",
    "saf")

s3 = insight(
    "Ethanol: deals were single plants of 120 and 18 million gallons a year, not mergers",
    bars("The two US ethanol plants that changed hands were 120 and 18 million gallons a year",
         [("POET buys Green Plains&rsquo; Obion, Tennessee plant <small>$190 million cash, closed 26 September 2025</small>", 120),
          ("A.E. Innovation buys Gevo&rsquo;s Agri-Energy plant, Luverne, Minnesota <small>price undisclosed, completed around November 2025</small>", 18)],
         accent="POET buys Green Plains&rsquo; Obion, Tennessee plant <small>$190 million cash, closed 26 September 2025</small>",
         fmt=lambda v: f"{v:g} million gal/yr",
         sub="Plant capacity, million gallons a year.",
         source="Original post, section 3. Gevo kept its separate isobutanol assets at the same site (roughly 1 million gallons a year).")
    + numbers(["Step", "Stake", "Price"],
              [["January 2024 tranche", "25.43%", "&#8377;35 crore"], ["June 2024 tranche", "36.34%", "&#8377;45 crore"],
               ["Total stake in Sir Shadi Lal Enterprises", "61.77%", "&#8377;80 crore combined"]],
              summary="India: how Triveni Engineering built control of Sir Shadi Lal Enterprises (not Shree Renuka Sugars)"),
    "POET paid $190 million in cash for its 35th facility and Green Plains used the proceeds to retire junior mezzanine debt due in 2026, "
    "while in India capacity build-out has so far outpaced company-level M&amp;A.",
    "The Department of Food and Public Distribution should publish a distillery-wise register of ethanol capacity, owner group and "
    "commissioning date, so that stakes such as Triveni&rsquo;s 61.77% can be read against roughly &#8377;40,000 crore of distillery investment.",
    "ethanol")

s4 = insight(
    "Daekyung O&amp;T: sold at about &#8361;500 billion, roughly 25% above its 2021 price",
    bars("Daekyung O&amp;T changed hands twice in five years, at about &#8361;400 billion then &#8361;500 billion",
         [("2021 purchase <small>SK On, Eugene Private Equity and KDB PE</small>", 400),
          ("2026 sale <small>Tenet Equity (about 80%) and HD Hyundai Oilbank (20%); signed late May, closed late June</small>", 500)],
         accent="2026 sale <small>Tenet Equity (about 80%) and HD Hyundai Oilbank (20%); signed late May, closed late June</small>",
         fmt=lambda v: f"about &#8361;{v:g} billion", vmax=500,
         sub="Korean won, billion. In its most recent reported year Daekyung had &#8361;501.3 billion revenue and &#8361;35.7 billion operating profit.",
         source="Original post, section 4.")
    + '<details class="xv-n"><summary>Biodiesel in the US, and the open distress case</summary>'
      '<p>Buffalo Biodiesel was acquired by HydroGenetics on 24 October 2025, alongside a separate $300 million growth-capital partnership '
      'with Verite Capital Partners to expand from 15 states to 25 across the eastern US.</p>'
      '<p>World Energy&rsquo;s SAF-producing Paramount, California refinery lost Air Products as funder of its SAF expansion (agreement terminated 24 February 2025) '
      'and had reportedly gone four months without producing SAF by late July 2025. No sale, bankruptcy filing or restructuring has been reported; '
      'the post calls it an open distress case and a possible second Global Clean Energy-style event.</p></details>\n',
    "Daekyung is a profitable seller of biodiesel feedstock rather than a distressed asset, which is part of why a strategic refiner paid up for feedstock security.",
    "Watch World Energy&rsquo;s Paramount refinery as the open distress case, since no sale, filing or restructuring has been reported for it.",
    "biodiesel")

deals = numbers(["Deal", "Segment", "Date", "Value or terms"],
                [["Global Clean Energy to Grapevine Energy (Chapter 11)", "Renewable diesel", "Filed April 2025; emerged mid-August 2025", "$2.1 billion claims; lenders take 100% of common equity"],
                 ["XCF Global, DevvStream and Southern Energy Renewables", "SAF", "April 2026 agreed; closed 16 October 2026", "All-stock business combination"],
                 ["Montana Renewables (Calumet) DOE loan", "SAF", "February 2025 first drawdown; amended September 2026", "$1.44 billion guarantee; $782 million drawn plus $150 million Calumet equity; second draw cut to a final $34 million"],
                 ["CMA CGM to Vanguard Renewables (minority stake)", "RNG", "August 2025", "Undisclosed; RNG from 4 projects"],
                 ["Archaea Energy to NextGen Power Holdings (historical context)", "RNG", "April to July 2022", "$215 million for 14 landfill-gas-to-electricity plants"],
                 ["POET to Green Plains (Obion, Tennessee plant)", "Ethanol", "August to September 2025", "$190 million cash, 120 million gallons a year"],
                 ["Triveni Engineering to Sir Shadi Lal Enterprises", "Ethanol (India)", "January and June 2024", "&#8377;80 crore combined, 61.77% stake"],
                 ["HD Hyundai Oilbank and Tenet Equity to Daekyung O&amp;T", "Biodiesel", "May to June 2026", "about &#8361;500 billion (roughly 25% above the 2021 price)"],
                 ["HydroGenetics to Buffalo Biodiesel", "Biodiesel", "October 2025", "Plus a separate $300 million Verite Capital growth partnership"]],
                summary="All deals in the post, each in its own currency")

fixes = '''<h2 class="gb-h2" id="fix">What would fix this</h2>
<ol>
<li><b>US Department of Energy, Loan Programs Office:</b> publish the amount committed, drawn and the date of each drawdown for every loan guarantee.</li>
<li><b>California Air Resources Board:</b> publish monthly renewable-diesel and SAF output by facility from Low Carbon Fuel Standard reporting.</li>
<li><b>Department of Food and Public Distribution:</b> publish a distillery-wise register of India&rsquo;s ethanol capacity, owner group and commissioning date.</li>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish oil marketing companies&rsquo; ethanol allocations by supplier group for each ethanol supply year.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

sections = [s1, s2, s3, s4]

extras = deals + fixes + (
    sources_block(body_links(FR.body))
)

body = STYLE + top + FR.keep_front + FR.notes + updated + "".join(sections) + extras
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
