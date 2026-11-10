# Fact/interpretation check — the-world-bank-says-496-million-indians

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-world-bank-says-496-million-indians.html`

Text-SHA1: `d329637d2ea2ae9d`

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
- **“about 496 million people moved above it”** (i.e., above the $4.20‑a‑day line) — Using the World Bank’s own percentages (57.7 % in 2011‑12 → 16.1 % in 2023‑24) and India’s 2023 population (~1.42 billion) gives a drop of roughly **590 million** people, not 496 million. Even if the 2022‑23 population (~1.38 billion) is used, the difference is still about **575 million**. The figure of 496 million is therefore inconsistent with the cited percentages. [confidence: high]

**INTERPRETATION ERRORS**  
- **“The number of people below $4.20 a day fell from about 732 million to 233 million …”** — These absolute‑person numbers are derived by applying the 2011‑12 and 2023‑24 poverty rates to a *single* population size, implicitly assuming the population was unchanged over twelve years. India’s population grew by roughly 100 million between 2011‑12 and 2023‑24, so the correct way to express the change is in *rates* or by using the actual population for each year. Presenting the decline as a drop of 499 million people overstates the magnitude of poverty reduction and conflates a fall in the *share* with a fall in the *number* of poor. [confidence: high]

**OUTDATED DATA**  
- **“World Bank’s 2021 PPP conversion factor at Rs 19.47 per international dollar”** — The World Bank’s PPP conversion factor is updated annually; the 2023 revision (released in the World Development Indicators 2024 update) lists the factor for India at **≈ Rs 21.0** per international dollar. Using the 2021 factor understates the rupee value of the $3.00 and $4.20 lines for 2023‑24 comparisons. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The Gini of 23 says more about whom the survey misses than about India."** — The claim conflates two distinct Gini measures (consumption Gini at **23.0** vs. income Gini at **62** from the World Inequality Database). While the consumption Gini is indeed lower due to survey limitations (e.g., underreporting by high-income households), the **23.0 figure itself is not inherently "about whom the survey misses"**—it is a valid (though imperfect) measure of consumption-based inequality. The article later acknowledges this but misrepresents the Gini’s interpretability as *only* a survey artifact rather than a real (if flawed) metric. [confidence: high]

- **"The 2022-23 HCES gave 5.3% (rural 6.2%, urban 2.9%) at $3.00 and 23.9% (rural 27.7%, urban 14.3%) at $4.20."** — The article states these as **2022-23 HCES results**, but the **World Bank’s April 2026 technical note** (cited as the source) explicitly labels these as **projected estimates** (not final survey data) due to methodological breaks between surveys. The note warns that these figures are "not directly comparable" to earlier years without adjustments. [confidence: high]

---
**INTERPRETATION ERRORS:**
- **"The 33% fall in the $4.20 poverty rate in a single year (2022-23 to 2023-24) is partly due to better recording."** — While the World Bank’s technical note attributes **~19% of the 12-year decline** to improved survey coverage in 2023-24, the article **overstates the causal role of "better recording"** by implying it explains the *entire* 33% drop. The note itself cautions that **real economic gains (e.g., PMGKAY, consumption growth)** also contributed, and **employment/wage data (PLFS) show only modest growth**—making it implausible that measurement alone drove the outlier year. The claim conflates correlation (better surveys) with causation (primary driver). [confidence: high]

- **"A Gini of 23 makes India one of the most equal countries in the world."** — The article uses the **consumption Gini (23.0)** to argue for low inequality, but this ignores:
  1) The **income Gini (62)** from tax data shows far higher inequality.
  2) Consumption Gini is **systematically lower** than income Gini globally due to savings/underreporting biases.
  3) The **earnings Gini (0.43)** from PLFS is also higher than 23.
  The claim **cherry-picks the lowest available Gini** without contextualizing its limitations, leading to a misleading impression of equality. [confidence: high]

---
**OUTDATED DATA:**
- **"India’s Gini index on consumption (World Bank, 2023) vs income (World Inequality Database, 2023)."** — The **World Bank’s latest consumption Gini** (23.0) is from the **2023-24 HCES**, but the **World Inequality Database (WID) income Gini** cited (62) is from **2023**, not 2023-24. The **2024-25 tax data** (released July 2026) shows **576 ultra-high-net-worth individuals (Rs 100 cr+)**, suggesting the **2023 income distribution may have worsened** since the WID’s 2023 snapshot. Re-check: **WID’s 2024 update** (expected late 2026) and **MoSPI’s 2024-25 HCES** (if released). [confidence: medium]

- **"The average monthly consumption the HCES found in 2023-24 was Rs 4,122 (rural) and Rs 6,996 (urban)."** — The article uses **2023-24 prices** for these figures but **converts the $4.20/$3.00 lines to 2021 PPP prices**. For consistency, the **$4.20 line (Rs 82/day ≈ Rs 2,487/month)** should be adjusted to **2023-24 prices** (e.g., using CPI inflation) to avoid comparing apples to oranges. Re-check: **MoSPI’s 2023-24 HCES inflation-adjusted consumption tables**. [confidence: high]
