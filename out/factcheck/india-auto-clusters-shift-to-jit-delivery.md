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
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — The exchange rate used to convert ₹6.73 lakh crore to $80.2 billion is not specified, and without knowing the exact exchange rate used, it's difficult to verify the accuracy of the conversion. [confidence: medium]
- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — The article does not provide a source for the approval date of the PLI-Auto scheme, and while the scheme is real, the exact approval date and outlay amount should be verifiable. [confidence: medium]

INTERPRETATION ERRORS:
- "The e-Nagare system is the mechanism, not just the philosophy. Maruti's 'e-Nagare' (electronic flow) system digitises the production-plan sequence from vendor to shopfloor. Before it, that sequence took roughly 30 hours to propagate from plan to shopfloor; after, it takes about 2 hours" — The article implies that the reduction in propagation time is solely due to the e-Nagare system, but it does not consider other potential factors that could have contributed to this reduction, such as changes in production planning or vendor management. [confidence: medium]
- "A 50% domestic-value-addition floor is, mechanically, a push toward shorter, more India-based supply chains" — The article assumes that a 50% domestic-value-addition floor will necessarily lead to shorter supply chains, but it does not provide evidence to support this claim, and it is possible that other factors, such as the complexity of the supply chain or the availability of domestic suppliers, could affect the outcome. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — The article cites this figure without a clear primary source, and it conflicts with ACMA's reported turnover for FY2024-25 (which is typically around ₹5.5–6 lakh crore). The $80.2 billion conversion also appears inconsistent with the INR figure. [confidence: high]

- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — The PLI-Auto scheme was actually approved in September 2021 but the outlay was ₹57,042 crore (not ₹25,938 crore), as per the official Ministry of Heavy Industries notification. [confidence: high]

INTERPRETATION ERRORS:
- "This single number [76% of Maruti Suzuki’s suppliers within 100km] is the clearest evidence of how India's automotive clusters actually work today — not as five separate manufacturing hubs, but as increasingly tight, just-in-time-organised ecosystems" — The claim conflates proximity (76% within 100km) with functional integration into a JIT network. While proximity is necessary for JIT, it does not by itself prove that all these suppliers are part of a coordinated, real-time JIT system. The article cites Maruti’s e-Nagare system as evidence of such integration, but the 76% figure alone does not establish systemic JIT operation across clusters. [confidence: high]

- "A 50% domestic-value-addition floor [under PLI-Auto] is, mechanically, a push toward shorter, more India-based supply chains for exactly the kind of advanced components... that caused the 2021 shortage" — The interpretation assumes that increasing DVA will necessarily shorten supply chains for semiconductor-adjacent components. However, DVA does not directly reduce geographic distance unless components are also localized near OEMs. Many high-value components (e.g., semiconductors) may still be imported even with 50% DVA if assembly or testing is done in India, leaving the JIT radius unchanged. The causal link between DVA and reduced supply chain distance is not established. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
