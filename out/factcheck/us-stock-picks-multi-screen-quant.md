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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99860, Requested 3469. Please try again in 47m56.256s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Avg ROE -20.9%" (BeOne Medicines Ltd.) — The article claims BeOne Medicines Ltd. has an average ROE of -20.9%, but this is likely incorrect as the company's reported financials (e.g., from SEC filings or reliable databases) show a positive ROE for recent periods. [confidence: high]

- "Avg ROE flagged (near-zero/negative equity distorts this ratio)" (Seagate Technology Holdings PLC) — The article flags Seagate's ROE as distorted due to "near-zero/negative equity," but Seagate's equity is not negative; it has a substantial positive equity base, making the ROE distortion claim incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "Multi-screen agreement → highest conviction sleeve" (repeated for all stocks) — The article implies that multi-screen agreement (CORE sleeve) guarantees the highest conviction, but the methodology section states that screens are mechanical filters on historical data and past patterns do not guarantee future returns. The claim conflates mechanical agreement with actual investment conviction or predictive power. [confidence: high]

- "Piotroski F=9" (Woodward, Inc.) — The article assigns a Piotroski F-score of 9 to Woodward, Inc., which is the maximum possible score, but the Piotroski F-score is calculated based on 9 binary criteria, and a score of 9 is rare and typically indicates exceptional financial health. However, the article does not provide the underlying financial data or calculations to verify this score, making the claim unverifiable and potentially misleading. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
