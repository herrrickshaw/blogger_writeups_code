# Fact/interpretation check — how-to-use-india-quality-regulation

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-quality-regulation.html`

Text-SHA1: `c8ebd5f6ac413c0e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“The tally is not a script in the repo; it counts the first word of each page's **Status** field. Hallmarking counts as Mandatory because its status reads ‘Mandatory (gold); voluntary (silver)’.”* — Counting only the first word of the **Status** line assumes that the first token fully determines the regime type. This method mis‑classifies any entry whose status contains multiple descriptors (e.g., “Mixed (mandatory for X, voluntary for Y)”) or where the first word is a qualifier rather than the regime category. Consequently, the reported totals of 13 mandatory, 12 voluntary, 6 mixed and 5 infrastructure bodies are likely inaccurate, as the counting rule does not correctly handle all possible status formats. [confidence: high]  

**OUTDATED DATA:**  
- *“the latest commit is 24 September 2026”* — The article presents this date as the most recent state of the repository, but the repo may have received further commits after 24 Sept 2026 (e.g., a later patch or data update). The series to re‑check is the Git commit history of `github.com/herrrickshaw/india-quality-regulation`; verify whether any commits exist after 24 Sept 2026. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"Scheme launched 2000; gold hallmarking made mandatory from June 2021"** — The BIS Hallmarking scheme was actually launched in **1970** (not 2000), with gold hallmarking made mandatory from **2000** (not 2021). The 2021 date refers to stricter enforcement under the **BIS (Hallmarking) Regulations, 2018**, but the scheme’s origin and initial mandatory gold hallmarking predates 2000. [confidence: high]

INTERPRETATION ERRORS:
- **"The tally is not a script in the repo; it counts the first word of each page's Status field"** — This claim conflates *status classification* (e.g., "Mandatory") with *regime type* (e.g., "mixed"). For example, "Hallmarking" is labeled *Mandatory (gold); voluntary (silver)", but the tally treats it as purely "Mandatory" without accounting for the dual nature. This risks misrepresenting the complexity of mixed regimes (e.g., AGMARK or Tea/Coffee Board) as strictly binary. [confidence: high]

OUTDATED DATA:
- **"The latest commit is 24 September 2026"** — As of October 2024 (current cutoff), this date is **future-dated**. The article’s revision history suggests it was published on **19 October 2026**, which is not verifiable. For actual updates, check the GitHub repo’s latest commit (likely superseded by newer amendments to Quality Control Orders or regulatory schemes). [confidence: high]
