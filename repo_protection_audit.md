# Repo IP-protection audit (herrrickshaw, 128 repos)

Method: `gh repo list` (visibility, license) + file-tree scan of every repo for secret-like names, vendor-data names, strategy/backtest files, bulk data. File *names* only, plus a regex check of 6 config files for hardcoded keys (none found). Contents were not reviewed in depth, so treat this as triage.

Headline: 127 public, 1 private. 87 public repos have no LICENSE (all rights reserved by default, but nothing says so). Only 2 repos are fully protected by being private.

## Tier 1: protect now (trading edge / proprietary logic is public)
Move to private, or strip strategy files, before anything else.

| Repo | Why |
|---|---|
| market-pipeline (635MB) | 83 strategy/backtest files, 278 data files, BLOOMBERG_SOURCES.md, edgar scraper |
| global-stock-screener | 44 edge files, 118 data files, vendor scrapers (screener_in.py), BLOOMBERG_SOURCES.md |
| global-stock-screener-public | public twin of the above, same files |
| global-market-data (1GB) | warehouse + backtest roadmap + vendor scraper |
| stock-screener-platform | 61 edge files, put_call_parity/ (trading logic), vendor files |
| BazaarTalks | PIT_BACKTEST_RESULTS.md, DARVAS_VOLUME.md, Trendlyne/Screener session code |
| Bazartalks_Py2Cplus | C++ port of the quant core (darvas_volume, signal consumer) |
| global-market-scanners | Darvas/Piotroski/Coffee Can scanners + PIT backtest results |
| data_validator | 24 edge files, screener_in_auth.py |
| price_prediction_backtest | replay_signals_*.parquet (actual signals) |
| market-data-artifacts | pit_backtest*.db (point-in-time backtest databases) |
| piotroski-liquidity-research | piotroski_plus.py + forward backtest (your validated edge) |
| karz | backtest_weight_optimization.py |
| Merlin, claude-stock-tools, stock-screener-ddd | multi-strategy screeners, backtest pipelines |
| market_screener_rag, europe-stock-screener, us-stock-picks, stock-portfolio-evaluator | scoring rules / picks |
| blogger_writeups_code | 6k files, includes earnings-drift/Piotroski work drafts |
| repo-traffic-analytics | data/market-screener-backtests.json, piotroski json |

Vendor-ToS exposure (separate from edge): repos containing Screener.in / Trendlyne session scrapers and Bloomberg-source notes (global-stock-screener x2, global-market-data, stock-screener-platform, BazaarTalks, data_validator, market-pipeline). Public vendor-scraping code and any vendor-derived data are a licence risk. Your earlier memory notes already flag this as a hazard.

## Tier 2: review, then license or privatise
- digital-twin-for-ipa (Strategy_Performance_Factsheet), event-driven-stock-analysis, global-market-kdb, global-ticker-universe, market-correlation-matrices, focus-sector-investor-map, company-database + company-database-public, ltm-warehouse-tests, llm-extract-citation-fix, reg-intel, eu-ets-compliance-platform, uco-ulo-tracking, saf-monitoring-system, ship2shore_rag, agentic-insurance-agent, financial-analysis-toolkit (+ -public), prompt-efficiency-tracker (+ -public), memory-map-optimizer, claude-provenance, vertistrat
- Reason: reusable engines or commercial-looking products with no licence. Decide per repo: private, or add a source-available licence (PolyForm Noncommercial / BSL).
- Look for data files derived from paid sources before leaving any public.
- Duplicate pairs (X and X-public, mospi-dataset-analysis, etc.): make sure the "public" copy really is the scrubbed one.

## Tier 3: fine public, just add a licence
Open-data/analysis and reference repos: india-* trade/mandi/gazette/election/quality repos, lok-rajya-sabha-qa, ppac-ready-reckoner-data, fuel-retail-outlets, toll-plaza-highways, cng-cgd-retail-outlet-mapping, kalki_flooding, CBSE_paper_patterns, FCI-warehouse-MSPvsMSV, agri-commodity-tracker, india-govt-whos-who, iem-tracker, plus process-safety/design toolkits (*-design-opensource, bms/EV/battery sims, medical CV demos, hydrogen, LNG), blogs, playbooks, colab, k8s, mlflow, bin, .github, research-design-system, etc.
- Many already MIT or "other". Fill the rest (about 87) with a LICENSE and copyright header.
- Check that scraped government/third-party data redistribution terms are respected.

## Already protected
- global-market-research-platform: private (but check that its content is not duplicated into the public repos above; stock-screener-platform and bms-battery-management contain `from-global-market-research-platform/` folders, so private material has already been copied into public repos).

## Hygiene findings
- `.env.example` files only (no real `.env`) and no hardcoded keys in the 6 config files checked. Good, but gitleaks doesn't catch proprietary data, so a data-level check is still needed.
- `put_call_parity/config.py` is public in stock-screener-platform. The credentials appear to be placeholders, but the strategy parameters inside are not.
- Git history: privatising or deleting files does not remove them from history or from forks/clones. For Tier 1 repos that have been public, assume the content has been copied; rotate any secrets and consider history rewriting (git filter-repo) if the strategy parameters are the crown jewels.
