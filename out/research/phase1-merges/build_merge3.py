import re
ROOT='/home/user/blogger_writeups_code/'
t=open(ROOT+'posts/upi-fees-are-now-legal-petrol-pumps.html').read()
b=open(ROOT+'posts/beyond-pump-what-upi-fee-would-cost.html').read()
B_URL='https://masaladeutsch.blogspot.com/2026/08/beyond-pump-what-upi-fee-would-cost.html'
T_URL='https://masaladeutsch.blogspot.com/2026/08/upi-fees-are-now-legal-petrol-pumps.html'
LPG_URL='https://masaladeutsch.blogspot.com/2026/08/lpgs-missing-number-7308-commission-and.html'
def rep(s,a,c,n=1):
    k=s.count(a); assert k==n,(k,a[:100]); return s.replace(a,c)
def grab(s,a,z):
    i=s.index(a); j=s.index(z,i); return s[i:j]

# head
t=rep(t,'while a fee would apply to all &#8377;100. The same forecourt, though, holds the hedge: cash, and the fee income of dispensing it.</p>',
 'while a fee would apply to all &#8377;100. The same forecourt, though, holds the hedge: cash, and the fee income of dispensing it. The piece then runs the same arithmetic across every other counter NPCI publishes, from groceries and restaurants to jewellery and electronics.</p>')
t=rep(t,'<p style="order:2" class="eyebrow">Payments &middot; Fuel retail &middot; Rural cash access</p>',
 '<p style="order:2" class="eyebrow">Payments &middot; Fuel retail &middot; Merchant categories &middot; Rural cash access</p>')
t=rep(t,'<p class="revised" data-gs-revision-v1="1">Published <time datetime="2026-08-08" itemprop="datePublished">8 August 2026</time> &middot; v1.0.0 &middot;',
 '<p class="revised" data-gs-revision-v1="1">Published <time datetime="2026-08-08" itemprop="datePublished">8 August 2026</time> &middot; revised <time datetime="2026-11-10" itemprop="dateModified">10 November 2026</time> &middot; v2.0.0 &middot; absorbs the retired companion post on UPI fees beyond the pump &middot; SBI Research, &ldquo;New Insights from UPI Data&rdquo; (18 August 2025) &middot;')

# 10 Nov note
note=('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
'<b>Updated 10 November 2026.</b> This page now carries this blog&rsquo;s companion post <i>UPI Mimicking the Plastic Card: Will MDR Be Like Visa Fees?</i>, which has been retired. '
'Its cross-category analysis is the section <a href="#beyond-the-pump">Beyond the pump</a> below. '
'The fee itself has still not started. The notified schedule is 0.4% on person-to-merchant UPI payments above &#8377;2,000, with smaller payments, person-to-person transfers and small merchants exempt, and a flat &#8377;5 for fuel and some other categories. '
'NPCI deferred it on 13 October 2026, and no start date had been announced by 10 November; a 1 January 2027 start has been reported but not decided. '
'Two consequences of the &#8377;2,000 threshold run through the merged sections. Most food and grocery payments, at average tickets of &#8377;113 to &#8377;214, would pay nothing. '
'And a domestic 14.2 kg LPG refill, &#8377;942 in Delhi in November (<a href="https://www.goodreturns.in/news/gas-cylinder-prices-hike-from-november-1-2026-19-kg-commercial-lpg-prices-hiked-by-rs-10-17-diwali-1544457.html">Goodreturns</a>), is below the threshold too, so it would not carry the fee at all.</div>\n')
anchor='<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 7 November 2026.</b>'
t=rep(t,anchor,note+anchor)

# companion note in the forecourt section -> in-page
t=rep(t,'That full cross-category analysis, including a dedicated look at groceries and food service, is worked in a <a href="'+B_URL+'">companion article</a>, &ldquo;Beyond the Pump.&rdquo; What follows here stays with the forecourt: the per-tank arithmetic, and the ATM hedge.</div>',
 'That full cross-category analysis, including a dedicated look at groceries and food service, is worked in the section <a href="#beyond-the-pump">Beyond the pump</a> below. What follows first stays with the forecourt: the per-tank arithmetic, and the ATM hedge.</div>')

# absorbed block
blk=grab(b,'<h2>Is UPI heading toward card-network pricing?</h2>','<div class="note"><b>What this article does not establish.</b>')
ex={'1':'6','2':'7','3':'8','4':'9'}
blk=re.sub(r'Exhibit (\d)',lambda m:'Exhibit '+ex[m.group(1)],blk)
blk=rep(blk,'<p class="exsrc">The fuel row is verified in the companion article (PPAC Ready Reckoner FY2025-26 H1).','<p class="exsrc">The fuel row is the Exhibit 2 figure above (PPAC Ready Reckoner FY2025-26 H1).')
blk=rep(blk,'LPG refills share the structure &mdash; a fixed regulated distributor commission on an &#8377;800-plus cylinder &mdash; but the current commission value is not in this author&rsquo;s PPAC documents, so it is named and not numbered.</li>',
 'LPG refills share the structure, a fixed regulated distributor commission, but at a wider margin than this blog first assumed: &#8377;73.08 on a &#8377;942 Delhi domestic cylinder, or 7.76% (<a href="'+LPG_URL+'">worked here</a>). More to the point, a domestic 14.2 kg refill is below the notified fee&rsquo;s &#8377;2,000 threshold, so it would not pay the MDR at all. A 19 kg commercial cylinder (&#8377;2,820 in Delhi from 1 November) is above it; whether LPG falls in the flat &#8377;5 fuel category or pays 0.4% was not established.</li>')
