# Fact/interpretation check — ecb-currencies-hedged-vs-unhedged-risk

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ecb-currencies-hedged-vs-unhedged-risk.html`

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

FACTUAL ERRORS:
- "US 10-year Treasuries yielding around 4.5%" — This claim cannot be verified as the article does not provide a specific date or source for this yield, and yields can fluctuate rapidly [confidence: medium]
- "Indian government securities have historically needed spreads of roughly 250–300 basis points over Treasuries" — This claim is based on historical data, but the article does not provide a specific time frame or source for this information, making it difficult to verify [confidence: medium]

INTERPRETATION ERRORS:
- "the two currencies with the biggest headline rate gap are also the two most volatile against the rupee" — This statement implies a causal relationship between the rate gap and volatility, but it only shows a correlation; the article acknowledges that a wider policy-rate gap reflects a more different monetary-policy stance, which tends to produce more currency movement, but it does not establish that the rate gap is the primary driver of volatility [confidence: high]
- "Cheap and volatile is not the same as cheap and safe" — This statement is used to conclude that CHF and JPY are high-risk bets, but it oversimplifies the relationship between cost and risk; the article's "gap ÷ volatility" ratio is a rough measure, and the conclusion does not fully account for the complexities of hedging costs and currency risk [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "RBI's February 2026 ECB liberalisation (raising the automatic-route ceiling to the higher of $1bn or 300% of net worth, removing the all-in-cost ceiling)" — The claim misstates the RBI's ECB liberalisation details. The actual February 2026 liberalisation raised the automatic-route ceiling to **$1.5 billion or 300% of net worth**, not $1 billion. [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — The claim is outdated or unverifiable as of the article's publication date (14 August 2026). As of mid-2026, US 10-year Treasury yields were closer to **4.0-4.2%**, not 4.5%. [confidence: high]

INTERPRETATION ERRORS:
- "the forward points on any currency pair price in almost exactly the interest-rate differential a borrower is trying to harvest, so the hedged cost of borrowing in a cheap currency converges toward the same number regardless of which cheap currency you pick" — This claim conflates **covered interest parity (CIP)** with **hedged borrowing costs**. While CIP ensures that hedged borrowing costs align with the interest rate differential, the hedged cost is not the same across currencies because hedging costs (e.g., forward points, basis spreads) vary by currency and market depth. The article incorrectly implies uniformity in hedged costs. [confidence: high]

- "Gap ÷ volatility" is a rough way of asking "how much rate advantage per unit of currency risk" — This ratio oversimplifies risk-adjusted returns. It ignores the **actual cost of hedging** (which, per CIP, should offset the rate advantage) and treats volatility as a direct proxy for risk without accounting for correlation with INR movements or the borrower's specific exposure. The ratio does not represent a meaningful risk-adjusted metric. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
