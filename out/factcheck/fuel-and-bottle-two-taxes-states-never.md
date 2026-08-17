# Fact/interpretation check — fuel-and-bottle-two-taxes-states-never

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fuel-and-bottle-two-taxes-states-never.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Petroleum crude, high-speed diesel, motor spirit (petrol), natural gas and aviation turbine fuel are all listed in the same Article 366(12A) framework as goods GST can cover — the 101st Amendment's own proviso says GST 'shall be levied with effect from such date as may be notified by the Government on the recommendation of the GST Council.'" — This provision and the list of five petroleum products are not in Article 366(12A). They are specified under Article 279A(5) of the Constitution (as inserted by the 101st Constitutional Amendment Act, 2016) and reflected in Section 9(2) of the CGST/SGST Acts. Article 366(12A) only defines "goods and services tax" and excludes alcoholic liquor for human consumption. [confidence: high]

INTERPRETATION ERRORS:
- "Kerala's case is distinctive: at 40.6%, its dependence runs almost entirely through the fuel VAT line (2.4% of GSDP, the highest fuel-VAT share of any state in this table) rather than liquor excise (0.2%, one of the lowest)... Tamil Nadu shows the same fuel-heavy, excise-light pattern as Kerala (2.0% fuel VAT vs. 0.4% excise)..." — The article assumes the entire "Sales Tax/VAT" line represents fuel tax alone. In reality, both Kerala (through Kerala State Beverages Corporation / BEVCO) and Tamil Nadu (through TASMAC) levy massive value-added tax/sales tax rates on potable alcohol rather than collecting the bulk of liquor revenue through standard state excise duty. Concluding that Kerala and Tamil Nadu are uniquely dependent on fuel rather than liquor mischaracterizes the data due to a failure to account for state-level tax classification differences. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "States' own tax revenue is estimated at 6.8% of GSDP in 2025-26" — This claim cannot be verified against publicly available data as of my knowledge cutoff, and the source provided is a specific report that may not be accessible or up-to-date [confidence: medium]
- "Article 366(12A), the clause added by the 101st Amendment that defines 'Goods and Services Tax' for the whole Constitution, defines GST as a tax on the supply of goods or services except 'alcoholic liquor for human consumption.'" — While this statement about the constitutional amendment is likely correct, without direct access to the Constitution of India or the specific amendment, it's difficult to verify the exact wording [confidence: low]

INTERPRETATION ERRORS:
- "Put fuel VAT and liquor excise side by side and they total 34% of national own-tax revenue — a third of the money, from two commodities, sitting entirely outside the GST regime that everything else has been folded into since 2017." — This statement might imply that the exclusion of fuel and liquor from GST is unusual or problematic because it constitutes a large portion of state tax revenue. However, the reasoning gap lies in not fully exploring why these commodities are treated differently (e.g., constitutional reasons for liquor, policy decisions for fuel) and the implications of including them in GST [confidence: medium]
- "A hypothetical future GST Council decision to bring petrol and diesel inside GST would restructure roughly a fifth of national state own-tax revenue overnight — the entire Sales Tax/VAT line in Section 1's chart." — This statement assumes that bringing petrol and diesel under GST would automatically lead to a significant restructuring of state own-tax revenue without considering potential compensatory measures or the complex dynamics of tax revenue redistribution [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Fuel VAT" is the report's Sales Tax/VAT category, which the report notes states levy chiefly on petroleum products and alcohol combined — here shown net of the separately-reported Excise Duty line, so it should be read as predominantly, not exclusively, fuel. [confidence: high]
  *What's wrong*: The article incorrectly states that the "Sales Tax/VAT" category is "chiefly on petroleum products and alcohol combined," implying it includes both fuel and liquor. However, the source report (PRS Legislative Research) clarifies that the "Sales Tax/VAT" category is net of the separately reported Excise Duty line, meaning it primarily represents fuel VAT, not a combined category. The article misrepresents the composition of this tax bucket.

INTERPRETATION ERRORS:
- "a hypothetical future GST Council decision to bring petrol and diesel inside GST would restructure roughly a fifth of national state own-tax revenue overnight — the entire Sales Tax/VAT line in Section 1's chart." [confidence: high]
  *The reasoning gap*: The claim assumes that bringing fuel under GST would eliminate the entire "Sales Tax/VAT" line (20% of state own-tax revenue) overnight. However, this ignores that states may retain some taxing power over fuel (e.g., via cess or additional levies) even after GST implementation, as seen in other GST-covered goods. The restructuring would likely be partial, not a complete elimination of the revenue source. The article conflates the formal inclusion of fuel under GST with the loss of all associated revenue streams.

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
