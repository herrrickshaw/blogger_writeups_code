import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-mining-law.html'

# ---------------------------------------------------------------- data
# PRS state budget analyses 2026-27 (budget estimates, Rs crore)
ODISHA = dict(own_tax=70000, own_nontax=71000, mining=53000, mining_tbl=56000, mining_2425=42067)
CHHATT = dict(own_tax=52000, own_nontax=25000, mining=19000, mining_2425=14609)
JHARK = dict(own_tax=45999, own_nontax=20700, mining=16000, mining_2425=12086, cess=14656,
             mining_2526_be=21900, mining_2526_re=16000)
for d in (ODISHA, CHHATT, JHARK):
    d["own"] = d["own_tax"] + d["own_nontax"]
    d["mining_share"] = d["mining"] / d["own"] * 100
JHARK["cess_share"] = JHARK["cess"] / JHARK["own"] * 100
assert ODISHA["own"] == 141000 and CHHATT["own"] == 77000 and JHARK["own"] == 66699

# Claims at stake (as reported; not audited)
ARREARS_NATIONAL = (150000, 200000)      # Rs crore, estimates of arrears from 1 Apr 2005
ARREARS_ODISHA = 100000                  # "over Rs 1 lakh crore", state Advocate General affidavit as reported
DUES_JHARK = 136000                      # Jharkhand claim incl. land compensation and other dues (broader)
ODISHA_ANNUAL = 12000                    # ORISED Act tax, contingent on validation (BJD / state minister)
KARNATAKA_BILL = 4713                    # Karnataka Mineral Rights and Mineral Bearing Land Tax Bill 2024 estimate
TATA_CONTINGENT = 17347                  # Tata Steel contingent liability disclosed
JH_CESS_RATES = [("Coal", 100), ("Iron ore", 100), ("Bauxite", 70), ("Limestone", 50), ("Manganese ore", 50)]
DEBATE_MIN = 45


