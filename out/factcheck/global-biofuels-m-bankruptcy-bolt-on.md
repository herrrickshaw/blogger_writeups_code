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
- "Global Clean Energy's $2.1 billion restructuring" — The article later clarifies that the $2.1 billion refers to "total potential claims," not the restructuring value itself. The restructuring outcome involved lenders taking equity, but the $2.1 billion is not the deal value or restructuring cost. [confidence: high]

- "Montana Renewables (Calumet) — a $1.44 billion US DOE loan guarantee, with a first drawdown of approximately $782 million in February 2025" — The article states the DOE loan guarantee was $1.44 billion, but the first drawdown was $782 million *plus* a further $150 million Calumet equity investment. The phrasing could imply the $782 million was the total drawdown, omitting the additional equity. [confidence: medium]

INTERPRETATION ERRORS:
- "The pattern in one line: renewable diesel is where distressed assets get recapitalized or wiped out; SAF and RNG are where growth capital and strategic buyers are still actively deploying" — While the article provides examples of distress in renewable diesel and growth in SAF/RNG, it does not establish a causal link between the industry segment and the type of capital flow. The claim implies a structural or inherent difference, but the evidence is limited to a few cases and does not rule out other factors (e.g., market conditions, technology maturity, or policy support) driving these outcomes. [confidence: high]

- "ethanol consolidation is happening plant-by-plant, not company-by-company" — The article cites specific plant-level transactions (e.g., POET buying a Green Plains plant) and a single India ownership consolidation (Triveni Engineering's stake in SSEL) as evidence of this pattern. However, the claim generalizes from these examples to the entire ethanol sector without addressing whether these transactions represent broader consolidation trends or are outliers. The reasoning does not account for potential company-level consolidation that may not be captured in the cited deals. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
