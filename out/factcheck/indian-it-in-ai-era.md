# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

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
- "Services · Balance of payments · 4 August 2026" — The article is dated 4 August 2026, but the referenced RBI data (e.g., "Developments in India's Balance of Payments, Q4 2025-26") and other sources (e.g., Economic Survey 2025-26) are from FY2025-26, which ended on 31 March 2026. The date is incorrect as it postdates the fiscal year data. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year" — The RBI data shows net services receipts of $216.6bn in FY2025-26, but the $27.8bn increase is incorrect. The correct increase is $27.8bn from FY2024-25 ($188.8bn to $216.6bn), which is accurate, but the phrasing implies a single-year jump from FY2024-25 to FY2025-26, which is correct. However, the claim that this is the "biggest jump on record" is unverified and lacks a source. [confidence: medium]

INTERPRETATION ERRORS:
- "The warning signs are elsewhere: net hiring has collapsed from ~450,000 (FY22) to 135,000 (FY26) against a growing revenue base, and chief executives now name 'AI deflation' worth 3–5% of revenue" — The claim conflates correlation with causation. While hiring has slowed and executives cite "AI deflation," the article does not establish that AI is the primary driver of either trend. Other factors (e.g., economic cycles, automation unrelated to AI, or strategic shifts in hiring) could also explain the decline in net hiring. The causal link to AI is speculative. [confidence: high]

- "It can produce a balance-of-payments event. If services receipts stall while the goods deficit keeps widening — and it widened by $50 billion in FY2026 alone — the adjustment happens in the exchange rate and the capital account, not in the unemployment rate" — The claim extrapolates from a single year's data ($50 billion goods deficit widening in FY2026) to a generalizable trend without sufficient evidence. The goods deficit widened from $286.9bn (FY2024-25) to $337.3bn (FY2025-26), a $50.4bn increase, but this is not necessarily indicative of a persistent trend. The article does not provide historical context or projections to support the assertion that this widening will continue or that it will directly trigger a balance-of-payments crisis. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
