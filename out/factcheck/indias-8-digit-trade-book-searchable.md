# Fact/interpretation check — indias-8-digit-trade-book-searchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-8-digit-trade-book-searchable.html`

Text-SHA1: `95cdf97b70f1bd66`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s biggest import line and the least usable series in the file: crude petroleum (27090010), flagged both RECODED and UNIT"* — The claim that crude petroleum is "the least usable series" is misleading because the **unit switch flag (UNIT)** is applied only to codes with >300× implied unit-value jumps (e.g., tonnes→kg). Crude petroleum’s unit-value change (316.1 → 0.5 $/kg) is explicitly cited as a **tonnes-to-kilogrammes switch**, which the article itself acknowledges as a **known nomenclature issue** (not a data error). The "least usable" label conflates a **documented data-quality flag** with a factual claim about usability. [confidence: high]

**INTERPRETATION ERRORS:**
- *"31.8 per cent of 2025-26 export value sits on codes that did not exist in 2017-18"* — This **overstates churn** because it ignores that **some "new" codes** are simply **renumbered versions of existing products** (e.g., smartphones under 71023910). The article later clarifies that **aggregating to HS4 headings reduces churn to <1%**, implying the 31.8% figure **double-counts structural changes** (retirements + renumberings) without distinguishing between them. [confidence: high]

- *"The export series has no FY2021-22; that gap is drawn as a break, not interpolated"* — While true, this **misleads readers** into assuming the gap is due to **missing data**, when the article later notes it’s likely a **publication delay** (not a data omission). The phrasing risks implying **FY2021-22 trade data is unavailable**, which contradicts the later caveat about **provisional FY2025-26 data**. [confidence: medium]

**OUTDATED DATA:**
- *"Source: DGCI&S TradeStat EIDB, FY2017-18–FY2025-26"* — The article cites **provisional FY2025-26 data** but does not clarify whether **FY2024-25 has been finalized** (as of August 2026). The **latest official TradeStat release** may include revised FY2024-25 figures. [confidence: medium]
  *(Series to re-check: DGCI&S TradeStat EIDB; newer period: FY2024-25 finalized data if available.)*

---
**Note:** The article’s **data-quality flags** (RECODED, UNIT, RETIRED) are **correctly applied** and not flagged as errors. The issues above stem from **claims that stretch beyond the data’s limitations** or **ambiguous phrasing**.
