# Language audit — How to use claude-provenance: an auditable log of every Claude message on your machine

*https://blog.vertistratsolution.com/2026/10/how-to-use-claude-provenance-auditable.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/ID_CASING]** This abbreviation for “identification” is spelled all-uppercase.
  context: ...integrity and lineage (SHA-256, message id and parent id).  Re-runs are incrementa...
  suggested: ID
- **[CASING/ID_CASING]** This abbreviation for “identification” is spelled all-uppercase.
  context: ...lineage (SHA-256, message id and parent id).  Re-runs are incremental: unchanged s...
  suggested: ID
- **[GRAMMAR/ONE_PLURAL]** Please verify that the plural noun “sessions” is in agreement with the quantifier “1”. Did you mean to use the singular form?
  context: ...n. Database now holds 5 messages across 1 sessions -> .../provenance.db Summary written ->...
  suggested: 1 session, a session, sessions
