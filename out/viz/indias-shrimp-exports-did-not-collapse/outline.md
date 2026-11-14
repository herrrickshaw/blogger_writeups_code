The short version.

- Working from DGCI&S 8-digit export data, FY2017-18 to FY2025-26: 12,698 commodity codes, value and quantity.
- 31.8 per cent of FY2025-26 export value sits on codes absent from FY2017-18. 23.4 per cent of FY2017-18 value sits on codes since retired.
- Smartphones are now India’s single largest export line at $29.4 billion — and the code only begins in FY2022-23.
- Of the six biggest apparent declines, five are recoding. Diesel, aviation fuel, shrimp, basmati and gold jewellery all moved to new codes.
- The one real collapse is cut diamonds: $23.5 bn to $12.1 bn, on a code that ran continuously throughout.
- Of lines that genuinely grew, 84 per cent grew on volume, not price.

## The dataset, and the trap inside it

The Directorate General of Commercial Intelligence and Statistics publishes commodity-wise export data at the 8-digit HS level through the TradeStat EIDB portal, in two forms: value and quantity. Pulled together across the available files, that gives 12,698 codes with value and 12,732 with quantity, covering FY2017-18 to FY2025-26. Total exports rise from $303,526 million to $441,452 million, a gain of 45.4 per cent.
Having both value and quantity on the same code is what makes this data unusually good. You can compute unit realisation — dollars per tonne, per piece, per kilogram — and therefore separate an export that grew because India sold more of something from one that grew because the price went up. Very little Indian trade commentary makes that distinction, because the aggregate data does not support it.
But before any of that is usable there is a problem to deal with, and it is large enough that most 8-digit analysis of Indian trade is probably wrong.

## A third of the book was recoded

The Harmonised System is revised periodically, and India applies national sub-divisions below the international 6-digit level. Over eight years the 8-digit nomenclature has churned substantially. The scale:


