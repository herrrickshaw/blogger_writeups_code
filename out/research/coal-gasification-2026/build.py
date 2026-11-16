"""India's coal gasification push, November 2026: the Rs 37,500 crore scheme's application rounds, the Rs 8,500 crore scheme's payouts, capacity against the 100 MT target, and the forex-saving claims.
Build from the repo root:  python3 out/research/coal-gasification-2026/build.py   (writes out/post-india-coal-gasification-incentive-scheme-applications-nov-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-coal-gasification-incentive-scheme-applications-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- The two schemes (Rs crore) ----
# Rajya Sabha USQ 2428 (10 Aug 2026) and Starred Q 165 (3 Aug 2026): Rs 8,500 crore scheme approved 24 Jan 2024; 8 projects; Rs 6,233.06 crore earmarked
#   (Cat I 3 x 1,350; Cat II 569.05 + 414.01 + 1,000; Cat III 2 x 100); Rs 235.52 crore disbursed in FY2026, all to Jindal Steel.
# Cabinet 13 May 2026: Rs 37,500 crore; RFP 7 Jun 2026; per-project cap Rs 5,000 crore, per-entity cap Rs 12,000 crore, 20% of plant and machinery, 4 equal instalments (Ministry slides, 29 May 2026).
# ET 5 Nov 2026: Secretary Vikram Dev Dutt "Rs 46,000 crore in financial incentives across two schemes".
OUTLAY_1, OUTLAY_2, QUOTED = 8500, 37500, 46000
CAT1, CAT2, CAT3 = 3 * 1350, 569.05 + 414.01 + 1000, 2 * 100
EARMARKED, PAID = 6233.06, 235.52
assert OUTLAY_1 + OUTLAY_2 == QUOTED
assert round(CAT1 + CAT2 + CAT3, 2) == EARMARKED and round(CAT2, 2) == 1983.06 and CAT1 == 4050
PAID_SHARE = 100 * PAID / EARMARKED
assert round(PAID_SHARE, 1) == 3.8
assert round(100 * PAID / OUTLAY_1, 1) == 2.8
JSL_SHARE = 100 * PAID / 569.05
assert round(JSL_SHARE) == 41

# ---- Applications under the Rs 37,500 crore scheme ----
# PIB 8 Sep 2026 (Round 1): 7 applications: NTPC 1 (SNG), Adani Enterprises 3 (urea), Gallantt Ispat 1 (DRI and syngas), Shyam Sel & Power 1 (syngas), Talcher Fertilisers 1 (urea).
# Business Standard and The Hindu, 10 Nov 2026 (Round 2): 2 applications, both NTPC (urea; methanol and DME). Round 3 opened 10 Nov, closes 11 Jan 2027.
R1 = {"NTPC": 1, "Adani Enterprises": 3, "Gallantt Ispat": 1, "Shyam Sel & Power": 1, "Talcher Fertilisers": 1}
R2 = {"NTPC": 2}
assert sum(R1.values()) == 7 and len(R1) == 5 and sum(R2.values()) == 2
APPS = sum(R1.values()) + sum(R2.values())
COMPANIES = len(set(R1) | set(R2))
assert APPS == 9 and COMPANIES == 5
EXPECTED_PROJECTS, SCHEME_MTPA = 25, 75
assert round(100 * APPS / EXPECTED_PROJECTS) == 36
AVG_INCENTIVE = OUTLAY_2 / EXPECTED_PROJECTS
assert AVG_INCENTIVE == 1500 and SCHEME_MTPA / EXPECTED_PROJECTS == 3
assert OUTLAY_2 / 5000 == 7.5          # projects the per-project cap would fund if every project took the cap

# ---- Capacity, MTPA ----
# Rajya Sabha USQ 46 (20 Jul 2026): about 22.6 MTPA operational or under implementation = Jindal Steel ~8 (operational) + Talcher Fertilisers ~2.6 (under implementation)
#   + projects under the Rs 8,500 crore scheme ~12 (under implementation); target 100 MT by 2030; new scheme expected to add ~75 MTPA.
# Rajya Sabha USQ 2428 (10 Aug 2026) says "approximately 22.6 MTPA ... approved under the Rs 8,500 crore scheme". Lok Sabha USQ 524 (22 Jul): the 8 projects use ~12 MT a year; Jindal's has reached financial closure
# and is "in the construction stage" (USQ 46 calls it operational).
JSL, TFL, SCHEME1 = 8, 2.6, 12
BUILT = JSL + TFL + SCHEME1
TARGET = 100
assert round(BUILT, 1) == 22.6
assert round(BUILT + SCHEME_MTPA, 1) == 97.6 and round(TARGET - BUILT - SCHEME_MTPA, 1) == 2.4

# ---- Forex-saving claims ----
# Lok Sabha USQ 524 (22 Jul 2026), expected-benefits table: 8 projects approx Rs 16,500 crore a year by FY2030; the 2026 scheme "Rs 1.5 lakh crore annually at maturity"; investment Rs 65,000 crore (8 projects), Rs 2.5-3 lakh crore (2026 scheme).
# ET 5 Nov 2026: Secretary: "saving about Rs one and a half lakh crore potentially of foreign exchange through this import substitution" in "five to seven years".
# PIB 8 Sep 2026: imports of LNG, urea, ammonia and methanol together about Rs 2.77 lakh crore in FY2024-25.
SAVE_8_CR, SAVE_2026_ANNUAL_CR, IMPORTS_CR = 16500, 150000, 277000
LOW_YR, HIGH_YR = SAVE_2026_ANNUAL_CR / 7, SAVE_2026_ANNUAL_CR / 5
assert round(LOW_YR) == 21429 and round(HIGH_YR) == 30000
assert round(100 * SAVE_2026_ANNUAL_CR / IMPORTS_CR) == 54 and round(100 * SAVE_8_CR / IMPORTS_CR) == 6
assert round(HIGH_YR / SAVE_8_CR, 1) == 1.8
assert round(SAVE_8_CR / EARMARKED, 2) == 2.65
assert round(100 * EARMARKED / 65000, 1) == 9.6 and 100 * OUTLAY_2 / 300000 == 12.5 and 100 * OUTLAY_2 / 250000 == 15.0
LAKH = lambda c: c / 1e5

TITLE = "Coal gasification: 9 applications in two rounds for a Rs 37,500 crore scheme"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    (f"{APPS} applications", f" came in under the Rs 37,500 crore scheme, 7 in Round 1 and 2 in Round 2 (both NTPC), from {COMPANIES} companies; the scheme was sized for about {EXPECTED_PROJECTS} projects."),
    ("Rs 235.52 crore", f" of the Rs 8,500 crore approved in 2024 had been paid by August 2026, {PAID_SHARE:.1f}% of the Rs 6,233.06 crore earmarked, all to Jindal Steel."),
    ("Rs 1.5 lakh crore", " is the forex saving the Coal Secretary cited on 5 November over five to seven years; a July Lok Sabha reply gave the same figure as an annual saving at maturity."),
])

s1 = insight(
    "Nine applications came in two rounds, 7 then 2, for a scheme sized for 25 projects",
    bars("Round 1 drew 7 applications and Round 2 drew 2; about 25 projects were expected",
         [("Round 1, closed by 8 September", 7, "5 companies"), ("Round 2, announced 10 November", 2, "NTPC only"),
          ("Total received", APPS), ("Projects the scheme expects", EXPECTED_PROJECTS)],
         accent="Total received", unit=" applications",
         sub="Applications under the Rs 37,500 crore scheme for surface coal and lignite gasification; Round 3 closes on 11 January 2027.",
         source="PIB, 8 September 2026; Business Standard and The Hindu, 10 November 2026; Lok Sabha unstarred question 524, 22 July 2026 (about 25 projects).")
    + numbers(["Round", "Applicant", "Applications", "Product"],
              [["1", "NTPC", "1", "Synthetic natural gas"], ["1", "Adani Enterprises", "3", "Urea"], ["1", "Gallantt Ispat", "1", "Direct reduced iron and syngas"],
               ["1", "Shyam Sel &amp; Power", "1", "Syngas"], ["1", "Talcher Fertilisers", "1", "Urea"], ["2", "NTPC", "2", "Urea; methanol and dimethyl ether"],
               ["3", "Open", "&ndash;", "Closes 11 January 2027"]]),
    f"The ministry called Round 1 an overwhelming response and the trade press called Round 2 thin, but both rounds together are {round(100 * APPS / EXPECTED_PROJECTS)}% of the projects the scheme expects and neither round published the capacity or cost of any application.",
    "The Coal Ministry should publish the capacity, product and project cost of each application received, so the share of the 75 million tonnes a year that applicants cover can be counted.",
    "applications")

s2 = insight(
    "Rs 235.52 crore of the Rs 8,500 crore scheme has been paid; Rs 6,233.06 crore is earmarked",
    bars("Of Rs 8,500 crore approved in 2024, Rs 6,233.06 crore is earmarked, Rs 235.52 crore paid",
         [("Outlay, 2024 scheme", OUTLAY_1), ("Earmarked for 8 projects", EARMARKED), ("Paid, all to Jindal Steel in FY2026", PAID)],
         accent="Paid, all to Jindal Steel in FY2026", unit="₹ crore",
         sub="Financial incentive under the scheme approved on 24 January 2024; the Rs 37,500 crore scheme of May 2026 has no award in the sources read.",
         source="Rajya Sabha starred question 165 (3 August 2026) and unstarred question 2428 (10 August 2026).")
    + numbers(["Category", "Earmarked, Rs crore", "Paid, Rs crore"],
              [["I: 3 government projects (1,350 each)", "4,050", "Nil"], ["II: Jindal Steel 569.05; Greta Energy 414.01; New Era Cleantech 1,000", "1,983.06", "235.52 (Jindal Steel)"],
               ["III: 2 demonstration projects (100 each)", "200", "Nil"], ["Total, 8 projects", "6,233.06", "235.52"],
               ["Projects with financial closure and a first instalment", "1 (Jindal Steel)", "&ndash;"], ["Projects with environmental clearance; ground-breaking", "4; 5", "&ndash;"]]),
    f"The Rs 46,000 crore quoted for both schemes is a ceiling and not spending, since the Rs 8,500 crore scheme has paid {PAID_SHARE:.1f}% of its earmarked amount, with one project through financial closure and Jindal Steel&rsquo;s first instalment equal to {round(JSL_SHARE)}% of its own Rs 569.05 crore.",
    "The Coal Ministry should publish the incentive earmarked, paid and still conditional for each project every quarter, so a reader can tell progress from approvals.",
    "payouts")

s3 = insight(
    "Gasification capacity built or approved is 22.6 million tonnes a year; the target is 100",
    bars("22.6 million tonnes a year is built or approved; the 2026 scheme is expected to add 75",
         [("Target for 2030", TARGET), ("Operational or under implementation, July 2026", BUILT), ("Expected from the 2026 scheme", SCHEME_MTPA),
          ("The two together", BUILT + SCHEME_MTPA)],
         accent="Operational or under implementation, July 2026", unit=" million t a year",
         sub="Coal gasification capacity in million tonnes of coal a year (MTPA). The 22.6 is Jindal Steel 8 + Talcher Fertilisers 2.6 + 12 under the 2024 scheme.",
         source="Rajya Sabha unstarred questions 46 (20 July 2026) and 2428 (10 August 2026); Lok Sabha unstarred question 524 (22 July 2026).")
    + numbers(["Statement", "Source", "Says"],
              [["22.6 MTPA is Jindal ~8 + Talcher ~2.6 + ~12 under the 2024 scheme", "Rajya Sabha question 46, 20 July", "Jindal Steel operational"],
               ["22.6 MTPA approved under the Rs 8,500 crore scheme", "Rajya Sabha question 2428, 10 August", "Jindal Steel is one of the 8 projects"],
               ["8 projects use about 12 million tonnes of coal a year", "Lok Sabha question 524, 22 July", "Jindal Steel at financial closure, in construction"],
               ["Projects with technology partner identified", "Rajya Sabha question 165, 3 August", "4 of 8"]]),
    f"The two schemes add to {BUILT + SCHEME_MTPA:.1f} million tonnes against the 100 target, but only the {BUILT} is approved and the 75 is an expectation for about {EXPECTED_PROJECTS} projects that two rounds have so far met with nine applications.",
    "The Coal Ministry should publish one project-wise register of capacity, status and incentive, so that the Parliament replies that describe the 22.6 million tonnes differently can be reconciled.",
    "capacity")

s4 = insight(
    "Rs 1.5 lakh crore is an annual saving in July and a 5-to-7-year saving in November",
    bars("One Rs 1.5 lakh crore saving is read as yearly and as over 5 to 7 years",
         [("8 approved projects, a year by FY2030", LAKH(SAVE_8_CR)), ("Rs 1.5 lakh crore over 5 to 7 years, read per year", LAKH(HIGH_YR), "from 0.21 to 0.30"),
          ("Rs 1.5 lakh crore a year at maturity (July reading)", LAKH(SAVE_2026_ANNUAL_CR)), ("Imports of LNG, urea, ammonia, methanol, FY2025", LAKH(IMPORTS_CR))],
         accent="Rs 1.5 lakh crore a year at maturity (July reading)", unit="₹ lakh crore", fmt=lambda v: f"₹{v:.3g} lakh crore",
         sub="Claimed foreign-exchange savings against the import bill. The same Rs 1.5 lakh crore is read two ways; the shorter bar divides it over 5 years.",
         source="Lok Sabha unstarred question 524 (22 July 2026); Economic Times, 5 November 2026; PIB, 8 September 2026.")
    + numbers(["Claim", "Value", "Source"],
              [["8 approved projects, a year by FY2030", "Rs 16,500 crore", "Lok Sabha question 524; Rajya Sabha question 2428"],
               ["2026 scheme, a year at maturity", "Rs 1.5 lakh crore", "Lok Sabha question 524"],
               ["Coal Secretary, over 5 to 7 years", "Rs 1.5 lakh crore (read here as Rs 21,429&ndash;30,000 crore a year)", "Economic Times, 5 November"],
               ["Investment: 8 projects; 2026 scheme", "about Rs 65,000 crore; Rs 2.5&ndash;3 lakh crore", "Lok Sabha question 524"],
               ["Incentive as share of investment", "9.6% (2024 scheme, earmarked); 12.5&ndash;15% (2026 scheme, outlay)", "Computed here"],
               ["Annual saving as share of FY2025 imports", "Rs 1.5 lakh crore is 54%; Rs 16,500 crore is 6%", "Computed here; import basket differs from product list"]]),
    "A Rs 1.5 lakh crore saving a year would offset 54% of the FY2025 import bill for LNG, urea, ammonia and methanol, while the same sum over five to seven years is Rs 21,429 to 30,000 crore a year, so the two readings differ by a factor of five to seven and only one can be right.",
    "The Coal Ministry should publish the method behind the saving, with the import price, product volumes and years assumed, so that the annual and the multi-year readings can be tested against each other.",
    "forex")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Coal:</b> publish the capacity, product, cost and state of every application received in each round, with the names of those shortlisted.</li>
<li><b>Ministry of Coal:</b> publish a project-wise register that reconciles the 22.6 million tonnes a year across the Parliament replies, with status and incentive paid.</li>
<li><b>Ministry of Coal and the Department of Economic Affairs:</b> state the method for the forex saving, including whether Rs 1.5 lakh crore is annual or cumulative.</li>
<li><b>Department of Economic Affairs:</b> consider gasification for the infrastructure master list, which the Gasification Technology and Research Council says would ease financing.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Applications are those the Coal Ministry announced for the Rs 37,500 crore scheme: Round 1 on 8 September 2026 and Round 2 on 10 November 2026; this piece counts one application per project, as the ministry lists them.</li>
<li>Incentive figures are rupees crore from Parliament replies; &ldquo;earmarked&rdquo; is the amount set aside for approved projects and &ldquo;paid&rdquo; is the amount disbursed.</li>
<li>MTPA is million tonnes of coal a year. The 22.6 is as stated in the Rajya Sabha reply of 20 July 2026; the 97.6 is this blog&rsquo;s sum of that and the 75 expected from the 2026 scheme.</li>
<li>The annual reading of the Secretary&rsquo;s Rs 1.5 lakh crore divides it by 5 and by 7 years; this is an interpretation of an ambiguous statement and is labelled as such.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The size, product and cost of each application: the ministry lists applicants and products but not capacity or project cost, so the share of the 75 million tonnes a year applied for is unknown.</li>
<li>Whether any project has been selected under the Rs 37,500 crore scheme: none was announced in the sources read.</li>
<li>Which of the two Parliament counts of the 22.6 million tonnes is right, and whether Jindal Steel&rsquo;s plant is operational or under construction; the replies differ.</li>
<li>Whether the Rs 1.5 lakh crore saving is annual or over five to seven years; the Lok Sabha reply and the Secretary&rsquo;s remark read differently, and the method is not published.</li>
<li>The composition of the Rs 2.77 lakh crore import figure: the ministry names LNG, urea, ammonia and methanol, while the 2024 scheme&rsquo;s projects also replace ammonium nitrate, acetic acid and direct reduced iron.</li>
<li>The reasons for the thin Round 2 beyond one industry-body view in Business Standard; lower gas and chemical prices, financing, coal supply and Chinese equipment were cited, none measured.</li>
<li>The state of the Talcher project, covered in a separate post, and any application figure after 10 November.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.coal.gov.in/sites/default/files/2026-11/Pib08sept26.pdf">PIB, 8 September 2026</a> (Round 1 applicants; import basket); '
    '<a href="https://www.business-standard.com/industry/news/coal-gasification-scheme-receives-only-2-applications-in-second-round-126111000846_1.html">Business Standard, 10 November 2026</a> and '
    '<a href="https://www.thehindu.com/business/Industry/ntpc-leads-second-round-of-coal-gasification-bids-with-two-applications/article71686471.ece">The Hindu, 10 November 2026</a> (Round 2; Round 3 deadline; industry views); '
    '<a href="https://m.economictimes.com/industry/indl-goods/svs/metals-mining/coal-gasification-projects-may-save-india-rs-1-5-lakh-crore-in-forex-over-5-7-years-coal-ministry-secretary/articleshow/135565406.cms">Economic Times, 5 November 2026</a> (Secretary&rsquo;s remarks); '
    '<a href="https://sansad.in/getFile/annex/271/AU46_lUEGmj.pdf?source=pqars">Rajya Sabha unstarred question 46, 20 July 2026</a>; '
    '<a href="https://sansad.in/getFile/annex/271/AU2428_4RGCOM.pdf?source=pqars">Rajya Sabha unstarred question 2428, 10 August 2026</a>; '
    '<a href="https://sansad.in/getFile/annex/271/AS165_x0lqMw.pdf?source=pqars">Rajya Sabha starred question 165, 3 August 2026</a>; '
    '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU524_dm5D0S.pdf?source=lsapps">Lok Sabha unstarred question 524, 22 July 2026</a>; '
    '<a href="https://coal.gov.in/sites/default/files/2026-05/29-05-2026a-wn.pdf">Ministry of Coal scheme presentation, 29 May 2026</a> (caps, instalments, eligibility). '
    'Shares, per-year readings and sums computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/09/the-reactor-nobody-names-how-coal.html", "Coal gasification in India: Talcher, the largest project, uses Shell's reactor"),
    (f"{B}/2026/08/indias-coal-to-chemicals-menu-ranked-by.html", "India's coal-to-chemicals options: most do not yet beat the import price"),
    (f"{B}/2026/10/how-to-use-coal-to-urea-design.html", "How to use coal-to-urea-design-opensource: size a coal-to-urea complex"),
    (f"{B}/2026/10/india-has-auctioned-141-commercial-coal.html", "Commercial coal mines in India: 141 auctioned since 2020, 15 producing"),
    (f"{B}/2026/08/indias-coking-coal-import-problem-and.html", "India's coking coal: roughly 90% imported, with biochar at pilot scale at SAIL"),
]

build("Energy &middot; Coal", TITLE,
      "A Rs 37,500 crore gasification incentive drew 7 applications in Round 1 and 2 in Round 2, while the 2024 scheme has paid Rs 235.52 crore and the forex saving is quoted two ways.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
