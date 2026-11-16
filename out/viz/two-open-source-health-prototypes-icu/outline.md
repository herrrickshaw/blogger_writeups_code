2open-source health prototypes, both labelled not a medical device

7ICU beds replayed from open, de-identified VitalDB surgical cases

600synthetic capsule-endoscopy frames screened in about 3.4 s on the guide’s Mac

0patient images used in the capsule demo; its thresholds were tuned on synthetic video

These two repositories show how a piece of health software is put together, from incoming data to a dashboard or a report. patient-history-tracking replays real, de-identified ICU vital signs into a multi-bed dashboard, raises alarms and keeps one linked patient record. capsule-endoscopy-cv screens every frame of a wireless capsule-endoscopy video, flags suspected bleeding and lesions, and writes a report.

The guides write for engineers who want to see a complete pipeline in one small codebase, health-IT students learning how a linked patient record is structured, and researchers who want a baseline and a report format before adding a deep-learning model. They also write for non-programmers who want an AI assistant to explain how an ICU dashboard works.

Not for patient care. Both projects are research and learning prototypes. Neither is a medical device, neither has been validated for clinical use, and neither gives clinical advice. The ICU dashboard runs on demo data marked “not for clinical use”; the capsule screener has not been validated on patient data, and the absence of a flag does not exclude disease.

## Which tool for which job


[T1 "Which tool for which job" 2 rows; use rows by number in a chart "table" spec]
  cols: c0 Tool | c1 What it does | c2 Use it when
  r0: patient-history-tracking | Replays de-identified ICU vitals into a multi-bed dashboard with alarm rules, and ties a synthetic health ID, simulated insurance, prescriptions and a discharge summary to one patient record | You want to see how a live-vitals pipeline and a linked patient record fit together in one small codebase
  r1: capsule-endoscopy-cv | Screens every frame of a capsule-endoscopy video for quality, suspected bleeding and lesion candidates, drops redundant frames, estimates gut regions and writes an HTML report | You want a classical computer-vision baseline and report format before adding a learned detector


## Which one to start with

capsule-endoscopy-cv is the quicker of the two to get running. It needs only Python 3.10 or newer and three packages, makes its own synthetic study, and analysed 600 frames in about 3.4 seconds on the guide’s Mac. patient-history-tracking has more moving parts: a Python backend, a Node.js dashboard in a second terminal, and an internet connection on first run to fetch VitalDB cases. Its API can be explored with the backend alone.

## The two tools

### 1. patient-history-tracking: a demo ICU dashboard and linked record

This repository shows how an ICU aggregation dashboard can be put together. A FastAPI backend fetches bedside-monitor numbers from VitalDB, a set of open, de-identified surgical cases, and replays them. It checks each reading against alarm rules and streams the readings over a WebSocket to a React and Vite dashboard with a live bed grid, sparklines and colour-coded alarms. A single patient record collects what other features write into it: a synthetic health ID, simulated insurance, prescriptions, alerts and a discharge summary. Optional OCR of prescriptions and lab reports uses a local Tesseract install.

The patient names, health ID numbers, insurer and policies are all invented, and nothing connects to a real hospital, health ID system or insurer. You need Python 3 for the backend, Node.js and npm for the dashboard, and internet on first run, because the vitaldb library fetches case data at runtime. No login, paid key, database server or Docker is needed; SQLite is created locally. In the guide’s demo the API returned:


