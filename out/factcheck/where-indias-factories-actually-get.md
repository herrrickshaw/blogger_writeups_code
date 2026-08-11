# Fact/interpretation check — where-indias-factories-actually-get

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-indias-factories-actually-get.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99052, Requested 5907. Please try again in 1h11m24.576s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 1,869,333 Rs cr implemented" — The article later states the 5-year total as Rs 19,51,828cr (Rs 1.95 lakh crore), which is inconsistent with the initial figure. The correct total is likely Rs 19,51,828cr as per the "All-India Part B 2021-2025" section. [confidence: high]

- "Appendix V is headed 'Up to Dec 2025' while Appendix VI says 'Up to Nov 2025' — yet both grand-total to the identical Rs 5,83,096cr" — The article claims both appendices total Rs 5,83,096cr, but this figure does not appear anywhere in the provided text. The grand totals mentioned are Rs 19,51,828cr (Part B) and Rs 5,83,096cr is not referenced in the article. [confidence: high]

INTERPRETATION ERRORS:
- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The claim implies that Gujarat implemented Rs 4.55 lakh crore in a single year (2024-2025), but the table shows Gujarat's 2025 (to Dec) as Rs 246,595cr (Rs 2.47 lakh crore). The Rs 4.55 lakh crore figure is the sum of Gujarat's 2024 (Rs 208,025cr) and 2025 (Rs 246,595cr), which is a 2-year total, not a single year. The article misrepresents this as a single-year figure. [confidence: high]

- "Rs 1,22,497cr of the 5-yr total sits in a single year (2024) against Rs 1-3,000cr in every other year" (Glass sector) — While the anomaly is correctly flagged, the article does not explain why this single-year spike is treated as an anomaly rather than a trend. The spike could reflect a genuine mega-project (e.g., solar glass manufacturing) or a data reporting quirk, but the article does not provide external evidence to justify dismissing it as an anomaly. The interpretation lacks justification for why this should not be considered a trend. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
