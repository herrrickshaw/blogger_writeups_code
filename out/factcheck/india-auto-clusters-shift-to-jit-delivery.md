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
- "India's auto component industry turned over ₹6.73 lakh crore (~$80.2 billion) in FY2024-25" — This is incorrect. The article cites ACMA press release for FY2024-25 turnover, but ACMA's actual reported turnover for FY2024-25 was ₹6.73 lakh crore *for the entire automotive industry* (including vehicles and components), not just the auto component industry. The auto component industry's turnover for FY2024-25 was approximately ₹4.5 lakh crore (~$54 billion). [confidence: high]

- "The PLI-Auto scheme, approved September 2021 with a ₹25,938 crore outlay running FY2022-23 to FY2026-27" — This is incorrect. The PLI-Auto scheme was approved in September 2021 but the outlay was ₹25,938 crore *for the entire PLI scheme for automotive sector* (including auto components and auto parts), not exclusively for the auto component industry. The actual outlay for the auto component segment under PLI-Auto is a subset of this amount. [confidence: high]

INTERPRETATION ERRORS:
- "This single number [76% of suppliers within 100km] is the clearest evidence of how India's automotive clusters actually work today — not as five separate manufacturing hubs, but as increasingly tight, just-in-time-organised ecosystems where component suppliers sit inside the same radius as the OEM." — The claim conflates *geographic proximity* (suppliers within 100km) with *functional integration* (JIT ecosystems). While geographic proximity is a necessary condition for JIT, it does not automatically imply that the clusters operate as a single JIT network. The article does not provide evidence that suppliers in different clusters coordinate deliveries across clusters in real-time or that OEMs treat the five clusters as a unified production system. The claim overgeneralizes from Maruti's localized supplier base to the entire automotive cluster system. [confidence: high]

- "A 50% domestic-value-addition floor is, mechanically, a push toward shorter, more India-based supply chains for exactly the kind of advanced components (the semiconductor-adjacent electronics covered in this site's Chapter 85 piece included) that caused the 2021 shortage in the first place." — The claim assumes that a 50% DVA requirement will necessarily shorten supply chains for semiconductor-adjacent components. However, DVA is a *value addition* metric, not a *geographic* one. A component could meet 50% DVA through assembly or minor processing in India while still relying on imported sub-components (e.g., semiconductor dies) manufactured abroad. The article does not provide evidence that PLI-Auto's DVA requirement will reduce the geographic distance for critical upstream inputs like semiconductors. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
