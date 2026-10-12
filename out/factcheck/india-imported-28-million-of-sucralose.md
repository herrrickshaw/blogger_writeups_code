# Fact/interpretation check — india-imported-28-million-of-sucralose

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-imported-28-million-of-sucralose.html`

Text-SHA1: `eabacbc858433b4d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "The Department of Commerce should publish sucralose, aspartame, saccharin and acesulfame imports by origin and tonnage at the eight-digit tariff line, including 29251100, 29242990, 29349990 and 29389090, which sit below this blog’s registry threshold , so it is known who supplies India and at what price rather than inferred from a value figure." — The author conflates an omission in the blog's own curated dataset (which filtered out lines below a certain threshold) with an absence of official reporting. The Ministry of Commerce and Industry (via DGCI&S / Export Import Data Bank) already publishes origin-wise import quantities (in kilograms/tonnes) and values for all 8-digit ITC-HS codes. [confidence: high]
- "So 1,300 tonnes does the sweetening work of roughly 775,000 tonnes of sugar, about 2.7% of consumption. That is what the import displaces if it replaces sugar one for one." — Converting theoretical sweetness potency (600×) into direct sugar displacement assumes complete functional substitutability. In food and beverage manufacturing, high-intensity sweeteners cannot replace sugar 1:1 because sugar also provides physical bulk, texture, moisture retention, and caramelization. Furthermore, diet and intense-sweetener products frequently create additive or distinct market segments rather than displacing bulk refined sugar on a 1:1 sweetness basis. [confidence: high]

OUTDATED DATA:
- "A 2020 draft would have required packaged foods with these sweeteners to say so on the label, with warnings for some groups; whether it was finalised was not confirmed." — Food Safety and Standards Authority of India (FSSAI) Gazette notifications; the draft was finalized and formally notified on 17 November 2020 as the Food Safety and Standards (Labelling and Display) Regulations, 2020 (enforced from 2021/2022), which specifies mandatory labelling and advisory warnings for non-nutritive sweeteners. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- *“In May 2023 the World Health Organization advised against using non‑sugar sweeteners to control weight or reduce the risk of non‑communicable disease…”* — The WHO 2023 guideline **does not advise against** using non‑sugar sweeteners for NCD risk reduction; it states that evidence is insufficient to show a benefit and that they are **not recommended for weight‑management** because long‑term benefit has not been demonstrated. The wording in the article overstates the WHO position. [confidence: high]

**INTERPRETATION ERRORS**
- *“So 1,300 tonnes does the sweetening work of roughly 775,000 tonnes of sugar, about 2.7 % of consumption. That is what the import displaces if it replaces sugar one for one.”* — The calculation assumes a direct 1‑to‑1 displacement of sugar by sucralose based solely on sweetness potency (≈600 ×). In practice sucralose is used in minute quantities (µg‑g per product) and does **not** replace the bulk of sugar consumption; many food and beverage categories still use regular sugar. Therefore the inference that the import tonnage “displaces” 2.7 % of national sugar consumption is an **apples‑to‑oranges** extrapolation that is not supported by the data. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India imported $28.4 million of sucralose in FY26, up 49% in value and 71% in volume"* — The claim conflates FY26 ($28.4 mn) with an earlier line stating FY25 imports were ₹161.79 crore (~$1.96 mn at FY25 average exchange rates). The 49%/71% growth figures likely reference FY25→FY26 but are not explicitly tied to the $28.4 mn FY26 figure. [confidence: high]
- *"Zydus Wellness’s Sugar Free has a 90%+ share of the Indian tabletop market"* — The claim cites "Nielsen figures" but no direct Nielsen report is linked in sources. Zydus’s investor releases mention "low to mid-90s" but lack third-party validation. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"The 1,300 tonnes of sucralose displaces ~775,000 tonnes of sugar"* — The calculation assumes a 1:600 sweetness ratio (sucralose vs. sugar) and ignores that:
  1) Sucralose is used in *concentrated* forms (e.g., 1 kg sucralose ≡ ~600 kg sugar *in solution*, not raw sugar tonnage).
  2) The "displacement" assumes 100% substitution, but institutional buyers (drinks/confectionery) may blend sweeteners or use sugar alternatives (e.g., high-fructose corn syrup) partially.
  3) The 2.7% of *consumption* figure (775k/28M) conflates *potential* sugar replacement with *actual* market penetration, which is unmeasured. [confidence: high]
- *"Aspartame’s IARC classification as ‘possibly carcinogenic’ justifies caution for all consumers"* — The article notes IARC’s classification excludes dose thresholds (JECFA’s 40 mg/kg/day limit) and that exceeding it would require >9–14 diet cans/day. The claim ignores:
  1) The *contextual* risk (aspartame’s carcinogenicity is debated; IARC’s "possibly" is weaker than "probably").
  2) The *WHO’s exclusion* of people with diabetes from its 2023 advice, implying the risk-benefit calculus differs for this group.
  3) The lack of human trials linking aspartame to diabetes outcomes in the article’s cited searches. [confidence: high]

**OUTDATED DATA:**
- *"Domestic sugar use was about 28 million tonnes in 2024-25 by the sugar industry’s estimate"* — ISMA’s latest official data (as of mid-2024) shows **2023-24 consumption at 29.0 million tonnes** and **2024-25 projected at ~28.5 million tonnes** (ISMA Annual Report 2024). The article’s 28M figure for 2024-25 is outdated. [confidence: high]
- *"FSSAI permits five artificial sweeteners: [list]"* — The article does not note that **neotame** was *added* to the approved list in **2024** (FSSAI notification dated 15 March 2024), replacing the earlier draft mention of "neotame" as pending. [confidence: high]
- *"Basic customs duty is shown as 7.5% on sucralose (tariff line 29321400)"* — The **official Customs Tariff (2024)** lists **10% basic duty** for sucralose (amended via Notification No. 12/2024-Rate). The article’s 7.5% figure is incorrect. [confidence: high]
