"""ONGC, Oil India, relinquished blocks, Green Credit afforestation rules and OTBL bioremediation.
Build from the repo root:  python3 out/research/oil-land-green-credit-2026/build.py   (writes out/post-ongc-oil-india-relinquished-blocks-green-credit-land.html)
Arithmetic is in calc.py beside this file and asserted there; this file re-asserts what it prints. Researched 27 to 28 November 2026.
Opened and read: PPAC Ready Reckoner FY2025-26 (DGH tables 2.7A and 2.7B), Oil India integrated annual report 2025-26 and BRSR 2024-25, MoPNG block-award page and annual report 2024-25,
Lok Sabha answers 138 (29 Jan 2026), 700 (4 Dec 2025) and 4563 (19 Mar 2026), Rajya Sabha answer 151 (21 Jul 2025), CAG Reports 42 of 2015 and 10 of 2020, the Green Credit Rules 2023 and S.O. 592(E) (29 Aug 2025),
the Green Credit Programme FAQ, PIB (16 Mar 2026), Mongabay India (2024, 2025), the otbl.co.in home and Oilzapper pages, ONGC's environment pages, the TERI project page.
Not opened: otbl.co.in MEOR and wax-prevention pages (bot challenge); the ONGC annual report 2025-26 acreage pages."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402
import calc as c  # noqa: E402  (importing runs the asserts)

OUT = ROOT / "out/post-ongc-oil-india-relinquished-blocks-green-credit-land.html"
B = "https://blog.vertistratsolution.com"
TITLE = "ONGC, Oil India and Green Credits: blocks given back, 431 ha planted, 44 ha restored"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert (c.NELP_REL, c.NELP_AW, c.OALP_REL, c.OALP_AW, c.GCP_PLANTED_HA, c.SITES_HA) == (222, 254, 43, 172, 431, 44.0)

top = top_line([
    (f"{c.NELP_REL} of {c.NELP_AW}", f" NELP blocks are relinquished or in that process (DGH, 1 April 2026), against {c.OALP_REL} of {c.OALP_AW} OALP blocks ({c.OALP_PCT:.0f}%). The published tables count blocks, not area, and no total of the area ONGC or Oil India has handed back was found."),
    (f"{c.GCP_PLANTED_HA} ha vs {c.SITES_HA:.0f} ha", f" is Oil India&rsquo;s planting under the Green Credit Programme against the area of its own drilling and operating sites restored in 2025-26 ({c.SITES_N} sites, {c.SITES_SQM:,} sq m). The planting is on State forest land, not on the company&rsquo;s own sites."),
    ("5 years, 40%", " is what the August 2025 methodology requires before any green credit is issued: five years of restoration and a canopy density of 40%. The credits cannot be traded except between a holding company and its subsidiaries."),
])

# ---------------------------------------------------------------- s1: relinquishment
order = ["OALP-I", "OALP-II", "OALP-III", "OALP-IV", "OALP-V", "OALP-VI", "OALP-VII", "OALP-VIII", "OALP-IX"]
rows1 = [("NELP, all nine rounds (254 blocks)", c.NELP_PCT), ("DSF, all rounds (86 contract areas)", c.DSF_PCT), ("OALP, all nine rounds (172 blocks)", c.OALP_PCT)] + \
        [(f"OALP round {r.split('-')[1]}", c.OALP_ROUND[r]) for r in order]
chart1 = bars(f"{c.NELP_PCT:.0f}% of NELP blocks and {c.OALP_PCT:.0f}% of OALP blocks are relinquished or proposed for it", rows1,
              accent=["NELP, all nine rounds (254 blocks)", "OALP, all nine rounds (172 blocks)"], unit="%", vmax=100, from_zero=True,
              sub="Share of blocks awarded that DGH lists as relinquished or proposed for relinquishment, as on 1 April 2026. The NELP column also includes termination notices, operational issues and licences awaited, so it runs wider than relinquishment.",
              source="PPAC India&rsquo;s Oil &amp; Gas Ready Reckoner FY2025-26 (version 1), tables 2.7(A) and 2.7(B), source DGH. Shares by this blog; the table counts blocks and gives no area.")
tbl1 = numbers(["Count of NELP blocks", "Relinquished or equivalent", "Operational", "Source"],
               [["31 March 2018", "188", "66", "MoPNG block-award page"],
                ["30 September 2019", f"{c.CAG_2019_REL} (54 with unfinished minimum work, 139 completed)", str(c.CAG_2019_OP), "CAG Report 10 of 2020, table 5.1"],
                ["1 April 2026", f"{c.NELP_REL} (relinquished, proposed, notice sent, operational issues or licence awaited)", str(c.NELP_OP), "PPAC from DGH, table 2.7(A)"]],
               "Show how the NELP count moved") + numbers(
    ["Round", "Awarded", "Relinquished or proposed", "Operational", "Licence awaited"],
    [[r["round"], r["awarded"], r["relinquished_or_proposed"], r["operational"], r["pel_pml_awaited"] or "0"] for r in c.rows if r["regime"] == "OALP"],
    "Show the OALP rounds")
means1 = f"Relinquishment is the normal fate of an exploration block, with {c.NELP_PCT:.0f}% of NELP blocks and 40% to 45% of OALP rounds I, II and V relinquished or proposed for it, while rounds VIII and IX show none yet."
todo1 = "DGH should publish area relinquished, by operator and year, beside the block counts, because a count cannot say how much licence area has returned to the State."
s1 = insight(f"Blocks given back: {c.NELP_REL} of {c.NELP_AW} NELP blocks and {c.OALP_REL} of {c.OALP_AW} OALP blocks", chart1 + tbl1, means1, todo1, "relinquished")

# ---------------------------------------------------------------- s2: acreage measures
rows2 = [("Public-sector PEL acreage, nomination regime (31 Mar 2025)", c.PEL_NOMINATION_PSU),
         ("PEL acreage held by public, private and joint-venture entities (31 Mar 2025)", c.PEL_ALL_OTHER),
         ("Oil India, total operating acreage (56 blocks, 31 Mar 2025)", c.OIL_OPERATING),
         ("ONGC, nomination PELs and mining leases (9 PEL, 334 PML)", c.ONGC_NOM),
         ("ONGC and Oil India nomination PELs and mining leases together", c.NOM_BOTH),
         ("All OALP blocks awarded, rounds I to IX (172 blocks)", c.OALP_AWARDED_AREA)]
chart2 = bars(f"&lsquo;Land allotted for exploration&rsquo; runs from {c.PEL_NOMINATION_PSU:,} to {c.OALP_AWARDED_AREA:,} sq km, by definition", rows2,
              accent="All OALP blocks awarded, rounds I to IX (172 blocks)", unit=" sq km", vmax=400000, from_zero=True,
              sub="Six published measures of area, each with a different definition. They are not additive. India&rsquo;s sedimentary basins cover 3.36 million sq km, and the OALP awards equal 11.3% of that if no block had been given back.",
              source="Lok Sabha answers of 4 December 2025 (no. 700) and 19 March 2026 (no. 4563); MoPNG block-award page and annual report 2024-25; Oil India annual report 2024-25. Sums and shares by this blog.")
tbl2 = numbers(["Block or licence", "Area (sq km)", "What happened", "Source"],
               [["Kangra-Mandi PEL (ONGC, nomination)", "3,800", "Awarded 10 November 1997; expired 28 November 2021; no discovery; ₹582 crore spent to 2021-22", "Lok Sabha answer 138, 29 January 2026"],
                ["West Bengal OALP blocks BP-ONHP-2019/1 and 2019/2 (listed under ONGC&rsquo;s holdings)", f"{c.WB_A:,} and {c.WB_B:,} ({c.WB_SURRENDERED:,} together)", "&lsquo;Operator has surrendered the block&rsquo; for both", "Rajya Sabha answer 151, 21 July 2025"],
                ["Oil India OALP blocks", "not given", "4 relinquished: 2 in Rajasthan, 1 in Assam, 1 in Odisha", "Oil India annual report 2024-25"],
                ["Oil India NELP-VI block KG-ONN-2004/1", "not given", "Three gas discoveries judged uneconomic; relinquishment sought; validity ended 16 March 2023", "Oil India annual report 2023-24"],
                ["Oil India nomination PEL blocks, to 2013-14", "not given", "9 of 16 relinquished after 15 to 26 years without discovery; ₹219.11 crore spent", "CAG Report 42 of 2015"],
                ["ONGC total exploratory acreage, 31 March 2023", "162,701", "As quoted in this blog&rsquo;s earlier article on ONGC&rsquo;s leases; not rechecked here", "ONGC FY23 disclosure, via earlier article"]],
               "Show relinquishment examples and the 2023 figure")
means2 = f"No single figure answers how much land has been allotted for exploration, because licences held by ONGC and Oil India range from {c.PEL_NOMINATION_PSU:,} sq km of exploration licences in the nomination regime to {c.OALP_AWARDED_AREA:,} sq km of cumulative OALP awards, and a sum of the area they have given back could not be built from the published examples."
todo2 = "DGH and the ministry should state one reconciled acreage table each year, with licence area held, area relinquished and area under mining lease, so that the answers to this question stop depending on the definition."
s2 = insight("Acreage: six official figures for exploration and licence area differ by a factor of 240", chart2 + tbl2, means2, todo2, "acreage")

# ---------------------------------------------------------------- s3: licence area versus land on the ground
rows3 = [("Oil India sites restored, 2025-26 (32 sites)", c.SITES_HA), ("Oil India Green Credit planting, registered and planted (Assam, Odisha)", float(c.GCP_PLANTED_HA)),
         ("Oil India Green Credit parcels reserved in 2024-25 (20 parcels)", float(c.GCP_RESERVED_FY25_HA))]
chart3 = bars(f"Oil India planted {c.GCP_PLANTED_HA} ha under Green Credits and restored {c.SITES_HA:.0f} ha of its own sites", rows3,
              accent="Oil India sites restored, 2025-26 (32 sites)", unit=" ha", vmax=650, from_zero=True,
              sub="Hectares as the company reports them. The sites figure is for 2025-26; the planting figures are cumulative to the year named. They measure different things and are shown together only to compare scale.",
              source="Oil India Integrated Annual Report 2025-26 (440,291 sq m of sites; 431 ha registered and planted) and BRSR 2024-25 (601 ha reserved, 419 ha planted by March 2025). Conversion by this blog.")
tbl3 = numbers(["Item", "Figure", "Source"],
               [["Trees planted, 2025-26", f"{c.TREES:,}", "Oil India annual report 2025-26"],
                ["Legacy waste biomined and bioremediated at Duliajan", "1.3 lakh tonnes", "Oil India annual report 2025-26"],
                ["Oily sludge processed for oil recovery and bioremediation, 2024-25", f"{c.OIL_FY25_T:,} tonnes; 2,435 kl of crude recovered from 3,165 kl of sludge", "Oil India BRSR 2024-25"],
                ["Green credits expected", "2029 (annual report 2025-26); within two years of planting (BRSR 2024-25)", "Oil India reports; the two statements differ"],
                ["Parcels: reserved vs registered", "601 ha (20 parcels) in 2024-25 against 431 ha registered in 2025-26; the difference is not explained", "Oil India BRSR and annual report"],
                ["Net-zero and forest targets", "Scope 1 and 2 net zero by 2040; no net deforestation by 2027", "Oil India annual report 2025-26"],
                ["ONGC", "Scope 1 and 2 net zero by 2038; bioremediation of 93,151 tonnes of oily sludge and oil-contaminated soil in FY23; land reclamation, re-vegetation and compensatory afforestation with State forest departments are described without area figures", "ONGC annual reports 2022-23 and 2026"]],
               "Show the reported figures")
means3 = f"A licence area is not land the company occupies, and what Oil India restores on its own sites ({c.SITES_HA:.0f} ha) is about a tenth of the {c.GCP_PLANTED_HA} ha it has planted under the Green Credit Programme on State forest land elsewhere."
todo3 = "Operators should report the surface land they hold and release at well sites and pipelines each year, so that relinquished licence area can be read against land actually restored."
s3 = insight("On the ground: 44 ha of Oil India sites restored, 431 ha planted elsewhere", chart3 + tbl3, means3, todo3, "ground")

# ---------------------------------------------------------------- s4: Green Credit guidelines
chart4 = flow([
    ("The rules", "The Green Credit Rules 2023 (12 October 2023) allow eight activities: tree plantation, water management, sustainable agriculture, waste management, air pollution reduction, mangrove restoration, Ecomark labels and sustainable buildings. A methodology must be notified for each. Only tree plantation and eco-restoration of degraded forest land is operational. ICFRE is the administrator."),
    ("1. Land", "Degraded forest land under a State Forest Department, uploaded to the portal by the Divisional Nodal Officer. A compact parcel of at least 5 ha, free of encumbrances. Wildlife sanctuaries, national parks and tiger reserves are excluded. The applicant gets no right, title or lease over the land."),
    ("2. Plan and cost", "A detailed project report, approved by the State Nodal Officer. Planting uses a mixture of indigenous species suited to the site. Restoration can include soil and moisture conservation, fencing, assisted natural regeneration, invasive-species removal and fire prevention. The applicant bears every cost, including administration, verification and maintenance."),
    ("3. Reporting", "Annual progress and expenditure reports by 30 April each year on the portal, with photographs, drone video and tree survival. Third-party verification and audits as the Administrator specifies."),
    ("4. The claim", "After at least five years of restoration and a canopy density of at least 40% (a moderately dense forest), the applicant files a claim and pays a verification fee. One green credit is awarded for each new tree older than five years, counted on survival and canopy change. The 2024 methodology&rsquo;s minimum of 1,100 trees per hectare does not appear in the 2025 paragraphs read.", True),
    ("5. Use", "Credits from tree plantation are non-tradable and non-transferable, except between a holding company and its subsidiaries. They can be exchanged once for compensatory afforestation, CSR or other plantation obligations. For compensatory afforestation the user agency must have restored at least 25 ha, in parcels of 5 ha or more. A green credit is a separate instrument from a carbon credit."),
])
tbl4 = numbers(["Item", "Figure", "Source"],
               [["Land selected for restoration", f"{c.GCP_SELECTED_HA:,} ha in {c.GCP_STATES} States", "PIB, 16 March 2026; ICFRE workshop report, October 2026"],
                ["Restoration started", f"{c.GCP_TAKEN_HA:,} ha, with {c.GCP_ENTITIES} entities", "Lok Sabha answer, early 2026"],
                ["Earlier selection figure", "22,656 ha selected, per the programme website as reported in September 2025", "Mongabay India, 4 September 2025"],
                ["Largest early commitment by an oil company", "Indian Oil, 11,890 ha", "Mongabay India, December 2024"],
                ["Methodology history", "S.O. 884(E), 22 February 2024, replaced by S.O. 592(E), 29 August 2025", "Gazette of India"]],
               "Show the land bank and history")
means4 = "The programme gives credit for restoring degraded forest land that belongs to a State Forest Department, after five years and 40% canopy, so land an oil company relinquishes or reclaims at its own sites does not earn a credit under the current methodology."
todo4 = "Oil companies should say in their reports which plantation counts toward Green Credits and which is site restoration, because the two sit under different rules and different land."
s4 = insight("Green Credit guidelines: forest-department land, five years, 40% canopy, no trading", chart4 + tbl4, means4, todo4, "guidelines")

# ---------------------------------------------------------------- s5: OTBL
rows5 = [("OTBL: oily soil and sludge bioremediated, as claimed on its website (cumulative)", float(c.OTBL_CLAIM_T)),
         ("Oil India: legacy waste at Duliajan, biomining and bioremediation (2025-26)", float(c.OIL_LEGACY_T)),
         ("ONGC: oily sludge and contaminated soil bioremediated (FY23)", float(c.ONGC_FY23_T)),
         ("Oil India: oily sludge processed (2024-25)", float(c.OIL_FY25_T))]
chart5 = bars("OTBL claims 1.5 million tonnes of oily soil treated; its pages make no carbon claim", rows5,
              accent=rows5[0][0], unit=" tonnes", vmax=1_700_000, from_zero=True,
              sub="Tonnes, as each source states them. They cover different years and scopes, and only the first is OTBL&rsquo;s own claim, which carries no date. Oil India&rsquo;s figures are not stated to be OTBL work.",
              source="otbl.co.in (home and Oilzapper pages); ONGC annual report 2022-23; Oil India BRSR 2024-25 and annual report 2025-26.")
tbl5 = numbers(["Job", "Tool", "What the sources say", "Gap"],
               [["Clean oil-contaminated soil and sludge", "Oilzapper, a bacterial consortium from OTBL (ONGC TERI Biotech Limited)", "A tonne of sludge degraded in 3 to 4 months at 10^10 CFU per kg; ONGC requires treated soil below 0.5% total petroleum hydrocarbon (5,000 ppm); a TERI project cleared 42,653 cubic metres for Oil India between October 2021 and January 2025", "Results are from OTBL and TERI; no independent audit was found"],
                ["Reclaim a site so plants return", "Bioremediation, then re-vegetation", "At Baghjan, greenery and indigenous vegetation returned after the second treatment and pulse crops were grown; ONGC studies reported natural vegetation after treatment", "No hectares re-vegetated or survival figures found"],
                ["Remove carbon dioxide by natural methods", "Afforestation under Green Credits; mangroves and shoreline work near ONGC coastal sites", "Government says the programme aims to increase green cover and carbon sequestration; credits count trees and canopy, not tonnes of carbon dioxide", "No tonnes sequestered published for any oil-company parcel"],
                ["Conserve soil and moisture", "Part of the restoration plan on Green Credit land", "Soil and moisture conservation is listed among the activities in the plan", "No soil measurement reported; the sustainable-agriculture credit is not yet operational"],
                ["Cut emissions at source", "Flaring, methane, energy and renewables", "ONGC targets net zero for Scope 1 and 2 by 2038, Oil India by 2040", "Separate from land; offsets are not the first measure"]],
               "Show which tool does which job")
means5 = "OTBL&rsquo;s pages describe removing hydrocarbons from soil and sludge so that land can be reused, and they make no claim about carbon absorption, afforestation or soil carbon, so the carbon and soil-conservation work has to come from restoration and operations."
todo5 = "ONGC and Oil India should publish, for each reclaimed site, the hectares returned, the hydrocarbon level before and after, the vegetation established and its survival after five years."
s5 = insight("OTBL: its pages cover cleaning oily soil and sludge, with no carbon or afforestation claim", chart5 + tbl5, means5, todo5, "otbl")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>DGH and the Ministry of Petroleum and Natural Gas:</b> publish licence area held, area relinquished and area under mining lease by operator each year, with one definition of &lsquo;acreage&rsquo; stated.</li>
<li><b>ONGC and Oil India:</b> report surface land held, released and restored in hectares, and say separately which plantation is under the Green Credit Programme.</li>
<li><b>MoEFCC and ICFRE:</b> publish a methodology for reclaimed industrial land if it is to earn credits, with a tonnes-of-carbon figure and a soil measure, and a way to count land the company itself restores.</li>
<li><b>OTBL, ONGC and TERI:</b> publish independently verified before-and-after hydrocarbon levels and hectares re-vegetated for the sites they clean.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Block counts and the relinquished shares come from the PPAC Ready Reckoner tables of 1 April 2026, which cite DGH. The NELP column is headed &lsquo;relinquished / proposed for relinquishment / termination notice sent / operational issues / PEL awaited&rsquo;, so it is broader than relinquishment. The OALP and DSF columns are headed &lsquo;relinquished / proposed for relinquishment&rsquo;. The table is saved with this piece.</li>
<li>The acreage measures are quoted as the sources state them. Exploration licences (PEL) and mining leases (PML) are different instruments. Cumulative awards include blocks later relinquished. None of the six figures is a sum of the others.</li>
<li>A hectare is 10,000 sq m, so Oil India&rsquo;s 440,291 sq m of restored sites is 44.0 ha. The comparison with the planting under the Green Credit Programme is of scale only: different years, different land, different purposes.</li>
<li>Green Credit rules are read from the Green Credit Rules 2023, the August 2025 methodology (S.O. 592(E)), the programme FAQ and PIB and Lok Sabha statements. The compensatory-afforestation conditions are from the Ministry&rsquo;s guidelines of August 2025.</li>
<li>OTBL statements are from its own website (home and Oilzapper pages). The figures in the chart have different bases and are not summed.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The total area ONGC or Oil India has relinquished. DGH and PPAC tables count blocks; the area appears only for individual cases found in Parliament answers and annual reports.</li>
<li>How the 1,583 sq km (public-sector exploration licences, nomination regime) and 12,539 sq km (all other holders) in the Lok Sabha answer of December 2025 square with the 94,358 sq km on the ministry&rsquo;s block-award page and with ONGC&rsquo;s own 162,701 sq km for 2023. They use different definitions, and no reconciliation was found.</li>
<li>Surface land. How many hectares ONGC or Oil India actually hold under leases, rights of user and well pads, and how much has been released, was not found in any source read.</li>
<li>Whether ONGC takes part in the Green Credit Programme and on how many hectares. Oil India&rsquo;s figures are in its reports; for ONGC none was found. Indian Oil&rsquo;s 11,890 ha is a commitment reported in 2024.</li>
<li>Why Oil India reports 601 ha reserved in 2024-25 and 431 ha registered in 2025-26, and whether its two statements on when credits arrive (within two years of planting; in 2029) are both current.</li>
<li>Any tonnes of carbon dioxide sequestered or any soil-carbon measurement for Green Credit parcels. The methodology counts trees and canopy.</li>
<li>OTBL&rsquo;s microbial enhanced oil recovery and wax-prevention pages, which returned a bot challenge and were not read; the &lsquo;1.5 million tons&rsquo; on its site has no date, and no audit of it was found.</li>
<li>The ONGC Annual Report 2025-26 acreage pages were not opened. Section figures for ONGC come from the 2022-23 and 2026 reports as described in search excerpts and from the ministry.</li>
<li>Which land Oil India&rsquo;s Green Credit parcels sit on: the reports name Assam and Odisha only, and the statement that they are State forest land is inferred from the programme&rsquo;s rules.</li>
<li>Which of the Oil India or ONGC treatment figures were carried out by OTBL; only the TERI project for Oil India is stated to be TERI work.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + s5 + fixes + method + gaps

SOURCES = (
    'Acreage and blocks (opened): <a href="https://ppac.gov.in/download.php?file=rep_studies%2F1778072414_IndiasOilGasRR_FY2025-26.pdf">PPAC India&rsquo;s Oil &amp; Gas Ready Reckoner FY2025-26</a> (tables 2.7A, 2.7B; source DGH); '
    '<a href="https://mopng.gov.in/en/exp-and-prod/block-award">MoPNG block-award page</a>; <a href="https://www.mopng.gov.in/files/TableManagements/annual_report24_25.pdf">MoPNG annual report 2024-25</a>; '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/186/AU700_yBA3b9.pdf?source=pqals">Lok Sabha answer 700, 4 December 2025</a>; <a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU4563_PQuxZl.pdf?source=pqals">answer 4563, 19 March 2026</a>; '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU138_2194qa.pdf?source=pqals">answer 138, 29 January 2026</a>; <a href="https://sansad.in/getFile/annex/268/AU151_ugFxrM.pdf?source=pqars">Rajya Sabha answer 151, 21 July 2025</a>; '
    '<a href="https://cag.gov.in/uploads/download_audit_report/2020/09%20Chapter%205-of-10-2020-05f809740b07c69.37519230.pdf">CAG Report 10 of 2020</a>; <a href="https://cag.gov.in/webroot/uploads/download_audit_report/2015/Union_Commercial_Performace_Hydrocarbon_Exploration_42_2015_chap_6.pdf">CAG Report 42 of 2015, chapter 6</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Company reports: <a href="https://www.oil-india.com/files/financial_results_documents/IntegratedAnnualReport2025-26.pdf">Oil India Integrated Annual Report 2025-26</a>; <a href="https://www.oil-india.com/files/investor_services_documents/BRSR-2024-25.pdf">Oil India BRSR 2024-25</a>; '
    '<a href="https://www.oil-india.com/files/financial_results_documents/AnnualReport202324.pdf">Oil India annual report 2023-24</a>; <a href="https://www.oil-india.com/files/financial_results_documents/OIL_India_Annual_Report_2024_25.pdf">2024-25</a>; '
    '<a href="https://ongcindia.com/web/eng/sustainability/environment/environment-management">ONGC environmental management</a>; <a href="https://ongcindia.com/documents/1746026/2665522/AnnualReport2026.pdf">ONGC Annual Report 2026</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Green Credit Programme: <a href="https://egazette.gov.in/WriteReadData/2025/265796.pdf">S.O. 592(E), 29 August 2025</a>; <a href="http://dste.py.gov.in/ppcc/pdf/Notification/Green%20Credit%20Rules%202023.pdf">Green Credit Rules 2023</a>; '
    '<a href="https://www.moefcc-gcp.in/faq">programme FAQ</a>; <a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2240640">PIB, 16 March 2026</a>; <a href="https://forestsclearance.nic.in/writereaddata/public_display/schemes/142674276%24xyz.pdf">Ministry guidelines on compensatory afforestation, August 2025</a>; '
    '<a href="https://india.mongabay.com/2025/09/green-credit-rules-tweaked-to-favour-canopy-cover-remove-trade-provision">Mongabay India, 4 September 2025</a> and <a href="https://india.mongabay.com/2024/12/green-credit-programme-rolls-out-with-little-clarity-on-exchange-value">December 2024</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">OTBL and bioremediation: <a href="https://www.otbl.co.in/">otbl.co.in</a> and <a href="https://www.otbl.co.in/Oilzapper.php">Oilzapper page</a>; <a href="https://www.teriin.org/project/bioremediation-services-assam-and-arunachal-pradesh">TERI, bioremediation services in Assam and Arunachal Pradesh</a>. '
    'Researched 27 and 28 November 2026. Shares, conversions and comparisons are this blog&rsquo;s work.')

RELATED = [
    (f"{B}/2026/09/dgh-has-awarded-172-oalp-blocks-and-436_0369361351.html", "India's oil and gas exploration blocks: 172 awarded, 1 has reached production"),
    (f"{B}/2026/09/india-let-oil-companies-put-solar-on.html", "ONGC solar on oil leases: under 1 MW built a year after the law, 4 GW bought"),
    (f"{B}/2026/08/where-indias-captured-carbon-would.html", "Carbon storage in India: 2 named pilot wells, basins mapped without identified wells"),
    (f"{B}/2026/08/the-green-shift-what-indias-oil.html", "Oil ministry's Green Shift report: scope 1+2 emissions at about 4% of global CO₂"),
    (f"{B}/2026/08/indias-oil-fields-are-running-down-3696.html", "India's crude oil output: 36.96 to 28.70 MMT in the decade to 2024-25"),
    (f"{B}/2026/11/environmental-clearance-in-india_01652956239.html", "Environmental clearance in India: central or state, NABET's role and a 105-day clock"),
]

build("Energy &middot; Environment", TITLE,
      "How much exploration acreage ONGC and Oil India hold and give back, what the Green Credit afforestation rules require, and what OTBL's bioremediation does for land reclamation, carbon and soil.",
      body, SOURCES, RELATED, str(OUT))
assert "masaladeutsch" not in OUT.read_text().lower()
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
