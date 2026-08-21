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
- "India produced an estimated 216.5 million tonnes (MT) of milk in 2025" — The article cites multiple credible sources with different figures for India's milk production in 2025 (e.g., 228 million tonnes per CRISIL/APEDA, 239.2 million tonnes for 2023-24). The 216.5 MT figure is not consistent with these sources and appears outdated or incorrect. [confidence: high]

- "Amul having 'expanded mozzarella production capacity by 1,200%'" — The article clarifies that this claim is incorrect; the 1,200% figure refers to mozzarella export volume growth (USD 3.29 million in April-September 2025, a YoY increase of >1,200%), not Amul's production capacity. The original claim conflates export growth with capacity expansion. [confidence: high]

INTERPRETATION ERRORS:
- "cheese isn't competing with milk, it's competing for a share of milk that's already leaving the liquid channel, against ghee, paneer and powder that got there first" — While the claim about cheese competing for non-liquid milk is plausible, the article does not provide evidence that the "pool" of non-liquid milk (75-76 MT) is a fixed or zero-sum resource. The volume of milk diverted to non-liquid products could expand with processing capacity, cold-chain improvements, or demand shifts, meaning cheese's growth does not necessarily come at the expense of other products. [confidence: medium]

- "The growth story is mozzarella, and mozzarella's growth story is pizza and QSR chains, not the breakfast table" — The article correctly notes the dominance of mozzarella in shredded/diced formats and its association with QSRs, but it does not address whether this shift is driven by *new* demand (e.g., pizza consumption) or merely a *reallocation* of existing cheese demand from other formats (e.g., blocks for home graters). Without data on total cheese consumption trends, the causal claim that pizza/QSR growth *causes* mozzarella's rise (rather than reflects a broader cheese market expansion) is unsupported. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
