"""EU CBAM certificate price (quarterly, 2026) against India's carbon credit trading scheme (CCTS): the price signal and the domestic gap.
Build from the repo root:  python3 out/research/cbam-q3-price-2026/build.py   (writes out/post-eu-cbam-price-2026-india-carbon-market-gap.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 15 November 2026."""
import datetime as dt
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-eu-cbam-price-2026-india-carbon-market-gap.html"
B = "https://blog.vertistratsolution.com"

# ---- EU CBAM certificate price, EUR per tCO2e ----
# European Commission, "Price of CBAM certificates", https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en
# (page read 15 Nov 2026): Q1 7 Apr 2026 75.36; Q2 6 Jul 2026 75.28; Q3 5 Oct 2026 82.32; Q4 due 4 Jan 2027. Weekly prices from 2027.
Q1, Q2, Q3 = 75.36, 75.28, 82.32
D_Q4, D_SALES, D_SURRENDER = dt.date(2027, 1, 4), dt.date(2027, 2, 1), dt.date(2027, 9, 30)
# Certificate sales "from February 2027" (EC price page); 1 Feb 2027 and surrender by 30 Sep 2027 from CNBC TV18, 12 Oct 2026, and Climate Decode, 20 Oct 2026.
UP_Q3_Q2 = Q3 - Q2
assert round(UP_Q3_Q2, 2) == 7.04 and round(100 * UP_Q3_Q2 / Q2, 1) == 9.4        # Climate Decode gives EUR 7.04 and 9.4%; recomputed here
assert round(Q3 - Q1, 2) == 6.96

# ---- India CCTS: no certificate trade ----
# CERC Record of Proceedings, Petitions 453/MP/2026 (PXIL), 546/MP/2026 (IEX), 574/MP/2026 (HPX), hearing 23 Oct 2026, next listing 12 Jan 2027:
#   https://cercind.gov.in/2026/ROP/453-MP-2026-Ors_231026.pdf   (CERC notes BEE "was yet to formulate the Detailed Procedure")
# BEE notice No. 45/02/NMEEE/Energy Efficiency/2025-CCTS, 19 Oct 2026, draft Detailed Procedure, comments for 15 days:
#   https://www.beeindia.gov.in/WriteReadData/RTF1984/RTF-PDF-20510f1d3ee6d4ba_1792664827.pdf
D_BEE, D_CERC, D_NEXT = dt.date(2026, 10, 19), dt.date(2026, 10, 23), dt.date(2027, 1, 12)
assert (D_NEXT - D_CERC).days == 81 and (D_NEXT - D_Q4).days == 8 and (D_SALES - D_NEXT).days == 20
assert D_Q4 < D_NEXT < D_SALES < D_SURRENDER
# Analyst expectation for first CCC price, Rs per tonne: International Carbon Trade, 10 Nov 2026 (400-900 central, 250-1,500 outer; also
# CarbonNeeti, 27 Oct 2026, "roughly INR 400 to INR 900"). ICT converts EUR 82.32 to about Rs 8,880. Single-source conversion: labelled as such.
RS_CBAM_Q3, RS_LOW, RS_HIGH, RS_OUT_LOW, RS_OUT_HIGH = 8880, 400, 900, 250, 1500
RATIO_LOW, RATIO_HIGH = RS_CBAM_Q3 / RS_HIGH, RS_CBAM_Q3 / RS_LOW
assert round(RATIO_LOW) == 10 and round(RATIO_HIGH) == 22

