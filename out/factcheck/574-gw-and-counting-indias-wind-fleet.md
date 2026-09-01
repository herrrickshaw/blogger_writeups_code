# Fact/interpretation check — 574-gw-and-counting-indias-wind-fleet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/574-gw-and-counting-indias-wind-fleet.html`

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
- "India's wind fleet crossed 57,443 MW in June 2026" — The article later states the cumulative installed wind capacity reached **57,443.39 MW** by the end of June 2026, implying the figure is precise to two decimal places. However, MW capacity is typically reported as a whole number in official statistics, and the decimal precision is unusual. [confidence: high]

- "India has an estimated 70 GW of technical offshore wind potential along the Gujarat and Tamil Nadu coasts, per GWEC's Global Offshore Wind Report 2026" — The article itself acknowledges inconsistencies in offshore potential estimates, stating that "offshore potential estimates have varied across studies and years" and that "the 70 GW offshore potential figure and the 91 GW figure cited in this blog's earlier Tamil Nadu piece are different numbers from different sourcing and years." This suggests the 70 GW figure may not be definitive or verified. [confidence: medium]

INTERPRETATION ERRORS:
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped" — The article claims that the 57.4 GW fleet uses "barely 8 per cent" of the 695.5 GW potential at 120m hub height. However, this calculation assumes that the entire 695.5 GW is *installable* and *available for immediate deployment*, which is not necessarily true. The NIWE potential figures are based on a **2% land-availability assumption**, meaning only 2% of land is considered suitable for wind farms. The 8% utilization figure does not account for practical constraints like land-use restrictions, environmental regulations, or competing land uses, which could significantly reduce the actual installable capacity. [confidence: high]

- "GWEC's 6.3 GW-in-2025 figure (calendar year) and MNRE's ~6 GW-in-FY2025-26 figure (fiscal year, April-March) describe overlapping but not identical periods and should not be read as confirming each other to the decimal" — While the article correctly notes that the two figures cover different timeframes (calendar year vs. fiscal year), it does not address the fact that the **6.3 GW figure is for new installations in 2025**, while the **~6 GW figure is for additions in FY2025-26 (April 2025–March 2026)**. These are not directly comparable because the fiscal year includes part of 2025 and part of 2026, and the calendar year figure does not align with the fiscal year. The article implies that the figures are close but not identical, but it does not clarify that they are measuring different things (new installations vs. additions), which could mislead readers into thinking the figures are more comparable than they are. [confidence: high]
