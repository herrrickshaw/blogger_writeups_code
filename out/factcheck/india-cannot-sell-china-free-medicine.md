# Fact/interpretation check — india-cannot-sell-china-free-medicine

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-cannot-sell-china-free-medicine.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "On 2 April 2026 the United States issued a Section 232 proclamation imposing a 100 per cent tariff on patented pharmaceuticals..." — This event and policy action are unverified/fictional; Section 232 of the Trade Expansion Act has not been used to impose a 100% tariff on patented pharmaceuticals. [confidence: high]
- "The BIOSECURE Act , enacted December 2025 as part of the FY2026 defence authorisation..." — This enactment date and mechanism cannot be verified; the BIOSECURE Act was not enacted as part of an FY2026 defense authorization in December 2025. [confidence: high]
- "India’s pharmaceutical exports reached $31.1 billion in FY2025-26, per Pharmexcil..." — Cannot be verified against authentic historical trade data, as FY2025–26 trade figures represent future/simulated data. [confidence: high]

INTERPRETATION ERRORS:
- "India’s pharmaceutical exports crossed $31 billion in 2025-26 — and 43.45 per cent of what goes into making them, by value, comes from China." / "India Cannot Sell “China-Free” Medicine While Importing 43% of What’s In It" — False equivalence / conflation. The 43.45% figure represents China's share of India's *total pharmaceutical import basket* (around $3.6 billion of ~$7.5–8 billion total imports), not 43.45% of the total value or input content of India's finished pharmaceutical output/exports (which exceed $31 billion). [confidence: high]
- "Two PLI Schemes, Same Goal, Opposite Outcomes... the ₹6,940 crore Bulk Drugs scheme built to cut China dependence produced ₹2,720 crore in sales; the ₹15,000 crore Pharmaceuticals PLI aimed at scale produced ₹3.17 lakh crore — 116x more." — Apples-to-oranges comparison and self-contradiction. The article asserts they share the "same goal," but explicitly notes elsewhere that the Bulk Drugs PLI focuses on upstream, capital-intensive chemical/fermentation import substitution of critical KSMs/APIs, whereas the Pharmaceuticals PLI focuses on downstream formulation scale. Comparing top-line sales across two fundamentally different segments with different value bases distorts the evaluation of their relative success. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India’s pharmaceutical exports crossed $31 billion in 2025-26" — The article later states the exports were $31.1 billion in FY2025-26, not "crossed" $31 billion. The term "crossed" implies a value greater than $31 billion, which is not supported by the data. [confidence: high]

- "the US Section 232 tariff hit patented drugs at 100 per cent from April 2026" — The article later clarifies that the tariff was effective 31 July 2026 for most importers and 29 September 2026 for seventeen named companies, not from April 2026. [confidence: high]

INTERPRETATION ERRORS:
- "India cannot credibly claim the label while depending on China for at least 70 per cent of ninety-seven separate active ingredients" — The claim conflates import dependency (43.45% of total pharma imports from China) with the share of specific active ingredients (70% or more for 97 APIs). The 70% figure applies only to a subset of APIs, not the entire import basket, and does not directly translate to the overall import dependency. The reasoning gap is that the article treats the subset statistic as representative of the whole, which is not justified. [confidence: high]

- "The Bulk Drugs PLI ... produced ₹2,720 crore of cumulative sales against a ₹6,940 crore outlay" — The article presents this as a failure of the scheme, but the PLI's goal was to reduce China dependence, not necessarily to generate high sales. The reasoning gap is that the metric of sales is misaligned with the scheme's actual objective of import substitution. [confidence: high]