blk=rep(blk,'the same order of magnitude as kirana in the companion piece, because in practice it largely is kirana.','the same order of magnitude as the kirana row in the leverage-curve list above, because in practice it largely is kirana.')
blk=rep(blk,'<h2>Is UPI heading toward card-network pricing?</h2>','<h3>Is UPI heading toward card-network pricing?</h3>')
blk=rep(blk,'<p class="h2sub">Four rows, one question: does a future UPI MDR converge on what Visa, Mastercard and RuPay already charge?</p>\n','')
blk=rep(blk,'<h2>The leverage curve, once more</h2>\n<p class="h2sub">Fee rate &divide; gross margin is the whole model.</p>','<h3>The leverage curve: fee rate &divide; gross margin is the whole model</h3>')
blk=rep(blk,'<h2>Where NPCI says the volume actually is</h2>\n<p class="h2sub">29 published categories, 82% of P2M volume, and groceries lead by a wide margin.</p>','<h3>Where NPCI says the volume actually is</h3>')
blk=rep(blk,'<h2>Food and grocery: the counters most Indians actually stand at</h2>\n<p class="h2sub">Three categories, 43.7% of UPI&rsquo;s P2M transaction count.</p>','<h3>Food and grocery: the counters most Indians actually stand at</h3>')
blk=rep(blk,'<h2>The rest of NPCI\'s top 15</h2>\n<p class="h2sub">Apparel, electronics, liquor, gaming, marketplaces, and bill payments &mdash; six more shapes on the same curve.</p>','<h3>The rest of NPCI&rsquo;s top 15</h3>')
blk=rep(blk,'which is exactly why a flat MDR on these categories would be politically invisible transaction-by-transaction while generating a multi-thousand-crore annual pool in aggregate.',
 'which is exactly why a flat MDR on these categories would be politically invisible transaction-by-transaction while generating a multi-thousand-crore annual pool in aggregate. Under the schedule actually notified, almost none of that pool would exist: at these tickets nearly every food and grocery payment falls under the &#8377;2,000 exemption.')
blk=rep(blk,'If Section 10A&rsquo;s new notification power is ever used, the leverage curve predicts the notification will not be one number: it will be a schedule',
 'The leverage curve predicted that any notification under Section 10A&rsquo;s new power would not be one number but a schedule, and the September 2026 notification was one')
blk=rep(blk,'&mdash; and given that groceries alone out-volumes every other category in NPCI\'s table, any exemption list that omits it would be exempting almost a quarter of UPI\'s entire merchant-payment count.</div>',
 '. Given that groceries alone out-volumes every other category in NPCI\'s table, the &#8377;2,000 ticket threshold, not a category list, is what keeps almost a quarter of UPI\'s merchant-payment count free.</div>')
assert 'companion' not in blk, re.findall(r'.{60}companion.{60}',blk)
assert 'Exhibit 5' not in blk
fig=re.search(r'<figure class="gb-figure".*?</figure>',b,re.S).group(0)
intro=('<h2 id="beyond-the-pump">Beyond the pump</h2>\n<p class="h2sub">The same arithmetic, run across every other counter UPI reaches.</p>\n'
'<p>Fuel is one counter. NPCI&rsquo;s own merchant-category data shows groceries, restaurants and fast food together carry <b>43.7% of UPI&rsquo;s person-to-merchant transaction volume</b>, at a volume-weighted average ticket of <b>&#8377;179</b>. This section runs the leverage arithmetic across them and across the rest of NPCI&rsquo;s published top 15.</p>\n'
'<p>Read it against the schedule that was notified in September and then deferred. Groceries, restaurants and fast food are not in the flat-&#8377;5 list, so they would fall under the general 0.4% rate. But that rate applies only above &#8377;2,000, and at average tickets of &#8377;113 to &#8377;214 most of their payments would pay nothing. Capital-market payments (mutual funds, securities, stockbrokers) were given 0.02%, capped at &#8377;300. The exhibits below price a uniform rate on every ticket: they show the range that was under debate and the relative leverage of each category, not what the notified schedule would collect.</p>\n'
+fig+'\n')
pos='<div class="note"><b>What this article does not establish.</b>'
t=rep(t,pos,intro+blk+pos)

