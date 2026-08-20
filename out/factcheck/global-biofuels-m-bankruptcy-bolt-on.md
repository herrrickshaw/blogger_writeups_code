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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Global Clean Energy Holdings ... filed Chapter 11 on 19 April 2025 in the Southern District of Texas" — The article later contradicts this by stating the company emerged from bankruptcy in "mid-August 2025," which would imply a filing date earlier than April 19, 2025, to allow for a ~4-month bankruptcy process. The exact filing date is unverified in the provided text. [confidence: medium]

- "Montana Renewables ... funding an expansion (called MaxSAF) toward roughly 300 million gallons/year of SAF capacity by 2028 — about half of that online by 2026" — The claim that "half of that [300 million gallons/year] would be online by 2026" is an extrapolation not supported by the $782 million first drawdown in February 2025 and $150 million equity investment alone. No source in the article provides a timeline for capacity additions. [confidence: high]

INTERPRETATION ERRORS:
- "The pattern in one line: renewable diesel is where distressed assets get recapitalized or wiped out; SAF and RNG are where growth capital and strategic buyers are still actively deploying" — This claim generalizes from a few examples (Global Clean Energy, XCF Global, CMA CGM/Vanguard) to the entire industries of renewable diesel, SAF, and RNG. The article does not provide sufficient evidence to support that these patterns apply broadly across these sectors. [confidence: high]

- "World Energy's SAF-producing refinery in Paramount, California ... had reportedly gone four months without producing SAF at all" — The article presents this as a distress signal but does not establish a causal link between Air Products' termination of the expansion funding agreement and the reported production halt. The lack of production could be due to other factors (e.g., operational issues, feedstock shortages), and the article does not verify the cause. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
