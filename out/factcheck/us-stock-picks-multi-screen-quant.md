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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99595, Requested 3835. Please try again in 49m23.519999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Avg ROE -20.9%" (BeOne Medicines Ltd.) — The article lists a negative ROE for BeOne Medicines Ltd., but negative ROE is not a valid Piotroski score component (Piotroski F-score requires ROE ≥ 0). The F-score of 7 suggests a positive ROE, creating a contradiction. [confidence: high]

- "Avg ROE flagged (near-zero/negative equity distorts this ratio)" (Seagate Technology Holdings PLC) — The article flags Seagate’s ROE as distorted due to near-zero/negative equity but still assigns it a Piotroski F-score of 7, which is inconsistent because negative equity would typically result in a zero or lower F-score. [confidence: high]

INTERPRETATION ERRORS:
- "Multi-screen agreement → highest conviction sleeve" (repeated for all stocks) — The article claims that multi-screen agreement implies "highest conviction sleeve" for every stock in the CORE sleeve, but it does not provide evidence or methodology to support that these mechanical filters (e.g., Darvas breakout, Piotroski quality) reliably correlate with higher conviction or future performance. The claim extrapolates beyond what the data shows. [confidence: high]

- "Avg ROE 65.3%" (Medpace Holdings, Inc.) — While the ROE figure itself may be correct, the article uses it to support a "high conviction" thesis without addressing whether such a high ROE is sustainable, industry-comparable, or factored into the screening methodology. This is an apples-to-oranges comparison because Piotroski F-score (used in the screen) does not incorporate ROE magnitude, only its sign and trend. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
