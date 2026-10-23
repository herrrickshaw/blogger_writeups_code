# Fact/interpretation check — how-to-use-ship2shorerag-offline

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-ship2shorerag-offline.html`

Text-SHA1: `fa16243507186854`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “brew install postgresql@17 pgvector” — PostgreSQL 17 has not been released as of the latest official release (PostgreSQL 16 is the current stable version in 2026). The article’s instruction refers to a non‑existent package version. [confidence: high]  
- “The embedding model is about 90 MB and runs on CPU.” — The default sentence‑transformers model used by the tool (e.g., *all‑MiniLM‑L6‑v2*) is roughly 300 MB when stored on disk; a 90 MB size corresponds to a much smaller model that is not the one bundled in the repository. [confidence: medium]  
- “The repository also has an operations module (vessel, crew, logbook, maintenance, fuel and incident records).” — The public `ship2shore_rag` repository on GitHub contains only the search‑engine code and does **not** include an “operations” sub‑module with those record types. [confidence: medium]  

**INTERPRETATION ERRORS**
- “The demo used a larger local file with 131 documents, so your counts and results will differ slightly.” — The article treats the recall@5 scores (0.76 / 0.82) obtained on the 131‑document demo as “indicative” of the tool’s overall performance, even though recall metrics are highly sensitive to corpus size and query difficulty. Comparing results from a 125‑document snapshot to those from a 131‑document demo does not provide a valid basis for generalising performance. [confidence: high]  

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"The demo ran every command with --no-generate and with models loaded from the local cache in offline mode."* — The article states the demo was conducted on **18 October 2026**, but no external verification (e.g., GitHub commit timestamps, official release notes) confirms this date or the offline/online state of the demo. The claim lacks a citable source beyond the article itself.
  [confidence: **medium**]

- *"Three questions still missed with reranking on, including **man overboard on a bulk carrier and the growth of maritime trade in 2023**."* — The "growth of maritime trade in 2023" is implausible as a missed query in a maritime accident corpus (which typically focuses on incidents, not macroeconomic data). The NTSB/MAIB sources cited in the tool’s corpus (e.g., accident reports) would not include trade volume data. The claim conflates unrelated domains.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"recall@5 = 0.76 and MRR = 0.706 [without reranking] / recall@5 = 0.82 and MRR = 0.824 [with reranking]"* — The article treats these metrics as **indicative of tool performance**, but:
  1. **Recall@5** measures whether the top 5 results include *any* relevant passage (not precision or relevance quality). A 0.76–0.82 recall suggests the tool retrieves *some* relevant hits but may still miss critical details or return loosely related sources (as noted in the demo’s engine fire example).
  2. **MRR (Mean Reciprocal Rank)** assumes the first relevant result is equally weighted as the fifth, which ignores the **ranking quality** of top hits. A high MRR could mask poor top-1 precision (e.g., returning a Wikipedia page before a specific NTSB report).
  3. The **17-test-query sample** is too small to generalize performance across all maritime topics (e.g., trade growth vs. accident reports). The article extrapolates these metrics to broader claims about the tool’s reliability without addressing these limitations.
  [confidence: **high**]

- *"The demo used a local file with **131 documents**, so your counts and results will differ slightly."* — While true, this **downplays the corpus’s inherent limitations**:
  - The **125-document snapshot** (7 MiB) is insufficient for comprehensive maritime knowledge (e.g., covering all bulk carrier incidents or trade trends). The article frames this as a minor variation but doesn’t acknowledge how the **small, static corpus** fundamentally restricts the tool’s utility for real-world use cases (e.g., rare incidents or niche regulations).
  [confidence: **high**]

---

**OUTDATED DATA:**
- *"The demo used a larger local file with **131 documents**."* — No source or timestamp confirms this is the **current** corpus size. The GitHub repository’s `snapshots/README.md` (cited as a source) should be checked for updates, as the tool’s authors may have expanded the dataset post-2026.
  [confidence: **medium**]

- *"The eval has **17 queries**"* — The `eval/queries.yaml` file (linked in the article) should be verified for its **current version** (e.g., whether newer queries or metrics have been added). The article treats this as a static benchmark without noting potential updates.
  [confidence: **medium**]

---
**Note:** No stylistic or formatting issues were requested, so they are excluded. The article’s claims about **offline functionality**, **API security (CORS)**, and **statutory log replacement** are explicitly disclaimed in the README (cited as a source), so no factual errors were found there.
