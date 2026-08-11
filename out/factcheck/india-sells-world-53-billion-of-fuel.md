# Fact/interpretation check — india-sells-world-53-billion-of-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-sells-world-53-billion-of-fuel.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99414, Requested 3965. Please try again in 48m39.456s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The date is impossible as the article references FY2025-26 data (which ends in March 2026) and mentions "FY2026-27" in the future tense. The correct publication date should be in 2025. [confidence: high]

- "US$53.0bn Refined petroleum exports, HS 2710, FY2025-26" — The article later cites the exact export value as US$52,973 million (≈US$53.0bn), but the table shows FY2025-26 exports as US$52,973 million, not US$53.0bn. The rounding is inconsistent with the precision of other figures. [confidence: high]

INTERPRETATION ERRORS:
- "The surplus is real. India buys crude and sells fuel, and the margin between them is one of the country’s largest export earnings." — While the net surplus of US$43.653bn is correct, attributing the entire margin to export earnings is misleading. The margin includes domestic consumption and refining profits, not just exports. The surplus is a trade surplus, not necessarily a pure export earnings surplus. [confidence: high]

- "Sri Lanka is the one genuine growth story here, and it is worth being precise about why that is not a template." — The article correctly notes Sri Lanka's growth but incorrectly implies that the growth is due to competitive market dynamics rather than other factors (e.g., supply chain disruptions, policy changes, or pricing anomalies). The data does not support the conclusion that Sri Lanka's growth is a "template" for other markets. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
