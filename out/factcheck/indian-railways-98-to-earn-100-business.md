# Fact/interpretation check — indian-railways-98-to-earn-100-business

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-railways-98-to-earn-100-business.html`

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
- "The pattern in one line: Railways' near-100% operating ratio isn't a mystery — freight overpays to cover passenger losses that are formally classified as a social obligation, not a business failure — but the accounting system needed to manage that trade-off deliberately, train by train, is the exact reform a 2015 government committee recommended and a 2024 RTI reply shows still hasn't happened." — The article incorrectly states that the 2015 committee recommended reforming the accounting system to manage the trade-off "train by train." The committee's actual recommendation was to switch to a commercial, accrual-based double-entry accounting system to determine the cost of running trains and their viability, not specifically to manage cross-subsidies train by train. [confidence: high]

- "The scale of the underlying loss has been substantial in specific years: CAG reported a loss of about ₹26,388 crore for 2019-20, with the operating ratio that year at 98.36%, up from 97.29% the year before." — The CAG report cited does not state a loss of ₹26,388 crore for 2019-20. The operating ratio figure is correct, but the loss figure appears to be misrepresented or conflated with another metric. [confidence: medium]

INTERPRETATION ERRORS:
- "Freight services cross-subsidise passenger services," and cites NITI Aayog's 2023 finding that freight charges ran almost three times passenger charges as of 2018-19; between 2009 and 2019, freight rates rose 91% while passenger fares rose just 28%. — While the claim about cross-subsidization is factually supported, the interpretation that this is a deliberate and efficient policy choice is an oversimplification. The article does not adequately address whether the cross-subsidy is optimal or sustainable, nor does it consider the broader economic inefficiencies or distortions this system may create. [confidence: high]

- "Railways' own internal revenue, forecast at ₹3,02,100 crore for the year, funds working expenses and little else." — The article implies that internal revenue is insufficient for capital expenditure, but it does not clearly distinguish between revenue sources or explain how internal revenue is allocated. The claim that internal revenue "funds working expenses and little else" is an interpretation that may not fully account for the complexity of Railways' financial structure or the role of budgetary support. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
