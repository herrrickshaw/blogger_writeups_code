# Fact/interpretation check — india-dropped-last-approvals-on-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-dropped-last-approvals-on-its.html`

Text-SHA1: `85a834f5148b258a`

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
- “25.17% corporate tax” — The article states that the Indian corporate tax rate applicable to the 15 % cost‑plus safe‑harbour margin is 25.17 %. The statutory rate for domestic companies (the typical Indian operators of data‑centre capacity) is 25 % plus a 4 % surcharge (if profit exceeds ₹1 cr) and a 4 % health‑and‑education cess, giving an effective rate of roughly 27 % (≈ 27.04 %). The 25.17 % figure does not match any current Indian corporate‑tax rate. [confidence: high]

**INTERPRETATION ERRORS**  
- “India would collect about Rs 45 crore a year of Indian tax” (based on a 100 MW campus with assumed load, PUE, power cost, and 50 % of operating cost being power). The article treats this single illustrative calculation as a sense‑of‑scale for the revenue the tax holiday foregoes. Because the assumptions (IT load 70 %, PUE 1.4, power price ₹7/kWh, power = 50 % of costs) are arbitrary and not tied to any actual data‑centre’s cost structure, the resulting Rs 45 crore figure cannot be used to infer the magnitude of the tax exemption. It extrapolates from a hypothetical example to a general conclusion, which is an apples‑to‑oranges comparison. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 3.78 of Indian tax on every Rs 115 a foreign cloud company pays a related Indian operator"* — The claim conflates the **15% safe-harbour margin (Rs 15 on Rs 100 costs)** with the **25.17% corporate tax rate applied to that margin (Rs 3.78 tax on Rs 15 profit)**, but the **Rs 115 figure is incorrect**. The foreign company pays **Rs 115 total to the Indian operator (Rs 100 costs + Rs 15 margin)**, but the **Rs 3.78 tax is only on the Rs 15 margin**, not per Rs 115. The phrasing misleads by implying Rs 3.78 tax is levied on every Rs 115 paid by the foreign company (which would be ~3.3% of Rs 115, but the tax is only on the Rs 15 margin, not the full Rs 115). [confidence: high]

- *"The Finance Minister offered foreign cloud companies a tax holiday to 2047: if they serve customers outside India from data centres in India, that income is exempt."* — The **2047 deadline is incorrect**. The **tax holiday applies to tax years ending on or before 31 March 2047**, meaning the exemption covers **tax years from FY 2026–27 to FY 2046–47 (21 years, not 22)**. The phrasing "to 2047" is technically accurate for the calendar year but misleading in economic terms (as it implies 22 years of exemption). [confidence: high]

---
**INTERPRETATION ERRORS:**
- *"India still taxes the Indian operator’s 15% margin, but no estimate of what the exemption costs has been published."* — While the **15% safe-harbour tax is correctly identified**, the claim **fails to distinguish between the tax collected on the Indian operator’s profit and the revenue forgone from the foreign company’s exempted income**. The **Rs 3.78 tax per Rs 115** is a **small fraction of the total exemption** (which could be **orders of magnitude higher**—e.g., if the foreign company’s global cloud revenue from Indian capacity is Rs 1,000 crore, the exemption could be **Rs 1,000 crore minus Rs 3.78 crore tax**, a negligible offset). The article **understates the scale of the forgone revenue** by focusing only on the Indian operator’s tax. [confidence: high]

- *"The Act was introduced on 4 August, passed by both Houses by 10 August, and received assent on 17 August, replacing an ordinance issued in June."* — The **timeline is factually correct**, but the **causal claim that the August Act "replaces" the June ordinance** is **incomplete**. The ordinance was **repealed by the Act**, but the **new provisions (e.g., leasing flexibility, no notifications)** were **not fully defined**—they are now subject to **future rules to be prescribed by the government**. The article **overstates certainty** by implying the Act fully operationalizes the scheme when key details remain pending. [confidence: high]

---
**OUTDATED DATA:**
- *"Rs 3.78 of Indian tax on every Rs 115 a foreign cloud company pays a related Indian operator"* — The **safe-harbour margin (15%) and corporate tax rate (25.17%)** are correct as of the **2026–27 Budget**, but **no official revenue-forgone estimate exists for the data-centre exemption**. The article cites **no newer fiscal data** (e.g., **Budget 2027–28 or the Finance Ministry’s latest "Statement of Revenue Forgone"**) to confirm whether this exemption was **retained, modified, or quantified** in subsequent years. [confidence: high]
  - **Series to re-check:** *Finance Ministry’s "Statement of Revenue Forgone" (Annual Budget Documents)*; **latest fiscal data post-2026–27**.

- *"The government-securities exemption, which the June ordinance introduced, is the costliest-looking change for the exchequer: foreign investors’ interest income from government bonds was previously taxed at 20%."* — While the **20% tax rate was correct for FY 2025–26**, the **June 2026 ordinance and August 2026 Act** may have been **amended or superseded** in later fiscal years (e.g., **Budget 2027–28**). The article **does not verify whether this exemption was extended, reduced, or replaced** in subsequent legislation. [confidence: medium]
  - **Series to re-check:** *Income-tax Ordinance (Section 115AD) and Budget documents for FY 2027–28 onward*.
