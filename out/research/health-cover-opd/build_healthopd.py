import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-health-cover-opd.html'

# ---------------------------------------------------------------- data
# National Health Accounts 2022-23 (released May 2026), as reported
THE_LCR = 8.81            # total health expenditure, Rs lakh crore
CHE_LCR = 7.66814         # current health expenditure, Rs lakh crore
GHE_CR = 385332           # government health expenditure, Rs crore
GHE_PC = 2786             # per-capita government health expenditure, Rs
OOPE_THE = 43.4           # % of THE, 2022-23
OOPE_CHE = 49.9           # % of CHE, 2022-23
OOPE_SERIES = [("2013-14", 64.2), ("2014-15", 62.6), ("2021-22", 39.4), ("2022-23", 43.4)]
GHE_GDP_OLD, GHE_GDP_NEW = 1.43, 1.48
PHARM_CHE = 21.19          # pharmacies as % of CHE
OOPE_LCR = OOPE_THE / 100 * THE_LCR
OOPE_LCR_CHK = OOPE_CHE / 100 * CHE_LCR
assert abs(OOPE_LCR - OOPE_LCR_CHK) < 0.05
POP_CR = GHE_CR * 1e7 / GHE_PC / 1e7          # population implied by NHA per-capita figure, crore
OOPE_PC = OOPE_LCR * 1e12 / (POP_CR * 1e7)
PHARM_LCR = PHARM_CHE / 100 * CHE_LCR

# Committee (Rajya Sabha Standing Committee on Health, report 176, 7 Aug 2026), as summarised by PRS
UNPROTECTED = 30           # % of population without structured financial protection
PVT_OPD_X = 5              # private outpatient cost vs public
OPD_SHARE = 70             # % of health spending on outpatient care, per the committee as cited in Parliament
TARGET_GDP = 2.5

# NSS 80th round (Jan-Dec 2025)
NSS_HOSP_MEAN, NSS_HOSP_MEDIAN = 34064, 11285
NSS_GOV_INS_RURAL, NSS_GOV_INS_URBAN = 45.5, 31.8

# PM-JAY
CARDS_CR = 48.51           # Ayushman cards issued, Sep 2026
ADM_CR = 13.25             # hospital admissions since 2018
ADM_LCR = 2.03             # value, Rs lakh crore
YEARS = 8                  # Sep 2018 to Sep 2026
ELIG_CR = 55               # eligible people in the central scheme (12 crore families), as reported
CENTRE_2627 = 9500         # Centre's PM-JAY allocation 2026-27, Rs crore
AVG_CLAIM = ADM_LCR * 1e12 / (ADM_CR * 1e7)
CLAIMS_PER_YR_CR = ADM_LCR * 1e5 / YEARS

# Illustrative cost of outpatient cover for PM-JAY's eligible population (2022-23 prices)
OPD_PC = OOPE_PC * OPD_SHARE / 100
SCEN = [("Low: poorer half spends half the national average", 0.5), ("High: spends the national average", 1.0)]
OPD_COST = [(n, f, OPD_PC * f * ELIG_CR * 1e7 / 1e7) for n, f in SCEN]   # Rs crore
GDP_LCR = GHE_CR / 1e5 / (GHE_GDP_NEW / 100)
GAP_CR = (TARGET_GDP - GHE_GDP_NEW) / 100 * GDP_LCR * 1e5
LOW_CR, HIGH_CR = OPD_COST[0][2], OPD_COST[1][2]


