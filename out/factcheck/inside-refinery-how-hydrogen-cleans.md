# Fact/interpretation check — inside-refinery-how-hydrogen-cleans

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/inside-refinery-how-hydrogen-cleans.html`

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
- "India's Bharat Stage VI standard, equivalent to Euro 6, caps diesel sulphur at 10 parts per million — down from 50 ppm under the outgoing BS-IV standard — and took effect nationwide on 1 April 2020." — The Bharat Stage VI (BS-VI) standard did not take effect on 1 April 2020; it was implemented nationwide on 1 April 2020, but the sulphur cap for diesel under BS-VI is 10 ppm, which is correct. However, the outgoing standard was BS-IV (not BS-VI), which had a sulphur cap of 50 ppm. The date is correct, but the phrasing implies BS-VI replaced BS-IV, which is accurate, but the claim as written could be misinterpreted as BS-VI being the outgoing standard. [confidence: high]

- "The green bid price sits roughly 1.7 to 3.2 times above grey hydrogen depending which grey benchmark is used — global natural-gas SMR pricing at the low end, India's own higher domestic grey-hydrogen cost estimate at the high end." — The article cites a green hydrogen bid price of ₹397 per kg (including GST) for IOCL's refineries, which is approximately $4.11–4.21/kg. However, the claim that the green bid price is 1.7 to 3.2 times above grey hydrogen is based on comparing this green price to a grey hydrogen cost range of $1.3–1.5/kg (global) and ₹150–200/kg (India, roughly $1.8–2.4/kg). While the math is correct, the phrasing "sits roughly 1.7 to 3.2 times above grey hydrogen" is misleading because it conflates the global and India-specific grey hydrogen costs without clear delineation. The ratio varies significantly depending on the benchmark, and the claim does not clarify this distinction. [confidence: medium]

INTERPRETATION ERRORS:
- "Almost all of that hydrogen still comes from steam methane reforming, a fossil-gas process that emits 9–12 kilograms of CO2 for every kilogram of hydrogen it makes." — While the CO2 emissions figure (9–12 kg CO2/kg H2) for steam methane reforming (SMR) is factually correct, the article implies that this emissions intensity is the sole or primary reason for India's policy push to adopt green hydrogen in refineries. However, the policy push is also driven by broader decarbonization goals, export competitiveness (e.g., CBAM), and long-term energy security, not just the carbon intensity of SMR. The article does not acknowledge these additional motivations, leading to an incomplete interpretation of the policy rationale. [confidence: high]

- "The transition is not simply a matter of swapping one hydrogen source for another at the plant gate. An industry technical overview of refinery hydrogen systems notes that existing refinery infrastructure is 'optimised around the predictable operating characteristics of reformers,' prioritising stability and availability, while electrolysers introduce short-term output variability — tied to when renewable power is actually available — that refinery hydrogen systems were never designed to absorb." — The article correctly identifies technical challenges in integrating electrolysers into refinery hydrogen systems, such as variability in renewable power supply. However, it does not address potential solutions or mitigations for these challenges, such as energy storage, grid balancing, or hybrid systems combining SMR and electrolysis. By focusing solely on the challenges without discussing solutions, the article presents an incomplete picture of the feasibility of transitioning to green hydrogen in refineries. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
