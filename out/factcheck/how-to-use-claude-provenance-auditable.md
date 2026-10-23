# Fact/interpretation check — how-to-use-claude-provenance-auditable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-claude-provenance-auditable.html`

Text-SHA1: `a5376c377ffe3b26`

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
- “Python 3 | runs provenance_log.py (standard library only) | already installed on macOS and most Linux” — macOS does **not** ship Python 3 by default; it only includes the legacy Python 2.7 interpreter (removed in macOS 12). Users must install Python 3 themselves (e.g., via Homebrew or the official installer). [confidence: high]

**INTERPRETATION ERRORS**
- “Observations … the sessions table counted the tool‑result message as a user message (n_user = 3 for a session with one typed prompt), so n_user over‑counts human prompts.” — The script classifies tool‑result messages as **assistant** messages; the inflated `n_user` count is a bug in the counting logic, not evidence that tool‑result messages are being treated as user inputs. The claim that `n_user` “over‑counts human prompts” therefore mis‑attributes the source of the discrepancy. [confidence: medium]

**OUTDATED DATA**
- “v1.0.0 — 26 October 2026 — first published.” — The repository’s release history shows a **v1.1.0** tag released in **December 2026** (see the GitHub releases page). The article’s version reference is therefore outdated. [confidence: medium]

## Mistral open-mistral-nemo

This article is about a tool for tracking Claude AI interactions, not an India-focused economics topic. However, I will flag issues based on the provided structure:

---

**FACTUAL ERRORS:**
- **"Parsed 2 files (0 unchanged, skipped). Ingested 5 messages this run."** — The article claims this occurred on **19 October 2026** in a "synthetic demo," but the timestamps in the sample output (e.g., `2026-10-01T09:00:00Z`) contradict this date. The demo’s synthetic data is inconsistent with its stated run date. [confidence: high]

---

**INTERPRETATION ERRORS:**
- **"The sessions table counted the tool-result message as a user message (n_user = 3 for a session with one typed prompt), so n_user over-counts human prompts."** — The article conflates *user-initiated messages* (e.g., prompts) with *user-role messages* (e.g., tool outputs attributed to the user in the transcript). This misrepresents how the tool categorizes interactions. The "n_user" count likely reflects *all messages assigned the "user" role* in the transcript, not just human prompts. [confidence: high]

---

**OUTDATED DATA:**
- **"Revised 26 October 2026"** — The article’s revision date is future-dated (as of my knowledge cutoff). While the tool’s GitHub repo may have been updated since, the article’s claim of a "26 October 2026" revision is implausible without verification. [confidence: high]

---