def chart_cost():
    rows = [("PM-JAY: Centre&rsquo;s budget, 2026-27", CENTRE_2627, "#868e96"),
            ("PM-JAY: hospital claims a year, average since 2018", CLAIMS_PER_YR_CR, "#868e96"),
            ("Outpatient cover, low estimate", LOW_CR, "#1c5d99"),
            ("Outpatient cover, high estimate", HIGH_CR, "#1c5d99"),
            ("Extra public spending to reach 2.5% of GDP", GAP_CR, "#a5402c")]
    W, L, top, bh, gap, lab = 400, 10, 28, 18, 9, 0
    H = top + len(rows) * (bh + gap + 13) + 30
    sc = (W - L - 80) / GAP_CR
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Rs crore a year: PM-JAY central budget {CENTRE_2627:,.0f}; average hospital claims {CLAIMS_PER_YR_CR:,.0f}; outpatient cover {LOW_CR:,.0f} to {HIGH_CR:,.0f}; extra spending to reach 2.5% of GDP {GAP_CR:,.0f}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Rs thousand crore a year</text>']
    y = top
    for n, v, col in rows:
        s.append(f'<text x="{L}" y="{y + 9}" font-size="10" fill="#212529">{n}</text>')
        y += 13
        s.append(f'<rect x="{L}" y="{y}" width="{max(v * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + max(v * sc, 2) + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v / 1000:,.1f}</text>')
        y += bh + gap
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Outpatient cover and the 2.5% gap in 2022-23 prices; PM-JAY figures in current</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">rupees. Illustrative; assumptions in the text. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_reco():
    return table(["The committee recommends", "Where things stand"], [
        ("Extend PM-JAY to outpatient consultations, diagnostics and medicines", "PM-JAY pays for hospital admissions only; a government reply to Parliament states that outpatient services are not covered"),
        ("Raise family cover to Rs 10 lakh a year", f"Rs 5 lakh per family a year; the average admission paid since 2018 is about Rs {round(AVG_CLAIM, -2):,.0f}"),
        ("Jan Aushadhi generic-medicine kendras in district hospitals and community health centres", "The committee wants them inside these hospitals; this blog&rsquo;s Jan Aushadhi piece covers what the kendras sell"),
        ("A binding standard for private hospital rates", "The committee asks for one; outside insurance packages, private hospitals set their own rates"),
        (f"Government health spending on a time-bound path to {TARGET_GDP}% of GDP, then 5%", f"{GHE_GDP_NEW}% of GDP in 2022-23 on the new GDP series ({GHE_GDP_OLD}% on the old)"),
    ])


def t_oope():
    rows = [(y, f"{v:.1f}%") for y, v in OOPE_SERIES]
    return table(["Year", "Out-of-pocket spending, % of total health expenditure"], rows)


