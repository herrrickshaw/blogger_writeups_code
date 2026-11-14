Published 9 August 2026 · v1.0.0 · Ministry of Finance small-savings notification, Q2 FY2026-27

A stack of Indian rupee notes — the kind of principal sum the Rule of 72 lets you mentally project forward at a stated interest rate, like PPF's 7.1%. [Stack of indian rupee.jpg](https://commons.wikimedia.org/wiki/File:Stack_of_indian_rupee.jpg), Vinoth offl, CC BY-SA 4.0, via Wikimedia Commons.

72 ÷ rYears to double your money at annual rate r%, compounded annually

114 ÷ rYears to triple your money at rate r%

144 ÷ rYears to quadruple your money at rate r%

~10.1 yrsTime for a PPF deposit to double at today's 7.1% rate, per the Rule of 72

Read this before using any number in this article. The Rule of 72, 114 and 144 are all built for a single, one-time lump-sum investment left untouched to compound — you put in money once, at the start, and don't add to it. They do not apply, as-is, to a Systematic Investment Plan (SIP) or any other recurring/staggered investment, where money goes in periodically rather than all at once. A SIP earning the same headline rate will always take longer to double than this article's numbers suggest, because each later instalment has had less time to compound than the first one did — the correct tool for that case is the future-value-of-annuity formula, not the doubling-time formula this article covers. This distinction is repeated in more detail further down, but it is the single most common way these rules get misapplied, so it's stated here first.

[kept verbatim: dated update notes]

## Where 72 actually comes from

It's an approximation of a logarithm, chosen because it's easy to divide by.

Compound interest grows a sum by a fixed factor (1 + r) every period. Money doubles when (1 + r)n = 2, which means the exact number of years to double is n = ln(2) / ln(1 + r). For the interest rates most savings products actually pay — roughly 3% to 15% — ln(1 + r) is very close to r itself (in decimal form), and ln(2) ≈ 0.6931. So the exact formula collapses to approximately n ≈ 0.6931 / r, or 69.3 / r when r is expressed as a percentage. That's the real constant. It gets rounded up to 72 for one practical reason: 72 divides evenly by 2, 3, 4, 6, 8, 9 and 12, so “72 ÷ 8” or “72 ÷ 6” can be done in your head, while “69.3 ÷ 8” can't. The trade-off is a small, predictable bias — the Rule of 72 slightly overstates doubling time at low rates and slightly understates it at high rates, because 72 is bigger than 69.3.

Exhibit 1

Rule of 72 vs the exact compound-interest doubling time, by rate

Exact time uses n = ln(2) / ln(1 + r). Error is the Rule-of-72 estimate minus the exact figure.


[T1 "Where 72 actually comes from" 10 rows; use rows by number in a chart "table" spec]
  cols: c0 Annual rate, % | c1 Rule-of-72 estimate, years | c2 Exact doubling time, years | c3 Error, years
  r0: 3 | 24.00 | 23.45 | +0.55
  r1: 4 | 18.00 | 17.67 | +0.33
  r2: 6 | 12.00 | 11.90 | +0.10
  r3: 7.1 (PPF) | 10.14 | 10.11 | +0.04
  r4: 8 | 9.00 | 9.01 | −0.01
  r5: 10 | 7.20 | 7.27 | −0.07
  r6: 12 | 6.00 | 6.12 | −0.12
  r7: 15 | 4.80 | 4.96 | −0.16
  r8: 20 | 3.60 | 3.80 | −0.20
  r9: 30 | 2.40 | 2.64 | −0.24


Calculated directly from the compound-interest doubling formula n = ln(2)/ln(1+r). PPF rate of 7.1% per the Ministry of Finance's small-savings notification for Q2 FY2026-27 (July–September 2026), unchanged since April 2020 and retained for Q3 (October–December 2026).

Two things stand out. First, the Rule of 72 is remarkably accurate in exactly the band that matters for Indian savings products — PPF at 7.1%, most bank and post-office FDs, and typical debt-fund returns all sit between 6% and 9%, where the error is under a tenth of a year. Second, the error direction flips around 8%: below that, 72 overestimates how long doubling takes (so your money actually doubles slightly faster than the rule says); above it, 72 underestimates (your money takes slightly longer). At 20%+ — the range equity investors and get-rich-quick pitches like to quote — the rule is off by two to three months, which matters less for a rough gut-check but is worth knowing before you rely on it for a real projection.

## The Rule of 114 (tripling) and the Rule of 144 (quadrupling)

Same logic, different multiple — and a different rounding trade-off each time.

