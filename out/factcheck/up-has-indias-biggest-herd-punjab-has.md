# Fact/interpretation check — up-has-indias-biggest-herd-punjab-has

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/up-has-indias-biggest-herd-punjab-has.html`

Text-SHA1: `33bb58905ddf2c4a`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The sector's compound annual growth rate from 2014-15 to 2023-24 was 12.77%, and livestock now contributes more than 31% of agricultural GVA and 5.5% of India's total GVA." — The 12.77% figure typically represents the nominal value growth (or value output growth at current prices) of the livestock sector over certain periods, but attributing a 12.77% real CAGR or conflating nominal output value growth with sector growth rates against real GDP misstates standard national accounts conventions where agricultural sub-sector CAGRs are usually lower in real terms. [confidence: medium]

INTERPRETATION ERRORS:
- "The 21st Livestock Census ... was launched on 25 October 2024, with the ministry stating it was 'likely to be completed by 31st March, 2025.' On that exact date, in a written Lok Sabha reply ... the same ministry stated: 'the enumeration work of 21st Livestock census is ongoing' — and answered the question using 20th Census figures instead." — The author treats a missed administrative target completion date as evidence of systemic failure or unusual delay, while large-scale decentralized national enumerations (like censuses involving millions of households and livestock across villages) frequently experience timeline extensions during the fieldwork phase. [confidence: low]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The 21st Livestock Census was launched on 25 October 2024 with a target completion date of 31 March 2025 — and on that very date, in a separate written Lok Sabha reply, the ministry itself confirmed the enumeration was still ongoing"* —
  The claim conflates two separate dates: the **31 March 2025** target completion date (as per the 2024 launch announcement) and the **25 March 2025** Lok Sabha reply (where the ministry stated enumeration was "ongoing"). The article incorrectly implies the 31 March deadline was met, but the reply explicitly states work was still in progress as of **25 March 2025** (6 days before the target). The article does not correct this misalignment between the stated target and the actual status at the deadline.
  [confidence: **high**]

- *"Uttar Pradesh's buffalo count — 3.3 crore — is more than double the next-largest state's"* —
  The next-largest buffalo population in the 2019 census is **Madhya Pradesh (1.03 crore)**, not a state with ~1.65 crore (which would be double 3.3 crore). The correct comparison is that Uttar Pradesh’s buffalo count (~3.3 crore) is **~3.2 times** Madhya Pradesh’s (~1.03 crore), not double.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"The headcount Parliament was given is a 2019 snapshot... Until the 21st Census numbers are released, every state-wise livestock-population figure the government cites — including the one placed on the record in December 2025 — is a 2019 measurement of a sector that has since grown at nearly 13% a year."*
  The article assumes the **12.77% CAGR (2014–2023)** applies uniformly to **all states** and directly to **livestock population growth**, but:
  1. The CAGR cited is for **milk production**, not livestock numbers. The article later acknowledges the 2019 census cannot track population changes post-2019 without the 21st Census.
  2. Even if population grew at ~13%, **milk yield per animal** (e.g., Punjab’s 14.1 kg/day vs. UP’s 9.16 kg/day) suggests **state-specific productivity shifts**—not just scaling. The article conflates aggregate growth with state-level distribution, ignoring that some states may have **declining herds** (e.g., Punjab’s smaller herd but higher yield) while others expand.
  [confidence: **high**]

- *"Punjab is the inverse case... its herd is a fraction of Uttar Pradesh's — yet it posts the highest cattle yield rate in the country... This article does not establish whether the 21st Census's enumeration itself has since finished..."*
  The article **correctly** notes the disconnect between herd size (2019 data) and yield (2024–25 data) but **fails to address causality**: Punjab’s high yield could stem from:
  - **Better feed/breeding** (e.g., Sahiwal cattle),
  - **Underreporting in the 2019 census** (e.g., if Punjab’s herd grew faster than other states),
  - **Data gaps** (e.g., the 21st Census may show Punjab’s herd expanded disproportionately).
  The article **does not rule out** that Punjab’s yield advantage is partly due to **updated population data** (which it cannot verify due to the 21st Census’s absence). It treats yield as a standalone efficiency metric without probing whether **population changes** (if any) might explain the gap.
  [confidence: **high**]

---
**OUTDATED DATA:**
- *"53.68 cr India's total livestock population, 20th Livestock Census (2019)"*
  — **Series to re-check**: *21st Livestock Census (ongoing as of March 2025, per PIB replies)*. The article notes the 21st Census was launched in **October 2024** with a **March 2025 target**, but no results have been published. The **latest official livestock population figure** should reflect the 21st Census (if completed) or a provisional update from DAHD.
  [confidence: **high**]

- *"12.77% Livestock sector's CAGR, FY2014-15 to FY2023-24"*
  — **Series to re-check**: *DAHD’s latest Basic Animal Husbandry Statistics (2025–26, if released)*. The article cites **BAHS 2025 (Nov 2025)**, which covers **2024–25 production data**. For CAGR, the next logical update would be **FY2024–25 to FY2025–26** (if available) or a revised **FY2014–15 to FY2024–25** range (extending the period by one year). The current claim stops at FY2023–24.
  [confidence: **medium**]

---
**Note**: The article’s **milk production data (247.87 MT, 2024–25)** and **global rankings (1st in milk, 2nd in eggs, 4th in meat)** are not flagged as outdated because:
- The **DAHD Basic Animal Husbandry Statistics 2025** (Nov 2025) is the **most recent official source** cited for these figures.
- No newer fiscal year (2025–26) data is referenced in the article or publicly available as of August 2026.
