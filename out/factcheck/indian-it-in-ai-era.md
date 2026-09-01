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
- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The article cites RBI data showing net services receipts at $216.6bn in FY2025-26, but the RBI's "Developments in India's Balance of Payments, Q4 2025-26" report (the cited source) lists net services receipts as $216.6bn for FY2025-26 and $188.8bn for FY2024-25, implying an increase of $27.8bn. However, the RBI report's table shows a net services receipts figure of $216.6bn for FY2025-26 and $188.8bn for FY2024-25, which is correct. The error lies in the article's claim that this is the "biggest jump on record," as the RBI data does not provide historical context to confirm this is the largest year-on-year increase. [confidence: medium]

- "The Economic Survey's own uncomfortable framing" section claims: "services exports are 'not a substitute for the goods-based export ecosystems that ultimately underpin durable external and currency stability.'" — The article quotes the Economic Survey 2025-26 but does not provide a direct quote or citation for this specific phrasing. The Economic Survey does discuss the limitations of services exports, but the exact wording is not verifiable from the cited sources. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services alone offset 64% of the goods deficit. Net services plus remittances offset 107% — they more than cover the goods gap." — The article correctly states that net services receipts offset 64% of the goods trade deficit and that net services plus remittances offset 107% of the goods deficit in FY2025-26. However, it then concludes that this means the goods deficit is "survivable at 0.6% of GDP," implying a causal link between services receipts and the current account deficit being manageable. The reasoning gap is that the current account deficit is determined by the balance of all components (merchandise trade, services, remittances, and primary income), not just services and remittances. The primary income deficit (investment income paid out) is a significant factor ($48.2bn in FY2025-26), and the current account deficit is the net result of all these components. The article overlooks the role of primary income in determining the current account deficit. [confidence: high]

- "A sector that is 1% of jobs but ~8% of GDP and covers two-thirds of the goods trade deficit cannot produce a mass-unemployment event. It can produce a balance-of-payments event." — The article correctly notes that IT is ~1% of India's workforce but ~8% of GDP and covers two-thirds of the goods trade deficit. However, it then claims that this asymmetry means an AI shock would show up in the rupee before jobs data, implying a direct causal link between services export performance and currency stability. The reasoning gap is that the article does not adequately explain *how* an AI shock to services exports would directly translate into currency movements. While services exports are important for the balance of payments, currency stability also depends on capital flows, foreign exchange reserves, and other macroeconomic factors. The article assumes a direct transmission mechanism without sufficient evidence or explanation. [confidence: medium]
