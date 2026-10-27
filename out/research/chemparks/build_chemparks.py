import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-chemparks.html'

# ---------------------------------------------------------------- BHAVYA Rasayan (Cabinet, 24 Jul 2026)
OUTLAY, INFRA, ADMIN = 3030, 3000, 30
PARKS, CENTRE_PER_PARK, STATE_MIN = 3, 1000, 500
MIN_SQKM, MIN_ACRES = 8, 2000
assert INFRA + ADMIN == OUTLAY and PARKS * CENTRE_PER_PARK == INFRA
CENTRE_PER_ACRE = CENTRE_PER_PARK / MIN_ACRES          # Rs crore an acre, at minimum size
PARK_SQKM = PARKS * MIN_SQKM

# ---------------------------------------------------------------- PCPIR (policy 2007)
PCPIR_TARGET_INV, PCPIR_TARGET_JOBS = 7.63e5, 33.96e5   # Rs crore, persons, four regions
AREA = {"Dahej (Gujarat)": 453, "Visakhapatnam-Kakinada (Andhra Pradesh)": 640, "Paradeep (Odisha)": 284.15}
PCPIR_AREA = sum(AREA.values())
INV_2014, INV_2026 = 140537, 349192                      # Rs crore, three regions (Rajya Sabha, 28 Jul 2026)
UNITS_2026, JOBS_2026 = 2246, 371263
DAHEJ_INV_2014, DAHEJ_INV, DAHEJ_UNITS, DAHEJ_JOBS = 69621, 137163, 2079, 245140
OTHER_INV, OTHER_UNITS, OTHER_JOBS = INV_2026 - DAHEJ_INV, UNITS_2026 - DAHEJ_UNITS, JOBS_2026 - DAHEJ_JOBS
INV_SHARE = INV_2026 / PCPIR_TARGET_INV * 100
JOB_SHARE = JOBS_2026 / PCPIR_TARGET_JOBS * 100
DAHEJ_UNIT_SHARE = DAHEJ_UNITS / UNITS_2026 * 100
PER_UNIT_DAHEJ = DAHEJ_INV / DAHEJ_UNITS
PER_UNIT_OTHER = OTHER_INV / OTHER_UNITS
TN_HA = 22928                                            # Cuddalore-Nagapattinam, delineated 2017

# ---------------------------------------------------------------- earlier parks schemes
BDP_OUTLAY, BDP_RELEASED = 3000, 180                     # bulk drug parks, released to Dec 2025
BDP_SHARE = BDP_RELEASED / BDP_OUTLAY * 100
HP_USED = 116                                            # Himachal park, central grant used to 30 Jun 2026

# ---------------------------------------------------------------- trade, US$ bn
CHEM_IMP, CHEM_EXP = 27.913, 28.673                      # Organic & inorganic chemicals, FY2025-26 (commerce quick estimates)
PLAS_IMP = 22.756                                        # Artificial resins & plastic materials imports, FY2025-26
PLAS_EXP = 12.5                                          # All plastics exports incl. products, FY2024-25 (Plexconcil)
CH = [("Ch. 29 Organic chemicals", 25.41), ("Ch. 39 Plastics and articles", 22.23),
      ("Ch. 28 Inorganic chemicals", 14.18), ("Ch. 38 Misc. chemical products", 8.86)]
TOP = [("LDPE and LLDPE", 1861), ("Terephthalic acid (TPA)", 1469), ("Polypropylene", 1372), ("HDPE", 939),
       ("para-Xylene", 721), ("Ethylene glycol", 650), ("Acetic acid", 490)]
