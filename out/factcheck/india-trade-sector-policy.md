# Fact/interpretation check — india-trade-sector-policy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-trade-sector-policy.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99416, Requested 1670. Please try again in 15m38.304s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "the $333bn deficit (current TradeStat running total is closer to $334.3bn)" — The claim conflates a specific figure ($333bn) with a "running total" ($334.3bn) without clarifying whether the latter is an updated, verified figure or a preliminary estimate. TradeStat data is typically revised, and the article does not provide a source or date for the $334.3bn figure, making it unverifiable as a factual correction. [confidence: medium]

- "₹1.97 lakh cr forex saved" — The claim attributes forex savings to PIB-verified ethanol blending but does not provide a source, methodology, or breakdown for how this figure was calculated. Without a cited government document or official report, the claim cannot be verified. [confidence: high]

INTERPRETATION ERRORS:
- "DPIIT attributes inflow to the recipient company's registered office, not the project site — with no published caveat" — The claim suggests a flaw in DPIIT's methodology by implying that attributing FDI to the registered office (rather than the project site) is inherently misleading. However, this attribution method is standard practice in FDI tracking (as FDI is legally tied to the recipient company's domicile, not the project location). The article does not explain why this practice is problematic or how it misrepresents FDI flows. [confidence: high]

- "FDI equity counts pure share purchases; no greenfield/brownfield split exists anywhere" — The claim implies that the lack of a greenfield/brownfield split in FDI data is a deficiency, but it does not acknowledge that equity FDI (as reported by DPIIT/RBI) is inherently distinct from greenfield/brownfield investments (which are tracked separately in other datasets). The article does not explain why the absence of this split in equity FDI data is problematic or how it affects the analysis. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
