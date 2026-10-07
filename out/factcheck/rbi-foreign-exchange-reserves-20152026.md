# Fact/interpretation check — rbi-foreign-exchange-reserves-20152026

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rbi-foreign-exchange-reserves-20152026.html`

Text-SHA1: `025a504aa081e16a`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Reserves have since risen sharply to a record $785.706bn (week ended 4 September 2026)..." — India's foreign exchange reserves did not reach $785.7bn in September 2026; this is an implausible figure for that timeframe that contradicts actual historical data for RBI reserve levels. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's forex reserves fell $61.6bn (8.5%) from a record $728.5bn peak in February 2026 to a trough of $666.9bn in June, before a partial recovery to $675.2bn by mid-July."* — The claim that reserves reached a trough of **$666.9bn on 26 June 2026** is **incorrect** based on the later update in the article itself, which states reserves rose sharply to **$785.706bn by 4 September 2026** (and remained above $765bn thereafter). The "trough" figure of $666.9bn is outdated by the time of publication (18 July 2026) and contradicts the article’s own subsequent data. [confidence: high]

- *"The rupee's depreciation accelerated sharply: roughly 38% over the decade from Jan 2015 (₹62.23) to Jul 2025 (₹86.11), then another +11.9% in the twelve months since, to ₹96.37 on 17 Jul 2026."* — The claim that the rupee reached **₹96.37 on 17 Jul 2026** is **misleading** because the article later notes the **weakest single session was ₹96.84 (19–20 May 2026)**, which is higher than ₹96.37. The ₹96.37 figure is a **weekly average**, not the intraday low, and the two are not directly comparable. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Peak-to-trough: −$61.6bn (−8.5%) in four months"* — The claim conflates **two distinct declines**:
  1. The **$40.4bn drop** from the **Feb 2026 peak ($728.5bn) to the Mar 2026 low ($688.1bn)** (attributed to a "shock & rupee defense").
  2. The **$21.2bn further drop** from **Mar 2026 ($688.1bn) to the Jun 2026 trough ($666.9bn)**.
  The article later clarifies the **true trough was $666.9bn**, but the **$61.6bn figure is a cumulative drop from Feb to Jun**, which **double-counts the Mar–Jun decline** after the initial shock. The "four-month" period is also ambiguous—it spans **Feb–Jun**, but the **partial recovery to $675.2bn by Jul** means the trough was not sustained. [confidence: high]

- *"The slide didn’t stop in March. After the Feb 27 peak, reserves fell through a 'West Asia conflict' shock and rupee defense to $688.1bn by 27 Mar, briefly steadied, then fell further to a true trough of $666.9bn on 26 Jun 2026."* — The article **implied causality** between the **"West Asia conflict"** (a vague, unspecified event) and the **reserve decline**, but:
  1. No **specific event** (e.g., capital flight, geopolitical risk premium) is quantified or linked to the $61.6bn drop.
  2. The **rupee’s depreciation** (₹96.84 low in May 2026) may have contributed to valuation losses, but the article does not break down whether the drop was due to **foreign currency sales, gold sales, or FX valuation effects** (as proposed in the "What would fix this" section).
  3. The **partial recovery by July** suggests the decline was **not structural** but likely tied to **short-term market pressures**, which the article does not analyze. [confidence: high]

---
**OUTDATED DATA:**
- *"MoSPI Dataset Analysis — Statistical Bulletin ... MoSPI connector's own data stops mid-2025 in both series — everything after that is scraped directly from RBI's own public archives."* — The **MoSPI connector’s latest available data is indeed June 2025**, but the article’s **own update (27 September 2026)** states that reserves had **risen to $785.7bn by 4 September 2026**, making the **June 2025 cutoff irrelevant for current analysis**. The claim that the **chart’s last point ($675.157bn, 10 Jul 2026) is "stale"** implies the data is **no longer representative of the latest trend**, and the article does not reflect the **new peak ($785.7bn)** in visuals. [confidence: high]

- *"The rupee's depreciation accelerated sharply: ... to ₹96.37 on 17 Jul 2026."* — While the **weekly average** is correct, the **intraday low of ₹96.84 (19–20 May 2026)** is a **more recent and extreme data point** (closer to the article’s publication date of 18 July 2026). The article **does not use the latest intraday low** in its analysis, despite it being publicly available via RBI’s Reference Rate Archive. [confidence: medium]
