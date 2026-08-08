# Project bonds and the carry trade: how the cheap-money channel actually reaches an Indian project

*8 August 2026. Built on deal data already verified in this blog's sustainable-debt piece
(REC EuroYen, IREDA, PFC–JBIC), BIS policy-rate series as previously retrieved, and current
reporting on NaBFID's credit-enhancement facility. Every number's provenance is stated;
the covered-interest-parity discipline from the earlier piece is applied throughout.*

---

## 1. Two instruments, one question

A **project bond** is debt sold against the cash flows of a specific project — an SPV's
toll receipts or a solar park's PPA payments — rather than against a corporate balance
sheet. The **carry trade** is funding in a low-rate currency to deploy at higher rates
elsewhere. The question in this brief is where the two genuinely meet: does cheap yen or
euro money actually lower the cost of building an Indian road or solar park, and through
what channel?

The honest answer, which the deal record supports: **the carry reaches Indian projects
almost entirely second-hand, through intermediaries — and the part of the "carry" that
survives hedging is not the interest differential at all, but the credit-spread and
investor-base advantage.** Project bonds proper are the *domestic* leg of the machine,
and 2025-26 is the first year India has built dedicated plumbing for them.

## 2. The carry, priced honestly

The visible gap is large: on the BIS policy-rate series used in the blog's earlier piece,
**RBI repo 5.25% vs Bank of Japan 1.00% — roughly a 4.25pp differential** (ECB 2.25%,
Fed ~3.6%). The verified deals show what that becomes in practice:

| Deal | Terms | What it proves |
|---|---|---|
| REC ¥61.1 bn EuroYen green bond (Jan 2024) | Coupons **1.76–2.20%**, ~50% Japanese book, GMTN format | Nominal coupons a third of domestic; a new investor base (Japanese insurers, regional banks) |
| IREDA ¥26 bn 5-yr loan, SBI Tokyo (Mar 2025) | **Hedged all-in landed under 7% — cheaper than domestic** | The real test: *after* hedging, still beats INR funding |
| PFC–JBIC ¥120 bn facility (Jan 2025); NLC ¥15.46 bn (Dec 2025) | Policy-bank anchored | The channel is repeatable, not a one-off |

**Covered interest parity is the discipline:** hedging INR/JPY forward costs roughly the
rate differential, so a 2% yen coupon hedges into approximately a domestic-cost
instrument. The naive carry — "borrow at 2%, lend at 9%" — exists only unhedged, which
is not a strategy but an open FX position; the 2013 taper episode is what that looks
like when it closes. What *survives* hedging, and what made IREDA's all-in land below
7%, is that **Japanese lenders price Indian PSU credit tighter than the domestic market
does**, plus tenor availability and hedge-market basis. The blog's earlier formulation
stands: *choose the currency for the investor base and the hedge economics; treat any
unhedged FX gain as luck.*

## 3. Why the carry cannot reach a project directly

A pure project bond in yen would strap a currency mismatch onto an SPV whose revenue is
rupees — toll collections, PPA tariffs, transmission charges are all INR (the exceptions
with partial natural hedges are airports and ports with dollar-linked revenue streams).
An SPV has no treasury desk, no basis-swap access at fine pricing, and lenders know it.
So the market that actually exists routes the carry through three intermediated channels:

1. **The PSU-NBFC transformer** — REC, PFC, IREDA borrow offshore (hedged), on-lend INR
   to projects. The intermediary holds the FX risk management; the project sees only a
   rupee loan whose price embeds whatever spread advantage the offshore leg captured.
   This is where the EuroYen playbook's benefit lands on an actual solar park.
