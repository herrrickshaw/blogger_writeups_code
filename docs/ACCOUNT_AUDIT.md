# Account audit — `github.com/herrrickshaw`

*Compiled 18 August 2026 across all 71 repositories on the account. This file
lives in `blogger_writeups_code` because that is the repository this session had
write access to — its subject is the whole account, not this repo. Its companion
`docs/REPO_ANALYSIS.md` is the deep read of this repository specifically.*

## Scope and method

Repositories were enumerated twice, from the account listing and from the GitHub
search API, and both agree on 71. For 70 of them this is a **metadata-level
audit**: visibility, archive state, language, description, topics, default
branch, open issues and last-push date. Nothing inside them was read.

Two exceptions were read directly: this repository (see `REPO_ANALYSIS.md`), and
`market-data-artifacts`, which was shallow-cloned to check finding 2.1.

**What this therefore cannot tell you**, and does not claim anywhere below: code
quality, test coverage, dependency health, or whether any credential is
committed in the 69 repositories that were not opened. A clean bill of health is
not implied by absence from this document.

## 1. Composition

| | |
|---|---|
| Total repositories | **71** |
| Public / private | 65 / 6 |
| Active / archived | 50 / 21 |
| Missing a description | 32 (45%) |
| Missing topics | 69 (97%) |
| Open issues, all repositories | 10 |

**Languages.** Python 43, HTML 13, none detected 7, Shell 3, Jupyter Notebook 2, CQL 1, JavaScript 1, C++ 1.

**Push recency, active repositories only.** 0-7 days: 10 · 8-30 days: 39 · 31-60 days: 1 · 60+ days: 0. Of 50 active repositories, 49 were pushed within 30 days.

## 2. Findings

### 2.1 One repository is public while its own README calls it private

`herrrickshaw/market-data-artifacts` is **public**. Its README opens
*"Market Data Artifacts (private backup)"* and states *"Private backup only —
derived market data, no personal files, no secrets."* Both the account listing
and the search API report it as public, and a shallow clone succeeded over an
anonymous, unauthenticated read — which is the practical confirmation that
anyone can fetch it.

Contents: 34 tracked files. `caches/` holds `edgar_facts.db` (point-in-time SEC
EDGAR facts), `fundamentals_cache.db` (yfinance fundamentals), `market.duckdb`,
and `viability*` / `dvm_*` / `pit_backtest*` screen and backtest results.
`seed_ohlc/` holds a 19-market daily OHLC seed as parquet. All are Git-LFS
tracked via `.gitattributes`.

**On severity — this is a labelling mismatch, not a breach.** The contents are
derived market data from public sources; the README's "no personal files, no
secrets" claim is consistent with what is in the tree; and the account's LFS
budget is exhausted, so the data files currently resolve to ~130-byte pointer
stubs rather than downloadable objects. Nothing sensitive is demonstrably
exposed today.

The reason to fix it anyway is second-order, and it is the real one: **a
repository you believe is private is where a secret eventually lands.** The
README has been telling every reader, including its author, that this is private
storage. Either set the repository private, or rewrite the README so the next
push into it is made with correct expectations. The current state is the one
combination that quietly invites a mistake.

### 2.2 The Git-LFS budget is exhausted account-wide

Recorded in that repository's own `DATA_ACCESS.md`: 30 LFS objects totalling
240.1 MB in that repo alone, and the budget is out **account-wide, not per
repository**. Any clone of an LFS-tracked repository yields pointer stubs unless
`GIT_LFS_SKIP_SMUDGE=1` is set, and the real files cannot be pulled at all.

This is not a latent problem — it is currently breaking data retrieval, and it
is the constraint driving the deduplication work in 2.3. Worth stating plainly
because it is invisible from the repository list: every affected repo looks fine
until someone tries to clone it.

### 2.3 Heavy thematic concentration — already a known problem

Twelve active repositories cover overlapping equity screening, backtesting and
portfolio work (see §3). Ordinarily this would be the headline finding.

It is not, because the account already answers it. `repo-data-dedup` carries a
`PLAYBOOK.md` (a migration recipe off LFS), a `SOP_DATA_SOURCES.md` (source
catalogue and re-collection procedure) and a full pointer inventory, and
`market-data-artifacts` cross-references all three. Consolidation is in flight,
not a blind spot, and this document should not present it as news.

