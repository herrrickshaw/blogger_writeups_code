# Fact/interpretation check — foreign-capital-found-indias-hospitals

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/foreign-capital-found-indias-hospitals.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "India's hospital beds fall well short of world norms" — The article later clarifies that the "world norms" (e.g., "3.5 beds per 1,000") are not formal WHO minimum standards but approximations of the global average (3.29 in 2021). The initial claim implies a formal standard exists, which is incorrect. [confidence: high]

- "Hospitals have permitted 100 per cent FDI on the automatic route since January 2000" — The article later states that hospitals have been on the 100% automatic route since January 2000, but the phrasing "permitted" could be misinterpreted as a post-2000 policy change, whereas the policy was already in place (as confirmed by DPIIT sources cited later). The claim is technically correct but risks implying a new permission was granted in 2000. [confidence: medium]

INTERPRETATION ERRORS:
- "Foreign hospital investment since 2000 has not moved this ratio [beds per 1,000 population]" — The article correctly notes that FDI inflows have not increased India's bed ratio, but it extrapolates this to imply that *all* foreign capital (including domestic capex) has failed to address the shortage. However, the article later acknowledges a ~30,000-bed capex pipeline (domestic) that could address the gap, meaning the conclusion that "the money that has actually arrived buys the beds that already exist" is an overgeneralization. The FDI-specific claim is accurate, but the broader interpretation conflates FDI with total investment. [confidence: high]

- "If the thesis were 'India needs more beds,' the rational foreign-capital response would be to build them" — The article assumes that foreign investors *should* prioritize greenfield projects to address the bed shortage, but it does not account for the fact that private equity's business model (buying existing assets) is inherently different from greenfield development. While the claim is logically consistent with the data, it misinterprets the *motivation* of investors: PE firms seek returns through operational efficiency, not capacity expansion. The reasoning gap is that the article judges investor behavior against a normative standard (building new beds) rather than their actual objectives. [confidence: high]
