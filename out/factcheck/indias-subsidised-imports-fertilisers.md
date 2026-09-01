# Fact/interpretation check — indias-subsidised-imports-fertilisers

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-subsidised-imports-fertilisers.html`

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
- "NIPU-2026 (Cabinet-approved 15 Jul 2026)" — The article states NIPU-2026 was approved 15 days before the data cutoff (31 Jul 2026), implying approval on 16 Jul 2026, not 15 Jul 2026. [confidence: high]

- "Fertiliser-grade urea up 148% — extraordinary" — The article claims urea imports grew 148% YoY, but the TradeStat data shows urea imports rose from $1,560M (FY24-25) to $3,869M (FY25-26), which is a 148% increase in value, not volume or unit terms. While numerically correct, the phrasing ("extraordinary") is subjective and could mislead readers into overstating the growth's significance without context. [confidence: medium]

INTERPRETATION ERRORS:
- "Fertilisers grew faster than any other subsidised import category in FY2025-26 — up 76% year-on-year, more than triple the next-fastest category." — The claim is factually correct (76% growth vs. next-fastest at 24.63%), but it conflates *growth rates* with *absolute impact* on the import bill. A 76% growth in a small base (fertilisers at ~$8.3bn to ~$14.6bn) is dwarfed by the absolute increase in mineral fuels (from $218.5bn to $203.4bn, a $15bn *decrease*), which still accounts for the largest share of imports. The focus on growth rates obscures the fact that mineral fuels remain the dominant import category by value, despite its decline. [confidence: high]

- "Roughly $633bn of the official $775bn FY2025-26 import bill (PIB: imports $774.98bn, deficit $333.19bn) sits in these protected categories." — The claim is numerically correct ($632.8bn vs. $775bn), but it misinterprets the *share* of protected categories. The article earlier states that the 12 categories account for 81.6% of total imports ($632.8bn/$775bn), but the phrasing implies that *only* these categories are "protected," ignoring that other imports (e.g., electronics, pharmaceuticals) may also receive subsidies or protection not covered in this analysis. This risks understating the total subsidy burden. [confidence: high]
