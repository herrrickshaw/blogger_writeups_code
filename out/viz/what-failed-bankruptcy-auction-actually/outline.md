Revised
15 September 2026
· v1.0.0 · [what changed](#changelog)

9,531IBBI liquidation auction notices on record, scraped 24 Jul 2026

25%, then 10%pre-2024 markdown schedule after a failed auction

3separate auction rounds recorded for Athena Chhattisgarh Power alone

13+ yrsDunlop India's most valuable property has been in liquidation litigation

India's Insolvency and Bankruptcy Board maintains a public, page-by-page list of every liquidation auction notice issued under the IBC — corporate debtor, reserve price, what's for sale, when the auction is. Individually, each one is a routine filing. Assembled into a single register of 9,531 notices, they show a mechanism that rarely gets discussed in percentage terms: a real, regulator-set markdown schedule for what happens when nobody bids.

## A register nobody reads end to end

The notices sit at ibbi.gov.in, twenty to a page, roughly 481 pages deep. A full scrape run on 24 July 2026 captured 9,528 of 9,531 listed notices, with fields for the corporate debtor's name, notice and auction dates, the insolvency professional running the sale, the reserve price, and a free-text description of the assets on offer.

A data-quality catch, on the record. The single highest reserve price in the raw scrape — ₹90,000 crore, against a corporate debtor named "LIQQQQQQQQQQQQQQQQQQQ" and an asset description of "zxc" — is an obvious corrupted or placeholder row, not a real auction notice. It is excluded from every figure in this post. A scraped government register deserves the same scrutiny as any other source before a number from it gets quoted.

## What gets marked down, and by how much

Until a February 2024 amendment tightened the rule, IBBI's Liquidation Process Regulations let a liquidator cut the reserve price by up to 25% after the first failed auction, and by up to a further 10% after each failed auction beyond that. That is not a vague industry habit — it is a specific, regulator-set percentage, and the register shows it applied almost exactly.


[T1 "What gets marked down, and by how much" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Corporate debtor | c1 Auction date | c2 Reserve price | c3 Change
  r0: Athena Chhattisgarh Power | 22 Dec 2021 | ₹1,503.08cr | —
  r1: Athena Chhattisgarh Power | 7 Jan 2022 | ₹1,127.31cr | -25.0%
  r2: Athena Chhattisgarh Power | 24 Jan 2022 | ₹1,014.58cr | -10.0%
  r3: Punj Lloyd | 10 Jul & 28 Aug 2023 | ₹1,061.00cr | —
  r4: Punj Lloyd | 13 Oct 2023 | ₹955.00cr | -10.0%


[chart: 
 
 The Markdown Ladder, in One Company's Numbers 
 Athena Chhattisgarh Power's reserve price, three liquidation-auction rounds, Dec 2021–Jan 2022 

 Round 1 (22 Dec 2021) 
 
 ₹1,503.08cr 

 Round 2 (7 Jan 2022, −25.0%) 
 
 ₹1,127.31cr 

 Round 3 (24 Jan 2022, −10.0%) 
 
 ₹1,014.58cr 

 Three rounds inside five weeks, cut by the maximum the pre-2024 regulation allowed at each step: 
 25% after the first failed auction, then a further 10% after the next. 
 Source: IBBI liquidation-auction-notice register, scraped 24 Jul 2026, as cited in this post. 
]

A near-exact textbook case of IBBI's pre-2024 markdown schedule: 25%, then 10%, on successive failed auctions.

Athena Chhattisgarh Power's three rounds inside five weeks are a near-exact textbook case: a 25.0% cut on the first re-listing, then a further 10.0% cut on the second — the maximum the old regulation allowed at each step. Punj Lloyd's register entries show the same 10% step on its final re-listing. Not every repeat listing in the register follows this pattern this cleanly: Ind-Barath Thermal Power's plant and land near Tuticorin and Karwar appear at three different reserve prices across mid-to-late 2023 that don't move in one direction, because each listing bundled a different combination of the sale's ten defined asset blocks rather than simply re-offering the same lot cheaper. The markdown ladder is real; it isn't the only thing driving repeat listings.

## What's actually being sold

The free-text asset descriptions, however inconsistently worded, point in one clear direction: liquidation auctions are overwhelmingly a real-estate and physical-plant register, not a market for brands, patents or going-concern intangibles.


[T2 "What's actually being sold" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 Asset type (as described) | c1 Notices
  r0: Land and Building | 157
  r1: Land | 120
  r2: Land & Building | 93
  r3: Plant & Machinery (both spellings) | 147
  r4: Open Plot | 32
  r5: Inventory | 34
  r6: Residential Flat | 23


Counts are for the exact free-text phrasing captured in the scrape; near-duplicate wordings for the same underlying asset type (for example "Land & Building" vs "Land and Building") were not merged beyond the two Plant & Machinery spellings shown, so the true totals for land- and building-type assets are almost certainly higher than any single row here suggests.

## The long tail: Dunlop India, thirteen years and counting

The Calcutta High Court, where Dunlop India's 2013 winding-up order and the litigation over its most valuable Kolkata property are still being worked through, thirteen years on. Source: Flickr upload bot, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Calcutta_High_Court.jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).

Most of the register is auctions that eventually clear, at some markdown. Dunlop India Ltd. — incorporated in 1929 as Dunlop Rubber Co. (India), later passing from the Chhabria (Jumbo) group to the Ruia group in 2005 — shows the other tail. Its Sahaganj (Hooghly, West Bengal) and Ambattur (Chennai) plants were suspended in 2011 and 2012; the Calcutta High Court ordered the company wound up on 31 January 2013, with an appeal dismissed that May. What has followed since is not a sale but litigation: a division-bench order the same year flagged an allegation that roughly ₹2,300 crore of the company's most valuable properties had been surreptitiously transferred while the case sat before the erstwhile Board for Industrial and Financial Reconstruction. One of those properties — a 50% share in "Kings Court," a five-storey, twelve-flat building on Chowringhee Road in Kolkata — is still contested: a Calcutta High Court judgment as recent as 17 March 2026 let an official-liquidator auction stand while giving one rival claimant the right to match the winning bid and another the liberty to separately sue for specific performance. Thirteen years after the winding-up order, the company's most valuable urban asset has still not finished changing hands.

## The net read

A single register holds both stories at once. For most of the 9,531 notices, "liquidation" means a plant, a plot or a flat moving through a markdown ladder the regulator wrote down in percentages, clearing eventually at some discount to its first asking price. For a smaller number, it means a company that stopped operating over a decade ago, its most valuable land or buildings still working through the courts long after the corporate entity itself ceased to matter. The register counts every auction attempt; it does not, on its own, tell you which kind of case any single notice belongs to.

Sources: this ecosystem's own digital-twin-for-ipa research (layer 34, "stressed_assets," built 2026-09-14), specifically its live IBBI liquidation-auction-notice register (scraped from ibbi.gov.in/liquidation-auction-notices on 24 July 2026, 9,528 of 9,531 notices captured; reserve-price and auction-date figures for Athena Chhattisgarh Power, Punj Lloyd and Ind-Barath Thermal Power, and the asset-type-mix counts, are drawn directly from that scrape) and its worked case study on Dunlop India (sourced in turn to a Calcutta High Court division-bench order and a 17 March 2026 judgment on indiankanoon.org, not independently re-verified against the court record for this post). The pre- and post-February-2024 IBBI reserve-price markdown rules are per legal-industry coverage of the amendment (Lexology, TaxGuru) found via search.

Revision history.

- v1.0.0 — 15 September 2026 — first published.

Related on this blog: [India's 14 PLI Schemes, and Every Company Publicly Named as a Winner, 2019–2026](https://blog.vertistratsolution.com/2026/08/nine-ministries-one-list-every-company.html) — another piece built the same way — reading a full official registry end to end rather than telling one case's story.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
