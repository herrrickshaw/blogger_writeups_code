# Fact/interpretation check — below-250-is-where-real-junk-lives

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/below-250-is-where-real-junk-lives.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99306, Requested 2334. Please try again in 23m36.96s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.5 years of weekly local NSE price data (2 January 2023 to 7 August 2026)" — The end date (7 August 2026) is in the future relative to the article's publication date (11 August 2026), making the data range impossible. The correct end date should likely be 7 August 2025. [confidence: high]

INTERPRETATION ERRORS:
- "Price itself still isn't the risk factor — market capitalisation and liquidity are, and they happen to correlate tightly with price only at the very bottom of the market" — While the article correctly notes that market cap and liquidity are the true risk factors, it implies that price correlates tightly with these factors *only* at the bottom (₹0–250). However, the data shows that median market cap increases sharply from ₹80 crore (₹0–250) to ₹1,154 crore (₹250–500), but the correlation between price and market cap is not explicitly tested or quantified beyond these sub-bands. The claim overgeneralizes the relationship without evidence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
