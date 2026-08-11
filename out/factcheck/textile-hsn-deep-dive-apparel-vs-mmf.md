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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98966, Requested 1808. Please try again in 11m8.736s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Total textiles & apparel exports ≈ US$37 bn (FY2024-25, +6% YoY); India is the world's 6th-largest T&A exporter with ~3.9% global share." — The FY2024-25 export figure is likely incorrect or unverifiable. The article cites sources like AEPC Annual Report 2024-25 and DGCI&S, but the US$37 bn figure is not corroborated by official government or industry reports (e.g., AEPC typically reports lower figures for FY2024-25). The global share of ~3.9% is plausible but not directly tied to the US$37 bn claim. [confidence: medium]

- "Domestic market: US$29 bn (FY24) → ~US$45 bn (2026), projected US$309 bn by 2047." — The US$309 bn projection for 2047 is an extreme extrapolation with no clear methodology or source cited. The US$29 bn (FY24) and US$45 bn (2026) figures are also unverified against official projections (e.g., no government or reputable industry source supports a 2047 figure of this magnitude). [confidence: high]

INTERPRETATION ERRORS:
- "India imports very little finished apparel (high duties + domestic supply) — a large structural surplus in Ch 61/62." — While the claim about high duties and domestic supply limiting apparel imports is plausible, the article does not provide data on import volumes or values for Ch 61/62 to substantiate the "large structural surplus" claim. The trade balance for Ch 61/62 is not explicitly quantified in the article, making this conclusion unsupported. [confidence: high]

- "The MMF gap is visible inside the 6-digit codes. Nearly every heading forks into '…of cotton' (61xx2), '…of man-made fibres' (61xx3), '…of other'... India's exports concentrate in the cotton lines; the synthetic-fibre lines [...] are underweight against a world where MMF accounts for ~70% of fibre consumption (a fibre-level share, not a garment-purchase share — India's own basket skews the other way, see below)." — The article correctly notes that India's apparel exports are cotton-skewed, but it conflates fibre consumption (global ~70% MMF) with garment exports (where MMF share is lower). The claim implies a direct comparison between global fibre consumption and India's export basket, which is an apples-to-oranges comparison. The article does not clarify whether the ~70% MMF share refers to global fibre use in apparel or total fibre use (including non-apparel). [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
