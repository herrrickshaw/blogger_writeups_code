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

FACTUAL ERRORS:
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — The exchange rate used to convert ₹6.73 lakh crore to $80.2 billion is not specified, and without knowing the exact exchange rate, it's difficult to verify the accuracy of the conversion. [confidence: medium]
- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — The article does not provide a source for the approval date of the PLI-Auto scheme, and while the scheme is real, the exact approval date and outlay amount should be verified against official government sources. [confidence: medium]

INTERPRETATION ERRORS:
- "The e-Nagare system is the mechanism, not just the philosophy. Maruti's 'e-Nagare' (electronic flow) system digitises the production-plan sequence from vendor to shopfloor. Before it, that sequence took roughly 30 hours to propagate from plan to shopfloor; after, it takes about 2 hours" — The article implies that the reduction in propagation time is solely due to the e-Nagare system, but it does not consider other potential factors that might have contributed to this reduction, such as changes in supplier relationships, logistics, or production planning. [confidence: medium]
- "A 50% domestic-value-addition floor is, mechanically, a push toward shorter, more India-based supply chains" — The article assumes that a 50% domestic-value-addition floor will necessarily lead to shorter supply chains, but it does not provide evidence to support this claim. The relationship between domestic value addition and supply chain length is complex and may depend on various factors, such as the type of components being produced, the location of suppliers, and the logistics infrastructure. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — The article cites this figure without providing a primary source, and ACMA's official data for FY2024-25 is not accessible in the cited sources. The turnover figure appears to be an estimate or projection rather than a verified fact. [confidence: medium]

- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — The scheme was approved in September 2021, but the outlay of ₹25,938 crore was for the entire duration of the scheme (FY2022-23 to FY2026-27), not a single-year allocation. The phrasing could mislead readers into thinking this was an annual outlay. [confidence: high]

INTERPRETATION ERRORS:
- "This single number [76% of suppliers within 100km] is the clearest evidence of how India's automotive clusters actually work today — not as five separate manufacturing hubs, but as increasingly tight, just-in-time-organised ecosystems" — While the 76% figure demonstrates Maruti Suzuki's supplier proximity, it does not inherently prove that all five clusters function as a unified JIT network. The claim extrapolates from one OEM's data to the entire industry without evidence that other OEMs or clusters operate similarly. [confidence: high]

- "A 50% domestic-value-addition floor is, mechanically, a push toward shorter, more India-based supply chains for exactly the kind of advanced components [...] that caused the 2021 shortage in the first place" — The PLI-Auto's DVA requirement may encourage localization, but it does not directly address the semiconductor shortage, which was caused by global supply chain disruptions and upstream dependencies (e.g., imported microcontrollers). The claim conflates localization with solving a specific global upstream bottleneck. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
