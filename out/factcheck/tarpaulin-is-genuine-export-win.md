# Fact/interpretation check — tarpaulin-is-genuine-export-win

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/tarpaulin-is-genuine-export-win.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99842, Requested 2081. Please try again in 27m41.472s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is the world's largest exporter of HDPE tarpaulin by shipment count" — The claim cites shipment counts (6,763 for India vs. 991 for Vietnam and 166 for China) but does not specify the time period or data source's recency. The article mentions "Volza trade-data compilations" but does not confirm if these are the latest available figures or if they cover a full calendar year. Without a clear timeframe, the claim is unverifiable. [confidence: medium]

- "The trade numbers back this up. This site's own TradeStat-based segment mapping [...] puts Agrotech at a stable net export surplus: FY2025-26 exports of $193M against imports of $100M" — The article presents these figures as if they are official or widely accepted, but they are explicitly described as "this site's own TradeStat-based 314-code segment mapping" and "a same-methodology proxy, not an official Ministry release." Using non-official, internally generated figures as factual evidence without caveats in the claim itself is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The real import dependency in agriculture-adjacent textiles sits one category over, in geotextiles for canal lining and highway embankments, where Indian MSMEs meet under a third of even flagship national-highway demand." — The claim conflates two different uses of geotextiles: canal lining (agriculture-adjacent) and highway embankments (infrastructure). The article later clarifies that the "less than 30% MSME-fulfilled" figure applies only to National Highway projects, not canal lining specifically. Using the highway figure as a proxy for agriculture-adjacent geotextile import dependency without explicit justification is an apples-to-oranges comparison. [confidence: high]

- "Tarpaulin is the segment India built its own supply chain for, feedstock included. Geotextiles are the segment still being filled in from Germany, the Netherlands, China and South Korea — two products woven from similar-sounding fibres, opposite trade positions." — While the individual facts about tarpaulin exports and geotextile imports may be correct, the causal claim that India "built its own supply chain" for tarpaulin *because* of domestic feedstock availability is not established by the evidence provided. The article mentions duty relief on PE/PP imports and domestic polymer production, but it does not demonstrate that these factors directly caused the supply chain development or export leadership. The conclusion overreaches beyond the cited data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
