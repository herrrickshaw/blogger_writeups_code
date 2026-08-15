# Fact/interpretation check — india-forest-wildlife-crz-clearances

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-forest-wildlife-crz-clearances.html`

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
- "Grant rate = granted ÷ (granted + in-process)" — This claim is incorrect because the article later states that the grant rate is calculated as "granted ÷ (granted + dead)", excluding 'in-process' and including 'dead' (rejected/withdrawn/returned) applications, but then also mentions that 'dead' and 'delisted' are excluded from the denominator, which seems to be the actual method used. [confidence: medium]
- None other found.

INTERPRETATION ERRORS:
- "Forest Clearance is a second land-creation channel" — This claim may be misleading because it implies that Forest Clearance directly creates new land, whereas it actually involves the diversion of existing forest land for other uses, which is a different concept. [confidence: high]
- None other found.

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "generated 2026-07-22" — The date is in the future (2026) relative to the current year (2023), making it unverifiable and likely incorrect. [confidence: high]

- "the entire national industrial land bank shows ~253,720 developed-and-vacant acres (Industrial Information & Land Bank, retrieved 2026)" — The cited source retrieval date (2026) is in the future, which is impossible and undermines the credibility of the figure. [confidence: high]

INTERPRETATION ERRORS:
- "Forest Clearance is a second land-creation channel" — The claim implies that Forest Clearance creates land, which is misleading. Forest Clearance is about diverting forest land for non-forest use (e.g., industrial projects), not creating new land. The term "land-creation" inaccurately frames the process as generating land rather than reallocating it. [confidence: high]

- "Forest diversion adds ~122,666 more acres of granted land-use change — a different channel (mining, linear infra, hydro), on a different clock." — While the statement is factually correct about the types of projects, it incorrectly suggests that these diversions are additive to the industrial land bank in a meaningful way. The granted land-use change is not "new" land but a reclassification of existing forest land, and the comparison to the industrial land bank is an apples-to-oranges comparison because the latter refers to developed-and-vacant land, not forest land. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
