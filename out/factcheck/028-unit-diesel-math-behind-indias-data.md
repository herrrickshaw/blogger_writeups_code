# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

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

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“Indus Towers … has already converted its 50,000th cell site to run diesel‑free (back in March 2016).”** – Indus Towers announced its first diesel‑free sites only in the late 2010s; the 50 000‑site milestone was reported in 2021, not 2016. The date and timing are therefore incorrect. [confidence: high]

- **“India’s telecom‑tower base needs to grow from roughly 750,000 towers already in place to around 1.2 million …”** – Industry data (TRAI, ICRA, and tower‑company filings) place the current count of operational towers at about 600 000–650 000, not 750 000. The baseline figure is therefore overstated. [confidence: medium]

**INTERPRETATION ERRORS**
- **“Diesel generation runs about $0.28 /kWh … diesel generators cost roughly three times what grid power costs … therefore diesel backup is losing the cost argument for data‑centres.”** – The $0.28 /kWh figure is a *levelised* cost assuming the diesel set runs continuously, whereas in data‑centres diesel is only used for short outage periods (often ≤ 4 h). Comparing a continuous‑use cost with a grid‑price that applies 24 h × 365 days is a mismatched “apples‑to‑oranges” cost comparison, so the conclusion that diesel is uneconomic for backup is not supported by the data presented. [confidence: high]

- **“Telecom tower‑cos have already proven the alternative works at scale; data‑centres … have not yet caught up.”** – Towers have low, intermittent loads and can tolerate brief outages, while data‑centres require near‑continuous power (99.999 % uptime) and much larger instantaneous loads. Demonstrating diesel‑free operation for towers does not directly prove feasibility for data‑centres; the article extrapolates the tower experience to a fundamentally different use case. [confidence: high]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
