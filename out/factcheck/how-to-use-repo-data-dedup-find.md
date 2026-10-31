# Fact/interpretation check — how-to-use-repo-data-dedup-find

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-repo-data-dedup-find.html`

Text-SHA1: `a53f7d148d967e89`

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
- “LFS storage is counted per repository, so a backup copy of a repo stores every large file again.” — GitHub LFS storage is accounted at the **account/organization level**, not per‑repository; the same LFS object (identified by its SHA‑256) is stored only once even if referenced by multiple repos. [confidence: high]  
- “LFS storage is only freed by deleting repositories, not by deleting files.” — LFS objects can be removed from the server (e.g., via `git lfs prune` after rewriting history) and the freed space is reflected without needing to delete the whole repository. [confidence: medium]

**INTERPRETATION ERRORS**
- “Evidence from the run: … flagged 1.12 GB of cross‑repo duplicate waste …” — The tool counts duplicate **pointer** files, but those pointers all reference the same underlying LFS object, which is stored only once on GitHub’s LFS server. Therefore the “duplicate waste” figure does **not** represent actual storage cost; it is an artefact of counting pointers, not a real monetary waste. The conclusion that you can save LFS quota by deleting duplicate repos is unsupported. [confidence: high]  
- “LFS storage is counted per repository, so a backup copy of a repo stores every large file again.” — This causal link (backup repo → extra LFS cost) is false because, as above, duplicate references do not increase LFS storage. The statement misinterprets how LFS deduplication works. [confidence: high]

**OUTDATED DATA**
- none found.

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The audit counts pointers, it does not prove a copy is safe to remove"** — The claim conflates *technical feasibility* (the tool identifies duplicates) with *operational safety* (whether deleting a repo is risk-free). The tool only flags potential duplicates; it does not verify whether a repo is a true backup (e.g., if it contains unique commits or branches beyond the LFS files). Users must manually confirm safety before deletion, as the article later states. [confidence: high]

OUTDATED DATA:
- **"audit_lfs.py run on 19 October 2026 against three synthetic local repositories"** — The article’s revision date is **26 October 2026**, but the demo run is dated **19 October 2026**. While plausible, the discrepancy suggests either:
  1) The demo was run *before* publication (unusual for a "revised" article), or
  2) The revision date is a placeholder (e.g., for future updates). No newer official release is implied, but the timing is inconsistent. [confidence: medium]
