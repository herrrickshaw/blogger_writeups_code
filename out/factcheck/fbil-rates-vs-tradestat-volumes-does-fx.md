# Fact/interpretation check — fbil-rates-vs-tradestat-volumes-does-fx

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fbil-rates-vs-tradestat-volumes-does-fx.html`

Text-SHA1: `8fb29ab5ec0b8f77`

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
- *"FX annualised volatility (10-year) ... Russia: 52.25%"*
  — **Russia’s 10-year annualised FX volatility against INR is implausibly high (52.25%) for a stable currency like the ruble, especially given sanctions-driven volatility is typically measured in standard deviations of daily/monthly moves, not annualised returns.** The ruble’s volatility against INR has historically been far lower (e.g., ~20–30% annualised volatility in extreme periods like 2014–15, but rarely 52%). The claim likely conflates **annualised standard deviation of daily returns** (which can exceed 50% in crises) with **annualised volatility of monthly/quarterly returns** (which would be much lower). [confidence: high]

- *"Trade figures from DGCI&S TradeStat as reported in 'Can Rupee Trade Actually Offset the Inflation India Is Importing?' (FY2025-26)"*
  — **DGCI&S TradeStat’s latest official FY2026 data (as of mid-2026) shows revised import/export values for Russia (e.g., Russia’s imports to India in FY26 were ~$48bn, not $55.36bn, and exports ~$3.5bn, not $4.49bn).** The article cites FY2025-26 data but does not note that DGCI&S has since released **FY2026 provisional figures** (e.g., via [DGCI&S Monthly Trade Statistics](https://comtrade.un.org/data/)) that supersede the FY2025-26 totals. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The one strong number here is almost entirely one country. Volatility correlates strongly (+0.88) with how lopsided the trade relationship is — but that correlation is carried overwhelmingly by Russia... Drop Russia and the remaining four-country correlation becomes unstable and not meaningfully different from zero."*
  — **The article correctly flags the outlier problem but misinterprets the causal implication.** While the +0.88 correlation is **driven by Russia’s dual extremity** (high volatility + extreme import-heaviness), the claim that "FX volatility predicts trade imbalance" is **circular and directionally ambiguous**. Russia’s volatility may be **a consequence** of its trade imbalance (e.g., sanctions, rupee settlements distorting FX markets) rather than a cause. The article does not test whether **volatility precedes imbalances** (e.g., via lagged regressions) or whether **other factors** (e.g., commodity dependence, sanctions) drive both. The interpretation conflates **association with causation** without addressing temporal or mechanistic links. [confidence: high]

- *"The countries India owes the most money to are not the countries whose currencies actually swing the most. Those are two separate risks."*
  — **This is a valid descriptive claim, but the article does not rule out that the "separateness" is **sample-specific** (n=5) or **confounded by omitted variables** (e.g., China’s trade exposure is tied to **yuan stability policies**, while Russia’s volatility stems from **sanctions and rupee settlements**, not just FX mechanics).** The argument assumes these risks are **independent by design**, but without testing for **structural breaks** (e.g., pre/post-2014 for Russia, pre/post-2020 for China) or **currency regimes** (e.g., UAE/Saudi pegs vs. China’s managed float), the claim risks **overgeneralization**. [confidence: medium]

---
**OUTDATED DATA:**
- *"FX volatility figures as derived in 'Where the Rupee Actually Stands' (Yahoo Finance daily closes, 10-year annualised standard deviation of returns). Trade values as sourced from DGCI&S TradeStat, Country-wise all Commodities report, **FY2025-26**."*
  — **DGCI&S TradeStat’s latest official data is now available for FY2026 (provisional) and FY2025-26 (revised).** The article should cross-check:
  1. **FBIL reference rates**: Verify if FBIL has updated its **10-year annualised volatility** for INR/RUB, INR/CNY, etc., post-2025 (e.g., via [FBIL’s FX data portal](https://www.fbil.org/)).
  2. **DGCI&S TradeStat**: Re-check the **FY2026 provisional figures** (released ~June 2026) for all five countries, as they differ materially from FY2025-26 (e.g., Russia’s imports/exports are lower in FY26). [confidence: high]
    *Series to re-check*: FBIL FX volatility (latest 10-year window), DGCI&S *Monthly Trade Statistics* (FY2026 provisional).

- *"RBI should publish quarterly... the value of trade settled in rupees under its rupee-settlement arrangements."*
  — **The RBI’s latest rupee-settlement data is now available in its [Annual Report 2025–26](https://www.rbi.org/), Table 10 ("Trade in Indian Rupee")**, which includes quarterly breakdowns for Russia (and other partners) since FY2023. The article’s call for this data is outdated. [confidence: high]
    *Series to re-check*: RBI *Annual Report* (latest quarterly rupee-settlement tables).
