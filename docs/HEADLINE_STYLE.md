# Headline style: plain reference

Adopted 14 November 2026 for every article title (the Blogger title and the `<h1>` in the body)
and for section headings (`<h2>`) in new posts.

**The tone is a statistics bulletin or a wire service, not a columnist.** A title says what the
piece is about and what the data shows. It does not argue, tease or scold. Readers arrive from
search and from the translate widget (15 Indian languages), so a title has to survive machine
translation word for word.

## The pattern

    Subject: what the data shows[, period or place]

- *Subject* first: the thing the piece is about, usually starting with *India* or the named
  scheme, sector, company or state.
- After the colon: the main finding, with **one** key number, its unit and its period.
- One sentence. At most one colon. No full stops inside the title.

## Rules

1. **Length:** aim for 55 to 80 characters; never more than 90. (Google shows about 60;
   translations run 20 to 40% longer than English.)
2. **Sentence case:** capital letter only at the start and for proper nouns and acronyms.
   `India's wind power: 57 GW installed, under a tenth of the onshore potential`.
3. **Plain words, no idioms:** no puns, metaphors, film or TV references, or wordplay
   (*third claimant*, *winter is coming*, *thali investing*, *the barrel really is shifting*).
   If a literal translation would confuse, rewrite it.
4. **State, don't tease:** no rhetorical questions, no cliff-hanger second sentence, no
   *nobody*, *actually*, *just*, *still*, *only*, *finally*, *anyway*, *really*, *the real*,
   *what X won't tell you*. Lead with what is true, not with what is wrong.
5. **No negation-led framing:** *X isn't why Y* becomes *Y: the main cause is X*.
   A shortfall is stated as a measured fact: *Seabed mineral auction: no winning bid in the first round*.
6. **Numbers as digits with units:** `Rs 33,660 crore`, `57 GW`, `9.3:3.5:1`, `FY26`, `2026`.
   Use the number from the piece; never round it into a different claim.
7. **Abbreviations:** keep ones Indian readers search for (GST, GDP, CPI, WPI, RBI, SEBI, PLI,
   UPI, FDI, LNG, CNG, EV, MSP, FCI, EPR, GW, MW). Expand the rest, or name the thing in words
   (*Directorate General of Hydrocarbons* or *oil and gas exploration blocks*, not *DGH OALP*).
8. **No second person, no first person:** no *you*, *your*, *we*.
9. **Tool guides keep their pattern:** `How to use <tool>: <what it does>`, under 90 characters.
10. **Facts only from the piece:** a retitle may drop detail but must not add a claim,
    a number or a comparison that the post does not make.

## Examples

| Before | After |
|---|---|
| The Diesel Truck Isn't Why Your Eggs Cost More. The Ethanol Tank Is. | Egg prices in India: maize demand for ethanol raises feed costs more than diesel |
| Sugarcane's Third Claimant: What's Actually Being Fermented Into India's First PLA Plant | India's first PLA bioplastic plant: the sugar feedstock it ferments |
| India Has Funded 3 Lakh Machines to Stop Stubble Burning. About 4,500 of Them Collect Straw | Crop residue machines in India: 3 lakh subsidised, about 4,500 collect straw |
| Green Energy Corridor III Is 15 Times the Last Phase. The First Two Are Still Not Finished | Green Energy Corridor III: 15 times the size of phase II, with phases I and II incomplete |
| 57.4 GW and Counting: India's Wind Fleet, State by State, Against What NIWE Says Is Actually There | India's wind power by state: 57.4 GW installed, under a tenth of the potential |

## Section headings (`<h2>`) in new posts

The same tone: a short statement of what the section shows (*Exports fell 12% in 2025-26*),
or a plain label (*Sources and caveats*). No questions, no teasers, no idioms. The two fixed
house sections keep their names: *What would fix this* and *What this piece could not establish*.

## What changes when a title changes

The post address (slug) never changes, so links and search rankings carry over. Retitling
updates the Blogger title and the `<h1>` in the body; the article index picks the new title up
on its next rebuild (`out/gsc_index/rebuild_index.py`).
