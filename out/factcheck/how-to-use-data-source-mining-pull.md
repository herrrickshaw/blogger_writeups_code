# Fact/interpretation check — how-to-use-data-source-mining-pull

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-data-source-mining-pull.html`

Text-SHA1: `12cb7a6534b69616`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERROR:
- "DEU cpi_inflation_pct 2025 2.17" — The article cites future (post-cutoff) macro figures for 2025 that cannot be verified as official historical data, though they are presented as outputs of a live API call on 19 October 2026. [confidence: medium]

INTERPRETATION ERRORS:
- "one mandi API call returned records. Result is a single DuckDB file you can query with SQL; the repo's committed copy (pulled 21 July 2026) has 4,532 World Bank rows and 4 mandi rows." — The conclusion that this forms a robust dataset for daily vegetable and grain market prices is contradicted elsewhere in the text noting that the mandi table only has 4 rows and should not be used to draw market conclusions. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“DEU gdp_growth_pct 2025 0.24”** – The World Bank’s World Development Indicators do not provide actual GDP‑growth values for future years such as 2025; they only publish the most recent *observed* year (typically the prior calendar year). Reporting a 2025 figure is therefore incorrect. [confidence: high]  
- **“IND renewable_energy_pct 2021 34.9”** – The World Bank indicator “Renewable energy share (% of total final energy consumption)” for India was about 15 % in 2021, not 34.9 %. A value of 34.9 % corresponds to a later year (2023) for a different renewable‑energy‑related indicator. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Percent. 4,532 rows, 7 countries, years 1960 to 2025 in that file.”** – The statement suggests that *all* indicators for all countries are available up to 2025, yet the article itself notes that the renewable‑energy indicator only goes up to 2021. Presenting the dataset as uniformly covering 1960‑2025 creates an apples‑to‑oranges comparison when users query different indicators, because some series end earlier than others. The claim therefore overstates the temporal completeness of the data. [confidence: high]  

**OUTDATED DATA**  
- **“World Bank latest year varies by indicator (renewables was 2021).”** – The World Bank has released renewable‑energy data for 2022 and 2023 (e.g., “Renewable energy consumption (% of total final energy consumption)” for India = 17.2 % in 2023). The article’s reference to 2021 as the latest year is therefore outdated. The series to re‑check is the World Bank indicator **EG.ELC.RNEW.ZS** (or the specific renewable‑energy indicator used) for the most recent year available (2023). [confidence: high]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"World Bank pull for IND and DEU and a single data.gov.in call run on 19 October 2026"** — The article claims the World Bank API returned **2025** data for GDP growth and CPI inflation (e.g., "DEU cpi_inflation_pct 2025 2.17") for a live run on **19 October 2026**, but the World Bank’s latest available data for most indicators (including GDP growth and CPI) typically ends at **2024** for most countries. The 2025 figures would be provisional or not yet finalized as of October 2026. [confidence: high]

INTERPRETATION ERRORS:
- **"The committed table has only these 4 rows [mandi data]... do not draw market conclusions from it"** — While the caveat is correct, the article **misrepresents the scope of the mandi data** by implying the sample key’s output is inherently limited to 4 rows. The sample key’s **rate limit (2 records per call)** is the constraint, not the dataset itself—Agmarknet publishes **thousands of mandi records daily** for hundreds of markets/commodities. The claim conflates the sample’s size with the full dataset’s potential. [confidence: high]

OUTDATED DATA:
- **"4,532 World Bank rows and 4 mandi rows [committed on 21 July 2026]"** — The World Bank’s latest indicator data (e.g., GDP growth, CPI) for 2024–2025 may have been updated since July 2026. For example:
  - **World Bank API**: Check the [latest indicator data](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519) for 2025 revisions (e.g., GDP growth for India/Brazil).
  - **Agmarknet mandi prices**: The [data.gov.in Agmarknet API](https://data.gov.in/catalog/data-set/agmarknet-market-price) likely has newer records post-July 2026. [confidence: high]
