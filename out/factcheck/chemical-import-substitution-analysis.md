# Fact/interpretation check — chemical-import-substitution-analysis

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/chemical-import-substitution-analysis.html`

Text-SHA1: `acfaecab94119839`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Total Investment (FY26–FY30): ₹1,78,630–1,79,230 crore (midpoint ≈ ₹1,78,930 crore, ~$21.4 billion at ~₹83.4/$1)" — The stated conversion yields approximately $21.44 billion, but ₹1,78,930 crore divided by 83.4 is approximately $21.46 billion, and summing the individual project costs (₹1,00,000 + ₹75,000 + ₹600–1,200 + ₹3,030) actually results in a range of ₹1,78,630 to ₹1,79,230 crore, which at 83.4 INR/USD is roughly $21.42 to $21.49 billion, making the precise single-point conversion of "$21.4 billion" mathematically inconsistent with the provided midpoint and ranges. [confidence: medium]

INTERPRETATION ERRORS:
- "Mixed public/private: BPCL is a government-owned (Maharatna PSU) refiner; RIL is a private company , not government capex; the Bina unit is BPCL-owned with L&T as EPC contractor." — The article groups these projects under a heading of "Public + Private" capex and evaluates them collectively as a single substitution strategy, but treats RIL's private investment as if it can be directly directed or planned alongside PSU projects through government policy levers, ignoring that private corporate capital allocation decisions operate on distinct commercial thresholds rather than mandated import substitution targets. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"ethylene was cited as 29011100 / $2,800M (the real line is 29012100, $44M)"** — The claim that the *original* article cited ethylene as **29011100 / $2.8B** is **incorrect**—the correction notice itself states the *original* figure was **$2.8B** (not $2.8M) but for the wrong HS code. The corrected value is **$44M** for **29012100**, but the original error was **$2.8B** (not $2.8M). [confidence: high]
- **"propylene as 29011200 / $1,400M (real: 29012200, $14M)"** — The original claim of **$1.4B** for **29011200** is **implausible** given the corrected value of **$14M** for **29012200**. The correction notice does not state the original figure was $1.4B—this appears to be a misinterpretation of the error magnitude. However, the **$1.4B claim itself is unsupported** by DGCI&S data (the corrected value is **$14M**). [confidence: medium]

*(Note: The correction notice clarifies that the original article’s figures for ethylene and propylene were **overstated by orders of magnitude**, but the exact original numbers are not provided. The above reflects the most plausible reconstruction of factual discrepancies.)*

---

**INTERPRETATION ERRORS:**
- **"Chapter 38 is labelled ‘Textile Auxiliaries, $620mn’ below. Authentic DGCI&S imports for Chapter 38 in FY2025-26 are $8,857M"** — The article **correctly identifies** that the original $620M figure was wrong but **fails to explain why the $8.86B figure (later corrected to $8.857B) is the "authentic" value**. The $8.86B figure is derived from **DGCI&S TradeStat**, but the article does not clarify whether this includes:
  1. **All sub-codes under Chapter 38** (which may include non-textile auxiliaries), or
  2. **Only the 77 deficit-running HS-8 lines** (as mentioned later).
  The **$5.32B gross deficit** and **$1.74B net deficit** imply a **subset of imports**, yet the $8.86B is presented as the **total chapter value without distinction**. This **double-counts risk**: the $8.86B may include non-substitution targets (e.g., auxiliaries with no domestic production gaps). [confidence: high]
- **"Tier 1 savings of $6.1 billion/year (FY30) are ‘HIGH confidence’ (80%)"** — The **80% confidence** is **misleading** because it is **derived from the now-retracted Tier 1 figures** (ethylene, propylene, PE, etc.), which were **based on incorrect HS codes and inflated import values**. The **corrected substitution exercise has not been performed**, so the $6.1B figure is **no longer valid**. The confidence level should be **suspended** until a **recomputed analysis** is done. [confidence: high]

---

**OUTDATED DATA:**
- **"Annual imports, $ billion (FY2025-26; reconciled total $74.37bn, corrected)"** — While the **correction notice (4 Aug 2026)** updates Chapter 38 to **$8.86B** (from $620M), the **full FY2025-26 import data for all chapters may still require verification against the latest DGCI&S TradeStat EIDB release**. The **reconciled total ($74.37B)** is now aligned with the corrected Chapter 38, but:
  - **No indication** whether the **other chapters (28, 29, 30–32, 39)** have been **fully rechecked** against the **latest TradeStat update** (e.g., if any minor code-level adjustments exist).
  - The **source series to re-check**: **DGCI&S TradeStat EIDB (FY2025-26)**. [confidence: medium]
- **"BHAVYA Rasayan Parks (3 sites) | ₹3,030 cr (FY28–30)"** — The **₹3,030 crore figure** is **not linked to a specific fiscal year breakdown** (e.g., annual capex milestones). While the **timeline (FY28–30)** is noted, the **source series to re-check** is:
  - **DCPC’s project-wise capex tracking** (if publicly available) or **BHAVYA Parks’ official financial updates**.
  The **site selection status ("ongoing")** suggests this may be **outdated** if new announcements have been made post-August 2026. [confidence: medium]