[T2 "1. patient-history-tracking: a demo ICU dashboard and linked record" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Endpoint | c1 What the demo returned
  r0: GET /api/beds | Seven beds, Bed-A to Bed-F plus Bed-DEMO, each backed by a VitalDB case (Bed-A is case 4096). Bed-DEMO has a 40-second encounter and is marked demo=True.
  r1: WebSocket /ws/vitals | One tick per bed with heart rate, oxygen saturation, respiratory rate and systolic blood pressure. At sim_t=8, Bed-A showed HR 76, SpO2 100, RR 19. Some values are None when a case has no reading.
  r2: GET /api/beds/Bed-A/identity | A generated name and a synthetic ABHA-style number, age 53, sex F, General surgery, Cholecystectomy, with a disclaimer that the number is not real.
  r3: GET /api/beds/Bed-DEMO/insurance | An invented insurer, an eligible status and an approved claim.
  r4: GET /api/beds/Bed-DEMO/record | Admission, eligibility check, prescriptions, alerts, discharge, discharge summary and claim in one append-only timeline: 27 events.
  r5: GET /api/beds/Bed-DEMO/discharge-summary | Vitals ranges (HR 71 to 82, SpO2 99 to 100), one alert (RR low), the approved claim and a disclaimer that it is not a real clinical document.


Start the backend from the backend folder after pip install -r requirements.txt; the dashboard then runs from frontend with npm install and npm run dev -- --port 5273, at http://localhost:5273.

uvicorn app.main:app --port 8710
Main limitation. Demo data, not for clinical use: it is a prototype, not validated, and not a medical device. The alarm thresholds in backend/app/alerts.py are illustrative defaults that have not been clinically reviewed. There is no real ABDM or insurer integration. Storage is one SQLite file in one process, so it does not scale across machines. The OCR features were not exercised in the demo; the README reports that handwriting OCR misread 650mg as 850mg, so every extracted result goes to a human review queue. The demo called the API in-process, so the browser dashboard itself was not shown.

Code: [github.com/herrrickshaw/patient-history-tracking](https://github.com/herrrickshaw/patient-history-tracking)

### 2. capsule-endoscopy-cv: triage and a report from capsule-endoscopy video

The capsule_cv package screens a capsule-endoscopy recording: a video file, a folder of frames, or a live TCP stream. It uses colour and texture heuristics to score frame quality (brightness, blur, debris), suspected blood, and compact pale or red lesion candidates. It drops frames that repeat the last kept frame and estimates where the stomach, small bowel and colon begin. Flagged frames are grouped into episodes with a peak frame.

Its outputs are report.html (KPIs, a timeline and annotated peak frames), highlights.mp4, frames.csv with every metric for every frame, and study.json. The TCP receiver uses sequence numbers and CRC32, and the guide points to FrameAnalyzer.analyze as the place to add a learned detector, whose results the events and report would then pick up. It needs Python 3.10 or newer with opencv-python-headless, numpy and pytest, and 8 tests passed.

.venv/bin/python -m capsule_cv analyze synthetic/capsule.mp4 --out report
Main limitation. It is a research and decision-support sketch, not a medical device, not validated on patient data and not a diagnosis. Its thresholds were tuned on its own synthetic generator, so the events it recovers show that the plumbing works, not that it works on patients; the README suggests re-tuning on labelled real data such as Kvasir-Capsule. It has no polyp or tumour detection and no deep model, and the region segmentation assumes the study reaches the colon. The live receive and send path was not run in the guide.

Code: [github.com/herrrickshaw/capsule-endoscopy-cv](https://github.com/herrrickshaw/capsule-endoscopy-cv)

## Worked example: screening a synthetic capsule study

This example is from the capsule-endoscopy-cv guide, run on 5 November 2026 in a scratch clone and a throwaway virtual environment, on synthetic data only.

Step 1: get the code and install.

git clone https://github.com/herrrickshaw/capsule-endoscopy-cv.git
cd capsule-endoscopy-cv
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
Step 2: make a synthetic study and analyse it.

.venv/bin/python -m capsule_cv synth --out synthetic/capsule.mp4
.venv/bin/python -m capsule_cv analyze synthetic/capsule.mp4 --out report
A JSON summary prints, and the report folder gains report.html, highlights.mp4, frames.csv and study.json. The guide’s summary, reformatted onto fewer lines with values unchanged:

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
Step 3: look at the events. study.json lists each episode. The first two, with fields rearranged for reading:

bleeding frames 210-227 t=52.5-56.75 s
 peak_score 0.163 region: small bowel
lesion frames 288-297 t=72.0-74.25 s
 peak_score 0.0081 region: small bowel
Step 4: run the tests. .venv/bin/python -m pytest -q tests gave 8 passed.

How to read it. Of 600 frames, 582 were usable and 131 were redundant, and 455 remained for review: a 24.2% cut in review work. The guide warns not to read that as typical, because it comes from one synthetic study. The two bleeding and two lesion events come from a synthetic study with known ground truth, and the thresholds were tuned on the same generator, so they show the plumbing works, not that it works on patients.

## What these tools do not do

- They are research prototypes, not medical devices. Both guides say so in those words. Neither is for diagnosis, patient care or monitoring of real people, and neither is clinical advice.

- Neither has been clinically validated. The ICU dashboard’s alarm thresholds have not been clinically reviewed. The capsule screener has not been validated on patient data, and a frame with no flag does not rule out disease.

- The demo results come from demo or synthetic data. The ICU vitals are real but de-identified surgical cases; the names, health IDs, insurer, policies, claims and prescriptions are invented. The capsule study is wholly synthetic.

- They do not connect to real systems. There is no real ABDM health ID or insurer integration, and the dashboard runs as one process on a SQLite file, not as a hospital system.

- Some features were not tested in the guides. The OCR path, the browser dashboard, the capsule screener’s live TCP path and its use on real recordings were not run.

- The data have conditions. VitalDB data are licensed CC BY-NC-SA 4.0 under a data use agreement: non-commercial use only, and no attempt at re-identification. The guide asks anyone who builds on it to cite Lee et al., Scientific Data 2022.
