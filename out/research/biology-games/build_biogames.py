import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-biology-games.html'

# ASER 2024 (rural, age 14-16): smartphone access and use
ASER_HOME, ASER_CANUSE, ASER_OWN, ASER_EDU, ASER_BRING = 89.1, 82.2, 31.4, 57, 65.9
# Share of all 14-16-year-olds who own a phone = can use x own-of-users
OWN_ALL = ASER_CANUSE * ASER_OWN / 100
assert round(OWN_ALL) == 26

def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

# Syllabus fit: 2 = good fit, 1 = partial, 0 = none
FIT = [
    ("Class 8", "Curiosity, Ch 2", 1, 0),
    ("Class 9", "Exploration, Ch 2 & 12", 2, 1),
    ("Class 10", "Heredity (no evolution)", 0, 0),
    ("Class 11", "Ch 8 Cell; Ch 10 division", 2, 0),
    ("Class 12", "Evolution", 0, 1),
    ("NEET-UG", "Units 3 and 7", 2, 1),
]

def fit_svg():
    W, top, row = 360, 58, 46
    H = top + row * len(FIT) + 34
    INK, MUTED, LINE, FILL = '#222', '#555', '#8a8a8a', '#2f6f9f'
    cx = (238, 316)
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="bgT" style="width:100%;max-width:420px;height:auto;display:block;margin:0 auto;font-family:-apple-system,\'Segoe UI\',sans-serif">',
         '<title id="bgT">Where each resource fits the NCERT syllabus, Class 8 to NEET: the cell games fit Classes 9 and 11 and NEET, the evolution game fits only partly, and Class 10 has no anchor for either</title>',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{cx[0]}" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="{INK}">BioMan</text>',
         f'<text x="{cx[0]}" y="38" text-anchor="middle" font-size="12" fill="{MUTED}">Cells</text>',
         f'<text x="{cx[1]}" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="{INK}">Cell to</text>',
         f'<text x="{cx[1]}" y="38" text-anchor="middle" font-size="12" fill="{MUTED}">Singularity</text>']
    for i, (cls, ch, a, b) in enumerate(FIT):
        y = top + i * row
        s.append(f'<line x1="8" y1="{y - 8}" x2="{W - 8}" y2="{y - 8}" stroke="#ddd"/>')
        s.append(f'<text x="8" y="{y + 12}" font-size="15" font-weight="700" fill="{INK}">{cls}</text>')
        s.append(f'<text x="8" y="{y + 29}" font-size="12" fill="{MUTED}">{ch}</text>')
        for x, v in zip(cx, (a, b)):
            if v == 2:
                s.append(f'<circle cx="{x}" cy="{y + 14}" r="11" fill="{FILL}"/>')
            elif v == 1:
                s.append(f'<circle cx="{x}" cy="{y + 14}" r="11" fill="#fff" stroke="{FILL}" stroke-width="2.5"/>')
                s.append(f'<path d="M{x} {y + 3} A11 11 0 0 1 {x} {y + 25} Z" fill="{FILL}"/>')
            else:
                s.append(f'<line x1="{x - 9}" y1="{y + 14}" x2="{x + 9}" y2="{y + 14}" stroke="{LINE}" stroke-width="2.5"/>')
    ly = top + row * len(FIT) + 10
    s.append(f'<circle cx="16" cy="{ly}" r="7" fill="{FILL}"/><text x="28" y="{ly + 5}" font-size="12" fill="{INK}">good fit</text>')
    s.append(f'<circle cx="104" cy="{ly}" r="7" fill="#fff" stroke="{FILL}" stroke-width="2"/><path d="M104 {ly - 7} A7 7 0 0 1 104 {ly + 7} Z" fill="{FILL}"/><text x="116" y="{ly + 5}" font-size="12" fill="{INK}">partial</text>')
    s.append(f'<line x1="180" y1="{ly}" x2="194" y2="{ly}" stroke="{LINE}" stroke-width="2.5"/><text x="202" y="{ly + 5}" font-size="12" fill="{INK}">no chapter to anchor it</text>')
    s.append('</svg>')
    return ('<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) +
            '<figcaption class="gb-note" style="margin-top:.5rem">This blog&rsquo;s reading of chapter content against what each resource covers. '
            'Class 9 is the new <i>Exploration</i> textbook (2026-27); Class 10 and 11 are the existing books, in use until new ones arrive in 2027-28.</figcaption></figure>')

stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>3 + quizzes</b><span>activities on BioMan Biology&rsquo;s free Cells page: an osmosis video and game, an organelle game and a cell-membrane game</span></div>
<div class="gb-stat"><b>1 crore+</b><span>Google Play downloads of Cell to Singularity, which carries ads and in-app purchases</span></div>
<div class="gb-stat"><b>{ASER_HOME}%</b><span>of rural 14&ndash;16-year-olds have a smartphone at home, but only about {OWN_ALL:.0f}% own one (ASER 2024)</span></div>
<div class="gb-stat"><b>Class 10</b><span>is where the word &ldquo;evolution&rdquo; left the NCERT science book: the chapter is now just &ldquo;Heredity&rdquo;</span></div>
</div>'''

T_COMPARE = table(
    ["", "BioMan Biology: Cells", "Cell to Singularity"],
    [
        ("What it is", "Browser games and a quiz set, made by a biology teacher", "Idle &ldquo;clicker&rdquo; game about the history of life, by Computer Lunch, New York"),
        ("Cost", "Free with ads; ad-free licence US$49 a year per teacher", "Free; in-app purchases"),
        ("Ads", "Display ads on the free site", "Opt-in rewarded ads, per the developer"),
        ("Device", "Any modern browser (HTML5); phone fit not tested here", "Android, iOS, Windows, Mac, browser"),
        ("Offline", "No; needs a connection", "Listed as playable offline"),
        ("Language", "English", "English, Hindi and 17 others"),
        ("Sign-up", "None for students", "None; cloud save optional"),
        ("Best fit", "Class 9 Ch 2; Class 11 Ch 8; NEET Unit 3", "Class 12 Evolution, as a timeline only"),
    ])

T_GAMES = table(
    ["Activity", "What it teaches", "NCERT link"],
    [
        ("Osmosis Interactive and Video", "Hypertonic, hypotonic and isotonic solutions; three filmed experiments", "Class 9 Ch 2 (osmosis); Class 11 Ch 8"),
        ("Cell Explorer: The Animal Cell", "Nucleus, ribosomes, ER, Golgi, lysosomes and other organelles", "Class 9 Ch 2; Class 11 Ch 8"),
        ("Cell Defense: The Plasma Membrane", "Membrane lipids and proteins; diffusion, active transport, osmosis", "Class 9 Ch 2; Class 11 Ch 8"),
        ("Cells quizzes", "Self-test; scores can be sent to a registered teacher", "Revision"),
    ])

body = f"""
{stats}

<p>Two free resources keep turning up when parents and students look for biology on a screen. One is the <a href="https://biomanbio.com/HTML5GamesandLabs/Cellgames/Cells.html">Cells page of BioMan Biology</a>, a set of browser games built by a biology teacher for their own classes and written to US state and national standards. The other is <a href="https://play.google.com/store/apps/details?id=com.computerlunch.evolution&amp;hl=en_IN">Cell to Singularity</a>, a mobile game in which you tap your way from the first cell to humans and beyond, and which has passed one crore downloads on Google Play. This piece asks a narrow question: what does each actually teach, and where does it fit in the Indian school syllabus, which has just changed again?</p>

<p>The short answer: the cell games line up closely with NCERT&rsquo;s new Class 9 chapter on the cell and with Class 11, and are worth a teacher&rsquo;s time. The evolution game is a good timeline of life and a poor teacher of how evolution works, and in the NCERT sequence it has almost nothing to attach to until Class 12, because evolution was cut from the Class 10 book.</p>

<h2 class="gb-h2">BioMan Biology&rsquo;s Cells page: three games and a quiz</h2>

<p>BioMan Biology describes itself as standards-based and &ldquo;designed by a teacher&rdquo;: its author says they have taught AP Biology, IB Biology and general science and built the site for their own students. All of it is free. The free site carries advertising; teachers can buy an ad-free licence for US$49 a year (US$149 for up to five teachers). Students do not register. A teacher who registers can collect quiz scores, and students can save progress to the cloud only by entering a registered teacher&rsquo;s email address. The site is in English.</p>

{T_GAMES}

<p>The fit with NCERT is close. The new Class 9 science book, <i>Exploration</i>, first published in April 2026, opens its biology with Chapter 2, &ldquo;Cell: The Building Block of Life&rdquo;. NCERT&rsquo;s draft syllabus for that chapter lists the structure and function of key organelles, the permeability of cell membranes, and demonstrating osmosis in cells. Class 11&rsquo;s &ldquo;Cell: The Unit of Life&rdquo; goes deeper into the endomembrane system that Cell Explorer is built around, and the NEET-UG 2026 syllabus repeats it almost word for word in its Unit 3, &ldquo;Cell Structure and Function&rdquo;. At Class 8, where the new <i>Curiosity</i> textbook introduces the cell in Chapter 2, &ldquo;The Invisible Living World: Beyond Our Naked Eye&rdquo;, the games are more detail than the chapter needs, but the osmosis video works at that level.</p>

<p>Two gaps matter. Cell Explorer is an animal cell only, while NCERT asks students to compare plant and animal cells; the cell wall, chloroplasts and the large central vacuole are in the text, not the game. And cell division, which Class 11 covers in its Chapter 10, &ldquo;Cell Cycle and Cell Division&rdquo;, is not on the Cells page; BioMan files mitosis and meiosis under its separate genetics section, which this piece did not review.</p>

<h2 class="gb-h2">Cell to Singularity: a timeline of life you tap through</h2>

<p>Cell to Singularity is made by Computer Lunch, a small New York studio founded by Andrew Garrahan and Kati Nawrocki. It went into early access on Google Play in 2018, launched fully on iOS in August 2019 and on Android in April 2020, and left early access on Steam in November 2021. It added a dinosaur expansion, Mesozoic Valley, in 2019, and a space expansion, the Beyond, in 2021. On the Indian Play Store it shows more than one crore downloads and a 4.6-star rating, is rated for ages 3 and up, and lists both ads and in-app purchases; the developer&rsquo;s press kit says ads are shown only when a player chooses to watch one for a reward. It is available in Hindi among 18 other languages, and the Play Store lists it as playable offline.</p>

<p>The game is an idle clicker. Tapping earns &ldquo;entropy&rdquo;, which buys the next step in the history of life: amino acids, the first cell, mitochondria, the nucleus, multicellular life, fish, reptiles, mammals, primates and humans; then &ldquo;ideas&rdquo;, which buy fire, farming, the Industrial Revolution and, eventually, Mars and machine intelligence. Each upgrade comes with a short factual note, and reviewers have praised it for exactly that. As a picture of deep time, of how long single cells had the planet to themselves and how late mammals and humans arrive, it does something a textbook page struggles to.</p>

<p>The problem is the mechanism. In the game, the player chooses each step and pays for it, and the story heads towards humans and then a technological &ldquo;singularity&rdquo;. That is close to the misconception biology teachers spend most effort undoing: that evolution is a ladder of progress with a goal, or that features appear because something needed them. Education researchers call this teleological or &ldquo;design&rdquo; thinking. A 2024 study of introductory university biology students found that more than a fifth defined evolution as progress towards something better; the evolution-education researcher Kostas Kampourakis argues that the real obstacle is the intuition that someone or something designed the outcome. A game in which the player literally designs the outcome sits squarely on that intuition. Natural selection, variation, drift and extinction as the normal fate of most lineages, the content of NCERT&rsquo;s Class 12 chapter and NEET&rsquo;s Unit 7, barely appear. The developer told an interviewer in 2018 that the evolutionary tree was mapped through &ldquo;a lot of Wikipedia research&rdquo; and help from scientist friends; its store page calls it &ldquo;the most accurate human evolution game on Earth&rdquo;, a claim nobody appears to have tested.</p>

<h2 class="gb-h2">Where they fit, class by class</h2>

{fit_svg()}

<p>The gap in the middle is a curriculum decision, not a feature of either game. In NCERT&rsquo;s textbook rationalisation of 2022-23, the Class 10 chapter &ldquo;Heredity and Evolution&rdquo; became &ldquo;Heredity&rdquo; and the word &ldquo;evolution&rdquo; left the Class 9 and 10 science books. Asked about it in the Rajya Sabha in December 2025, the education ministry said Darwin&rsquo;s theory remains part of the school science curriculum as a continuum and that the cuts were made to reduce curriculum load. In practice a CBSE student meets evolution properly in Class 12, in a full chapter, and in NEET. The new Class 9 book does have a chapter on diversity and classification, &ldquo;Patterns in Life&rdquo;, where the game&rsquo;s branching history of animals is a reasonable companion. The new Class 10 book is due in 2027-28; until then, Cell to Singularity is something a curious student plays, not something a teacher can set.</p>

<h2 class="gb-h2">Side by side</h2>

{T_COMPARE}

<h2 class="gb-h2">Will they run on the phones Indian students have?</h2>

<p>Most will play on a shared phone. ASER 2024, the household survey run by Pratham, found that 89.1% of rural 14&ndash;16-year-olds have a smartphone at home and 82.2% can use one, but only 31.4% of those who can use one own it; 57% had used a phone for something educational in the week before the survey, against 76% for social media. On the survey day, 65.9% could actually bring a phone to do the survey&rsquo;s tasks.</p>

<p>That favours short sessions on a borrowed phone. BioMan&rsquo;s games are browser games that need a connection while you play and were built for classroom use; this piece could not test them on a low-end Android phone. Cell to Singularity is a large download (more than 500 MB on Apple&rsquo;s store; Google Play does not show a size), but once installed it is listed as playable offline, and it is an idle game: progress builds up while the phone is doing something else. That is good for a family phone and bad for homework, because idle games are built to keep players coming back for weeks; Play Store reviewers who love it also complain about the length of its reward ads.</p>

<h2 class="gb-h2">How to use them</h2>
<ul>
<li><b>Class 9, Chapter 2.</b> Start with the hands-on osmosis demonstration the syllabus asks for, then the BioMan osmosis video and game, then Cell Defense for membrane transport. Use Cell Explorer for organelles, and then have students list what a plant cell has that the game&rsquo;s animal cell does not.</li>
<li><b>Class 11 and NEET revision.</b> Cell Explorer and Cell Defense map onto Chapter 8 and NEET Unit 3 closely enough to use as timed revision; the BioMan quizzes give instant feedback.</li>
<li><b>Cell to Singularity as a timeline, with a correction.</b> Let students play it for the sequence of life, then ask them to redraw its path as a branching tree with dead ends, and to say what, in real evolution, did the &ldquo;buying&rdquo;. Class 12 students can match each upgrade to the evidence their chapter lists: fossils, comparative anatomy, molecular evidence.</li>
<li><b>Keep the textbook in front.</b> Neither resource replaces the NCERT text; the e-content and QR-linked material on DIKSHA, the government&rsquo;s school-content platform, is the natural next stop for Indian-language support.</li>
</ul>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li><b>NCERT and DIKSHA could publish a short, vetted list of free external simulations mapped to chapters</b>, starting with the new Class 9 cell chapter, and say for each one what it gets wrong. Teachers are using these resources anyway.</li>
<li><b>DIKSHA could commission cell and membrane games of its own that run offline and in Indian languages</b>, so a student on a shared phone with patchy data does not depend on a US site&rsquo;s browser games.</li>
<li><b>When the new Class 10 science book arrives in 2027-28, NCERT could state plainly where evolution sits</b> between Class 9&rsquo;s diversity chapter and Class 12, so that students do not go from Class 8 to Class 12 without the idea.</li>
<li><b>Teachers using Cell to Singularity could pair it with one explicit lesson on why evolution has no goal</b>; the research on teleological thinking suggests the misconception is sticky enough to need naming, not just correcting.</li>
</ul>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>Neither resource&rsquo;s game files could be loaded from the machine used to research this piece, so the games were not played or tested on phones here; descriptions come from their own pages, store listings and reviews. No study was found measuring what Indian students learn from either. Google Play&rsquo;s rating and age band for Cell to Singularity differ by country (4.6 stars and &ldquo;3+&rdquo; on the Indian store; 4.5 and &ldquo;Everyone 10+&rdquo; on the US store), and its Android download size and data use were not found. BioMan Biology does not name its author on the pages read. The chapter fit in the chart is this blog&rsquo;s judgement, and the Class 10 and 11 books will change in 2027-28.</p>
"""

sources = ("BioMan Biology: Cells page, game pages (Cell Explorer, Cell Defense), Teachers page, Help/FAQs and ad-free licence page (biomanbio.com, read November 2026). "
           "Cell to Singularity: Google Play listing (Indian and US stores, November 2026); Apple App Store listings; developer press kit (celltosingularity.com/press); "
           "Steam store page (release dates); Wikipedia entry for release history; TechRaptor interview with Andrew Garrahan (20 November 2018); Google for Publishers profile of Computer Lunch. "
           "NCERT: <i>Curiosity</i> (Grade 8) contents; <i>Exploration</i> (Grade 9, 2026-27) chapter list via textbook distributors; draft Grade 9 science syllabus (ncert.nic.in); Class 11 Biology Chapters 8 and 10 (Reprint 2026-27); NCERT advisory of 17 March 2026 on the rollout of new Grade 9&ndash;11 books. "
           "Rajya Sabha Unstarred Question 1139 (10 December 2025) on evolution in Classes 9 and 10; The News Minute (3 August 2025); Times of India (13 June 2023) on the Class 12 evolution chapter. "
           "NEET-UG 2026 syllabus (National Medical Commission, December 2025). ASER 2024 national findings (Pratham/ASER Centre, January 2025). "
           "Evolution education: Werth (2012), <i>Evolution: Education and Outreach</i>; Kampourakis (2020), same journal; a 2024 study of introductory biology students&rsquo; definitions of evolution, same journal. "
           "Chapter mapping and the phone-ownership arithmetic ({:.1f}% &times; {:.1f}%) are this blog&rsquo;s (builder at out/research/biology-games/).").format(ASER_CANUSE, ASER_OWN)

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/ai-is-not-taking-indias-offshore-work.html", "AI Is Not Taking India&rsquo;s Offshore Work Evenly: A Sector-by-Sector Check, and the Government Backlogs the Same Skills Could Clear"),
]

build("Education · 4 November 2026",
      "A Free Cell Game Fits India&rsquo;s New Class 9 Book. The Evolution Game With 1 Crore Downloads Fits Almost Nothing Before Class 12",
      "BioMan Biology&rsquo;s browser games line up with NCERT&rsquo;s cell chapters in Classes 9 and 11. Cell to Singularity is a vivid timeline of life that teaches evolution as a ladder with a goal, and since evolution left the Class 10 book, it has little to attach to until Class 12.",
      body, sources, related, OUT)
print("own-all", round(OWN_ALL, 1))
