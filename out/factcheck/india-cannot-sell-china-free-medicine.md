# Fact/interpretation check — india-cannot-sell-china-free-medicine

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-cannot-sell-china-free-medicine.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India’s pharmaceutical exports crossed $31 billion in 2025-26 — and 43.45 per cent of what goes into making them, by value, comes from China." (and the title: "India Cannot Sell “China-Free” Medicine While Importing 43% of What’s In It") — This misstates the metric. China accounts for 43.45% of India's total *pharmaceutical imports* (approx. $3.6 billion out of ~$7.5 billion total imports), not 43.45% of the input value of India's total pharmaceutical exports ($31.1 billion). [confidence: high]

INTERPRETATION ERRORS:
- "India's two PLI schemes, opposite outcomes: the ₹6,940 crore Bulk Drugs scheme built to cut China dependence produced ₹2,720 crore in sales; the ₹15,000 crore Pharmaceuticals PLI aimed at scale produced ₹3.17 lakh crore — 116x more." — This is an apples-to-oranges comparison. The Pharmaceuticals PLI covers high-value finished formulations and complex drug products from established large manufacturers where gross turnover is naturally massive. The Bulk Drugs PLI targets capital-intensive, greenfield capacity creation for specific upstream chemical starting materials and APIs (KSMs/DIs) to substitute specific imports. Comparing top-line cumulative sales figures between upstream bulk raw materials and downstream finished retail formulations misrepresents the structural objectives and output metrics of the two interventions. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India’s pharmaceutical exports crossed $31 billion in 2025-26" — The article later clarifies that exports were $31.1 billion in FY2025-26, not "crossed" (which implies surpassing a threshold). Additionally, the claim that "43.45 per cent of what goes into making them, by value, comes from China" is misleading because the 43.45% figure refers to **imports** (FY2023-24), not the value of inputs into exports. [confidence: high]

- "the Bulk Drugs PLI ... produced ₹2,720 crore of cumulative sales against a ₹6,940 crore outlay" — The article later states that the Bulk Drugs PLI produced ₹2,192 crore in **import substitution**, not cumulative sales. The ₹2,720 crore figure is for cumulative sales, while the ₹2,192 crore is for import substitution. The two are conflated in the claim. [confidence: high]

INTERPRETATION ERRORS:
- "India cannot credibly claim the label while depending on China for at least 70 per cent of ninety-seven separate active ingredients" — The article correctly notes that China supplies ≥70% of 97 APIs, but it does not establish that these specific APIs are the **same ones used in India’s exported formulations**. The claim implies a direct dependency for exports, but the APIs in question could be for domestic consumption or other non-exported products. [confidence: high]

- "The Pharmaceuticals PLI ... produced 116 times more [sales] than the Bulk Drugs PLI" — While the sales figures are correct (₹3.17 lakh crore vs. ₹2,720 crore), the comparison is apples-to-oranges because the two PLI schemes had **different objectives**: one aimed at import substitution (Bulk Drugs PLI) and the other at scale (Pharmaceuticals PLI). The claim misleadingly suggests the Bulk Drugs PLI was a failure relative to the Pharmaceuticals PLI, ignoring their distinct goals. [confidence: high]
