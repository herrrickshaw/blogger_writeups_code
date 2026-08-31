# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "4 August 2026" — The article is dated in the future relative to the current date (2025), making it unverifiable and likely incorrect. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year" — The RBI data in Exhibit 1 shows net services receipts rising from $188.8bn (FY2024-25) to $216.6bn (FY2025-26), a $27.8bn increase, which is correct. However, the article later states "Net services receipts rose $27.8 billion in one year, the largest increase on record," which is unverifiable as no prior record is cited or verifiable. [confidence: medium]

INTERPRETATION ERRORS:
- "The warning signs are elsewhere: net hiring has collapsed from ~450,000 (FY22) to 135,000 (FY26) against a growing revenue base, and chief executives now name 'AI deflation' worth 3–5% of revenue." — The claim correctly notes a decline in net hiring and mentions "AI deflation," but it implies a causal link between AI and the hiring decline without sufficient evidence. The article acknowledges that the displacement has not been measured and cites executive testimony, which is not a causal proof. The reasoning gap is assuming that the hiring slowdown is directly caused by AI without robust data. [confidence: high]

- "So when people ask whether AI threatens Indian IT, the question that matters for the country is narrower and sharper: does it threaten the dollar receipts that make a $337 billion goods deficit survivable at 0.6% of GDP?" — The article correctly highlights the importance of services receipts for India's balance of payments, but it extrapolates from this that the primary concern is AI's threat to dollar receipts without demonstrating that AI is currently reducing these receipts. The reasoning gap is treating the potential future risk as a present reality based on leading indicators and executive statements, rather than measured data. [confidence: high]