def t_scen():
    rows = []
    for n, f, c in OPD_COST:
        rows.append((n, f"Rs {OPD_PC * f:,.0f}", f"{ELIG_CR} crore", f"Rs {c / 1e5:.2f} lakh crore", f"{c / CLAIMS_PER_YR_CR:.1f}&times;"))
    return table(["Scenario", "Outpatient spending per person a year", "People covered", "Cost a year", "vs PM-JAY&rsquo;s yearly hospital claims"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{OOPE_THE}%</b><span>of India&rsquo;s health spending was paid out of pocket in 2022-23, up from {OOPE_SERIES[2][1]}% a year earlier</span></div>
<div class="gb-stat"><b>~{OPD_SHARE}%</b><span>of health spending goes on outpatient care, which PM-JAY does not cover, per the Parliamentary committee</span></div>
<div class="gb-stat"><b>~Rs {round(AVG_CLAIM, -2):,.0f}</b><span>average PM-JAY admission paid since 2018, against Rs {NSS_HOSP_MEAN:,} average out-of-pocket per hospital stay in 2025</span></div>
<div class="gb-stat"><b>Rs {LOW_CR / 1e5:.1f}&ndash;{HIGH_CR / 1e5:.1f} lakh cr</b><span>a year: this blog&rsquo;s rough cost of outpatient cover for PM-JAY&rsquo;s 55 crore eligible people</span></div>
</div>'''

body = f"""
{stats}

<p>On 7 August the Rajya Sabha&rsquo;s Standing Committee on Health presented a report on how affordable healthcare is in India. Its central finding is that about {UNPROTECTED}% of people have no structured financial protection against health costs, and its central proposal is to extend Ayushman Bharat PM-JAY, which pays for hospital admissions, to doctor visits, tests and medicines. It also wants family cover raised from Rs 5 lakh to Rs 10 lakh a year and government health spending put on a time-bound path to {TARGET_GDP}% of GDP.</p>
<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/indias-two-tracks-of-health-cover-and.html">piece on India&rsquo;s two tracks of health cover</a> looked at how PM-JAY and private insurance have grown. This piece looks at the gap the committee is pointing to: where out-of-pocket money actually goes, why most of it falls outside PM-JAY, and roughly what covering outpatient care would cost.</p>

<h2 class="gb-h2">What the committee found and asked for</h2>
{t_reco()}
<p>The {UNPROTECTED}% figure echoes NITI Aayog&rsquo;s 2021 estimate that at least 30% of the population, about 40 crore people, were a &ldquo;missing middle&rdquo; with no health insurance: mostly self-employed and informal workers too well-off for PM-JAY and outside employer schemes. Since then PM-JAY has been extended to everyone over 70 and to some groups of workers, so the share may now be lower; the committee did not publish a new estimate. The committee also found that outpatient care in private facilities costs about {PVT_OPD_X} times as much as in public ones.</p>

<h2 class="gb-h2">Out-of-pocket spending stopped falling</h2>
{t_oope()}
<p>India&rsquo;s National Health Accounts for 2022-23, released in May 2026, put total health spending at Rs {THE_LCR} lakh crore. Households paid {OOPE_THE}% of it directly, about Rs {OOPE_LCR:.2f} lakh crore, or about Rs {OOPE_PC:,.0f} for every person in the country. That share had fallen steadily for a decade, but rose in 2022-23 from {OOPE_SERIES[2][1]}% as government spending fell after the pandemic years. Government health spending was {GHE_GDP_NEW}% of GDP on the new GDP series.</p>
<p>Pharmacies alone took {PHARM_CHE}% of current health spending, about Rs {PHARM_LCR:.2f} lakh crore, nearly all of it paid by households. The NSS survey of 2025 shows the same pattern from the household side: government insurance now covers {NSS_GOV_INS_RURAL}% of rural and {NSS_GOV_INS_URBAN}% of urban people, but the average out-of-pocket cost of a hospital stay was Rs {NSS_HOSP_MEAN:,} (median Rs {NSS_HOSP_MEDIAN:,}), and a NITI Aayog-commissioned study found that 65% of PM-JAY beneficiaries still paid something themselves, mainly for medicines, tests and transport.</p>

<h2 class="gb-h2">Why PM-JAY misses most of it</h2>
<p>PM-JAY has issued {CARDS_CR} crore Ayushman cards and paid for about {ADM_CR} crore hospital admissions worth Rs {ADM_LCR} lakh crore since 2018, or about Rs {round(AVG_CLAIM, -2):,.0f} an admission and about Rs {CLAIMS_PER_YR_CR / 1000:,.1f} thousand crore a year. But hospital stays are rare and doctor visits frequent. The committee puts the outpatient share of health spending at nearly {OPD_SHARE}%, and an NIPFP analysis of the 2014 NSS survey found that households spent more than twice as much on outpatient care as on hospital care over a year, because they need it far more often. A scheme that pays only for admissions cannot reach most of what households pay.</p>

<h2 class="gb-h2">What outpatient cover might cost</h2>
{t_scen()}
<p>This is a rough, illustrative calculation, not a costing. It takes out-of-pocket spending per person from the 2022-23 health accounts (Rs {OOPE_PC:,.0f}), assumes {OPD_SHARE}% of it is outpatient care (about Rs {OPD_PC:,.0f} a person), and applies it to PM-JAY&rsquo;s roughly {ELIG_CR} crore eligible people. Because poorer households spend less, the low case assumes they spend half the national average. The answer is Rs {LOW_CR / 1e5:.1f}&ndash;{HIGH_CR / 1e5:.1f} lakh crore a year in 2022-23 prices, {LOW_CR / CLAIMS_PER_YR_CR:.1f} to {HIGH_CR / CLAIMS_PER_YR_CR:.1f} times what PM-JAY pays for hospital care in an average year, and many times the Centre&rsquo;s Rs {CENTRE_2627:,} crore PM-JAY budget for 2026-27.</p>
{chart_cost()}
<p>Set against the committee&rsquo;s other target, though, it is affordable. Raising government health spending from {GHE_GDP_NEW}% to {TARGET_GDP}% of GDP would have meant about Rs {GAP_CR / 1e5:.2f} lakh crore more a year at 2022-23 GDP, so outpatient cover for PM-JAY&rsquo;s eligible population would take {LOW_CR / GAP_CR * 100:.0f}&ndash;{HIGH_CR / GAP_CR * 100:.0f}% of that increase. How it is delivered matters as much as the money. Outpatient claims are small and numerous, so paying for them through insurance claims can cost a lot to administer; providing free medicines and tests at public facilities such as Ayushman Arogya Mandirs reaches the same spending without a claim for each visit. The question of what drugs cost at the pharmacy counter, the subject of a separate committee report on drug pricing, bears on both routes.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The National Health Authority should publish an annual split of out-of-pocket spending by beneficiaries and non-beneficiaries of PM-JAY, by outpatient care, medicines, tests and hospital stays, so the scheme&rsquo;s effect on what families pay is measured rather than assumed.</li>
<li>Before any outpatient extension, the Centre should pilot two models in comparable districts, insurance reimbursement and free medicines and diagnostics at public facilities, and publish the cost per person and the change in out-of-pocket spending for each.</li>
<li>The National Health Accounts should be published within two years of the year they cover, not three, and should report outpatient and inpatient spending separately.</li>
<li>NITI Aayog should update its 2021 &ldquo;missing middle&rdquo; estimate now that PM-JAY covers everyone over 70, so the size of the uncovered group is known.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The committee report, the National Health Accounts and the NSS report could not be opened directly; figures come from the PRS summary, news reports and summaries of those documents. The {OPD_SHARE}% outpatient share is the committee&rsquo;s figure as cited in a parliamentary question; the health accounts&rsquo; own outpatient and inpatient split was not found. PM-JAY&rsquo;s eligible population is reported as about 55 crore for the central scheme and 60 crore or more with state extensions; this piece uses 55 crore. The outpatient cost is in 2022-23 prices, ignores any rise in use once care is free, and assumes the poorer half spends between half and all of the national average per person. The average PM-JAY admission and the yearly average are this blog&rsquo;s division of cumulative figures over eight years.</p>
"""

sources = ("Committee: Rajya Sabha Department-related Parliamentary Standing Committee on Health and Family Welfare, Report 176, &ldquo;Affordability and Accessibility of Healthcare in India&rdquo; (7 August 2026), via the PRS report summary and Monthly Policy Review (August 2026); outpatient share as cited in a Lok Sabha question; PM-JAY&rsquo;s exclusion of outpatient services per an earlier government reply in Parliament. "
           "National Health Accounts 2022-23 (Ministry of Health, May 2026) via The Hindu, Daily Excelsior, Dataful, ThePrint and Medical Dialogues; 2013-14 to 2021-22 shares via PIB (October 2024) and IANS. "
           "NSS 80th round, Household Social Consumption: Health (January&ndash;December 2025), via ORF, AIR News and summaries. NIPFP report to WHO on NSS 2014 (outpatient vs inpatient spending). NITI Aayog, &ldquo;Health Insurance for India&rsquo;s Missing Middle&rdquo; (October 2021). "
           "PM-JAY cards, admissions and value (September 2026) via Open Magazine and Shankar IAS; eligible population via the Society of Actuaries (July 2026); Union Budget 2026-27 allocation via PIB and JSA; NITI Aayog-commissioned study on beneficiaries&rsquo; out-of-pocket costs as reported. "
           "Per-person spending, averages and the outpatient-cover scenarios are this blog&rsquo;s arithmetic (builder in the repository at out/research/health-cover-opd/). Nothing here is medical or financial advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-two-tracks-of-health-cover-and.html", "India&rsquo;s Two Tracks of Health Cover, and Where They Actually Meet"),
    ("https://masaladeutsch.blogspot.com/2026/09/jan-aushadhi-sells-2439-products-heres.html", "Jan Aushadhi Sells 2,439 Products. Here&rsquo;s What We Actually Know About Where Their APIs Come From"),
    ("https://masaladeutsch.blogspot.com/2026/08/abha-what-indias-14-digit-health-id.html", "ABHA: What India&rsquo;s 14-Digit Health ID Actually Does, in the Real Numbers"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-tracks-every-taxpayer-in-minutes.html", "India Tracks Every Taxpayer in Minutes. Its Patients Got a Digital ID in 2021"),
]

build("Healthcare · 28 October 2026",
      "Most of What Indians Pay for Health Is Outpatient Care. Ayushman Bharat Pays Only for Hospital Stays",
      "A Parliamentary committee wants PM-JAY extended to doctor visits, tests and medicines. Out-of-pocket spending rose to 43.4% of health spending in 2022-23, and most of it is outpatient care the scheme does not touch. Covering it for PM-JAY&rsquo;s eligible population would cost a fraction of the committee&rsquo;s own spending target.",
      body, sources, related, OUT)
print("OOPE lcr", round(OOPE_LCR, 3), "pop cr", round(POP_CR, 1), "oope pc", round(OOPE_PC), "opd pc", round(OPD_PC), "avg claim", round(AVG_CLAIM), "claims/yr", round(CLAIMS_PER_YR_CR), "low", round(LOW_CR), "high", round(HIGH_CR), "gdp lcr", round(GDP_LCR, 1), "gap", round(GAP_CR), "pharm", round(PHARM_LCR, 2))
