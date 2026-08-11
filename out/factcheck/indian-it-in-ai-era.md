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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99395, Requested 4951. Please try again in 1h2m34.944s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites the Reserve Bank of India (RBI) data showing net services receipts at $216.6bn in FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) does not show this figure. The RBI data in the article's Exhibit 1 shows net services receipts as $216.6bn for FY2025-26, but the $27.8bn increase is not directly verifiable from the RBI data presented. The RBI table shows an increase from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), which is a $27.8bn increase, but the RBI does not explicitly state this as the "largest increase on record." [confidence: high]

- "The merchandise trade deficit was $337.3 billion." — The RBI data in Exhibit 1 shows the merchandise trade deficit as $337.3bn for FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) does not explicitly state this figure. The RBI table shows the deficit as $337.3bn, but the RBI does not label it as the "largest" or provide historical context to confirm it is the largest on record. [confidence: medium]

INTERPRETATION ERRORS:
- "AI deflation" worth 3–5% of revenue — Chief executives (e.g., HCLTech's C. Vijayakumar) state that "AI deflation" would take 3–5% off revenue in the coming year, but this claim conflates *potential* future revenue loss with *actual* measured revenue loss. The executives' statements are forward-looking and speculative, not based on verified FY2025-26 data. The article does not provide evidence that this "AI deflation" has already occurred or is directly tied to measurable revenue declines in the reported period. [confidence: high]

- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — While the arithmetic in Exhibit 1 is correct ($216.6bn services receipts / $337.3bn goods deficit ≈ 64%; $216.6bn + $143.6bn remittances = $360.2bn > $337.3bn), the interpretation implies that services and remittances *cause* the goods deficit to be manageable. However, the goods deficit is driven by import demand and export performance in goods, not by services or remittances. The services surplus merely offsets the goods deficit ex post; it does not explain or reduce the underlying goods trade imbalance. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
