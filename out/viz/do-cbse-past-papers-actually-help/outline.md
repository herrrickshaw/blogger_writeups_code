Revised
10 November 2026
· v1.2.0 · [what changed](#changelog)

1,955CBSE Class-XII papers parsed, 2022–2026

49%of Accountancy's high-mark marks sit on a recurring topic

0%of English Core's high-mark marks do

10/10sample-paper sessions, 2015-16–2024-25, testing Physics's “electric field”

"Solve the last five years' papers" is close to universal advice from CBSE coaching material. It is also, on the evidence, true for some subjects and nearly meaningless for others. A parse of 1,955 Class-XII question papers from cbse.gov.in (2022–2026, main and compartment sittings, 30,734 questions extracted) can measure this directly: for each subject, what share of the high-mark (≥4-mark) marks sit on a topic — a 2–4-word phrase — that recurs across at least three of the five exam years. Call it the repetition index.

[kept verbatim: dated update notes]

## The repetition index, by subject

The split does not track how big a subject's syllabus is. It tracks how formulaic its questions are — and that is a very different sort by subject than most study advice assumes:


[T1 "The repetition index, by subject" 11 rows; use rows by number in a chart "table" spec]
  cols: c0 Subject | c1 Papers | c2 High-mark Qs | c3 Repetition index, %
  r0: Accountancy | 50 | 109 | 49
  r1: Physics | 64 | 120 | 44
  r2: Economics | 61 | 173 | 38
  r3: Mathematics | 62 | 90 | 22
  r4: Business Studies | 54 | 119 | 16
  r5: History | 67 | 167 | 16
  r6: Geography | 60 | 229 | 14
  r7: Political Science | 60 | 200 | 7
  r8: Chemistry | 72 | 133 | 5
  r9: Biology | 62 | 169 | 5
  r10: English Core | 72 | 259 | 0


[chart: 
 
 Repetition index by subject (2022–2026 corpus) 
 
 Accountancy 49% 
 Physics 44% 
 Economics 38% 
 Mathematics 22% 
 Business Studies 16% 
 History 16% 
 Geography 14% 
 Political Science 7% 
 Chemistry 5% 
 Biology 5% 
 English Core 0% 
 
 Share of ≥4-mark marks sitting on a phrase recurring in ≥3 of 5 exam years (2022–2026). 
]

Repetition is a subject property, not a syllabus-size property — Physics and English Core have similar syllabus scope but sit at opposite ends of the index.

Read this as lexical repetition, not conceptual repetition. The index measures repeated wording, mined as 2–4-word phrases, not repeated ideas. Chemistry and Biology score 5% not because the board tests wildly different concepts each year, but because their questions describe the same chemistry in differently-worded ways (“calculate emf of the following cell…” vs “consider the following standard electrode potential values…” is one topic, two phrasings). English Core scoring 0% is correct by design — its long-answer questions quote unseen passages, which never repeat.

## What actually recurs, and where

Accountancy is the most repetitive paper in the corpus. Two topics alone — admission/retirement of a partner (14 papers across 2023/25/26, 139 marks) and the balance sheet incl. Common Size Balance Sheet (20 papers across 2024/25/26, 139 marks) — plus profit-sharing-ratio changes, cash flow from investing activities, and dissolution of the firm make up most of the high-mark paper, year after year.

Physics has exactly two topics that recur at high marks in 4 of the 5 years, across the entire 11-subject corpus: electric field (14 papers, 84 marks) and magnetic field (11 papers, 73 marks). Parallel-plate capacitors and refractive index follow at 3-of-5 years. No other subject has a single content topic that reliable.

Economics leans on a recurring numerical format — the “for a hypothetical economy, it is known that…” problem appears in 14 papers worth 133 marks — plus aggregate demand, commercial banks/RBI, and gross value added. History circles a small set of sourced narratives (Vijayanagara Empire, Quit India Movement, Salt Satyagraha, Bombay Deccan riots) even though its index reads a modest 16%, because those set-pieces sit specifically in the 8-mark long-answer slot. Business Studies reuses “functions of management” (planning, directing) almost verbatim across three straight years.

## A separate finding: the same skill-subject block, six times over

Away from topic recurrence, the corpus's structural analysis turns up a more actionable pattern for students taking any of CBSE's Skill Education electives (Artificial Intelligence, Information Technology, Web Applications, Taxation, Financial Markets Management, Typography & Computer Applications). Every one of these papers devotes roughly 10 of its 50–60 marks — 17–20% — to an identical five-unit Employability Skills block: communication, self-management, ICT basics, entrepreneurship, and green skills. The wording repeats near-verbatim across subjects — the same active-listening question appears in both the Taxation and Web Applications papers; the same “Ctrl+M adds a slide” item appears in both AI and Typography.

The single highest-leverage move for a Skill Education student is this block, not the subject content. It is graded, worth a fixed ~10 marks, and identical across whichever of the six papers a student sits — unlike any subject-specific topic, which recurs at best 3 years out of 5.

## Does this hold over more years? Ten years of official sample papers say: mostly, yes

The repetition index above is built on five years of administered exam papers (2022–2026) — cbse.gov.in itself does not publish real Class-XII papers from earlier sessions in a form this analysis could fetch. But CBSE separately publishes an official Sample Question Paper (SQP) before each session, illustrating that year's format and a slice of its content, going back to 2015-16. Searching that decade-long SQP archive for the specific topics already found recurring in the real-paper analysis gives an independent, longer-run check on the same claim:


[T2 "Does this hold over more years? Ten years of official sample papers sa" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Subject · topic | c1 SQP sessions with the subject | c2 Sessions where the topic appears
  r0: Physics · “electric field” | 10 (2015-16 to 2024-25) | 10 of 10
  r1: Physics · “magnetic field” | 10 (2015-16 to 2024-25) | 10 of 10
  r2: Economics · “aggregate demand” | 10 (2015-16 to 2024-25) | 10 of 10
  r3: Accountancy · “balance sheet” | 7 (2018-19 to 2024-25) | 7 of 7
  r4: Accountancy · partner admission/retirement | 7 (2018-19 to 2024-25) | 2 of 7


Physics's two field topics and Economics's “aggregate demand” check out in every single sample paper CBSE has released in the last decade — a far stronger confirmation than the original 4-of-5-years finding, and evidence that this isn't a quirk of the 2022–2026 window. Accountancy's broad “balance sheet” topic is equally universal. But the specific partnership-admission/retirement cycle that dominates Accountancy's high-mark real-exam questions (14 of 20 papers across three exam years) shows up in only 2 of 7 sample papers.

Why the Accountancy result diverges, and why that's not a contradiction. A Sample Question Paper is one illustrative paper per session; the real-exam repetition index is built from an entire exam year's worth of papers — multiple sets and sittings, including compartment exams. A topic can recur reliably across a whole year's real papers without appearing in the single SQP that year, simply because the SQP is a smaller sample of the same syllabus, not a shrunk copy of the full exam. This divergence is a fact about SQPs' sampling method, not a reason to doubt the original real-paper finding — and it is exactly the kind of check that could have gone the other way; it didn't for Physics or Economics, which is why those two results are reported as a genuine strengthening. CBSE did not publish an Accountancy SQP for 2015-16 through 2017-18 in this corpus, so that subject's window is 7 years, not 10.

## What would break this analysis

Method caveats, stated plainly. (1) Topics were mined automatically as recurring n-grams, not hand-picked, so the conclusion isn't smuggled in by a curated list — but recurrence is counted in exam years, not papers, because papers within one sitting overlap roughly 75% and would otherwise manufacture false recurrence. (2) Hindi-medium text extracts as mojibake in this corpus (embedded-font code-point mapping), so only the English-medium ~54% of parsed questions could be analysed; the index does not cover Hindi-medium-specific patterns. (3) Marks for most of the 2022–2026 archive were parsed heuristically from paper text rather than reconciled against each paper's own instructions (only a 32-paper 2024-25 subset was exactly reconciled) — treat every index value as accurate to a few percentage points, not exact.

## The takeaway

"Practise past papers" is not one piece of advice; it's eleven, and they don't agree. For Accountancy and Physics students, five years of past papers genuinely rehearse a large share of what will be asked again — and for Physics and Economics specifically, a decade of official sample papers backs that up further still. For English Core, Biology, and Chemistry students, the same advice mostly teaches format and timing, not content, because those subjects are built not to repeat. And for anyone taking a Skill Education elective, the highest-certainty ten marks in the entire paper are a shared syllabus block that has nothing to do with the subject's name.

## Use the tool yourself
Note, 11 November 2026: the CBSE_paper_patterns repository has since been made private, so the clone commands below no longer work for readers. The figures in this post are unchanged.

The analysis comes from the CBSE_paper_patterns repository. You do not need to rebuild the corpus to check the figures: the repository ships the derived tables in data/, and reading them needs only Python’s standard library. A [video walkthrough](https://youtu.be/PnWtmpgs4Hg) shows the same steps.

git clone --depth 1 https://github.com/herrrickshaw/CBSE_paper_patterns.git
cd CBSE_paper_patterns

# the repetition index by subject (subject, papers, index %)
python3 -I -c "import csv;[print(r['subject'],r['papers'],round(float(r['repetition_index'])*100)) for r in csv.DictReader(open('data/subject_repetition.csv'))]"

# the recurring content topics for one subject (phrase, years, papers, marks)
python3 -I -c "import csv,sys;[print(r['phrase'],r['year_list'],r['papers'],r['marks']) for r in csv.DictReader(open('data/recurring_topics.csv')) if r['subject']==sys.argv[1] and r['kind']=='content_topic']" Physics
The first command prints the eleven subjects with the index in the table above (Accountancy 49, Physics 44 and so on). The second, for Physics, starts with electric field (2023 to 2026, 14 papers, 84 marks) and magnetic field (11 papers, 73 marks). Swap Physics for any subject. The repository also holds question_type_mix.csv, paper_structures.csv and syllabus_vs_actual.csv for anyone who wants to go further, and the analysis notes explain three traps for parsing CBSE PDFs: reprinted options, Hindi-medium text that extracts as mojibake, and exam sets counted as separate papers.

Two limits on reuse. The repetition pattern is descriptive: revise the whole syllabus, and do not use it to skip topics or to predict next year’s paper. And the question papers remain CBSE’s copyright; check CBSE’s terms before reusing any question text the repository carries. The clone is about 246 MB because it includes the corpus; rebuilding that corpus from scratch needs a 6 GB download and macOS OCR, and was not run for this post.

Sources: 1,955 CBSE Class-XII question papers, main and compartment sittings, downloaded directly from cbse.gov.in/cbsenew/question-paper.html, academic years 2022–2026; 30,734 questions parsed (16,633 usable English-medium text), extracted with pdftotext -layout and mined for 2–4-word recurring phrases (n-grams appearing in ≥3 of 5 exam years, boilerplate stripped). Paper-architecture detail (Employability Skills block, section structure) from a separately reconciled 32-paper 2024-25 subset whose marks were checked against each paper's own General Instructions. The ten-year extension uses CBSE's own Sample Question Paper archive (cbseacademic.nic.in, sessions 2015-16 to 2024-25, sourced from this account's corpus), searched directly for the phrases already found recurring in the real-paper analysis — a targeted presence check, not an independent re-mining of the SQP text. cbse.gov.in and cbseacademic.nic.in could not be fetched directly from this piece's research environment for anything beyond what the underlying repository already held; no post-2024-25 SQP or pre-2022 real exam paper is claimed here that was not already in that corpus. Full analysis, methodology and the underlying DuckDB tables are documented in this account's own CBSE_paper_patterns research repository; the “Use the tool yourself” commands were run against its data/subject_repetition.csv and data/recurring_topics.csv on 10 November 2026.

Revision history.

- v1.2.0 — 10 November 2026 — added “Use the tool yourself”: how to check the repetition index and recurring topics from the open-source repository, merged in from a separate how-to post that has been retired.

- v1.1.0 — 17 September 2026 — added a ten-year (2015-16–2024-25) extension using CBSE's official Sample Question Paper archive, confirming the electric-field/magnetic-field and aggregate-demand findings hold in every sample paper released in the last decade, and finding a genuine divergence on Accountancy's partnership-cycle topic.

- v1.0.0 — 17 September 2026 — first published.

Related on this blog: [Thirty-One Years of Asking Parliament the Same Question About Fertiliser](https://blog.vertistratsolution.com/2026/08/thirty-one-years-of-asking-parliament.html) — another piece built the same way — read years of one specific document type end to end to find what's actually constant versus what changed.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
