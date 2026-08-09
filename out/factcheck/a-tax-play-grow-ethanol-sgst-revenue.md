# Fact/interpretation check — a-tax-play-grow-ethanol-sgst-revenue

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-tax-play-grow-ethanol-sgst-revenue.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Delhi taxes it at 0%, Himachal Pradesh at 13.75%, and the national average price at the pump ranges from ₹76.08/kg (Delhi) to a national high of ₹122.00/kg (Himachal Pradesh, maximum observed)." — The text misstates ₹122.00/kg as the upper bound of the national average price range. As shown in the article's own tables, ₹122.00/kg is the single maximum observed outlet price in Himachal Pradesh, whereas the highest state average CNG price is Uttarakhand at ₹103.15/kg (and Himachal Pradesh's average is ₹101.70/kg). [confidence: high]

INTERPRETATION ERRORS:
- "For Telangana specifically, the package is close to self-funding within the same state's own ledger: money recovered on the ethanol side offsets money given up on the CNG side." — The article provides no data on Telangana's total annual CNG VAT collection or the exact revenue loss the state would incur by reducing its CNG VAT from 14.5% to 5%. Furthermore, the text explicitly acknowledges elsewhere that it did not attempt to cost state-level CNG revenue neutrality due to a lack of state treasury data. Asserting that the package is "close to self-funding" for Telangana is an extrapolation beyond what the presented data supports. [confidence: high]
- "PPAC's state-wise CNG sales data (Ready Reckoner FY2025-26, Table 3.7) lets us check whether the high-VAT states are also the ones where CNG hasn't caught on, or whether demand is inelastic to price:" — The article compares absolute state-level CNG sales volumes in thousand metric tonnes (e.g., Delhi's 610 TMT vs. Himachal Pradesh's 1 TMT) to assess whether tax rates drive adoption. This is an apples-to-oranges comparison because total sales volume is primarily dictated by state population, vehicle fleet size, urban density, and commercial fleet concentration rather than tax policy alone. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The mechanism is simple. Petrol sits outside GST — states tax it directly under their own VAT laws, at rates from 13% to over 35% depending on the state." — The article does not provide a source to verify the range of VAT rates for petrol (13% to over 35%) [confidence: medium]
- "Punjab's CNG-specific VAT (14.3%) against its headline DPNG rate (3.3%) is unexplained in the source PNGRB table." — This claim may be incorrect if the PNGRB table or other sources provide an explanation for the difference, but based on the information provided, it appears to be unexplained [confidence: medium]
- "At the national E20 blend, that companion piece modelled the gap at roughly ₹19,485 crore in VAT foregone against ₹1,622 crore in SGST gained — a net state shortfall of about ₹17,863 crore a year" — The article does not provide a source to verify the exact figures of the gap (₹19,485 crore, ₹1,622 crore, ₹17,863 crore) [confidence: medium]

INTERPRETATION ERRORS:
- "The honest reading: VAT is a real, visible driver of the northern-hill-state CNG price problem, but it isn't the only one — transport distance from source and terrain economics in HP and Uttarakhand are doing some of the work too." — This statement may be an interpretation error because it implies that VAT is a primary driver of the price problem, when in fact, the article later notes that transport distance and terrain economics also play a significant role [confidence: medium]
- "If Himachal Pradesh's CNG VAT were harmonized down to the 5% rate charged in the low-VAT cluster... the state's average CNG price would fall from ₹101.70/kg to roughly ₹93.88/kg" — This claim assumes that the only factor affecting the price is the VAT rate, and does not account for other factors such as transport costs, which may affect the actual price reduction [confidence: medium]
- "Option B, the near-term version, does not achieve full parity. Redirecting the entire OMC blending margin still leaves roughly 60% of the state shortfall unclosed at both E20 and E30" — This statement may be an interpretation error because it implies that achieving full parity is the only goal, when in fact, the article presents Option B as a partial fix that can still provide significant benefits [confidence: medium]
