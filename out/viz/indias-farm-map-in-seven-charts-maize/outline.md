+64%Growth in India’s maize area over ten years, to 144 lakh hectares in 2025-26; mustard grew as much

−42%Fall in jowar area over the same decade, the steepest of any major crop

5Crop-mix clusters a k-means analysis finds among India’s states, from the rice east to the dryland west

11.5%Typical monthly price move in the onion-potato-tomato price cluster, against 3.4% for harvest-bunched field crops such as wheat

Three earlier pieces on this site looked at [23 crops ranked by mandi volume and price volatility](https://blog.vertistratsolution.com/2026/10/indias-biggest-mandi-crops-have.html), at [state-wise maize and rice price cycles](https://blog.vertistratsolution.com/2026/10/maize-is-cheapest-in-different-state.html), and at [maize trading by ethanol plants](https://blog.vertistratsolution.com/2026/10/ethanol-plants-that-trade-maize-to.html). This one combines two government sources for a wider picture: what India grows, where, how its yields have moved, and how prices behave once the crop reaches the mandi. It also uses k-means clustering, a standard method that groups items so that those within a group are as alike as possible, to sort states by what they grow and crops by how their prices behave.

How much to trust it. Area, production and yield come from the Department of Agriculture’s Unified Portal for Agricultural Statistics (UPAG): state figures from 1997-98 and all-India figures from 1966-67, with 2025-26 at the third advance estimate. Mandi prices and arrivals come from Agmarknet’s state-wise monthly data, January 2019 to 23 October 2026. Both were pulled from the portals’ public endpoints. The extracts, the code and every table here are published in an open repository, [india-mandi-arrivals](https://github.com/herrrickshaw/india-mandi-arrivals). Ladakh is counted with Jammu & Kashmir on the maps, which use simplified DataMeet boundaries. “Fertility” in the sense of soil nutrients is not covered by these sources; the trends shown are crop yields, the output per hectare that soil fertility, seed and irrigation together produce.

## What India grows: area by crop

All-India area by crop, 2025-26, and change over ten years

[chart: 
 
 Area 2025-26, lakh hectares (change vs 2015-16) 
 Rice 
 
 528 +21% 
 Wheat 
 
 336 +10% 
 Maize 
 
 144 +64% 
 Soybean 
 
 124 +7% 
 Cotton 
 
 115 −6% 
 Gram 
 
 97 +15% 
 Rapeseed & Mustard 
 
 94 +64% 
 Bajra 
 
 70 −2% 
 Moong 
 
 62 +61% 
 Sugarcane 
 
 59 +19% 
 Groundnut 
 
 59 +28% 
 Tur 
 
 45 +13% 
 Jowar 
 
 35 −42% 
 Urad 
 
 32 −13% 
 Lentil 
 
 18 +38% 
 Sesamum 
 
 15 −22% 
]

Lakh hectares, all seasons. Change compares 2025-26 (third advance estimates) with 2015-16. Aggregates such as total food grains are left out. Source: UPAG all-India area, production and yield; this blog’s calculations.

Rice and wheat still take the most land, at 528 and 336 lakh hectares, and rice area grew 21% over the decade. The fastest growth came in crops with new demand or new price support: maize and mustard each grew 64%, moong 61% and lentil 38%. Maize is now the feedstock for much of India’s ethanol, and the government has pushed edible oilseeds and pulses to cut imports. The losers were the traditional dryland cereals and cotton: jowar area fell 42%, the millets group 18% and cotton 6%.

## Yields: what each hectare produces

All-India yield, 1966-67 to 2025-26 (kg per hectare)

[chart: 
 
 
 Rice 
 2025-26: 2,915 kg/ha 
 0 
 1,000 
 2,000 
 3,000 
 1970 
 1990 
 2010 
 
 
 Wheat 
 2025-26: 3,591 kg/ha 
 0 
 1,000 
 2,000 
 3,000 
 1970 
 1990 
 2010 
 
 
 Maize 
 2025-26: 3,824 kg/ha 
 0 
 1,000 
 2,000 
 3,000 
 4,000 
 1970 
 1990 
 2010 
 
 
 Gram 
 2025-26: 1,295 kg/ha 
 0 
 500 
 1,000 
 1970 
 1990 
 2010 
 
 
 Tur 
 2025-26: 805 kg/ha 
 0 
 500 
 1,000 
 1970 
 1990 
 2010 
 
 
 Soybean 
 2025-26: 1,017 kg/ha 
 0 
 500 
 1,000 
 1970 
 1990 
 2010 
 
 
 Mustard 
 2025-26: 1,460 kg/ha 
 0 
 500 
 1,000 
 1,500 
 1970 
 1990 
 2010 
 
 
 Groundnut 
 2025-26: 2,228 kg/ha]

Each panel has its own scale. Cotton yield is lint per hectare. Source: UPAG all-India area, production and yield.


[T1 "Yields: what each hectare produces" 11 rows; use rows by number in a chart "table" spec]
  cols: c0 Crop | c1 Yield 2025-26 (kg/ha) | c2 1970–2000 | c3 2000–2025 | c4 2015–2025
  r0: Maize | 3,824 | 1.9% | 2.7% | 3.5%
  r1: Groundnut | 2,228 | 0.6% | 3.4% | 4.3%
  r2: Moong | 727 | – | 2.7% | 4.2%
  r3: Gram | 1,295 | 0.6% | 1.7% | 3.4%
  r4: Jowar | 1,228 | 1.7% | 1.8% | 4.7%
  r5: Rice | 2,915 | 2.0% | 1.6% | 2.0%
  r6: Wheat | 3,591 | 2.5% | 1.1% | 2.0%
  r7: Mustard | 1,460 | 2.3% | 1.7% | 2.3%
  r8: Soybean | 1,017 | – | 0.4% | 1.2%
  r9: Tur | 805 | -0.1% | 0.7% | 0.8%
  r10: Cotton | 428 | 1.7% | 3.3% | -0.7%


Each rate compares the three-year average around the start year with the latest three years (2023-24 to 2025-26). Moong and soybean series start after 1970. Source: UPAG; this blog’s calculations.

Measured between three-year averages, so that one drought or bumper year does not set the rate, yields of maize, groundnut, moong, gram and jowar have grown 3.4–4.7% a year since 2015. Rice and wheat have grown about 2% a year, slower than wheat’s 2.5% over 1970–2000, the Green Revolution decades. Tur and soybean have barely moved, at about 1% a year, and cotton yield has slipped since the gains of the Bt-cotton years after 2002 levelled off.

## Where each crop is grown

Each state’s share of national production, average of 2023-24 to 2025-26

[chart: 
 
 
 Rice 
 Top: Uttar Pr. 13%, Telangana 12%, 
 West Bengal 11% 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Wheat 
 Top: Uttar Pr. 30%, Madhya Pr. 21%, 
 Punjab 15% 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Maize 
 Top: Madhya Pr. 15%, Karnataka 13%, 
 Bihar 12% 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pulses 
 Top: Madhya Pr. 21%, Maharashtra 18%, 
 Rajasthan 15% 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Oilseeds 
 Top: Rajasthan 23%, Madhya Pr. 20%, 
 Gujar]

Shading is scaled to each crop’s largest producing state. Pulses and oilseeds are the official group totals. Boundaries simplified from DataMeet’s state boundaries; Ladakh is included with Jammu & Kashmir; Andaman & Nicobar and Lakshadweep are omitted. Source: UPAG state-wise area, production and yield.

Wheat is the most concentrated of the six: Uttar Pradesh, Madhya Pradesh and Punjab produce two-thirds of it. Rice is the most spread out, with no state above 13%. Pulses and oilseeds belong to the centre and west, led by Madhya Pradesh for pulses and Rajasthan for oilseeds, and cotton to Maharashtra, Gujarat and Telangana. Maize has moved south and east: Karnataka and Bihar now rank second and third behind Madhya Pradesh.

## Five farming regions, found by k-means

Each state was described by the share of its cropped area under nine crop groups (rice, wheat, maize, millets and sorghum, pulses, oilseeds, cotton, sugarcane, jute and fibres), averaged over the last three crop years. K-means then grouped states with similar mixes. Five groups gave the clearest split: by the silhouette score, a standard check of how well separated the groups are, five scored 0.37 against 0.30 for six. Three groups scored a little higher but merged regions with plainly different farming.

States grouped by crop-area mix (k-means, five clusters)

[chart: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Cluster 1 
 rice 76% + pulses 8% + oilseeds 7% 
 Assam, Chhattisgarh, Kerala, Manipur, 
 Meghalaya, Odisha, Tripura, West Bengal 
 Cluster 2 
 rice 51% + pulses 14% + maize 11% 
 Andhra Pradesh, Arunachal Pradesh, Jharkhand, 
 Nagaland, Tamil Nadu, Telangana 
 Cluster 3 
 oilseeds 24% + pulses 21% + wheat 12% 
 Gujarat, Karnataka, Madhya Pradesh, 
 Maharashtra, Rajasthan 
 Cluster 4 
 wheat 38% + rice 34% + millets & sorghum 6% 
 Bihar, Haryana, Punjab, Uttar Pradesh, 
 Uttarakhand 
 Cluster 5 
 wheat 38% + maize 34% +]

Percentages are each cluster’s average share of cropped area under the crops listed, 2023-24 to 2025-26. Only field crops in UPAG’s area, production and yield series count; plantation crops, fruit and vegetables are not included, which matters most for Kerala and the north-east. Grey: not clustered (too little field-crop area). This blog’s calculation on UPAG data.

The groups follow India’s agro-climatic map closely. The eastern and north-eastern rice belt puts about three-quarters of its field-crop area under rice. The Indo-Gangetic plain, from Punjab to Bihar, splits its land between wheat and rice. The dryland west and centre, from Gujarat and Rajasthan to Karnataka, is the only region where no single crop dominates: oilseeds, pulses, wheat, cotton and millets all hold large shares. The southern and eastern plateau states grow rice alongside pulses and maize, and the Himalayan states pair wheat with maize.

## Urea and yields: checking an earlier finding

An [earlier piece on this site](https://blog.vertistratsolution.com/2026/08/379-kilos-hectare-in-punjab-44-in.html) divided each state’s 2025-26 urea sales, as reported by the Department of Fertilizers, by its cropped area. It found a range from 379 kg a hectare in Punjab to 44 in Kerala, and argued that the pattern follows what each state grows. The k-means clusters above, built only from crop-area data and with no fertiliser figures in them, allow a direct test of that claim. A second test sets the same urea figures against UPAG’s food-grain yields.

Urea per hectare against food-grain yield, 18 states, coloured by crop-mix cluster

[chart: 
 
 0 
 100 
 200 
 300 
 400 
 1,000 
 2,000 
 3,000 
 4,000 
 Urea per hectare of cropped land, 2025-26 (kg) 
 Food-grain yield 2025-26 (kg/ha) 
 
 Punjab 
 
 Haryana 
 
 Bihar 
 
 Andhra Pradesh 
 
 Uttar Pradesh 
 
 Telangana 
 
 Jharkhand 
 
 Tamil Nadu 
 
 Chhattisgarh 
 
 Gujarat 
 
 West Bengal 
 
 Madhya Pradesh 
 
 Karnataka 
 
 Odisha 
 
 Maharashtra 
 
 Assam 
 
 Rajasthan 
 
 Kerala 
 Cluster 1 
 Cluster 2 
 Cluster 3 
 Cluster 4 
 correlation 0.67]

Urea: 2025-26 state sales divided by gross cropped area, from the earlier post (Department of Fertilizers data). Yield: food grains, 2025-26 third advance estimates, UPAG. Clusters as in the map above; Himachal Pradesh and Jammu & Kashmir are not in the urea data.


[T2 "Urea and yields: checking an earlier finding" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Cluster | c1 States in the urea data | c2 Urea (kg/ha) | c3 Food-grain yield (kg/ha) | c4 Food grain per tonne of urea (t)
  r0: 1 Eastern rice belt | Chhattisgarh, West Bengal, Odisha, Assam, Kerala | 124 | 2,640 | 11.7
  r1: 2 Southern rice and mixed | Andhra Pradesh, Telangana, Jharkhand, Tamil Nadu | 242 | 3,046 | 12.2
  r2: 3 Dryland west and centre | Gujarat, Madhya Pradesh, Karnataka, Maharashtra, Rajasthan | 131 | 1,971 | 8.1
  r3: 4 Indo-Gangetic wheat–rice | Punjab, Haryana, Bihar, Uttar Pradesh | 326 | 3,602 | 8.6


The clusters confirm the earlier finding. The Indo-Gangetic wheat–rice cluster uses about 326 kg of urea a hectare, roughly two and a half times the eastern rice belt (124 kg) and the dryland west and centre (131 kg). The southern rice-and-mixed cluster sits in between at 242 kg. Grouping states by crop mix alone reproduces the urea map.

Urea and yield move together, with a correlation of 0.67 across the 18 states: Punjab, Haryana, Andhra Pradesh and Telangana combine high urea use with the highest food-grain yields. But the return on each tonne of urea is lower where use is highest. The Indo-Gangetic states produced about 8.6 tonnes of food grain per tonne of urea sold, against about 12 in the eastern rice belt and the south. That is consistent with diminishing returns to nitrogen in the most heavily fertilised states. The ratio is only a rough guide: urea also goes on sugarcane, cotton, fruit and vegetables, which is why Gujarat and Maharashtra score low. Kerala stands out the other way: its small rice area yields above the national average of 2,646 kg a hectare, while its 44 kg of urea is spread across a cropped area dominated by plantations. Nationally, urea sales rose 10.8% between 2023-24 and 2025-26, while UPAG’s food-grain production rose 13.3%, so recent output growth has not needed proportionally more urea.

## Median mandi prices, last 12 months

The table gives each crop’s median national mandi price over the past twelve months, with its arrivals, its typical monthly move and the months when it is usually cheapest and dearest.


[T3 "Median mandi prices, last 12 months" 23 rows; use rows by number in a chart "table" spec]
  cols: c0 Crop | c1 Median price (Rs/qtl) | c2 Arrivals, last 12 months (million tonnes) | c3 Typical monthly move (%) | c4 Cheapest month | c5 Dearest month
  r0: Paddy | 2,478 | 36.85 | 3.1 | May | Dec
  r1: Wheat | 2,532 | 31.79 | 2.5 | Apr | Dec
  r2: Onion | 1,440 | 17.23 | 13.5 | May | Nov
  r3: Potato | 771 | 16.33 | 6.2 | Feb | Nov
  r4: Maize | 1,803 | 16.15 | 2.9 | Oct | Aug
  r5: Soybean | 5,482 | 5.85 | 2.5 | Oct | Aug
  r6: Tomato | 1,783 | 4.91 | 20.4 | Mar | Jul
  r7: Mustard | 6,737 | 3.77 | 2.3 | Mar | Nov
  r8: Rice | 3,673 | 3.59 | 2.3 | Jan | Aug
  r9: Cotton | 8,021 | 3.45 | 1.8 | Sep | Aug
  r10: Chana | 5,492 | 2.32 | 2.6 | Mar | Sep
  r11: Garlic | 7,138 | 1.75 | 16.0 | Mar | Dec
  r12: Groundnut | 7,176 | 1.74 | 3.1 | Jan | Mar
  r13: Bajra | 2,217 | 1.55 | 3.2 | Sep | Dec
  r14: Tur | 7,478 | 1.39 | 3.4 | Jan | Aug
  r15: Moong | 7,316 | 1.30 | 3.3 | Jul | Apr
  r16: Dry chilli | 18,528 | 1.10 | 5.5 | May | Dec
  r17: Urad | 7,648 | 0.53 | 3.5 | Oct | Apr
  r18: Jeera | 19,900 | 0.50 | 3.8 | Mar | Jul
  r19: Turmeric | 13,550 | 0.48 | 4.2 | Jan | Mar
  r20: Jowar | 3,649 | 0.40 | 6.0 | Oct | Jul
  r21: Masur | 6,909 | 0.32 | 2.2 | Mar | Sep
  r22: Ragi | 3,416 | 0.13 | 2.8 | Apr | Feb


All-India price = arrival-weighted average of state prices; state-months with under 50 tonnes of arrivals are excluded. Cheapest and dearest months from 2019–2025 averages. Source: Agmarknet; this blog’s calculations.

## Price volatility: four kinds of crop

A second k-means run grouped all 217 commodities with at least two years of reliable national prices, from field crops to fruit, vegetables and flowers, by three features of their national mandi price: the typical monthly price move, the gap between the dearest and cheapest month of the year, and how much of a year’s arrivals land in the busiest month.

Crops by price volatility and seasonality, coloured by k-means cluster

[chart: 
 
 2% 
 5% 
 10% 
 20% 
 50% 
 10% 
 30% 
 100% 
 300% 
 1000% 
 Typical monthly price move (log scale) 
 Seasonal spread, dearest vs cheapest month (log) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Apple ]

Each dot is a commodity; the 20 labelled are field crops and a few familiar fruits and vegetables. Both axes are log scales. Typical monthly move: median absolute month-on-month change in the all-India price, January 2023 to October 2026. Seasonal spread: dearest calendar month over cheapest, 2019 to 2025 averages. Source: Agmarknet; this blog’s calculations.

The four groups separate cleanly. Harvest-bunched field crops (46 commodities, including wheat, paddy, maize, soybean, mustard, cotton, pulses and the spices) move 3.4% in a typical month and swing 18% between their cheapest and dearest months, but receive about 21% of a year’s arrivals in their busiest month: the harvest glut, absorbed by storage and government purchases. Steady crops (44, including rice, moong, jowar and coconut) move about as little, 3.5%, and arrive evenly through the year, with 12% in the peak month. Volatile vegetables (85, led by onion, potato, tomato, garlic and cauliflower, with banana) move 11.5% a month and swing 73% across the year. Very volatile perishables (42, mostly leafy greens, herbs, flowers and seasonal fruit such as mango) move 17.8% a month, with seasonal swings of about 201%.

Storability explains much of the split. The calm groups are dominated by grains, pulses, oilseeds and spices that can be dried and held for months, although the steady group also contains a few perishables traded evenly all year, such as coconut, papaya and green banana. The two volatile groups are almost entirely produce that lasts days or weeks.

## Seasonality: when each crop is cheap and dear

All-India seasonal price index by crop, 2019–2025 (1.00 = the crop’s average month)

[chart: 
 
 Jan 
 Feb 
 Mar 
 Apr 
 May 
 Jun 
 Jul 
 Aug 
 Sep 
 Oct 
 Nov 
 Dec 
 Onion 
 
 1.06 
 
 0.94 
 
 0.72 
 
 0.59 
 
 0.58 
 
 0.73 
 
 0.81 
 
 0.92 
 
 1.16 
 
 1.44 
 
 1.60 
 
 1.45 
 Tomato 
 
 0.69 
 
 0.64 
 
 0.62 
 
 0.65 
 
 0.76 
 
 1.11 
 
 1.66 
 
 1.21 
 
 1.03 
 
 1.27 
 
 1.26 
 
 1.10 
 Potato 
 
 0.77 
 
 0.66 
 
 0.75 
 
 0.87 
 
 0.96 
 
 1.03 
 
 1.12 
 
 1.14 
 
 1.15 
 
 1.21 
 
 1.31 
 
 1.04 
 Garlic 
 
 1.13 
 
 0.91 
 
 0.70 
 
 0.77 
 
 0.83 
 
 0.87 
 
 0.97 
 
 1.07 
 
 1.09 
 
 1.12 
 
 1.22 
 
 1.32 
 Turmeric 
 
 0.89 
 
 1.11 
 
 1.26 
 
 1.07 
 
 0.94 
 
]

Average arrival-weighted national price in each calendar month divided by the average of all months. Crops are ordered by seasonal spread. Source: Agmarknet; this blog’s calculations.

The vegetables carry the largest seasonal swings. Onion is cheapest in April and May, at about 0.58 of its average, after the rabi harvest, and dearest in November, at 1.60, before the next crop arrives in volume. Tomato is cheapest from February to April and peaks in July, at 1.66, during the monsoon. Potato is cheapest in February, around harvest, and dearest in November, late in the storage season. Among field crops the pattern is gentler: wheat is cheapest in April and May at harvest and about 5% dearer in November and December; paddy runs from 0.92 in May to 1.09 in December. Turmeric, a spice, peaks sharply in March, at 1.26, before its new crop is traded.

## What it adds up to

India’s farm map is shifting toward the crops that policy and new industries reward. Maize, mustard and moong have expanded fastest, and their yields are rising faster than those of rice and wheat. Prices sort crops into two worlds. Grains, pulses and oilseeds, which store well and many of which the government buys at a support price, move a few percent a month. Vegetables, which cannot be stored for long, can double or halve in price within a season. The open repository behind this piece holds the data and code for anyone who wants to test these patterns for a particular crop, state or year.

Sources and method. UPAG ([upag.gov.in](https://upag.gov.in/)), Department of Agriculture & Farmers Welfare: state-wise and all-India area, production and yield, retrieved through the portal’s public report service. Agmarknet ([agmarknet.gov.in](https://agmarknet.gov.in/)): state-wise monthly weighted-average prices and arrivals. State boundaries: [DataMeet](https://github.com/datameet/maps), simplified. K-means: Lloyd’s algorithm with 50 k-means++ starts. States were clustered on crop-area shares; crops on the logarithms of the three price features, standardised. Cluster count chosen with the silhouette score. All data, code and outputs: [github.com/herrrickshaw/india-mandi-arrivals](https://github.com/herrrickshaw/india-mandi-arrivals). This post is AI-assisted analysis of public data, not investment advice.
