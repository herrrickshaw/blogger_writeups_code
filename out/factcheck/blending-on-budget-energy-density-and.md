# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "...nearly half of E20's 6.9% ceiling despite isobutanol displacing a deeper share of the base fuel." (and "isobutanol's proposed 15% ceiling is far deeper than E20's 20% actual blend...") — A 15% blend displaces less of the base fuel than a 20% blend (E20). Describing 15% as a "deeper share" than 20% is mathematically inverted. [confidence: high]
- "SAF traded globally in 2026 at roughly $1,817 per tonne, on the order of five times a conventional jet-fuel benchmark in tight markets..." — Conventional jet fuel priced at $0.60–$0.80 per litre translates to roughly $750–$1,000 per metric tonne (at standard jet fuel density of ~0.80 kg/L). A price of $1,817 per tonne is roughly 1.8× to 2.4× conventional jet fuel, not 5× (which would require conventional jet fuel to trade around $360/tonne or SAF to trade around $4,000/tonne). [confidence: high]

INTERPRETATION ERRORS:
- "Because CBG is metered into the same pipeline network and sold at the same per-kilogram CNG price, with no separate CBG retail rate, there is no cost-per-kilometre penalty for the consumer to detect..." — The article notes in Table 1 and Section 4 that CBG carries lower gravimetric energy density (47–52 MJ/kg, ~93–95%) than fossil CNG (50–56 MJ/kg). Because CNG is retailed and metered by mass (₹/kg), blending a fuel with lower MJ/kg and selling it at the same ₹/kg price means the consumer receives fewer megajoules per rupee, resulting in a mileage/range loss per kilogram purchased. Selling at the same pump price shifts the cost directly onto vehicle efficiency/range, contradicting the article's conclusion that CBG imposes no mileage penalty. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "19 August 2026" — The date is in the future relative to the current date (June 2025), making it unverifiable and likely incorrect. [confidence: high]

- "SAF traded globally in 2026 at roughly $1,817 per tonne" — The article cites a global SAF price for 2026, but as of June 2025, this figure is speculative and unverifiable. [confidence: high]

INTERPRETATION ERRORS:
- "The pattern in one line: ethanol carries 66% of petrol's energy per litre and isobutanol carries 74% of diesel's, so both mandates cost the driver mileage." — While the energy density ratios are correct, the conclusion that *both* mandates cost the driver mileage is an oversimplification. The article later acknowledges that isobutanol's mileage loss is smaller than ethanol's (1–2% vs. 2–6%), but the initial claim implies a uniform penalty, which is misleading. [confidence: high]

- "Because CBG is metered into the same pipeline network and sold at the same per-kilogram CNG price, with no separate CBG retail rate, there is no cost-per-kilometre penalty for the consumer to detect — the running-cost figures already published for CNG vehicles [...] already implicitly include whatever share of CBG is in the pipeline blend, indistinguishably." — While CBG blending does not directly cause a mileage penalty, the claim that there is *no cost-per-kilometre penalty at all* ignores potential indirect costs (e.g., infrastructure adjustments, supply chain inefficiencies, or future price adjustments to offset blending costs). The reasoning assumes perfect pass-through of costs, which may not hold. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
