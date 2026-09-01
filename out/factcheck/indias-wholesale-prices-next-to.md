# Fact/interpretation check — indias-wholesale-prices-next-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-wholesale-prices-next-to.html`

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
- "India’s five-year cumulative consumer total rises from 25.2% to 27.4%" — The article claims this is a correction from a previous figure, but the original 25.2% is not supported by the cited World Bank data (FP.CPI.TOTL.ZG). The World Bank series shows India's cumulative consumer inflation from 2020–2025 as 27.4%, not 25.2%. The 25.2% appears to be an incorrect extrapolation or misinterpretation of the data. [confidence: high]

- "+8.3% India WPI" (Exhibit 4, April 2026) — The article states India's April 2026 WPI year-on-year inflation is +8.3%, but the MoSPI API value (167.0) and the Office of the Economic Adviser index file (167.6) yield slightly different year-on-year rates (approximately +8.2% and +8.3%, respectively). The article rounds to +8.3%, which is technically correct but obscures a discrepancy between two official sources. [confidence: medium]

---

INTERPRETATION ERRORS:
- "India’s consumer inflation has quietly become one of the lowest in the G20" — The article presents India's 2025 consumer inflation (2.4%) as being "one of the lowest in the G20," but this claim is based on a partial comparison. The G20 includes 19 countries (excluding the EU), and the article omits several economies (e.g., Saudi Arabia, Turkey, Russia) whose 2025 inflation rates are not shown. Without a full G20 comparison, the claim cannot be verified as accurate. [confidence: high]

- "The 2026 producer-price turn: US hardest, not India" — The article asserts that the United States "turned hardest" in producer-price inflation in 2026, based on Exhibit 4's data (+12.3% in May 2026 for the US PPI vs. +8.3% for India's WPI in April 2026). However, this comparison is apples-to-oranges: the US PPI is an annual average of monthly year-on-year rates, while India's WPI is a single month (April) year-on-year rate. The US figure is not directly comparable to India's, as it reflects a different time frame and methodology. [confidence: high]
