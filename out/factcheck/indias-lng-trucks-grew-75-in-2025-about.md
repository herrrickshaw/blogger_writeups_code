# Fact/interpretation check — indias-lng-trucks-grew-75-in-2025-about

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-lng-trucks-grew-75-in-2025-about.html`

Text-SHA1: `0a65f2681fe64f3c`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "forecasts from major players and Vahan registration estimates going into the year pointed to roughly three times that growth. Instead, some retail LNG stations have shut for lack of truck traffic to serve..." — Vahan dashboard data does not historically break out LNG vehicles as an independent category in a manner that allows major industry players to derive reliable baseline registration estimates or triple-growth forecasts directly from it. [confidence: medium]

INTERPRETATION ERRORS:
- "forecasts from major players and Vahan registration estimates going into the year pointed to roughly three times that growth... against an industry expectation of roughly 3×" — The text conflates a 3x growth *rate* with a 3x magnitude miss. If actual growth was 75% (+0.75), an expectation of "roughly three times that growth" implies an expected growth rate of roughly 225%, whereas the table and later text define the expectation as "roughly 3× the actual 75% growth rate" (which would be 225%) yet elsewhere treats it as a 3x overall volume target or general miss without maintaining consistent mathematical phrasing. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's fleet of LNG-powered trucks grew 75% in 2025 — a real number, not a rounding error. It is also, by the industry's own earlier expectations, a disappointment: forecasts from major players and Vahan registration estimates going into the year pointed to roughly three times that growth."*
  — The claim conflates **growth rate (75%)** with **absolute growth target (~3× the fleet size, i.e., ~2,241 trucks)**. The article later clarifies the industry expected **tripling the fleet (from 747 to ~2,241)**, not tripling the growth rate (which would be ~225%). The headline’s phrasing ("grew 75%... against an industry forecast of roughly three times that growth rate") is misleading because it implies the forecast was for 225% growth (3×75%), when it was for 3× the fleet size. [confidence: high]

- *"China's heavy-duty truck sales that were LNG [captured] close to 30% in 2024"*
  — The article cites **Wood Mackenzie (May 2025)** and **IEEFA (May 2025)** for this claim, but the caveat states that China’s LNG-truck share has since **stalled due to surging electric truck sales**. The 30% figure is correct for 2024 but **no longer reflects current trends** (2026 data would show a decline). The article does not flag this as outdated, despite the caveat. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"India has none of the third lever: industry sources describe the Government of India as offering no transport-sector incentive for LNG trucks at all, leaving adoption to run on fuel-cost economics alone."*
  — The reasoning gap is that **fuel-cost economics alone** (as cited in the linked post) show LNG trucks have **total cost of ownership (TCO) roughly equal to diesel**, not meaningfully lower. The article then claims this explains the **75% growth shortfall relative to a 3× target**, but:
  1. The 3× target was **not based on cost parity** but on China’s subsidized adoption (where LNG was cheaper than diesel and backed by incentives).
  2. The article later admits **private players (Ultra Gas/Think Gas) are still expanding via corridor-first strategies**, suggesting demand exists in specific routes—implying incentives (e.g., guaranteed traffic) can bridge the gap even without subsidies. The claim that "no incentives = adoption fails" ignores these exceptions. [confidence: high]

- *"LNG combustion produces more nitrogen oxide, not less."*
  — While true for **some LNG engines** (depending on technology and aftertreatment), the article **generalizes this to all LNG trucks** without specifying:
  1. Whether the **2025 fleet** uses newer low-NOx LNG engines (e.g., SCR-equipped).
  2. How this compares to **older diesel trucks** (which may also emit higher NOx without modern controls).
  The claim **overstates the environmental disadvantage** of LNG without context, which weakens the argument that **lack of incentives is the sole barrier**. [confidence: medium]

---
**OUTDATED DATA:**
- *"India's fleet of LNG-powered trucks grew 75% in 2025 — 1,309 LNG trucks on Indian roads by end-2025, up from 747 in 2024"*
  — The article was **revised on 14 September 2026** but cites **Business Standard/Essar (Jan 2026)** for 2025 fleet counts. No indication whether **2026 data** (e.g., Vahan registrations for 2026) or **quarterly updates** (e.g., PNGRB station closures) have been released since. The claim is likely correct for 2025 but **should prompt a check for 2026 figures** (e.g., if the fleet grew further or refiner expansions resumed). [confidence: medium]

- *"China's heavy-duty truck sales that were LNG [captured] close to 30% in 2024"*
  — As noted above, this is **2024 data** but the article does not verify if **2025/2026 figures** (from Wood Mackenzie or IEEFA) have been updated to reflect the **stall in LNG growth** due to electric trucks. The claim risks being **misleading as a "current" benchmark**. [confidence: high]

---
**none found** (for other categories).
