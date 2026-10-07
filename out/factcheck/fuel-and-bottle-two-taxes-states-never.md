# Fact/interpretation check — fuel-and-bottle-two-taxes-states-never

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fuel-and-bottle-two-taxes-states-never.html`

Text-SHA1: `8154b98e3dcaa29d`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Alcohol is excluded from GST by the Constitution itself, permanently. Article 366(12A), the clause added by the 101st Amendment that defines 'Goods and Services Tax' for the whole Constitution, defines GST as a tax on the supply of goods or services except 'alcoholic liquor for human consumption.' That's not a policy choice the GST Council can revisit — the tax on liquor was never brought inside the constitutional definition of GST in the first place, and un-defining it back in would require another constitutional amendment, not a Council vote." — Article 366(12A) defines GST as "a tax on supply of goods or services or both except taxes on the supply of the alcoholic liquor for human consumption." However, Article 279A (which established the GST Council) explicitly empowers the GST Council to make recommendations on the date from which goods and services tax be levied on "petrol, high speed diesel, diesel, aviation turbine fuel and natural gas," but it does *not* contain a similar permissive provision enabling the Council to bring alcohol under GST. Crucially, the exclusion of alcohol is absolute under the constitutional framework, but the text conflates the permanence of the exclusion with the definition mechanism; more importantly, the 101st Amendment also specifically kept "petrol, high speed diesel, motor spirit, natural gas, and aviation turbine fuel" outside the immediate levy through Article 279A(5) rather than Article 366(12A) alone. [confidence: medium]

INTERPRETATION ERRORS:
- "Put fuel VAT and liquor excise side by side and they total 34% of national own-tax revenue — a third of the money, from two commodities, sitting entirely outside the GST regime that everything else has been folded into since 2017." — The article uses the PRS "Sales Tax/VAT" category as a proxy for fuel VAT to calculate this 34% share, but as the author's own footnote acknowledges, the source report notes states levy this category chiefly on petroleum products and alcohol combined (net of state excise). Treating this entire "Sales Tax/VAT" bucket as exclusively "fuel VAT" creates an apples-to-oranges or over-attribution error, because residual sales taxes on non-fuel items residing in that category are being counted as fuel. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Fuel VAT and liquor excise together: 34% of the total — a tax base GST never absorbed"* — The claim conflates **fuel VAT** (Sales Tax/VAT on petroleum, which *is* constitutionally eligible for GST but deferred) with **liquor excise** (permanently excluded by Article 366(12A)). While both are outside GST *currently*, the reasoning misrepresents fuel as inherently "never absorbed" when the Constitution explicitly allows it (with a deferral mechanism). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Fuel VAT and liquor excise together account for 34% of what Indian states raise on their own — a bigger share than stamp duty and nearly as much as SGST itself"* — The comparison is misleading because **SGST (44%) is a share of total own-tax revenue**, while **fuel+liquor (34%) is also a share of the same base**. The claim implies fuel+liquor exceed SGST in absolute terms, but the 34% is already a subset of the 44% (SGST + fuel+liquor+others). The correct framing would note that fuel+liquor are *additional* to SGST, not a direct comparison. [confidence: high]

**OUTDATED DATA:**
- *"States' own tax revenue is estimated at 6.8% of GSDP in 2025-26"* — The source is PRS’s *State of State Finances 2025* (Oct 2025), but **2025-26 is a Budget Estimate**, not a finalized figure. For actual collections, re-check the **RBI’s *State Finances: A Study of Budget and Economic Data* (latest fiscal year, e.g., 2024-25 or 2025-26 actuals if released)**. [confidence: high]
