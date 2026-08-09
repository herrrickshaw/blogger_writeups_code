# Fact/interpretation check — beyond-pump-what-upi-fee-would-cost

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/beyond-pump-what-upi-fee-would-cost.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "25.8× Leverage of a 1% MDR on a 3.87%-margin ticket — the fuel-dealer case, for scale" — The calculation of a 1.00% fee against a 3.87% margin is $1.00 / 3.87 = 0.25839$, which is 25.8% (as correctly stated in Exhibit 2), not 25.8× (25.8 times, which would equal 2,580%). [confidence: high]
- "On the leverage curve (Exhibit 3), a 10–15% margin puts a 0.30% MDR at roughly 2–3% of margin" — The article misidentifies its own exhibits. Exhibit 2 is the leverage curve, Exhibit 3 is the top 15 merchant category table, and Exhibit 4 contains the combined grocery/restaurant totals and fee computations (which are also miscited as Exhibit 2 and Exhibit 3 in the Sources section). [confidence: high]

INTERPRETATION ERRORS:
- "RuPay-credit-on-UPI is the existence proof that the title's question is not hypothetical: the same UPI QR code, scanned with a RuPay credit card instead of a bank account, already carries a fee within spitting distance of what Visa and Mastercard charge on ordinary credit cards — roughly 2% against their 1.8–2.5%... suggests convergence toward card pricing is not a hypothetical extreme; it is a rate this ecosystem has already priced once." — This is an apples-to-oranges comparison. Credit products (whether on UPI or physical cards) carry credit risk, unsecured cost of funds, and interest-free grace periods, which account for their ~2% MDR. Standard bank-to-bank UPI transactions are immediate debits against existing savings balances with no credit extension or credit risk. The existence of card-level pricing on a credit product does not support the claim that basic bank-to-bank UPI transfers will converge toward credit card pricing. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Six years of statutory zero-MDR on UPI ended on 4 August 2026" — The article does not provide a specific start date for the statutory zero-MDR period, but based on the information given, it can be inferred that the period started on January 1, 2020, as mentioned later in the article. However, without a clear start date, the accuracy of the six-year period cannot be verified [confidence: medium].
- "RBI debit-card MDR caps (turnover-tiered, ₹200/₹1,000 per-transaction ceilings): as summarised by Razorpay, tracing to RBI's post-2017 debit-card MDR rationalisation" — The article relies on secondary reporting by Razorpay for RBI's debit-card MDR caps. While this might be accurate, it introduces a layer of potential inaccuracy due to the reliance on a third-party summary rather than direct RBI sources [confidence: medium].

INTERPRETATION ERRORS:
- "One flat MDR rate taxes margins wildly unevenly — 26% of a fuel dealer’s margin and 2% of a restaurant’s at the same 1% rate" — The article concludes that a flat MDR rate would tax margins unevenly across different merchant categories. However, this conclusion assumes that the impact of the MDR on these margins is directly comparable without considering other factors that might influence how these margins are affected, such as differences in business models, cost structures, and market conditions [confidence: high].
- "If Section 10A’s new notification power is ever used, the leverage curve predicts the notification will not be one number: it will be a schedule" — The article extrapolates from the leverage curve analysis to predict the form of future notifications under Section 10A. This prediction assumes that policymakers will directly apply the insights from the leverage curve to their decision-making, which may not necessarily be the case due to the complexity of policy decisions and the influence of various stakeholders and factors [confidence: medium].
