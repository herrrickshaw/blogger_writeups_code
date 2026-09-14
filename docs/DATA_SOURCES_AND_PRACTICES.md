# Data sources and standard practices

A cross-repo status snapshot: what data sources feed the masaladeutsch ecosystem, how
they're collected and turned into posts, what's still reachable, and where the known
gaps are. Built 2026-09-14 by walking `blogger_writeups_code`, `india-govt-yellow-pages`,
`india-trade-sector-policy-recommendations`, and `digital-twin-for-ipa`, plus live
reachability tests from a sandboxed session (see caveat under Reachability).

This is a snapshot, not a live dashboard — re-run the checks below before trusting any
status in it more than a few weeks old.

## 1. The pipeline, end to end

```
external source --> scraper script --> local cache (sqlite/JSON) --> classifier
    --> generated doc/dashboard (digital-twin-for-ipa, india-govt-yellow-pages)
    --> hand-drafted or hand-updated post (out/ in blogger_writeups_code)
    --> tools/blogger_api.py update/insert (manual, reviewed)
    --> tools/snapshot.py writes posts/ + meta/ (or a documented manual workaround)
```

Four repos, four different roles:

| Repo | Role |
|---|---|
| `blogger_writeups_code` | The blog itself — source of truth for what's actually published, and the only repo with a publish step |
| `india-govt-yellow-pages` | Contact directory (igod.gov.in org index, ministry who's-who) + a self-contained dashboard |
| `india-trade-sector-policy-recommendations` | PIB press-release index (`pib_index.sqlite`) + ~20 trade/policy bulletins, published as a GitHub Pages site |
| `digital-twin-for-ipa` | Output docs only (`reportage_latest.html`, `pq_registry.html`, `rs_pq_registry.html`, state-wire feed, global filing sweep) — no scraper scripts live here; whatever built these wasn't found in any repo this session could reach |

## 2. Data sources by category

### 2a. Central government — systematically scraped

| Source | What's pulled | Script | Cadence | Status |
|---|---|---|---|---|
| PIB (pib.gov.in) | Every press release, all ministries, since 2017 | `india-trade-sector-policy-recommendations/scripts/pib_index.py` | Cron on a machine with access; `--update` catches up from `last_indexed_date` | **Live** — 124,730 rows through 2026-09-14 |
| igod.gov.in (NIC's govt-site directory) | Org index (9,461 rows), contacts, who's-who | `india-govt-yellow-pages/scripts/igod_crawl.py`, `igod_org_details.py` | Monthly (`scripts/refresh.sh`, cron `30 10 1 * *`) | Not re-verified this pass |
| Ministry sites (17 ministries deep-scraped) | Full officer rosters, room/phone/email | `india-govt-yellow-pages/scripts/ministry_whoswho.py` | Same monthly cron | ~78 ministry sites are Akamai JS-shell templates and don't yield to this method (documented gap, not a bug) |
| Lok Sabha Q&A (sansad.in) | Questions + answer PDFs, scheme-tagged | Undocumented API `sansad.in/api_ls/question/qetFilteredQuestionsAns` | Ad hoc | **Broken** — 404s now; the JS-chunk-mining method that works for RS hasn't relocated it yet (see §4) |
| Rajya Sabha Q&A | Same, via a different backend | `rsdoc.nic.in/Question/Search_Questions?whereclause=...` (raw SQL-style, params: `ses_no`, `qtype`, `qno`, `min_code`, `mp_code`, `adate`, `qtitle`) | Ad hoc | **Confirmed working** 2026-09-14 — found by mining `/rs/_next/static/chunks` for the real backend host |

### 2b. State government — systematic (the "state wire")

`digital-twin-for-ipa/docs/STATE_SOURCES.md` tracks this in detail; summary:

- **18 states/UTs integrated** — a mix of server-rendered HTML tables, Drupal views,
  ASP.NET Core pages, one RSS feed (Telangana), and one open JSON API (Andhra Pradesh,
  via `ap.gov.in`'s unminified Angular bundle — reverse-engineered, not documented).
- **5 probed but not integrated** — Chhattisgarh (WAF serves empty 200s to
  curl/urllib), Odisha (archive stale since Sep 2023), West Bengal (stale, narrow),
  Uttarakhand (feeds disabled), and a closed non-finding on Andhra Pradesh's separate
  IPR site (its own site requires a per-request signed RSA+AES-GCM+HMAC exchange —
  correctly declined as a deliberate anti-automation gate, not attempted).
- **15 states/UTs unreachable** — Arunachal Pradesh, Bihar, Haryana, Himachal Pradesh,
  Jharkhand, Manipur, Meghalaya, Tamil Nadu, Tripura, Delhi, J&K, Ladakh, Puducherry,
  Andaman & Nicobar, Lakshadweep. Each has a documented "next lead" already.

A quick spot-check this pass on two of these: Bihar's documented lead
(`state.bihar.gov.in/prdbihar`) is confirmed still the right URL but still 302-loops —
no change. Tamil Nadu surfaced one lead not yet in the doc: `tn.gov.in/department/31`
looks like a real DIPR department page, worth a follow-up scrape attempt (not verified
working, just not-yet-tried).

### 2c. Land / investment infrastructure (state industrial-land banks)

From `india-trade-sector-policy-recommendations/data/data_completeness_audit_2026-07-22.json`:

- **Machine-readable now (6)**: Odisha IDCO (open ArcGIS REST, per-plot geometry),
  UP's UPSIDA (HTML table with price), Andhra's APIIC, Telangana's TGIIC, Rajasthan's
  RIICO (explicitly the undeveloped bank), Haryana's HSIIDC.
  Odisha is the only one with per-parcel lat/lng — the rest lack coordinates entirely,
  which blocks any proximity-to-port/highway analysis.
- **Needs headless browser**: Maharashtra's MIDC (AJAX controller returns 411 to a
  plain GET).
- **Login or PDF-only**: Gujarat's GIDC, Karnataka's KIADB, West Bengal's silpasathi,
  Madhya Pradesh's MPIDC (down).
- **Hijacked/parked domains — do not trust**: `sipcot.com`/`sipcot.in` (real site is
  `sipcotweb.tn.gov.in`), `wbidc.com` (real site is `silpasathi.wb.gov.in` /
  `wbiidc.wb.gov.in`).
- The other 27 industrial states' undeveloped land banks are simply unquantified —
  flagged as the single biggest swing factor in that repo's land-supply analysis.

### 2d. International — foreign-exchange filing feeds

`digital-twin-for-ipa/docs/GLOBAL_SWEEP_TARGETS.md` (built 2026-08-21) mines
disclosure/filing systems for "India interest" signals in foreign-listed companies:
Korea's DART (heavily used — most of the 110 Tier-1 hits), Norway's Oslo Børs
NewsWeb, Switzerland's SIX Equity Issuer News. The doc's own header flags this as a
**snapshot, not final** — Japan's EDINET and the EU's ESEF filing systems are "only
lightly tested so far." If a fresh sweep is wanted, that's the natural next tier to
extend rather than re-running the already-thorough DART pull.

### 2e. LLM validation / fact-checking backends

Not a data *source* in the same sense, but part of the same pipeline:
`tools/content_validate.py` and `tools/multi_model_factcheck.py` in
`blogger_writeups_code` call out to whatever OpenAI-compatible endpoint is configured
(OmniRoute locally, or Gemini's own endpoint directly) to sanity-check a post's
internal consistency and claims. These are gated to run only against already-drafted
posts, never to originate content unsupervised.

### 2f. Ad hoc citation sources (not systematic)

Roughly 150+ distinct news outlets, company press releases, and industry publications
turn up as one-off citations across the scripts and docs (grep for URLs in
`tools/*.py` and `docs/*.md` if you need the full list — it's long and not worth
tabulating here). These are gathered per-article during research, not collected on a
schedule, and don't belong in the same reachability/freshness tracking as §2a-2d.

### 2g. Diplomatic sources — embassies, high commissions, bilateral MoUs (new, 2026-09-14)

Not previously tracked anywhere in this ecosystem. Government-to-government MoUs and
diplomatic events are announced through two channels that rarely overlap fully: the
Indian side (MEA, sometimes PIB) and the foreign mission's own site. Neither alone is
complete — a bilateral MoU signing is often covered by both, with different framing
and sometimes different dates (signing date vs. announcement date).

**Indian side (central, one source covers all countries):**

| Source | What it has | URL |
|---|---|---|
| MEA press releases | All MEA press releases, not just bilateral | mea.gov.in/press-releases |
| MEA Bilateral/Multilateral Documents | The actual MoU/agreement text repository — the closest thing to a structured MoU registry | mea.gov.in/bilateral-documents |
| MEA Bilateral Briefs | Country-by-country relationship summaries (context, not a feed) | mea.gov.in/bilateral-briefs |

No public API found for any of the three — same pattern as PIB before `pib_index.py`
existed: HTML pages meant for browsing, would need the same kind of scraper built.

**Foreign missions in India — press/news sections found for 12 major partners**
(all unverified against this sandbox's egress, same caveat as everything in §4):

| Country | Mission | News/press URL |
|---|---|---|
| United States | Embassy, New Delhi | in.usembassy.gov/news/ |
| United Kingdom | High Commission | gov.uk/world/organisations/british-high-commission-new-delhi |
| Japan | Embassy | in.emb-japan.go.jp/itpr_en/index.html |
| Australia | High Commission | india.highcommission.gov.au/ndli/news.html |
| European Union | Delegation (covers all 27 member states jointly) | eeas.europa.eu/delegations/india_en |
| Germany | Embassy | india.diplo.de/in-en |
| France | Embassy | in.ambafrance.org |
| Russia | Embassy | india.mid.ru/en/news/ |
| South Korea | Embassy | overseas.mofa.go.kr/in-en/brd/m_22090/list.do |
| UAE | Embassy | mofa.gov.ae/en/missions/new-delhi |
| Singapore | High Commission | new-delhi.mfa.gov.sg |
| Israel | Embassy | embassies.gov.il/india/en/the-embassy |

Each of these is a different CMS/platform (WordPress, Drupal, a shared MFA template
per country, bespoke .gov sites) — there's no single scraping pattern that covers
all 12 the way `pib_index.py` covers every central ministry in one place. Realistic
build order: MEA's bilateral-documents page first (one source, structured,
covers every country), then add individual missions only for the handful of
countries this ecosystem actually tracks closely (the DART/Oslo/SIX filing-feed
countries in §2d are a reasonable starting shortlist: Korea, Norway/EU-adjacent,
Switzerland — plus the US, Japan and UAE given their weight in the trade-policy
analysis elsewhere in this ecosystem).

**Adjacent, not strictly diplomatic**: the Foreign Investment Facilitation Portal
(fifp.gov.in, DPIIT's FDI single-window) and data.gov.in's own "FDI Equity Inflows"
catalog entry are both closer to §2a (central government, systematic) than to this
section, but surfaced during the same search — worth folding into whichever gets
built first, since both bear on the same "which country is doing what with India"
question an MoU tracker would answer.

## 3. Standard practices (synthesized from CLAUDE.md, AI_GOVT_AFFAIRS_ANALYSIS.md, and this session's fixes)

**Publishing discipline**
1. Draft into `out/`, never edit `posts/` or `meta/*.json` directly — they're
   `snapshot.py`'s outputs. If `snapshot.py` can't reach the public feed (true for
   any sandbox without blogspot.com access), hand-editing the manifest is a
   documented, explicitly-flagged exception, never a silent one.
2. `blogger_api.py update`/`insert` always gets a `--dry-run` pass first.
3. Nothing on a timer drafts, edits, or publishes post content. Every cron is
   read-only or a narrowly-scoped sync of already-approved content. Publishing is a
   manual, reviewed action, always.
4. Version bumps mean something: MAJOR = a figure or conclusion changed, MINOR = a
   section (or a batch of new dated items) was added, PATCH = wording/styling only.

**Verification, every time, before publish**
1. `svg_chart_lint.py` on any post with a chart.
2. `content_validate.py --file ... --skip-llm` for the 10 deterministic house rules
   (JS parses, disclaimer present, translate widget, index link, table-units-in-header,
   etc.) — 10/10 is the bar, not "close enough."
3. A plain Node syntax check (`new Function(code)`) on every inline `<script>` when
   the post uses hand-rolled JS (charts, filters) — a script error silently blanks
   the whole block.
4. `render_svg_figure.py` for an actual visual check of any edited chart — a
   lint-clean SVG can still misrender (labels off-canvas, bars miscomputed).
5. For a page whose JS reads the DOM directly (the `ipa-digital-twin-reportage-latest`
   filter bar is one) — new `<li>`/`<details>` inserted in the existing markup
   pattern just work; no JS data array to keep in sync separately.

**Classification / keyword-matching (learned the hard way this session)**
1. Word-boundary every keyword (`\bpli\b`, not bare `pli`) — a bare substring match
   WILL hit "Simplify" for "pli" and "SVANidhi" for "nidhi". This exact failure mode
   is now explicitly called out in `ipa-digital-twin-reportage-latest.html`'s own
   method note, so it's a known, recurring risk, not a one-off.
2. Never chain `.*` wildcards across a whole title in a keyword regex — it matches
   across unrelated words that happen to share short substrings.
3. Spot-check every match before inserting, especially newly-written keyword lists —
   a first pass this session had 6 false positives out of 16 raw matches (37%) before
   tightening; the same tightened list on the same data produced 0 false positives on
   review.
4. State the classification method inline in the post, in plain language, so a
   reader knows a "scheme touched" chip is a keyword hit, not a manual review.

**Epistemic hygiene**
1. Every "as reported" / "per X" qualifier stays attached to the specific claim it
   qualifies, not buried in a general disclaimer.
2. A "What this piece does not establish" card names the specific sources that
   couldn't be verified directly (egress-blocked, paywalled, etc.), not a blanket
   "may contain errors."
3. When new information contradicts something already published (the tariff piece's
   stale-50%-premise correction is the reference case), correct it transparently
   with a MAJOR version bump and an explicit note — never quietly edit it away.
4. A company's own performance claim (Zaara Biotech, Carbelim, AlgaeTree) gets the
   same scrutiny as a government press release: real ≠ verified. A confirmed
   deployment (AlgaeTree's Bhopal pilot) is not the same claim as a confirmed
   capture rate.

**Network reality**
1. This sandbox's egress is a strict allowlist proxy, not a general connection —
   confirmed via `/root/.ccr/__agentproxy/status`: `masaladeutsch.blogspot.com`,
   `pib.gov.in`, `sansad.in`, every `*.gov.in`/`*.nic.in` host tried, and most state
   portals all came back `403` (`connect_rejected`, policy denial). Only the Blogger
   API itself (via `blogger_api.py`, not a raw fetch) and a short allowlist of dev
   infra (npm, PyPI, crates.io, Anthropic's own API) get through.
2. **Never treat a 403 from this proxy as retriable** — the README is explicit:
   report the blocked host, don't route around it.
3. WebSearch (not WebFetch) is the one channel that still surfaces real content
   from blocked domains — useful for spot-checks and citations, not a substitute
   for a systematic crawl.
4. Any script that needs a government or state-portal source has to run from a
   machine with real access (this session used the operator's own Mac throughout) —
   plan for that hand-off explicitly rather than discovering it mid-task.

## 4. Reachability check (2026-09-14, from this sandbox)

Every one of the following returned `403` / `connect_rejected` at the proxy
(policy denial, not a transient failure) — confirmed via
`curl -sS http://127.0.0.1:41093/__agentproxy/status`:

`pib.gov.in`, `sansad.in`, `rsdoc.nic.in`, `igod.gov.in`, `cpcb.gov.in`,
`rbi.org.in`, `data.gov.in`, `dpiit.gov.in`, `nsws.gov.in`, `meity.gov.in`,
`gis.investodisha.gov.in`, `eservices.onlineupsida.com`, `mpinfo.org`,
`ipr.punjab.gov.in`, `ap.gov.in`, and even `masaladeutsch.blogspot.com` itself
(direct fetch — the Blogger *API* still works via `blogger_api.py`'s OAuth flow,
a completely separate path).

**This means every check in §2 needs to be re-run from a machine with real network
access, not from a session like this one.** The same day, from the operator's Mac:
- `pib_index.py --update` worked cleanly (124,730 rows, current to 2026-09-14).
- `sansad.in/ls` and `sansad.in/rs` both returned 200 directly.
- The Rajya Sabha question API (`rsdoc.nic.in/...`) returned real data.
- The Lok Sabha question API (`sansad.in/api_ls/...`) still 404'd even with real
  network access — this is a genuine endpoint change/breakage, not a sandbox
  artifact. Re-discovery (mining `/ls/business`'s JS chunks the way the RS one was
  found) came up empty; the real path likely moved to a different `/ls/*` sub-page
  not yet identified, or the search UI now calls the backend a different way
  entirely (worth a browser DevTools session rather than more blind chunk-mining).

## 5. Sweep for new sources — findings this pass

### Round 1 (initial pass)

1. **Two already-known gaps got a fresh (negative) data point**: Bihar's
   documented lead is confirmed still the correct URL, still broken (302 loop) —
   no regression, no fix, just confirmed current.
2. **One new lead surfaced for Tamil Nadu**, not yet in `STATE_SOURCES.md`:
   `tn.gov.in/department/31` looks like a real DIPR department page.
3. **The Lok Sabha question API break (§4) is itself the most actionable finding
   here** — it's not a new source, but an existing one silently going stale. A
   reminder is scheduled (2026-11-20) to re-check once Parliament's Winter Session
   opens.

### Round 2 — fresh leads for 13 of the 15 unreachable states/UTs

A second WebSearch pass (not yet verified against live reachability — that needs
Mac-side `curl`, see the checklist below) found a *different* domain or path than
whatever `STATE_SOURCES.md` had already tried and failed on, for every state except
the two (Bihar, Tamil Nadu) already covered in Round 1:

| State/UT | Old (dead) lead | New lead found |
|---|---|---|
| Arunachal Pradesh | arunachalipr.gov.in (conn. error) | diprarunachal.org/press-releases/ — different domain (`.org`, not `.gov.in`) |
| Haryana | prharyana.gov.in root (404) | prharyana.gov.in/en/news-press-releases — same domain, real sub-path |
| Himachal Pradesh | himachalpr.gov.in (conn. error) | himachalpr.gov.in/PressRelease.aspx?Language=1 — same domain, specific page; worth a retry in case the earlier failure was transient |
| Jharkhand | prdjharkhand.in (302 loop) | prdjharkhand.in/iprd/index.php — same domain, specific path |
| Manipur | dipr.mn.gov.in (404) | dipr.mn.gov.in/pageInfo.aspx?contType=press_release — same domain, specific path |
| Meghalaya | meghalaya.gov.in/press-releases (404) | meghalaya.gov.in/press — different path, reportedly current through Jul 2026 |
| Tamil Nadu | dipr.tn.gov.in (conn. error) | tn.gov.in/department/31 (Round 1) |
| Tripura | icatripura.nic.in (conn. error) | ica.tripura.gov.in/press-release — different domain entirely |
| Delhi | dip.delhi.gov.in (conn. error) | publicity.delhi.gov.in/press-releases — different subdomain |
| J&K | dipr.jk.gov.in (conn. error) | dipr.jk.gov.in/ — same domain; retry, may have been transient |
| Ladakh | ladakh.gov.in/press-releases (404) | ladakh.gov.in/category/press-release/ — different path (WordPress-style taxonomy) |
| Puducherry | information.py.gov.in (conn. error) | info.py.gov.in/press-section — different subdomain |
| Andaman & Nicobar | dt.andaman.gov.in (conn. error) | andssw1.and.nic.in/doip/index.php/home/index — different domain |
| Lakshadweep | lakshadweep.gov.in/press-releases (404) | lakshadweep.gov.in/category/press-release/ — different path, same WordPress-style pattern as Ladakh (worth checking if other NE/UT sites share this template) |

None of these are confirmed live yet — WebSearch surfaces a page's existence and
title, not a working fetch. A `curl` reachability pass was handed to the operator to
run from a machine with real network access; results pending as of this writing.

### Round 2 — national platforms not yet used anywhere in this ecosystem

- **NDAP** (`ndap.niti.gov.in`) — NITI Aayog's National Data & Analytics Platform.
  Standardized-schema datasets across many sectors, explicitly designed to be
  merged/cross-referenced, with API access (mechanism unconfirmed — needs a direct
  look at the platform's own docs).
- **NITI for States** (`nitiforstates.gov.in`) — a separate NITI Aayog property: a
  Data Catalogue + Data Explorer across 10 sectors and 8 cross-cutting themes
  (SDGs, innovation, gender & social inclusion, etc.).
- **FIFP** (`fifp.gov.in`) — DPIIT's Foreign Investment Facilitation Portal, the
  actual single-window FDI application system. More operationally useful than
  descriptive, but worth knowing about alongside the diplomatic/MoU sources in §2g.
- `data.gov.in`'s general API endpoint (`data.gov.in/apis`) exists and is separate
  from the NITI-specific catalog page already known — not yet connected to
  anything in these repos.

### Round 3 — diplomatic/MoU sources

See §2g (new section) — MEA's bilateral-documents page plus 12 major embassies,
none of it previously tracked anywhere in this ecosystem.

### Still not attempted

`rbi.org.in` (macro/financial time series), PARIVESH (mentioned in
`AI_GOVT_AFFAIRS_ANALYSIS.md` as an existing connector but not located in this
sweep), and the NIRYAT trade-visualization portal (previously found blocked at the
TLS level per `india-trade-sector-policy-recommendations`'s own README — worth one
retry from a fresh IP before writing it off permanently).
