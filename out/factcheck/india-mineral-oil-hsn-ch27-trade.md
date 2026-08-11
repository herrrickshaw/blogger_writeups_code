# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99789, Requested 3553. Please try again in 48m7.488s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The article claims this figure is for FY25-26 H1, but the fiscal year 2025-26 (April 2025–March 2026) has not yet occurred as of the current date (June 2025). This is a future projection mislabeled as a historical fact. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46" — The Kirit Parikh Committee report (2023) does not set a floor/ceiling mechanism tied to the Indian crude basket for APM gas. The committee recommended a market-linked pricing formula, not a fixed floor/ceiling tied to crude. [confidence: high]

---

INTERPRETATION ERRORS:
- "Implied $/bbl from trade value÷quantity tracks the Indian basket within ±6% every year — the core consistency check." — While the implied $/bbl may track the Indian basket closely, this does not necessarily validate the *entire* pricing mechanism or trade data accuracy. The ±6% range could reflect minor discrepancies in trade reporting, currency conversion, or timing differences rather than a true validation of the pricing formula's integrity. The claim implies a stronger causal link between the consistency check and the reliability of the pricing formula than is justified. [confidence: medium]

- "80 : 20 Trade Parity Price = IPP : EPP weight" — The article states this ratio as a fixed rule, but the Trade Parity Price (TPP) formula is actually defined as TPP = 0.80 × IPP + 0.20 × EPP, where IPP and EPP are weighted components. The phrasing "80 : 20 Trade Parity Price = IPP : EPP weight" incorrectly suggests a direct equivalence between the ratio and the weights, rather than clarifying that the weights are applied to the components in the formula. This conflates the formula's structure with a standalone ratio. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
