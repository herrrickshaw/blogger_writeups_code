# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

## Gemini gemini-flash-latest

**FACTUAL ERRORS:**
- *"Crude | Indian basket — 78.71% Oman+Dubai (sour) + 21.29% Brent"* — The official PPAC (Petroleum Planning & Analysis Cell) composition of the Indian Crude Basket is **75.62% Sour (Oman & Dubai average)** and **24.38% Sweet (Brent)** (effective since April 2019, based on refinery processing data). The 78.71 : 21.29 split is factually incorrect. [confidence: high]
- *"Worked duty stack — Base oil (HSN 2710 1971), CIF ₹100 ... SWS 10% on (BCD+AIDC) = ₹1.00"* — Under Indian Customs Law (CBIC Notification No. 11/2021-Customs), the Agriculture Infrastructure and Development Cess (AIDC) is specifically exempted from the Social Welfare Surcharge (SWS). SWS is calculated as 10% on the Basic Customs Duty (BCD) only (i.e., 10% of ₹5.00 = ₹0.50), not on (BCD + AIDC). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket , floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas."* — Reasoning gap / false claim: Domestic LPG pricing in India is not anchored to the Indian crude basket; it is benchmarked to the Saudi Aramco Contract Price (CP) for Propane and Butane (which the article itself correctly notes in the table immediately above). Concluding that the Indian crude basket anchors LPG is contradictory and unsupported by pricing mechanics. [confidence: high]
- *"Crude, petrol, diesel, ATF & natural gas are outside GST — Central Excise + State VAT/CST apply instead, and their refinery-gate price is set by the Trade Parity formula, not a simple duty add-on."* — Extrapolation / overgeneralization: Trade Parity Pricing (TPP = 80% IPP + 20% EPP) applies exclusively to Motor Spirit (Petrol) and High-Speed Diesel (HSD) pursuant to the 2006 Rangarajan Committee recommendations. It does not apply to Crude (upstream feed), Natural Gas (Administered Price Mechanism / market formulas), or ATF (market-determined / import parity). Applying the TPP formula across all five non-GST hydrocarbons is incorrect. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The claim refers to FY25-26 H1 (first half of fiscal year 2025-26), but the data source (PPAC Ready Reckoner) is provisional and explicitly noted as "FY2025-26 H1" in the caveats. The article does not clarify that this is a half-year figure, which could mislead readers into interpreting it as an annual figure. [confidence: high]

- "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" — The claim states FY25-26 imports as $203.4B, but the caveats note that FY2025-26 data is provisional and based on H1 figures. Using H1 data to project full-year imports without explicit methodology or a clear disclaimer risks overstating the figure. [confidence: high]

INTERPRETATION ERRORS:
- "80 : 20 Trade Parity Price = IPP : EPP weight" — The claim states that the Trade Parity Price (TPP) formula is an 80:20 weight between Import Parity Price (IPP) and Export Parity Price (EPP). However, the article later defines TPP as "TPP = 0.80 × IPP + 0.20 × EPP," which is mathematically correct but does not explain why this specific weight (80:20) is used or whether it is empirically justified. The gap is that the article does not provide evidence or reasoning for why these weights are appropriate or how they were derived, leaving the reader to assume their validity without support. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas." — The claim suggests that the Kirit Parikh 2023 formula for gas pricing is directly tied to the Indian crude basket, implying a single commodity (crude) anchors the pricing of crude, LPG, motor spirit (MS), high-speed diesel (HSD), and gas. However, the article does not explain how the crude basket price translates to gas pricing or provide evidence that the same crude benchmark is used for all these products. The gap is that the claim conflates the pricing mechanisms of different commodities without clarifying the distinct methodologies or benchmarks involved. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
