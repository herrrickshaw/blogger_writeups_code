import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-farmer-payments-dlt.html'
REPO = 'https://github.com/herrrickshaw/farmer-payments-dlt'

# ---- PM-KISAN (PIB backgrounders and Parliament answers) ----------------------------------
PMK_24_FARMERS = 9.34e7          # 24th instalment, 30 Oct 2026 (PIB)
PMK_24_AMT = 18690               # Rs crore
PMK_19_FARMERS = 100685615       # 19th instalment, Dec 2024-Mar 2025 (PIB annexure, 29 Jul 2025)
PMK_CUM = 4.64                   # Rs lakh crore over 24 instalments
PMK_RECOVERED = 416.75           # Rs crore recovered from ineligible beneficiaries, as of Dec 2025
PMK_DBT_SAVING = 22106.14        # Rs crore, DBT Bharat "estimated gains" to Mar 2025
PMK_DELETED = 2.1174e7           # ineligible beneficiaries deleted (DBT Bharat)
PMK_PEND_SEED = 2345714          # stop-payment: Aadhaar not seeded with bank account (RS answer, 9 Mar 2026)
PMK_PEND_EKYC = 3360535          # stop-payment: e-KYC pending
PMK_SUCCESS_19 = 99.92           # transaction success rate, 19th instalment (PIB, 5 Aug 2025)
INSTAL = 2000

drop = PMK_19_FARMERS - PMK_24_FARMERS
drop_pct = drop / PMK_19_FARMERS * 100
pend = PMK_PEND_SEED + PMK_PEND_EKYC
pend_amt = pend * INSTAL / 1e7   # Rs crore per instalment, upper bound (categories may overlap)
fail_19 = (100 - PMK_SUCCESS_19) / 100 * PMK_19_FARMERS

# ---- Farmer IDs and e-NAM -----------------------------------------------------------------
FID = 11e7                       # 23 Oct 2026
FID_JUL = 102825379              # 30 Jul 2026, Lok Sabha
FID_TENANTS = 28680              # tenants/sharecroppers registered in five states (Hindu BusinessLine/Indian Express via Elets)
ENAM_FARMERS = 1.89e7            # 30 Jun 2026
ENAM_TRADE = 4.84e5              # Rs crore cumulative 2016-Mar 2026
ENAM_INTERSTATE = 83.95          # Rs crore cumulative inter-state
ENAM_IS_2526 = 14.28             # Rs crore inter-state 2025-26
ENAM_BIDS = 2.8                  # trader bids per lot 2025-26
is_share = ENAM_INTERSTATE / ENAM_TRADE * 100

# ---- Cane dues, 2025-26 season ------------------------------------------------------------
CANE_DUE = 112740                # Rs crore payable for the season (PIB, 5 May 2026)
CANE_PAID_APR = 99961            # paid by 20 Apr 2026
CANE_ARR_FEB = 16087             # unpaid on 16 Feb 2026 (Standing Committee, via The Hindu)
CANE_PAID_AUG_PCT = 97           # cleared by 20 Aug 2026 (USDA FAS GAIN, Oct 2026)
CANE_STATES_FEB = [("Karnataka", 4956), ("Maharashtra", 4252), ("Uttar Pradesh", 3287)]
cane_apr = CANE_DUE - CANE_PAID_APR
cane_aug = CANE_DUE * (100 - CANE_PAID_AUG_PCT) / 100
# Escrow sizing: 14 days of cane purchases, assuming the season's dues accrue over a 150-180 day crush
esc_lo = CANE_DUE / 180 * 14
esc_hi = CANE_DUE / 150 * 14


def cr(x):
    return f"&#8377;{x:,.0f} crore"


