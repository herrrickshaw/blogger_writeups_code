# Fact/interpretation check — indias-state-incentive-war-gujarats

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-state-incentive-war-gujarats.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹0 ACC Battery Storage PLI disbursed of an ₹18,100cr outlay, as of 31 Dec 2025" — The article claims ₹0 disbursement for ACC Battery Storage PLI as of 31 Dec 2025, but the source (PIB PRIDs) indicates that disbursement is deferred until a year after commissioning (~30GW already commissioned). The ₹0 figure is a design feature, not an execution failure. [confidence: high]

- "Maharashtra is both #3 by implementation and #1 by FDI (32.5% of the national cumulative total)" — The article incorrectly states Maharashtra is #3 by implementation. The data shows Maharashtra is #3 by FDI share (32.5%) but ranks #4 by implementation share (12.2%), behind Gujarat (33.8%) and Odisha (17.2%). [confidence: high]

INTERPRETATION ERRORS:
- "Karnataka: 22.8% of FDI, 2.2% of implemented investment — the sharpest inversion in the data" — The article presents Karnataka's FDI share (22.8%) and implementation share (2.2%) as evidence of a stark inversion, implying a causal link between high FDI and low implementation. However, the FDI data is distorted by registered-office attribution (e.g., software/services firms registered in Karnataka but operating elsewhere), while implementation data reflects actual factory investments. The inversion is largely an artifact of FDI measurement, not a meaningful economic contrast. [confidence: high]

- "Odisha is the starkest case: 17.2% of India's implemented industrial investment on just $212 million of cumulative FDI — 0.08% of the national FDI total over the same five years. Its investment is almost entirely domestic capital (steel, metals, refining) landing and getting built, not foreign money." — The article uses Odisha's high implementation share and low FDI share to argue that its investment is "almost entirely domestic." However, the FDI data is unreliable due to registered-office attribution (e.g., domestic projects like Tata's Assam semiconductor project are invisible in FDI statistics), and the implementation data does not distinguish between domestic and foreign capital. The conclusion overreaches by conflating low FDI with domestic investment. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
