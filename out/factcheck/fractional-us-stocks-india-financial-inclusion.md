# Fact/interpretation check — fractional-us-stocks-india-financial-inclusion

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fractional-us-stocks-india-financial-inclusion.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99968, Requested 2583. Please try again in 36m44.064s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — The cited source (SBI Securities) reports 23.15 crore demat accounts as of June 2026, but the article itself notes this is a cross-check against "more recent June 2026 industry reporting," implying the figure may not be final or officially confirmed. The claim lacks a primary government or exchange source (e.g., CDSL/NSDL) for verification. [confidence: medium]

- "MRF Ltd (NSE, India's highest-priced listed stock) | ₹1,34,200 | 10 Aug 2026" — The price of ₹1,34,200 for MRF Ltd is not verifiable against the cited source (StockAnalysis.com) or other mainstream financial data providers. MRF's share price as of August 2026 is significantly lower (e.g., ~₹1,00,000–1,10,000 per share in recent trading). [confidence: high]

INTERPRETATION ERRORS:
- "Fractional investing hasn't closed that gap yet" — The claim implies fractional investing is the *only* solution to the price barrier for Indian stocks, but it ignores alternative mechanisms (e.g., stock splits, bonus issues, or mutual funds) that could make whole shares more accessible without legal changes. The article frames the problem as solely solvable via fractional ownership, which is an overgeneralization. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric" — While the article correctly notes that fractional investing for US stocks is available, it extrapolates this to claim the *inclusion case itself* is "asymmetric" without quantifying the actual impact on retail participation or comparing pre- and post-fractional investing metrics (e.g., demat account growth rates or retail ownership of high-priced stocks). The conclusion is not directly supported by the data presented. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
