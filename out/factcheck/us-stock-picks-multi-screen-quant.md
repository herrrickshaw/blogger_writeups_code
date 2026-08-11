# Fact/interpretation check — us-stock-picks-multi-screen-quant

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/us-stock-picks-multi-screen-quant.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99874, Requested 3422. Please try again in 47m27.744s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "AI Disclosure: This article was researched and written with AI assistance (Claude Sonnet), drawing on publicly available government, industry, and academic sources cited above." — The article does not cite any sources above the disclosure, making the claim unverifiable. [confidence: high]

- "Generated 2026-07-24 13:33 UTC" — The article header states "scan as of 2026-07-24 00:43," while the footer claims generation at "2026-07-24 13:33 UTC," creating a contradiction in timestamps. [confidence: high]

INTERPRETATION ERRORS:
- "Avg ROE -20.9%" (BeOne Medicines Ltd.) — While the negative ROE is correctly stated, it is used to support a "Quality A/B" rating despite Piotroski F=7 (which typically requires positive earnings and improving financial health). The negative ROE contradicts the implied quality, creating a reasoning gap. [confidence: high]

- "Breakout quality A (80)" (Woodward, Inc.) — The article claims a "Darvas breakout" and "Breakout quality A (80)" while also noting the stock is priced at $414.37, which is far above typical Darvas breakout thresholds (often seen in lower-priced stocks). The high price may distort the breakout signal's validity, but this is not addressed. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
