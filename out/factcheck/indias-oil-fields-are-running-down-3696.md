# Fact/interpretation check — indias-oil-fields-are-running-down-3696

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-oil-fields-are-running-down-3696.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 97812, Requested 3192. Please try again in 14m27.456s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "91.8% achieved" (for crude production in FY2024-25) — The article states that 28.70 MMT was achieved against a 31.27 MMT target, which is 91.8%. However, the table in the article shows the target as 31,272 TMT (31.272 MMT) and actual as 28,703 TMT (28.703 MMT), which calculates to 91.78% (28.703/31.272 * 100). Rounding to one decimal place should yield 91.8%, but the exact figure is 91.78%, which is not precisely 91.8%. [confidence: high]

- "11.8% Self-sufficiency in petroleum products" — The article cites this figure for FY2024-25, but the text later clarifies that the correct figure is 11.8% for indigenous crude-based petroleum products as a share of domestic consumption, not overall self-sufficiency in petroleum products. The initial claim conflates these two distinct metrics. [confidence: high]

INTERPRETATION ERRORS:
- "Gas has held up — but only because private deepwater replaced the state fields that were shrinking underneath it." — While the data shows PSC gas production increased from 7.84 to 13.38 BCM, the claim implies a direct replacement of state fields' decline by private deepwater gas. However, the decline in ONGC/OIL gas (21.18 → 18.80 BCM) is not fully offset by PSC gas growth (7.84 → 13.38 BCM), as total gas production only rose from 32.25 to 36.11 BCM. The net increase is modest, and the phrasing overstates the replacement effect. [confidence: high]

- "The refining industry is world-scale, expanding and profitable. It simply runs on other people's oil, and 78.5% of what it processes is high-sulphur crude, which narrows the grades India can realistically substitute toward when it wants to change supplier." — The claim that 78.5% of refined crude is high-sulphur is presented as a constraint on substitution, but the source (PPAC) likely refers to the *share of high-sulphur crude in total crude processed*, not the *share of high-sulphur crude in India's total crude imports*. The interpretation conflates processing capacity constraints with import substitution flexibility, which are distinct issues. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
