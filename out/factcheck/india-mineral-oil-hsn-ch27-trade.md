# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99732, Requested 3718. Please try again in 49m40.8s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The article claims this figure is for FY25-26 H1, but the data source (PPAC Ready Reckoner) likely refers to FY2025-26 full-year data, not half-year. The abbreviation "H1" is misleading here. [confidence: high]

- "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" — The claim that Chapter 27 imports represent 26.2% of all imports lacks a clear definition of "all imports." If "all imports" refers to total merchandise imports, the percentage seems unusually high for a single HS chapter (typically far lower). The source does not provide a breakdown to verify this claim. [confidence: medium]

INTERPRETATION ERRORS:
- "80 : 20 Trade Parity Price = IPP : EPP weight" — The article states that the Trade Parity Price (TPP) formula uses an 80:20 weight between IPP (Import Parity Price) and EPP (Export Parity Price), but this is a misinterpretation. The correct formula is TPP = 0.80 × IPP + 0.20 × EPP, not a direct 80:20 ratio of IPP to EPP. The phrasing implies a ratio between the two components, which is incorrect. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas." — The claim suggests that the Kirit Parikh Committee (2023) formula ties gas pricing directly to the Indian crude basket, but this is an oversimplification. The committee's recommendations for gas pricing (e.g., APM gas) are not solely anchored to the crude basket but include other factors like cost-recovery mechanisms and field-specific caps. The statement conflates different pricing regimes (e.g., APM vs. non-APM gas). [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
