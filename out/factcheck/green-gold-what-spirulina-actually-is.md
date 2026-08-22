# Fact/interpretation check — green-gold-what-spirulina-actually-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/green-gold-what-spirulina-actually-is.html`

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
- "A quarter-acre of shallow ponds, harvested every 15–18 days, can out-earn an acre of most row crops" — This claim is unverified and presented as a general truth without supporting evidence or context. The article later notes that the income figures are from "commercial farming guides and trade press, not an audited farm-income survey," making this a factual error due to lack of verification. [confidence: high]

- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in" — While the article later clarifies that South Korea is not a major spirulina grower, the initial phrasing implies a definitive statement about South Korea's role that is not fully supported by the subsequent nuanced discussion. The claim oversimplifies South Korea's actual involvement in microalgae (e.g., Phycoil Biotech Korea's DHA production). [confidence: medium]

INTERPRETATION ERRORS:
- "A batch reaches harvestable density in roughly 15–18 days, against a cereal crop's 90–120-day cycle, so a single pond turns over multiple harvests a season" — While the timeframes are factually correct, the conclusion that this directly translates to higher earnings per acre is an interpretation error. The article does not account for operational costs, market demand, or yield variability, which could significantly impact profitability. The claim assumes a direct correlation between faster growth cycles and higher earnings without evidence. [confidence: high]

- "The scale argument is the whole pitch: a quarter-acre to one-acre pond, requiring far less water than an equivalent area of paddy or sugarcane, can be run by a household without heavy machinery or land consolidation" — This claim conflates lower water and land requirements with economic viability. While spirulina may require less water per kilogram of protein, the statement implies that small-scale household operations are inherently feasible and profitable, which is not substantiated by the article's own caveats about unverified income figures and subsidy dependence. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
