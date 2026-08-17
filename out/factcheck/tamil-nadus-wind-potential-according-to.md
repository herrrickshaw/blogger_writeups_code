# Fact/interpretation check — tamil-nadus-wind-potential-according-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/tamil-nadus-wind-potential-according-to.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99879, Requested 3401. Please try again in 47m13.92s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Energy & Fuels · India Trade & Policy · 14 August 2026" — The date is impossible (August 2026 is in the future as of the current date), and the category "India Trade & Policy" is not a standard section for an economics blog focused on energy/renewables. [confidence: high]

- "Tamil Nadu's installed wind capacity stood at roughly 11,938 MW as of 31 October 2025" — The source cited (RenewableAffairs.com's 2025 state-ranking compilation) is not provided, and the date (October 2025) is in the future relative to the article's publication date (which is incorrectly listed as 14 August 2026). [confidence: medium]

INTERPRETATION ERRORS:
- "The utilisation math. ~11,938 MW installed against NIWE's 33,799 MW 100m-hub-height potential works out to roughly 35% utilisation — meaning nearly two-thirds of NIWE's own assessed onshore potential in India's most mature wind state remains unbuilt." — The calculation assumes that the 33,799 MW figure (based on a 100m hub height) is directly comparable to the installed capacity (which uses modern turbines at higher hub heights). This is an apples-to-oranges comparison because the potential figure understates the true installable capacity at modern hub heights (e.g., 120m or 150m), as acknowledged later in the article. The "two-thirds unbuilt" conclusion is misleading without adjusting for hub height. [confidence: high]

- "Wind alone won't close that gap, but at 35% utilisation of NIWE's own onshore estimate and near-zero offshore development, it's the renewable resource with the most obvious unused headroom in the state's own numbers." — The article conflates "unused headroom" with unbuilt capacity, ignoring that the NIWE's 100m-hub-height estimate is not the true potential at modern hub heights. The claim implies that Tamil Nadu could theoretically install more wind capacity based on the 33,799 MW figure, but this ignores the fact that the same land could yield significantly more capacity at taller hub heights. The "headroom" is overstated. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
