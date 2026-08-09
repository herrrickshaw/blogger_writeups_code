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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99700, Requested 5182. Please try again in 1h10m18.048s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data in Exhibit 1, which shows net services receipts at $216.6bn for FY2025-26, but the $27.8bn increase is incorrect. The actual increase from FY2024-25 ($188.8bn) to FY2025-26 ($216.6bn) is $27.8bn, but the article does not explicitly state the prior year's figure, making the claim ambiguous. However, the calculation itself is correct based on the provided data. [confidence: high]

- "The merchandise trade deficit was $337.3 billion." — The article cites the RBI data in Exhibit 1, which shows the merchandise trade deficit at $337.3bn for FY2025-26. However, the RBI's "Developments in India's Balance of Payments, Q4 2025-26" (as cited) likely refers to FY2024-25, not FY2025-26, as the fiscal year 2025-26 would not have been published by Q4 2025-26. This suggests a possible mislabeling of the fiscal year in the article. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the arithmetic is correct (64% and 107% based on the provided figures), this interpretation implies that the services surplus is the sole reason India's current account deficit remains manageable. However, the article later notes that the primary income deficit (investment income paid out) is the actual driver of the current account deficit ($48.2bn). The framing risks oversimplifying the balance-of-payments dynamics by focusing only on the offsetting role of services and remittances without adequately emphasizing the structural role of investment income outflows. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — While the sector's employment share (~1%) and GDP share (~8%) are correctly cited, the causal claim that an AI shock would *only* manifest as a balance-of-payments event (currency adjustment) and not affect employment is an overgeneralization. The article acknowledges that AI-driven productivity gains are being passed to clients as price reductions, which could eventually lead to job losses (e.g., via reduced hiring or layoffs). The claim ignores the potential lagged or indirect employment effects of such productivity-driven price adjustments. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
