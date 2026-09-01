# Fact/interpretation check — india-hit-e20-on-maize-and-rice-not

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-hit-e20-on-maize-and-rice-not.html`

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
- "Maize alone is 45.7 per cent, up from 6.2 per cent in ESY 2022-23 — a sevenfold shift in three years." — The article later states maize's share as 45.68% in ESY 2025-26 and 6.2% in ESY 2022-23, which is a **sevenfold increase** (6.2% × 7 ≈ 43.4%, close to 45.68%). However, the claim of "sevenfold shift" is an **approximation**, not an exact calculation, and the phrasing could mislead readers into thinking it's a precise sevenfold increase. The exact increase is ~7.36x (45.68/6.2), not sevenfold. [confidence: high]

- "Surplus FCI rice supplies more of India’s petrol blend than sugarcane juice does." — The article later quantifies this as 22.25% (rice) vs. 15.82% (sugarcane juice), which is correct. However, the phrasing "more of India’s petrol blend" is ambiguous—it could imply **total volume** (which is correct) or **proportion of total petrol**, which is not explicitly stated. The claim is technically correct but could be misinterpreted. [confidence: medium]

---

INTERPRETATION ERRORS:
- "The target has been met. Blending has held at 20 per cent through the current Ethanol Supply Year. And the assumption behind the question turned out to be wrong." — The article correctly states that blending has held at 20% in ESY 2025-26, but it **does not prove** that the original assumption (that sugarcane would be the primary feedstock) was the reason the target was met. The shift to grain-based ethanol was driven by **availability and price**, not the failure of sugarcane. The conclusion that the assumption was "wrong" conflates **unmet expectations** with **causal failure**. The original feedstock objection was about **sufficiency**, not **composition**, and the target was met despite (not because of) the shift away from sugarcane. [confidence: high]

- "Maize is India’s priciest ethanol feedstock at ₹71.86 a litre. Both things are true at once, and together they are the point: the most expensive feedstock became the largest one. Cost was not the binding constraint. Availability was." — While maize may be the most expensive feedstock **per litre of ethanol produced**, the claim that "cost was not the binding constraint" is **not supported by the data**. The article does not compare the **total cost** of maize-based ethanol (which includes higher feedstock costs) to alternatives like sugarcane or rice. The **allocation decision** by oil marketing companies was likely based on **price per litre of ethanol**, but this does not mean **total system cost** was irrelevant. The conclusion assumes that because maize was allocated the most, its **unit cost** was not a constraint, but this ignores **economics of scale, distillery efficiency, and policy incentives**. [confidence: high]
