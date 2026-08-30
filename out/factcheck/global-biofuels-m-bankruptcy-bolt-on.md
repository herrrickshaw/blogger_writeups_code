# Fact/interpretation check — global-biofuels-m-bankruptcy-bolt-on

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/global-biofuels-m-bankruptcy-bolt-on.html`

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
- "Global Clean Energy Holdings... filed Chapter 11 on 19 April 2025" — The article later states the company emerged from bankruptcy in mid-August 2025, but the filing date is correct as per the restructuring-support agreement details. No factual error found in this claim. [confidence: high]
- "Montana Renewables (owned by Calumet) isn't an M&A story but is the segment's largest capital event of the period: a $1.44 billion US DOE loan guarantee" — The DOE loan guarantee is correct, but the claim that it is the "largest capital event" is unverified and potentially misleading without broader market context. [confidence: medium]

INTERPRETATION ERRORS:
- "renewable diesel is where distressed assets get recapitalized or wiped out; SAF and RNG are where growth capital and strategic buyers are still actively deploying" — This broad generalization lacks nuance. While the article provides specific examples (e.g., Global Clean Energy's bankruptcy, CMA CGM's investment in Vanguard Renewables), it does not establish that this pattern holds universally across all renewable diesel, SAF, and RNG deals. The claim extrapolates from a few cases to an entire industry segment without sufficient evidence. [confidence: high]
- "ethanol consolidation is happening plant-by-plant, not company-by-company" — The article cites specific plant-level transactions (e.g., POET buying Green Plains' plant) but does not rule out broader company-level consolidation in the ethanol sector. The claim implies a universal trend that may not account for other potential consolidation mechanisms (e.g., minority stake acquisitions, joint ventures). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
