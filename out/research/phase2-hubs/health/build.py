"""Hub: health and medical research prototypes (replaces two separate how-to guides).
Build from the repo root: PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/health/build.py
Every figure, command and caveat is taken from the source guides listed in hubs.json under "health":
posts/how-to-use-patient-history-tracking.html and out/research/phase2-hubs/sources/drafts/capsule-endoscopy-cv.html."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-health.html'
GH = 'https://github.com/herrrickshaw/'


def tw(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def code(text):
    return '<pre><code>' + html.escape(text.strip('\n'), quote=False) + '</code></pre>'


def repo(name):
    return f'<a href="{GH}{name}">github.com/herrrickshaw/{name}</a>'


def rl(name):
    return f'<a href="{GH}{name}">{name}</a>'


stats = '''<div class="gb-stats">
<div class="gb-stat"><b>2</b><span>open-source health prototypes, both labelled not a medical device</span></div>
<div class="gb-stat"><b>7</b><span>ICU beds replayed from open, de-identified VitalDB surgical cases</span></div>
<div class="gb-stat"><b>600</b><span>synthetic capsule-endoscopy frames screened in about 3.4 s on the guide&rsquo;s Mac</span></div>
<div class="gb-stat"><b>0</b><span>patient images used in the capsule demo; its thresholds were tuned on synthetic video</span></div>
</div>'''

warn = '''<div class="gb-warn"><strong>Not for patient care.</strong> Both projects are research and learning prototypes. Neither is a medical device, neither has been validated for clinical use, and neither gives clinical advice. The ICU dashboard runs on demo data marked &ldquo;not for clinical use&rdquo;; the capsule screener has not been validated on patient data, and the absence of a flag does not exclude disease.</div>'''

choose = tw(["Tool", "What it does", "Use it when"], [
    [rl("patient-history-tracking"),
     "Replays de-identified ICU vitals into a multi-bed dashboard with alarm rules, and ties a synthetic health ID, simulated insurance, prescriptions and a discharge summary to one patient record",
     "You want to see how a live-vitals pipeline and a linked patient record fit together in one small codebase"],
    [rl("capsule-endoscopy-cv"),
     "Screens every frame of a capsule-endoscopy video for quality, suspected bleeding and lesion candidates, drops redundant frames, estimates gut regions and writes an HTML report",
     "You want a classical computer-vision baseline and report format before adding a learned detector"],
])

api = tw(["Endpoint", "What the demo returned"], [
    ["<code>GET /api/beds</code>", "Seven beds, Bed-A to Bed-F plus Bed-DEMO, each backed by a VitalDB case (Bed-A is case 4096). Bed-DEMO has a 40-second encounter and is marked demo=True."],
    ["<code>WebSocket /ws/vitals</code>", "One tick per bed with heart rate, oxygen saturation, respiratory rate and systolic blood pressure. At sim_t=8, Bed-A showed HR 76, SpO2 100, RR 19. Some values are None when a case has no reading."],
    ["<code>GET /api/beds/Bed-A/identity</code>", "A generated name and a synthetic ABHA-style number, age 53, sex F, General surgery, Cholecystectomy, with a disclaimer that the number is not real."],
    ["<code>GET /api/beds/Bed-DEMO/insurance</code>", "An invented insurer, an eligible status and an approved claim."],
    ["<code>GET /api/beds/Bed-DEMO/record</code>", "Admission, eligibility check, prescriptions, alerts, discharge, discharge summary and claim in one append-only timeline: 27 events."],
    ["<code>GET /api/beds/Bed-DEMO/discharge-summary</code>", "Vitals ranges (HR 71 to 82, SpO2 99 to 100), one alert (RR low), the approved claim and a disclaimer that it is not a real clinical document."],
])

t_ph = f'''<h3>1. patient-history-tracking: a demo ICU dashboard and linked record</h3>
<p>This repository shows how an ICU aggregation dashboard can be put together. A FastAPI backend fetches bedside-monitor numbers from VitalDB, a set of open, de-identified surgical cases, and replays them. It checks each reading against alarm rules and streams the readings over a WebSocket to a React and Vite dashboard with a live bed grid, sparklines and colour-coded alarms. A single patient record collects what other features write into it: a synthetic health ID, simulated insurance, prescriptions, alerts and a discharge summary. Optional OCR of prescriptions and lab reports uses a local Tesseract install.</p>
<p>The patient names, health ID numbers, insurer and policies are all invented, and nothing connects to a real hospital, health ID system or insurer. You need Python 3 for the backend, Node.js and npm for the dashboard, and internet on first run, because the vitaldb library fetches case data at runtime. No login, paid key, database server or Docker is needed; SQLite is created locally. In the guide&rsquo;s demo the API returned:</p>
{api}
<p>Start the backend from the <code>backend</code> folder after <code>pip install -r requirements.txt</code>; the dashboard then runs from <code>frontend</code> with <code>npm install</code> and <code>npm run dev -- --port 5273</code>, at http://localhost:5273.</p>
{code("uvicorn app.main:app --port 8710")}
<p><strong>Main limitation.</strong> Demo data, not for clinical use: it is a prototype, not validated, and not a medical device. The alarm thresholds in backend/app/alerts.py are illustrative defaults that have not been clinically reviewed. There is no real ABDM or insurer integration. Storage is one SQLite file in one process, so it does not scale across machines. The OCR features were not exercised in the demo; the README reports that handwriting OCR misread 650mg as 850mg, so every extracted result goes to a human review queue. The demo called the API in-process, so the browser dashboard itself was not shown.</p>
<p>Code: {repo("patient-history-tracking")}</p>'''

t_cv = f'''<h3>2. capsule-endoscopy-cv: triage and a report from capsule-endoscopy video</h3>
<p>The capsule_cv package screens a capsule-endoscopy recording: a video file, a folder of frames, or a live TCP stream. It uses colour and texture heuristics to score frame quality (brightness, blur, debris), suspected blood, and compact pale or red lesion candidates. It drops frames that repeat the last kept frame and estimates where the stomach, small bowel and colon begin. Flagged frames are grouped into episodes with a peak frame.</p>
<p>Its outputs are report.html (KPIs, a timeline and annotated peak frames), highlights.mp4, frames.csv with every metric for every frame, and study.json. The TCP receiver uses sequence numbers and CRC32, and the guide points to FrameAnalyzer.analyze as the place to add a learned detector, whose results the events and report would then pick up. It needs Python 3.10 or newer with opencv-python-headless, numpy and pytest, and 8 tests passed.</p>
{code(".venv/bin/python -m capsule_cv analyze synthetic/capsule.mp4 --out report")}
<p><strong>Main limitation.</strong> It is a research and decision-support sketch, not a medical device, not validated on patient data and not a diagnosis. Its thresholds were tuned on its own synthetic generator, so the events it recovers show that the plumbing works, not that it works on patients; the README suggests re-tuning on labelled real data such as Kvasir-Capsule. It has no polyp or tumour detection and no deep model, and the region segmentation assumes the study reaches the colon. The live receive and send path was not run in the guide.</p>
<p>Code: {repo("capsule-endoscopy-cv")}</p>'''

worked = '''<p>This example is from the capsule-endoscopy-cv guide, run on 5 November 2026 in a scratch clone and a throwaway virtual environment, on synthetic data only.</p>
<p><strong>Step 1: get the code and install.</strong></p>
''' + code('''
git clone https://github.com/herrrickshaw/capsule-endoscopy-cv.git
cd capsule-endoscopy-cv
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
''') + '''
<p><strong>Step 2: make a synthetic study and analyse it.</strong></p>
''' + code('''
.venv/bin/python -m capsule_cv synth --out synthetic/capsule.mp4
.venv/bin/python -m capsule_cv analyze synthetic/capsule.mp4 --out report
''') + '''
<p>A JSON summary prints, and the report folder gains report.html, highlights.mp4, frames.csv and study.json. The guide&rsquo;s summary, reformatted onto fewer lines with values unchanged:</p>
''' + code('''
{
  "frames": 600, "duration_s": 149.8,
  "usable_frames": 582, "usable_pct": 97.0,
  "duplicate_frames": 131, "frames_to_review": 455,
  "review_reduction_pct": 24.2,
  "bleeding_frames": 30, "lesion_frames": 19,
  "events": {"bleeding": 2, "lesion": 2},
  "region_confidence": 0.73,
  "gastric_transit_s": 22.5, "small_bowel_transit_s": 90.0
}
''') + '''
<p><strong>Step 3: look at the events.</strong> study.json lists each episode. The first two, with fields rearranged for reading:</p>
''' + code('''
bleeding  frames 210-227  t=52.5-56.75 s
          peak_score 0.163   region: small bowel
lesion    frames 288-297  t=72.0-74.25 s
          peak_score 0.0081  region: small bowel
''') + '''
<p><strong>Step 4: run the tests.</strong> <code>.venv/bin/python -m pytest -q tests</code> gave 8 passed.</p>
<p><strong>How to read it.</strong> Of 600 frames, 582 were usable and 131 were redundant, and 455 remained for review: a 24.2% cut in review work. The guide warns not to read that as typical, because it comes from one synthetic study. The two bleeding and two lesion events come from a synthetic study with known ground truth, and the thresholds were tuned on the same generator, so they show the plumbing works, not that it works on patients.</p>'''

donot = '''<ul>
<li><strong>They are research prototypes, not medical devices.</strong> Both guides say so in those words. Neither is for diagnosis, patient care or monitoring of real people, and neither is clinical advice.</li>
<li><strong>Neither has been clinically validated.</strong> The ICU dashboard&rsquo;s alarm thresholds have not been clinically reviewed. The capsule screener has not been validated on patient data, and a frame with no flag does not rule out disease.</li>
<li><strong>The demo results come from demo or synthetic data.</strong> The ICU vitals are real but de-identified surgical cases; the names, health IDs, insurer, policies, claims and prescriptions are invented. The capsule study is wholly synthetic.</li>
<li><strong>They do not connect to real systems.</strong> There is no real ABDM health ID or insurer integration, and the dashboard runs as one process on a SQLite file, not as a hospital system.</li>
<li><strong>Some features were not tested in the guides.</strong> The OCR path, the browser dashboard, the capsule screener&rsquo;s live TCP path and its use on real recordings were not run.</li>
<li><strong>The data have conditions.</strong> VitalDB data are licensed CC BY-NC-SA 4.0 under a data use agreement: non-commercial use only, and no attempt at re-identification. The guide asks anyone who builds on it to cite Lee et al., Scientific Data 2022.</li>
</ul>'''

body = f"""{stats}

