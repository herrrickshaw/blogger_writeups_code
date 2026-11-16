Revised
15 September 2026
· v1.0.0 · [what changed](#changelog)

12,385listed investment opportunities, 42 sectors

$314.2bnRoads & Highways' headline sector value — the largest disclosed

$81.7bncombined value of the grid's two biggest "projects" — both whole national schemes

22 of 42sectors with no matching central incentive scheme identified

The India Investment Grid — DPIIT and Invest India's public portal, built and run by TCS — is the visible front door to the National Infrastructure Pipeline and PM Gati Shakti: the actual GIS master-plan portal is login-gated to state and ministry users, so this is where an outside investor, or an outside researcher, actually looks. It currently lists 12,385 opportunities across 42 sectors. Read past the headline count, two things stand out: opportunity count and investment size don't move together, and the grid's own published list of "flagship projects" mixes genuinely discrete infrastructure builds with what are, on inspection, entire ongoing government schemes counted as a single line item.

India's new Parliament Building, New Delhi — seat of the central government whose DPIIT/Invest India portal lists the 12,385 opportunities this piece traces. Source: Ministry of Parliamentary Affairs/Press Information Bureau, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:New_Parliament_Building,_New_Delhi.jpg), [GODL-India](https://en.wikipedia.org/wiki/Government_Open_Data_License_%E2%80%93_India).

[chart: 
 
 Opportunity Count Isn't Investment Value 
 The 3 of 42 sectors where the Grid discloses a total dollar value 

 Roads & Highways 
 
 $314.2bn 
 2,306 opportunities — ~$136.3m average per opportunity 

 Waste & Water 
 
 $76.4bn 
 1,020 opportunities — ~$74.9m average per opportunity 

 Healthcare 
 
 $33.0bn 
 1,153 opportunities (more than Waste & Water) — ~$28.6m average 

 Source: India Investment Grid (indiainvestmentgrid.gov.in) sector-level analytics chart, a DPIIT/Invest India portal. 
]

Healthcare has more listed opportunities than Waste & Water, and less than a third of its disclosed value.

## Count isn't value

The portal discloses a total dollar value for only three sectors. Divide that by the sector's own opportunity count and a real gap in project size shows up immediately.


[T1 "Count isn't value" 3 rows; use rows by number in a chart "table" spec]
  cols: c0 Sector | c1 Listed opportunities | c2 Disclosed sector value | c3 Implied average per opportunity
  r0: Roads & Highways | 2,306 | $314.2bn | ~$136.3m
  r1: Waste & Water | 1,020 | $76.4bn | ~$74.9m
  r2: Healthcare | 1,153 | $33.0bn | ~$28.6m


Healthcare has more listed opportunities than Waste & Water, and less than a third of its total disclosed value. A sector's position on an "opportunities" leaderboard, on its own, says almost nothing about how much capital is actually on offer there — and the portal discloses that headline dollar figure for only these three of its 42 sectors, so this comparison is the exception, not something that can be run across the whole list.

## The grid's two biggest "projects" are national schemes

The portal's own flagship-projects list names nine entries. Two of them are not construction projects in any conventional sense — they are entire, ongoing national government schemes, given a single dollar figure and listed as if they were one investable opportunity alongside genuinely discrete builds.


[T2 "The grid's two biggest "projects" are national schemes" 9 rows; use rows by number in a chart "table" spec]
  cols: c0 Listed "project" | c1 Value ($bn) | c2 What it actually is
  r0: Pradhan Mantri Gram Sadak Yojana Project | 46.9 | The entire national rural-roads scheme, not one road
  r1: Jal Jeevan Mission Implementation Project | 34.8 | The entire national rural piped-water-supply mission
  r2: Western Dedicated Freight Corridor | 15.6 | A single, discrete rail freight corridor
  r3: Manufacturing of Passenger Coach Project | 15.3 | A discrete manufacturing programme
  r4: Nagpur–Mumbai Expressway Upgradation | 7.0 | A single, discrete expressway upgrade
  r5: Ganga Expressway Road Construction | 4.6 | A single, discrete expressway build
  r6: Waste Water Management Project | 1.3 | Appears to be a bundled programme, not one plant
  r7: Piped Water Supply Infrastructure Project | 0.9 | Appears to be a bundled programme, not one scheme
  r8: Wardha–Balharshah Quadrupling (135km) | 0.3 | A single, discrete rail-line quadrupling


What this means for the headline numbers. PMGSY and Jal Jeevan Mission alone account for $81.7bn of the flagship list's $126.6bn combined value — roughly 65% of it — and neither is a project an investor could realistically "enter" the way they could bid into the Western DFC or the Ganga Expressway. Whatever the portal's total pipeline value actually is, treating these two entries as comparable line items to the other seven overstates how much of the list is genuinely discrete, investable opportunity versus a restated scheme budget.

## Nearly a quarter of the opportunities sit outside any named incentive scheme

Cross-referencing each of the 42 listed sectors against this ecosystem's own catalogue of central incentive instruments (PLI schemes, PM Gati Shakti funding lines, mission-mode programmes) found a named match for only 20 of them. The other 22 — among them Healthcare, Real Estate, Education, Water Resources, Tourism, BFSI, IT/ITES and Construction — carry no identified central incentive lane at all, despite accounting for 5,088 of the 12,385 listed opportunities (41% of the total). That is not necessarily a gap in government support — some of these sectors may be covered by instruments this cross-reference didn't capture — but it is a real limit on how far "opportunity count" can be read as a proxy for policy backing.

## The net read

None of this means the India Investment Grid is misleading on its own terms — it names its methodology and its sources, and every figure here comes from the portal's own published data. It does mean the single headline number, "12,385 opportunities," is doing a lot of compression: a rural-roads scheme worth tens of billions of dollars, a 135-kilometre rail quadrupling worth a few hundred million, and thousands of listings in sectors with no visible matching incentive scheme are all counted the same way, as one line each.

Sources: this ecosystem's own digital-twin-for-ipa research (layer 26, "project_pipeline," built 2026-09-14), itself sourced to the India Investment Grid (indiainvestmentgrid.gov.in, a DPIIT/Invest India portal built by TCS) — specifically its sector-level opportunity counts and disclosed headline values (scraped from the portal's own analytics chart) and its named flagship-project list with individual project values and IDs. The incentive-scheme cross-reference (the 20-of-42 sectors with a named central instrument) is from the same layer's own mapping against this ecosystem's incentive-scheme catalogue, not an independent audit of every scheme's actual sectoral scope.

Revision history.

- v1.0.0 — 15 September 2026 — first published.

Related on this blog: [India's 14 PLI Schemes, and Every Company Publicly Named as a Winner, 2019–2026](https://blog.vertistratsolution.com/2026/08/nine-ministries-one-list-every-company.html) · [A ₹2,223 Crore Coal-Freight Railway Line Is Being Acquired One Farm Plot at a Time](https://blog.vertistratsolution.com/2026/09/a-2223-crore-coal-freight-railway-line.html) — two more pieces reading an official registry or list literally, rather than taking its headline count at face value.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
