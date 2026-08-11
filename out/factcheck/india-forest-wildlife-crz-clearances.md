# Fact/interpretation check — india-forest-wildlife-crz-clearances

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-forest-wildlife-crz-clearances.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99461, Requested 1676. Please try again in 16m22.367999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "the entire national industrial land bank shows ~253,720 developed-and-vacant acres" — The claim is unverifiable as the source (Industrial Information & Land Bank) is not provided, and the figure appears to be a direct quote without citation. [confidence: medium]

- "MAHESH NAIR (likely a data-entry artifact — an individual's name, not an agency)" — The article assumes the name "MAHESH NAIR" is a data-entry error without providing evidence or a primary source to confirm this claim. [confidence: medium]

INTERPRETATION ERRORS:
- "Forest diversion adds ~122,666 more acres of granted land-use change — a different channel (mining, linear infra, hydro), on a different clock." — The claim implies that all forest diversions are for mining, linear infrastructure, or hydro projects, but the data does not specify the project types. The interpretation extrapolates beyond what the data shows. [confidence: high]

- "Wildlife (10.7% granted) is the real bottleneck: 4,319 of 4,919 sit in process, most 'Pending at Proponent' (the ball is with the project applicant, not the regulator) — projects near protected areas stall here for the National/State Board for Wildlife recommendation." — While the grant rate is low, the article conflates the "in process" status with a bottleneck caused by project applicants ("Pending at Proponent"). The data does not explain why applications are pending, and the interpretation assumes a causal link without evidence. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
