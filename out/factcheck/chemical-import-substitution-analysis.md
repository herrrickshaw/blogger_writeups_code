# Fact/interpretation check — chemical-import-substitution-analysis

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/chemical-import-substitution-analysis.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Four Major Government Capex Projects (Load-Bearing) ... RIL Oil-to-Chemicals (O2C)" — Reliance Industries Limited (RIL) is a private, investor-owned corporation, not a government entity. Classifying RIL's O2C investment under "Government Capex Projects" / "Government Capex Required" is factually incorrect. [confidence: high]
- "Total Investment (FY26–FY30): ₹1,38,514 crore (~$16.6 billion)" — The sum of the capex figures listed for the four projects in the table (BPCL AP: ₹1,00,000 crore; RIL O2C: ₹75,000 crore; L&T Bina: ₹600–1,200 crore; BHAVYA Parks: ₹3,030 crore) totals ₹1,78,630–1,79,230 crore, which contradicts the stated total of ₹1,38,514 crore. [confidence: high]
- "Lecithin (HSN 29239090) [retracted — see correction notice above] real: 39021000" — The inline text cites HSN 39021000 as the corrected code for lecithin. HSN 39021000 corresponds to Polypropylene (plastics), whereas Lecithin is an organic compound/phospholipid (HS 29232090). [confidence: high]

INTERPRETATION ERRORS:
- "Payback Period: 4–6 years post-FY30 ... ROI (Conservative): 45–55% over 10 years" — The analysis estimates payback period and ROI by directly comparing capital expenditure against gross annual forex savings (macroeconomic trade value). Gross import substitution value is top-line market revenue, not net project profit or cash flow to the operating companies, which depends on feedstock costs, operating expenses, and margins. Conflating gross macro trade savings with project cash flows is an apples-to-oranges calculation gap. [confidence: high]
- "Chapter 38 | Textile Auxiliaries | $620mn" — HS Chapter 38 covers "Miscellaneous Chemical Products" in full (a broad chapter covering diagnostic reagents, catalysts, chemical preparations, etc.). Equating the entire chapter to "Textile Auxiliaries" and treating a single product category's import value ($620mn) as the full chapter import total misrepresents a narrow sub-segment as an entire tariff chapter. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "ethylene was cited as 29011100 / $2,800M (the real line is 29012100, $44M )" — The article incorrectly states the HS code and import value for ethylene, which is actually 29012100 with a value of $44M, not $2,800M. [confidence: high]
- "propylene as 29011200 / $1,400M (real: 29012200, $14M )" — The article incorrectly states the HS code and import value for propylene, which is actually 29012200 with a value of $14M, not $1,400M. [confidence: high]
- "polyethylene as 39021010/30 / $8.5bn (real 3901 lines total ~$2.8bn ; 3902 is polypropylene)" — The article incorrectly states the import value for polyethylene, which is actually ~$2.8bn, not $8.5bn. [confidence: high]
- "lecithin as 29239090 / $100M (real: 29232090, ~$19M )" — The article incorrectly states the HS code and import value for lecithin, which is actually 29232090 with a value of ~$19M, not $100M. [confidence: high]
- "Chapter 38 is labelled “Textile Auxiliaries, $620mn” below. Authentic DGCI&S imports for Chapter 38 in FY2025-26 are $8,857M" — The article incorrectly states the import value for Chapter 38, which is actually $8,857M, not $620mn. [confidence: high]

INTERPRETATION ERRORS:
- "The $8.3–11.5bn FY30 savings headline is therefore retracted pending a from-scratch substitution-target exercise against corrected import bases." — The article uses incorrect import values to support a conclusion about potential savings, which may not be accurate once the correct import bases are used. [confidence: high]
- "Tier 1: LOAD-BEARING (Capex-Triggered) FY30 Savings: $6.1 billion/year" — The article uses incorrect import values and HS codes for certain chemicals (e.g. ethylene, propylene) to support a conclusion about potential savings, which may not be accurate once the correct values and codes are used. [confidence: high]
