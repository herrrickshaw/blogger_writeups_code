# Fact/interpretation check — the-milk-india-doesnt-drink-cheese-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-milk-india-doesnt-drink-cheese-and.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India produced an estimated 216.5 million tonnes (MT) of milk in 2025" — The article cites multiple conflicting figures for India's milk production (216.5 MT, 228 MT, and 239.2 MT for 2025/2023-24), and the 216.5 MT figure is not the most recent or authoritative one. [confidence: high]

- "India's mozzarella exports reached USD 3.29 million in April-September 2025, a year-on-year increase of more than 1,200%" — The 1,200% figure refers to export growth, not Amul's production capacity expansion, which was incorrectly conflated in the claim. [confidence: high]

INTERPRETATION ERRORS:
- "cheese isn't competing with milk, it's competing for a share of milk that's already leaving the liquid channel, against ghee, paneer and powder that got there first" — While cheese competes for non-liquid milk, the article does not provide evidence that cheese is *actually* displacing other products (e.g., ghee or paneer) in the non-liquid milk pool. The claim assumes competition without demonstrating substitution or market dynamics. [confidence: medium]

- "The growth story is mozzarella, and mozzarella's growth story is pizza and QSR chains, not the breakfast table" — The article correctly identifies mozzarella's dominance and QSR-driven demand but does not quantify the relative decline of breakfast cheese (e.g., processed cheese cubes) or prove that QSR growth is the *sole* driver of mozzarella's expansion. The causal claim is overstated. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
