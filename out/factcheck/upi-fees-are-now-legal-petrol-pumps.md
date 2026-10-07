# Fact/interpretation check — upi-fees-are-now-legal-petrol-pumps

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/upi-fees-are-now-legal-petrol-pumps.html`

Text-SHA1: `f30c8e6ebe2ecf6f`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The Taxation and Other Laws (Amendment) Bill, introduced 4 August 2026 , replaces that blanket ban... The pressure behind the change is documented — the Payments Council of India formally sought “urgent reconsideration” of zero-MDR in March 2025, and the budget line that compensated banks for carrying free UPI was cut from ₹2,000 crore to ₹437 crore this fiscal year." — Section 10A of the Payment and Settlement Systems (PSS) Act was originally inserted by the Finance Act 2021 (effective retrospectively from January 1, 2020), and amendments to payment infrastructure acts or tax laws in India are introduced through Finance Bills or specific legislative amendments rather than a "Taxation and Other Laws (Amendment) Bill" dated August 2026. Furthermore, referencing August 2026 events as historical facts contradicts established legislative timelines known as of the knowledge cutoff. [confidence: medium]

INTERPRETATION ERRORS:
- "An MDR is levied on the merchant, and both network rules and the 2017 settlement history say it cannot simply be surcharging onto the customer. But incidence has a way of travelling, and the per-fill arithmetic is what every constituency — dealer, fleet operator, commuter — will actually argue about." — The author conflates statutory legal incidence with economic incidence. While legal incidence falls on the merchant due to network anti-surcharging rules, the economic incidence (who actually bears the burden via higher prices or altered terms) does not travel via a simple per-fill surcharge arithmetic on regulated petroleum products, whose retail selling prices (RSP) are tightly controlled and computed centrally based on state taxes and dealer commissions rather than freely adjusted by individual dealers to absorb merchant fees. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The shield came off on 4 August [2026]: the government may now notify which payment modes stay fee-exempt, and the rest may lawfully carry a merchant discount rate rate."* — The amendment was enacted on **4 August 2026**, but the **actual MDR notification** (0.4% ad-valorem + ₹5 flat fee for fuel) was published **14 September 2026** (MoF gazette) and operationalized **15 October 2026**. The article conflates the legislative power to notify fees with the *timing* of the first notification, which occurred **5 weeks later**. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"A fee on the whole ticket, paid out of a 3.87% slice of it"* — The claim conflates **gross dealer margin (3.87%)** with **net payment acceptance costs**. The 3.87% is a **blended margin** (comprising excise, VAT, oil company markup, and *gross* dealer commission), not the portion specifically allocated to payment processing. The article later acknowledges this ambiguity ("the commission must also fund staff, power, evaporation losses and licence fees"), but the initial framing risks implying the entire 3.87% is at risk from MDR, which would be incorrect. [confidence: high]

- *"The pump’s float is the ATM’s inventory"* — While conceptually true, this oversimplifies **cash logistics constraints**. The article ignores:
  1. **RBI’s currency-fitness rules** (e.g., note sorting, recycling requirements) that prevent direct drawer-to-dispenser cash dispensing without a recycler machine.
  2. **Operational friction**: Fuel pumps handle **high-value, low-denomination notes** (e.g., ₹2000/₹500), which are less efficient for ATMs (optimized for ₹200/₹100). The "float" analogy assumes seamless interchangeability, which isn’t feasible without additional infrastructure. [confidence: high]

---
**OUTDATED DATA:**
- *"India runs roughly 2.58 lakh ATMs and cash recyclers (February 2025)"* — As noted in the article’s update, **RBI shifted WLA-operator reporting to CIMS in April 2026**, and **industry coverage in April 2026** identified **only five licensed WLA operators nationally**, with the largest (Indicash) at **~15,000 machines**. The 2.58 lakh figure (from Feb 2025) is outdated and lacks granularity. Re-check: **RBI’s CIMS reports (quarterly)** or **RBI’s ATM/WLA FAQ updates** for the latest counts by deployment type (urban/rural). [confidence: high]

- *"Fuel stations in SBI’s Cash@PoS list: 693"* — The article cites **July 2026 data** but notes the **join against PPAC’s 103,682 outlets failed on source data quality**, leaving only **18 matches**. The 693 figure is **not auditable** as of the article’s publication date. Re-check: **PPAC’s July 2026 outlet-level dataset** (if updated) or **direct data from IOCL/BPCL/HPCL** (requested in the "What would fix this" section). [confidence: high]
