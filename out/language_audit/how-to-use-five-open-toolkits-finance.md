# Language audit — How to use 5 open toolkits: finance models, documents, care audits

*https://blog.vertistratsolution.com/2026/10/how-to-use-five-open-toolkits-finance.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/FILE_EXTENSIONS_CASE]** File types are normally capitalized.
  context: ...n -m dlt.cli status  4 documents found (docx, pptx, xlsx, pdf), 4 converted, 0 faile...
  suggested: DOCX
- **[CASING/FILE_EXTENSIONS_CASE]** File types are normally capitalized.
  context: ...lt.cli status  4 documents found (docx, pptx, xlsx, pdf), 4 converted, 0 failed, cat...
  suggested: PPTX
- **[CASING/FILE_EXTENSIONS_CASE]** File types are normally capitalized.
  context: ... status  4 documents found (docx, pptx, xlsx, pdf), 4 converted, 0 failed, catalog: ...
  suggested: XLSX
- **[CASING/FILE_EXTENSIONS_CASE]** File types are normally capitalized.
  context: ...s  4 documents found (docx, pptx, xlsx, pdf), 4 converted, 0 failed, catalog: 4 doc...
  suggested: PDF
- **[GRAMMAR/A_INSTALL]** The word ‘install’ is not a noun.
  context: ...otero library and cloud account, so the install and workflow steps were taken from the ...
  suggested: installation
