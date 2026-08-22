# Fact/interpretation check — where-india-actually-burns-its-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-india-actually-burns-its-fuel.html`

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
- "Published 8 August 2026 · v1.0.0" — The article claims a publication date of 8 August 2026, but the PPAC workbook data cited (FY2024-25) would not be available until after the fiscal year ends (March 2025), making a 2026 publication date implausible. The PPAC website itself typically lags in publishing such data by several months. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The PNGRB (Petroleum and Natural Gas Regulatory Board) does not publish data with dates in the future (e.g., 31.05.2026). The latest available data would be from May 2025 or earlier. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is the finding hiding in the slow column. The capital’s fuel sales grew 22% in sixteen years — a period in which its vehicle stock multiplied. The explanation is substitution, not stagnation: Delhi runs India’s densest gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count — a metro carrying millions of trips, and the country’s most aggressive vehicle-age rules." — While the substitution effect (CNG, metro, vehicle rules) is plausible, the article does not provide quantitative evidence to decompose the 22% growth in fuel sales. Without controlling for population growth, vehicle stock changes, or cross-border fuel purchases (e.g., Haryana-Delhi VAT leakage), the causal claim that these policies *alone* explain the slow growth is unsupported. The article acknowledges VAT leakage but does not adjust for it. [confidence: high]

- "The frontier moved east; the plateau is scattered across the rest of the map" — The article attributes rapid growth in eastern states (Odisha, Chhattisgarh) to "late motorisation compounding on top of mining and industrial freight," but the data only shows growth rates, not causality. The interpretation assumes that mining/industrial activity *caused* the growth without controlling for other factors (e.g., policy incentives, infrastructure development, or demographic shifts). The claim conflates correlation with causation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
