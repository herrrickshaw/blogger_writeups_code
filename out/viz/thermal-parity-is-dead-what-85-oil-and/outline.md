Published 8 August 2026 · v1.0.0 · PPAC Indian crude basket and domestic gas price notifications, August 2026 · EIA Henry Hub spot, 6 August 2026

India's domestic natural-gas infrastructure, like this ONGC gas-fired power plant in Tripura, sits behind the administered pricing formula this piece examines. [PM Modi at the dedication of Unit-II of ONGC Tripura Company Ltd Power Plant](https://commons.wikimedia.org/wiki/File:PM_Modi_at_the_dedication_of_Unit-II_of_ONGC_Tripura_Company_Ltd_Power_Plant.jpg), Prime Minister's Office, Government of India, CC BY-SA 2.0, via Wikimedia Commons.

5.55MMBtu of energy in one barrel of crude — the thermal-parity anchor

10.8×1India’s actual oil-to-gas price ratio today, at the notified APM price

32×1The same ratio against US Henry Hub gas — more than five times thermal parity

$7.86PPAC’s notified domestic gas (formula) price, $/MMBtu, Aug 2026, against $85 crude; the binding APM ceiling is $7.00

[kept verbatim: dated update notes]

## The number nobody quotes

Thermal parity, in one calculation.

A barrel of crude oil contains about 5.55 million British thermal units — the conversion this article uses throughout, taken from a peer-reviewed treatment of the oil-gas relationship. If oil and gas priced purely on heat content, one MMBtu of gas would cost 1/5.55th of a barrel of oil, and the oil-to-gas price ratio, expressed in dollars per barrel against dollars per MMBtu, would sit at roughly 5.55:1. That is thermal parity. Nothing about it is a market outcome — it is physics, not economics, and the entire literature on oil-gas “decoupling” is the story of markets refusing to price that way.

Exhibit 1

Where today’s prices actually sit against thermal parity

Oil-to-gas ratio = crude price, $/bbl ÷ gas price, $/MMBtu. Thermal parity = 5.55:1. Industry’s informal “rule of thumb” = 10:1.


