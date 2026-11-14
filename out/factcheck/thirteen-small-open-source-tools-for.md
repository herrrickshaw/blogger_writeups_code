# Fact/interpretation check — thirteen-small-open-source-tools-for

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thirteen-small-open-source-tools-for.html`

Text-SHA1: `b6e3ed4fb8d46245`

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
- “In the guide’s run of 19 October 2026 on a throwaway Postgres 17, all three test files passed.” — PostgreSQL 17 has not been released; the latest stable major version as of the knowledge cutoff is PostgreSQL 16 (released 2023). Claiming a Postgres 17 instance is a factual inaccuracy. [confidence: high]

**INTERPRETATION ERRORS:**
- none found

**OUTDATED DATA:**
- “The committed database was pulled on 21 July 2026 and has 4,532 World Bank rows.” — World Bank indicator data are updated regularly (typically annually or quarterly). A dataset frozen in July 2026 is likely superseded by newer releases (e.g., 2024‑2025 updates). The series to re‑check is the World Bank Open Data API for the listed indicators; a newer snapshot should be used. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"13 small tools, most of them one script or one short package"** — The article lists **13 repositories**, but the claim that "most of them are one script or one short package" is misleading. While many are lightweight, several (e.g., `ship2shore_rag`, `memory-map-optimizer`, `data-source-mining`) include multiple files, dependencies (e.g., `sentence-transformers`, `Postgres/SQLite`), and non-trivial setup (e.g., Docker-like environments for `ship2shore_rag`). The article itself notes that some require **~1 GB disk** or **model downloads (1.5 GB)**. [confidence: high]

INTERPRETATION ERRORS:
- **"0.76 → 0.82 recall@5 without and with reranking on 17 test questions"** — The claim implies a **statistically meaningful improvement** from reranking, but the article later states the test set is **"indicative, not a benchmark"** and only **17 questions** were used. Reranking’s impact cannot be generalized beyond this small, synthetic dataset. [confidence: high]
- **"1.83 GB vs 0.71 GB LFS storage counted against unique content in a synthetic three-repo audit"** — The comparison conflates **storage size (1.83 GB)** with **unique content (0.71 GB)**, which may include metadata or redundant pointers. The tool only **counts pointers**, not actual duplicate bytes (as noted in the limitations), so the "waste" figure overstates savings. [confidence: high]

OUTDATED DATA:
- **"Committed database was pulled on 21 July 2026 and has 4,532 World Bank rows and 4 mandi rows"** — The **World Bank API** and **Agmarknet** data are dynamic; the article does not verify if the figure is current as of the article’s **12 November 2026** publication. Re-check the `data-source-mining` repo’s latest commit or run `mine_underused_sources.py --wb-only` to confirm. [confidence: high]
- **"The guide rendered all four [research-design-system] themes on 19 October 2026"** — While the date is noted, the article does not confirm whether the **CSS kit** or **templates** have been updated since. The "live copy is not auto-synced with the repo," so the rendered output may differ from the latest version. [confidence: medium]
