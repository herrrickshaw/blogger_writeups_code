# Fact/interpretation check — 379-kilos-hectare-in-punjab-44-in

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/379-kilos-hectare-in-punjab-44-in.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "FOM | Nutrient content | Must clear 5% total NPK by weight" (and the accompanying claim: "FOM has to clear only 5 per cent total NPK, so on any nutrient-for-nutrient basis it is an order of magnitude more expensive.") — This directly contradicts the notified Schedule VIII specifications detailed earlier in the article, which correctly state that the March 2025 amendment removed the 5% NPK minimum entirely and established a carbon-and-safety standard with no minimum NPK requirement. [confidence: high]

INTERPRETATION ERRORS:
- "Punjab is applying 379 kg per cropped hectare and Haryana 333 — and because gross cropped area already counts the second crop separately, those are per-crop-season figures, not annual totals across a double crop." — The author compares this 379 kg/ha statewide aggregate directly against ICAR's single-crop kharif rice recommendation (130 kg urea/ha) to assert massive over-application on paddy. Dividing total annual state urea sales by Gross Cropped Area produces a blanket average across all seasons and diverse crops (including high-nitrogen crops like sugarcane, potatoes, and wheat), plus non-agricultural diversion and buffer stock; attributing this state-level average directly as the per-season application rate for individual paddy crops is an ecological fallacy. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India sold 396.6 lakh tonnes of urea in 2025-26" — The article cites Department of Fertilizers data showing urea sales of 357.81 lakh tonnes in 2023-24, 387.92 in 2024-25, and 396.60 in 2025-26. However, the initial sentence claims "India sold 396.6 lakh tonnes of urea in 2025-26," which is correct, but the subsequent sentence states "India moved 357.81 lakh tonnes in 2023-24, 387.92 in 2024-25 and 396.60 in 2025-26," which is inconsistent in phrasing ("moved" vs. "sold") and could cause confusion. The figures themselves are consistent with the Department of Fertilizers data. [confidence: high]

- "The Economic Survey 2025-26 tracks the applied ratio from 4:3.2:1 in 2009-10, close to the benchmark, to 7:2.8:1 by 2019-20 and about 10.9:4.1:1 by 2023-24" — The article cites the Economic Survey 2025-26 for these ratios, but the ratios appear to be inconsistent with the standard NPK ratio format (where the first number represents nitrogen, the second phosphorus, and the third potassium). The ratio 10.9:4.1:1 suggests an extremely high nitrogen application relative to potassium, which is plausible but should be double-checked against the original Economic Survey document. [confidence: medium]

INTERPRETATION ERRORS:
- "The states above the line share a cropping pattern rather than a geography. Punjab, Haryana and western Uttar Pradesh run irrigated wheat-paddy rotations; Bihar runs paddy-wheat-maize; coastal Andhra Pradesh and Telangana run paddy and maize. Every one of those is a cereal system, and cereals are where nitrogen goes." — The claim correctly identifies that cereal crops (paddy, wheat, maize) are major nitrogen consumers, but it implies that all nitrogen use is driven solely by crop type, ignoring other factors such as soil fertility, irrigation, and farmer practices. The reasoning gap is that the statement oversimplifies the drivers of nitrogen application by attributing it entirely to crop choice, without acknowledging that even within the same crop, nitrogen use can vary significantly based on soil conditions and agronomic practices. [confidence: high]

- "Substituting a quarter of the nitrogen on Punjab’s 379 kg of urea a hectare still leaves it near 285 — well above the recommended dose for either crop in its rotation." — The claim assumes that substituting 25% of chemical nitrogen with organic manure (FOM/LFOM) would reduce total nitrogen application to 285 kg/ha, but this is an oversimplification. The reasoning gap is that the substitution rate of 25% is based on yield benefits and partial nutrient replacement claims, not on a direct 1:1 reduction in nitrogen application. Organic manure also contributes some nitrogen, but its availability and mineralization rates are slower, meaning the actual reduction in nitrogen applied may not be proportional to the substitution claim. The article does not provide evidence that a 25% substitution translates directly to a 25% reduction in urea application. [confidence: high]
