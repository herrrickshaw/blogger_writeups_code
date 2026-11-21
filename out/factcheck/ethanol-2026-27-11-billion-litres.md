# Fact/interpretation check — ethanol-2026-27-11-billion-litres

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ethanol-2026-27-11-billion-litres.html`

Text-SHA1: `cb10bfcaafb8746d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Rs 73,996 crore was spent on ethanol in 2024-25, up 52% from Rs 48,757 crore" — A percentage increase from Rs 48,757 crore to Rs 73,996 crore is approximately 51.77% (or 52% rounded), but the procurement value for 2023-24 is cited elsewhere in the text as Rs 48,757 crore while the absolute math checks out, the text also mentions "Rs 49,577 crore was spent by June 2026" under the procurement section, which creates a chronological/labeling contradiction regarding the 2025-26 period depending on the specific fiscal or supply year definitions applied. [confidence: low]

INTERPRETATION ERRORS:
- "A price gap of Rs 13.89 a litre between maize and C-heavy molasses explains why distilleries lean on grain, and it is paid for by the procurement bill of Rs 73,996 crore in 2024-25." — The price gap cited is between maize (Rs 71.86) and C-heavy molasses (Rs 57.97), which equals Rs 13.89. However, attributing the total procurement bill of Rs 73,996 crore directly to paying for this price gap is a reasoning gap, as the total bill is a function of total volume multiplied by respective feedstock prices, not just the differential cost of maize over molasses. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“E20 petrol with a minimum RON of 95 became the national standard from 1 April 2026.”** – The Indian government announced that E20 would become mandatory from 1 April 2025, not 2026, and the RON 95 specification was also stipulated in the 2025 directive. The article’s date is therefore incorrect. [confidence: high]  

- **“Installed capacity of about 20 billion litres is nearly twice the 10 to 11 billion litres that E20 needs.”** – Official capacity figures from the Ministry of Petroleum (2023‑24) place total ethanol production capacity at roughly 12‑13 billion litres per year, not 20 billion. The claim overstates capacity by a large margin. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“A price gap of Rs 13.89 a litre between maize and C‑heavy molasses explains why distilleries lean on grain, and it is paid for by the procurement bill of Rs 73,996 crore in 2024‑25.”** – The article treats the price differential as the primary driver of feedstock choice, implying a causal link. In reality, the shift toward grain‑based ethanol is also driven by policy exclusions (cane juice and B‑heavy molasses barred from the tender) and availability constraints, not solely by price. The conclusion over‑attributes the behaviour to price alone. [confidence: medium]  

- **“Installed capacity … is nearly twice the 10 to 11 billion litres that E20 needs, so the tender volume is set by policy and not by what distilleries can make.”** – This reasoning assumes that because capacity exceeds the theoretical requirement, the tender amount is purely a policy decision. However, actual production is limited by feedstock availability, plant utilisation rates, and logistical bottlenecks; capacity figures alone do not prove that distilleries could not meet a larger tender. The argument conflates theoretical capacity with practical output. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The government says no decision has been taken to go beyond 20%"* — This contradicts the **USDA GAIN Biofuels Annual (23 July 2026)**, which explicitly states that *"industry sources call E30 attainable"* and projects **23.4% blending for calendar 2026**. The article’s claim omits this conflicting industry projection. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Installed capacity of about 20 billion litres is nearly twice the 10 to 11 billion litres that E20 needs, so the tender volume is set by policy and not by what distilleries can make"* — The reasoning conflates **total installed capacity** (20 bln litres) with **actual E20 requirement** (10–11 bln litres), but this ignores that:
  1) **E20 demand is dynamic** (depends on petrol sales, not fixed at 10–11 bln litres).
  2) **Capacity utilisation varies by feedstock** (e.g., sugarcane vs. maize), and the tender’s 11 bln litres may reflect **supply-side constraints** (e.g., FCI rice quotas, seasonal feedstock availability) rather than purely policy-driven targets.
  The claim falsely assumes capacity is idle or irrelevant to tender sizing. [confidence: high]

**OUTDATED DATA:**
- *"Rs 49,577 crore was spent by June 2026"* — This covers **only November 2025–June 2026** (half of ESY 2025-26), not the full year. For a **2025-26 total**, re-check **Rajya Sabha unstarred question 141 (20 July 2026)** for the full-year figure (likely superseded by ESY 2026-27 data). [confidence: high]

---
*Note: The article’s sources (e.g., PIB, USDA GAIN) are current as of July/October 2026, but the claim about "no decision beyond 20%" directly contradicts USDA’s industry projections. The capacity/requirement gap also misrepresents the relationship between supply and demand.*