# ---- Exposure: EU imports of CBAM goods from India, 2025, EUR million ----
# CBAM Guide, "CBAM India", updated 12 Nov 2026, quoting Eurostat Comext DS-045409 (extracted 12 Oct 2026):
#   https://cbamguide.com/countries/india  (secondary; Eurostat itself not opened)
EU_TOTAL, EU_STEEL, EU_ALU, EU_FERT = 5300, 4390, 903.9, 4.4        # cement given as "under EUR 1 million" (disagrees with other sources; left off the chart)
assert round(100 * EU_STEEL / EU_TOTAL) == 83                                   # CBAM Guide states 83%
assert abs(EU_STEEL + EU_ALU + EU_FERT - EU_TOTAL) <= 5                         # remainder is cement (under EUR 1 million) and rounding
# Commerce Ministry officials, ETV Bharat 17 Sep 2026: "close to 3 million tonnes of steel to the EU in FY2025-26".
# Calendar 2025, Eurostat via CBAM Guide: 4.01 Mt CBAM iron and steel. Sandbag (4 Aug 2026): 4.00 Mt. Different year, scope (ferro-alloys, pig iron) and unit.

# ---- Verifiers ----
# Rajya Sabha USQ 857, 6 Feb 2026 (Commerce, Jitin Prasada): no NABCB-accredited Indian agencies recognised under EU Reg 2018/2067.
#   https://sansad.in/getFile/annex/270/AU857_zZgiIe.pdf?source=pqars
# CNBC TV18, 12 Oct 2026: six applications for recognition of Indian verification agencies, aim of at least 10; request for EU recognition of NABCB.
#   https://www.cnbctv18.com/economy/india-pushes-for-home-grown-carbon-verification-as-talks-with-eu-on-cbam-continue-20010232.htm
# S&P Global, 21 Oct 2026: BEE list of 18 Accredited Carbon Verification Agencies empanelled under the CCTS, 16 Oct 2026 (a domestic-scheme list).
V_RECOG, V_APPLIED, V_AIM, V_CCTS = 0, 6, 10, 18

# ---- EU widening of CBAM to downstream goods ----
# Commission proposal COM(2025)989, 17 Dec 2025, about 180 products, start 1 Jan 2028; Council general approach 12 Jun 2026; Parliament position
# 15 Sep 2026, 464 to 50 with 159 abstentions; first trilogue 20 Oct 2026, no overall agreement; second trilogue reported for 30 Nov 2026
# (CBAM Guide, 23 Oct 2026; Mayer Brown, 7 Oct 2026; European Parliament press release 15 Sep 2026). Council Coreper II agenda CM 4969/26, 13 Nov 2026:
#   20 Nov 2026 "Regulation on the extension of the scope of CBAM to downstream goods ... Preparation for the trilogue".
#   https://data.consilium.europa.eu/doc/document/CM-4969-2026-INIT/en/pdf
assert 464 + 50 + 159 == 673

TITLE = "EU CBAM price: €82.32 in Q3 2026, with no carbon certificate traded in India"
assert 55 <= len(TITLE) <= 80, len(TITLE)

top = top_line([
    (f"€{Q3}", f" a tonne of CO2e was the EU's CBAM certificate price for Q3 2026, {100 * UP_Q3_Q2 / Q2:.1f}% above Q2. India&rsquo;s carbon market has traded no certificate; "
               f"the €{Q3} is about Rs {RS_CBAM_Q3:,}, roughly {RATIO_LOW:.0f} to {RATIO_HIGH:.0f} times the Rs {RS_LOW}&ndash;{RS_HIGH} analysts expect (one source)."),
    ("12 Jan 2027", f" is the next date CERC lists the three exchange petitions, {(D_NEXT - D_Q4).days} days after the Q4 price (4 January) and "
                    f"{(D_SALES - D_NEXT).days} days before CBAM certificate sales open on 1 February; BEE&rsquo;s trading procedure is still a draft."),
    (f"{V_RECOG}", f" NABCB-recognised CBAM verifiers on 6 February 2026, then {V_APPLIED} applications by 12 October against a government aim of at least {V_AIM}. "
                   f"Steel is {100 * EU_STEEL / EU_TOTAL:.0f}% of the €{EU_TOTAL / 1000:.2f} billion of CBAM goods the EU imported from India in 2025."),
])