Tripling requires (1 + r)n = 3, and ln(3) ≈ 1.0986, so the exact continuous-compounding tripling-time constant is 109.9 — not simply rounded up to arrive at 114, the same way 72 itself isn't a simple rounding of the doubling constant 69.3. Both 72 and 114 are conventional constants nudged upward from their exact continuous-compounding values, chosen to stay accurate across the range of interest rates these rules actually get used at (roughly 4–15%) while keeping useful integer divisors (114 = 2 × 3 × 19). Quadrupling is the cleanest of the three mathematically, because ln(4) = 2 × ln(2) exactly — quadrupling your money is just doubling it twice, so unlike 72 and 114, the Rule of 144 constant isn't independently derived from a continuous-compounding constant at all: it's simply 2 × 72 = 144, making “144 ÷ r” the same as taking the Rule-of-72 doubling time and doubling it, which is both intuitive and exactly right (since doubling twice literally is quadrupling).

Exhibit 2

All three rules applied to the same set of rates

Years to reach each multiple, using the rounded constant divided by the rate.


[T2 "The Rule of 114 (tripling) and the Rule of 144 (quadrupling)" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Annual rate, % | c1 Double (72 ÷ r), years | c2 Triple (114 ÷ r), years | c3 Quadruple (144 ÷ r), years
  r0: 6 | 12.0 | 19.0 | 24.0
  r1: 7.1 | 10.1 | 16.1 | 20.3
  r2: 8 | 9.0 | 14.3 | 18.0
  r3: 10 | 7.2 | 11.4 | 14.4
  r4: 12 | 6.0 | 9.5 | 12.0
  r5: 15 | 4.8 | 7.6 | 9.6


All figures are rounded-constant approximations (72, 114, 144), not the exact logarithmic values; see Exhibit 1 for how closely the doubling column tracks the true figure at each rate.

## What these rules are actually for — and where they break

A mental sanity-check, not a substitute for the real formula.

The practical use is catching implausible claims fast. If a pitch says an investment “doubles your money in 4 years,” the Rule of 72 tells you instantly that it's implicitly promising an 18% annual compounded return (72 ÷ 4 = 18) — a real number you can then judge against what that asset class has actually delivered historically, rather than nodding along to “doubles in 4 years” as a vague good-sounding phrase. The same works in reverse: knowing PPF pays 7.1% lets you say, without a calculator, that a PPF deposit today roughly doubles by 2036 and roughly triples by the early 2040s — useful for a retirement napkin-sketch even though nobody actually holds one static deposit for 30 years.

Where the shortcut stops working. All three rules assume one constant, fully compounding annual rate applied to a single lump sum with no additions or withdrawals. They do not directly apply to a Systematic Investment Plan (SIP), where money goes in periodically rather than all at once — that needs the future-value-of-annuity formula, not the doubling-time formula, and will always take longer to double than a lump sum earning the same headline rate, because later instalments have less time to compound. They also say nothing about real (inflation-adjusted) growth: a 7.1% PPF return against ~5% inflation is really compounding your purchasing power at roughly 2.1%, which by the Rule of 72 takes about 34 years to double — not 10. And they assume the rate stays constant, which is fine for a fixed-rate instrument like PPF but not for equity, where the same 12% CAGR quoted over 10 years might have been earned through several down years and a few sharp up years, not a smooth 12% every single year.

The formula underneath all of this, for anyone who wants the exact answer rather than the shortcut, is straightforward: Final amount = Principal × (1 + r)n, where r is the annual rate as a decimal and n is the number of years. Rearranged to solve for time, n = ln(multiple) / ln(1 + r) — the same formula Exhibit 1's “exact” column uses for doubling (multiple = 2), and it works identically for any target multiple by swapping in ln(3) for tripling or ln(10) for a tenfold increase. A calculator with a natural-log function reproduces every number in this article; the Rule of 72/114/144 exist purely so you don't need one at the moment someone is pitching you a return.

[kept verbatim, collapsed: What this piece could not establish]

Sources. The compound-interest doubling/tripling/quadrupling formulas and their logarithmic derivations (Exhibits 1 and 2) are standard financial mathematics, calculated directly for this article using n = ln(multiple)/ln(1+r); no external claim is being cited for the mathematics itself. PPF interest rate of 7.1% for Q2 FY2026-27 (July–September 2026), unchanged since April 2020 — Ministry of Finance (Department of Economic Affairs) notification on small savings scheme interest rates, announced 30 June 2026, as reported contemporaneously by financial press; this article did not independently locate and read the notification's own gazette text and relies on that contemporaneous reporting for the rate figure and effective dates. Rates retained for Q3 FY2026-27 (October–December 2026) per the memorandum of 30 September 2026, as reported by [Business Today](https://www.businesstoday.in/personal-finance/story/small-savings-scheme-interest-rates-unchanged-for-q3-fy27-check-ppf-scss-ssy-rates-558892-2026-09-30).

Related on this blog: [The 50/30/20 Rule — and the Case for Flipping It to Save First](https://blog.vertistratsolution.com/2026/08/the-503020-rule-is-elizabeth-warrens.html) — another personal-finance rule of thumb (50/30/20 budgeting) put through the same check-the-arithmetic treatment.

## What would fix this

[kept verbatim, open: What would fix this; 3 items]
