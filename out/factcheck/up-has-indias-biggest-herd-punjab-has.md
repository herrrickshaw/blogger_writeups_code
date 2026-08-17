# Fact/interpretation check — up-has-indias-biggest-herd-punjab-has

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/up-has-indias-biggest-herd-punjab-has.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99615, Requested 3828. Please try again in 49m34.752s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "53.68cr India's total livestock population, 20th Livestock Census (2019)" — The correct figure is 536.76 million (53.676 crore), not 53.68 crore. The article rounds incorrectly. [confidence: high]

- "247.87 MT Milk production, 2024-25 — up 3.58% year-on-year, per BAHS 2025" — The article does not specify the unit "MT" (million tonnes) in the claim itself, but the context implies it. However, the claim is accurate as per the cited source (DAHD Basic Animal Husbandry Statistics 2025). No error found here. [confidence: high]

INTERPRETATION ERRORS:
- "Uttar Pradesh's position holds on raw output: it produces 15.66% of India's milk, more than any other state, consistent with its lead in cattle-plus-buffalo population." — While the claim about Uttar Pradesh's milk production share is factually correct, the article implies a causal link between herd size and milk production share without acknowledging that yield per animal (efficiency) also plays a significant role. The reasoning gap is that herd size alone does not fully explain milk production share; yield per animal is a critical factor, as shown in Exhibit 2 (e.g., Punjab's high yield despite smaller herd size). [confidence: high]

- "The livestock-population count, however current, only measures the first of these." — This claim is accurate, but the article does not sufficiently emphasize that the 2019 census data is outdated and cannot reflect recent growth or changes in herd distribution. The reasoning gap is that the article does not clearly state that using 2019 census data to explain current production dynamics is flawed due to the time lag, even if the general point about population counts measuring only one aspect is correct. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
