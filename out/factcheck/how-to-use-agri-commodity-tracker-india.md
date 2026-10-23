# Fact/interpretation check — how-to-use-agri-commodity-tracker-india

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-agri-commodity-tracker-india.html`

Text-SHA1: `afb65e0bab171ca7`

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
- **“Wood” price quoted in rupees per quintal (1005 → 605 ₹/qtl, –39.8 %)** — Wood is not an agricultural commodity sold in the Indian APMC mandi system, and it is never priced in rupees per quintal (a unit used for grain, pulses, etc.). Agmarknet does not publish wood prices; the figure is therefore a mis‑statement of what the source actually contains. [confidence: high]

**INTERPRETATION ERRORS**
- none found

**OUTDATED DATA**
- **“9 World Bank agriculture indicators”** — The article states that the tracker includes “9 World Bank agriculture indicators.” The World Bank’s “World Development Indicators” and “Agriculture, forestry and fishing” databases have been expanded several times since the last release (the most recent update was in 2024 and added more than 20 agriculture‑related series). The count of “9” is likely outdated; the repository should be re‑checked against the current World Bank API to confirm the exact number of indicators now available. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"13,375 rows in the fullest day (24 Sep 2026)"** — The article states this as a fact, but the screenshot query (`select pulled_on, count(*) n, count(distinct commodity) com, count(distinct state) st from m group by 1 order by 1 desc limit 4`) shows **13,375 rows for 24 Sep 2026**, while the table below it lists **13,375 rows for 24 Sep 2026** but the *next row* (23 Sep) shows **11,583 rows**, not 13,375. The claim conflates the highest row count (24 Sep) with the highest *commodity* count (227 on 24 Sep), which is inconsistent with the phrasing. [confidence: high]

- **"The run also showed a trap worth knowing: a naive commodity-average day-on-day comparison put 'Wood' at -39.8%..."** — The claim that "Wood" prices dropped **39.8%** is plausible in magnitude but misleading in context. The article later clarifies that this is due to **changes in which markets reported that day**, not actual price movement. The initial claim lacks this critical caveat, which undermines its validity as a standalone fact. [confidence: high]

INTERPRETATION ERRORS:
- **"The snapshot ends on 24 Sep 2026 (pulled dates 21 Jul to 24 Sep 2026), so it is not current as of the post date."** — The article uses the **date of the latest data (24 Sep 2026)** to argue the dataset is "not current" for the **post date (19 Oct 2026)**, but this ignores that the data is **open-source and actively updated** (as evidenced by the GitHub repo’s collectors and the note that "days before 23 Jul 2026 are stubs"). The claim conflates *static snapshot* with *ongoing data collection*, implying stagnation where none is implied. [confidence: high]

- **"Always compare like with like."** — While the article correctly demonstrates the pitfalls of **naive commodity-average comparisons** (e.g., Wood’s -39.8% vs. flat prices in like-for-like checks), it does not address that **some commodities may lack sufficient "same-market" overlaps** for meaningful comparisons. The blanket advice ignores cases where only a subset of markets report consistently, making the recommendation overly simplistic. [confidence: medium]

OUTDATED DATA:
- **"463,023 mandi price rows in the committed snapshot"** — The snapshot is explicitly dated **21 Jul to 24 Sep 2026** (as per the query output). While the article notes it’s not "current," it does not clarify whether a **newer snapshot exists** (e.g., post-24 Sep 2026 data). Readers cannot verify if the count is still accurate without checking the latest GitHub release or the `mandi_prices_snapshot.csv` file. [confidence: high]
  - *Series to re-check*: GitHub repo’s `data/mandi_prices_snapshot.csv` or `agri.duckdb`; newer period unknown (likely post-24 Sep 2026 if updated).

- **"9 World Bank agriculture indicators"** — The article lists World Bank data as included but does not specify **which indicators** or their **latest release dates**. The World Bank’s [Agriculture & Rural Development](https://data.worldbank.org/topic/agriculture-rural-development) page may have newer data (e.g., 2025–2026 estimates). [confidence: medium]
  - *Series to re-check*: World Bank’s [Agriculture & Rural Development Data](https://data.worldbank.org/topic/agriculture-rural-development); newer period likely 2025–2026.
