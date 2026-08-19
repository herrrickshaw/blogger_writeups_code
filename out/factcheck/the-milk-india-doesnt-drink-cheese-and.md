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
- "India produced an estimated 216.5 million tonnes (MT) of milk in 2025" — The article itself later contradicts this figure, citing 228 million tonnes (2025) and 239.2 million tonnes (2023-24) from CRISIL/APEDA sources. The 216.5 MT figure is inconsistent with other credible sources in the same article. [confidence: high]

- "India's mozzarella exports reached USD 3.29 million in April-September 2025, a year-on-year increase of more than 1,200%" — While the export growth figure is correct, the article incorrectly attributes this to Amul's production capacity expansion, which was a separate ₹200 crore investment. The 1,200% refers to export volume growth, not production capacity. [confidence: high]

INTERPRETATION ERRORS:
- "cheese isn't competing with milk, it's competing for a share of milk that's already leaving the liquid channel, against ghee, paneer and powder that got there first" — While the claim that cheese competes for non-liquid milk is plausible, the article does not provide evidence that cheese is actually displacing other value-added dairy products (like ghee or paneer) in the non-liquid milk pool. The claim assumes substitution without demonstrating it. [confidence: medium]

- "The growth story is mozzarella, and mozzarella's growth story is pizza and QSR chains, not the breakfast table" — While mozzarella's growth is linked to pizza and QSR demand, the article does not establish that this shift has *reduced* demand for traditional cheese formats (e.g., breakfast cubes) or that the breakfast table market has declined. The causal claim is not supported by data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
