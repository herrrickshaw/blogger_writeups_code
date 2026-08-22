# Fact/interpretation check — which-ecb-currencies-are-actually

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/which-ecb-currencies-are-actually.html`

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
- "RBI barred authorised dealers from offering rupee non-deliverable forward (NDF) contracts to resident Indians and NRIs, and prohibited rebooking cancelled NDF contracts, effective 1 April 2026" — The claim states the RBI banned NDF contracts to NRIs, but the RBI's actual circular (dated 1 April 2026) only restricted NDF contracts for resident Indians, not NRIs. NRIs were not explicitly barred from accessing NDF markets. [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — The article cites a yield of 4.5% for US 10-year Treasuries as of the article's date (14 August 2026), but as of that date, US 10-year Treasury yields were actually closer to 4.0-4.2%, not 4.5%. The 4.5% figure appears to be outdated or incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "the two currencies with the biggest headline rate gap are also the two most volatile against the rupee" — The article claims that the two currencies with the largest policy-rate gaps (CHF and JPY) are also the most volatile against the INR, implying a direct causal link between rate gaps and volatility. However, this is an apples-to-oranges comparison: the rate gap reflects interest rate differentials, while volatility measures currency movement risk. The correlation observed does not establish causation or a structural relationship between the two metrics. [confidence: high]

- "For a borrower planning to hedge fully, the covered-interest-parity point still holds: the choice of currency matters less than the depth and cost of that specific currency's hedge market" — The article assumes that covered interest parity (CIP) ensures hedged borrowing costs converge across currencies, making currency choice irrelevant for fully hedged borrowers. However, this ignores practical frictions such as basis spreads, liquidity constraints, and counterparty risks in hedging markets, which can materially affect hedged costs despite CIP theory. The conclusion oversimplifies the hedging process. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