s1 = insight(
    f"EU CBAM price: €{Q1}, €{Q2} and €{Q3} in three quarters, and none yet in India",
    bars("The EU has published three CBAM prices in 2026; India&rsquo;s carbon market has none",
         [("Q1 2026", Q1, "published 7 April"), ("Q2 2026", Q2, "published 6 July"), ("Q3 2026", Q3, "published 5 October"),
          ("India CCTS certificate", None, "no exchange trade by early November 2026", "no trade")],
         accent="Q3 2026", unit="€/t", sub="Price of one CBAM certificate, € per tonne of CO2e. The Q4 price is due 4 January 2027; prices become weekly from 2027.",
         source="European Commission, Price of CBAM certificates (page read 15 November 2026); CERC record of proceedings, 23 October 2026.")
    + numbers(["Item", "Value", "Source"],
              [["Q3 against Q2", f"+€{UP_Q3_Q2:.2f}, +{100 * UP_Q3_Q2 / Q2:.1f}%", "Computed by this blog from the Commission prices"],
               ["Q3 against Q1", f"+€{Q3 - Q1:.2f}", "Computed"],
               ["Indian certificate, analyst range", f"Rs {RS_LOW}&ndash;{RS_HIGH} a tonne (outer Rs {RS_OUT_LOW:,}&ndash;{RS_OUT_HIGH:,})", "International Carbon Trade, 10 November 2026; CarbonNeeti, 27 October 2026"],
               ["Q3 price in rupees", f"about Rs {RS_CBAM_Q3:,}", "International Carbon Trade conversion; rate not stated"]]),
    "Each 2026 quarterly price is set from EU emissions-trading auctions and applies to goods imported in that quarter, so a shipment in July to September carries €82.32 whenever the certificate is bought, while an Indian certificate has no price to compare or deduct.",
    "Exporters and EU buyers should index CBAM cost clauses to the published quarterly price now and to the weekly price from 2027, and budget 2026 shipments with no Indian carbon-price deduction.",
    "price")

s2 = insight(
    "India's certificate market: two rulebooks pending before the first trade",
    flow([("27 Feb 2026", "CERC notifies the regulations for purchase and sale of Carbon Credit Certificates, with trading on power exchanges."),
          ("31 Jul 2026", "Original deadline for first-year compliance filings (Form A); a three-month extension was reported on 8 October by Carbon Pulse, as cited by Climate Decode."),
          ("16 Oct", "BEE lists 18 accredited carbon verification agencies for the scheme (S&P Global)."),
          ("19 Oct", "BEE issues the draft Detailed Procedure for transacting certificates, open for comments for 15 days; it gives no date for a first session."),
          ("23 Oct", "CERC admits petitions from PXIL, IEX and HPX, notes that BEE has not yet formulated the procedure, and lists them for 12 January 2027.", True),
          ("4 Jan 2027", "European Commission publishes the Q4 2026 CBAM price."),
          ("12 Jan 2027", "CERC hearing on the exchange petitions."),
          ("1 Feb 2027", "CBAM certificate sales open to importers; 2026 declarations and surrender are due by 30 September 2027.")]),
    f"The petitions return to CERC {(D_NEXT - D_CERC).days} days after the 23 October hearing, so first exchange trading can come only after BEE finalises its procedure and CERC approves the exchanges&rsquo; contracts, and officials&rsquo; start dates range from early 2027 (S&P Global) to the end of 2027 for most sectors (one 4 November report).",
    "BEE should publish the final procedure, the floor and forbearance prices and a first-session date, and CERC should list the exchange approvals together with the procedure.",
    "gap")

