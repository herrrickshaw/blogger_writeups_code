# Fact/interpretation check — chemical-import-substitution-quarterly

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/chemical-import-substitution-quarterly.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "DGFT TPA/Dyes anti-dumping duty decisions expected Q2-FY27" — Anti-dumping investigations and recommendations in India are conducted by the Directorate General of Trade Remedies (DGTR), and duties are notified by the Department of Revenue (Ministry of Finance). The Directorate General of Foreign Trade (DGFT) does not investigate or issue anti-dumping duty decisions. [confidence: high]
- "QCO (29071100?)" listed under "DGFT ANTI-DUMPING DUTY TRACKING" — A Quality Control Order (QCO) is a mandatory technical standard issued by line ministries (such as the Department of Chemicals and Petrochemicals) via the Bureau of Indian Standards (BIS); it is not an anti-dumping duty measure administered under trade remedy mechanisms. [confidence: high]
- "L&T Bina LLDPE" — The Bina petrochemical facility and refinery are owned and operated by Bharat Petroleum Corporation Limited (BPCL), not Larsen & Toubro (L&T). L&T is an engineering, procurement, and construction contractor, not the project owner or plant operator. [confidence: high]

INTERPRETATION ERRORS:
- "GST Exemption (18% capex) ~$3bn (capex phase)" — GST paid on capital expenditure is credited back through standard Input Tax Credit (ITC) mechanisms for operational businesses. Categorizing domestic indirect tax accounting credits on facility construction as a $3 billion trade import substitution saving is an apples-to-oranges comparison between internal tax mechanics and national import reduction. [confidence: high]
- "Capex-Driven Savings (Base Case) Tier 1 (Ethylene, PP, HDPE, TPA) $5.0bn" combined with "Anti-Dumping Duty Upside TPA Duty (15-20%) +$220-290mn" — This constitutes double-counting. If new domestic plant capacity replaces imported TPA, the foreign exchange savings are already captured in the capex substitution model; tariff duties on those same displaced imports cannot be added as independent, additive import savings. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Dyes/Azo (32030010)" — The HSN code 32030010 is stated to be for dyes/azo, but according to the correction notice, it is actually for Cutch/Catechu Extracts, indicating an error in the HSN code usage or description [confidence: high]
- "QCO (29071100?)" — The HSN code for QCO is uncertain, indicated by a question mark, suggesting that the code might not be accurate or is unverified [confidence: medium]

INTERPRETATION ERRORS:
- "Final determinations will increase FY30 savings by $430-640mn" — This statement implies a direct causal relationship between the final determinations of the DGFT TPA/Dyes anti-dumping duty decisions and the increase in FY30 savings, without considering potential factors that could affect the actual savings, such as the timing of the decisions, the actual duty rates applied, and the response of domestic producers [confidence: medium]
- "Delay risk: 6-12 months = FY28-29 commissioning vs. target FY28" for BPCL AP Environmental Clearance — This statement assumes a direct and linear relationship between the delay in environmental clearance and the commissioning timeline, without accounting for potential mitigating actions or the complexity of project timelines [confidence: medium]
