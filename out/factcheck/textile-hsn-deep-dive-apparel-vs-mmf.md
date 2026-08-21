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
- "India is the world's 6th-largest T&A exporter with ~3.9% global share" — The claim about India's global share is unverified and likely incorrect. While India is a major textile exporter, the 3.9% figure is not supported by the cited sources (AEPC Annual Report 2024-25, CITI T&A export statistics, IBEF) and contradicts widely reported data (e.g., WTO trade statistics place India's textile and apparel exports at a higher share). [confidence: high]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047" — The projection of US$309 bn by 2047 is implausible and unsupported. The source (IBEF) does not provide such a long-term projection, and the growth rate implied (from US$29 bn to US$309 bn in ~23 years) is unrealistic for the technical-textiles sector. [confidence: high]

INTERPRETATION ERRORS:
- "The imports that matter sit upstream: MMF fabric and specialty synthetic fabric — hence the Minimum Import Price on 13 synthetic knitted-fabric codes and anti-dumping duties against cheap MMF fabric" — The claim implies a direct causal link between India's import dependence on MMF fabrics and the need for MIP/anti-dumping duties, but it does not establish whether these measures are effective or justified. The article does not provide evidence that the imports are harming domestic industry or that the duties are the appropriate solution. [confidence: medium]

- "India holds only ~4–5% of the global technical-textiles market; technical textiles are just 12–15% of India's textile value chain vs ~50% in advanced economies" — While the figures may be correct, the comparison is an apples-to-oranges issue. The 4–5% global share is likely based on export data, while the 12–15% vs 50% comparison refers to the domestic value chain composition, which are different metrics and not directly comparable. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