2. **The bank construction / bond take-out sequence** — banks carry construction risk
   (where cash flows don't yet exist and bonds are unsuitable); once the project is
   operational and cash flows are observable, bonds refinance the bank debt. The bond
   investor buys an operating annuity, not construction risk.
3. **The InvIT aggregator** — operating assets pooled into a trust that issues at scale
   with diversification, the listed version of the same take-out.

## 4. What changed in 2025-26: the domestic leg finally got plumbing

The binding constraint on project bonds was never demand in aggregate — it was that
insurance and pension money is largely confined to AA/AAA paper, while a single-project
SPV rates around A. The **Budget 2025-26 answered this directly**: a **Partial Credit
Enhancement facility at NaBFID** — a first-loss guarantee designed to lift infrastructure
bond ratings **from A to AA**, the exact threshold that unlocks insurer/pension demand
([Business Standard on the Budget announcement](https://www.business-standard.com/budget/news/budget-2025-nabfid-s-partial-credit-guarantee-to-boost-corporate-bond-mkt-125020101435_1.html)).

Current state, per reporting and ADB documentation:

- NaBFID targets PCE support for **4–5 projects raising about ₹15,000 crore in bonds in
  H2 FY2025-26**, predominantly **renewables and roads**
  ([Business Standard, Sep 2025](https://www.business-standard.com/industry/banking/nabfid-eyes-partial-credit-enhancement-for-bonds-worth-15-000-cr-in-h2fy26-125093001103_1.html)).
- ADB's **PACE-FIN** programme backs the facility with a **$500 million risk-sharing
  line, co-financed with the World Bank**
  ([ADB project 59474-001](https://www.adb.org/projects/59474-001/main)) — which is
  itself the carry channel in institutional form: multilateral hard-currency balance
  sheets absorbing tail risk so that *domestic* INR bonds can fund the project, no SPV
  currency mismatch anywhere.
- Practitioner caution is on record — RBI's earlier bank-PCE framework (2015) produced
  almost no issuance because capital treatment made enhancement uneconomic for banks;
  whether NaBFID's version prices workably is the open question
  ([Fox Mandal's analysis](https://foxmandal.in/pce-facility-for-infra-bonds-game-changer-or-pipe-dream/)).

## 5. The full machine, end to end

Put the two halves together and the financing chain for, say, a solar park reads:

```
Japanese insurer buys REC EuroYen at ~2%      (offshore leg: spread + investor base)
   → REC hedges, on-lends INR to the SPV      (carry transformed into credit)
      → bank/NBFC debt carries construction   (risk the bond market won't hold)
         → COD: cash flows become observable
            → NaBFID PCE lifts the take-out bond A → AA
               → Indian insurers/pension funds buy the bond
                  → bank capital recycles into the next project
```

Every leg is load-bearing: remove the hedge discipline and you have 2013's taper
casualties; remove the intermediary and the SPV wears FX risk it cannot manage; remove
the credit enhancement and the take-out bond can't reach the deepest domestic pool;
remove the take-out and bank balance sheets silt up with 25-year assets.

**The refined claim the evidence supports:** the carry trade helps finance Indian
projects not by making any project's debt cheaper directly, but by (a) widening the
funding base of the intermediaries that lend to projects, at spreads that survive
hedging (IREDA's <7% all-in is the existence proof), and (b) — via the multilateral
variant — putting hard-currency risk capacity behind the credit enhancement that lets
*domestic rupee* project bonds reach insurance and pension money. The currency risk is
held where it can be managed; the project gets rupees either way.

## 6. What this analysis does not establish

- **Hedge costs to the basis point** — forward-implied INR/JPY costs move daily; "roughly
  the rate differential" is the earlier piece's verified characterisation, not a quote.
- **Whether NaBFID's PCE will be taken up** — the ₹15,000 crore is a stated target, and
  the 2015 precedent failed on pricing; H2 FY26 issuance is the test.
- **On-lending spreads** — what REC/PFC/IREDA charge projects over their own cost is
  commercial and not decomposed here.
- **SPV-level foreign-currency project bonds** — asserted rare on structural grounds;
  no census of exceptions (airport/port issuers) was attempted.
- Any yield or rate not carried over from the blog's previously verified material or
  the cited reporting.