<p>These two repositories show how a piece of health software is put together, from incoming data to a dashboard or a report. patient-history-tracking replays real, de-identified ICU vital signs into a multi-bed dashboard, raises alarms and keeps one linked patient record. capsule-endoscopy-cv screens every frame of a wireless capsule-endoscopy video, flags suspected bleeding and lesions, and writes a report.</p>

<p>The guides write for engineers who want to see a complete pipeline in one small codebase, health-IT students learning how a linked patient record is structured, and researchers who want a baseline and a report format before adding a deep-learning model. They also write for non-programmers who want an AI assistant to explain how an ICU dashboard works.</p>

{warn}

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<h2 class="gb-h2">Which one to start with</h2>
<p>capsule-endoscopy-cv is the quicker of the two to get running. It needs only Python 3.10 or newer and three packages, makes its own synthetic study, and analysed 600 frames in about 3.4 seconds on the guide&rsquo;s Mac. patient-history-tracking has more moving parts: a Python backend, a Node.js dashboard in a second terminal, and an internet connection on first run to fetch VitalDB cases. Its API can be explored with the backend alone.</p>

<h2 class="gb-h2">The two tools</h2>
{t_ph}

{t_cv}

<h2 class="gb-h2">Worked example: screening a synthetic capsule study</h2>
{worked}

