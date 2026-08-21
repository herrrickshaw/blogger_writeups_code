# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

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
- "India now has one live nationwide fuel-blending mandate (E20 petrol)" — The article incorrectly states that E20 petrol is a live nationwide mandate. As of the article's publication date (19 August 2026), E20 petrol is only a voluntary standard (IS 17021) and not a nationwide mandate. The government had not yet mandated E20 nationwide, despite earlier discussions. [confidence: high]

- "SAF in ATF ... from 2027" — The article claims India's SAF mandate starts in 2027, but this is incorrect. The mandate timeline is already set: 1% from January 2025, 2% from January 2026, and 5% from January 2030, as per ICAO CORSIA Phase II and India's own policy alignment. The article misdates the start by two years. [confidence: high]

INTERPRETATION ERRORS:
- "the Compressed Biogas Blending Obligation (CBO), approved by the National Biofuels Coordination Committee, mandates CBG blending into the CNG (transport) and PNG (domestic) streams of city gas distribution starting at 1% of consumption in FY2025-26, rising to 3% in FY2026-27, 4% in FY2027-28 and 5% from FY2028-29 onward" — The article uses the CBO blending schedule to claim that CBG blending "is metered into the same pipeline network and sold at the same per-kilogram CNG price," implying no cost impact. However, the blending obligation applies to *consumption*, not supply, and the cost of CBG is typically higher than fossil CNG due to production costs. The blending mandate may require blending more expensive CBG into the supply, which could still result in a price premium for consumers, even if it is not directly visible as a mileage loss. The article conflates the lack of mileage penalty with no cost impact at all. [confidence: medium]

- "the MC²+ Grand Butanol Challenge ... Applications closed 15 August 2026" — The article presents the challenge as a forward-looking initiative to develop bio-based isobutanol supply, but it does not acknowledge that the challenge's timeline (applications closed 15 August 2026) is after the article's publication date (19 August 2026). This creates a logical inconsistency: the article discusses the challenge as if it were ongoing or completed, but the application deadline had already passed by the time of publication. This undermines the article's projection about supply readiness for the proposed 2027 mandate. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