[T1 "A third of the book was recoded" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Measure | c1 Value $ million | c2 Share of that year
  r0: FY2025-26 exports on codes absent in FY2017-18 | 140,411 | 31.8%
  r1: FY2017-18 exports on codes since retired | 70,915 | 23.4%
  r2: FY2025-26 total | 441,452 | 100%
  r3: FY2017-18 total | 303,526 | 100%


Retired codes are identified by the asterisk prefix DGCI&S puts on the commodity description. An independent recount confirms the FY2025-26 figure exactly (31.81 per cent) and puts the FY2017-18 figure at 23.11 per cent when retirement is defined by the value series rather than the asterisk — so the 23.4 per cent above is right to within a third of a point, but by a different route than the label suggests. The asterisk is a weak marker: it catches only about a quarter of codes that actually stop trading. Of 662 asterisked codes, 46 still carry some FY2025-26 value — the marker is a strong signal, not an absolute rule, and about $4,271 million of FY2025-26 trade still sits on them during transition.
Nearly a third of what India exported last year is booked under codes that did not exist eight years ago. Any 8-digit series that ignores this is comparing two different nomenclatures and calling the difference growth.

## The five collapses that never happened

Rank every code by the change in its export value between FY2017-18 and FY2025-26, and the biggest falls look alarming. Trace each one and five of the six turn out to be the same product wearing a new number.


[T2 "The five collapses that never happened" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Product | c1 Old code | c2 FY2017-18 $ mn | c3 Old code last live | c4 New code | c5 FY2025-26 $ mn
  r0: Aviation turbine fuel | 27101920 | 6,441 | 25-26 | 27101939 | 8,563
  r1: Diesel | 27101930 | 15,264 | 19-20 | 27101944 | 19,519
  r2: Motor gasoline | 27101219 | 8,339 | 19-20 | 27101241 | 9,474
  r3: Shrimp | 03061790 | 4,575 | 25-26 | 03061720 | 4,052
  r4: Basmati rice | 10063020 | 4,170 | 24-25 | 10063019 | 3,555
  r5: Gold jewellery, unstudded | 71131910 | 5,418 | 22-23 | 71131911 | 4,695


Successor codes are matched here by product description and by the timing of the handover — the old series going to zero in the same year the new one begins. DGCI&S does not publish a concordance table alongside this data, so these pairings are this article’s inference, not an official mapping. The basmati case is the cleanest: the entire rice book was recoded in FY2025-26, with basmati, parboiled and other-than-parboiled all going to zero simultaneously and new codes appearing.
The shrimp example is the most misleading. Code 03061790, “other shrimps and prawns”, falls from $4,575 million to $247 million — a 95 per cent collapse in a flagship agricultural export. What actually happened is that Vannamei shrimp got its own species-specific code, 03061720, which starts in FY2020-21 and carries $4,052 million in FY2025-26. India’s shrimp exports are roughly flat. The line that used to hold them is nearly empty.
The petroleum cases matter for a different reason. Diesel, gasoline and ATF together are around $37.6 billion of FY2025-26 exports across three codes, none of which existed in FY2017-18 in its current form. Any analysis of India’s refined-product export boom built on matched 8-digit codes will simply lose the largest part of it.

Cut diamonds are the one genuine collapse in the data: 23.5 billion dollars of exports in 2017-18, 12.1 billion in 2025-26, on a code that never changed. [Round Brilliant Cut Diamond.jpg](https://commons.wikimedia.org/wiki/File:Round_Brilliant_Cut_Diamond.jpg), Petragems, CC BY-SA 4.0, via Wikimedia Commons.

## The one that is real: cut diamonds

Code 71023910 — cut or otherwise worked non-industrial diamonds — runs continuously across all eight years. There is no successor code, no asterisk, no handover. The decline is the product.


[T3 "The one that is real: cut diamonds" 1 rows; use rows by number in a chart "table" spec]
  cols: c0 Year | c1 FY17-18 $ mn | c2 FY18-19 $ mn | c3 FY19-20 $ mn | c4 FY20-21 $ mn | c5 FY22-23 $ mn | c6 FY23-24 $ mn | c7 FY24-25 $ mn | c8 FY25-26 $ mn
  r0: Cut diamonds (71023910) | 23,511 | 23,769 | 18,609 | 16,534 | 22,027 | 15,941 | 13,264 | 12,113


FY2021-22 is absent from the value files used here and is shown as a gap rather than interpolated.

From $23,511 million to $12,113 million is a fall of 48 per cent, and it is still India’s third-largest single export line. This is the genuine structural story hiding inside a list of fake ones: a sector that was one of India’s largest foreign-exchange earners has roughly halved, on a code stable enough to prove it.

## What the quantity column adds

Restricting to codes that exist in both years with quantity on both sides and at least $1 million of base value leaves 4,958 comparable lines. Of these, 3,139 grew in value. Splitting them by whether the quantity rose or fell:


[T4 "What the quantity column adds" 2 rows; use rows by number in a chart "table" spec]
  cols: c0 Growth type | c1 Lines | c2 Share of growing lines
  r0: Volume-driven — quantity up | 2,633 | 84%
  r1: Price-driven — quantity flat or down, value up | 506 | 16%


Comparable set only, so the petroleum and smartphone lines discussed above are excluded by construction — their codes do not span both years. Quantity units differ by code and are not aggregated; the test is direction of change within each code.
Eighty-four per cent of growing export lines grew because India shipped more, not because the price rose. That is worth stating because the opposite is often assumed — that a weaker rupee or global inflation is doing the work. At the level of individual commodity lines, it is mostly volume.
The price-driven minority is instructive about where India has pricing power. Aluminium ingots grew 4 per cent in value while shipping 24 per cent less metal, a 36 per cent gain in unit realisation. Dredgers rose 141 per cent in value on 17 per cent fewer units. Non-galvanised oil and gas pipe gained 50 per cent per unit. These are lines where India is selling a better or scarcer thing, not simply more of it.

## How concentrated it actually is

The other thing 8-digit data shows that aggregates hide is how few lines matter. Of 11,562 codes carrying export value in FY2025-26:


[T5 "How concentrated it actually is" 8 rows; use rows by number in a chart "table" spec]
  cols: c0 Concentration | c1 Value $ million | c2 Share of exports per cent
  r0: Top 10 codes | 110,263 | 25.0%
  r1: Top 25 codes | 152,819 | 34.6%
  r2: Top 50 codes | 183,624 | 41.6%
  r3: Top 100 codes | 222,528 | 50.4%
  r4: Top 250 codes | 282,636 | 64.0%
  r5: Top 500 codes | 329,486 | 74.6%
  r6: Top 1,000 codes | 375,093 | 85.0%
  r7: All 11,562 live codes | 441,452 | 100.0


One hundred commodity codes carry half of India’s exports. A thousand carry 85 per cent. The remaining ten and a half thousand codes share the last 15 per cent between them.


[T6 "How concentrated it actually is" 10 rows; use rows by number in a chart "table" spec]
  cols: c0 Rank | c1 HS code | c2 Commodity | c3 FY2025-26 $ million | c4 Share per cent
  r0: 1 | 85171300 | Smartphones | 29,363 | 6.7
  r1: 2 | 27101944 | Automotive Diesel Fuel, Not Containing Biodies | 19,519 | 4.4
  r2: 3 | 71023910 | Diamond(Othr Thn Indstrl Diamond)Cut Or Othe | 12,113 | 2.7
  r3: 4 | 30049099 | Other Medcne Put Up For Retail Sale N.E.S | 10,984 | 2.5
  r4: 5 | 27101241 | Motor Gasoline Conforming To Standard Is 2796 | 9,474 | 2.1
  r5: 6 | 27101939 | Aviation Turbine Fuels, Kerosene Type Conformi | 8,563 | 1.9
  r6: 7 | 87032291 | Motor Car Wth Cylndr Cpcty>=1000Cc But < 1 | 5,501 | 1.2
  r7: 8 | 84111200 | Turbo-Jets Of A Thrust>25 Kn | 5,118 | 1.2
  r8: 9 | 27101290 | Others-Of-Light Oils And Preparations: | 4,932 | 1.1
  r9: 10 | 71131911 | Of Gold, Unstudded | 4,695 | 1.1


Smartphones at the top of that list is the single most consequential fact in this dataset, and the code carrying it is four years old.

[chart: 
 
 India's Top 10 Export Codes, FY2025-26 
 $ million, by 8-digit HS code 

 

 Smartphones 
 $29,363M 

 Diesel fuel 
 $19,519M 

 Cut diamonds 
 $12,113M 

 Retail medicine 
 $10,984M 

 Motor gasoline 
 $9,474M 

 Aviation turbine fuel 
 $8,563M 

 Small motor cars 
 $5,501M 

 Turbo-jets >25kN 
 $5,118M 

 Light oils 
 $4,932M 

 Unstudded gold 
 $4,695M 

 Source: DGCI&S TradeStat, 8-digit HS codes, FY2025-26; top 10 codes = 25.0% of all exports 
]

One hundred codes carry half of India's exports; these ten alone carry a quarter.

## The other trap: the unit that changed without telling anyone

Recoding is the visible hazard. There is a second one that leaves no trace in the code list at all, and it is arguably worse because it corrupts the quantity column rather than the value column.

The dataset carries one unit string per code, not one per year. The schema has no year axis on the unit field. So if a commodity’s quantity is reported in tonnes for some years and kilogrammes for others, the file cannot record that, and the label simply says whichever unit was current when the file was generated.

It happens, and it happens on the largest lines in the book. Petroleum crude carries the label KGS across its whole series, and its implied unit value moves from 316.1 to 0.5 US dollars per “kilogramme” between 2020-21 and 2021-22. Half a dollar a kilo is about $500 a tonne, which is roughly $68 a barrel — correct. Three hundred and sixteen dollars a kilogramme is absurd. Back out the quantities and India imported around 196 million tonnes in the first year and 215 million tonnes in the second: the numbers are right and the unit silently changed from tonnes to kilogrammes.


[T7 "The other trap: the unit that changed without telling anyone" 2 rows; use rows by number in a chart "table" spec]
  cols: c0 Where the tonnes-to-kilogrammes break appears | c1 Codes affected | c2 Value on those codes | c3 Share of that book
  r0: Exports (iron ore, petroleum products) | 22 | $92,964 mn | 3.1%
  r1: Imports (crude, coking coal, steam coal) | 42 | $756,498 mn | 14.1%


Detected by testing weight-denominated codes for an implied unit-value jump in the 300× to 3,000× band. Import breaks cluster hard at 2020-21 to 2021-22; export breaks at 2019-20 and 2020-21 to 2022-23. Machinery codes counted in NOS are excluded from the test because a thousand-fold unit-value swing there is a genuine parts-versus-whole-machine effect, not a unit change.

Fourteen per cent of India’s import value sits on codes whose quantity units change mid-series while the unit label insists nothing happened.

The practical rule is short: before computing a unit value across years on any weight-denominated code, test the ratio for a break in that band. The volume-versus-price finding above survives this check — excluding the 50 affected codes leaves the 84 per cent volume share unchanged — but it survives because it was tested, not because the data is clean.

## How to use this data without getting it wrong

- Never match on code alone across a revision. Check whether the description carries the asterisk, and check whether a same-description code appears in the year the old one dies.
- Work at 6-digit or chapter level for long series. The international 6-digit level is far more stable than India’s national 8-digit sub-divisions. Use 8-digit for composition within a year, not for trend across many.
- Use the quantity file. It is published alongside the value file and almost nobody uses it. It is the only way to separate price from volume, and it is the difference between describing a trend and explaining one.
- Test weight-denominated quantities for a unit break before using them. One unit string per code and no year axis means a tonnes-to-kilogrammes switch is unrepresentable and therefore invisible. Run the 300×–3,000× ratio test.

- Treat a 95 per cent collapse as a data question first. Genuine commodity lines rarely fall that far that fast. When one appears to, look for the successor code before writing the story.

## The honest summary

India’s export growth over eight years is real, it is broad, and at the level of individual commodity lines it is overwhelmingly a volume story rather than a price one. Smartphones have become the largest single line, refined petroleum products are a very large second block, and cut diamonds — once the anchor of the export book — have halved.
All four of those statements required handling a nomenclature change that affects roughly a third of the data. The change is not hidden: DGCI&S marks retired codes with an asterisk and publishes the quantity file that makes the volume test possible. It is simply not accounted for in most analysis built on this data, including analysis that reaches confident conclusions about which Indian exports are dying.

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
