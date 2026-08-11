# Fact/interpretation check — diesel-doesnt-move-cpi-it-moves-40

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/diesel-doesnt-move-cpi-it-moves-40.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Source: WPI — DPIIT/Office of the Economic Adviser, rebased 2022-23 = 100." — India's official Wholesale Price Index (WPI) published by DPIIT uses 2011-12 as its base year; there is no official DPIIT series rebased to 2022-23 = 100. [confidence: high]
- "Pearson correlation of year-on-year growth rates, April anchor, n = 15 years" — Across the 15 fiscal years from FY2012 through FY2026, there are only 14 annual year-on-year growth rate observations (FY13 through FY26), not 15. [confidence: high]

INTERPRETATION ERRORS:
- "Fourteen years of official data do not show that link. [...] The number that would matter is diesel against retail inflation, and it is +0.11 — indistinguishable from noise." — The article uses an unadjusted bivariate correlation of annual growth rates to claim there is no pass-through from diesel to consumer inflation. Simple annual correlation fails to account for short-term/high-frequency pass-through, monetary policy responses, price controls, or confounding macro variables like global crude prices. Inferring a lack of economic transmission from a raw, unadjusted annual correlation is an over-extrapolation. [confidence: high]
- "CNG runs at roughly three-quarters of the diesel cost per kilometre [...] This table is four-wheelers; the recommendation is not. The segments modelled are passenger cars. This article’s conversion case is about heavy and light commercial vehicles, buses and gensets..." — The article relies on passenger car cost-per-kilometre data (Exhibit 5) to justify its recommendation for switching commercial fleets and stationary gensets to CNG. Passenger cars operate on fundamentally different duty cycles, load factors, fuel efficiencies, and pricing structures (retail vs. bulk/cascade) than heavy commercial vehicles or gensets, making this an invalid extrapolation / apples-to-oranges comparison. [confidence: high]
- "Freight indicators are running three to seven times faster than diesel demand" (citing commercial vehicle sales at +5.3% and tractor sales at +11.2% alongside diesel consumption at +1.6%) — Comparing new vehicle and tractor sales growth with diesel consumption growth is an apples-to-oranges comparison between capital stock additions (sales during a period) and operational flow (fuel consumed during that period). Furthermore, tractor sales represent agricultural equipment additions rather than freight movement. [confidence: high]
- "a petrol-to-CNG conversion on the same nameplate vehicle shows a mileage gain ." — Petrol fuel efficiency is measured in kilometres per litre (km/L), whereas CNG efficiency is measured in kilometres per kilogram (km/kg). Because 1 kg of CNG contains significantly more energy than 1 litre of petrol, comparing the raw numerical values directly to assert a physical "mileage gain" is an apples-to-oranges comparison across different units of measurement. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India’s crude import dependency reached 88.2% in FY2024-25" — This claim cannot be verified against available data as of the knowledge cutoff date, and the article does not provide a primary source for this specific figure [confidence: medium]
- "Domestic gas production also fell 0.9% while LNG imports rose 15.4%" — Similar to the previous claim, this figure cannot be verified against available data as of the knowledge cutoff date, and the article does not provide a primary source for this specific figure [confidence: medium]

INTERPRETATION ERRORS:
- "The +0.92 is not evidence of transmission. Diesel sits inside the wholesale index, so the index partly measures diesel by construction. The number that would matter is diesel against retail inflation, and it is +0.11 — indistinguishable from noise." — This statement may be an example of an interpretation error because it dismisses the +0.92 correlation as not being evidence of transmission due to diesel being a component of the wholesale index. However, the article does not fully explore the implications of this correlation or provide alternative explanations for why the +0.11 correlation with retail inflation might be considered "indistinguishable from noise" [confidence: medium]
- "A quarter off the per-kilometre running cost is the switching case, and it does not depend on any claim about inflation or emissions." — This statement assumes that a 25% reduction in running cost is sufficient to make a switching case, but it does not consider other factors that might influence the decision to switch, such as upfront costs, infrastructure availability, or potential emissions benefits [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Revised 6 August 2026 · v2.2.0" — The date is impossible as the current date is before August 2026, making this a clear factual error. [confidence: high]

- "43.3% Diesel’s share of India’s total petroleum product market, May 2026" — The claim lacks a clear definition of "total petroleum product market" (e.g., whether it includes LPG, naphtha, etc.), and no verifiable source is provided to confirm this specific percentage. [confidence: medium]

INTERPRETATION ERRORS:
- "Diesel moves freight; freight moves food; food moves the consumer price index. Therefore holding diesel prices down holds inflation down." — The article correctly notes that the data does not support a link between diesel prices and CPI inflation, yet it still presents this causal chain as a common but untested argument without fully dismantling its underlying logic. The reasoning gap is that the article does not adequately explain why this intuitive chain is flawed beyond citing correlation data. [confidence: high]

- "A diesel-to-CNG shift swaps one import exposure for another, partly rupee-denominated one. It is a better exposure — but it should be argued as a swap, not an escape." — While the claim about import exposure is likely correct, the article does not provide evidence or data to support the assertion that CNG is "a better exposure" compared to diesel. The reasoning gap is the lack of substantiation for the normative judgment about the relative merits of the two exposures. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
