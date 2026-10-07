# Fact/interpretation check — fci-storage-scenario-capacity-stock-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fci-storage-scenario-capacity-stock-and.html`

Text-SHA1: `2ed944d764044a63`

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
- *"FCI storage scenario rose from 851.54 LMT (2018) to 917.83 LMT (2025)"* — The 2018 figure (851.54 LMT) includes **FCI+State covered+CAP capacity**, but the 2025 figure (917.83 LMT) is explicitly labeled as **FCI+State covered+CAP capacity**, which is a narrower subset than the 2018 baseline (which also included *total agri-storage* components like CAP). The claim conflates two different capacity definitions, making the 66 LMT increase misleading as a direct comparison. [confidence: high]

- *"FCI's own owned covered-storage capacity is only about 147 LMT of its roughly 482 LMT total"* — The 482 LMT figure cited in the article (from PIB PRID 2080612) is the **total FCI capacity (covered+CAP)**, not just *owned* capacity. The 147 LMT is the *owned covered* portion, but the 482 LMT includes **hired CAP and other rented storage**, which skews the "70% hired" claim. The article’s phrasing implies 482 LMT is purely owned capacity, which is incorrect. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The ₹1-lakh-crore cooperative plan targets 2,150 LMT total agri-storage"* — While the **700 LMT cooperative addition** is correctly framed as a structural shift (owned vs. hired), the **2,150 LMT target** is presented as a direct replacement for the existing system’s constraints. However, the **907 LMT 2021 peak** was a **temporary stockpile**, not a capacity ceiling—India’s procurement and buffer norms (e.g., 25–30% of production) inherently require **cyclical surpluses** far exceeding 907 LMT. The plan’s 2,150 LMT target is **not a fix for structural rental costs** but rather an **arbitrary expansion target** that may still face procurement-driven stockpiling pressures. [confidence: high]

- *"The 900+ LMT chart figure above is FCI+State combined, a different, larger base"* — This claim is **partially correct** but misleading in context. The **907 LMT (2021) peak** was **central-pool stock** (FCI+State), but the **851.54 LMT (2018) baseline** was **total FCI+State covered+CAP capacity**, not a direct comparison. The article treats these as interchangeable bases for growth (851→918→2,150), but the **2021 spike was a usage spike, not a capacity expansion**—the 907 LMT exceeded the **effective covered capacity** (not the theoretical 917.83 LMT in 2025), forcing spillover into CAP. The logic conflates **capacity** and **stock levels**. [confidence: high]

---
**OUTDATED DATA:**
- *"FCI storage capacity rose from 851.54 LMT (2018) to 917.83 LMT (2025)"* — The **2025 figure (917.83 LMT)** is from PIB PRID 2172351 (July 2025), but **no official Year-End Review for 2024–25** has been published yet (as of mid-2024). The article cites "Year-End Reviews 2024/2025" as pending, implying the 917.83 LMT may not yet be realized. Re-check: **DFPD’s latest Foodgrain Bulletin (2024–25)** or **FCI’s annual report** for actual 2024–25 capacity. [confidence: high]

- *"FCI 1,923 warehouses / 371.93 LMT (01-07-2023)"* — The **371.93 LMT** figure (from PIB PRID 1945170) is **covered storage only**, but the article later uses it to imply **total FCI capacity** (including CAP). For consistency, re-check: **FCI’s latest "Warehouse Inventory Report"** (e.g., 2023–24) for **total covered+CAP capacity** as of March 2024. [confidence: medium]