s3 = insight(
    f"CBAM goods from India: steel is {100 * EU_STEEL / EU_TOTAL:.0f}% of €{EU_TOTAL / 1000:.2f} billion in 2025",
    bars(f"Steel is {100 * EU_STEEL / EU_TOTAL:.0f}% of the EU&rsquo;s CBAM-goods imports from India; fertiliser is under €5 million",
         [("Iron and steel", EU_STEEL), ("Aluminium", EU_ALU), ("Fertilisers", EU_FERT)],
         accent="Iron and steel", unit="€ million",
         sub="EU imports from India in calendar 2025, € million. Cement is left off: sources give under €1 million, 84,000 tonnes and US$162 million (2024).",
         source="CBAM Guide, updated 12 November 2026, quoting Eurostat Comext DS-045409 (Eurostat itself not opened).")
    + numbers(["Measure", "Value", "Source"],
              [["Steel to the EU, FY2025-26", "close to 3 million tonnes", "Commerce Ministry officials, ETV Bharat, 17 September 2026"],
               ["CBAM iron and steel, calendar 2025", "4.01 Mt (Eurostat); 4.00 Mt (Sandbag)", "CBAM Guide; Sandbag, 4 August 2026"],
               ["Steel and aluminium to the EU, FY2024-25", "US$5.82 billion, down 24.4%", "GTRI, as reported by CBAM Guide"],
               ["Share of CBAM goods in India&rsquo;s EU exports, 2024", "8.2%", "RIS Policy Brief 128"]]),
    "Almost all of the exposure is steel and aluminium, the sectors where India&rsquo;s own scheme has no traded price, with iron and steel targets still in draft and no fertiliser target, so little carbon price paid at home can yet count at the border.",
    "The Commerce Ministry and the Ministry of Steel should publish EU-bound exports by CBAM product for FY2025-26 from TradeStat on one schedule, so exporters can size the 2026 bill against the €82.32 price.",
    "exposure")

s4 = insight(
    f"CBAM verifiers: {V_RECOG} NABCB-recognised, {V_APPLIED} applications, a target of {V_AIM}",
    bars(f"India has {V_CCTS} verifiers for its own scheme, none recognised for CBAM through NABCB",
         [("CCTS verification agencies", V_CCTS, "BEE list, 16 October 2026"),
          ("Applications for EU recognition", V_APPLIED, "government sources, 12 October 2026"),
          ("NABCB-recognised for CBAM", V_RECOG, "Rajya Sabha answer, 6 February 2026")],
         accent="NABCB-recognised for CBAM", unit=" agencies", ref=(V_AIM, f"government aim: at least {V_AIM} agencies apply"),
         sub="Counts of agencies, different lists and dates; the CCTS list is a domestic-scheme list, not an EU one.",
         source="BEE via S&P Global, 21 October 2026; CNBC TV18, 12 October 2026; Rajya Sabha USQ 857, 6 February 2026.")
    + numbers(["Item", "Status", "Source"],
              [["NABCB recognition by the EU", "requested; MoU with an EU-recognised accreditation body under discussion", "CNBC TV18, 12 October 2026"],
               ["Indian bodies applying under EU and UK CBAM", "2, office assessments under way", "CNBC TV18, citing the Commerce Ministry"],
               ["Verifiers documented as accredited, EU side", "7 by 12 November 2026", "CBAM Guide (Commission list unpublished)"]]),
    "Verified emissions data replaces the EU default value and its 10% mark-up in 2026, so the shortage of recognised domestic verifiers raises the CBAM bill on the same steel while the Indian certificate price stays unset.",
    "The Commerce Ministry and NABCB should publish the applicant list and assessment dates, and the Commission should state when it will rule on recognising NABCB.",
    "verifiers")

