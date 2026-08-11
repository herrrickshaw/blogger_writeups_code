# Fact/interpretation check — ethanol-blending-omc-books-e20-today-vs

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ethanol-blending-omc-books-e20-today-vs.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Source: PPAC Oil & Gas Ready Reckoner FY2025-26" — Citing the PPAC Ready Reckoner for FY2025-26 (as well as "CareEdge, ESY 2025-26") to cite current installed capacity and historical FY24-25 figures (Tables 4.11 and 8.17) is an error, as FY2025-26 / ESY 2025-26 is a future period and these official report editions do not exist. [confidence: high]

INTERPRETATION ERRORS:
- "Petrol freed from the domestic tank, sold abroad at ~$86/bbl — more than covering the exchequer's loss." — This is an apples-to-oranges comparison that conflates gross corporate export revenues with government tax receipts. The gross export forex ($8.8 bn / ₹74,751 cr) is collected by oil marketers/refiners, not the government treasury, so it cannot "cover" or compensate for the exchequer's foregone excise and VAT revenue. Additionally, gross export earnings ignore the cost of importing the crude oil required to refine that petrol, overstating the net trade benefit. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Petrol demand · MMT/yr FY26→FY31" and related numbers — the article does not provide a clear source for the specific petrol demand forecast, and the numbers seem to be based on a 7% trend and EV share, but without a direct reference to verify these numbers against official data or forecasts [confidence: medium]
- "Installed capacity is now ~2,000 cr L (CareEdge, ESY 2025-26)" — without access to the specific CareEdge report or data for ESY 2025-26, it's difficult to verify the exact installed ethanol capacity [confidence: medium]

INTERPRETATION ERRORS:
- "The read: ethanol adds ~₹7,200 cr to OMC/refiner contribution today and ~₹11,100 cr at E30 — a +53% lift — with the freed-petrol export margin the single biggest piece." — this conclusion assumes that the increase in OMC/refiner contribution is directly and solely due to ethanol blending, without considering other potential factors that could influence this increase [confidence: medium]
- "The tax the exchequer no longer collects grows from ~₹39,400 cr to ~₹56,000 cr as blending goes E20→E30. The proposed 5% ethanol SGST returns ₹5,513 cr to states — a partial, price-neutral recovery (full VAT-parity would need ~27%)." — the comparison between the tax not collected and the SGST return implies a direct trade-off, but it does not account for the potential economic effects of ethanol blending on other tax revenues or the overall economy [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Domestic petrol 54.05 bn L (40 MMT, PPAC FY24-25)" — The conversion from billion litres to MMT (million metric tonnes) is incorrect. 1 litre of petrol weighs approximately 0.74 kg, so 54.05 billion litres ≈ 40.0 MMT (54.05 * 0.74 = 39.997 ≈ 40.0). However, the article states "54.05 bn L (40 MMT)" without clarifying the conversion factor, which could mislead readers unfamiliar with the calculation. [confidence: high]

- "ethanol capacity ~2,000 cr L" — The article later states "Installed capacity is now ~2,000 cr L (CareEdge, ESY 2025-26), with a further ~400 cr L due by FY27." However, "cr L" (crore litres) is ambiguous—it could mean 20 billion litres (2,000 crore litres = 20 billion litres) or 200 billion litres (2,000 crore litres = 200 billion litres). The context suggests it is 20 billion litres (2,000 crore litres = 20 billion litres), but the notation is unclear and could lead to misinterpretation. [confidence: medium]

INTERPRETATION ERRORS:
- "A dedicated state SGST on ethanol recovers a slice for states. ... The proposed 5% ethanol SGST returns ₹5,513 cr to states — a partial, price-neutral recovery (full VAT-parity would need ~27%)." — The claim implies that the 5% SGST is a meaningful recovery of foregone VAT, but the calculation of "full VAT-parity" (~27%) is not clearly justified. The foregone VAT is ~₹18/litre, while the 5% SGST on ethanol would be ~₹0.75/litre (assuming ethanol price ~₹15/litre), which is far below the foregone VAT. The article does not explain how the 27% figure is derived or whether it accounts for the ethanol price, blending ratios, or other factors. This makes the comparison misleading. [confidence: high]

- "The petrol ethanol pushes out of the domestic tank doesn't vanish — India, a net product exporter, ships it." — While India is a net exporter of petroleum products, the claim that *all* displaced petrol is exported is an overgeneralization. The article later quantifies this as "~8 MMT at E20" and "~12 MMT at E30," but it does not address whether there is sufficient export demand, infrastructure, or market conditions to absorb this additional volume. The conclusion that the displaced petrol is "shipped abroad" assumes perfect market conditions, which may not hold. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