TOP_SUM = sum(v for _, v in TOP)


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_trade():
    W, L, top, bh, gap, lab = 400, 10, 44, 16, 4, 128
    rows = [("Organic and inorganic chemicals", CHEM_IMP, CHEM_EXP, "FY26"),
            ("Plastics", PLAS_IMP, PLAS_EXP, "imports FY26, exports FY25")]
    H = top + len(rows) * (2 * bh + gap + 22) + 30
    sc = (W - L - lab - 50) / 30
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Chemicals trade is roughly balanced: imports {CHEM_IMP:.1f} and exports {CHEM_EXP:.1f} billion dollars. Plastics are not: raw-material imports {PLAS_IMP:.1f} against exports of {PLAS_EXP:.1f} billion dollars.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">India&rsquo;s trade in chemicals and plastics, US$ billion</text>',
         f'<rect x="{L}" y="22" width="9" height="9" fill="#a5402c"/><text x="{L + 13}" y="30" font-size="9.5" fill="#212529">Imports</text>',
         f'<rect x="{L + 70}" y="22" width="9" height="9" fill="#1c5d99"/><text x="{L + 83}" y="30" font-size="9.5" fill="#212529">Exports</text>']
    y = top
    for n, imp, exp, note in rows:
        s.append(f'<text x="{L}" y="{y + 10}" font-size="10.5" font-weight="700" fill="#212529">{n}</text>')
        y += 14
        for v, col, lbl in ((imp, "#a5402c", "imports"), (exp, "#1c5d99", "exports")):
            s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9.5" fill="#212529" text-anchor="end">{lbl}</text>')
            s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
            s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{v:.1f}</text>')
            y += bh + gap
        y += 8
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Chemicals and plastic imports: commerce ministry quick estimates, FY2025-26.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Plastics exports (incl. finished products): Plexconcil, FY2024-25.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_pcpir():
    W, L, top, bh, gap, lab = 400, 10, 30, 18, 8, 150
    rows = [("Investment, Rs lakh crore", DAHEJ_INV / 1e5, OTHER_INV / 1e5, "{:.2f}"),
            ("Units, hundreds", DAHEJ_UNITS / 100, OTHER_UNITS / 100, "{:.1f}"),
            ("Jobs, lakh", DAHEJ_JOBS / 1e5, OTHER_JOBS / 1e5, "{:.2f}")]
    H = top + len(rows) * (2 * bh + gap + 18) + 22
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Dahej holds {DAHEJ_UNITS:,} of the {UNITS_2026:,} units in India&rsquo;s three PCPIRs; Visakhapatnam-Kakinada and Paradeep together hold {OTHER_UNITS}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">PCPIRs in July 2026: Dahej against the other two regions</text>',
         f'<rect x="{L}" y="18" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="26" font-size="9.5" fill="#212529">Dahej</text>',
         f'<rect x="{L + 60}" y="18" width="9" height="9" fill="#868e96"/><text x="{L + 73}" y="26" font-size="9.5" fill="#212529">Visakhapatnam-Kakinada + Paradeep</text>']
    y = top + 6
    for n, a, b, fmt in rows:
        mx = max(a, b, 0.01)
        sc = (W - L - lab - 46) / (mx * 1.05)
        s.append(f'<text x="{L}" y="{y + 10}" font-size="10.5" font-weight="700" fill="#212529">{n}</text>')
        y += 14
        for v, col in ((a, "#1c5d99"), (b, "#868e96")):
            s.append(f'<rect x="{L + 4}" y="{y}" width="{max(v * sc, 1.5):.1f}" height="{bh}" fill="{col}"/>')
            s.append(f'<text x="{L + 4 + max(v * sc, 1.5) + 4:.1f}" y="{y + 13}" font-size="9.5" fill="#212529">{fmt.format(v)}</text>')
            y += bh + 2
        y += gap
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Rajya Sabha reply, 28 Jul 2026, as reported; other-region values are this blog&rsquo;s subtraction.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_scheme():
    return table(["Feature", "BHAVYA Rasayan"], [
        ("Approved", "Union Cabinet, 24 July 2026; announced in the Union Budget 2026-27"),
        ("Outlay and period", f"Rs {OUTLAY:,} crore (Rs {INFRA:,} crore for common infrastructure, Rs {ADMIN} crore administration), 2026-27 to 2030-31"),
        ("Parks", f"{PARKS}, developed by states chosen through a challenge route"),
        ("Central grant", f"Up to Rs {CENTRE_PER_PARK:,} crore a park, if the state puts in at least Rs {STATE_MIN} crore"),
        ("Minimum size", f"{MIN_SQKM} sq km (about {MIN_ACRES:,} acres) of contiguous, encumbrance-free land"),
        ("What the grant pays for", "Common effluent treatment, hazardous-waste treatment, storage and disposal, solvent recovery, steam networks, pipelines, water, logistics and warehousing"),
        ("What it does not set", "No capacity, investment, product or import-substitution target was given in the Cabinet decision"),
    ])


