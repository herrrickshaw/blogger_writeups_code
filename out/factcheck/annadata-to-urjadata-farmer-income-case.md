# Fact/interpretation check — annadata-to-urjadata-farmer-income-case

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/annadata-to-urjadata-farmer-income-case.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "FCI rice goes into ethanol at ₹2,320/quintal (₹60.32/litre) — the cheapest of the grain feedstocks, cheaper even than damaged food grains (₹64.00/L) and well below maize (₹66.07/L plus a ₹5.79/L incentive)." — This is an apples-to-oranges comparison that conflates two different stages of the supply chain. ₹2,320/quintal (₹23.20/kg) is the raw feedstock purchase price paid by distillers to FCI to buy rice, whereas ₹60.32/L, ₹64.00/L, and ₹71.86/L are OMC procurement prices paid to distillers for finished ethanol. Raw grain input cost per quintal cannot be directly compared to ethanol output procurement prices per litre. [confidence: high]

- "(a seasonal crop with a hard annual ceiling of roughly 400 crore litres of ethanol capacity, the constraint that kept blending stuck near 1.5% for a decade)" — This is a false causal claim. As stated elsewhere in the article, a 1.5% blending rate in 2013-14 required only ~38 crore litres of ethanol. A sugarcane ethanol capacity ceiling of ~400 crore litres is more than ten times higher than 38 crore litres and could have supported roughly 10% blending at the time. Therefore, the 400 crore litre ceiling could not logically be the constraint that kept blending stuck near 1.5%. [confidence: high]

- "The overcapacity is a margin and utilisation problem for distillers, not a farmer-income problem — yet. Farmers are paid a fixed administered price regardless of how much of the OMCs' total ethanol offer gets absorbed..." — This contains a gap in reasoning. The administered prices set by the government (e.g., ₹60.32–₹71.86/L) are ethanol procurement prices paid by OMCs to distilleries, not direct crop prices paid to farmers at the farm gate. If distilleries operate at low capacity because OMCs absorb only ~60% of the ethanol offered, distilleries reduce their volume purchases of raw grain/maize from farmers. A fixed per-litre ethanol price paid to distillers does not protect farmers from reduced sales volumes when total ethanol demand is capped. [confidence: high]

- "CareEdge Ratings' May 2026 note on the sector puts cumulative CO₂ reduction from capacity expansion at ~8.69 crore tonnes (≈869 lakh MT)" — This is a false causal link. Avoided CO₂ emissions result from blending and burning ethanol in place of fossil petrol in engines, not from the physical construction or expansion of industrial distillery capacity (which itself generates construction emissions). [confidence: medium]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's ethanol blending rate has moved from roughly 1.5% in 2013-14 — stuck there for most of the following decade — to a national average of 20% by the end of 2025" — The article does not provide a source to verify the exact blending rate of 1.5% in 2013-14, and the claim of being "stuck" at this rate for most of the decade is not supported by data. [confidence: medium]
- "The government sets a procurement price per litre for each feedstock category, and Oil Marketing Companies are obligated to buy at that price under long-term offtake agreements" — The article does not provide a primary source to confirm the specifics of the procurement price setting and the terms of the offtake agreements. [confidence: medium]

INTERPRETATION ERRORS:
- "The programme's own pace, checkpointed against an earlier written Lok Sabha reply from the Petroleum Minister (21 August 2025), shows how fast these cumulative numbers have been moving" — The article implies a causal relationship between the programme's pace and the cumulative numbers, but it is unclear if the pace is the primary driver of the changes in the cumulative numbers. [confidence: medium]
- "The result, in CareEdge's words: 'at the current 20% blending level, it will take several years for this surplus capacity to be absorbed'" — The article uses this quote to support the claim that the surplus capacity is a significant problem, but it does not consider alternative scenarios or solutions that could accelerate the absorption of the surplus capacity. [confidence: medium]