def chart_cane():
    rows = [("16 Feb 2026", CANE_ARR_FEB, ""), ("20 Apr 2026", cane_apr, ""), ("20 Aug 2026", cane_aug, "~")]
    W, L, top, bh, gap, lab = 340, 4, 50, 24, 12, 96
    H = top + len(rows) * (bh + gap) + 40
    mx = max(r[1] for r in rows)
    sc = (W - L - lab - 92) / mx
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Unpaid sugarcane dues owed by mills to farmers in the 2025-26 season, at three dates.">',
         f'<text x="{L}" y="16" font-size="14" fill="#495057">Cane dues unpaid, 2025-26 season</text>',
         f'<text x="{L}" y="35" font-size="11.5" fill="#6c757d">&#8377; crore owed by mills on each date</text>']
    for i, (d, v, pre) in enumerate(rows):
        y = top + i * (bh + gap)
        w = max(v * sc, 2)
        s.append(f'<text x="{L + lab - 6}" y="{y + 17}" font-size="12.5" fill="#212529" text-anchor="end">{d}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{w:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L + lab + w + 5:.1f}" y="{y + 17}" font-size="12.5" fill="#212529">{pre}{v:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 22}" font-size="10.5" fill="#6c757d">Standing Committee (Feb); PIB (Apr); USDA FAS, 97% cleared (Aug).</text>')
    s.append(f'<text x="{L}" y="{H - 7}" font-size="10.5" fill="#6c757d">Aug figure is this blog&rsquo;s arithmetic from the 97% share.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_fail():
    rows = [
        ("<b>Ineligible people paid</b><br><i>Income-tax payers, officials on the list</i>", "<b>No.</b> A ledger records a wrong entry faithfully", "Check income and land data before enrolment"),
        ("<b>Duplicate payments</b><br><i>Same person, two registrations</i>", "<b>Partly.</b> Any database with a unique key does this", "One Farmer ID per person"),
        ("<b>Eligible farmers held back</b><br><i>e-KYC, bank-Aadhaar seeding, land seeding</i>", "<b>No.</b> The block is before the payment", "Seed bank accounts at enrolment; village camps"),
        ("<b>Credit fails</b><br><i>Account closed, Aadhaar de-seeded</i>", "<b>No.</b> PFMS already tracks each transfer", "Publish failure and retry counts"),
        ("<b>Mill pays late</b><br><i>Mill short of cash</i>", "<b>Partly.</b> Escrow works only if someone funds it", "Bank-guaranteed escrow; enforce interest on delay"),
        ("<b>Buyer underbids</b><br><i>Few bidders per lot</i>", "<b>Partly.</b> A tamper-evident bid log", "More buyers per mandi; inter-state licences"),
        ("<b>Grade disputed</b><br><i>No trusted assay</i>", "<b>No.</b> The ledger trusts whoever types the grade", "Lab assays at the mandi"),
        ("<b>Land record conflicts</b><br><i>Revenue, survey, registration disagree</i>", "<b>Yes.</b> Three offices, one shared record", "What Andhra Pradesh is piloting"),
    ]
    return table(["Where it goes wrong", "Does a shared ledger help?", "What fixes it"], rows)


def t_cases():
    rows = [
        ("AgriDigital, Australia (2016)", "First grain sale settled on a blockchain: 23.46 t of wheat, grower paid within an hour", "Payment went through a wallet backed by ordinary banking; the extended pilot did not settle on blockchain"),
        ("Etherisc and ACRE Africa, Kenya (2021)", "17,000+ farmers insured; replanting payouts triggered by smart contract", "Money moved on M-Pesa, the existing mobile-money rail"),
        ("Oxfam, Etherisc and Sanasa, Sri Lanka", "About 200 farmers, first weather-index payouts made", "Small; no cost comparison found"),
        ("UNEP/CTCN, Thailand (2025)", "Feasibility study for parametric crop insurance", "Pilot planned for 200&ndash;300 farmers"),
        ("Mee Bhoomi Blockchain, Andhra Pradesh (Jul 2026)", "Land records on a blockchain; 1,37,763 parcels in 89 villages", "Registry, not payments; state-wide roll-out planned from November"),
    ]
    return table(["Project", "What happened", "The catch"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{PMK_24_FARMERS / 1e7:.2f} crore</b><span>farmers paid in PM-KISAN&rsquo;s 24th instalment (30 October 2026), down from {PMK_19_FARMERS / 1e7:.2f} crore in early 2025</span></div>
<div class="gb-stat"><b>&#8377;{PMK_RECOVERED:,.0f} cr</b><span>recovered from ineligible PM-KISAN beneficiaries by December 2025, the only recovery figure the government publishes</span></div>
<div class="gb-stat"><b>{cr(cane_apr).replace(' crore', ' cr')}</b><span>of 2025-26 cane dues still unpaid by mills on 20 April 2026, despite a 14-day payment rule</span></div>
<div class="gb-stat"><b>{is_share:.3f}%</b><span>of e-NAM&rsquo;s &#8377;4.84 lakh crore of trade since 2016 has crossed a state border</span></div>
</div>'''

body = f"""
{stats}

<p>Blockchain keeps being offered as a fix for how Indian farmers get paid. A 2022 review in the <i>Journal of Agricultural Extension Management</i>, published by MANAGE, the agricultural extension institute in Hyderabad, says the technology &ldquo;allows widespread financial transactions between underutilized groups, without the need for intermediaries such as banks&rdquo;. A small open-source project built on that review, <a href="{REPO}">farmer-payments-dlt</a>, takes the claim seriously enough to write the code. It models three payment flows on a distributed ledger (DLT): escrow for crop sales, government scheme payments, and reconciliation against bank credits.</p>

<p>Its design note is unusually honest. It says a ledger is worth using only &ldquo;where several parties who don&rsquo;t fully trust each other need one shared, tamper-evident record&rdquo;, that a single database should be used where one will do, and that money should keep moving on India&rsquo;s existing rails (bank transfers, UPI and direct benefit transfer, or DBT). This piece takes that test and applies it to the places where farmer payments in India actually go wrong.</p>

<p>The short answer: most failures happen before any payment is made, in deciding who is eligible and which bank account belongs to them. A ledger records those decisions; it does not make them. The one place where several parties genuinely share a record they do not trust each other to keep, land records, is where an Indian state is now testing a blockchain.</p>

<h2 class="gb-h2">Scheme payments: the problem is the list, not the transfer</h2>

<p>PM-KISAN pays landholding farmer families &#8377;6,000 a year in three instalments of &#8377;{INSTAL:,}. The 24th instalment, released on 30 October 2026, sent about &#8377;{PMK_24_AMT:,} crore to {PMK_24_FARMERS / 1e7:.2f} crore farmers, taking the total since 2019 past &#8377;{PMK_CUM} lakh crore. The transfer itself works: the agriculture ministry says the 19th instalment had a transaction success rate of {PMK_SUCCESS_19}%, which on that instalment&rsquo;s {PMK_19_FARMERS / 1e7:.2f} crore payees means roughly {fail_19 / 1e3:,.0f} thousand failed credits, retried later. It names the causes as Aadhaar numbers dropped from the National Payments Corporation of India (NPCI) mapper, which routes a payment from an Aadhaar number to one bank account, accounts not mapped at all, and closed accounts.</p>

<p>The larger numbers are elsewhere. The scheme began on trust, with states registering farmers on self-declaration and Aadhaar checks relaxed in some states. Income-tax payers, government employees and others not entitled to it were paid. The government&rsquo;s DBT portal credits PM-KISAN with &#8377;{PMK_DBT_SAVING:,.0f} crore of &ldquo;savings&rdquo; from deleting {PMK_DELETED / 1e7:.2f} crore ineligible names. Against money already paid to ineligible people, states had recovered &#8377;{PMK_RECOVERED} crore by December 2025. State audits show how hard recovery is: Bihar&rsquo;s auditor found &#8377;62.67 crore recoverable and about &#8377;5 crore recovered by early 2022; Haryana&rsquo;s found &#8377;40.70 crore paid to ineligible people and income-tax payers, of which &#8377;4.60 lakh had been recovered.</p>

<p>Tightening the list has also cut people off. Payees fell from {PMK_19_FARMERS / 1e7:.2f} crore in the 19th instalment to {PMK_24_FARMERS / 1e7:.2f} crore in the 24th, about {drop / 1e5:,.0f} lakh fewer ({drop_pct:.1f}%). In March 2026 the ministry told the Rajya Sabha that {PMK_PEND_SEED / 1e5:.1f} lakh beneficiaries had payments stopped because Aadhaar was not seeded to their bank account and {PMK_PEND_EKYC / 1e5:.1f} lakh because e-KYC was pending, alongside those whose land records were not yet seeded. If none of those overlap, that is up to {pend / 1e5:.0f} lakh farmers and about &#8377;{pend_amt:,.0f} crore withheld per instalment.</p>

<p>Look at what the project&rsquo;s prototype does for scheme payments. Its <code>disburse</code> rule rejects a second payment for the same scheme, period and farmer, and rejects any farmer not marked verified. The duplicate check is a unique key, which any database enforces. The verification is a <code>verified</code> flag passed in by the paying agency itself: the ledger takes the agency&rsquo;s word for it. That is not a flaw in the code; it is the point. Whether a farmer owns land, pays income tax or is the person holding the bank account is decided in land records, the income-tax database and the NPCI mapper. A ledger downstream of those would record ineligible payments just as permanently as eligible ones.</p>

<p>The government&rsquo;s own answer is a better register. Under AgriStack, states have built farmer registries in which each Farmer ID is generated by matching a farmer to digitised land records; the count passed 11 crore on 23 October 2026, five months ahead of the March 2027 target, up from {FID_JUL / 1e7:.2f} crore on 30 July. The ministry says more than 6 crore farmers have already received scheme benefits through Farmer ID-based delivery. The register inherits the limits of the land records it is built on: only about {FID_TENANTS:,} tenants and sharecroppers had been registered, in five states, by October.</p>

<h2 class="gb-h2">Crop payments: escrow fixes a risk mills cannot afford to cover</h2>

<p>The prototype&rsquo;s second flow is an escrow. A buyer locks the price up front; the money is released when delivery is confirmed at the promised grade, and otherwise held until an arbiter decides the farmer&rsquo;s share. This answers a real Indian problem: sugar mills paying for cane late.</p>

{chart_cane()}

<p>The Sugarcane (Control) Order, 1966 requires mills to pay within 14 days of delivery, and states enforce it. In 2025-26 that rule held poorly. On 16 February 2026 mills owed farmers {cr(CANE_ARR_FEB)}, according to figures given to a parliamentary standing committee, with Karnataka ({cr(4956)}), Maharashtra ({cr(4252)}) and Uttar Pradesh ({cr(3287)}, across 121 mills) the largest. By 20 April, of {cr(CANE_DUE)} due for the season, {cr(CANE_PAID_APR)} had been paid, leaving {cr(cane_apr)}. The US Department of Agriculture&rsquo;s office in New Delhi put dues 97% cleared by 20 August, which leaves about {cr(cane_aug)}.</p>

<p>An escrow would have made those payments certain only if the mills had the money to lock up first. Mills are paying a cane price that has risen from &#8377;275 a quintal in 2019-20 to &#8377;365 for 2026-27, while the minimum price at which they may sell sugar has been held at &#8377;31 a kilo since February 2019. Arrears are a symptom of that squeeze. To escrow 14 days of purchases, mills would need roughly &#8377;{esc_lo:,.0f}&ndash;{esc_hi:,.0f} crore set aside at any time, by this blog&rsquo;s arithmetic, assuming the season&rsquo;s &#8377;1.13 lakh crore of purchases is spread over a crushing season of 150&ndash;180 days. A bank would have to fund or guarantee that, and price it. The project&rsquo;s own design note lists this as an open question: who funds an escrow if buyers pay on credit.</p>

<p>Mandi sales are a different case. e-NAM, the national electronic market, already pays sale proceeds directly into farmers&rsquo; bank accounts after an online auction. It had {ENAM_FARMERS / 1e7:.2f} crore farmers registered by June 2026 and has handled &#8377;4.84 lakh crore of trade since 2016. Its weakness is not payment but competition: an average of {ENAM_BIDS} trader bids per lot in 2025-26, and inter-state trade worth &#8377;{ENAM_IS_2526} crore that year and &#8377;{ENAM_INTERSTATE} crore in total, or {is_share:.3f}% of all e-NAM trade. A tamper-evident log of bids would help show manipulation, which is what a 2020 study of three Uttar Pradesh mandis proposed after finding gaps between arrival prices and bidding prices. It would not add buyers.</p>

<p>Grade disputes have the same limit. In the prototype the buyer enters the delivered grade; if it is below the promised grade, the escrow goes to dispute. Whoever controls the grade entry controls the outcome. An independent assaying lab at the mandi solves that; a ledger only records the lab&rsquo;s result.</p>

<h2 class="gb-h2">Where each failure point lands</h2>

{t_fail()}

<p class="gb-note">This blog&rsquo;s assessment, using the project&rsquo;s own test: a shared ledger helps where several parties who do not trust each other must keep one record. &ldquo;Partly&rdquo; means the ledger adds an audit trail, but the cause of the failure lies elsewhere.</p>

<h2 class="gb-h2">Reconciliation: already being done, centrally</h2>

<p>The third flow compares payments the ledger approved with credits the bank reports, and flags shortfalls. For government schemes that job belongs to the Public Financial Management System (PFMS), which issues each fund-transfer order, records the bank&rsquo;s response and returns rejections with a reason code, such as Aadhaar not seeded in the NPCI mapper. A farmer can see the result through the PM-KISAN portal&rsquo;s status page. The DBT Mission has told departments that account-number-based payments through PFMS will be switched off, leaving only payments routed by Aadhaar. The system is centralised, and the farmer cannot audit it, but the parties involved (the ministry, PFMS, NPCI and banks) are all regulated public or quasi-public bodies, which is a weak case for the multi-party distrust a blockchain is for.</p>

<p>Reading the prototype also shows how easy it is to leave a gap. Its <code>reconcile</code> function counts what a farmer is owed from released escrows and scheme disbursements only. When a disputed escrow is settled by the arbiter with a share for the farmer, that share is recorded on the ledger but never added to what is owed, so a bank&rsquo;s failure to pay it would not be flagged. A test run here, with one disputed escrow settled at 60% of &#8377;10,000 and one &#8377;2,000 scheme payment, flagged only the &#8377;2,000. It is a small fix, and exactly the kind of issue a farmer could never spot from outside.</p>

<h2 class="gb-h2">What the evidence elsewhere shows</h2>

{t_cases()}

<p>The best-known farmer-payment case, Australia&rsquo;s AgriDigital, settled its first grain sale on a blockchain in December 2016 and paid the grower within an hour. Even then, the payment ran through a digital wallet backed by conventional banking, and the company said it was not using blockchain for settlements during the extended pilot that followed. Index insurance pilots in Kenya and Sri Lanka used smart contracts to trigger payouts, but paid through mobile money. A 2026 review of such initiatives in <i>Frontiers in Sustainable Food Systems</i> puts the limit plainly: &ldquo;Blockchain provides certainty about data integrity, not about counterparty intentions.&rdquo; CGAP, the World Bank-hosted financial inclusion group, warned in 2018 that cost, complexity and context may erase blockchain&rsquo;s advantages over conventional approaches.</p>

<p>In India, the project&rsquo;s search found no blockchain payment pilot inside AgriStack, e-NAM or the crop insurance scheme PMFBY. Its survey of open-source code found agriculture repositories with between 0 and 34 stars on GitHub, mostly hackathon projects, none production-grade. The one live government deployment found for this piece is Andhra Pradesh&rsquo;s Mee Bhoomi Blockchain, launched on 23 July 2026: land records from the revenue, survey and registration departments on Hyperledger Fabric, a permissioned blockchain, piloted on 1,37,763 parcels in 89 re-surveyed villages, with a state-wide roll-out planned from November. That is the right layer. Three departments keep separate records of the same land; disputes over which one is right are what block mutation, loans and, downstream, scheme payments. Whether it works will show in mutation times and dispute counts, which have not yet been published.</p>

<h2 class="gb-h2">The prototype, briefly</h2>

<p>The <a href="{REPO}">farmer-payments-dlt</a> code is a teaching model of about 140 lines of standard-library Python with seven passing tests. Each block is hash-chained to the previous one and carries a keyed-hash (HMAC) signature from the consortium member who added it, so tampering is detectable and only members can write. It has no network, no consensus between nodes, and no public-key signatures; escrow states and the duplicate register live in memory rather than being rebuilt from the chain. It records instructions and confirmations, never money. As its README says, a real system would run on a permissioned platform such as Hyperledger Fabric, or on an Ethereum-compatible chain with audited contracts. Its value is the documentation: the reading of the 2022 review, the list of challenges and how a consortium design answers each, and the plain statement of what stays off the ledger.</p>

<h2 class="gb-h2">What would fix this</h2>

<ul>
<li><b>Publish PM-KISAN&rsquo;s ineligible-payment ledger, state by state.</b> The government publishes the amount recovered (&#8377;{PMK_RECOVERED} crore) but not, in its recent releases, the total paid to people later found ineligible. Without that figure the recovery rate cannot be judged.</li>
<li><b>Publish stop-payment and failure counts with every instalment</b>: how many farmers were held for e-KYC, bank seeding or land seeding, how many credits failed, and how many were later paid, so the fall from {PMK_19_FARMERS / 1e7:.2f} crore to {PMK_24_FARMERS / 1e7:.2f} crore can be split into cleaning and exclusion.</li>
<li><b>Seed the bank account at enrolment.</b> The DBT Mission already asks schemes to check NPCI mapper status when Aadhaar is authenticated. Making that check part of Farmer ID creation would catch failed payments before they happen.</li>
<li><b>Price cane escrow before mandating it.</b> A bank-guaranteed escrow for cane, backed by a mill&rsquo;s sugar or ethanol receivables, could be tested in one state with high arrears. Enforcing the interest that the Sugarcane (Control) Order already allows on late payment would come first.</li>
<li><b>Put assaying labs, not ledgers, at the centre of e-NAM grade disputes</b>, and log results so they cannot be edited afterwards; that log is where a hash chain is cheap and useful.</li>
<li><b>Measure Andhra Pradesh&rsquo;s blockchain land records</b> against its old system on mutation time, disputes and fraud before other states copy it.</li>
</ul>

<p>These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>

<p>The total amount paid to ineligible PM-KISAN beneficiaries nationally was not found in a recent official source; a figure of about &#8377;4,350 crore circulates but could not be traced to a Parliament answer or audit report, so it is not used. In 2021 the government was asked about recovering about &#8377;3,000 crore from 42 lakh ineligible beneficiaries, but that figure appears in the question, not in a confirmed answer. The count of beneficiaries stopped for pending land seeding in March 2026 was not read. The stop-payment categories may overlap, so the {pend / 1e5:.0f} lakh total is an upper bound. The February cane arrears and the comparison with earlier years come from press reports of a standing committee report; one report said arrears were up about &#8377;2,049 crore on the previous season, another said the previous figure was &#8377;497 crore, and the earlier-year comparison is therefore not used. The August cane figure is calculated from a rounded 97%. The escrow sizing assumes a 150&ndash;180 day crushing season and an even pace of purchases. No cost per payment, time-to-credit data or outcome study was found for any blockchain farmer-payment pilot, in India or abroad, and no results have been published for Andhra Pradesh&rsquo;s land-record pilot.</p>
"""

sources = ("PM-KISAN: PIB backgrounders on the 23rd (20 Jun 2026) and 24th (30 Oct 2026) instalments; PIB, &ldquo;Beneficiaries under PM-KISAN&rdquo; (29 Jul 2025, instalment annexure); PIB, &ldquo;Aadhaar seeding for PM-KISAN&rdquo; (5 Aug 2025, 99.92% success rate and failure causes); Rajya Sabha unstarred question 2402 (answered March 2026, stop-payment counts); Lok Sabha unstarred question 448 (21 Jul 2026). "
           "DBT savings: DBT Bharat, &ldquo;Estimated Gains&rdquo; (to March 2025). PFMS, &ldquo;DBT Validation/Payment Error/Rejection and action thereon&rdquo;; DBT Mission letter on Aadhaar Payment Bridge (May 2026, as published by Himachal Pradesh NHM). "
           "State audits: CAG report on Bihar (2022, Chapter II); CAG report on Haryana as reported by NewsClick (March 2023). "
           "Farmer IDs: Lok Sabha unstarred question 2753 (4 Aug 2026); Ministry of Agriculture via PIB and PTI (24 Oct 2026); registry profile from The Hindu BusinessLine and The Indian Express as summarised by Elets eGov (search text only). "
           "e-NAM: PIB, &ldquo;Strengthening of agricultural marketing&rdquo; (28 Jul 2026); PIB/DD News on 1,656 mandis and &#8377;4.84 lakh crore (2026). "
           "Cane: PIB, FRP for 2026-27 (5 May 2026); The Hindu and Times of India on the Standing Committee figures (March&ndash;April 2026); USDA FAS GAIN Sugar Semi-annual IN2026-0051 (Oct 2026); Lok Sabha unstarred question 2901 (10 Mar 2026) for the 14-day rule. Sugar minimum selling price of &#8377;31/kg since February 2019 as used in earlier posts on this blog. "
           "Blockchain evidence: Deshmukh &amp; Patil (2022), J. Agricultural Extension Management 23(1); UNSW BusinessThink on AgriDigital (June 2017); Frontiers in Sustainable Food Systems, &ldquo;When verification is not enough&rdquo; (2026); Etherisc blog on ACRE Africa (Aug 2021); CGAP, &ldquo;Exploring Blockchain Applications to Agricultural Finance&rdquo; (2018); Sri Lanka and Thailand pilots as listed in the project&rsquo;s literature file (search text only). "
           "Andhra Pradesh: The Hindu, New Indian Express and Deccan Chronicle (22&ndash;24 Jul 2026). "
           f"Project: <a href=\"{REPO}\">github.com/herrrickshaw/farmer-payments-dlt</a> (README, design note, article notes, literature and repository lists; tests run for this piece). "
           "Arithmetic (beneficiary fall, withheld amounts, cane balances, escrow size, inter-state share) is this blog&rsquo;s, in out/research/farmer-payments-dlt/. This is not financial or legal advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html", "A 17% Rural Pay Rise That Nobody Received"),
    ("https://masaladeutsch.blogspot.com/2026/09/pmfby-advertises-51-return-to-farmers.html", "PMFBY Advertises a 5:1 Return to Farmers. Farmers Put In About a Fifth of the Premium. Governments Put In the Rest."),
    ("https://masaladeutsch.blogspot.com/2026/08/sugar-at-5570-kilo-why-cane-acreage.html", "Sugar at &#8377;55.70 a Kilo: Why Cane Acreage Isn&rsquo;t Growing, and Ethanol Is Losing the Diversion Race"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-2026-27-ethanol-tender-drops.html", "India&rsquo;s 2026-27 Ethanol Tender Drops Cane Juice, Cuts Maize by Rs 3 a Litre and Flips From Sugar-First to Cheapest-First"),
    ("https://masaladeutsch.blogspot.com/2026/07/the-price-of-grain-msp-msv-and.html", "The Price of Grain: MSP, MSV, and the Arithmetic of the Indian Grain State"),
    ("https://masaladeutsch.blogspot.com/2026/10/gems-purchases-stopped-growing-in-2025.html", "GeM&rsquo;s Purchases Stopped Growing in 2025-26. Small Firms Won Two-Thirds of the Orders but Less Than Half the Money"),
]

build("Agriculture &middot; Fintech &middot; 3 November 2026",
      "India Doesn&rsquo;t Need a Blockchain to Pay Its Farmers. It May Need One to Agree on Who Owns the Land",
      "A small open-source project models farmer payments on a ledger. Tested against where Indian payments actually fail (PM-KISAN&rsquo;s beneficiary list, sugar mills&rsquo; arrears, thin mandi auctions), most problems arise before any money moves. The one multi-party record worth a blockchain is land, which Andhra Pradesh is now piloting.",
      body, sources, related, OUT)
print("drop", round(drop / 1e5), "lakh", round(drop_pct, 1), "% | pend", round(pend / 1e5, 1), "lakh, Rs", round(pend_amt), "cr | fail19", round(fail_19),
      "| cane apr", cane_apr, "aug", round(cane_aug), "| escrow", round(esc_lo), round(esc_hi), "| interstate", round(is_share, 4))
