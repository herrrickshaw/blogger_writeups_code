# Fact/interpretation check — india-has-tax-treaties-with-97

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-tax-treaties-with-97.html`

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
- "India's double-taxation network is nearly universal — 97 countries, built up over six decades, still being amended monthly." — The claim that the network is "nearly universal" is unverifiable without a defined universe of countries (e.g., all UN member states). The article later cites 97 comprehensive DTAAs, but this does not confirm universality. [confidence: medium]

- "the India–UK CETA (signed July 2025)" — The article lists the India–UK CETA as signed in July 2025, but the source (PIB release ID 2236134, 6 March 2026) does not provide a signing date. The claim appears to be an extrapolation beyond the cited source. [confidence: high]

INTERPRETATION ERRORS:
- "The two networks answer different questions — one about where income gets taxed, the other about what tariff a shipment pays — and reading them side by side shows how much further India's trade-agreement reach still has to run to catch its tax-treaty reach." — While the networks serve different purposes (tax jurisdiction vs. tariffs), the conclusion that India's trade-agreement reach "still has to run to catch its tax-treaty reach" assumes that the breadth of coverage (97 countries for DTAAs vs. 38 for FTAs) directly implies a lag in trade integration. This ignores that trade agreements are typically narrower in scope (targeting specific partners for tariff reductions) and may not need to mirror the tax-treaty network. The comparison conflates *coverage* with *relevance* or *depth* of integration. [confidence: high]

- "A country can have a functioning tax relationship with India, in the form of a DTAA governing how income is taxed, for years or decades before any tariff-level trade agreement exists between the two. The US framework announced in February 2026 is the clearest current example: India and the US have had a functioning DTAA since 1990, but as of this article's research have only an interim framework, not a concluded free trade agreement." — While the premise (DTAAs and FTAs serve different purposes) is correct, the implication that the absence of an FTA *necessarily* reflects a lag in trade integration is flawed. The US framework may be a strategic step toward an FTA, but the lack of an FTA could also reflect policy differences (e.g., non-tariff barriers, regulatory alignment) unrelated to the DTAA's existence. The example does not support the causal claim that the DTAA's presence explains the FTA's absence. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
