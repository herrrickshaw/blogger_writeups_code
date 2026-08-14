# Fact/interpretation check — fuel-pricing-to-crude-cost

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fuel-pricing-to-crude-cost.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Punjab | Jalandhar" and "Haryana | Ambala" in Section 4's table of state capitals — The capital of both Punjab and Haryana is Chandigarh, not Jalandhar or Ambala. [confidence: high]
- "All 35 state capitals" / "across all 35 state capitals" — India consists of 28 states and 8 Union Territories (36 entities total). The list conflates states and UTs while omitting the Union Territory of Lakshadweep. [confidence: high]

INTERPRETATION ERRORS:
- "That spare capacity means blending can be pushed harder during a crude shock without waiting on new plants; the real limit is feedstock supply... competing with food-security demand for the same grain, not distillery capacity itself." — The reasoning overlooks vehicle fleet compatibility and regulatory standards. Most legacy vehicles on Indian roads are engineered for E10 or E20; pushing blend rates higher (such as E25 or E35) causes engine degradation, fuel system corrosion, and warranty invalidation unless the automotive fleet itself is adapted, making vehicle tolerance and fuel specifications a binding constraint alongside feedstock supply. [confidence: high]
- "That is the structural reason India's petrochemical import bill is far more exposed to a crude/rupee swing than the pump price is: fuel pricing has a flat-rate excise shock absorber built in; ad-valorem GST-rated chemical imports do not." — This makes an apples-to-oranges comparison between final retail consumer pricing and intermediate industrial imports. Integrated GST (IGST) paid on petrochemical feedstock imports is an Input Tax Credit (ITC) available for offset downstream, meaning it does not act as an unbuffered cumulative cost in the same manner as non-creditable retail fuel taxes. [confidence: medium]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The Indian basket crude ($/bbl) ... +12.0% vs PPAC's last published Jul–Sep 2025 average" — The article does not provide a clear source for the "+12.0% vs PPAC's last published Jul–Sep 2025 average" claim, but according to the text, the calculation is based on the implied Indian basket of $78.30/bbl and the PPAC's published Jul–Sep 2025 quarterly average of $69.89/bbl. The percentage increase is calculated correctly as ((78.30-69.89)/69.89)*100 = 12.06%, which rounds to 12.0%. However, without access to the original PPAC data, it's difficult to verify the accuracy of the $69.89/bbl figure. [confidence: medium]
- "Naphtha and other petrochemical feedstocks ... are priced and taxed under GST" — This claim may not be entirely accurate, as some petrochemical feedstocks might be exempt from GST or have different tax treatments. However, without more specific information, it's challenging to verify the accuracy of this statement. [confidence: low]

INTERPRETATION ERRORS:
- "A 97% swing in crude (past-year low to high) would, on a naive full pass-through, move Delhi petrol by ≈43% (₹87.65 to ₹125.71) — a smaller swing than crude's own, because the flat-rate excise and commission layers don't move at all, and only the dealer-price and VAT layers scale" — The article correctly notes that the flat-rate excise and commission layers do not move with crude prices. However, it implies that the VAT layer scales directly with crude prices, which might not be the case. The VAT rate is a percentage of the retail selling price, which includes the dealer price, excise duty, and commission. The article does not provide a clear explanation of how the VAT layer scales with crude prices, which could lead to an incorrect interpretation of the relationship between crude price swings and retail price movements. [confidence: medium]
- "The scenario range makes the excise lever visible: ... government has repeatedly cut excise duty when crude spiked (and raised it when crude fell) specifically to smooth this pass-through — a policy choice this build-up deliberately does not model, so as to isolate what the tax structure alone would do" — The article acknowledges that the government has used excise duty as a policy tool to smooth the pass-through of crude price changes. However, by not modeling this policy choice, the article may be overestimating the impact of crude price swings on retail prices. This could lead to an incorrect interpretation of the effectiveness of the tax structure in isolating the impact of crude price changes. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Energy pricing · Crude oil · 5 August 2026" — The article is dated 5 August 2026, but the PPAC Ready Reckoner cited (FY2025-26 H1 edition) is based on data as of 01.10.2025, which is in the past relative to the publication date. This creates a temporal inconsistency where the article claims to use "live" data but relies on outdated PPAC tables. [confidence: high]

- "$78.87/bbl Brent Crude, live (OilPriceAPI & Rigzone agree to 2¢)" — The article later notes a data-quality issue where OilPriceAPI's "BRENT_SPOT_USD" field shows $91.82, conflicting with the $78.87 figure. While the article acknowledges this discrepancy, it does not correct the initial claim of agreement to 2¢, which is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "Because none of these four components [of excise duty] move with crude, they are the lever government has historically pulled to cushion pump prices when crude spikes, and the reason the 'full pass-through' scenarios below likely overstate how much of a crude rally would actually reach the pump." — The article correctly notes that excise duties are fixed and do not move with crude, but it then implies that this alone explains why "full pass-through" scenarios overstate pump price increases. This ignores other policy tools (e.g., state VAT adjustments, dealer commission changes, or direct subsidies) that governments may use to cushion prices, as well as the fact that the scenarios explicitly hold excise, commission, and VAT constant. The conclusion conflates the tax structure's mechanical effect with actual policy responses. [confidence: high]

- "Capacity is not the constraint. India's installed ethanol distillery capacity is roughly 2,000 crore litres for ESY2025-26 (CareEdge estimate), against 904.8 crore litres actually drawn by PSU OMCs in ESY2024-25 (PPAC Table 6.10) — about 1,095 crore litres of spare, already-built capacity sitting unused." — While the capacity figures may be correct, the claim that "capacity is not the constraint" is an overgeneralization. The article later acknowledges that feedstock supply (e.g., maize) is the real limiting factor, but the initial statement ignores logistical, regulatory, and seasonal constraints on ethanol production and blending. The claim conflates installed capacity with operational feasibility. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