[T1 "The number nobody quotes" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Benchmark pair | c1 Crude, $/bbl | c2 Gas, $/MMBtu | c3 Ratio | c4 × thermal parity
  r0: Thermal parity (physics) | — | — | 5.55:1 | 1.0×
  r1: Industry rule of thumb | — | — | 10:1 | 1.8×
  r2: Indian crude basket vs India’s notified APM gas price | 85.2 | 7.86 | 10.8:1 | 2.0×
  r3: Indian crude basket vs US Henry Hub spot | 85.2 | 2.64 | 32.3:1 | 5.8×


Indian crude basket, $85.2/bbl, 4 August 2026 — PPAC. Henry Hub spot, $2.64/MMBtu, 6 August 2026 — US EIA/FRED series DHHNGSP. India’s notified domestic natural gas (APM) price, $7.86/MMBtu — PPAC, “Domestic Natural Gas Price for the period 1st August 2026 to 31st August 2026,” Gross GCV basis, read directly from ppac.gov.in. Barrel-to-MMBtu conversion (5.55) from Mittal (2016), “Pricing Relationship Between Oil and Natural Gas,” Business Analyst 36(2). The Indian-crude-vs-Henry-Hub row compares two different geographies’ benchmarks and is illustrative of scale, not a claim that Indian crude and US gas trade in the same market.

Reading Exhibit 1 honestly. Both real-world rows sit well above thermal parity, and the gap is not new. What is new is which benchmark is closer: India’s own APM-priced gas, formula-linked to crude by government notification, sits at roughly 2.0× thermal parity — almost exactly the informal “10:1” the industry has used as a rule of thumb since long before this pricing formula existed. Unregulated US gas, by contrast, sits at nearly 6× thermal parity. That is not a coincidence of geography; it is two different pricing regimes, one of them mechanically tied to oil and one of them not.

## What the literature actually found

A cointegrated relationship that broke, and never came back.

The idea that gas “should” track oil is old and, for decades, was largely true. Long-term LNG and pipeline gas contracts across Europe and Asia were built explicitly on oil-indexed formulas — a 2006 industry-institute review describes contract prices computed on a net-back basis from the average price of competing petroleum products, with clauses like P = Po + A×(G–Go) + B×(F–Fo) tying the monthly gas price directly to heating-oil and heavy-fuel benchmarks. That structure existed to protect long-lived pipeline and LNG infrastructure investment: indexing gas to oil guaranteed a market-competitive price without a standalone gas market to reference.

Deregulation broke that logic first in the United States, then, more slowly, in Europe. A 2015 empirical study using daily NYMEX spot data from January 2006 to December 2014 tested exactly this question with cointegration analysis — the formal statistical test for whether two price series share a genuine long-run equilibrium rather than just moving together by coincidence. Its finding: the correlation between crude oil and natural gas prices was strongly positive before the 2008 financial crisis (+0.72), moderately positive during it (+0.58), and had turned negative afterward (−0.17). The Johansen cointegration test could not reject the null of no long-run relationship in the full sample, the pre-crisis, during-crisis or post-crisis periods — formal confirmation that whatever equilibrium once tied the two series together, it had come apart. The paper attributes this to the shale gas supply surge in North America, which expanded gas supply without a matched increase in oil-linked demand for it.

Exhibit 2

Oil-gas correlation, before and after the break

Pearson correlation coefficient, NYMEX daily spot prices, January 2006–December 2014.


[T2 "What the literature actually found" 3 rows; use rows by number in a chart "table" spec]
  cols: c0 Period | c1 Dates | c2 Correlation
  r0: Pre-crisis | Jan 2006–Sep 2008 | +0.72
  r1: During crisis | Sep 2008–Apr 2009 | +0.58
  r2: Post-crisis | May 2009–Dec 2014 | −0.17


Mittal (2016), Table 3, using NYMEX spot data retrieved from investing.com; structural break dates identified via Augmented Dickey-Fuller breakpoint selection (crude: 22 Sep 2008; natural gas: 29 Sep 2009). Reproduced as reported; this article did not re-run the underlying econometrics.

An independent industry review from 2005–06, written before this decoupling was fully visible, had already flagged the mechanism that would drive it: on deregulated markets, gas prices are “influenced directly by using formulas based on the price of petroleum products, or indirectly” through fuel-switching — utilities substituting toward coal or heavy fuel oil when gas gets too expensive relative to them, and back again when it gets cheap. That substitution channel is a soft, indirect tether, not a formula, and it is exactly the kind of link that a genuine supply glut — shale gas, in this case — can overwhelm. The 2015 cointegration study’s empirical finding is the after-the-fact confirmation of what the 2006 review predicted was possible.

## India’s counter-example: a formula that re-couples on purpose

The Kirit Parikh mechanism ties domestic gas to crude by law, not by market forces.

India’s domestic natural gas pricing does not participate in the decoupling described above, because it was not designed to be market-discovered in the first place. Since April 2023, following the Kirit Parikh Committee’s recommendations, the price of gas from ONGC and Oil India’s nomination fields has been set monthly at 10% of the average Indian crude basket price in dollars per barrel, converted to dollars per MMBtu — with a floor and a ceiling. The floor was set at $4/MMBtu, and the ceiling has stepped up in stages since the formula's introduction. PPAC's own August 2026 notification puts the actual domestic natural gas price at $7.86/MMBtu (Gross GCV basis) for the month. Gas from more difficult fields — deepwater, ultra-deepwater and high-pressure-high-temperature blocks — carries its own, separate ceiling, published by PPAC as $8.90/MMBtu for the period 1 April to 30 September 2026.

What the formula actually does. At the Indian crude basket’s recent average of roughly $84–85/bbl, 10% works out to a raw formula output of $8.4–8.5/MMBtu. The notified price of $7.86/MMBtu sits below that, which is consistent with the ceiling still constraining the raw 10% output, though this article could not locate PPAC's precise nomination-field ceiling figure for August 2026 as a standalone published number distinct from the $8.90 difficult-fields ceiling — the $7.86 is read here as the notified, binding price for nomination-field gas, whatever the exact mechanics behind it. Either way, India’s domestic gas price is not floating freely at 10% of crude; something is holding it below the formula's raw output, and that something is a policy choice to protect city-gas and fertiliser consumers from a full pass-through of crude-linked pricing, layered on top of a formula that already ties the two together by design.

## What would actually decouple the two, on purpose

The question this article was asked to answer.

Decoupling India’s domestic gas price from crude oil, as a policy matter rather than a market outcome, would mean replacing the Parikh formula’s crude-basket input with a gas-specific reference — the same shift the international literature above describes as having already happened, unplanned, in the United States after 2009. Three routes exist, and each has a real cost this blog has not previously quantified:

- Index to a domestic or regional gas hub instead of crude. India does not yet have a liquid, transparent domestic gas trading hub of the depth needed to serve as a pricing reference — IGX (Indian Gas Exchange) exists but trades a fraction of the volume a benchmark would need. Until that liquidity exists, any hub-indexed formula risks being thin and manipulable, which is precisely the objection long-term oil-indexed contracts were originally designed to avoid, per the 2006 review above.

- Import an external gas benchmark (Henry Hub, JKM, TTF) instead of a crude basket. This would sever the mechanical 10%-of-crude linkage immediately, but would import US or Asian gas-market volatility — including the shale-driven price collapses the literature documents — directly into Indian producer economics, with no guarantee that a foreign gas benchmark tracks Indian supply-cost realities any better than crude currently does.

- Leave the ceiling as the de facto decoupling mechanism. Because the $7 ceiling is currently binding below the formula’s raw 10%-of-crude output, India’s gas price is already partially decoupled from crude in practice, just not by formula — a rising crude price stops passing through once the ceiling binds, exactly the kind of administrative cap this blog has documented elsewhere for fuel and LPG. A crude price fall, symmetrically, would flow straight through to the 10% calculation until it hits the $4 floor.

[kept verbatim, collapsed: What this piece could not establish]

Related on this blog — fertilisers. [India's Fertiliser Import Bill Hits $18 Billion](https://blog.vertistratsolution.com/2026/08/indias-fertiliser-import-bill-hits-18.html) · [Nature Versus Nurture: India's Fertiliser-Fed Food Security](https://blog.vertistratsolution.com/2026/08/nature-versus-nurture-indias-fertiliser.html) · [Bio-Fertiliser and Green Credits: Regrowing India's Arid Land](https://blog.vertistratsolution.com/2026/08/bio-fertiliser-and-green-credits.html) · [India's Subsidised Imports — Fertilisers Explode +76% (FY25 vs FY26)](https://blog.vertistratsolution.com/2026/07/indias-subsidised-imports-fertilisers.html) · [Imported Fertiliser & Fuel Prices → Diesel → CPI/WPI](https://blog.vertistratsolution.com/2026/08/imported-fertiliser-fuel-prices-diesel.html).
Related — gas & LPG. [City Gas Just Became India's Largest Gas Consumer](https://blog.vertistratsolution.com/2026/08/city-gas-just-became-indias-largest-gas.html) · [LPG's Missing Number](https://blog.vertistratsolution.com/2026/08/lpgs-missing-number-7308-commission-and.html) · [Europe Bought a Record Amount of LNG](https://blog.vertistratsolution.com/2026/08/europe-bought-record-amount-of-lng-and.html) · [The CBG Incentive Stack](https://blog.vertistratsolution.com/2026/07/the-cbg-incentive-stack-every-leg-of.html).

Sources. Update of 7 November 2026: APM ceiling of $7.00/MMBtu from April 2026 and April domestic price of $10.76 — [Free Press Journal](https://www.freepressjournal.in/business/govt-raises-apm-gas-price-to-usd-7mmbtu-for-ongc-oil-india); September 2026 Indian basket average — [ThePrint](https://theprint.in/economy/indias-crude-import-bill-jumps-46-to-90-6-billion-in-april-september-as-oil-prices-surge/3074774/), citing PPAC. Thermal-parity conversion (1 barrel crude = 5.55 MMBtu) and the cointegration/correlation findings in Exhibit 2 — Arjun Mittal, “Pricing Relationship Between Oil and Natural Gas,” Business Analyst (The Indian Journal of Industrial Relations), Vol. 36 No. 2, October 2015–March 2016, pp. 185–197, using NYMEX spot data January 2006–December 2014. Oil-indexed contract structure and formulas — Guy Maisonnier, “The Ties between Natural Gas and Oil Prices,” IFP Panorama 2006 (text finalised November 2005). Indian crude basket price, $85.2/bbl (4 August 2026) and July 2026 range/average — PPAC, Crude Oil FOB Price (Indian Basket), and press aggregation of the same series. India’s APM gas pricing formula and floor structure — reporting on the Kirit Parikh Committee recommendations (accepted April 2023) via Business Standard, Angel One and IAS Express explainer coverage. Current notified domestic natural gas price, $7.86/MMBtu for August 2026, and the $8.90/MMBtu ceiling for deepwater/ultra-deepwater/HPHT fields for April–September 2026 — read directly from PPAC's website (ppac.gov.in), correcting an earlier version of this article that relied on secondary reporting citing a stale $7/MMBtu and $9.72/MMBtu. Henry Hub spot price, $2.64/MMBtu (6 August 2026) — US Energy Information Administration, series DHHNGSP via FRED. General gas-contract pricing concepts (energy-equivalence billing, hub-based vs oil-indexed contracts) — natgas.info, “Gas Pricing & Contracts.” India-specific macro context on crude-price pass-through to domestic gas and OMC finances — ICRA-Petrofed, Impact of Soft Global Crude Oil Prices on Indian Oil & Gas Industry (2016), used here only for historical/structural background, not as a source of any current-year figure.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
