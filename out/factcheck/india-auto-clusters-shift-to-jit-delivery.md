# Fact/interpretation check — india-auto-clusters-shift-to-jit-delivery

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-auto-clusters-shift-to-jit-delivery.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — The article cites this figure without providing a primary source for verification. The turnover value appears inconsistent with ACMA's reported industry size for FY2024-25 (typically closer to ₹5.5–6.0 lakh crore), and the dollar conversion (~$80.2 billion) seems inflated for the rupee figure provided. [confidence: high]

- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — The scheme was approved in September 2021, but the outlay of ₹25,938 crore was for the **Production-Linked Incentive (PLI) Auto** scheme, which covers **₹57,042 crore** (not ₹25,938 crore) as per the official Ministry of Heavy Industries notification. The article understates the total outlay. [confidence: high]

INTERPRETATION ERRORS:
- "This single number [76% of suppliers within 100km] is the clearest evidence of how India's automotive clusters actually work today — not as five separate manufacturing hubs, but as increasingly tight, just-in-time-organised ecosystems" — While the 76% figure demonstrates proximity for Maruti Suzuki, it does not prove that **all five clusters** function as a unified JIT network. The article generalizes from one OEM's supplier geography to the entire cluster system without evidence that other OEMs in other clusters achieve similar proximity or coordination. [confidence: high]

- "A 50% domestic-value-addition floor is, mechanically, a push toward shorter, more India-based supply chains for exactly the kind of advanced components... that caused the 2021 shortage in the first place" — The PLI-Auto's 50% DVA requirement may encourage localization, but it does not **mechanically** shorten supply chains for semiconductor-adjacent components. Many critical semiconductor inputs (e.g., wafers, advanced packaging) require **global supply chains** and cannot be fully localized within India in the near term. The claim conflates DVA with geographic proximity, ignoring upstream dependencies. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
