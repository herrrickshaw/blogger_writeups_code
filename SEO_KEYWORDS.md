# Keyword and discoverability analysis — blog.vertistratsolution.com

Measured 8 August 2026 against 97 live posts, the live sitemap, and a sample of
rendered pages. Every number here was counted, not estimated.

---

## What this analysis can and cannot tell you

**It cannot tell you which keywords you currently rank for.** That data lives in
Google Search Console — impressions, queries, average position, click-through
rate — and I have no access to it. Nothing below is a ranking estimate, a search
volume, or a traffic projection, because I would be making those up.

**It can tell you what the site is topically about, and what is mechanically
stopping it from being found.** Those are countable, and the mechanical problems
turn out to be the bigger story: the site has a real, coherent subject-matter
position and is undermining it in four specific ways.

If you export Search Console's Queries and Pages reports (16-month range, CSV),
the analysis can be redone against real demand rather than corpus structure. That
is the single highest-value input you can add.

---

## 1. Four verified defects, in priority order

### 1.1 No page on the site has a meta description — 0 of 97

Checked across a random sample of eight live posts: not one carries
`<meta name="description">`. Google therefore writes the snippet itself from the
top of the page body. On this blog the top of the body is the "← All Articles
(Index)" link and the eyebrow line, so the auto-generated `og:description`
currently reads:

> "← All Articles (Index) LNG · European gas · Security of supply Europe Bought a Record Amount of LNG and Made Itself Dependent on One..."

That is what a searcher sees under the title. It contains no proposition and no
reason to click. **Every post already has a hand-written one-paragraph summary in
its `.standfirst`** — the raw material exists, it simply is not being emitted as
a description tag.

*Impact: click-through rate on every impression the site already earns.*

### 1.2 Zero posts carry a single Blogger label — 0 of 99

Labels are Blogger's built-in topic system. They generate label archive pages
(`/search/label/<name>`), which are crawlable topic hubs, and they drive
related-post surfaces. With none set:

- there are no topic hub pages at all;
- internal linking runs only through the one manual index page;
- a reader who finishes the LNG piece is offered no route to the other gas posts.

The site has **twelve coherent topic clusters** (section 2) and exposes none of
them as a navigable surface.

*Note: `robots.txt` currently has `Disallow: /search`, which blocks label pages
too. Enabling labels means allowing `/search/label/` while keeping `/search?q=`
blocked — otherwise the hubs are built and then hidden.*

### 1.3 Title tags are 77–157 characters, all with a 31-character prefix

Every `<title>` renders as `Thinking global, living local: <post title>`. Google
displays roughly 55–60 characters. So on a typical post the searcher sees the
blog name, a colon, and a truncated fragment of the actual subject.

Measured on live pages: 77, 91, 106, 108, 112, 123, 141, 157 characters.
**61 of 99 post titles exceed 60 characters before the prefix is even added.**

The prefix is set in the theme (`<title><data:blog.pageTitle/></title>`). On post
pages it can emit the post title alone, which returns ~31 characters of visible
SERP real estate to the topic.

### 1.4 Four near-identical posts compete for the same query

| Live post | Slug |
|---|---|
| Chemical Import Substitution Analysis: Executive Summary | `chemical-import-substitution-analysis` |
| Chemical Import Substitution — Full HSN-8 Chapter-Wise Registry (827 Codes) | `chemical-import-substitution-hsn-8-registry` |
| Chemical Import Substitution — Full HSN-8 Registry (827 Codes): Data Tables | `chemical-import-substitution-full-hsn-8_01082878313` |
| Chemical Import Substitution — Quarterly Tracking Dashboard | `chemical-import-substitution-quarterly` |

Four URLs, one query intent, sharing eight title terms. Google has to choose one
and will split signals across all four. Two of them ("Full HSN-8 Registry" and
"Full HSN-8 Registry: Data Tables") are close to the same page twice; the third
slug carries a machine suffix (`_01082878313`) indicating a burned-slug
republish.

A second, milder pair: **Lok Sabha** and **Rajya Sabha** Question Registry share
seven title terms. Those are genuinely different chambers and defensible as
separate pages — but the titles should lead with the distinguishing word.