<h2 class="gb-h2">What these tools do not do</h2>
{donot}
"""

sources = ("This page replaces the two separate how-to guides this blog wrote for these tools, one per repository. "
           "Everything here is taken from those guides: the patient-history-tracking guide used the repository README, "
           "backend/requirements.txt and a demo run of 18 October 2026; the capsule-endoscopy-cv guide used the README, "
           "capsule_cv/ and tests/, run on 5 November 2026 on synthetic data only, with no patient images. "
           "Neither project is a medical device. Repositories: " + repo("patient-history-tracking") + "; "
           + repo("capsule-endoscopy-cv") + ".")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/abha-what-indias-14-digit-health-id.html", "ABHA: What India&#x27;s 14-Digit Health ID Actually Does, in the Real Numbers"),
    ("https://masaladeutsch.blogspot.com/2026/09/abha-covers-93-crore-patients-its.html", "ABHA Covers 93 Crore Patients. Its Doctor Registry Covers 67%, and Insurers Aren&#x27;t Required to Use the Claims Exchange Yet"),
    ("https://masaladeutsch.blogspot.com/2026/09/endoscopes-never-made-indias-pli-list.html", "Endoscopes Never Made India&#x27;s PLI List. At 57% Export Coverage, They Didn&#x27;t Need To."),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-medical-device-trade-gap-and.html", "India&#x27;s Medical-Device Trade Gap — and the Devices Worth Making Here"),
]

TITLE = "Two Open-Source Health Prototypes, an ICU Vitals Dashboard and a Capsule-Endoscopy Screener, and Why Neither Is a Medical Device"
build("Open-Source Tools &middot; 12 November 2026", TITLE,
      "One free project replays de-identified ICU vital signs into a multi-bed dashboard tied to a single patient record; "
      "the other screens capsule-endoscopy video for suspected bleeding and lesions and writes a report. "
      "Both are research and learning prototypes run on demo or synthetic data, and both say plainly that they are not medical devices.",
      body, sources, related, OUT)
print("built", OUT)
