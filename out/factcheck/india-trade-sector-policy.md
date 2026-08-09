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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99711, Requested 1992. Please try again in 24m31.392s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹1.97 lakh cr forex saved" — The claim about forex savings from ethanol blending is unverifiable as stated. While ethanol blending can reduce import dependence, the specific figure of ₹1.97 lakh crore is not a standard or widely recognized metric in official government reports or reputable economic analyses. The source of this figure is not provided, and it cannot be independently verified against known data (e.g., from the Ministry of Petroleum or NITI Aayog). [confidence: high]

- "Odisha #2 with 0.14% of FDI" — The claim that Odisha ranks #2 in implemented industrial investment (2021–2025) with only 0.14% of FDI is highly implausible. Odisha is a major mineral-rich state with significant industrial activity (e.g., steel, mining), and such a low percentage would contradict its known economic profile. The figure likely misrepresents the data or is taken out of context (e.g., possibly referring to a subset of FDI rather than total industrial investment). [confidence: high]

INTERPRETATION ERRORS:
- "DPIIT attributes inflow to the recipient company's registered office, not the project site — with no published caveat" — This claim suggests a causal or systemic issue with FDI attribution, but it does not logically follow that the lack of a published caveat invalidates the data or implies misrepresentation. The DPIIT's methodology may be standard practice (e.g., attributing FDI to the legal entity's location rather than the project site), and the absence of a caveat does not inherently indicate a problem. The interpretation conflates methodological convention with data quality without evidence. [confidence: high]

- "FY2025-26 verdict re-run — trade impact dashboard — All 10 verdicts re-run on FY2025-26 FDI (both former greens fell; Pharma took the green slot)" — The claim that "former greens fell" and Pharma "took the green slot" implies a shift in trade performance, but the methodology for re-running "verdicts" is not explained. Without clarity on how "greens" (presumably sectors flagged as performing well) are defined or recalculated, the conclusion that Pharma "took the green slot" is unsupported. This is an apples-to-oranges comparison if the criteria for "green" changed between runs. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
