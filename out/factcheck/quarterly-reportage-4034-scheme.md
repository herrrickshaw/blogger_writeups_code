# Fact/interpretation check — quarterly-reportage-4034-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/quarterly-reportage-4034-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99421, Requested 904. Please try again in 4m40.8s. Need more tokens? Upgrade to Dev Tier today at https://]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Quarters are calendar quarters, so 2026Q3 is Jul–Sep 2026" — The claim incorrectly defines 2026Q3 as July–September 2026. In standard fiscal/quarterly reporting (including India's), Q3 typically refers to October–December (Q1: Jan–Mar, Q2: Apr–Jun, Q3: Jul–Sep, Q4: Oct–Dec). The article's definition contradicts common usage. [confidence: high]

- "Thirty-two such rows were removed on 2026-08-04 by an explicit veto list" — The date "2026-08-04" is in the future relative to the article's publication date (4 August 2026), making this claim unverifiable or potentially a placeholder. [confidence: high]

INTERPRETATION ERRORS:
- "A release qualifies as an announcement here if its title matches the scheme-keyword map, or if it is a Cabinet/CCEA approval carrying incentive language" — The method conflates two distinct criteria for inclusion (keyword matching vs. incentive language in approvals) without clarifying how conflicts are resolved (e.g., a Cabinet approval with no incentive language but matching a keyword). This risks double-counting or omitting releases inconsistently. [confidence: medium]

- "Use it to find the release, then read the release" — While the disclaimer acknowledges mapping limitations, the framing implies the index is reliable for locating relevant releases, which may mislead users into assuming the mapping is accurate for all purposes (e.g., policy tracking). The lack of transparency about false positives/negatives (e.g., "Krishi Unnati Mela" vs. "UNNATI 2024") undermines this claim. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
