"""PM-KUSUM progress and agrivoltaics estimates (MNRE replies, portal to 30 Sep 2026).
Build from the repo root:  python3 out/research/agrivoltaics-2026/build.py   (writes out/post-india-pm-kusum-agrivoltaics-nov-2026.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-pm-kusum-agrivoltaics-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- National portal, as of 30 Sep 2026 ----
A_SANC, A_INST = 10000.00, 2425.99
B_SANC, B_INST = 1307190, 1190639
CIPS_SANC, CIPS_INST = 55392, 16528
CFLS_SANC, CFLS_INST = 3536602, 1717983
PCT = {"A: grid-connected plants (MW)": 100 * A_INST / A_SANC, "B: standalone solar pumps": 100 * B_INST / B_SANC, "C: individual pump solarisation": 100 * CIPS_INST / CIPS_SANC, "C: feeder-level solarisation": 100 * CFLS_INST / CFLS_SANC}
assert [round(v, 1) for v in PCT.values()] == [24.3, 91.1, 29.8, 48.6]
# ---- Component A MW added by year (Lok Sabha USQ 1613, till 30 Jun 2026) ----
A_YEARS = [("FY2021-22", 36.0), ("FY2022-23", 63.95), ("FY2023-24", 66.33), ("FY2024-25", 397.20), ("FY2025-26", 489.47), ("FY2026-27, April to June", 673.97)]
assert round(sum(v for _, v in A_YEARS), 2) == 1726.92                       # matches Rajya Sabha USQ 300: 1,726.92 MW at 30 Jun 2026
A_30JUN, A_31JUL = 1726.92, 1986.30
assert round(A_INST - A_30JUN, 2) == 699.07 and round(A_INST - A_31JUL, 2) == 439.69
assert round(673.97 / 489.47, 2) == 1.38
# ---- Agrivoltaic potential estimates ----
MNRE_LOW, MNRE_HIGH = 3, 14          # GW, MNRE "Story of India's Solar Journey", Oct 2026
SEC_5GW = 5                          # Secretary, next 3 to 4 years (The Hindu, 19 Oct)
TERI_LOW, TERI_HIGH = 1192, 2129     # GW theoretical (Lok Sabha SQ 47)
assert round(TERI_LOW / MNRE_HIGH) == 85 and round(TERI_HIGH / MNRE_LOW) == 710
# ---- Cost ----
AVG_SUPPLY = 7.0; AGRI_LOW, AGRI_HIGH = 3.20, 3.30
PREMIUM = (25, 30)
# ---- Area ----
CROP_SUITABLE_MHA, REPORTING_MHA, GEO_MHA = 47.5, 306.96, 328.7
assert round(100 * CROP_SUITABLE_MHA / GEO_MHA) == 14 and round(100 * CROP_SUITABLE_MHA / REPORTING_MHA) == 15
AGRI_SHARE = 0.55
assert round(AGRI_SHARE * REPORTING_MHA, 1) == 168.8

TITLE = "PM-KUSUM: 24% of grid plants built; agrivoltaics estimates span 5 to 2,129 GW"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("2,426 MW", " of the 10,000 MW sanctioned for grid-connected solar plants under PM-KUSUM Component A was installed by 30 September 2026, 24%; solar pumps reached 91% of their sanction."),
    ("5 to 2,129 GW", " is the spread of agrivoltaic estimates: the MNRE Secretary expects more than 5 GW in 3 to 4 years, a slide says 3 to 14 GW, and a TERI study puts theoretical potential at 1,192 to 2,129 GW."),
    ("25 to 30%", " is how much more the minister says elevated agrivoltaic structures cost than ground-mounted solar; the next phase of PM-KUSUM is to include an agrivoltaic component."),
])

s1 = insight(
    "Solar pumps reached 91% of their PM-KUSUM sanction; grid plants 24%",
    bars("Installed share of sanction: pumps 91%, feeders 49%, individual pumps 30%, grid plants 24%",
         [(k, round(v, 1)) for k, v in sorted(PCT.items(), key=lambda kv: -kv[1])], accent="A: grid-connected plants (MW)", unit="%",
         sub="Installed or solarised as a percentage of sanction, 30 September 2026. Phase 1 ended in March 2026; the implementation timeline is extended to 31 March 2027.",
         source="National Portal for PM-KUSUM (pmkusum.mnre.gov.in), achievements as of 30.09.2026; Lok Sabha unstarred question 1613 (timeline).")
    + numbers(["Component", "Sanctioned", "Installed or solarised"],
              [["A: grid-connected plants", "10,000 MW", "2,425.99 MW"], ["B: standalone pumps", "13,07,190", "11,90,639"], ["C: individual pump solarisation", "55,392", "16,528"],
               ["C: feeder-level solarisation", "35,36,602", "17,17,983"]]),
    "Farmer-facing pumps scaled while plants that need land, tariffs and grid connection did not, which is the pattern the Centre for Science and Environment describes for Phase 1.",
    "MNRE should publish the reasons for each state&rsquo;s shortfall in Component A with the land, tariff or grid cause, before the second phase allocates new capacity.",
    "progress")

s2 = insight(
    "Component A added 674 MW in April to June 2026, more than in all of FY2025-26",
    bars("Component A added 674 MW in April to June 2026 against 489 MW in all of FY2025-26",
         A_YEARS, accent="FY2026-27, April to June", unit=" MW",
         sub="Component A solar capacity installed by year, MW, to 30 June 2026. The yearly figures add to the 1,726.92 MW that MNRE reported on that date.",
         source="Lok Sabha unstarred question 1613 (29 July 2026); Rajya Sabha unstarred question 300 (21 July 2026).")
    + numbers(["Date", "Installed, MW", "Source"],
              [["30 June 2026", "1,726.92", "Rajya Sabha question 300"], ["31 July 2026", "1,986.30", "Lok Sabha question 3911"], ["30 September 2026", "2,425.99", "PM-KUSUM portal"],
               ["End of Phase 1, March 2026", "about 2,400", "CSE, 28 October (this is higher than the 30 June figure of 1,726.92)"]]),
    "Capacity rose by 699 MW between 30 June and 30 September, but a Centre for Science and Environment figure of about 2,400 MW for the end of Phase 1 in March does not fit a 30 June total of 1,727 MW, so the dates attached to the figures need checking.",
    "MNRE should publish the installed capacity by month and state with the commissioning date, so that the dates of the 1,727 MW, 1,986 MW and 2,426 MW figures can be reconciled.",
    "capacity")

s3 = insight(
    "Agrivoltaic potential is put at 3 to 14 GW by MNRE and 1,192 to 2,129 GW by TERI",
    bars("Estimates of agrivoltaic potential differ by a factor of about 700 between sources",
         [("MNRE Secretary, in 3 to 4 years, over", SEC_5GW), ("MNRE slide, upper estimate", MNRE_HIGH), ("TERI theoretical, lower", TERI_LOW), ("TERI theoretical, upper", TERI_HIGH)],
         accent="MNRE Secretary, in 3 to 4 years, over", unit=" GW",
         sub="GW. The TERI figures are theoretical potential; the Ministry says they depend on land suitability, cropping and technical configuration.",
         source="MNRE, The Story of India's Solar Journey (October 2026); The Hindu, 19 October 2026; Lok Sabha starred question 47 (22 July 2026).")
    + numbers(["Measure", "Value", "Source"],
              [["Cropland suitable for agrivoltaics", "47.5 million hectares, 14% of India's land area", "MNRE slide"], ["Water saving in pilots", "30%", "MNRE slide"],
               ["Pilots", "100 kW at ICAR-IARI and 37 others", "Lok Sabha question 47"], ["Global installed, 2025", "18.4 GW", "Minister, 21 October 2026"],
               ["Agricultural land", "about 55% of 306.96 million hectares reporting area, 168.8 million hectares", "Drishti IAS, Land Use Statistics 2023-24"]]),
    "A spread of about 700 times between the lowest and highest estimate means the numbers describe different things, with the large ones measuring land that could host panels and the small ones measuring what states are likely to build.",
    "MNRE should publish a single agrivoltaic potential with its land, crop and tariff assumptions, so that a target in the next phase of PM-KUSUM can be set against it.",
    "potential")

s4 = insight(
    "Agrivoltaic power is put at Rs 3.20 to 3.30 a unit against Rs 7 average supply cost",
    bars("Agrivoltaic power is cited at Rs 3.20 to 3.30 a unit against Rs 7 average supply cost",
         [("Average cost of supply, 2025-26 (minister)", AVG_SUPPLY), ("Agrivoltaic generation, upper (some assessments)", AGRI_HIGH), ("Agrivoltaic generation, lower (some assessments)", AGRI_LOW)],
         accent="Agrivoltaic generation, upper (some assessments)", unit="₹/unit", fmt=lambda v: f"Rs {v:.2f}",
         sub="Rs a unit, as stated on 21 October 2026. The agrivoltaic cost holds only under specific assumptions; elevated structures cost 25 to 30% more than ground-mounted solar.",
         source="PIB, 21 October 2026, remarks by the Minister of New and Renewable Energy.")
    + numbers(["Item", "Value"],
              [["Structure premium", "25 to 30% over ground-mounted plants"], ["PM-KUSUM 2.0 financial requirement", "up to Rs 51,000 crore including existing liabilities, in public reports (CSE); not approved"],
               ["PM-KUSUM original outlay", "about Rs 34,400 crore (printed as Rs 344 billion), 2019"], ["Phase 2 plan", "dedicated agrivoltaic component"]]),
    "A generation cost that is less than half the average supply cost would make the 25 to 30% structure premium worth paying, but the figure holds only under specific assumptions that the minister did not list.",
    "MNRE should publish the assumptions behind the Rs 3.20 to 3.30 figure, including tariff, farm yield and structure cost, so that bidders and states can test them.",
    "cost")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>MNRE:</b> publish Component A installed capacity by month and state with the commissioning date, and reconcile the figures given on different dates.</li>
<li><b>MNRE:</b> publish the cause of each state&rsquo;s shortfall (land, tariff or grid) before the next phase allocates capacity.</li>
<li><b>MNRE and TERI:</b> publish one agrivoltaic potential with stated assumptions.</li>
<li><b>MNRE:</b> publish the assumptions behind the Rs 3.20 to 3.30 generation cost.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>Component A is decentralised grid-connected solar plants up to 2 MW; B is standalone solar pumps; C is solarisation of grid-connected pumps, by individual pump (IPS) or by feeder (FLS).</li>
<li>Installed share is installed divided by sanctioned on the portal date; the yearly additions are summed to check them against the reported total.</li>
<li>The 700-fold spread is TERI&rsquo;s upper figure of 2,129 GW divided by the low end of MNRE&rsquo;s slide of 3 GW.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The reason Component A capacity for March 2026 (about 2,400 MW per CSE) exceeds the 30 June total in the Rajya Sabha reply.</li>
<li>Whether the 25 to 30% premium and the Rs 3.20 to 3.30 cost refer to the same plant design.</li>
<li>How much agrivoltaic capacity exists today: 37 pilots and a 100 kW plant are reported, with no total.</li>
<li>The final outlay of PM-KUSUM 2.0, which the CSE says remains subject to approval.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://pmkusum.mnre.gov.in/g">National Portal for PM-KUSUM, achievements as of 30 September 2026</a>; '
  '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU1613_pL4wQI.pdf">Lok Sabha unstarred question 1613, 29 July 2026</a>; '
  '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU3911_80Ueu0.pdf?source=lsapps">Lok Sabha unstarred question 3911, 12 August 2026</a>; '
  '<a href="https://sansad.in/getFile/annex/271/AU300_JkXloq.pdf?source=pqars">Rajya Sabha unstarred question 300, 21 July 2026</a>; '
  '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AS47_Vp3e5K.pdf?source=lsapps">Lok Sabha starred question 47, 22 July 2026</a>; '
  '<a href="https://mnre.gov.in/static/uploads/2026/11/80f5d6e5efb892ac55998a309e7a63c4.pdf">MNRE, The Story of India&rsquo;s Solar Journey, October 2026</a>; '
  '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2326059&amp;reg=48&amp;lang=2">PIB, 21 October 2026</a>; '
  '<a href="https://www.thehindu.com/business/Industry/indias-agrivoltaic-capacity-is-expected-to-be-more-than-5-gigawatts-in-next-3-4-years-5-gigawatts/article71602893.ece">The Hindu, 19 October 2026</a>; '
  '<a href="https://www.cseindia.org/cse-offers-a-blueprint-for-making-pm-kusum-2-0-stronger-on-implementation-13310">CSE, 28 October 2026</a>; '
  '<a href="https://www.drishtiias.com/current-affairs-news-analysis-editorials/news-analysis/13-11-2026">Drishti IAS, 13 November 2026</a>. Shares computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/08/rooftop-solar-is-working-household.html", "Rooftop solar in India: over 12 GW by May 2026, household batteries unsubsidised"),
           (f"{B}/2026/09/india-let-oil-companies-put-solar-on.html", "ONGC solar on oil leases: under 1 MW built a year after the law, 4 GW bought"),
           (f"{B}/2026/10/indias-approved-solar-cell-makers-can.html", "India's approved solar-cell list: 37.8 GW a year, rooftop exemption ends 31 December"),
           (f"{B}/2026/08/basf-and-mitsubishi-are-running.html", "Rice and carbon: methane credits, Indian company schemes, Japan's solar paddies")]
build("Energy &middot; Agriculture", TITLE, "PM-KUSUM has built 24% of its grid-plant target and 91% of its pump target, and the next phase adds agrivoltaics whose estimated potential ranges from 5 to 2,129 GW.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