The observation worth adding is narrower: the deduplication effort is itself
spread across three repositories (`repo-data-dedup`, `market-data-artifacts`,
`global-stock-screener`), and `market-data-artifacts/DATA_ACCESS.md` already
notes its own contents "overlap `global-stock-screener`; check there first". A
consolidation plan that needs a cross-reference to explain where its own data
lives is at risk of the problem it was created to solve.

### 2.4 Discoverability is thin for 65 public repositories

**32 of 71 repositories (45%) have no description, and 69 of 71 (97%) have no
topics** — only `global-market-scanners` and `claude-stock-tools` carry any, and
the latter is archived.

For private repositories this costs nothing. For 65 public ones it is the
difference between findable and invisible: GitHub search and topic pages are
driven by exactly these two fields. It lands hardest on substantial work that
gives a reader nothing to go on — `digital-twin-for-ipa`, `market_screener_rag`,
`price_prediction_backtest`, `global-ticker-universe`, `kalki_flooding` and
`karz` all ship code under a bare name.

This is the cheapest item in this document to fix and the only one whose benefit
is external rather than internal.

### 2.5 Three default branches differ from the rest

`india-election-analysis` and `Merlin` default to `master`; the other 69 use
`main`. Both are archived, so this is cosmetic.

`working-files` (private, active) defaults to **`import/working-files`**, which
reads like an import branch that became the default and was never moved. Worth
checking whether `main` exists there and carries the work someone would expect
to find on a default checkout.

## 3. Thematic concentration

| Cluster | Repos | Active | Archived |
|---|---:|---:|---:|
| Equity screening / quant platform | 17 | 11 | 6 |
| India trade / macro analysis | 11 | 7 | 4 |
| Fuel / energy / OMC | 9 | 5 | 4 |
| Local machine / agent tooling | 8 | 6 | 2 |
| Market data warehouse / pipeline | 6 | 5 | 1 |
| Blog / publishing | 4 | 4 | 0 |
| Agri / food | 4 | 4 | 0 |
| Battery / EV | 3 | 2 | 1 |
| Health | 2 | 2 | 0 |
| *(unclustered)* | 7 | 4 | 3 |

The equity cluster in full, active first:

- **`BazaarTalks`**
- **`Bazartalks_Py2Cplus`**
- **`colab-market-fundamentals`**
- **`global-market-scanners`**
- **`global-stock-screener`**
- **`global-ticker-universe`**
- **`market-correlation-matrices`**
- **`market_screener_rag`**
- **`piotroski-liquidity-research`**
- **`price_prediction_backtest`**
- **`stock-screener-platform`**
- ~~`claude-stock-tools`~~ (archived)
- ~~`europe-stock-screener`~~ (archived)
- ~~`event-driven-stock-analysis`~~ (archived)
- ~~`market-brief-base`~~ (archived)
- ~~`stock-portfolio-evaluator`~~ (archived)
- ~~`stock-screener-ddd`~~ (archived)

## 4. What is healthy

Stated because an audit that lists only problems misrepresents the thing it
audits.

**The account is actively worked, not accumulating abandonware.** Of 50 active
repositories, 49 were pushed within the last 30 days and 10 within the last
week. The single repository past 30 days is at 31.

**Archiving is used deliberately.** 21 repositories are archived rather than
left to rot in an ambiguous state — including entire superseded lines of work
(`europe-stock-screener`, `stock-screener-ddd`, `event-driven-stock-analysis`).
The account distinguishes "finished with this" from "still live", which is
what makes the 50 active repositories meaningful as a number.

**Issue debt is near zero** — 10 open issues across 71 repositories, four of
them in this repo.

**The known problems have written plans attached.** The LFS and duplication
issues are documented in `repo-data-dedup` with a playbook and an SOP, not
carried as folklore.

## 5. Recommended order

1. **Resolve the `market-data-artifacts` visibility mismatch** (§2.1) — set it
   private, or rewrite the README. Minutes, and it closes the one finding here
   with a plausible bad outcome attached.
2. **Deal with the LFS budget** (§2.2) via the existing `PLAYBOOK.md`. It is
   actively breaking clones and blocking the consolidation work.
