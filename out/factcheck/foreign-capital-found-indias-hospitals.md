# Fact/interpretation check — foreign-capital-found-indias-hospitals

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/foreign-capital-found-indias-hospitals.html`

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

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Hospitals have permitted 100 per cent FDI on the automatic route since January 2000" — The correct phrasing should be "Hospitals have been open to 100 per cent automatic-route FDI since January 2000" (as stated earlier in the article). The verb "permitted" is incorrect; the policy is about openness, not permission. [confidence: high]

- "India's hospital beds fall well short of world norms" — The article later clarifies that the "3.5" figure often cited is not a formal WHO minimum standard but rather approximates the global average (3.29 in 2021). The claim that India falls short of "world norms" is misleading because there is no formal WHO norm; it should specify that India falls short of the global average. [confidence: high]

INTERPRETATION ERRORS:
- "Foreign hospital investment since 2000 has not moved this ratio [hospital beds per 1,000 population]." — The article correctly notes that FDI inflows have primarily gone into buying existing hospital chains rather than building new capacity, and the bed ratio has not improved. However, the conclusion that this proves FDI has "not moved this ratio" is an overstatement. The bed ratio is influenced by multiple factors (e.g., population growth, government spending, domestic investment), and the absence of FDI-driven greenfield projects is only one variable. The claim implies a direct causal link between FDI and the bed ratio, which is not supported by the data. [confidence: high]

- "If the thesis were 'India needs more beds,' the rational foreign-capital response would be to build them." — While the article correctly highlights that foreign capital has focused on roll-ups rather than greenfield projects, the claim that building new hospitals would be the "rational" response assumes that foreign investors are primarily motivated by addressing capacity shortages. In reality, private equity firms prioritize returns, speed, and cost efficiency, which favor acquisitions over greenfield projects. The reasoning gap is that the article conflates the *stated need* (more beds) with the *investor's objective* (profit maximization), which may not align. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
