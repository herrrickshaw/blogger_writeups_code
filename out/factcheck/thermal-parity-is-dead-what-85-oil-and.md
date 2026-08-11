# Fact/interpretation check — thermal-parity-is-dead-what-85-oil-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thermal-parity-is-dead-what-85-oil-and.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99922, Requested 3654. Please try again in 51m29.664s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026 · v1.0.0" — The date is impossible as the article references data from August 2026 (e.g., "Indian crude basket, $85.2/bbl, 4 August 2026"), which would not be available in advance. [confidence: high]

- "$7 India’s notified APM gas ceiling, $/MMBtu, against $85 crude" — The article later cites the actual notified price as $7.86/MMBtu (not $7) for August 2026. [confidence: high]

INTERPRETATION ERRORS:
- "India’s notified APM gas ceiling sits at roughly 2.0× thermal parity — almost exactly the informal '10:1' the industry has used as a rule of thumb since long before this pricing formula existed." — While the ratio is correct (10.8:1), the claim implies the formula was designed to match the industry rule of thumb, which is misleading. The Kirit Parikh formula ties gas to crude at 10% of the crude basket price (not the 10:1 ratio), and the ceiling is a separate policy choice. The ratio is a coincidental outcome, not a deliberate alignment. [confidence: high]

- "A crude price fall, symmetrically, would flow straight through to the 10% calculation until it hits the $4 floor." — This suggests a direct pass-through of crude price changes to gas prices, but the article later notes that the notified price ($7.86) is below the raw formula output ($8.4–8.5), implying the ceiling is binding. The pass-through is not symmetric because the ceiling artificially caps the price, breaking the direct linkage. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
