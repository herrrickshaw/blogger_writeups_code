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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99562, Requested 855. Please try again in 6m0.288s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "56 raw PARIVESH status values consolidated into canonical process stages" — The article claims 56 raw status values were consolidated, but the PARIVESH 2.0 API documentation (as of the referenced period) does not explicitly confirm this number. The source link provided does not detail the exact count of raw status values, making this unverifiable. [confidence: medium]

- "Grant rate = granted ÷ decided" — While the formula is mathematically correct, the article does not clarify whether "decided" includes only proposals that reached a final decision (e.g., rejected, withdrawn, returned, or granted) or if it excludes auto-delisted proposals. The PARIVESH data may treat auto-delisted proposals differently, potentially skewing the denominator. [confidence: high]

INTERPRETATION ERRORS:
- "Only 49% of these EC proposals are fresh new projects. The rest are activity on land that already holds a clearance" — The claim implies that 51% of proposals are not "new projects," but the article does not define what constitutes a "fresh new project" versus an "activity on land." Without clear criteria (e.g., whether expansions or transfers are considered new projects), this distinction is arbitrary and unsupported by the data. [confidence: high]

- "The real attrition is auto-delisting (22%) and pipeline backlog (31% of live still pending) - not rejection" — While the percentages are correct, the conclusion that rejection is not a major attrition factor is misleading. The article acknowledges that 6,954 proposals were not approved (including 2,553 rejected), which is ~11.3% of decided proposals. Framing rejection as insignificant ignores its role in the approval funnel. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
