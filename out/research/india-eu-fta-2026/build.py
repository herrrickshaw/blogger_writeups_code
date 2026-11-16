"""India-EU FTA: timeline to entry into force, where tariffs fall, what stays outside, exporter prerequisites.
Build from the repo root:  python3 out/research/india-eu-fta-2026/build.py   (writes out/post-india-eu-fta-signing-2026-what-exporters-need.html)
Every figure is from the source named beside it, or computed here with an assert. Read and checked 15 and 16 November 2026.
Search excerpts were read through the Parallel search tool; the Commission, PIB and Commerce pages were not opened in a browser."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

SLUG = "india-eu-fta-signing-2026-what-exporters-need"
OUT = ROOT / f"out/post-{SLUG}.html"

# ---------------------------------------------------------------- dates
# Negotiations concluded 27 Jan 2026: European Commission press release IP/26/184, https://ec.europa.eu/commission/presscorner/detail/en/ip_26_184 (27 Jan 2026)
# Commission proposals to the Council 11 Sep 2026: IP/26/1842, https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1842 (11 Sep 2026)
#   Commission steps: Council adoption, signing, Parliament consent, Council conclusion, India ratifies: https://commission.europa.eu/topics/trade/eu-india-trade-agreement_en
#   Fast track on the English text only; signing reported for 16 Dec 2026 by Indian press: European Parliament Legislative Train, https://www.europarl.europa.eu/legislative-train/theme-a-global-europe-leveraging-our-power-and-partnerships/file-eu-india-fta-bit-and-gi-agreement (undated page, read 15 Nov 2026)
# EU ambassador, 7 May 2026: legal scrubbing by the summer, signing by end of year, entry into force possibly first half of 2027: https://www.eeas.europa.eu/delegations/india/decoding-eu-india-fta-address-he-herv%C3%A9-delphin-ambassador-european-union_en
# MEA spokesperson, 29 Oct 2026: legal and procedural scrubbing ongoing, no signing date announced: https://www.newkerala.com/news/a/main-negotiating-tracks-concluded-india-eu-fta-text-undergoing-198.htm (29 Oct 2026, press report of the briefing)
# ANI/Economic Times, 2 Nov 2026: text under legal scrubbing ahead of signing proposed for mid-December: https://m.economictimes.com/news/economy/foreign-trade/india-eu-discuss-fta-implementation-customs-cooperation-and-market-access-in-brussels/amp_articleshow/135448876.cms
# David McAllister (European Parliament foreign affairs committee chair) via TOI/Economic Times, 30 Oct 2026: signing by mid-December, consent vote by spring 2027, in force by mid-2027: https://m.economictimes.com/news/economy/foreign-trade/india-eu-fta-likely-to-rollout-in-mid-2027-pm-modi-to-travel-to-brussels-for-official-signing-in-december-top-eu-lawmaker/articleshow/135341725.cms
# Hindu BusinessLine, 2 Nov 2026: signing in December in Brussels; in force early to mid-2027; phased cuts over up to ten years: https://www.thehindubusinessline.com/economy/india-eu-to-maintain-close-contact-on-fta-implementation-issues/article71657244.ece

# ---------------------------------------------------------------- tariff coverage, India's exports to the EU (share of export value)
# Commerce Ministry factsheet 27 Jan 2026 and PIB release PRID 2219146, 27 Jan 2026: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2219146
#   https://www.commerce.gov.in/files/2026-01/Factsheet-on-India-EU-trade-deal-27.1.2026_1.pdf
IMMEDIATE_LINES, IMMEDIATE_VAL = 70.4, 90.7      # % of EU tariff lines / % of India's exports, duty-free at entry into force
YEARS35_LINES, YEARS35_VAL = 20.3, 2.9           # zero duty over 3 and 5 years
REDUCED_LINES, REDUCED_VAL = 6.1, 6.0            # reduced duty or tariff-rate quotas (cars, steel, some shrimp)
COVER_VAL = 99.5                                 # preferential access, % of trade value as stated
assert abs(IMMEDIATE_VAL + YEARS35_VAL + REDUCED_VAL - COVER_VAL) <= 0.11      # 99.6 summed vs 99.5 stated: rounding in the source
assert round(IMMEDIATE_LINES + YEARS35_LINES + REDUCED_LINES, 1) == 96.8       # 96.8% of lines, as in the Commerce Ministry's FTA highlights (Mar 2026)

# ---------------------------------------------------------------- sector table (USD million, CY2024), Commerce Ministry
# PIB FAQ, PRID 2220413, 29 Jan 2026: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2220413
# Rajya Sabha starred question 158, 13 Feb 2026 (same table): https://sansad.in/getFile/annex/270/AS158_JGhmvv.pdf?source=pqars
# (sector, duty up to %, % lines duty-free at entry, exports duty-free at entry, % lines phased, exports phased)
SECTORS = [
    ("Chemicals", 12.8, 59.3, 13683.6, 39.1, 354.0),
    ("Apparel and clothing", 12.0, 100.0, 5706.3, 0.0, 0.0),
    ("Base metals", 10.0, 79.1, 3350.6, 20.9, 164.7),
    ("Gems and jewellery", 4.0, 96.6, 2661.3, 3.4, 1.1),
    ("Plastic and rubber", 6.5, 62.7, 2556.4, 37.3, 109.5),
    ("Leather and footwear", 17.0, 100.0, 2511.4, 0.0, 0.0),
    ("Textiles", 12.0, 100.0, 1636.0, 0.0, 0.0),
    ("Furniture, lighting, misc. consumer goods", 10.5, 94.2, 817.7, 5.8, 5.0),
    ("Marine products", 26.0, 94.4, 239.0, 1.9, 673.2),
    ("Railway, aircraft, ships and boats", 7.7, 88.2, 232.9, 11.8, 0.3),
    ("Toys", 4.7, 100.0, 58.8, 0.0, 0.0),
    ("Sports goods", 4.7, 100.0, 43.6, 0.0, 0.0),
]
TOT_FREE, TOT_PHASED = 33497.6, 1307.8           # the table's TOTAL row
assert round(sum(s[3] for s in SECTORS), 1) == TOT_FREE
assert round(sum(s[5] for s in SECTORS), 1) == TOT_PHASED
CHEM, APP = SECTORS[0][3], SECTORS[1][3]
TOP2_SHARE = 100 * (CHEM + APP) / TOT_FREE
assert round(TOP2_SHARE) == 58
MARINE_PHASED_SHARE = 100 * 673.2 / (239.0 + 673.2)
assert round(MARINE_PHASED_SHARE, 1) == 73.8

# ---------------------------------------------------------------- CII / Confederation of Swedish Enterprise estimate
# "EU-India Free Trade Agreement: Boosting trade and growth", Confederation of Swedish Enterprise with CII, May 2026 (model: Copenhagen Economics)
# https://www.svensktnaringsliv.se/english/publications/eu-india-free-trade-agreement-boosting-trade-and-growth_1255061.html (17 May 2026)
# PDF: https://www.svensktnaringsliv.se/sakomraden/internationell-handel/gmupk0_sn-cii-report-eu-india-free-trade-agreement-publishpdf_1255205.html/SN%20CII%20report%20EU-India%20Free%20Trade%20Agreement%20PUBLISH_1.pdf
EST_EU_EXP, EST_IN_EXP, EST_TOTAL = 71, 48, 119   # EUR bn by 2035, 2024 prices, vs a no-FTA scenario ("up to")
EST_EU_PCT, EST_IN_PCT = 47, 22                   # % above the no-FTA scenario, as stated
EST_GDP_IN, EST_GDP_EU = 72, 44                   # EUR bn; the Confederation's web page says EU GDP "almost EUR 45 billion"
assert EST_EU_EXP + EST_IN_EXP == EST_TOTAL

# ---------------------------------------------------------------- steel quota (tonnes a year)
# Annex 2-B, published 11 Sep 2026 by the Commission, via Argus, 15 Sep 2026:
# https://www.argusmedia.com/en/news-and-insights/latest-market-news/2878211-indian-steel-exporters-seek-clarity-on-eu-fta-quotas
# Reuters 14 Sep 2026 (GTRI analysis; 2.4 Mt exports in 2025): https://www.reuters.com/world/india/india-gains-wider-eu-steel-access-carbon-levy-remains-2026-09-14
# Takshashila, 12 Oct 2026: https://takshashila.org.in/content/blogs/2026-10-12-India-EU-FTA-and-its-steel-challenges.html
MFN_Q, FTA_Q = 946_616, 694_853
COMBINED_Q = MFN_Q + FTA_Q
assert COMBINED_Q == 1_641_469                    # reported as 1.64 Mt (Argus), 1,641,470 (ET Now): a one-tonne rounding difference
EXPORTS_2025 = 2_400_000                          # "2.4 million tons" in 2025 (Reuters, Crisil, LSE Grantham): a rounded figure
SH_MFN, SH_COMB = 100 * MFN_Q / EXPORTS_2025, 100 * COMBINED_Q / EXPORTS_2025
assert round(SH_MFN, 1) == 39.4 and round(SH_COMB, 1) == 68.4     # Reuters states 39.4% and 68.4%
# Three largest flat-steel categories: Annex 2-B total vs the EU's June 2026 country allocation (Argus table, from the Commission)
CATS = [("Hot-rolled coil (1.A)", 509_605, 597_274), ("Cold-rolled coil (2)", 218_658, 269_974), ("Metallic-coated sheet (4.A)", 197_860, 233_183)]
GAPS = [b - a for _, a, b in CATS]
assert GAPS == [87_669, 51_316, 35_323]

# ---------------------------------------------------------------- CBAM
# Commission CBAM Questions and Answers, 15 Oct 2026 (Q1.2, 3.1, 3.5, 4.25, 5.1, 5.9, 5.12): https://taxation-customs.ec.europa.eu/document/download/013fa763-5dce-4726-a204-69fec04d5ce2_en
MARKUP = [("2026", 10), ("2027", 20), ("2028 onwards", 30)]      # % added to default embedded-emissions values; 1% for fertilisers
assert [m[1] for m in MARKUP] == [10, 20, 30]
# CBAM certificate prices: European Commission, "Price of CBAM certificates" (Q1 7 Apr, Q2 6 Jul, Q3 5 Oct 2026): https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en
# Climate Decode, 20 Oct 2026 (same prices; FTA "does not exempt Indian exports from CBAM"; no CCTS trade yet): http://climate-decode.com/insights/india-ccts-series/cbam-q3-2026-certificate-price
# 50% additional duty above quota, India country quotas from 1 Jul 2026: Implementing Regulation (EU) 2026/1457, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML?uri=OJ:L_202601457
# Signing date: The Hindu, 23 Sep 2026 (16 December, two diplomatic sources): https://www.thehindu.com/business/Economy/india-eu-fta-to-be-signed-on-december-16/article71499760.ece
#   Hindustan Times, 25 Oct 2026 (around 17 or 18 December): https://www.hindustantimes.com/india-news/india-eu-race-to-finalise-fta-before-december-deadline-to-coincide-with-pm-modis-brussels-visit-101792926809767.html
# India merchandise exports to the EU USD 75.85 bn in 2024-25 (PIB FAQ, PRID 2220413); EU goods imports from India EUR 71 bn in 2024 (Commission memo)
PRICES = [("Q1 2026 (published 7 April)", 75.36), ("Q2 2026 (6 July)", 75.28), ("Q3 2026 (5 October)", 82.32)]
# Climate Decode, 18 Sep 2026 (CBAM annexure): http://climate-decode.com/insights/india-ccts-series/india-eu-fta-cbam-annexure
# Rajya Sabha unstarred question 695, 24 Jul 2026 (Annex on Carbon Border Measures; MFN-type clause; verifier accreditation dialogue): https://sansad.in/getFile/annex/271/AU695_i30WPX.pdf?source=pqars
# Argus, 27 Jan 2026 (Commission spokesperson: no commitment to change CBAM or give India more favourable treatment): https://www.argusmedia.com/en/news-and-insights/latest-market-news/2781007-eu-india-fta-leaves-cbam-untouched
# RIS Policy Brief 128, Feb 2026 (UN Comtrade): CBAM goods USD 6,321 million = 8.2% of India's exports to the EU in 2024; iron and steel USD 5,400 million:
#   https://www.ris.org.in/sites/default/files/Publication/Policy_Brief-128_Rajeev-Kher_and_Anshuman-Gupta.pdf
CBAM_USD, CBAM_SHARE, CBAM_STEEL_USD = 6321, 8.2, 5400
assert round(100 * CBAM_STEEL_USD / CBAM_USD) == 85          # RIS: iron and steel are 85% of India's CBAM exports to the EU
# ETV Bharat, 17 Sep 2026: six foreign institutions applied to verify for Indian exporters (Commerce Ministry officials): https://www.etvbharat.com/en/business/india-eu-fta-a-relief-for-steel-exporters-says-commerce-ministry-industry-not-convinced-enn26091705003
# CBAM Guide, 30 Jul 2026, corrected 23 Oct 2026 (only EU national accreditation bodies accredit verifiers): https://cbamguide.com/news/2026-07-30-india-eu-fta-cbam-annexure-work-plan

# ---------------------------------------------------------------- origin and standards
# Commission chapter-by-chapter memo, 27 Jan 2026 (rules of origin: statement on origin, portal; TBT working group; SPS no exception): https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/india/eu-india-agreements/memo-eu-india-free-trade-agreement-chapter-chapter-summary_en
# Khaitan & Co, 12 Oct 2026 (Annex 3-B product-specific rules, Annex 3-D authentication): https://www.khaitanco.com/sites/default/files/2026-10/12%20October%202026_India-EU%20Free%20Trade%20Agreement_Ergo.pdf
# Text of the agreements (final upon signature): https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/india/eu-india-agreements/text-agreements_en

TITLE = "India-EU FTA: 90.7% of India's exports to the EU duty-free at entry into force"
assert 55 <= len(TITLE) <= 90, len(TITLE)

# ================================================================ parts
top = top_line([
    ("16 Dec 2026", " is the signing date The Hindu reported from two diplomatic sources; Hindustan Times reported 17 or 18 December. "
                    "No official date had been announced by 29 October, and entry into force is projected for early to mid-2027."),
    (f"{IMMEDIATE_VAL}%", f" of India&rsquo;s exports to the EU by value enter duty-free at entry into force, the Commerce Ministry says. "
                          f"Another {YEARS35_VAL}% reach zero duty over 3 to 5 years and {REDUCED_VAL:g}% get reduced duty or quotas."),
    ("&euro;82.32", " per tonne of CO2e is the Commission&rsquo;s CBAM certificate price for July to September 2026. The agreement gives no CBAM exemption, "
                    "and steel above the quota faces the EU&rsquo;s 50% out-of-quota duty."),
])

# ---- S1 timeline
s1 = insight(
    "India-EU FTA timeline: signing planned for December 2026, in force expected in 2027",
    flow([
        ("27 Jan 2026", "Negotiations conclude at the India-EU summit in New Delhi (Commission press release)."),
        ("11 Sep 2026", "The Commission sends its proposals for signature and conclusion to the Council, on a fast track that completes the legal work on the English text only. "
                        "The published texts, including the steel quota annex, stay subject to legal revision."),
        ("29 Oct and 2 Nov 2026", "The Ministry of External Affairs and ANI report that legal scrubbing is still under way and that no signing date has been announced. "
                                  "The EU ambassador had aimed for scrubbing to finish by summer.", True),
        ("Mid-December 2026", "Signing in Brussels during a planned visit by the Prime Minister, reported for 16 December (The Hindu) or 17 to 18 December (Hindustan Times). "
                              "The Council has to authorise signature first; this blog found no Council decision by 16 November."),
        ("Spring 2027", "European Parliament consent vote expected, according to the chair of its foreign affairs committee. Council conclusion and India&rsquo;s ratification follow."),
        ("Early to mid-2027", "Entry into force expected. The EU ambassador said first half of 2027 in May. Tariff cuts then phase in over up to 10 years."),
    ]),
    "No preference can be claimed before entry into force, which needs signature, Parliament consent, Council conclusion and India&rsquo;s ratification, so duties in force on the import date apply until then.",
    "Exporters should price 2027 orders at current EU duties and treat the entry-into-force notice, which has not been published, as the first date on which a claim is possible.",
    "timeline")

# ---- S2 sectors
rows2 = [(f"{n} <small>EU duty up to {d:g}%</small>", v, "", f"{v:,.1f}") for n, d, _, v, _, _ in SECTORS]
acc2 = [rows2[0][0], rows2[1][0]]
s2 = insight(
    "Duty-free entry covers USD 33.5 billion of exports in 12 sectors that pay EU duty today",
    bars(f"Chemicals and apparel are about {TOP2_SHARE:.0f}% of the USD 33.5 billion in the 12 listed sectors",
         rows2, accent=acc2, unit=" USD m",
         sub="India's exports to the EU in 2024 on tariff lines that become duty-free at entry into force, USD million, as reported.",
         source="Commerce Ministry, PIB FAQ of 29 January 2026 (calendar year 2024 values). Duty figures are the highest EU duty in each sector today. "
                f"Marine products have a further USD 673.2 million, about {MARINE_PHASED_SHARE:.0f}% of the sector&rsquo;s listed exports, on lines phased in over time.")
    + numbers(["Sector", "EU duty up to", "Lines duty-free at entry", "Exports duty-free, USD m", "Lines phased", "Exports phased, USD m"],
              [[n, f"{d:g}%", f"{a:g}%", f"{v:,.1f}", f"{p:g}%", f"{pv:,.1f}"] for n, d, a, v, p, pv in SECTORS]
              + [["Total", "", "", f"{TOT_FREE:,.1f}", "", f"{TOT_PHASED:,.1f}"]],
              "Show the sector table, including lines phased in"),
    f"These sectors face EU duties of 4% to 26% today, and a May 2026 report by the Confederation of Swedish Enterprise with CII estimates up to EUR {EST_IN_EXP} billion "
    "of extra Indian exports to the EU by 2035, a modelled figure and not a forecast.",
    "Exporters should map each product to its EU tariff line, staging category and origin rule in the published schedules before quoting 2027 prices.",
    "sectors")

# ---- S3 steel quota
s3 = insight(
    "Steel enters under a quota, and CBAM applies to every tonne",
    bars(f"Published FTA text: a 1.64 Mt steel quota, about {SH_COMB:.0f}% of India's 2.4 Mt exports in 2025",
         [("Most-favoured-nation part <small>the existing WTO quota</small>", MFN_Q), ("FTA part <small>added by the agreement</small>", FTA_Q),
          ("Combined country quota in Annex 2-B", COMBINED_Q)],
         accent="Combined country quota in Annex 2-B", unit=" t", ref=(EXPORTS_2025, "India's steel exports to the EU in 2025, about 2.4 Mt (a rounded figure)"),
         sub="Annual tariff-rate quota for Indian steel in the EU, tonnes, as in Annex 2-B. A government official put the country quota at 1.9 Mt on 17 September; the two figures are not reconciled. The EU steel regulation sets a 50% duty above quota.",
         source="Annex 2-B as reported by Argus (15 September 2026) and Reuters (14 September 2026); the text is subject to legal revision. The 50% duty is in Implementing Regulation (EU) 2026/1457.")
    + numbers(["Category", "Annex 2-B total, t", "EU country allocation, June 2026, t", "Difference, t"],
              [[c, f"{a:,}", f"{b:,}", f"-{b - a:,}"] for (c, a, b) in CATS], "Show the three largest flat-steel categories against the June allocation"),
    "Steel above the quota pays the EU&rsquo;s 50% duty, by a GTRI reading of the text, and the Commission has said the agreement does not change CBAM, so every covered tonne still carries a carbon charge.",
    "Steel exporters should plan 2027 volumes around the Annex 2-B quota, not around 2025 shipments, until the Commission explains the gap of about 300,000 tonnes that Indian industry has flagged.",
    "steel")

# ---- S4 prerequisites
s4 = insight(
    "Exporter prerequisites: statement on origin, EU product rules, verified emissions data",
    bars("Default CBAM emissions values carry a mark-up that rises from 10% in 2026 to 30% from 2028",
         [(y, p) for y, p in MARKUP], accent="2028 onwards", unit="%",
         sub="Percentage added to the Commission's default embedded-emissions values for CBAM goods other than fertilisers (1%).",
         source="European Commission, CBAM Questions and Answers, 15 October 2026, question 4.25.")
    + numbers(["CBAM date or price", "Value"],
              [["Definitive period starts", "1 January 2026"], ["Certificate sales open", "1 February 2027"],
               ["First annual declaration and surrender, for 2026 imports", "30 September 2027"],
               ["Importer threshold, below which no authorisation is needed", "50 tonnes a year"]]
              + [[f"Certificate price, {q}, EUR per tonne CO2e", f"{p:.2f}"] for q, p in PRICES], "Show the CBAM dates and quarterly prices"),
    "Preference needs a statement on origin that meets the product-specific rule, EU product and food-safety rules continue to apply, and verified actual emissions replace marked-up default values for steel, aluminium and other CBAM goods.",
    "Exporters should build a bill-of-materials origin file for each product, check EU product rules such as REACH and labelling, and contract an accredited CBAM verifier in 2026 for the declaration due on 30 September 2027.",
    "prereq")

prereq = f'''<details class="xv-n"><summary>The prerequisites in detail</summary>
<ul>
<li><b>Origin proof is a statement, not an agency certificate.</b> The Commission&rsquo;s summary says origin rests on self-certification: a statement on origin, uploaded to a portal so the importing customs authority can verify it.</li>
<li><b>Origin rules are product by product.</b> Product-specific rules sit in Annex 3-B and the authentication procedure in Annex 3-D. The statement&rsquo;s form and the portal were not confirmed in the sources read.</li>
<li><b>Product standards are not waived.</b> The EU keeps its sanitary and phytosanitary rules with no exception. The technical barriers chapter sets up a working group on conformity assessment that can take up India&rsquo;s quality control orders, but it does not remove EU rules such as REACH or labelling.</li>
<li><b>Carbon verification is the importer&rsquo;s legal duty and the exporter&rsquo;s data task.</b> Only an authorised CBAM declarant may import covered goods above 50 tonnes a year. Actual emissions must be verified by an accredited verifier, which can be a third-country firm accredited by an EU national accreditation body.</li>
<li><b>Verifiers for Indian plants are few so far.</b> Commerce Ministry officials were reported on 17 September as saying six foreign institutions had applied to verify for Indian exporters. Recognition of Indian verifiers is a subject of the annex&rsquo;s technical dialogue, not an EU rule.</li>
<li><b>The CBAM annex gives process, not an exemption.</b> It extends to India any CBAM flexibility the EU gives another country and opens a dialogue on verifiers, default values and India&rsquo;s own carbon price. India has no traded carbon price to deduct yet, so the deduction is zero for 2026 goods, according to Climate Decode on 20 October.</li>
</ul></details>
'''

estimate = numbers(["The CII and Confederation of Swedish Enterprise estimate, by 2035", "EUR billion"],
                   [["Extra EU exports to India", f"up to {EST_EU_EXP} ({EST_EU_PCT}% above the no-FTA scenario)"],
                    ["Extra Indian exports to the EU", f"up to {EST_IN_EXP} ({EST_IN_PCT}% above the no-FTA scenario)"],
                    ["Extra bilateral trade, goods and services", f"up to {EST_TOTAL}"],
                    ["Higher GDP, India", f"up to {EST_GDP_IN}"], ["Higher GDP, EU", f"{EST_GDP_EU} in the report; &ldquo;almost 45&rdquo; on the Confederation&rsquo;s page"]],
                   "Show the EUR 119 billion estimate by component")
estimate_note = '''<details class="xv-n"><summary>How the EUR 119 billion estimate was built</summary>
<ul>
<li>The Confederation of Swedish Enterprise published it in May 2026 in cooperation with the Confederation of Indian Industry; the modelling is by Copenhagen Economics, using a gravity model.</li>
<li>It assumes all tariffs are removed and non-tariff barriers and services restrictions fall by 63%. The report calls the results estimates, not forecasts, and says full details of the agreement were not yet public.</li>
<li>It assumes the agreement has been in place for 10 years by 2035. With entry into force expected in 2027, the period in force would be shorter; this is this blog&rsquo;s reading.</li>
<li>Sector differences are not modelled, and some firms and sectors may lose from the competition.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="s1">What would fix this</h2>
<ol>
<li><b>The European Commission (DG Trade)</b> should publish a dated reconciliation of the Annex 2-B steel quotas with its June 2026 country allocations before signature.</li>
<li><b>India&rsquo;s Department of Commerce</b> should publish the statement-on-origin procedure, the portal and the authentication rules of Annex 3-D before entry into force.</li>
<li><b>The Commerce Ministry and the Commission, through the CBAM technical dialogue,</b> should publish the list of verifiers that can serve Indian plants and a timetable for default values.</li>
<li><b>The Bureau of Energy Efficiency</b> should finalise the iron and steel targets under the Carbon Credit Trading Scheme, so that a domestic carbon price exists to be recognised.</li>
<li><b>The Department of Commerce and DGCI&amp;S</b> should publish preferential-claim and utilisation data by sector each quarter from entry into force.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method</summary>
<ul>
<li>Dates come from the Commission&rsquo;s press releases and trade pages, Indian government statements and press reports dated 27 January to 13 November 2026. Reported dates are labelled as reported.</li>
<li>Sector values are the Commerce Ministry&rsquo;s own table for calendar year 2024, which sums to USD 33,497.6 million duty-free at entry into force and USD 1,307.8 million phased. This blog added the shares.</li>
<li>The table covers 12 sectors that pay EU duty today, not all trade: India&rsquo;s merchandise exports to the EU were USD 75.85 billion in 2024-25 (PIB), and EU goods imports from India were EUR 71 billion in 2024 (Commission).</li>
<li>Steel shares divide the Annex 2-B quota by the rounded 2.4 Mt export figure and match the shares Reuters reported (39.4% and 68.4%).</li>
</ul></details>
'''

gaps = f'''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li><b>Whether legal scrubbing is finished.</b> The last statements found, on 29 October and 2 November, say it is ongoing. No Council decision authorising signature and no official signing date were found by 16 November.</li>
<li><b>The signed text.</b> The Commission says the texts are final only on signature; every tariff schedule and quota here is as published on 11 September 2026.</li>
<li><b>Line-by-line staging.</b> The tariff schedules were not opened, so no single product&rsquo;s duty path is given.</li>
<li><b>EU-side trade data.</b> The sector values are India&rsquo;s figures; Eurostat and DG Trade data were not used to check them.</li>
<li><b>The CBAM annex text.</b> It is described from a Rajya Sabha answer, the Commission&rsquo;s position as reported, and trade-press and think-tank summaries.</li>
<li><b>FTA utilisation.</b> No claim data exists, because the agreement is not in force.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + prereq + estimate + estimate_note + fixes + method + gaps

# ================================================================ sources and related
BR = '</p><p class="gb-note" style="margin:.6rem 0 0">'
SOURCES = (
    '<b>Primary.</b> European Commission: <a href="https://ec.europa.eu/commission/presscorner/detail/en/ip_26_184">conclusion, 27 January 2026</a>; '
    '<a href="https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1842">proposals to the Council, 11 September 2026</a>; '
    '<a href="https://commission.europa.eu/topics/trade/eu-india-trade-agreement_en">next steps</a>; '
    '<a href="https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/india/eu-india-agreements/memo-eu-india-free-trade-agreement-chapter-chapter-summary_en">chapter-by-chapter summary</a>; '
    '<a href="https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/india/eu-india-agreements/text-agreements_en">text of the agreements</a>; '
    '<a href="https://taxation-customs.ec.europa.eu/document/download/013fa763-5dce-4726-a204-69fec04d5ce2_en">CBAM Questions and Answers, 15 October 2026</a>; '
    '<a href="https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en">price of CBAM certificates</a>; '
    '<a href="https://eur-lex.europa.eu/legal-content/EN/TXT/HTML?uri=OJ:L_202601457">Implementing Regulation (EU) 2026/1457</a> (steel quotas from 1 July 2026, 50% duty above quota); '
    '<a href="https://www.eeas.europa.eu/delegations/india/decoding-eu-india-fta-address-he-herv%C3%A9-delphin-ambassador-european-union_en">EU ambassador, 7 May 2026</a>. '
    + BR + 'Government of India: <a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2219146">PIB release, 27 January 2026</a>; '
    '<a href="https://www.commerce.gov.in/files/2026-01/Factsheet-on-India-EU-trade-deal-27.1.2026_1.pdf">Commerce Ministry factsheet, 27 January 2026</a>; '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2220413">PIB FAQ, 29 January 2026</a> (sector table, calendar year 2024); '
    '<a href="https://sansad.in/getFile/annex/270/AS158_JGhmvv.pdf?source=pqars">Rajya Sabha question 158, 13 February 2026</a>; '
    '<a href="https://sansad.in/getFile/annex/271/AU695_i30WPX.pdf?source=pqars">Rajya Sabha question 695, 24 July 2026</a> (CBAM annex). '
    + BR + '<b>Estimate.</b> <a href="https://www.svensktnaringsliv.se/english/publications/eu-india-free-trade-agreement-boosting-trade-and-growth_1255061.html">Confederation of Swedish Enterprise with CII, EU-India Free Trade Agreement: Boosting trade and growth, May 2026</a> '
    '(<a href="https://www.svensktnaringsliv.se/sakomraden/internationell-handel/gmupk0_sn-cii-report-eu-india-free-trade-agreement-publishpdf_1255205.html/SN%20CII%20report%20EU-India%20Free%20Trade%20Agreement%20PUBLISH_1.pdf">PDF</a>); '
    'the EUR 119 billion is a model result, read here through excerpts of the report. '
    + BR + '<b>Press and analysis, secondary.</b> <a href="https://www.thehindu.com/business/Economy/india-eu-fta-to-be-signed-on-december-16/article71499760.ece">The Hindu, 23 September 2026</a>; '
    '<a href="https://www.hindustantimes.com/india-news/india-eu-race-to-finalise-fta-before-december-deadline-to-coincide-with-pm-modis-brussels-visit-101792926809767.html">Hindustan Times, 25 October 2026</a>; '
    '<a href="https://www.thehindubusinessline.com/economy/india-eu-to-maintain-close-contact-on-fta-implementation-issues/article71657244.ece">Hindu BusinessLine, 2 November 2026</a>; '
    '<a href="https://m.economictimes.com/news/economy/foreign-trade/india-eu-fta-likely-to-rollout-in-mid-2027-pm-modi-to-travel-to-brussels-for-official-signing-in-december-top-eu-lawmaker/articleshow/135341725.cms">Economic Times, 30 October 2026</a>; '
    '<a href="https://m.economictimes.com/news/economy/foreign-trade/india-eu-discuss-fta-implementation-customs-cooperation-and-market-access-in-brussels/amp_articleshow/135448876.cms">Economic Times, 2 November 2026</a>; '
    '<a href="https://www.newkerala.com/news/a/main-negotiating-tracks-concluded-india-eu-fta-text-undergoing-198.htm">NewKerala report of the MEA briefing, 29 October 2026</a>; '
    '<a href="https://www.europarl.europa.eu/legislative-train/theme-a-global-europe-leveraging-our-power-and-partnerships/file-eu-india-fta-bit-and-gi-agreement">European Parliament Legislative Train</a> (16 December signing, as reported by Indian press). '
    + BR + '<b>Steel and CBAM, secondary.</b> <a href="https://www.reuters.com/world/india/india-gains-wider-eu-steel-access-carbon-levy-remains-2026-09-14">Reuters, 14 September 2026</a>; '
    '<a href="https://www.argusmedia.com/en/news-and-insights/latest-market-news/2878211-indian-steel-exporters-seek-clarity-on-eu-fta-quotas">Argus, 15 September 2026</a>; '
    '<a href="https://www.argusmedia.com/en/news-and-insights/latest-market-news/2781007-eu-india-fta-leaves-cbam-untouched">Argus, 27 January 2026</a>; '
    '<a href="https://takshashila.org.in/content/blogs/2026-10-12-India-EU-FTA-and-its-steel-challenges.html">Takshashila, 12 October 2026</a>; '
    '<a href="https://www.etvbharat.com/en/business/india-eu-fta-a-relief-for-steel-exporters-says-commerce-ministry-industry-not-convinced-enn26091705003">ETV Bharat, 17 September 2026</a>; '
    '<a href="http://climate-decode.com/insights/india-ccts-series/cbam-q3-2026-certificate-price">Climate Decode, 20 October 2026</a> (no CBAM exemption; no Indian carbon price to deduct) and '
    '<a href="http://climate-decode.com/insights/india-ccts-series/india-eu-fta-cbam-annexure">18 September 2026</a>; '
    '<a href="https://cbamguide.com/news/2026-07-30-india-eu-fta-cbam-annexure-work-plan">CBAM Guide, 30 July 2026, corrected 23 October</a>; '
    '<a href="https://www.ris.org.in/sites/default/files/Publication/Policy_Brief-128_Rajeev-Kher_and_Anshuman-Gupta.pdf">RIS Policy Brief 128</a> (CBAM goods USD 6,321 million, 8.2% of India&rsquo;s exports to the EU in 2024, Comtrade-based); '
    '<a href="https://www.khaitanco.com/sites/default/files/2026-10/12%20October%202026_India-EU%20Free%20Trade%20Agreement_Ergo.pdf">Khaitan &amp; Co, 12 October 2026</a>. '
    + BR + '<b>Where sources differ.</b> Signing date: 16 December (The Hindu) against 17 or 18 December (Hindustan Times); none official. '
    'Legal review: the Commission sent its proposals to the Council on 11 September, while the Ministry of External Affairs said on 29 October that legal scrubbing was ongoing. '
    'Steel exports to the EU: about 2.4 Mt in 2025 (Reuters, Crisil, LSE Grantham) against close to 3 Mt in 2025-26 (Commerce Ministry, as reported). '
    + BR + '<b>Steel quota.</b> 1.64 Mt in Annex 2-B (Argus, Reuters) against a 1.9 Mt country quota plus 0.9 Mt residual quota, reported from a government official on 17 September, and the EU&rsquo;s June allocation of about 1.94 Mt (LSE Grantham); the Annex total is about 300,000 t lower than June. '
    + BR + 'Quota total: 1,641,469 t summed here, 1,641,470 t in ET Now. EU GDP gain: 44 in the report, almost 45 on the Confederation&rsquo;s page, 45 in Firstpost. '
    'Entry into force: early to mid-2027 (BusinessLine), first half of 2027 (EU ambassador), mid-2027 (McAllister), February to March 2027 (Outlook Business, via a law-firm page). '
    + BR + '<b>Utilisation.</b> FTA utilisation data does not yet exist for this agreement, because it is not in force; claim and utilisation rates cannot be stated. '
    'Analysed 15 and 16 November 2026.')

M = json.loads((ROOT / "meta/manifest.json").read_text(encoding="utf-8"))["posts"]
BY = {p["slug"]: p for p in M.values()}
REL_SLUGS = ["what-tepa-actually-opens-efta-goods", "to-comply-or-not-to-comply-cbam-costs", "europe-wants-green-steel-it-cant-afford",
             "priority-export-destinations-by-growth", "textile-hsn-deep-dive-apparel-vs-mmf"]
RELATED = [(BY[s]["url"], BY[s]["title"]) for s in REL_SLUGS]

STANDFIRST = ("The Commerce Ministry says 90.7% of India&rsquo;s exports to the EU by value enter duty-free when the agreement takes effect. "
              "It is not signed or in force: signing is reported for December 2026 and entry into force expected in 2027. Steel is under a quota and CBAM still applies.")

build("Trade policy &middot; European Union", TITLE, STANDFIRST, body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