def t_pcpir():
    return table(["Region", "Notified area, sq km", "Investment, Rs crore", "Units", "Jobs"], [
        ("Dahej (Gujarat)", f"{AREA['Dahej (Gujarat)']:,}", f"{DAHEJ_INV:,} (Rs {DAHEJ_INV_2014:,} in March 2014)", f"{DAHEJ_UNITS:,}", f"{DAHEJ_JOBS:,}"),
        ("Visakhapatnam-Kakinada (AP) and Paradeep (Odisha)", f"{AREA['Visakhapatnam-Kakinada (Andhra Pradesh)']:,} and {AREA['Paradeep (Odisha)']:,}", f"{OTHER_INV:,} (derived)", f"{OTHER_UNITS} (derived)", f"{OTHER_JOBS:,} (derived)"),
        ("Cuddalore-Nagapattinam (Tamil Nadu)", f"{TN_HA / 100:,.0f} delineated in 2017", "Not listed in 2026", "&mdash;", "&mdash;"),
        ("<b>Three regions, July 2026</b>", f"<b>{PCPIR_AREA:,.0f}</b>", f"<b>{INV_2026:,}</b> ({INV_SHARE:.0f}% of the Rs 7.63 lakh crore expected for four)", f"<b>{UNITS_2026:,}</b>", f"<b>{JOBS_2026:,}</b> ({JOB_SHARE:.0f}% of 33.96 lakh)"),
    ])


