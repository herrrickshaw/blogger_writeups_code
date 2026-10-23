# Fact/interpretation check — india-tracks-every-taxpayer-in-minutes

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-tracks-every-taxpayer-in-minutes.html`

Text-SHA1: `f8f3a7eb80b6658f`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8542, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India has had a permanent tax number since 1972 and now issues one in about ten minutes"* — The **Permanent Account Number (PAN)** was introduced in **1972**, but the **computerized 10-digit PAN format** (as used today) was only standardized in **1995** (via the Income Tax Act amendments). The claim conflates the original ward-level GIR numbers (1972) with the modern PAN system. [confidence: high]

- *"Indian IT firms built the tax system"* — While **Infosys, L&T Infotech, and LTIMindtree** were key contractors for components like the **Central Processing Centre (CPC), GSTN, and PAN 2.0**, the **core tax infrastructure (e.g., TDS, GSTN architecture)** was designed by government agencies (e.g., CBDT, GSTN Authority) with IT firms as implementers. The phrasing implies sole ownership by Indian IT firms, which oversimplifies the public-sector role. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The gap at home is not a shortage of technology or engineers. It is the difference between a system the state needed to collect money and a system it has chosen to fund modestly and leave optional."*
  **Gap in reasoning:** The article correctly identifies **compulsion (mandate) and funding** as key differences, but it **overstates the "technology gap"** by ignoring that the **health system’s voluntary adoption is also a *design choice***—not just a funding issue. For example, **eSanjeevani (teleconsultation)** runs at scale because the government is **both provider and payer**, creating a **perverse incentive** (unlike health, where private providers lack such alignment). The claim implies technology is the limiting factor, but the **lack of a single payer or legal deadline** (as seen in Asia) is the structural flaw. [confidence: high]

- *"India’s IT companies built the tax system and a business processing health data for American insurers..."*
  **Misattribution of causality:** The article suggests Indian IT firms’ **export success in foreign health systems** directly contrasts with India’s domestic health digitalization **because of a "lack of mandate and money."** However, the **same firms (Infosys, TCS, Cognizant) have not built the core of India’s health stack** (e.g., ABHA, claims exchange)—their involvement is limited to **outsourced components** (e.g., vendor support for ABHA registration). The comparison **falsely equates export capability with domestic system-building capacity**, ignoring that **foreign systems operate under different regulatory mandates** (e.g., HITECH Act in the U.S.). [confidence: high]

---
**OUTDATED DATA:**
- *"1.3 of 5.47 lakh Health facilities actually connected to the digital health mission, against those registered"* —
  **Series to re-check:** *National Health Authority’s "ABDM-enabled facilities" registry* (updated as of **September 2026** in the article’s own updates). The **latest official count** (from PIB’s 17 September 2026 update) is **~1.3 lakh connected facilities**, but the **total registered facilities** may have changed post-2025 (no newer source cited). [confidence: medium]

- *"US$6.35bn Cognizant’s health-sciences revenue in 2025, 30% of the total, from a workforce more than 85% in India"* —
  **Series to re-check:** *Cognizant’s 2025 10-K filing* (latest available). While the **2025 figure is correct**, the **2026 fiscal year (ending March 2027)** may show revised revenue streams (e.g., post-Optimum Healthcare IT acquisition). The article does not verify if this **$6.35B figure includes 2026 earnings** or is strictly CY2025. [confidence: medium]

---
**Note:** The article’s **disclaimer about outdated data** (e.g., ABHA count updated to 97.6 crore) is acknowledged, but the **structural claims (e.g., "no large Indian IT firm built the health stack")** lack **recent verification** (e.g., NHA procurement records post-2025). The **export vs. domestic comparison** also assumes static conditions, ignoring potential **post-2025 policy shifts** (e.g., AI-driven domestic health digitization).
