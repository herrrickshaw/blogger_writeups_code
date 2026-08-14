# Cross-post knowledge graph (this session's research cluster)

Links the 10 posts written/updated in this session's connected research
thread — currencies, trade agreements, sovereign debt, and energy — through
the real-world entities (countries, institutions, agreements) they share, so
the actual cross-referencing structure of the reporting is visible as a
graph rather than just prose links.

## Posts included

1. Raising Green Debt Globally (REC EuroYen, sovereign-ceiling ratings)
2. Where the Rupee Actually Stands (10y FX trends, NEER/REER)
3. Financing the Fuel-to-Chemicals Pivot (IOCL debt, refinery-petrochem capex)
4. What TEPA Actually Opens (EFTA goods, tariff schedule)
5. Tamil Nadu Wind Potential (NIWE)
6. Can Rupee Trade Actually Offset the Inflation India Is Importing?
7. What India Is Actually Paying For (post-COVID import bill)
8. If India Paid BRICS in Rupees (de-dollarisation scenario)
9. Where the World's Oil Sits (global storage, Hormuz)
10. India's Coking Coal Import Problem

## Method

1. **Entity extraction**: [`dslim/bert-base-NER`](https://huggingface.co/dslim/bert-base-NER)
   (Hugging Face Hub, BERT fine-tuned on CoNLL-2003) run locally via
   `transformers`, CPU inference, no API key. Each post's rendered plain text
   (HTML tags stripped) was chunked to ~350 words per NER call and entities
   aggregated with `aggregation_strategy="simple"`.
2. **Cleaning**: dropped low-confidence tags (score < 0.80), wordpiece
   fragments, nationality adjectives used as generic filler ("Indian",
   "Chinese"), and site-wide accessibility-widget boilerplate (footer links
   to Trestle Labs / Jyoti AI that appear on every post regardless of
   content). A small canonicalisation map merges obvious tokenisation splits
   (`"S & P"` → `S&P Global`, `"Moody ' s"` → `Moody's`, `"DGCI & S"` →
   `DGCI&S`).
3. **Pruning to a real graph**: an entity earns a node only if it appears in
   **2 or more** of the 10 posts — that's the actual cross-post linking
   signal. Entities mentioned in only one post are real but don't tell you
   anything about how the posts relate to each other, so they're excluded
   from this graph (they're still in `masaladeutsch_kg.json`'s raw NER pass
   if you want the full per-post entity list).
4. **Graph construction**: `networkx`, undirected bipartite-ish graph —
   post nodes and entity nodes, edge = "this entity is mentioned in this
   post." Exported to GraphML (for Gephi/Cytoscape) and node-link JSON.

## What it actually shows

The highest-degree hub entities — **India** (10/10 posts), **China**,
**Russia**, **RBI**, **Saudi Arabia**, **PIB**, **USA**, **UAE** — are exactly
the five trading partners and two regulatory bodies this research thread was
built around, which is a reasonable sanity check that the extraction is
capturing real signal rather than noise. The graph's structure also makes an
implicit editorial fact explicit: the currency/trade-partner cluster (posts
2, 3, 6, 7, 8) is far more densely interconnected than the energy cluster
(posts 1, 5, 9, 10), because the currency pieces deliberately cross-reference
the same five countries repeatedly, while the energy pieces each stand more
independently.

## Files

- `masaladeutsch_kg.graphml` — full graph, GraphML format
- `masaladeutsch_kg.json` — same graph, node-link JSON
- `charts/masaladeutsch_kg.svg` — force-directed layout visualisation (networkx spring layout, static SVG)

## Known limitations

- No relation *typing* beyond "co-mentioned" — this is a co-occurrence graph,
  not a triples-based knowledge graph with typed edges (e.g. it doesn't
  encode "REC ISSUED EuroYen-bond" as a directed, labelled edge). A proper
  relation-extraction pass (e.g. a HF REBEL-style model) would be needed for
  that and was out of scope here.
- `dslim/bert-base-NER` is a general-purpose CoNLL-trained model, not
  finance/trade-domain-tuned — it correctly catches countries and named
  organisations but will miss or mis-tag domain-specific entities like HS
  codes, currency-pair tickers, or bond ISINs entirely.
- 10-post scope, not site-wide (158 posts) — sized to this session's
  connected research thread, not the whole archive.
