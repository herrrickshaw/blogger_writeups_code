# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

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
- "India now has one live nationwide fuel-blending mandate (E20 petrol)" — This is incorrect as of the article's publication date (19 August 2026). India has multiple live blending mandates, including E10 petrol (not just E20) and the CBG blending obligation. The E20 mandate is not yet nationwide in practice, as compliance varies by state and vehicle compatibility. [confidence: high]

- "SAF traded globally in 2026 at roughly $1,817 per tonne" — While the article cites this figure, it does not provide a primary source or context for the global SAF price in 2026. SAF prices are highly volatile and region-specific, and this figure appears to be an outlier compared to other cited projections (e.g., India-specific PBtL SAF at $1.4/L). The claim lacks verifiable sourcing. [confidence: medium]

---

INTERPRETATION ERRORS:
- "Ethanol and isobutanol fall well short of their host fuel's energy density, which is why those mandates cost drivers mileage; CBG and SAF sit near parity, which is why their cost shows up as price instead." — This claim conflates energy density with cost implications without accounting for market dynamics. While energy density differences explain *potential* mileage loss, the actual cost to drivers depends on pricing, subsidies, and fuel taxes, not just energy content. For example, E20 petrol may still cost the same per litre as E0 petrol despite lower energy density, but the *effective cost per kilometre* could be higher due to reduced efficiency. The article assumes the cost burden is solely tied to energy parity, ignoring how fuel pricing and policy interventions (e.g., subsidies) might offset or exacerbate the impact. [confidence: high]

- "The blend chemistry decides who pays and how; the mandate percentage is almost beside the point." — This overgeneralizes the role of blend chemistry. While energy density is a critical factor, the *mandate percentage* still matters for supply chain logistics, infrastructure readiness, and economic feasibility. For instance, a 5% SAF mandate may be easier to implement than a 20% ethanol mandate due to compatibility with existing infrastructure, even if SAF is a "true drop-in." The article dismisses the mandate percentage as irrelevant, but it directly influences transition costs, blending feasibility, and policy timelines. [confidence: high]
