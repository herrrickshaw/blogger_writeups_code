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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99547, Requested 911. Please try again in 6m35.712s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "17th and 18th Lok Sabha (2019-06-21 → 2026-08-04)" — The 17th Lok Sabha's term ended in 2024 (elected in 2019, dissolved in 2024), and the 18th Lok Sabha was elected in 2024. The date range "2019-06-21 → 2026-08-04" is incorrect because it implies the 18th Lok Sabha will last until 2026, which is not the case. [confidence: high]

- "Generated 2026-08-04 by scripts/build_pq_registry.py in digital-twin-for-ipa" — The date "2026-08-04" is in the future relative to the current date (2023), making it an impossible date for generation. [confidence: high]

INTERPRETATION ERRORS:
- "This registry is the parliamentary companion to the Quarterly Reportage: where the reportage tracks what government announced, this tracks what Parliament asked — and the ministry's answer of record." — The claim implies a direct complementary relationship between the two datasets (what government announced vs. what Parliament asked), but it does not establish whether the questions asked in Parliament actually reflect oversight or scrutiny of the announcements. The registry may capture questions about announcements, but it does not inherently demonstrate a causal or oversight link between the two. [confidence: medium]

- "Questions are classified by the same scheme-keyword map, so the two views filter identically." — The claim suggests that the classification system ensures identical filtering between the registry and the Quarterly Reportage, but it does not address potential inconsistencies in how keywords or schemes are applied across the two datasets. The method section mentions a "scheme-regex map" and "acronym-veto list," but the claim does not acknowledge potential discrepancies in classification logic or human error in mapping. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
