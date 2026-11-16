"""India-US interim trade agreement, 16 November 2026: what is in force, what is open, and the dates ahead.
Build from the repo root:  python3 out/research/us-trade-deal-2026/build.py   (writes out/post-india-us-trade-deal-tariffs-open-items-nov-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-us-trade-deal-tariffs-open-items-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Section 301 forced-labour duty on India ----
# PIB (Ministry of Commerce and Industry), 25 Jul 2026, PRID 2289348: USTR announced final measures on 23 Jul 2026; additional 10% ad valorem on imports from India
#   (12.5% had been proposed on 2 Jun 2026); products already under Section 232 (steel, aluminium, auto parts) are outside it; generic pharmaceuticals and smartphones stay at zero;
#   "an estimated 45% of India's exports to the United States remain outside the purview of the additional 10% duty"; the remaining 55% attract it; the textile-specific mechanism
#   "is yet to be established and operationalised".   https://www.pib.gov.in/PressReleasePage.aspx?PRID=2289348&lang=1&reg=3
# Federal Register, 28 Jul 2026, 91 FR 47318 (doc 2026-15181): 10% on goods of India, "except as provided in Annex I and Annex II, Part A"; India adopted a forced-labour import
#   prohibition after the 5 Jun 2026 notice.  https://www.federalregister.gov/documents/2026/07/28/2026-15181/
# USTR press release, July 2026: 10% tier = Argentina, Bangladesh, Cambodia, Canada, Ecuador, El Salvador, Guatemala, Honduras, India, Indonesia, Jordan, Malaysia, Mexico, Pakistan,
#   Sri Lanka, Trinidad and Tobago, UK; EU and Taiwan: 10% net of MFN; Japan, Korea, Switzerland: 12.5% net of MFN; all other investigated economies 12.5%.
SHARE_OUT, SHARE_IN = 45, 55
assert SHARE_OUT + SHARE_IN == 100
RATE_INDIA, RATE_PROPOSED = 10, 12.5
# ELP (law firm), 24 Jul 2026 (secondary): India's 10% is "in addition to the ordinary MFN duty"; no MFN cap as for the EU, Taiwan, Japan, South Korea and Switzerland;
#   FY2025-26 goods exports to the US about $87 billion, imports about $54 billion (not checked against TradeStat).
EXPORTS_US_BN = 87
IN_SCOPE_BN = EXPORTS_US_BN * SHARE_IN / 100
assert round(IN_SCOPE_BN) == 48

# Illustration: a product with a normal (MFN) US duty of 5%. India, Bangladesh, Cambodia, UK: MFN + 10; EU, Taiwan: the higher of MFN and 10; Japan, Korea, Switzerland: the higher of MFN and 12.5.
MFN = 5.0
TOTAL = {"India, Bangladesh, Cambodia, UK (10% on top)": MFN + 10, "Japan, Korea, Switzerland (12.5% total)": max(MFN, 12.5), "EU, Taiwan (10% total)": max(MFN, 10.0),
         "China, Brazil and other 12.5% economies (12.5% on top)": MFN + 12.5}
assert TOTAL["India, Bangladesh, Cambodia, UK (10% on top)"] == 15.0 and TOTAL["EU, Taiwan (10% total)"] == 10.0 and TOTAL["Japan, Korea, Switzerland (12.5% total)"] == 12.5
assert TOTAL["China, Brazil and other 12.5% economies (12.5% on top)"] == 17.5

# ---- Legal timeline ----
# ATB Legal, 22 Oct 2026 (secondary summary of statutes and orders): framework 6 Feb 2026 with an 18% rate that never took effect; extra 25% Russian-oil tariff removed from 7 Feb.
# CRS Legal Sidebar LSB11398, 23 Feb 2026: Learning Resources v. Trump, 20 Feb 2026, IEEPA does not authorise tariffs.
# MEA, Lok Sabha USQ 5525, 27 Mar 2026: reciprocal tariffs no longer in force; Section 122 10% surcharge for 150 days from 24 Feb 2026.
# Federal Register 91 FR 12886, 17 Mar 2026: Section 301 excess-capacity investigations; economies: Bangladesh, Cambodia, China, EU, India, Indonesia, Japan, Malaysia, Mexico, Norway,
#   Singapore, South Korea, Switzerland, Taiwan, Thailand, Vietnam (Trade Compliance Resource Hub tracker, 3 Nov 2026).
EXCESS_CAP = ["Bangladesh", "Cambodia", "China", "European Union", "India", "Indonesia", "Japan", "Malaysia", "Mexico", "Norway", "Singapore", "South Korea", "Switzerland", "Taiwan", "Thailand", "Vietnam"]
assert len(EXCESS_CAP) == 16
# Hindu BusinessLine, 12 Nov 2026: India wants the excess-capacity result before settling tariff terms; Democrats won both chambers in the 3 Nov mid-terms; the 60-day waiver under the
#   Sanctioning Russia and Iran Act issued in October; a two-member US team visited Delhi on 2-3 Nov on customs and trade facilitation.
# PTI / Business Standard, 14 Nov 2026: Jaishankar, "last stretch"; G20 summit in Miami 14-15 Dec; Modi-Trump meeting likely. New Indian Express and Rediff, 14 Nov: US assured India a comparative
#   tariff advantage over rivals; the legal text to include safeguards against additional duties.
# ATB Legal: Pub. L. 119-111 s.113: duties up to 100% on the five largest buyers of Russian crude or gas from 18 Oct 2026 unless waived; not applied to India as at 12 Oct.

TITLE = "India-US trade deal, November 2026: 10% duty in force, agreement text unsigned"
assert 55 <= len(TITLE) <= 80, len(TITLE)

top = top_line([
    ("10%", f" Section 301 duty applies to goods of India since 24 July 2026, on top of the normal duty; USTR proposed 12.5% in June. About {SHARE_IN}% of India&rsquo;s exports to the US pay it and about {SHARE_OUT}% do not (a PIB estimate)."),
    ("0", " signed texts of an India-US interim agreement. The 6 February framework&rsquo;s 18% rate was never applied, and on 20 February the Supreme Court held that the emergency-powers law behind it does not authorise tariffs."),
    ("16", " economies, India among them, are in a second Section 301 inquiry, on excess capacity, with no result; trade-press reports say India wants it before settling tariffs. The G20 summit in Miami, 14&ndash;15 December, is the next likely date."),
])

s1 = insight(
    "About 55% of India's exports to the US pay the 10% duty, and about 45% do not",
    bars("An estimated 45% of India's US exports are outside the 10% duty; 55% attract it",
         [("Pay the additional 10% duty", SHARE_IN), ("Outside it (Section 232 goods, exempted lines)", SHARE_OUT)],
         accent="Pay the additional 10% duty", unit="%",
         sub="Estimated share of India&rsquo;s goods exports to the US, per cent. Steel, aluminium and auto parts pay Section 232 rates instead; generic pharmaceuticals and smartphones stay at zero extra duty.",
         source="PIB, Ministry of Commerce and Industry, 25 July 2026; USTR notice, 91 FR 47318.")
    + numbers(["Measure", "Value", "Source"],
              [["Additional duty on India", f"{RATE_INDIA}% (12.5% proposed on 2 June 2026), on top of the normal duty", "PIB; Federal Register"],
               ["Share outside / inside the duty", f"{SHARE_OUT}% / {SHARE_IN}% of exports to the US (estimate)", "PIB"],
               ["Goods exports to the US, FY2025-26", f"about ${EXPORTS_US_BN} billion; the 55% would be about ${IN_SCOPE_BN:.0f} billion", "ELP (law firm), secondary; computed here"],
               ["Textile-specific mechanism", "referenced in the final measures, not yet established; India not among the economies contemplated for it", "PIB; ELP"]]),
    f"With the duty covering about {SHARE_IN}% of exports, on the ELP figure of about ${EXPORTS_US_BN} billion of goods exports that is roughly ${IN_SCOPE_BN:.0f} billion a year of trade paying an extra 10%.",
    "The Commerce Ministry should publish the exempted share by HS chapter and value, since the 45% is an estimate and exporters cannot see which lines it covers.",
    "coverage")

s2 = insight(
    "India's 10% is added to the normal duty; the EU and Taiwan pay 10% in total",
    bars("On a product with a 5% normal duty, India pays 15% in total and the EU and Taiwan 10%",
         [(k, v) for k, v in TOTAL.items()], accent="India, Bangladesh, Cambodia, UK (10% on top)", unit="%",
         sub="Illustration only: total US duty, per cent, on a product with a 5% normal (MFN) duty, assuming no other duty. Real rates vary by product.",
         source="USTR press release, July 2026 (tiers); ELP, 24 July 2026 (India has no MFN cap); the 5% is an assumption of this blog.")
    + numbers(["Tier", "Rule", "Source"],
              [["India, Bangladesh, Cambodia, UK and others", "10% on top of the normal duty", "USTR; Federal Register"],
               ["EU and Taiwan", "10% in total: the 301 duty is only what is needed to reach 10%", "USTR"],
               ["Japan, South Korea, Switzerland", "12.5% in total", "USTR"],
               ["All other investigated economies", "12.5% on top, per USTR&rsquo;s rule", "USTR"]]),
    "Because India&rsquo;s 10% is added to the normal rate while the EU&rsquo;s and Taiwan&rsquo;s totals are capped at 10%, an Indian exporter pays at least as much in total as an EU or Taiwanese competitor on every line, and more wherever the normal duty is above zero.",
    "Exporters should compare total landed duty by product line against EU, Taiwanese and Japanese rivals, not the headline tier, because the headline is not the competitive measure.",
    "stacking")

s3 = insight(
    "The 18% rate announced in February never applied; three legal bases replaced it",
    flow([("6 Feb 2026", "India and the US announce a framework for an interim agreement with an 18% US rate; the extra 25% Russian-oil tariff is removed from 7 February (ATB Legal)."),
          ("20 Feb", "The US Supreme Court holds, 6 to 3, that IEEPA does not authorise tariffs; the reciprocal tariff behind the 18% ends."),
          ("24 Feb", "A 10% temporary surcharge under Section 122 starts for 150 days (MEA reply to the Lok Sabha, 27 March)."),
          ("17 Mar", f"USTR opens a second Section 301 inquiry, into excess capacity, covering {len(EXCESS_CAP)} economies including India (91 FR 12886)."),
          ("24 Jul", "The Section 301 forced-labour duty of 10% on India takes effect as the Section 122 surcharge expires (PIB; USTR).", True)]),
    "The 18% was tied to a statute the Court then excluded, so what India pays today is a different duty under a different law with no signed agreement beneath it.",
    "The US and Indian governments should publish the framework text and the legal basis intended for the agreed rate, since the February joint statement named a rate but not an authority.",
    "timeline")

s4 = insight(
    "Four items are open: the text, the excess-capacity result, the Russia-oil law and textiles",
    flow([("Pending", "Interim agreement text: not published; officials describe a last stretch, and the US has promised India a comparative tariff advantage with safeguards against extra duties (PTI, 14 November)."),
          ("Pending", f"Result of the excess-capacity Section 301 inquiry into {len(EXCESS_CAP)} economies; trade-press reports say India wants it before settling tariff terms."),
          ("Oct to Dec", "The Sanctioning Russia and Iran Act allows duties of up to 100% on the largest buyers of Russian oil from 18 October unless waived; a 60-day waiver was issued in October (Hindu BusinessLine, 12 November)."),
          ("Pending", "Textile-specific mechanism referenced in the July measures: not yet set up, with India not among the economies contemplated (PIB; ELP)."),
          ("14&ndash;15 Dec", "G20 summit in Miami; a Modi-Trump meeting is likely and an announcement is speculated, not confirmed (PTI; CNBC).", True)]),
    "India wants protection from the sanctions law and clarity on the excess-capacity result before it settles tariff terms, and the US side still has to finish its own tariff framework, so the order of those decisions sets the timing more than the December meeting does.",
    "The Commerce Ministry should state which of the four items it treats as conditions for signing, so exporters can plan around the likely order.",
    "open")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Commerce and Industry:</b> publish the share of exports outside the 10% duty by HS chapter, with the annexes of the Federal Register notice that define it.</li>
<li><b>Ministry of Commerce and Industry and USTR:</b> publish the framework text, the legal authority intended for the agreed rate, and the safeguards promised against additional duties.</li>
<li><b>Ministry of Commerce and Industry:</b> publish a list of conditions for signing, naming the excess-capacity result, the sanctions-law protection and the textile mechanism.</li>
<li><b>Export promotion councils:</b> publish landed-duty comparisons against EU, Taiwanese and Japanese suppliers by product line.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>&ldquo;Section 301 duty&rdquo; is the additional duty imposed on 24 July 2026 after USTR&rsquo;s forced-labour investigations of about 60 economies; it is charged in addition to the ordinary (MFN) duty for India. EU, Taiwan, Japan, South Korea and Switzerland are capped on a total basis.</li>
<li>The 45% and 55% are the Ministry&rsquo;s estimate of the share of exports to the US outside and inside the duty, as published by PIB on 25 July; the dollar value of the 55% multiplies a secondary-source export total by that share.</li>
<li>The stacking chart is an illustration with an assumed 5% normal duty; the rule for each tier is USTR&rsquo;s, and real rates depend on the product line.</li>
<li>The dates of the Supreme Court judgment, Section 122 surcharge and the Section 301 notice are from official documents (CRS, the MEA reply and the Federal Register); the framework&rsquo;s 18% and the 25% Russian-oil removal are from a law-firm summary.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The framework text of 6 February: it was not read; the 18% rate and other terms are from a law-firm summary and Indian parliamentary replies.</li>
<li>Whether Vietnam pays 10% or 12.5%: USTR&rsquo;s own list of the 10% tier does not name it, while a third-party tracker lists it at 10%; this piece does not rely on it.</li>
<li>The waiver&rsquo;s end date under the Sanctioning Russia and Iran Act: Hindu BusinessLine reports a 60-day waiver issued in October without a date, and it could not be confirmed here.</li>
<li>The result and timing of the excess-capacity inquiry, and the effect of the Democratic win in both houses of Congress on 3 November: reports say the executive keeps Section 232 and 301 tools, not that the timing is changed.</li>
<li>Refunds: IEEPA and Section 122 refunds go to the importer of record, not the Indian exporter, and their status was not tracked here.</li>
<li>Whether a deal will be announced at the G20: reports say it is likely or speculated; no source confirms it.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2289348&amp;lang=1&amp;reg=3">PIB, Final US Section 301 Measures on Forced Labour, 25 July 2026</a> (10% tier, 45% and 55% estimate, textile mechanism); '
    '<a href="https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies">Federal Register, 91 FR 47318, 28 July 2026</a>; '
    '<a href="https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations">USTR press release, July 2026</a> (tiers); '
    '<a href="https://www.congress.gov/crs-product/LSB11398">Congressional Research Service, LSB11398, 23 February 2026</a> (Supreme Court on IEEPA); '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU5525_tDtsku.pdf?source=pqals">Ministry of External Affairs, Lok Sabha unstarred question 5525, 27 March 2026</a>; '
    '<a href="https://www.tradecomplianceresourcehub.com/2026/11/03/trump-2-0-tariff-tracker">Trade Compliance Resource Hub tariff tracker, 3 November 2026</a> (excess-capacity economies, 91 FR 12886); '
    '<a href="https://atblegal.com/blog/international-trade/india-us-trade-deal">ATB Legal, 22 October 2026</a> (framework, 18%, Russian-oil tariff, sanctions law; secondary); '
    '<a href="https://elplaw.in/wp-content/uploads/2026/07/ELP-Trade-Update-USTR-Finalises-Section-301-Forced-Labour-Tariffs.pdf">ELP Trade Update, July 2026</a> (no MFN cap for India; export total; secondary); '
    '<a href="https://www.thehindubusinessline.com/economy/us-mid-term-results-unlikely-to-speed-up-india-trade-deal-as-tariff-uncertainties-persist/article71692377.ece">The Hindu BusinessLine, 12 November 2026</a>; '
    '<a href="https://www.business-standard.com/economy/news/india-us-trade-deal-nearing-finish-line-may-be-sealed-soon-jaishankar-126111400766_1.html">Business Standard (PTI), 14 November 2026</a>; '
    '<a href="https://www.newindianexpress.com/india/2026/Nov/14/us-promises-india-trade-tariff-edge-over-rivals">The New Indian Express, 14 November 2026</a>; '
    '<a href="https://www.rediff.com/business/report/revealed-what-india-us-trade-deal-is-waiting-for/20261114.htm">Rediff, 14 November 2026</a>; '
    '<a href="https://www.cnbc.com/2026/11/12/us-india-trade-tariffs-trump-modi.html">CNBC, 12 November 2026</a>. '
    'Dollar value, share arithmetic and the stacking illustration computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/09/the-50-tariff-and-234-one-untangling.html", "US tariffs on Indian goods: from 50% in August 2025 to 10% since 24 July 2026"),
    (f"{B}/2026/10/new-zealand-opens-every-tariff-line-to.html", "New Zealand's tariffs on India: zero from 20 October 2026, most lines already free"),
    (f"{B}/2026/08/indias-trade-story-has-three-big-wins.html", "India's exports, first half of the fiscal year: goods up 2.4%, services up 6.5%"),
    (f"{B}/2026/08/the-rupee-fell-10-and-exports-grew-09.html", "Rupee and exports in FY2025-26: the rupee fell 10%, merchandise exports grew 0.9%"),
    (f"{B}/2026/07/textile-hsn-deep-dive-apparel-vs-mmf.html", "India's apparel exports by HSN code: cotton lines lead, man-made fibre lines lag"),
]

build("Trade &middot; Tariffs", TITLE,
      "The US charges a 10% Section 301 duty on most Indian goods; the framework&rsquo;s 18% never took effect, no agreement text has been signed, and four decisions remain open before the G20 summit on 14&ndash;15 December.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
