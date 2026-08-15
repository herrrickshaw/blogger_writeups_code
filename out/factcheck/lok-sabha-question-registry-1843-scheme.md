# Fact/interpretation check — lok-sabha-question-registry-1843-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/lok-sabha-question-registry-1843-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99200, Requested 1336. Please try again in 7m43.104s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "17th and 18th Lok Sabha (2019-06-17 → 2026-08-04)" — The 17th Lok Sabha's term ended in 2024, not 2026. The 18th Lok Sabha began in 2024, but the end date (2026-08-04) is incorrect as it implies the current date is in 2026, which is not accurate. [confidence: high]

- "Generated 2026-08-04 by scripts/build_pq_registry.py" — The date "2026-08-04" is incorrect as it refers to a future date (August 4, 2026), which is not plausible for a current or recent build. [confidence: high]

INTERPRETATION ERRORS:
- "This registry is the parliamentary companion to the Quarterly Reportage: where the reportage tracks what government announced, this tracks what Parliament asked — and the ministry's answer of record." — The claim implies a direct and meaningful comparison between "what government announced" and "what Parliament asked," but the registry only tracks questions asked in Parliament, not the government's announcements. The two datasets may not be comparable in a way that supports the stated purpose. [confidence: medium]

- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — While the caution about verifying AI-generated figures is valid, the claim that AI "can misstate figures" is presented as a general warning without evidence or specificity. It does not explain how or why this might occur in the context of the article's claims. [confidence: low]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
