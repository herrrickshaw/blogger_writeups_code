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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98935, Requested 1293. Please try again in 3m16.992s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "17th and 18th Lok Sabha (2019-06-17 → 2026-08-04)" — The 17th Lok Sabha was constituted on **June 17, 2019**, but the 18th Lok Sabha was **not yet constituted as of August 4, 2026** (the date in the article). The 18th Lok Sabha elections were held in April–May 2024, and the new Lok Sabha was formed in June 2024, but the term would not extend to 2026. [confidence: high]

- "Generated 2026-08-04 by scripts/build_pq_registry.py in digital-twin-for-ipa" — The date **August 4, 2026**, is in the future relative to the current date (June 2024). This is likely a placeholder or typo, as the article cannot be generated for a future date. [confidence: high]

INTERPRETATION ERRORS:
- "This registry is the parliamentary companion to the Quarterly Reportage: where the reportage tracks what government announced, this tracks what Parliament asked — and the ministry's answer of record." — While the registry tracks parliamentary questions and answers, it does not inherently establish a **direct causal or comparative relationship** between government announcements and parliamentary questions. The claim implies a systematic linkage that may not exist in practice (e.g., questions may not always correlate with announcements, and answers may not reflect actual policy implementation). [confidence: medium]

- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — The article acknowledges AI limitations but does not clarify **how or why** AI-generated text might misstate figures in this specific context. The warning is generic and does not address potential biases or errors in the registry's construction (e.g., keyword matching flaws or classification bugs). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
