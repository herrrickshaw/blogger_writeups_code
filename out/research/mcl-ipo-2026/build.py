"""Mahanadi Coalfields IPO, November 2026: offer for sale by Coal India, price band, valuation, earnings and output trend.
Build from the repo root:  python3 out/research/mcl-ipo-2026/build.py   (writes out/post-mahanadi-coalfields-ipo-offer-for-sale-valuation-nov-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026, the day the price band was announced."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-mahanadi-coalfields-ipo-offer-for-sale-valuation-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- The offer ----
# Coal India Reg 30 filing, 14 Nov 2026: RHP dated 13 Nov; offer for sale of up to 661,836,300 equity shares (face value Rs 2) by Coal India. FinTech BizNews, 16 Nov 2026: price band Rs 129-136, lot 110 shares,
# 6,618,363,000 shares outstanding before the offer. CNBC TV18, 16 Nov: at Rs 136 the issue is Rs 8,981.12 crore and post-listing market capitalisation Rs 90,009.74 crore.
# Mint, 14 Nov: reservations about 3.31 crore shares for eligible employees and 6.61 crore for Coal India shareholders; net offer about 56.25 crore; QIB up to 50%, NII at least 15%, retail at least 35% of net offer.
OFFER, PRE = 661_836_300, 6_618_363_000
LOW, HIGH, LOT = 129, 136, 110
CR = 1e7
assert OFFER * 10 == PRE
GROSS_HIGH, GROSS_LOW = OFFER * HIGH / CR, OFFER * LOW / CR
assert round(GROSS_HIGH, 2) == 9000.97 and round(GROSS_LOW, 2) == 8537.69
REPORTED_HIGH, MCAP_REPORTED = 8981.12, 90009.74
GAP = GROSS_HIGH - REPORTED_HIGH
assert round(GAP, 2) == 19.85
assert round(PRE * HIGH / CR, 2) == MCAP_REPORTED
PRESS_LOW, PRESS_HIGH = 9500, 10000          # Mint 14 and 15 Nov: "about Rs 9,500 crore to Rs 10,000 crore", before the band was set
assert round(PRESS_LOW - REPORTED_HIGH) == 519
LOT_COST_HIGH, LOT_COST_LOW = LOT * HIGH, LOT * LOW
assert LOT_COST_HIGH == 14960 and LOT_COST_LOW == 14190
assert round(66.18 - 3.31 - 6.61, 2) == 56.26       # Mint says 56.25; the two reservations are rounded to the nearest 0.01 crore

# ---- Financials, Rs crore (DRHP and RHP restated; Mint 14 Nov and CNBC TV18 16 Nov) ----
REV = {"FY24": 31634.35, "FY25": 31353.02, "FY26": 30549.59}
PAT = {"FY24": 11841.37, "FY25": 10823.58, "FY26": 10677.74}              # profit attributable to owners
H1_REV, H1_REV_PRIOR = 16093.04, 14724.54
H1_PAT, H1_PAT_PRIOR = 4878.57, 4572.66
EPS, NAV = 16.13, 32.29                                                   # FY26 basic EPS and net asset value per share at 31 March 2026 (DRHP)
assert round(PAT["FY26"] * CR / PRE, 2) == EPS
PE_HIGH, PE_LOW = HIGH / EPS, LOW / EPS
PB_HIGH, PB_LOW = HIGH / NAV, LOW / NAV
assert round(PE_HIGH, 1) == 8.4 and round(PE_LOW, 1) == 8.0 and round(PB_HIGH, 1) == 4.2 and round(PB_LOW, 1) == 4.0
MARGIN = {k: 100 * PAT[k] / REV[k] for k in REV}
assert [round(MARGIN[k], 1) for k in ("FY24", "FY25", "FY26")] == [37.4, 34.5, 35.0]
assert round(100 * (REV["FY26"] / REV["FY25"] - 1), 1) == -2.6 and round(100 * (PAT["FY26"] / PAT["FY25"] - 1), 1) == -1.3
assert round(100 * (H1_REV / H1_REV_PRIOR - 1), 1) == 9.3 and round(100 * (H1_PAT / H1_PAT_PRIOR - 1), 1) == 6.7
assert round(100 * (PAT["FY26"] / PAT["FY24"] - 1)) == -10

# ---- Output and offtake, million tonnes (DRHP table) ----
PROD = {"FY24": 206.10, "FY25": 225.17, "FY26": 218.31}
OFFTAKE = {"FY24": 199.02, "FY25": 210.45, "FY26": 211.35}
Q1_PROD, Q1_PROD_PRIOR, Q1_OFF, Q1_OFF_PRIOR = 42.53, 51.58, 54.97, 51.98
assert round(100 * (Q1_PROD / Q1_PROD_PRIOR - 1), 1) == -17.5
assert round(100 * (PROD["FY26"] / PROD["FY25"] - 1), 1) == -3.0
assert round(100 * Q1_OFF / Q1_PROD) == 129 and round(100 * OFFTAKE["FY26"] / PROD["FY26"], 1) == 96.8
RESERVES = 9840.31
assert round(RESERVES / PROD["FY26"]) == 45
CIL_OUTPUT = PROD["FY26"] / 0.284
assert round(100 * PROD["FY26"] / (CIL_OUTPUT / 0.74)) == 21     # 28.4% of Coal India, Coal India about 74% of India: consistent with 21% of domestic output (CNBC TV18)

TITLE = "Mahanadi Coalfields IPO: Rs 8,981 crore offer, all proceeds to Coal India"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("Rs 8,981 crore", f" is the offer at the top of the Rs 129 to Rs 136 band, 10% of Mahanadi Coalfields sold by Coal India; the company receives nothing, and the issue opens 19 November."),
    (f"{PE_HIGH:.1f} times", f" FY26 earnings and {PB_HIGH:.1f} times book value is the price at Rs 136, a market value of Rs 90,009.74 crore on 6,618,363,000 shares."),
    ("Rs 10,678 crore", f" was FY26 profit, {abs(100 * (PAT['FY26'] / PAT['FY24'] - 1)):.0f}% below FY24, on output of 218.31 million tonnes, 3.0% below FY25; the first half of FY27 shows profit up 6.7%."),
])

s1 = insight(
    "At Rs 136 the offer is Rs 8,981 crore, below the Rs 9,500 crore reported earlier",
    bars("The offer is Rs 8,981 crore at the top of the band; earlier reports said Rs 9,500 crore",
         [("Press estimate before the band, low", PRESS_LOW), ("Press estimate before the band, high", PRESS_HIGH),
          ("Gross at Rs 136, computed", round(GROSS_HIGH, 2)), ("Reported at Rs 136", REPORTED_HIGH), ("Gross at Rs 129, computed", round(GROSS_LOW, 2))],
         accent="Reported at Rs 136", unit="₹ crore",
         sub="Offer for sale of 661,836,300 shares by Coal India; none of the money reaches Mahanadi Coalfields.",
         source="Mint, 14 and 15 November 2026; CNBC TV18, 16 November 2026; FinTech BizNews, 16 November 2026; shares from Coal India's filing of 14 November.")
    + numbers(["Item", "Value", "Source"],
              [["Shares offered by Coal India", "661,836,300 (10% of 6,618,363,000)", "Coal India filing, 14 November; FinTech BizNews"],
               ["Price band; lot", "Rs 129 to Rs 136; 110 shares (Rs 14,190 to Rs 14,960 a lot)", "FinTech BizNews, 16 November"],
               ["Gross offer at the band", f"Rs {GROSS_LOW:,.2f} crore at Rs 129; Rs {GROSS_HIGH:,.2f} crore at Rs 136", "Computed here"],
               ["Reported offer at Rs 136", f"Rs 8,981.12 crore, Rs {GAP:.2f} crore below the gross figure; not explained in the sources", "CNBC TV18, 16 November"],
               ["Reserved", "about 3.31 crore shares for employees; 6.61 crore for Coal India shareholders; net offer 56.25 crore", "Mint, 14 November"],
               ["Net offer split", "qualified buyers up to 50%; non-institutional at least 15%; retail at least 35%", "FinTech BizNews, 16 November"],
               ["Dates", "anchors 18 November; open 19 to 23 November; allotment 25 November; listing 27 November (tentative)", "Mint, 14 November"]]),
    f"Because the whole issue is a sale by Coal India, the Rs 8,981.12 crore goes to the parent and not to a company that has identified 12 first-mile connectivity facilities to build by FY30, and the reported size is Rs {GAP:.2f} crore below the share count times the top price, a gap the sources do not explain.",
    "Coal India should state in the offer summary what it will do with the proceeds of the sale, and the exchanges should show the gross and net issue sizes at both ends of the band.",
    "offer")

s2 = insight(
    "At Rs 136 the issue is 8.4 times FY26 earnings and 4.2 times book value",
    bars("At Rs 136 the price is 8.4 times FY26 earnings per share and 4.2 times book value",
         [("Price to earnings, Rs 129", round(PE_LOW, 2)), ("Price to earnings, Rs 136", round(PE_HIGH, 2)),
          ("Price to book, Rs 129", round(PB_LOW, 2)), ("Price to book, Rs 136", round(PB_HIGH, 2))],
         accent="Price to earnings, Rs 136", unit="x",
         fmt=lambda v: f"{v:.1f} times",
         sub="Price divided by FY26 basic earnings per share of Rs 16.13, and by net asset value of Rs 32.29 a share at 31 March 2026.",
         source="Offer document (DRHP) restated financials, 1 September 2026; price band from FinTech BizNews, 16 November 2026; ratios computed here.")
    + numbers(["Item", "Value", "Source"],
              [["Market value at Rs 136", "Rs 90,009.74 crore on 6,618,363,000 shares", "CNBC TV18, 16 November; checked here"],
               ["Pre-band press range", "Rs 83,000 to 90,000 crore (up to $10 billion)", "Mint, 14 November"],
               ["FY26 basic earnings per share", "Rs 16.13 (FY25 Rs 16.35; FY24 Rs 17.89)", "DRHP"],
               ["Net asset value per share, 31 March 2026", "Rs 32.29 (31 March 2025 Rs 27.72; 31 March 2024 Rs 24.36)", "DRHP"],
               ["Grey-market premium", "Rs 12.50 on 14 November and Rs 7.75 on 15 November, before the band was set; unofficial", "Mint, 14 and 15 November"],
               ["Comparison with listed peers", "not computed: the sources read give no multiples for Coal India, BCCL or CMPDI", "&ndash;"]]),
    "The multiples rest on the single year FY26, a year in which profit fell and output fell, so a valuation on a different year, or against Coal India and the two subsidiaries already listed, would give another ratio that this piece cannot supply.",
    "Anyone comparing the issue with Coal India, Bharat Coking Coal and CMPDI should put all four on the same year&rsquo;s earnings and book value, since the sources here supply only Mahanadi&rsquo;s.",
    "valuation")

s3 = insight(
    "Profit fell from Rs 11,841 crore in FY24 to Rs 10,678 crore in FY26",
    bars("Profit fell 10% in two years to Rs 10,678 crore; the first half of FY27 rose 6.7%",
         [("FY24", PAT["FY24"]), ("FY25", PAT["FY25"]), ("FY26", PAT["FY26"])],
         accent="FY26", unit="₹ crore",
         sub="Profit attributable to owners of the company, Rs crore, restated; the FY26 margin on revenue is 35.0%, against 37.4% in FY24.",
         source="Mint, 14 November 2026 and CNBC TV18, 16 November 2026, from the offer documents (DRHP and RHP).")
    + numbers(["Measure", "FY24", "FY25", "FY26"],
              [["Revenue from operations, Rs crore", "31,634.35", "31,353.02", "30,549.59"],
               ["Profit attributable to owners, Rs crore", "11,841.37", "10,823.58", "10,677.74"],
               ["Profit as % of revenue", f"{MARGIN['FY24']:.1f}", f"{MARGIN['FY25']:.1f}", f"{MARGIN['FY26']:.1f}"],
               ["Six months to 30 September, Rs crore", "&ndash;", "revenue 14,724.54; profit 4,572.66 (2025)", "revenue 16,093.04; profit 4,878.57 (2026): +9.3% and +6.7%"],
               ["Capex, Rs crore", "3,839.80", "2,907.52", "2,929.61"]]),
    "Revenue fell 2.6% and profit 1.3% in FY26, the second yearly decline, while the first half of FY27 reversed it with revenue up 9.3% and profit up 6.7%, so the earnings used for the multiple sit at a low point in the series shown.",
    "Investors should weigh the FY26 earnings against the first-half FY27 trend, and read the offer document&rsquo;s note on what drove each half before taking either as the base.",
    "profit")

s4 = insight(
    "Output peaked at 225.17 million tonnes in FY25; Q1 FY27 was 17.5% lower",
    bars("Output was 225.17 million tonnes in FY25 and 218.31 in FY26; Q1 FY27 was 17.5% lower",
         [("FY24", PROD["FY24"]), ("FY25", PROD["FY25"]), ("FY26", PROD["FY26"])],
         accent="FY26", unit=" million t",
         sub="Coal production in million tonnes, almost all from opencast mines. The June 2026 quarter (Q1 FY27) was 42.53 against 51.58 a year earlier.",
         source="Offer document (DRHP) key performance indicators; Mint, 14 November 2026.")
    + numbers(["Measure", "FY24", "FY25", "FY26", "Q1 FY27 (Q1 FY26)"],
              [["Production, million tonnes", "206.10", "225.17", "218.31", "42.53 (51.58)"],
               ["Offtake, million tonnes", "199.02", "210.45", "211.35", "54.97 (51.98)"],
               ["Offtake as % of production", "96.6", "93.5", "96.8", "129 (101)"],
               ["Reserves, JORC, 1 April 2026", "&ndash;", "&ndash;", "9,840.31 million tonnes, about 45 years at FY26 output", "&ndash;"],
               ["Share of domestic output, FY26", "&ndash;", "&ndash;", "21% (CRISIL); 28.4% of Coal India", "&ndash;"]]),
    "In the June 2026 quarter offtake of 54.97 million tonnes ran at 129% of production, which implies that stock was drawn down, so output and dispatch moved apart in that quarter.",
    "Readers should check the offer document for the cause of the June 2026 output fall and for stock held at the pit head, since the sources here give the numbers but not the reason.",
    "output")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Coal India:</b> state in the offer summary how the proceeds of the sale will be used, since the company being listed receives none of them.</li>
<li><b>Stock exchanges and the SEBI offer-document summary:</b> show gross and net issue size at both ends of the band, with any employee or shareholder discount.</li>
<li><b>Coal India and the Ministry of Coal:</b> publish one table of the listed subsidiaries (BCCL, CMPDI, Mahanadi, SECL) with price-to-earnings and price-to-book at the offer and at today&rsquo;s price.</li>
<li><b>Mahanadi Coalfields:</b> publish monthly production, offtake and pit-head stock after listing in one standard table.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>An offer for sale is a sale of existing shares by a shareholder; here Coal India sells 10% of a wholly owned subsidiary, so Mahanadi Coalfields issues no shares and receives no money.</li>
<li>Gross offer size is shares offered multiplied by the price; the reported figure is as given by CNBC TV18 on 16 November and is compared, not substituted.</li>
<li>Price to earnings divides the price by FY26 basic earnings per share (Rs 16.13) and price to book divides it by net asset value per share at 31 March 2026 (Rs 32.29); both are from the offer document.</li>
<li>Profit is the figure attributable to owners of the company, in Rs crore; production and offtake are in million tonnes from the offer document&rsquo;s key performance indicators.</li>
<li>The grey-market premium is an unofficial figure and is not used in any calculation.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The reason the reported offer (Rs 8,981.12 crore) is Rs 19.85 crore below the share count times Rs 136: the gap is consistent with a discount on the employee reservation of about 3.31 crore shares, but the discount is not in the sources read.</li>
<li>Any comparison with Coal India, Bharat Coking Coal or CMPDI: the sources give no multiples for them, and their post-listing price performance was not read.</li>
<li>The cause of the lower June 2026 quarter output, and a conflict on FY26 dispatches: the offer document table shows offtake of 211.35 million tonnes while a Mint report gives 210.74.</li>
<li>Coal India&rsquo;s share of national output: CNBC TV18 gives about 74% in FY26 and a Mint report says more than 80%; the 74% fits MCL&rsquo;s 21% and 28.4% shares and is used.</li>
<li>The date of SEBI&rsquo;s observations on the draft offer document; the draft was filed on 1 September and the final document on 13 November.</li>
<li>What happens after 23 November: subscription, the allotment price and listing day are not covered. SECL&rsquo;s draft filing of 1 November (up to 668,056,100 shares) is noted but not analysed.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.sebi.gov.in/sebi_data/attachdocs/sep-2026/1788761365481.pdf">Mahanadi Coalfields draft red herring prospectus, SEBI, September 2026</a> (restated financials, EPS, net asset value, production and offtake); '
    '<a href="https://www.bseindia.com/xml-data/corpfiling/AttachLive/35b32c1e-b430-4b98-9236-9b0a240fe081.pdf">Coal India filing under Regulation 30, 14 November 2026</a> (offer for sale of 661,836,300 shares); '
    '<a href="https://www.cnbctv18.com/market/mahanadi-coalfields-ipo-price-band-fixed-subscription-issue-to-open-on-november-19-20034562.htm">CNBC TV18, 16 November 2026</a> (issue size and market value at Rs 136); '
    '<a href="https://www.fintechbiznews.com/exchanges-ipos-nfos/mahanadi-coalfields-ipo-opens-on-19nov">FinTech BizNews, 16 November 2026</a> (price band, lot, shares outstanding, reservation split); '
    '<a href="https://www.livemint.com/market/ipo/mahanadi-coalfields-ipo-coal-india-subsidiary-files-rhp-latest-gmp-at-rs-12-5-check-key-dates-size-valuation-more-11794640652111.html">Mint, 14 November 2026</a> and '
    '<a href="https://www.livemint.com/market/ipo/coal-indias-mahanadi-coalfields-ipo-stage-set-for-launch-price-band-tomorrow-gmp-allotment-listing-other-details-11794731994241.html">Mint, 15 November 2026</a> (financials, dates, reservations, grey-market premium); '
    '<a href="https://www.oquilia.com/news/mahanadi-coalfields-files-rhp-coal-india-offer-for-sale">Oquilia, 15 November 2026</a> (secondary: mines and reserves); '
    '<a href="https://nsearchives.nseindia.com/corporate/COALINDIA_02112026120108_SECL.pdf">Coal India filing, 2 November 2026</a> (SECL draft offer document). '
    'Gross sizes, ratios, margins and changes computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/10/india-has-auctioned-141-commercial-coal.html", "Commercial coal mines in India: 141 auctioned since 2020, 15 producing"),
    (f"{B}/2026/10/india-ordered-112-captive-coal-plants.html", "Captive coal plants: 112 ordered to full output as exchange prices rose 50%"),
    (f"{B}/2026/09/indias-live-ipo-queue-has-232-companies.html", "India's 232-company IPO queue: power and renewables lead oil and gas nearly 5 to 1"),
    (f"{B}/2026/09/a-2223-crore-coal-freight-railway-line.html", "₹2,223 crore coal-freight railway: land acquired one survey number at a time"),
]

build("Markets &middot; IPO", TITLE,
      "Coal India is selling 10% of Mahanadi Coalfields for about Rs 8,981 crore at the top of a Rs 129 to Rs 136 band, valuing it at 8.4 times FY26 earnings, with no money reaching the company.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
