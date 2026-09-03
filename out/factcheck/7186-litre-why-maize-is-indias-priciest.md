# Fact/interpretation check — 7186-litre-why-maize-is-indias-priciest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/7186-litre-why-maize-is-indias-priciest.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The government has separately cut the mandatory buffer-stock reserve requirement for rice from 25 per cent to 10 per cent, freeing up more surplus and broken rice specifically for ethanol distillation" — India's foodgrain buffer stocking norms (maintained by the Food Corporation of India) are prescribed in absolute quantities (million metric tonnes/lakh tonnes) varying quarterly by operational and strategic reserve needs, not as percentage ratios. There is no mandatory buffer-stock reserve requirement defined as 25% cut to 10%. [confidence: high]
- "Maize-based ethanol supply to OMCs went from zero in ESY 2021-22 to 498.49 crore litres in ESY 2024-25" — The figure of ~498.5 crore litres refers to total ethanol procurement across *all* feedstocks by OMCs in ESY 2022-23 (where all-India supply reached approximately 500 crore litres), not volume derived from maize alone. Maize-based ethanol accounts for a fraction of that overall procurement. [confidence: high]
- "for ESY 2025-26 Cycle 1, OMCs received supply offers totalling 1,776.49 crore litres — of which 1,304.86 crore litres came from grain-based feedstock alone — against a stated requirement of roughly 1,050 crore litres for that cycle" — This tender data belongs to the tender for ESY 2024-25 Cycle 1 (floated in late 2024 where OMCs sought ~1,050 crore litres and received 1,776.49 crore litres in offers, including 1,304.86 crore litres from grains), not ESY 2025-26. [confidence: high]

INTERPRETATION ERRORS:
- "Maize is now India's most expensive ethanol feedstock by government-set price — ₹71.86 a litre, ahead of sugarcane juice, rice, and every grade of molasses" — Category error / apples-to-oranges comparison: ₹71.86 per litre is not the price of maize feedstock (which is an agricultural solid commodity traded in quintals), but the procurement price OMCs pay distilleries for finished ethanol produced *from* maize. Describing it as the feedstock price alongside liquid feedstocks conflates the final processed fuel price with raw feedstock costs. [confidence: high]
- "The demand-side price signal and the on-the-ground planting decision are currently pointing in opposite directions... The price incentive and the acreage decision are telling two different stories at once... It just isn't, on its own, enough to make farmers plant more maize in a season where other factors pulled the other way." — False transmission mechanism / causal reasoning gap: The ₹71.86/litre price is paid by OMCs to distillers to compensate for the higher capital, conversion, and processing costs of grain-based distilleries. It is not an MSP or farmgate procurement price paid directly to farmers. A higher OMC ethanol purchase price incentivizes distillers to bid for grain, but farmgate maize prices are dictated by overall domestic demand (such as the feed and starch industries) and open-market conditions. Framing the distillery procurement price as a direct farmer planting incentive creates an unjustified contradiction with planting acreage. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Maize-based ethanol volumes went from zero to nearly 500 crore litres in three years" — The article cites maize-based ethanol supply to OMCs as going from zero in ESY 2021-22 to 498.49 crore litres in ESY 2024-25, which is a span of **four years**, not three. [confidence: high]

- "Wheat is a rabi (winter) crop and maize/rice/sugarcane figures above are kharif; the four aren't measured in the same sowing window" — While this is technically correct, the article later states that wheat's "prior year" comparison is given as a range due to varying progress-report snapshots, implying inconsistency in the data. However, the **primary factual error** is the incorrect time span for maize ethanol growth. [confidence: high]

INTERPRETATION ERRORS:
- "Maize's price premium over every other feedstock is the direct policy lever behind the demand-side story: it pays millers and grain processors more per litre to convert maize into ethanol than to run any other feedstock through the same process" — The article correctly notes maize's price premium but **does not establish causation** between this price signal and the acreage decline. Multiple factors (weather, input costs, competing crops) could explain the 9.7% acreage drop, and the article acknowledges this uncertainty but still frames the price incentive as the primary driver without sufficient evidence. [confidence: high]

- "Grain-based feedstocks (maize plus rice) are now supplying more ethanol capacity than the programme currently needs: for ESY 2025-26 Cycle 1, OMCs received supply offers totalling 1,776.49 crore litres — of which 1,304.86 crore litres came from grain-based feedstock alone — against a stated requirement of roughly 1,050 crore litres for that cycle, an oversubscription of more than 70 per cent." — While the oversubscription figure is correct, the **interpretation that this "oversupply" is due to maize acreage decline is flawed**. The oversupply is a result of **built-up distillation capacity** (as the article later notes) and policy-driven grain availability (e.g., rice buffer stock reduction), not directly tied to maize planting decisions. The acreage dip is a separate factor and does not logically explain the oversupply. [confidence: high]
