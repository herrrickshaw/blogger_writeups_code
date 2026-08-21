# Fact/interpretation check — the-national-beekeeping-honey-mission

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-national-beekeeping-honey-mission.html`

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
- "India became the world's second-largest honey exporter in 2024" — The article cites APEDA and CRISIL's July 2025 dashboard for this claim, but the article itself is dated 20 August 2026. The claim about 2024 exports cannot be verified as of August 2026, as 2024 data would not yet be finalized or confirmed. [confidence: high]

- "the National Beekeeping & Honey Mission (NBHM) ... launched ... with a total outlay of ₹500 crore for FY2020-21 to FY2022-23" — The article later states that the scheme was extended using ₹370 crore carried forward as unspent balance from the original allocation, implying the total outlay was not ₹500 crore but rather ₹500 crore allocated over FY2020-23, with additional funds carried forward. The phrasing "total outlay of ₹500 crore" is misleading as it suggests the total spent or allocated was ₹500 crore, when in fact the scheme's total funding envelope includes carried-forward funds. [confidence: high]

INTERPRETATION ERRORS:
- "the purity test that infrastructure depends on for credibility remains optional for the honey Indians actually buy in shops, four years after the scandal that made the test necessary in the first place" — The article correctly notes that the NMR test is not mandatory for domestic honey, but it does not establish that the export infrastructure's credibility *depends* on the NMR test. The export infrastructure relies on FSSAI standards (including the rice-syrup marker), which are mandatory for export but not for domestic sales. The claim implies a direct dependency that is not clearly supported by the evidence presented. [confidence: medium]

- "the National Beekeeping & Honey Mission has genuinely built export-grade infrastructure and pushed India to the world's No. 2 honey exporter" — While the article provides data on export growth and infrastructure sanctioned, it does not establish a causal link between NBHM's infrastructure and India's rise to the second-largest honey exporter. The export growth could be due to other factors (e.g., global demand, price competitiveness, or existing capacity), and the article does not provide evidence to support the claim that NBHM alone caused this shift. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
