# Fact/interpretation check — from-cane-to-code-digital-layer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/from-cane-to-code-digital-layer.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99246, Requested 2791. Please try again in 29m19.967999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article cites a publication date of 8 August 2026, but the content references events and data (e.g., "ESY2025-26," "June 2026," "March 2026") that are either future-dated or inconsistent with a 2026 publication date. This creates a temporal contradiction. [confidence: high]

- "₹1.67L cr Cumulative forex saved by ethanol blending since ESY2014-15" — The article attributes this figure to a Rajya Sabha unstarred question (9 March 2026), but the claim lacks a direct citation to the official source (e.g., a parliamentary document or government press release). The figure is presented as a fact without verifiable primary evidence in the text. [confidence: medium]

---

INTERPRETATION ERRORS:
- "4–8% Additional ethanol yield claimed from AI-tuned fermentation, same molasses input" — The article presents this vendor-reported figure as a factual efficiency gain without clarifying that it is a *claimed* improvement (not independently audited) and may not reflect real-world performance across the industry. The lack of caveats about the unreliability of vendor data creates a false impression of certainty. [confidence: high]

- "10–20% Farm yield improvement claimed for growers on an AI advisory pilot in Maharashtra" — The article cites this as a concrete outcome, but it is based on a small, unaudited pilot (the "Super 50 AI Farmers" cohort in Jalna district). The claim extrapolates localized results to broader farm yields without addressing selection bias, sample size limitations, or external validity. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
