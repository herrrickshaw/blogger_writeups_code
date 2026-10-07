# Fact/interpretation check — indias-60000-crore-api-push-traced-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-60000-crore-api-push-traced-to.html`

Text-SHA1: `87f3ed21e42a9739`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Investment is the one figure that moved more visibly: ₹4,814cr attracted by December 2025 against a ₹4,322cr committed figure" — This contradicts the earlier table in the same article which explicitly states that the total government outlay/committed figure for the Bulk Drugs PLI scheme is ₹6,940 crore (and ₹4,322cr is neither mentioned as the committed figure in the table nor does it mathematically align with the scheme's layout). [confidence: high]

INTERPRETATION ERRORS:
- "Against a China import bill running in the billions of dollars a year, ₹2,190–2,192 crore of cumulative import substitution since 2020 is real progress on individual molecules... but it has not moved the 43.45% headline number" — The reasoning compares a cumulative stock/flow metric of import substitution (₹2,190 crore total generated locally over several years) against an annual trade share percentage (43.45% of total annual imports) without normalizing them to the same annual denominator or accounting for total market growth, making it an apples-to-oranges comparison to claim the former mathematically "moves" the latter in a direct 1:1 manner. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"₹60,000 crore API push, announced in December 2025"* — The claim that this is a single, new scheme is incorrect; it is a roll-up of at least six pre-existing schemes (e.g., PLI schemes dating back to 2020, Biopharma SHAKTI announced in 2025) plus private co-investment. The ₹60,000 crore figure itself is a **misleading aggregation** of government outlays (~₹43,000–44,000 crore) plus expected private/state co-investment, not a single appropriation. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The Bulk Drugs PLI has made real (if still modest) progress"* — While the scheme has created capacity for 33 drugs (up from 26 in Sept 2025) and achieved ₹2,190 crore in import substitution, the **March 2026 figures are nearly identical to December 2025** (₹2,722 crore sales vs ₹2,720 crore; ₹2,190 crore vs ₹2,192 crore import substitution), suggesting **no meaningful quarterly growth**—only restated data. The claim of "progress" conflates incremental capacity creation with actual substitution impact. [confidence: high]

- *"India's API market is estimated at roughly $15.28 billion in 2026, forecast to reach $22.18 billion by 2031"* — This **global market size** is unrelated to India’s **domestic import dependency** (43.45% from China), which the article later highlights as the policy’s core target. The two metrics measure **different things** (global supply vs. domestic substitution) but are presented as complementary without clarifying the distinction. [confidence: high]

**OUTDATED DATA:**
- *"43.45% Share of India's pharma imports still coming from China"* — This figure is reused from the blog’s earlier 2023 article ("India Cannot Sell ‘China-Free’ Medicine...") but **no newer official data** (e.g., latest DGCI&S import statistics or Ministry of Commerce trade reports) is cited to confirm its validity for 2026. [confidence: high]
  - **Series to re-check:** DGCI&S *Pharmaceuticals Import Data* (annual); Ministry of Commerce *Trade Statistics* (monthly/quarterly).

- *"₹4,814 crore actually invested under the Bulk Drugs PLI by Dec 2025"* — The article notes this exceeds the ₹4,322 crore committed figure but **does not verify if this includes private co-investment** or whether it reflects **finalized disbursements** (vs. pledges). No source confirms whether this is a **finalized** or **projected** figure as of March 2026. [confidence: medium]
  - **Series to re-check:** Department of Pharmaceuticals *PLI Scheme Implementation Reports* (quarterly updates).
