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
- "India's Bharat Stage VI standard, equivalent to Euro 6, caps diesel sulphur at 10 parts per million — down from 50 ppm under the outgoing BS-IV standard — and took effect nationwide on 1 April 2020." — The Bharat Stage VI (BS-VI) standard for diesel sulphur was indeed set at 10 ppm, but it replaced BS-IV (which had a 50 ppm limit) only after BS-V (equivalent to Euro 5) was skipped. BS-VI was implemented nationwide on **1 April 2020**, but the transition from BS-IV to BS-VI was not direct; BS-V was introduced in 2019 for certain regions before BS-VI's nationwide rollout. The claim oversimplifies the timeline by implying a direct BS-IV to BS-VI transition. [confidence: high]

- "The green bid price sits roughly 1.7 to 3.2 times above grey hydrogen depending which grey benchmark is used — global natural-gas SMR pricing at the low end, India's own higher domestic grey-hydrogen cost estimate at the high end." — The article cites a green hydrogen bid price of ₹397/kg (≈$4.16/kg) and compares it to grey hydrogen costs of $1.3–1.5/kg (global) and ₹150–200/kg (≈$1.8–2.4/kg, India-specific). However, the ratio calculation is inconsistent: $4.16 / $1.5 ≈ 2.77 (not 1.7), and $4.16 / $2.4 ≈ 1.73 (not 3.2). The article's stated range of 1.7–3.2 times is incorrect based on the provided figures. [confidence: high]

---

INTERPRETATION ERRORS:
- "The transition is not simply a matter of swapping one hydrogen source for another at the plant gate. An industry technical overview of refinery hydrogen systems notes that existing refinery infrastructure is 'optimised around the predictable operating characteristics of reformers,' prioritising stability and availability, while electrolysers introduce short-term output variability — tied to when renewable power is actually available — that refinery hydrogen systems were never designed to absorb." — The article correctly notes technical challenges in integrating electrolysers into refineries, but it implies these challenges are solely due to variability in renewable power supply. However, the variability issue is a secondary concern compared to the **primary challenge of scaling up electrolysers to meet the massive hydrogen demand of refineries** (2.5 MTPA today, projected to grow to 4.5 MTPA by FY2030). The article understates the magnitude of the transition by focusing on operational integration rather than the feasibility of replacing a tiny fraction (30 KTPA) of grey hydrogen with green hydrogen at scale. [confidence: high]

- "CBAM's initial phase does not yet directly tax refined fuel exports the way it taxes hydrogen itself, but the mechanism's existence, and the general direction of EU carbon policy, is part of why refiners with export exposure are moving early rather than waiting for a domestic mandate to force the issue." — The article suggests that the **anticipation of future CBAM coverage for refined fuels** (not just hydrogen) is a key driver for Indian refiners' early adoption of green hydrogen. However, CBAM's **current phase (2026–2034) only covers hydrogen, steel, aluminium, cement, fertilisers, and electricity**—not refined fuels like diesel. While the EU may expand CBAM to include refined fuels in future phases, the article presents this as a **current motivation**, which is speculative and not supported by current policy. The reasoning gap is conflating **potential future policy** with **current strategic decisions**. [confidence: high]