# merged "does not establish" note
t=rep(t,'And which specific outlets host cash-out today &mdash; the source data cannot support that join.</div>',
 'And which specific outlets host cash-out today &mdash; the source data cannot support that join. Beyond fuel: actual merchant margins by category &mdash; NPCI does not publish them, and every non-fuel margin figure above is characterisation by retail-trade convention, flagged as such. Whether July 2025 is representative of a full year &mdash; NPCI&rsquo;s category-level series does not yet run long enough to check for seasonality. And the split between delivery-platform and direct restaurant transactions, which this data cannot separate.</div>')

# sources
t=rep(t,'All computed figures are reproducible from these inputs; the MDR grid is scenario arithmetic, not a forecast.',
 'Merchant-category volumes, values and tickets (Exhibits 8 and 9, and the 29-of-~300 coverage figures) &mdash; NPCI merchant-category classification data for July 2025, decoded and published by SBI Research, &ldquo;New Insights from UPI Data&rdquo; (Issue 20, FY26, <a href="https://sbi.bank.in/documents/13958/14472/New+Insights+from+UPI+Data_SBI+Research.pdf/5e8227bf-78b1-5838-59b5-1ba3e76099b5?t=1755680722524">18 August 2025</a>); NPCI&rsquo;s own merchant-category pages returned an access error on 8 August 2026. Card MDR comparison (Exhibit 6) &mdash; RBI debit-card MDR caps as summarised by Razorpay; RuPay-credit-on-UPI interchange per NPCI&rsquo;s October 2022 circular, effective 1 October 2023, as reported by Terra Insight (the primary circular was not independently verified); credit-card MDR ranges as compiled by Honest Money&rsquo;s 2026 processing-fee comparison. PDS kerosene dealer commission &mdash; PPAC Ready Reckoner FY2025-26 H1. LPG commission and Delhi cylinder price &mdash; this blog&rsquo;s LPG commission piece; November 2026 cylinder prices &mdash; Goodreturns. Category margins other than fuel, kerosene and LPG are stated as retail-trade convention, not measured data. All computed figures are reproducible from these inputs; the MDR grids are scenario arithmetic, not a forecast.')
t=rep(t,'flat &#8377;5 for railways, telecom, insurance, fuel, agri-inputs, utility bills and electricity; effective 15 October 2026) is per',
 'flat &#8377;5 for railways, telecom, insurance, fuel, agri-inputs, utility bills and electricity; 0.02% capped at &#8377;300 for capital markets; originally effective 15 October 2026, deferred on 13 October) is per')

# what would fix this
ul=grab(t,'<h2>What would fix this</h2>\n<ul>','</ul>')+'</ul>'
t=rep(t,ul,'<h2>What would fix this</h2>\n<ul>\n'
'<li><b>NPCI should publish monthly UPI person-to-merchant volume and value for the fuel-retail category</b>, so the digital share of forecourt payments &mdash; which this post found no authoritative source for, forcing a 30&ndash;90% grid &mdash; can be measured directly.</li>\n'
'<li><b>NPCI should publish monthly volume, value and average ticket for every merchant category code it uses, not only the 29 of roughly 300 released so far, in a public month-by-month archive</b>, so fee-pool estimates rest on all categories and a full year rather than a single July 2025 snapshot covering 82 per cent of volume and 52 per cent of value.</li>\n'
'<li><b>The Finance Ministry and NPCI should publish, from the month the MDR starts, the fee actually collected under each tier of the notified schedule</b> &mdash; the 0.4 per cent general rate, the flat ₹5 categories including fuel, and the 0.02 per cent capital-market rate &mdash; so the fee&rsquo;s real incidence by category can be checked against the scenarios debated before it was notified.</li>\n'
'<li><b>The Ministry of Finance should publish, alongside the MDR notification, the share of person-to-merchant UPI volume and value that falls under each exemption</b> &mdash; tickets of ₹2,000 or less and merchants under ₹1 lakh a month &mdash; so the scope of the carve-outs is stated rather than inferred.</li>\n'
'<li><b>NPCI should tag payments routed through delivery platforms and online marketplaces with the underlying merchant&rsquo;s category as well as the platform&rsquo;s</b>, so restaurant, fast-food and marketplace-seller volumes are not undercounted when fee exposure is measured.</li>\n'
'<li><b>PPAC should decompose the dealer commission in its Ready Reckoner price build-up into its cost components, stating whether any allowance for payment-acceptance costs is included</b>, so the question this post could not settle is answered from the formula itself.</li>\n'
'<li><b>IOCL, BPCL and HPCL should publish an outlet-coded list of their retail outlets offering cash withdrawal through Cash@PoS, micro-ATM or UPI-ATM</b>, since only 18 of SBI\'s 693 listed fuel stations could be matched to a specific outlet and cash-out at pumps cannot currently be audited.</li>\n'
'<li><b>The RBI should publish ATM and white-label ATM counts by rural, semi-urban, urban and metropolitan population group every quarter</b>, so the rural share of cash machines is a published number rather than a characterisation of where white-label operators deploy.</li>\n'
'</ul>')
assert B_URL not in t and 'beyond-pump-what-upi' not in t
assert T_URL not in t
open(ROOT+'out/update-2026-11-10-upi-fees-are-now-legal-petrol-pumps.html','w').write(t)
print(len(t))