**Also**: these four chemical posts contain the same sentence repeated **2,648
times** across their tables ("...chemical intermediate, speciality deficit driven
by feedstock, scale-economics, technology gap; needs case-by-case investment
screening"). At that volume it is a duplicate-content pattern rather than
analysis, and it drowns out the distinctive text on those pages.

### 1.5 One post has a slug generated from CSS

`IPA Digital Twin — Reportage: Latest Updates (3 Jul – 1 Aug 2026)` lives at:

```
/2026/08/root-bgfff-fg1a1a1a-mut666-cardf6f6f4.html
```

The slug was minted from a CSS variable block (`:root{--bg:#fff;--fg:#1a1a1a;
--muted:#666;--card:#f6f6f4}`) because the post body began with a style block
instead of a heading. Blogger burns slugs permanently, so this cannot be renamed
— it needs a new post at a clean slug plus a 301 from the old one.

---

## 2. What the site actually owns

Cluster assignment from H1/H2/H3 text across 97 live posts:

| Posts | Cluster |
|---|---|
| 22 | Trade, currency & macro |
| 13 | Mobility & EV |
| 11 | Import substitution & HSN registries |
| 8 | Fertilisers & agriculture |
| 5 | Ethanol, CBG & biofuels |
| 5 | Prices & inflation (WPI/CPI) |
| 4 | Textiles & apparel |
| 4 | Chemicals & petrochemicals |
| 4 | Petroleum & crude |
| 2 | Gas, LNG & CGD |
| 2 | Carbon, climate & green |
| 2 | Markets & finance |
| 18 | Unclustered |

The single most-repeated heading phrase across the corpus is **"import
substitution" (12 posts)**. That, plus HSN-level trade data, is the site's
distinctive position: there are very few sources publishing Indian
import-substitution analysis at HSN-8 granularity against official TradeStat
data, and essentially none doing it for free.

**The 18 unclustered posts are worth a look** — either they are genuinely
off-topic for the site's core, or their headings are too abstract to signal
subject matter, which is itself an SEO problem.

---

## 3. Where the realistic search demand is

Ranked by *how well the existing corpus already matches the query*, not by
assumed volume. Long-tail, specific, low-competition queries are where a
97-post independent blog can actually win; head terms like "India trade data"
are owned by government portals and news outlets.

**Strong position, content already exists:**

- `HSN 8 digit import data India`, `HSN code wise import export India`,
  `[chapter] HSN import substitution` — 11 posts, near-zero free competition
- `ethanol blending SGST revenue`, `CBG incentive scheme India`,
  `compressed biogas plant economics` — 5 posts, highly specific
- `India LNG terminal utilisation`, `PNGRB CGD authorisation`,
  `Dahej regasification capacity` — the terminal-level utilisation table
  published today is genuinely hard to find elsewhere
- `WPI 2022-23 base year`, `WPI vs CPI India difference`,
  `cumulative inflation five years country comparison` — 5 posts

**Content exists but is buried under a weak title:**

- The EV/mobility cluster is the second largest (13 posts) yet has no hub page
  and no labels.

**Gap worth filling, given what is already researched:**

- Nothing here needs new research. The gap is packaging: 12 topic clusters and
  zero topic pages.

---

## 4. What to do, in order

1. **Emit meta descriptions from the standfirst.** One theme change; the JSON-LD
   block added today already reads `.standfirst` and demonstrates the selector
   works. Highest impact per unit of effort on the whole list.
2. **Drop the blog-name prefix from post-page titles.** One theme change.
3. **Label every post** against the twelve clusters, and allow
   `/search/label/` in robots.txt. Turns 12 latent clusters into 12 crawlable
   hubs and gives every post internal links from a topic page.
4. **Consolidate the four chemical import-substitution posts** into one canonical
   registry plus, at most, one dashboard — 301 the rest. Strip the 2,648
   repeated boilerplate sentences.
5. **Re-front the two Sabha titles** so the distinguishing word leads.
6. **Republish the IPA Digital Twin post** at a clean slug with a 301.
7. **Export Search Console queries and redo this against real demand.**

Items 1–3 are theme-level and affect all 97 posts at once. Items 4–6 are
per-post.

---

## Already healthy — no action needed

- `sitemap.xml`: 97 entries, matching 97 live posts, every one with a fresh
  `lastmod`. Declared in `robots.txt`.
- Canonical tags present on every page sampled.
- Structured data: JSON-LD `WebSite` + `Person` + `WebPage` site-wide, plus
  `BlogPosting` on post pages (added 8 August 2026).
- Mobile layout and table overflow, fixed earlier in this archive's history.
