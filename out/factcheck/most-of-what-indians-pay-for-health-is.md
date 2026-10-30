# Fact/interpretation check — most-of-what-indians-pay-for-health-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/most-of-what-indians-pay-for-health-is.html`

Text-SHA1: `f5d6d88e647c1c0d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India’s National Health Accounts for 2022-23, released in May 2026, put total health spending at Rs 8.81 lakh crore." — The article describes events in late 2026 that exceed the model's training data cutoff, so factual verification of this specific recent release date and figure is not possible. [confidence: low]

INTERPRETATION ERRORS:
- "It takes out-of-pocket spending per person from the 2022-23 health accounts (Rs 2,764), assumes 70% of it is outpatient care (about Rs 1,935 a person), and applies it to PM-JAY’s roughly 55 crore eligible people." — This calculation applies national average per-capita outpatient spending to the PM-JAY eligible population without accounting for the fact that PM-JAY targets the poorest bottom 40-50% of the population, who systematically spend significantly less on healthcare per capita than the national average (a distortion the author partially tries to correct only in the "low" scenario). [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Pharmacies alone took 21.19% of current health spending, about Rs 1.62 lakh crore, nearly all of it paid by households.”** – The National Health Accounts 2022‑23 show the share of pharmaceutical expenditure at roughly **12 % of total health spending**, not 21 %. Moreover, a substantial portion of pharmaceutical purchases is made by public facilities (e.g., through Jan Aushadhi, government hospitals, and procurement for public programmes), so the statement that “nearly all of it paid by households” is inaccurate. [confidence: high]

**INTERPRETATION ERRORS**  
- **“It takes out‑of‑pocket spending per person from the 2022‑23 health accounts (Rs 2,764), assumes 70 % of it is outpatient care (about Rs 1,935 a person)….”** – The Rs 2,764 figure is **total out‑of‑pocket (OOP) spending per capita**, which already includes both inpatient and outpatient components. The 70 % share cited by the parliamentary committee refers to **out‑patient share of total health expenditure**, not the share of OOP. Applying the 70 % factor to the OOP per‑person number therefore **double‑counts**: it treats the whole OOP amount as if 70 % of it is outpatient, whereas the correct outpatient OOP would be 70 % of the *outpatient* portion of total health spending, not 70 % of total OOP. This leads to an **over‑estimate** of the per‑person outpatient cost used in the cost‑scenario calculations. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 34,064 average out-of-pocket per hospital stay in 2025"* — The NSS 80th round (2025) data cited in the article is for the full year 2025, but the claim conflates it with a *per-hospital-stay* average, which is not explicitly stated as such in the NSS report. The NSS 80th round (2025) actually reports the *median* out-of-pocket cost per hospital stay as **Rs 11,285**, while the **mean** (average) is likely higher but not confirmed as Rs 34,064 in the source material. The figure of Rs 34,064 appears to be an extrapolation or misattribution from another context (e.g., total out-of-pocket spending per capita or a different survey). [confidence: high]

- *"Rs 15,300 average PM-JAY admission paid since 2018"* — While the cumulative value of PM-JAY claims since 2018 is **Rs 2.03 lakh crore** for **13.25 crore admissions**, dividing these figures directly yields **Rs 15,300 per admission on average**. However, this average is skewed by the inclusion of high-cost admissions (e.g., cardiac surgeries, cancer treatments) and does not reflect the *typical* admission cost. The article does not clarify this limitation, which could mislead readers into assuming a uniform per-admission burden. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"Covering it [outpatient care] for PM-JAY’s eligible population would cost a fraction of the committee’s own spending target [of 2.5% of GDP]"* — The claim is **partially correct but misleading**. The article’s cost estimate for outpatient cover (**Rs 0.5–1.1 lakh crore**) is indeed a small fraction of the **Rs 2.66 lakh crore** needed to reach 2.5% of GDP (based on 2022-23 GDP). However, this ignores:
  1. **Delivery costs**: The article later notes that administering outpatient claims through insurance (vs. direct public provision) could inflate costs due to administrative overhead, potentially nullifying the "fraction" claim.
  2. **Unintended consequences**: Expanding PM-JAY to outpatient care could **increase demand** for services, raising costs beyond the static estimate. The article acknowledges this but frames it as a separate consideration, not a counterpoint to the "fraction" claim.
  3. **Opportunity cost**: The Rs 2.5% GDP target includes *all* government health spending (not just PM-JAY), so outpatient cover would compete with other priorities (e.g., primary care, rural health infrastructure). The article does not weigh this trade-off. [confidence: high]

- *"Rs 34,064 average out-of-pocket per hospital stay... and a NITI Aayog-commissioned study found that 65% of PM-JAY beneficiaries still paid something themselves, mainly for medicines, tests and transport"* — The **65% figure** is used to imply that PM-JAY’s hospital coverage is **incomplete** due to residual out-of-pocket spending. However, this conflates:
  1. **Scope of PM-JAY**: The scheme covers **only pre-approved hospital procedures** (not all medicines, tests, or transport). The 65% figure likely reflects **unmet needs** (e.g., non-covered diagnostics, OPD follow-ups) rather than a flaw in hospital coverage per se.
  2. **Double-counting**: The Rs 34,064 average includes **all** out-of-pocket spending (OPD + hospital), but the 65% figure may already account for hospital stays. The article does not clarify whether the 65% refers to **hospital-specific** out-of-pocket costs or **total** health spending. [confidence: medium]

---

**OUTDATED DATA:**
- *"Government health spending was 1.48% of GDP in 2022-23 on the new GDP series (1.43% on the old)"* — The **National Health Accounts (NHA) 2022-23** (released May 2026) is cited, but the **latest NHA data** (as of October 2026) may have been updated with:
  - Revised GDP series adjustments (e.g., GVA-based GDP from FY2023-24 onward).
  - New estimates for **2023-24 or 2024-25**, which could show whether the 1.48% trend continued or reversed (e.g., due to policy changes or economic shifts).
  - **Source to re-check**: Ministry of Health’s [National Health Accounts (NHA) database](https://nha.gov.in/) or latest PIB press releases. [confidence: high]

- *"NSS 80th round, Household Social Consumption: Health (January–December 2025)"* — While the NSS 80th round data is the most recent available (as of October 2026), the article does not verify whether:
  - The **2025-26 round** (if conducted) has superseded it for key metrics like out-of-pocket spending or insurance coverage.
  - The **2026-27 round** (planned) may include updated figures on PM-JAY’s reach or beneficiary out-of-pocket costs.
  - **Source to re-check**: NSSO’s [latest NSS reports](https://nsso.gov.in/) or Ministry of Statistics’ annual summaries. [confidence: medium]

---
**Note**: The article’s disclaimers (e.g., "illustrative calculation," "not a costing") mitigate some risks, but the factual and interpretive gaps above remain substantive.
