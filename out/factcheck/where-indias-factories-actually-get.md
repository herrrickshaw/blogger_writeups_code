# Fact/interpretation check — where-indias-factories-actually-get

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-indias-factories-actually-get.html`

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
- "1,869,333 Rs cr implemented, top 15 states, 2021–Dec 2025" — The article later states "All-India Part B 2021-2025: Rs 19,51,828cr" (Rs 19.52 lakh cr), which contradicts the initial figure of Rs 1,869,333 cr (Rs 1.87 lakh cr). The discrepancy suggests a decimal error or misplaced comma. [confidence: high]

- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The table shows Gujarat's 2024 and 2025 (to Dec) figures as 208,025 cr and 246,595 cr, respectively, totaling ~454,620 cr (Rs 4.55 lakh cr). However, the article claims this is "2024-2025 alone," which is ambiguous (does it mean FY2024-25 or calendar years 2024 and 2025?). If it refers to FY2024-25, the data does not align with standard fiscal year definitions (April 2024–March 2025), as the table includes partial-year 2025 data (to Dec 2025). [confidence: medium]

INTERPRETATION ERRORS:
- "The implementation engine of Indian industry -- Rs 2.09 lakh cr in 2025 alone (the largest single-year sector figure in the series). This is the Odisha/Gujarat/Chhattisgarh steel-and-metals capex, overwhelmingly domestic-funded..." — While Metallurgical Industries is the top implemented sector, the claim that it is "the largest single-year sector figure in the series" is misleading. The table shows "Metallurgical Industries" at Rs 209,301 cr for 2025, but "Fuels" has Rs 70,117 cr in 2025 (likely a single mega-project) and "Glass" has Rs 1,22,497 cr in 2024 (also likely a single project). The article does not clarify whether these are one-off anomalies or trends, nor does it compare sectoral figures across years to justify the "largest" claim. [confidence: high]

- "Rs 1,22,497cr of the 5-yr total [for Glass] sits in a single year (2024) against Rs 1-3,000cr in every other year -- either one mega-project (solar glass?) or a data quirk. Not treated as a trend." — While the article flags this as an anomaly, it then uses the 2025 Metallurgical Industries figure (Rs 209,301 cr) as a trend indicator without acknowledging that this could also be a one-off mega-project (e.g., a single steel plant). The reasoning gap is that the article treats Metallurgical Industries as a reliable trend while dismissing Glass as an anomaly, without providing evidence to distinguish between the two. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