def t_parks():
    return table(["Scheme", "Design", "Where it stood"], [
        ("Bulk drug parks (approved 2020)", f"Rs {BDP_OUTLAY:,} crore, three parks, up to Rs 1,000 crore each, to 2026-27; same common-infrastructure list as BHAVYA Rasayan", f"Rs {BDP_RELEASED} crore released across the three by December 2025 ({BDP_SHARE:.0f}% of the outlay); Himachal Pradesh had used Rs {HP_USED} crore by June 2026; Gujarat and Andhra Pradesh works under way"),
        ("Plastic parks", "Ten approved; grant up to half of project cost, capped at Rs 40 crore a park", "Government aimed to finish infrastructure in nine by end-2025; three or four were partly operating in April 2025, one stayed by the National Green Tribunal"),
        ("PCPIRs (2007)", "No central grant for the regions themselves; the Centre was to fund external links such as roads, rail and ports", f"Rs {INV_2026 / 1e5:.2f} lakh crore committed or invested in three regions after 19 years; no digital monitoring dashboard, the government told Parliament"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {OUTLAY:,} cr</b><span>for three chemical parks by 2030-31, up to Rs {CENTRE_PER_PARK:,} crore each from the Centre</span></div>
<div class="gb-stat"><b>{BDP_SHARE:.0f}%</b><span>of the identically designed bulk-drug parks scheme&rsquo;s Rs 3,000 crore had been released after nearly six years</span></div>
<div class="gb-stat"><b>{DAHEJ_UNIT_SHARE:.0f}%</b><span>of units in India&rsquo;s three petrochemical investment regions are in one of them, Dahej</span></div>
<div class="gb-stat"><b>${PLAS_IMP:.1f} bn</b><span>of plastic raw-material imports in 2025-26, the gap that parks of this kind are least able to close</span></div>
</div>'''

body = f"""
{stats}

<p>On 24 July 2026 the Cabinet approved BHAVYA Rasayan, a Rs {OUTLAY:,} crore scheme for three chemical parks by 2030-31. States will compete for them, and each winner gets up to Rs {CENTRE_PER_PARK:,} crore from the Centre to build shared plant that chemical makers otherwise have to build or do without: effluent treatment, hazardous-waste disposal, solvent recovery, steam and pipelines. It is a separate scheme from the Rs 33,660 crore BHAVYA programme for 100 general industrial parks that <a href="https://masaladeutsch.blogspot.com/2026/10/india-will-spend-rs-33660-crore-on.html">this blog covered last week</a>.</p>
<p>India has tried to plan chemical clusters before. This piece sets out what the new scheme pays for, which part of India&rsquo;s chemical import bill it can plausibly reduce, and what happened to the two closest precedents: the 2007 petroleum, chemicals and petrochemicals investment regions (PCPIRs), and the 2020 bulk-drug parks, whose design BHAVYA Rasayan copies almost exactly.</p>

<h2 class="gb-h2">What the scheme pays for</h2>
{t_scheme()}
<p>At the minimum size, the central grant works out to about Rs {CENTRE_PER_ACRE:.1f} crore an acre, half the Rs 1 crore an acre ceiling in the general BHAVYA parks. The three parks together need at least {PARK_SQKM} sq km, under 2% of the {PCPIR_AREA:,.0f} sq km already notified for the three PCPIRs. The money is for shared utilities only; the plants themselves are left to private investors.</p>

<h2 class="gb-h2">Which imports a park can replace</h2>
{chart_trade()}
<p>India does not run a deficit in chemicals as a whole. In 2025-26 it imported US${CHEM_IMP:.1f} billion of organic and inorganic chemicals and exported US${CHEM_EXP:.1f} billion, on the commerce ministry&rsquo;s quick estimates. The deficit is in plastics: US${PLAS_IMP:.1f} billion of resins and plastic materials imported in 2025-26, against all plastics exports, finished products included, of about US${PLAS_EXP:.1f} billion in 2024-25.</p>
{table(["Largest single-line chemical imports, FY2025-26", "US$ million"], [(n, f"{v:,}") for n, v in TOP] + [("<b>Seven lines together</b>", f"<b>{TOP_SUM:,}</b>")])}
<p class="gb-note">From this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/07/top-15-chemicals-for-import.html">corrected top-15 table</a>, built from DGCI&amp;S TradeStat. By HS chapter, the same source puts 2025-26 imports at {"; ".join(f"{n}, US${v:.2f} bn" for n, v in CH)}. The commerce ministry&rsquo;s &ldquo;organic and inorganic chemicals&rdquo; group is narrower than chapters 28 and 29 together, because it counts some of their lines under other headings.</p>
<p>The biggest single gaps are polymers and the petrochemical intermediates behind them: polyethylene, polypropylene, terephthalic acid, para-xylene, ethylene glycol. Those come from crackers and aromatics complexes that cost Rs 75,000 crore to more than Rs 1 lakh crore each and bring their own utilities. A Rs {CENTRE_PER_PARK:,} crore park will not decide whether one gets built. What shared effluent treatment, waste disposal and solvent recovery do make possible is smaller speciality and fine-chemical plants, the kind held back by pollution clearances and the cost of treating their own waste. That is useful, but it is mostly an export and value-added story, not an import-substitution one.</p>
<p class="gb-note">Correction to this blog&rsquo;s earlier tables: the chemical import posts in July attached 150 KTPA of dye and 80 KTPA of pigment capacity to the &ldquo;BHAVYA parks&rdquo;. The Cabinet decision sets no capacity target, and those figures were this blog&rsquo;s assumptions; the corrected top-15 table also shows azo-dye imports of only about US$8&ndash;25 million.</p>

<h2 class="gb-h2">What happened to the PCPIRs</h2>
{chart_pcpir()}
{t_pcpir()}
<p>The 2007 policy expected four regions to draw about Rs 7.63 lakh crore and employ about 33.96 lakh people. Nineteen years later, three regions report Rs {INV_2026 / 1e5:.2f} lakh crore of investment, {INV_SHARE:.0f}% of that expectation, and {JOBS_2026 / 1e5:.2f} lakh jobs, {JOB_SHARE:.0f}%. The investment figure covers sanctioned and committed projects, not only completed ones. Tamil Nadu&rsquo;s Cuddalore-Nagapattinam region, delineated over about {TN_HA / 100:,.0f} sq km in 2017 amid farmer protests and a court challenge, no longer appears in the government&rsquo;s count.</p>
<p>The split is the more telling number. Dahej has {DAHEJ_UNITS:,} of the {UNITS_2026:,} units, about {DAHEJ_UNIT_SHARE:.0f}%, at an average of about Rs {PER_UNIT_DAHEJ:,.0f} crore of investment each. The other two regions together have {OTHER_UNITS} units averaging about Rs {PER_UNIT_OTHER:,.0f} crore, which points to a few very large refinery and anchor projects rather than a cluster. Dahej sits beside Bharuch and Ankleshwar, Gujarat&rsquo;s existing chemical belt; the regions that had to be built from a plan mostly did not fill. Visakhapatnam-Kakinada&rsquo;s anchor cracker was still listed as &ldquo;yet to be finalised&rdquo; in the department&rsquo;s undated status table.</p>

<h2 class="gb-h2">The bulk-drug parks are the closer precedent</h2>
{t_parks()}
<p>BHAVYA Rasayan copies the bulk-drug parks scheme of 2020 almost line for line: three parks, up to Rs 1,000 crore each, state competition, the same list of shared utilities. By December 2025, with the scheme due to end in 2026-27, Rs {BDP_RELEASED} crore of its Rs {BDP_OUTLAY:,} crore had been released. Himachal Pradesh, whose park has the most detailed figures, had used Rs {HP_USED} crore of central money by June 2026 and was asking for more to build a zero-liquid-discharge plant the guidelines do not fund. The new scheme gives itself five years; the precedent suggests site preparation alone can take most of that.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Chemicals and Petrochemicals should publish, for each BHAVYA Rasayan park, a quarterly report of land handed over, utilities commissioned, plots allotted, investment committed and units producing, starting with the challenge-round scores of every state that applied.</li>
<li>The challenge round should give weight to sites inside or next to existing chemical clusters and notified PCPIR land, where Dahej&rsquo;s record shows demand already exists, over greenfield sites.</li>
<li>Release of central money should be tied to anchor tenants signed, not only to construction milestones.</li>
<li>The scheme should name the HS lines it expects the parks to serve, so that their effect on imports and exports can be tracked against DGCI&amp;S data.</li>
<li>The government should report realised, not committed, investment for the PCPIRs, region by region, since it told Parliament there is no monitoring dashboard.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet release, the PCPIR status table and the parliamentary replies could not be opened directly; figures come from their text as indexed by search engines and from news reports (ANI, PTI, DeshGujarat). The split of PCPIR investment, units and jobs between Visakhapatnam-Kakinada and Paradeep was not published; the combined figures are this blog&rsquo;s subtraction of Dahej from the total. The 2007 targets come from later government statements, not the original policy text. The plastics comparison mixes a 2025-26 import figure for raw materials with a 2024-25 export figure that includes finished products, so it shows the size of the gap, not its exact value. The challenge round&rsquo;s deadlines, criteria and applicants had not been published by 27 October 2026.</p>
"""

sources = ("BHAVYA Rasayan: Cabinet decision of 24 July 2026 as reported by ANI (via India&rsquo;s News, India Gazette), Outlook Business, Governance Now, Indian Masterminds, Vision IAS and Onmanorama; minimum area and challenge route per the government text quoted by IMPRI and Manorama Yearbook. "
           "PCPIRs: Rajya Sabha reply of 28 July 2026 (Minister of State Anupriya Patel) as reported by PTI via Deccan Chronicle, Indian Chemical News and Construction World, and DeshGujarat for Dahej; notified areas and 2018 status per the Department of Chemicals and Petrochemicals statement (2018); 2007 targets per FICCI and later government statements; Cuddalore-Nagapattinam delineation and challenge per Plastemart; Visakhapatnam-Kakinada anchor per the department&rsquo;s PCPIR status page and Lok Sabha replies. "
           "Bulk-drug and plastic parks: government replies of December 2025 and 2026 (Lok Sabha, PIB documents), Medical Dialogues and Tribune (2020 approvals); plastic parks per the department&rsquo;s scheme page and PTI via The Week and Business Standard (April 2025). "
           "Trade: commerce ministry quick estimates for 2025-26 (PIB documents, June 2026); Plexconcil for 2024-25 plastics exports (Indian Chemical News); HS-chapter and HS-8 imports from this blog&rsquo;s analysis of DGCI&amp;S TradeStat. "
           "Per-acre, share and per-unit figures are this blog&rsquo;s arithmetic (builder at out/research/chemparks/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/india-will-spend-rs-33660-crore-on.html", "India Will Spend Rs 33,660 Crore on Ready-Made Factory Parks. Its Existing Parks Have 1.25 Lakh Empty Plots"),
    ("https://masaladeutsch.blogspot.com/2026/07/top-15-chemicals-for-import.html", "The Top 15 Import-Substitution Chemicals, Code by Code"),
    ("https://masaladeutsch.blogspot.com/2026/07/indias-petrochemical-import-tree-from.html", "India&rsquo;s Petrochemical Import Tree"),
    ("https://masaladeutsch.blogspot.com/2026/07/chemical-import-substitution-analysis.html", "Chemical Import Substitution Analysis"),
]

build("Chemicals · 27 October 2026",
      "India&rsquo;s Rs 3,030 Crore Chemical Parks Copy the Bulk-Drug Parks. Those Released 6% of Their Money in Six Years",
      "BHAVYA Rasayan will pay for shared effluent, waste and steam plant in three state-run chemical parks. The design is the 2020 bulk-drug parks scheme&rsquo;s, and the plastics and petrochemical imports that make up India&rsquo;s real deficit need crackers, not parks.",
      body, sources, related, OUT)
print("per acre", CENTRE_PER_ACRE, "pcpir area", PCPIR_AREA, "inv share", round(INV_SHARE, 1), "job share", round(JOB_SHARE, 1),
      "other", OTHER_INV, OTHER_UNITS, OTHER_JOBS, "per unit", round(PER_UNIT_DAHEJ), round(PER_UNIT_OTHER), "bdp", BDP_SHARE, "dahej units", round(DAHEJ_UNIT_SHARE, 1))
