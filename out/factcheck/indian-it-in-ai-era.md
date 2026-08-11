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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99759, Requested 5278. Please try again in 1h12m31.968s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data for FY2025-26, but the RBI's *Developments in India's Balance of Payments, Q4 2025-26* (as referenced in Exhibit 1) shows net services receipts of $216.6bn for FY2025-26, but the prior year (FY2024-25) is listed as $188.8bn, implying an increase of $27.8bn. However, the RBI data in Exhibit 1 shows a current account deficit of -$25.2bn for FY2025-26, which contradicts the article's earlier statement that the current account deficit was 0.6% of GDP (which aligns with -$25.2bn only if GDP is ~$4.2trn, but the article does not provide GDP figures to verify this). The increase in net services receipts is correctly calculated, but the GDP-based current account deficit claim lacks explicit verification. [confidence: medium]

- "The Economic Survey's own uncomfortable framing" section quotes the 2025-26 Survey as saying services exports are “not a substitute for the goods-based export ecosystems that ultimately underpin durable external and currency stability.” — The article does not provide a direct quote or citation from the Economic Survey 2025-26 to verify this claim. While the Economic Survey is mentioned as a source, the specific phrasing is not directly attributed to any publicly available document or page, making it unverifiable. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the numbers are factually correct (64% and 107% based on the RBI data), the interpretation that this means services exports are "macro-stabilising" is an overstatement. The article implies that because services receipts cover the goods deficit, they are inherently stabilizing, but this ignores the fact that the primary income deficit (investment income paid out) is what drives the current account deficit. The services surplus offsets the goods deficit, but the primary income deficit (which is structural and growing) is the real macroeconomic constraint. The article conflates the accounting identity with economic stability. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — The claim is correct in stating the sector's share of jobs and GDP, but the causal leap that an AI shock to services exports would *only* produce a balance-of-payments event (and not any employment effects) is an overinterpretation. While the sector's employment share is small, the broader economy could still face indirect employment effects (e.g., through reduced demand for ancillary services, vendor ecosystems, or multiplier effects). The article dismisses employment impacts too categorically. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