3. **Add descriptions and topics to the public repositories** (§2.4). Cheap,
   external benefit, and it makes the account legible to anyone who finds it.
4. **Check `working-files`' default branch** (§2.5).
5. **Continue the consolidation already planned** (§2.3), with the caveat that
   the plan itself now spans three repositories.

Items 1 and 2 have a failure mode attached. Items 3 to 5 are hygiene.

## 6. Limits

A metadata read of 70 repositories and a shallow read of one, taken on a single
day. It cannot speak to code quality, test coverage, dependency health or
committed credentials in the 69 repositories that were not opened, and it should
not be cited as evidence that those are clean — only that they were not
examined. A genuine secret-scanning pass means cloning each repository and
scanning its contents, which this was not.

Every count is reproducible from the appendix below.


---

## Appendix — full inventory

Sorted by last push, newest first. `desc` / `topics` mark metadata presence.

| # | Repository | Vis | State | Language | desc | topics | Branch | Issues | Last push |
|--:|---|---|---|---|:--:|:--:|---|--:|---|
| 1 | `blogger_writeups_code` | private | active | HTML | y | **n** | main | 4 | 2026-08-18 |
| 2 | `global-market-research-platform` | public | active | CQL | y | **n** | main | 3 | 2026-08-18 |
| 3 | `global-market-data` | public | active | Python | y | **n** | main | 0 | 2026-08-17 |
| 4 | `repo-traffic-analytics` | private | active | Python | **n** | **n** | main | 0 | 2026-08-17 |
| 5 | `masaladeutsch` | public | active | JavaScript | y | **n** | main | 0 | 2026-08-16 |
| 6 | `digital-twin-for-ipa` | public | active | Python | **n** | **n** | main | 0 | 2026-08-16 |
| 7 | `agri-commodity-tracker` | public | active | Python | y | **n** | main | 0 | 2026-08-15 |
| 8 | `cache_memory_cleaner` | public | active | Shell | y | **n** | main | 0 | 2026-08-14 |
| 9 | `memory-map-optimizer` | public | active | Python | **n** | **n** | main | 0 | 2026-08-14 |
| 10 | `ai-tools-tracker` | public | active | — | **n** | **n** | main | 0 | 2026-08-11 |
| 11 | `fuel-retail-outlets` | public | active | HTML | y | **n** | main | 0 | 2026-08-08 |
| 12 | `india-omc-fuel-fleet-model` | public | active | Python | y | **n** | main | 1 | 2026-08-08 |
| 13 | `repo-data-dedup` | public | active | Shell | **n** | **n** | main | 0 | 2026-08-08 |
| 14 | `kalki_flooding` | public | active | Python | **n** | **n** | main | 0 | 2026-08-08 |
| 15 | `india-govt-yellow-pages` | public | active | HTML | **n** | **n** | main | 0 | 2026-08-08 |
| 16 | `CBSE_paper_patterns` | public | active | Python | y | **n** | main | 0 | 2026-08-08 |
| 17 | `market-pipeline` | private | active | — | **n** | **n** | main | 0 | 2026-08-06 |
| 18 | `research-design-system` | public | active | Python | y | **n** | main | 0 | 2026-08-04 |
| 19 | `global-stock-screener` | public | active | Python | y | **n** | main | 0 | 2026-08-04 |
| 20 | `india-trade-data-analysis` | public | active | HTML | y | **n** | main | 0 | 2026-08-03 |
| 21 | `india-commodity-trade-deficit` | public | active | HTML | y | **n** | main | 0 | 2026-08-03 |
| 22 | `india-trade-sector-policy-recommendations` | public | active | HTML | y | **n** | main | 0 | 2026-08-02 |
| 23 | `mospi-dataset-analysis` | private | active | HTML | **n** | **n** | main | 0 | 2026-08-02 |
| 24 | `Ai_for_exploration` | public | active | Shell | **n** | **n** | main | 0 | 2026-08-02 |
| 25 | `price_prediction_backtest` | public | active | Python | **n** | **n** | main | 0 | 2026-08-01 |
| 26 | `piotroski-liquidity-research` | public | active | Python | y | **n** | main | 0 | 2026-08-01 |
| 27 | `market_screener_rag` | public | active | Python | **n** | **n** | main | 0 | 2026-08-01 |
| 28 | `global-market-scanners` | public | active | Python | y | y | main | 0 | 2026-08-01 |
| 29 | `BazaarTalks` | public | active | Python | y | **n** | main | 1 | 2026-08-01 |
| 30 | `Bazartalks_Py2Cplus` | public | active | C++ | y | **n** | main | 0 | 2026-08-01 |
| 31 | `jal_jeevan_lottery` | public | active | — | **n** | **n** | main | 0 | 2026-07-31 |
| 32 | `FCI-warehouse-MSPvsMSV` | public | active | HTML | **n** | **n** | main | 0 | 2026-07-31 |
| 33 | `jai_kisan_jai_javan` | public | active | HTML | **n** | **n** | main | 0 | 2026-07-31 |
| 34 | `vehicle_fuel_mileage` | public | active | Python | **n** | **n** | main | 0 | 2026-07-29 |
| 35 | `cng-cgd-retail-outlet-mapping` | public | active | HTML | **n** | **n** | main | 0 | 2026-07-29 |
| 36 | `india-trade-tracker` | public | active | Python | y | **n** | main | 0 | 2026-07-27 |
| 37 | `global-ticker-universe` | public | active | Python | **n** | **n** | main | 0 | 2026-07-27 |
| 38 | `market-correlation-matrices` | public | active | Python | **n** | **n** | main | 0 | 2026-07-24 |
| 39 | `cell-guardian` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 40 | `ev-battery-management-sim` | public | active | Python | y | **n** | main | 0 | 2026-07-22 |
| 41 | `.github` | public | active | — | **n** | **n** | main | 0 | 2026-07-22 |
| 42 | `hydrogen-electrolyser-control` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 43 | `toll-plaza-highways` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 44 | `stock-screener-ddd` | public | archived | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 45 | `stock-portfolio-evaluator` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 46 | `saf-monitoring-system` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 47 | `prenatal-care-toolkit` | public | active | Python | y | **n** | main | 0 | 2026-07-22 |
| 48 | `ltm-warehouse-tests` | public | active | Python | y | **n** | main | 0 | 2026-07-22 |
| 49 | `karz` | public | active | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 50 | `india-trade-export-analysis` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 51 | `india-election-analysis` | public | archived | Python | **n** | **n** | `master` | 0 | 2026-07-22 |
| 52 | `india-ec-subsector-analysis` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 53 | `heart-valve-defect-detection` | public | active | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 54 | `focus-sector-investor-map` | public | archived | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 55 | `event-driven-stock-analysis` | public | archived | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 56 | `europe-stock-screener` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 57 | `discom-debt-and-revenue-models` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 58 | `data_validator` | public | archived | Python | **n** | **n** | main | 0 | 2026-07-22 |
| 59 | `colab-market-fundamentals` | public | active | Jupyter Notebook | y | **n** | main | 0 | 2026-07-22 |
| 60 | `colab-experiments` | public | archived | Jupyter Notebook | y | **n** | main | 0 | 2026-07-22 |
| 61 | `claude-stock-tools` | public | archived | Python | y | y | main | 0 | 2026-07-22 |
| 62 | `claude-lmstudio-router` | public | archived | Python | y | **n** | main | 0 | 2026-07-22 |
| 63 | `bms-battery-management` | public | active | Python | y | **n** | main | 0 | 2026-07-22 |
| 64 | `Merlin` | public | archived | Python | **n** | **n** | `master` | 0 | 2026-07-22 |
| 65 | `stock-screener-platform` | public | active | HTML | y | **n** | main | 1 | 2026-07-22 |
| 66 | `market-data-artifacts` | public | active | — | y | **n** | main | 0 | 2026-07-22 |
| 67 | `working-files` | private | active | HTML | **n** | **n** | `import/working-files` | 0 | 2026-07-22 |
| 68 | `market-brief-base` | private | archived | Python | **n** | **n** | main | 0 | 2026-07-21 |
| 69 | `mospi-dataset-analysis-public` | public | active | HTML | **n** | **n** | main | 0 | 2026-07-18 |
| 70 | `india-forex-analysis` | public | archived | — | y | **n** | main | 0 | 2026-07-03 |
| 71 | `interpreter_toolkit` | public | archived | — | **n** | **n** | main | 0 | 2026-07-03 |
