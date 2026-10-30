# Fact/interpretation check — maize-is-cheapest-in-different-state

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/maize-is-cheapest-in-different-state.html`

Text-SHA1: `b4ffe6671b1f1157`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Rice moves within a narrow band all year… Rice swings 5–9% across the year in the main states, typically cheapest around January after the kharif harvest and dearest between August and October.” — The kharif (monsoon) rice harvest in India is normally harvested in October‑November, not in January. Therefore rice cannot be “cheapest around January after the kharif harvest.” The timing described contradicts the known agricultural calendar. [confidence: high]

- “The spread, about Rs 510 a quintal from Madhya Pradesh to Tamil Nadu, is wider than the roughly Rs 400 a quintal it costs to truck grain that far, at about Rs 3 a tonne‑kilometre.” — Road freight rates for bulk grain in India are generally around **Rs 1–2 per tonne‑km**, not Rs 3. Using Rs 3 inflates the estimated transport cost, making the comparison inaccurate. [confidence: medium]

**INTERPRETATION ERRORS**
- “For a feed mill or distillery, the data argues for buying where and when the harvest is, rather than storing.” — This conclusion is drawn from a **six‑month carry test that assumes a fixed warehouse rent of Rs 10 / quintal month, interest at 10.5 % p.a., and shrinkage of 0.1 % month**, but real‑world storage costs, financing rates, quality degradation, and transaction taxes vary widely across firms and regions. Extrapolating the test’s negative results to all buyers overstates the case against storage. [confidence: high]

- “That gap is the opening a trader moving grain from the central states to the southern poultry belt works with.” — The analysis treats the **price spread alone as a tradable arbitrage opportunity**, ignoring additional costs (e.g., loading/unloading, quality segregation, market risk, taxes, and possible price movements during transit). Hence the claim that the spread “opens” a profitable trade is an **apples‑to‑oranges** inference. [confidence: medium]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Madhya Pradesh accounted for 7.4 million of the 16.1 million tonnes reported to Agmarknet over the past year"* — **Madhya Pradesh’s reported arrivals (1.7 Mt in Dec 2025) cannot sum to 7.4 Mt over a full year** (even if scaled to 12 months, this would require ~1.5 Mt/month, which contradicts the chart’s peak of 1.7 Mt in Dec 2025). The claim conflates annualized production estimates with Agmarknet’s monthly arrival data, which is explicitly scaled to *peak months* (e.g., 1.7 Mt in Dec 2025). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Buying and holding for six months lost money on average"* — **This ignores transaction costs and storage inefficiencies**. The analysis assumes a fixed 10% annual interest rate and 0.1% monthly shrinkage, but real-world storage (e.g., FCI godowns, private warehouses) incurs higher costs (insurance, handling, depreciation), and the "loss" may reflect *opportunity costs* (e.g., reinvesting capital elsewhere) rather than pure storage arbitrage. The claim thus misrepresents the *net* viability of holding grain. [confidence: high]

---
**OUTDATED DATA:**
- *"Rice prices mix many varieties and grades, so a state’s rice price partly reflects what kind of rice it trades, not only where it is"* — **No outdated data flagged**, but the article notes Agmarknet’s coverage widened in **November 2025**, making pre-2025 arrival volumes *non-comparable*. The claim about "many varieties" should explicitly state that **grade-wise price data (e.g., broken rice) is unavailable for state-level comparison** and direct readers to check the [FCI OMSS-D 2026-27 price (Rs 2,390/qtl)](https://chinimandi.gov.in) for distillery-relevant grades. [confidence: medium]

---
**Note:** The article’s reliance on Agmarknet’s *weighted-average* prices (which mix grades) and the lack of granular grade data (e.g., broken rice) is a **methodological limitation**, but not strictly "outdated data." The November 2025 coverage change is the closest to a data gap.
