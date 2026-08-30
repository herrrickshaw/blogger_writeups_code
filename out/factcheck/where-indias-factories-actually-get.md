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
- "Rs 1,869,333 Rs cr implemented" — The correct figure for all-India Part B implementation (2021–Dec 2025) is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 cr. The initial figure appears to be a typographical error or misformatting of the correct value. [confidence: high]

- "Appendix V is headed 'Up to Dec 2025' while Appendix VI says 'Up to Nov 2025' -- yet both grand-total to the identical Rs 5,83,096cr" — The article claims this is an inconsistency in DPIIT's own document, but the grand total of Rs 5,83,096 cr does not appear anywhere in the provided text or standard DPIIT reports. This figure is likely incorrect or misstated. [confidence: high]

INTERPRETATION ERRORS:
- "Gujarat ... implementing 178% of same-period intent (the pre-2021 pipeline landing)" — The article attributes Gujarat's 178% conversion rate to "pre-2021 pipeline landing," implying that the excess implementation is due to older filings. However, the conversion rate is calculated as a same-period flow ratio (Part B in 2021–2025 divided by Part A in the same period), not a cohort-matched analysis. This risks conflating pipeline effects with contemporaneous intent, potentially overstating the "boom" in new industrial activity. [confidence: high]

- "Metallurgical Industries ... overwhelmingly domestic-funded (the same sector whose FDI proxy is amber and whose PLI has disbursed 0.8%)" — The article uses the low PLI disbursement (0.8%) and "amber" FDI proxy to imply that metallurgical industries are overwhelmingly domestic-funded. However, PLI disbursement is not a direct measure of funding source (domestic vs. foreign), and FDI equity inflows are an incomplete proxy for total investment (which includes debt and domestic capital). This reasoning conflates different metrics and misrepresents the funding composition. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
