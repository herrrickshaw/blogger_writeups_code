# Fact/interpretation check — indias-military-quantum-plan-has-four

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-military-quantum-plan-has-four.html`

Text-SHA1: `8b1016cc88e60ffc`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "The budget lines for 2024-25 to 2026-27 add up to between about ₹1,460 crore and ₹1,740 crore, depending on which 2025-26 revised figure is right: 24% to 29% of the outlay, with nearly half the mission period gone." — The calculation mixes Revised Estimates (RE) of past years with a forward-looking Budget Estimate (BE) for 2026-27, creating an apples-to-oranges aggregation of distinct budget stages. Furthermore, comparing linear time elapsed ("nearly half the mission period gone") against cumulative budget provisions assumes linear funding, ignoring standard multi-year deep-tech mission profiles where initial hub-establishment phases require lower outlays before capital-intensive scaling occurs in later years. [confidence: high]
- "1 bought Only secure communication has moved from research to procurement: a quantum key distribution contract (2024) and post-quantum cryptography in rollout (2025)" — Post-quantum cryptography (PQC) relies on classical mathematical algorithms executed on standard computing infrastructure to defend against future quantum decryption. Conflating PQC deployment with the operationalization or procurement of quantum hardware/technology under the quantum communications pillar is a category error. [confidence: high]
- "The military framework has no published budget of its own; it leans on the civilian mission." — The absence of a publicly disclosed standalone budget in an unclassified policy overview does not support the conclusion that military quantum programmes financially rely on the civilian NQM. Defence initiatives cited in the text (such as iDEX procurements and DRDO Technology Development Fund grants) draw directly from Ministry of Defence allocations. [confidence: medium]

OUTDATED DATA:
- "Released to institutions, to February 2026 | 699.50 of 2,330.68 sanctioned" — Ministry of Science and Technology / Parliament Question answers on the National Quantum Mission; newer releases to re-check are the Lok Sabha / Rajya Sabha answers of 31 July 2026 (PIB 2291775) and 12 August 2026 (PIB 2298218), which postdate the cited February 2026 figures. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“NQM‑supported startup launched a 25‑qubit machine (April 2025)”** – No publicly documented Indian quantum‑hardware startup had a functional 25‑qubit superconducting processor by April 2025. The only Indian quantum‑computing prototypes reported up to that date were 5‑ to 6‑qubit demonstrators (e.g., DRDO’s Young Scientists Laboratory test in August 2024). Claims of a 25‑qubit machine are therefore inaccurate. [confidence: high]  

**OUTDATED DATA**  
- **“about 12 % had been released to institutions by February 2026”** – The article cites the Lok Sabha answer of 4 February 2026 (₹699.50 cr released) but also notes that Parliament answers of 31 July and 12 August 2026 exist and “may carry newer figures.” Because the article still presents the February 2026 release percentage as current, the data are outdated; the newer answers should be checked for the latest released amount. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"the Army has bought Only secure communication has moved from research to procurement"* — The claim conflates the **2024 procurement contract for QNu Labs’ QKD system** (a specific, limited deployment) with the **2022 trial of the same system** (already referenced earlier in the article). The 2022 trial was not a procurement event but a demonstration under the iDEX program. The phrasing misrepresents the timeline of actual *purchases* vs. trials. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Most of the protection against future quantum code-breaking will come from post-quantum cryptography, which is new mathematics running on existing networks"* — While post-quantum cryptography (PQC) is a critical long-term solution, the claim **overstates its immediate efficacy** against quantum threats. PQC algorithms (e.g., lattice-based cryptography) are still being standardized (NIST’s finalization is ongoing) and lack the same maturity as classical encryption. The article does not address whether the Army’s rollout (June 2025) uses **standardized PQC** or experimental implementations, nor does it quantify how much of its network is transitioned. The leap from "new mathematics" to "most protection" is unsupported. [confidence: high]

**OUTDATED DATA:**
- *"National Quantum Mission outlay for 2023-24 to 2030-31: ₹6,003.65 crore"* — The **2026-27 budget allocation** (₹900 crore) and **revised estimates for 2025-26** (₹477 crore or ₹755 crore) suggest the article’s focus on the **original 2023 approval** (₹6,003.65 crore) is outdated for recent fiscal years. For current spending trends, re-check the **Department of Science and Technology’s annual budget documents** (e.g., Expenditure Budget 2026-27) and **Lok Sabha answers** (PIB 2291775/2298218 from July/August 2026, which the article couldn’t access). [confidence: high]
