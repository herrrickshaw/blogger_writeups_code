# Fact/interpretation check — india-ec-approval-funnel-parivesh-20

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-ec-approval-funnel-parivesh-20.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99490, Requested 855. Please try again in 4m58.08s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Only 49% of these EC proposals are fresh new projects" — The article claims that 49% of proposals are fresh new projects, but the data provided does not support this. The text states that 54,406 grants are issued out of 113,970 proposals, but it does not explicitly state that 49% of these are fresh projects. The 49% figure appears to be an unsupported assertion. [confidence: high]

INTERPRETATION ERRORS:
- "Grant rate of DECIDED proposals: 88.7%" — The article calculates the grant rate as 88.7% (54,406 granted out of 61,360 decided), but this interpretation may be misleading. The "decided" category includes proposals that are rejected, withdrawn, or returned, which are not necessarily "decided" in the sense of being evaluated for approval. The grant rate should ideally be calculated only among proposals that have undergone full appraisal, not those auto-delisted or withdrawn. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
