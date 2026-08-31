# Fact/interpretation check — inside-refinery-how-hydrogen-cleans

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/inside-refinery-how-hydrogen-cleans.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's Bharat Stage VI standard, equivalent to Euro 6, caps diesel sulphur at 10 parts per million — down from 50 ppm under the outgoing BS-IV standard — and took effect nationwide on 1 April 2020." — The Bharat Stage VI (BS-VI) standard for diesel sulphur was indeed set at 10 ppm, but it replaced BS-IV (which had a 50 ppm limit) in April 2020. However, BS-VI was introduced in two phases: BS-IV was replaced by BS-VI in April 2020 for new vehicles, but the nationwide rollout for all vehicles and fuels was completed by April 2022. The claim incorrectly states the nationwide implementation date as April 2020. [confidence: high]

- "The green bid price sits roughly 1.7 to 3.2 times above grey hydrogen depending which grey benchmark is used — global natural-gas SMR pricing at the low end, India's own higher domestic grey-hydrogen cost estimate at the high end." — The article cites a green hydrogen bid price of ₹397/kg (≈$4.16/kg) and compares it to grey hydrogen costs of $1.3–1.5/kg (global) and ₹150–200/kg (India). However, ₹150–200/kg translates to roughly $1.8–2.4/kg (assuming ₹94.3/$), which is only about 1.2–1.6 times the global grey benchmark, not 1.7–3.2 times. The upper end of the ratio (3.2x) appears inflated. [confidence: high]

INTERPRETATION ERRORS:
- "The transition is not simply a matter of swapping one hydrogen source for another at the plant gate. An industry technical overview of refinery hydrogen systems notes that existing refinery infrastructure is 'optimised around the predictable operating characteristics of reformers,' prioritising stability and availability, while electrolysers introduce short-term output variability — tied to when renewable power is actually available — that refinery hydrogen systems were never designed to absorb." — While the claim about variability is correct, the article does not address whether refineries could mitigate this through energy storage, grid management, or hybrid systems (e.g., blending green hydrogen with grey hydrogen). The implication that electrolysers cannot be integrated without major disruptions is an overgeneralization, as some refineries may already have flexibility in their hydrogen networks or could adapt their operations. [confidence: medium]

- "Part of the motivation is regulatory rather than purely domestic: hydrogen is one of the product categories explicitly covered by the European Union's Carbon Border Adjustment Mechanism (CBAM), alongside steel, aluminium, cement, fertilisers, and electricity, and India's refiners are large exporters of diesel and other gasoil products into European markets — one 2025 trade forecast put India's gasoil exports, much of it winter-heating-season diesel bound largely for Europe, at 560,000–630,000 barrels a day." — The article conflates CBAM's coverage of *hydrogen* with its potential impact on *diesel exports*. CBAM does not currently tax diesel exports; it only applies to hydrogen and a few upstream commodities. The claim that CBAM's existence is a motivation for refiners to switch to green hydrogen due to diesel export exposure is misleading, as the mechanism does not directly affect diesel. The strategic motivation may be plausible, but the causal link to CBAM's current rules is incorrect. [confidence: high]