widen = '''<details class="xv-n"><summary>EU talks on widening CBAM to downstream goods</summary>
<ul>
<li><b>17 December 2025:</b> Commission proposes about 180 downstream steel and aluminium products from 1 January 2028.</li>
<li><b>12 June and 15 September 2026:</b> Council and Parliament adopt positions; Parliament&rsquo;s vote was 464 to 50 with 159 abstentions, and trade press puts its list at about 457 product types.</li>
<li><b>20 October:</b> first trilogue ends with no overall agreement, according to press reports; four issues went to technical work (an aluminium threshold, scrap, online platforms, default values).</li>
<li><b>20 November:</b> Council ambassadors (Coreper II) prepare the trilogue, per the Council agenda of 13 November. The second trilogue is reported for 30 November, not confirmed by an EU readout.</li>
<li>The counts of 180, about 200 and 457 use different units (products, codes, types) and are not final.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>BEE and CERC:</b> publish the final Detailed Procedure, the floor and forbearance prices and a first-session date, and decide the exchange petitions in one listing.</li>
<li><b>Ministry of Power and BEE:</b> notify the iron and steel and fertiliser targets so the scheme covers the sectors the EU charges.</li>
<li><b>Commerce Ministry and NABCB:</b> publish the verifier applicant list, the assessment calendar and the EU&rsquo;s decision date on recognising NABCB.</li>
<li><b>Commerce Ministry:</b> publish FY2025-26 EU-bound exports for each CBAM product from TradeStat.</li>
<li><b>European Commission:</b> state which carbon prices it will recognise under its draft Article 9 rules and what evidence an Indian certificate must carry.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>EU-bound exports by CBAM product for FY2025-26 from TradeStat: not obtained here. The sector split is Eurostat for calendar 2025 through a secondary page; the FY2025-26 steel figure is an official&rsquo;s round number.</li>
<li>Whether any Carbon Credit Certificate has been issued: no source confirms issuance, and the Q3 price comparison in rupees rests on one publisher&rsquo;s conversion and analyst range.</li>
<li>The start date for Indian trading: S&amp;P Global reports officials projecting early 2027; a 4 November report (OneStop ESG, single page) cites the BEE director for the end of 2027 for most sectors. The two are not reconciled.</li>
<li>Cement: sources disagree (under €1 million, 84,000 tonnes, US$162 million in 2024), so it is not charted.</li>
<li>The deduction rules: the Commission&rsquo;s draft Article 9 rules of 13 May 2026 are cited through Climate Decode only.</li>
</ul></details>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>CBAM prices are read from the European Commission&rsquo;s own page. The percentage changes and day counts are computed by this blog.</li>
<li>One Indian certificate (CCC) is one tonne of CO2e; the EU price is also per tonne of CO2e. The two are not like-for-like: the Indian scheme sets intensity targets and prices only the gap to target, and the EU price is an auction average.</li>
<li>The rupee comparison uses International Carbon Trade&rsquo;s own conversion of €82.32 to about Rs 8,880 and its analyst range of Rs 400&ndash;900; both come from one publisher.</li>
<li>Dates for CERC and BEE come from their own documents; exchange trading rules (monthly sessions, last Thursday) are from secondary summaries of BEE&rsquo;s draft and may change.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + widen + fixes + method + gaps

SOURCES = (
    '<a href="https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en">European Commission, Price of CBAM certificates</a> (Q1 to Q3 prices, publication dates, weekly prices from 2027; read 15 November 2026); '
    '<a href="https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en">European Commission, CBAM page</a>; '
    '<a href="https://cercind.gov.in/2026/ROP/453-MP-2026-Ors_231026.pdf">CERC record of proceedings, Petitions 453, 546 and 574/MP/2026, 23 October 2026</a>; '
    '<a href="https://www.beeindia.gov.in/WriteReadData/RTF1984/RTF-PDF-20510f1d3ee6d4ba_1792664827.pdf">BEE notice of 19 October 2026 (draft Detailed Procedure)</a>; '
    '<a href="https://sansad.in/getFile/annex/270/AU857_zZgiIe.pdf?source=pqars">Rajya Sabha USQ 857, 6 February 2026</a> and '
    '<a href="https://sansad.in/getFile/annex/271/AU695_i30WPX.pdf?source=pqars">USQ 695, 24 July 2026</a>; '
    '<a href="https://www.cnbctv18.com/economy/india-pushes-for-home-grown-carbon-verification-as-talks-with-eu-on-cbam-continue-20010232.htm">CNBC TV18, 12 October 2026</a> (verifiers, NABCB, 180 downstream products); '
    '<a href="https://data.consilium.europa.eu/doc/document/CM-4969-2026-INIT/en/pdf">Council of the EU, Coreper II agenda CM 4969/26, 13 November 2026</a>; '
    '<a href="https://www.europarl.europa.eu/news/en/press-room/20260911IPR47450/strengthening-the-eu-carbon-border-adjustment-mechanism-and-closing-loopholes">European Parliament, 15 September 2026</a>; '
    '<a href="https://cbamguide.com/news/2026-10-23-cbam-downstream-first-trilogue-no-deal">CBAM Guide, first trilogue, 23 October 2026</a> (press-report basis); '
    '<a href="https://www.mayerbrown.com/en/insights/publications/2026/10/eus-cbam-downstream-extension-and-anti-circumvention-amendments-the-road-to-trilogue">Mayer Brown, 7 October 2026</a>; '
    '<a href="https://cbamguide.com/trade/cbam-statistics/">CBAM Guide, statistics</a> (accredited verifiers, 12 November 2026); '
    '<a href="https://cbamguide.com/countries/india">CBAM Guide, India (Eurostat Comext 2025 figures, secondary)</a>; '
    '<a href="https://www.etvbharat.com/en/business/india-eu-fta-a-relief-for-steel-exporters-says-commerce-ministry-industry-not-convinced-enn26091705003">ETV Bharat, 17 September 2026</a> (Commerce Ministry, steel to the EU in FY2025-26); '
    '<a href="https://sandbag.be/wp-content/uploads/04.08.2026-Sandbag-CBAM-impact-on-India-updated.pdf">Sandbag, 4 August 2026</a>; '
    '<a href="https://ris.org.in/sites/default/files/Publication/Policy_Brief-128_Rajeev-Kher_and_Anshuman-Gupta.pdf">RIS Policy Brief 128</a>; '
    '<a href="https://www.icwa.in/show_content.php?lang=1&amp;level=1&amp;lid=8575&amp;ls_id=14132">ICWA issue brief, 16 January 2026</a> (ITC Trade Map, 2024); '
    '<a href="https://climate-decode.com/insights/india-ccts-series/cbam-q3-2026-certificate-price">Climate Decode, 20 October 2026</a> (secondary: Article 9 draft, extension of Form A deadline, UK list); '
    '<a href="https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/102126-indian-carbon-market-advances-verification-as-first-credit-issuance-nears">S&amp;P Global, 21 October 2026</a>; '
    '<a href="https://internationalcarbontrade.com/blogs/carbon-credit-price-in-india-what-a-ccc-may-cost">International Carbon Trade, 10 November 2026</a> (single-publisher rupee figures); '
    '<a href="https://carbonneeti.com/blog/carbon-credit-certificates-trading-india">CarbonNeeti, 27 October 2026</a>; '
    '<a href="https://onestopesg.com/esg-resources/article/what-is-india-carbon-credit-trading-scheme-ccts">OneStop ESG, 12 November 2026</a> (single-page report of the end-2027 start). '
    'Percentages, ratios and day counts computed by this blog. Analysed 15 November 2026.')

RELATED = [
    (f"{B}/2026/10/to-comply-or-not-to-comply-cbam-costs.html", "CBAM on Indian steel in 2026: €93 a tonne with verified data, €270 without"),
    (f"{B}/2026/08/greenhouse-emissions-reduction-and-cbam.html", "India's carbon credit scheme and CBAM: 490 entities covered by January 2026"),
    (f"{B}/2026/09/india-solved-carbon-credit-banking-with.html", "Carbon credits in India: banking has no limit or expiry, trading not yet live"),
    (f"{B}/2026/10/europe-wants-green-steel-it-cant-afford.html", "European green steel: up to twice the cost, and CBAM shuts out cheaper imports"),
]

build("Trade &middot; Climate",
      TITLE,
      "The European Commission now publishes a CBAM certificate price every quarter; India&rsquo;s carbon credit scheme has no certificate trade, so there is no Indian price to set against it.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
