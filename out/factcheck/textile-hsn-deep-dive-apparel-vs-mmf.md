# Fact/interpretation check — textile-hsn-deep-dive-apparel-vs-mmf

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/textile-hsn-deep-dive-apparel-vs-mmf.html`

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
- "India is the world's 6th-largest T&A exporter with ~3.9% global share" — The claim about India's global share is unverifiable as the article does not cite a source for this specific percentage. The AEPC Annual Report 2024-25 and PIB references do not explicitly state this figure. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047" — The projection of US$309 bn by 2047 is not sourced or explained. The IBEF Apparel Industry source does not provide such a long-term projection. [confidence: high]

INTERPRETATION ERRORS:
- "The MMF gap is visible inside the 6-digit codes. Nearly every heading forks into '…of cotton' (61xx2), '…of man-made fibres' (61xx3), '…of other'... India's exports concentrate in the cotton lines; the synthetic-fibre lines (610323, 610333, 610343, 610463, 610520, 610620, 611130, 611430…) are underweight against a world where MMF accounts for ~70% of fibre consumption (a fibre-level share, not a garment-purchase share — India's own basket skews the other way, see below)." — The claim that India's synthetic-fibre garment lines are "underweight" compared to global fibre consumption (70%) is misleading because it compares fibre-level consumption (global) with garment-level export composition (India). Garment exports are not a direct reflection of fibre consumption patterns, as they involve value addition, fashion trends, and market demand, not just raw fibre usage. [confidence: high]

- "Trade balance: Apparel = strong surplus · Technical textiles = balanced, deficit in high-tech segments · upstream MMF fabric = deficit (hence the import curbs)." — The article conflates trade balance categories without clarifying that "upstream MMF fabric" imports are part of the broader technical-textiles and MMF supply chain, potentially leading to double-counting or misattribution of deficits. The deficit in upstream MMF fabric is not clearly separated from the technical-textiles trade balance, making the synthesis misleading. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
