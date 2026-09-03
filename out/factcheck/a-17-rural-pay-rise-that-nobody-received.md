# Fact/interpretation check — a-17-rural-pay-rise-that-nobody-received

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-17-rural-pay-rise-that-nobody-received.html`

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
- "The month rural India got a 12.7 per cent raise" — The article claims a 12.7% raise between June and July 2025, but the data shows a jump from ₹454 to ₹511, which is a 12.56% increase (511/454 ≈ 1.1256). The 12.7% figure is incorrect. [confidence: high]

- "VB-G RAM G came into force on 1 July 2026" — The article states this date, but the presidential assent was on 21 December 2025, and the commencement date is likely incorrect or unverified. The source does not explicitly confirm the 1 July 2026 date. [confidence: medium]

INTERPRETATION ERRORS:
- "The newly added regions have smaller agricultural workforces, more concentrated skills, and average wages roughly 50 to 55 per cent above the states in the original sample." — While the claim about higher wages in newly added regions is factually correct, the article implies this alone explains the entire 17% wage growth, ignoring other potential factors like economic activity or policy changes. The reasoning gap is that the article attributes the entire wage growth to the sample change without ruling out other contributing factors. [confidence: high]

- "The same village sample now does two jobs at once." — The article claims the sample change affects both wage reporting and inflation measurement in a way that artificially inflates wages and deflates inflation, but it does not provide evidence that the sample change is the sole or primary driver of these effects. The reasoning gap is that the article assumes the sample change is the dominant factor without isolating its impact from other methodological changes (e.g., geometric mean adoption). [confidence: medium]
