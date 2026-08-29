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

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The article claims crude imports for FY2025-26 H1 (first half) were 121.1 million metric tonnes (MMT), but this figure is inconsistent with known data. India's total crude imports for FY2024-25 were approximately 270 MMT, implying H1 imports would be around 135 MMT, not 121.1 MMT. The figure appears to be an underestimate. [confidence: high]

- "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" — The article states Chapter 27 imports for FY2025-26 were $203.4 billion, but this conflicts with the earlier per-partner data showing Russia ($47.8B), UAE ($24.3B), USA ($17.3B), and China ($0.3B) summing to $89.7B, which is far below $203.4B. The total is likely overstated. [confidence: high]

INTERPRETATION ERRORS:
- "80 : 20 Trade Parity Price = IPP : EPP weight" — The article claims the Trade Parity Price (TPP) formula uses an 80:20 weight between Import Parity Price (IPP) and Export Parity Price (EPP), but this is misleading. The actual formula is TPP = 0.80 × IPP + 0.20 × EPP, which does not imply a direct 80:20 ratio in the sense of a balanced trade parity but rather a weighted average where IPP dominates. The phrasing suggests a symmetric trade-off, which is incorrect. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas." — The article implies that the Kirit Parikh 2023 formula for gas pricing is directly anchored to the Indian crude basket, but this is an oversimplification. While gas pricing reforms may reference crude prices, the actual APM (Administered Pricing Mechanism) gas pricing formula is more complex and includes factors like inflation adjustments and field-specific costs, not a direct crude basket linkage. The claim conflates different pricing mechanisms. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
