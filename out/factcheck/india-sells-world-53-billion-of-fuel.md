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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99494, Requested 3965. Please try again in 49m48.576s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The article cites DGCI&S TRADESTAT data for FY2024-25 and FY2025-26, but the publication date is implausible as it predates the end of FY2025-26 (which would conclude in March 2026). The data run date (8 August 2026) is also inconsistent with the FY2025-26 data being finalized before the fiscal year ends. [confidence: high]

- "US$53.0bn Refined petroleum exports, HS 2710, FY2025-26" — The article later contradicts this by stating exports were US$52,973 million (US$52.973bn), not US$53.0bn. The rounding is inconsistent with the precise figure provided elsewhere. [confidence: high]

INTERPRETATION ERRORS:
- "The surplus is real — India buys crude and sells fuel, and the margin between them is one of the country’s largest export earnings." — While the surplus is real in terms of trade value, the article conflates *trade surplus* (exports minus imports) with *profit margin* (revenue minus cost of crude). The trade surplus does not reflect refining margins, which depend on crude prices, refining costs, and product prices—none of which are accounted for in the trade data. [confidence: high]

- "Sri Lanka is the one genuine growth story here, and it is worth being precise about why that is not a template." — The article correctly notes Sri Lanka's growth but incorrectly implies that its competitive market structure (where India both exports to and imports from Sri Lanka) is unique among neighbors. However, the trade data shows Bangladesh also had a small two-way trade (though not explicitly highlighted), and the article does not establish that Sri Lanka's growth is structurally different from other neighbors in a way that invalidates it as a template. The reasoning gap is in overgeneralizing Sri Lanka's uniqueness without broader comparative analysis. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
