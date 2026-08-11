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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99472, Requested 4951. Please try again in 1h3m41.471999999s. Need more tokens? Upgrade to Dev Tier today ]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) as the source, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" does not show net services receipts increasing by $27.8bn in a single year. The table shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), which is an increase of $27.8bn, but the RBI data is for Q4 2025-26, not the full fiscal year. The article misrepresents the RBI's data as covering the full fiscal year when it does not. [confidence: high]

- "The merchandise trade deficit was $337.3 billion." — The RBI table in the article shows the merchandise trade deficit as −$337.3bn for FY2025-26, but the article states it as "$337.3 billion" without the negative sign, implying a surplus rather than a deficit. This is a factual error in the sign of the trade balance. [confidence: high]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the arithmetic is correct (64% and 107% are accurate based on the RBI data), the interpretation that this means the services surplus is "macro-stabilising" is flawed. The article implies that because services receipts cover the goods deficit, they are inherently stabilizing, but this ignores the fact that the primary income deficit (investment income paid out) is what drives the current account deficit. The services surplus offsets the goods deficit, but the primary income deficit is the actual driver of the CAD, which remains small due to the services surplus. The conclusion that services receipts are "macro-stabilising" is an overreach because it conflates offsetting a deficit with creating stability. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's share of employment (1%) and GDP (~8%) is correct, the causal claim that it "cannot produce a mass-unemployment event" is an overgeneralization. The article assumes that because the sector is small in employment terms, job losses cannot be significant, but this ignores the concentration of job losses in specific segments (e.g., middle management) and the potential for spillover effects in related industries. The claim conflates aggregate employment with sector-specific impacts, which is an apples-to-oranges comparison. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