def chart_share():
    W, L, top, bh, gap, lab = 400, 10, 44, 20, 14, 92
    rows = [("Odisha", ODISHA["mining_share"], 0), ("Chhattisgarh", CHHATT["mining_share"], 0),
            ("Jharkhand", JHARK["mining_share"], JHARK["cess_share"])]
    H = top + len(rows) * (bh + gap) + 32
    sc = (W - L - lab - 70) / 50
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Mining receipts as a share of own revenue, 2026-27 budgets: Odisha {ODISHA["mining_share"]:.0f}%, Chhattisgarh {CHHATT["mining_share"]:.0f}%, Jharkhand {JHARK["mining_share"]:.0f}% plus {JHARK["cess_share"]:.0f}% from its mineral-land cess.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Mining money as a share of each state&rsquo;s own revenue, 2026-27 budgets, %</text>',
         f'<rect x="{L}" y="22" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="30" font-size="9.5" fill="#212529">Royalty and other mining receipts</text>',
         f'<rect x="{L + 190}" y="22" width="9" height="9" fill="#a5402c"/><text x="{L + 203}" y="30" font-size="9.5" fill="#212529">Mineral-land cess (now barred)</text>']
    for i, (n, m, c) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 14}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{m * sc:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L + lab + m * sc / 2:.1f}" y="{y + 14}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{m:.0f}</text>')
        if c:
            s.append(f'<rect x="{L + lab + m * sc:.1f}" y="{y}" width="{c * sc:.1f}" height="{bh}" fill="#a5402c"/>')
            s.append(f'<text x="{L + lab + m * sc + c * sc / 2:.1f}" y="{y + 14}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{c:.0f}</text>')
        s.append(f'<text x="{L + lab + (m + c) * sc + 4:.1f}" y="{y + 14}" font-size="9.5" fill="#212529">{m + c:.0f}%</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Own revenue = own tax + own non-tax revenue. PRS budget analyses 2026-27.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Jharkhand&rsquo;s cess is booked across tax and non-tax heads. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_claims():
    rows = [("All states, arrears since 2005 (high)", ARREARS_NATIONAL[1], "#868e96"),
            ("All states, arrears since 2005 (low)", ARREARS_NATIONAL[0], "#868e96"),
            ("Jharkhand, all dues it claims", DUES_JHARK, "#a5402c"),
            ("Odisha, arrears it claimed", ARREARS_ODISHA, "#1c5d99"),
            ("Tata Steel, contingent liability", TATA_CONTINGENT, "#495057")]
    W, L, top, bh, gap, lab = 400, 10, 24, 16, 8, 190
    H = top + len(rows) * (bh + gap) + 32
    sc = (W - L - lab - 60) / 200000
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Reported mineral-tax arrears and claims, Rs thousand crore.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Reported mineral-tax arrears and related claims, Rs thousand crore</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{v / 1000:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Claims as reported, not audited; they overlap and use different definitions.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Jharkhand&rsquo;s figure includes land compensation, not only mineral tax.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_timeline():
    return table(["Date", "What happened"], [
        ("25 July 2024", "Nine-judge Supreme Court bench (Mineral Area Development Authority v. Steel Authority of India), 8&ndash;1: royalty is not a tax; states may tax mineral rights and mineral-bearing land"),
        ("14 August 2024", "Follow-up order: states may recover dues back to 1 April 2005, paid in instalments over 12 years from 1 April 2026, with interest and penalties for the period before the judgment waived (as widely reported)"),
        ("2024&ndash;25", "Jharkhand enacts the Mineral Bearing Land Cess Act 2024; Karnataka passes a mineral-rights tax bill, reserved for the President&rsquo;s assent; Odisha says it must first get its 2004 ORISED Act validated"),
        ("10&ndash;13 August 2026", f"MMDR Amendment Bill introduced and passed by both Houses; about {DEBATE_MIN} minutes of debate in all (PRS)"),
        ("17 August 2026", "Presidential assent, as reported; the Act comes into force on a date the Centre notifies"),
        ("August&ndash;September 2026", "Karnataka, Kerala and Telangana announce a joint Supreme Court challenge; Jharkhand&rsquo;s cabinet approves its own"),
    ])


def t_provisions():
    return table(["Provision", "What it does"], [
        ("Mineral-bearing land brought under the Act", "Section 2 now covers &ldquo;mineral bearing lands&rdquo;, defined by parameters the Centre prescribes, so they fall under central regulation"),
        ("New Section 9D", "No state tax, cess or levy on mineral rights or mineral-bearing land, whether computed on quantity, value, royalty or any other basis, except under conditions the Centre prescribes"),
        ("Rule-making (Section 13)", "The Centre sets the conditions and parameters for any future state levy; PRS notes the Act gives no guiding principles for them"),
        ("Past levies", "Any such levy not deposited with or recovered by the state before the Act commences is deemed invalid; amounts already collected are not refunded"),
        ("Scope", "Major minerals such as coal, iron ore, bauxite, manganese and copper; minor minerals such as sand stay with states"),
    ])


def t_states():
    return table(["State", "Own revenue, 2026-27 BE (Rs cr)", "Mining receipts (Rs cr)", "Share", "What the Act stops"], [
        ("Odisha", f"{ODISHA['own']:,}", f"{ODISHA['mining']:,}", f"{ODISHA['mining_share']:.0f}%", f"A claimed Rs 1 lakh crore of arrears; a possible Rs {ODISHA_ANNUAL:,} crore a year under the ORISED Act, if validated"),
        ("Chhattisgarh", f"{CHHATT['own']:,}", f"{CHHATT['mining']:,}", f"{CHHATT['mining_share']:.0f}%", "Any future state levy on mineral land, unless the Centre allows it"),
        ("Jharkhand", f"{JHARK['own']:,}", f"{JHARK['mining']:,} + cess {JHARK['cess']:,}", f"{JHARK['mining_share']:.0f}% + {JHARK['cess_share']:.0f}%", f"The cess budgeted at Rs {JHARK['cess']:,} crore; a claimed Rs 1.36 lakh crore of dues"),
        ("Karnataka", "&mdash;", "&mdash;", "&mdash;", f"A bill expected to raise about Rs {KARNATAKA_BILL:,} crore a year, still awaiting the President&rsquo;s assent"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>~{DEBATE_MIN} min</b><span>of debate across both Houses for the law that reverses a nine-judge Supreme Court ruling (PRS)</span></div>
<div class="gb-stat"><b>Rs 1.5&ndash;2 lakh cr</b><span>of state mineral-tax arrears since 2005, as estimated, cancelled unless already collected</span></div>
<div class="gb-stat"><b>Rs {JHARK['cess']:,} cr</b><span>Jharkhand budgeted from its mineral-land cess in 2026-27, {JHARK['cess_share']:.0f}% of its own revenue</span></div>
<div class="gb-stat"><b>{ODISHA['mining_share']:.0f}%</b><span>of Odisha&rsquo;s own revenue comes from mining, which the Act leaves untouched; its new-tax hopes are not</span></div>
</div>'''

body = f"""
{stats}

<p>In July 2024 a nine-judge bench of the Supreme Court settled a forty-year argument: royalty on minerals is not a tax, and states have the power to tax mineral rights and the land that holds minerals. It then let states collect what they were owed back to April 2005, in instalments starting in April 2026. Two years later, in August 2026, Parliament passed the Mines and Minerals (Development and Regulation) Amendment Act in four days. PRS counts about {DEBATE_MIN} minutes of debate across both Houses. It bars states from taxing mineral rights or mineral-bearing land except on terms the Centre sets, and cancels any such dues not already collected.</p>
<p>This piece sets out what the Act does, what mineral-rich states stand to lose, and what the Centre says it gains. It follows this blog&rsquo;s pieces on <a href="https://masaladeutsch.blogspot.com/2026/10/seven-states-plan-to-borrow-above-new-3.html">state deficits</a> and <a href="https://masaladeutsch.blogspot.com/2026/10/india-has-auctioned-141-commercial-coal.html">commercial coal mines</a>.</p>

<h2 class="gb-h2">From the court to the Act</h2>
{t_timeline()}

<h2 class="gb-h2">What the Act does</h2>
{t_provisions()}
<p>The Act does not take away royalty, the District Mineral Foundation levy or auction premiums, which states already collect under the central law. What it removes is the separate power the Supreme Court recognised: to tax mineral rights and mineral-bearing land on top of royalty. Future levies are not banned outright, but each would need the Centre&rsquo;s conditions, which the Act leaves entirely to rules. PRS flags two legal questions: whether cancelling unpaid dues while keeping paid ones treats companies that delayed differently from those that paid, contrary to Article 14, and whether the delegation to the Centre has enough guiding principles.</p>

<h2 class="gb-h2">What the states stand to lose</h2>
{chart_share()}
{t_states()}
<p class="gb-note">Mining receipts are PRS&rsquo;s figures for mining-related heads in each 2026-27 budget; PRS&rsquo;s comparison table gives Odisha Rs {ODISHA['mining_tbl']:,} crore on a wider set of heads. Jharkhand&rsquo;s cess is booked across tax and non-tax heads, so it may partly overlap with the mining figure. Budget estimates, not outturns: Jharkhand&rsquo;s 2025-26 mining receipts came in at Rs {JHARK['mining_2526_re']:,} crore against Rs {JHARK['mining_2526_be']:,} crore budgeted.</p>
<p>The states differ in what they lose. Jharkhand is the clearest case: its 2024 cess, at Rs 100 a tonne on coal and iron ore and Rs 50&ndash;70 on bauxite, limestone and manganese, was budgeted at Rs {JHARK['cess']:,} crore this year, about {JHARK['cess_share']:.0f}% of everything the state raises itself. Odisha, which earns about {ODISHA['mining_share']:.0f}% of its own revenue from mining, had not yet levied a new tax: its minister told the Assembly it first needed the Supreme Court to validate its 2004 ORISED Act, under which it expected about Rs {ODISHA_ANNUAL:,} crore a year. Karnataka&rsquo;s bill, estimated to raise about Rs {KARNATAKA_BILL:,} crore a year, was still awaiting the President&rsquo;s assent. For Chhattisgarh the loss is an option rather than a budget line.</p>

<h2 class="gb-h2">The arrears</h2>
{chart_claims()}
<p>The larger sums are the arrears. Estimates of what mining companies owed states for 2005 onwards run to Rs 1.5&ndash;2 lakh crore. Odisha&rsquo;s Advocate General described more than Rs 1 lakh crore as legitimate dues in an affidavit, as reported; Jharkhand claims Rs 1.36 lakh crore from coal companies and others, a figure that also includes land compensation. Tata Steel alone disclosed a contingent liability of Rs {TATA_CONTINGENT:,} crore. Because the first instalments were only due from April 2026, little of this had been paid, and under the Act what was not collected before it commenced is gone. Many of the companies that owed it are central public-sector firms such as Coal India&rsquo;s subsidiaries and SAIL, so part of the &ldquo;loss&rdquo; is a transfer between the Centre&rsquo;s companies and the states.</p>

<h2 class="gb-h2">The Centre&rsquo;s case</h2>
<p>The Bill&rsquo;s statement of objects cites a heavy tax burden on the sector and retrospective taxes, and aims for &ldquo;certainty, stability and predictability&rdquo;. The argument has substance: coal, iron ore and limestone feed power, steel and cement, and a state cess of Rs 100 a tonne on coal or iron ore would pass into electricity, steel and cement prices across the country, not only in the taxing state. Different levies in each state can also distort where mines are bid for. The Mines Ministry says states will keep about 90% of mining-related payments; that claim could not be checked, and it concerns existing payments rather than the new taxing power.</p>
<p>The counter-argument is about who decides. The Supreme Court found the power to be the states&rsquo;, and the Act moves it to the Centre by ordinary law rather than constitutional amendment, with almost no debate. Whether that holds will be decided by the challenges Karnataka, Kerala, Telangana and Jharkhand have announced.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Centre should publish the rules under the new Section 13, setting out on what terms a state may levy, with a cap per tonne by mineral, so that states know what they can raise and industry knows its maximum cost.</li>
<li>The Ministry of Mines should publish, state by state, the arrears that the Act cancels and how much was collected before it commenced, with the share owed by central public-sector companies.</li>
<li>If the Centre&rsquo;s aim is uniform mineral costs, a shared levy collected centrally and passed to producing states by output would meet it without removing the states&rsquo; revenue.</li>
<li>Laws that reverse a Constitution Bench ruling should go to a standing committee before passage.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Act&rsquo;s text and gazette notification could not be opened; its provisions come from PRS&rsquo;s summary of the Bill as passed and legal commentary, and the commencement date had not been found. The arrears figures are claims and estimates, not audited amounts, and they overlap. Whether Jharkhand actually collected any cess before commencement, and how much, was not found. Mining receipts for Karnataka, Rajasthan and Madhya Pradesh were not found on a comparable basis and are left out. The status of the states&rsquo; Supreme Court challenges at the end of October 2026 is not known. This is not legal advice.</p>
"""

sources = ("Act: PRS Legislative Research, bill track and issues for consideration on the MMDR (Amendment) Bill 2026, Monsoon Session 2026 vital stats and August 2026 Monthly Policy Review; SCC Online (20 August 2026), Bar &amp; Bench, PSU Watch, Takshashila, PIB factsheet as indexed. "
           "Supreme Court: Mineral Area Development Authority v. Steel Authority of India (25 July 2024) and the 14 August 2024 order, as reported. "
           "States: PRS budget analyses 2026-27 for Odisha, Chhattisgarh and Jharkhand; Jharkhand Mineral Bearing Land Cess Act 2024 (LegitQuest; Bloomberg, August 2024); Karnataka bill (Business Standard; Deccan Herald); Odisha ORISED Act and arrears (OdishaBytes; Policy Circle; UNI); Jharkhand challenge (ThePrint; UNI, September 2026); Congress-ruled states&rsquo; challenge (Business Standard, 20 August 2026). "
           "Arrears and liabilities: Federal, National Herald, Business Standard, Studycafe (Tata Steel). Shares of own revenue are this blog&rsquo;s arithmetic. Not legal advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/seven-states-plan-to-borrow-above-new-3.html", "Seven States Plan to Borrow Above the New 3% Limit. Last Year, Most Missed Their Targets Anyway"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-has-auctioned-141-commercial-coal.html", "India Has Auctioned 141 Commercial Coal Mines Since 2020. Fifteen Produce Coal"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-draft-steel-policy-plans-604-mt.html", "India&rsquo;s Draft Steel Policy Plans 604 Mt by 2047"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-first-seabed-mineral-auction.html", "India&rsquo;s First Seabed Mineral Auction Drew No Winner"),
]

build("Mining · 28 October 2026",
      "States Won the Right to Tax Mines in 2024. A 45-Minute Law Took It Back, Along With Up to Rs 2 Lakh Crore of Dues",
      "A nine-judge Supreme Court bench ruled that states may tax mineral rights and mineral land. The MMDR Amendment Act 2026 now bars such levies except on the Centre&rsquo;s terms and cancels uncollected arrears. Jharkhand loses a cess worth a fifth of its own revenue; Odisha loses the arrears it claimed.",
      body, sources, related, OUT)
print({k: round(v, 1) for k, v in [("od", ODISHA["mining_share"]), ("cg", CHHATT["mining_share"]), ("jh", JHARK["mining_share"]), ("jhc", JHARK["cess_share"])]})
