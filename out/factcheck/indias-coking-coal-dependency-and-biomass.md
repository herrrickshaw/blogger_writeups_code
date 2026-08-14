# Fact/interpretation check — indias-coking-coal-dependency-and-biomass

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coking-coal-dependency-and-biomass.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 5812, Requested 7742. Please try again in 7.77s. Need more tokens? Upgrade to Dev Tier today at https://]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" when the correct reference period should be December 2024 (as the article itself later uses FY2024-25 data). The 35 MT figure for 2022-23 is correct, but the December 2025 date is inconsistent with the article's own timeline. [confidence: high]

- "140 MT Mission Coking Coal's domestic production target for FY2029-30" — While the article cites this figure from the Ministry of Coal's Year End Review, it does not clarify whether this target is for raw coking coal or washed coking coal. The distinction is critical because Mission Coking Coal's focus includes washery capacity expansion, and raw vs. washed coal volumes are not directly comparable. [confidence: medium]

INTERPRETATION ERRORS:
- "The result is a stark asymmetry: while India is broadly self-sufficient in the iron ore that goes into steel, it imports an estimated 90% of the coking coal that goes in alongside it, making coking coal the single most expensive raw material in Indian steel production." — The claim implies a direct causal link between import dependence and cost without accounting for domestic production costs, logistics, or quality differences. India's iron ore may be "broadly self-sufficient," but its domestic iron ore is often low-grade (e.g., high alumina content), which may offset any cost advantage from self-sufficiency. The comparison does not control for these variables. [confidence: high]

- "The Ministry states this [stamp-charging technology] raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — While the Ministry's claim is plausible, the article does not verify whether the 30% domestic-coal share in the blend actually reduces the *volume* of imported coking coal. The substitution could be offset by increased total coking coal demand (e.g., if steel production grows), leaving import volumes unchanged. The interpretation assumes a direct substitution effect without evidence of net import reduction. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
