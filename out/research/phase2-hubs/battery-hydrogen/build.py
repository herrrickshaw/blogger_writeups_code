"""Hub: battery, hydrogen and control simulators (replaces five separate how-to guides).
Build from the repo root: PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/battery-hydrogen/build.py
Every figure, command and caveat is taken from the source guides listed in hubs.json under "battery-hydrogen":
posts/how-to-use-{bms-battery-management, ev-battery-management-sim, hydrogen-electrolyser}.html and
out/research/phase2-hubs/sources/drafts/{cell-guardian, bionic-limb-control}.html."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-battery-hydrogen.html'
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


def tool(name, heading, paras, cmd, cmd_note, limit):
    out = [f'<h3>{heading}</h3>']
    out += [f'<p>{p}</p>' for p in paras]
    out.append(f'<p>{cmd_note}</p>')
    out.append(code(cmd))
    out.append(f'<p><strong>Main limitation.</strong> {limit}</p>')
    out.append(f'<p>Code: {repo(name)}</p>')
    return "\n".join(out)


stats = '''<div class="gb-stats">
<div class="gb-stat"><b>5</b><span>open-source simulators: three battery management systems, one electrolyser controller, one EMG hand decoder</span></div>
<div class="gb-stat"><b>112</b><span>tests passed in each of the three battery repos</span></div>
<div class="gb-stat"><b>7 of 8</b><span>bundled electrolyser examples ran to the end; one crashed</span></div>
<div class="gb-stat"><b>97.2%</b><span>EMG decoder accuracy on synthetic data; its README expects 75&ndash;90% on real amputee data</span></div>
</div>'''

choose = tw(["Tool", "What it does", "Use it when"], [
    [rl("cell-guardian"),
     "Simulates a battery management system: cell model, Kalman-filter charge estimate, health tracking, balancing, thermal control, fault supervisor; 8 chemistries",
     "You want the battery simulator with the newest guide and a choice of eight chemistries"],
    [rl("ev-battery-management-sim"),
     "The same kind of battery simulator, plus a NASA battery-data cleaning notebook and a six-dataset validation suite",
     "You plan to bring in the NASA or Kaggle battery data later"],
    [rl("bms-battery-management"),
     "The same kind of battery simulator for scooters, retrofitted cars and buses, with a requirements.txt",
     "You want to step through a single 2-wheeler charge and discharge"],
    [rl("hydrogen-electrolyser-control"),
     "Simulates the controller of a PEM, AEM or alkaline electrolyser: setpoints, ramps, safety limits and a REST API",
     "You want to see how an electrolyser controller is organised, as a teaching reference"],
    [rl("bionic-limb-control"),
     "Turns surface EMG from forearm muscles into prosthetic-hand commands in one Python file",
     "You need a leakage-free baseline for myoelectric pattern recognition"],
])

bms_compare = tw(["Battery repo", "Guide and test run", "Install note"], [
    [rl("cell-guardian"), "Guide of 6 November 2026; 112 tests passed in 3.6 s",
     "No requirements.txt: install numpy, pandas, matplotlib, scipy and pytest yourself; Python 3.10+"],
    [rl("ev-battery-management-sim"), "Guide of 23 October 2026, run 19 October; 112 tests passed in 4.2 s",
     "No requirements.txt: install numpy, pandas, pytest, scipy and matplotlib by hand"],
    [rl("bms-battery-management"), "Guide of 18 October 2026; 112 tests passed in 10.33 s",
     "requirements.txt lists only numpy and pytest; add pandas and matplotlib for the validation and plot runs"],
])

t_cell = tool(
    "cell-guardian", "1. cell-guardian: a battery management system with eight chemistries",
    ["cell-guardian simulates a battery pack the way a BMS controller would manage it. An Extended Kalman Filter "
     "estimates state of charge from voltage and current over a 2-RC Thevenin cell model. A separate estimator tracks "
     "state of health as capacity and resistance fade. A supervisor opens the contactors on over-voltage, "
     "under-voltage, over-current, over-temperature and isolation faults. Balancing, thermal control and power limits "
     "are included.",
     "It ships presets for an electric scooter (15S LFP), a lead-acid 4W retrofit, a modern LFP 4W and an electric "
     "bus, and 8 cell chemistries including LFP, NMC, Na-ion and LTO. It generates its own battery datasets in the "
     "Kaggle file layouts, so analysis code written now should work when you swap in the real CSVs."],
    "python -m bms.simulation --datasets",
    "The quick validation run (about 9 seconds in the guide):",
    "Its validation data are synthetic, generated by the package&rsquo;s own cell model, so the very low errors show "
    "internal consistency only, not accuracy on real cells. It is not certified BMS firmware and must not manage a real "
    "battery. The default <code>python -m bms.simulation</code> run is slow (about 2 min 9 s), and its comparison table "
    "shows 1.4 kWh for the scooter while the scooter&rsquo;s detail block prints 4.8 kWh (100 Ah).")

t_ev = tool(
    "ev-battery-management-sim", "2. ev-battery-management-sim: the battery simulator plus NASA data cleaning",
    ["This repository has the same parts: a two-RC equivalent-circuit cell, an Extended Kalman Filter for state of "
     "charge, capacity and resistance fade for state of health, passive balancing, thermal control, power limits and a "
     "supervisor that opens the contactor on faults. Its command-line flags are --vehicle, --degradation, --cold, "
     "--driving, --manufacturers, --datasets and --plot.",
     "It adds a notebook that turns the NASA battery .mat files into CSVs, and a validation suite for six Kaggle "
     "datasets. The degradation run for a 48 V scooter pack shows health at 90.0% at cycle 100, 80.0% at cycle 200 "
     "and 70.0% at cycle 300, with resistance rising from 2.20 to 2.60 mOhm over that span; end of life at 80% comes "
     "at about 200 cycles."],
    "python -m bms.simulation --degradation",
    "The degradation run:",
    "The six &lsquo;Kaggle validation&rsquo; checks run on synthetic stand-ins, and the script says so itself. Check 2 "
    "is partly circular: the fitted fade rate (0.1001 %/cycle) matches the rate used to generate the data. The NASA "
    "notebook needs a Kaggle login and download and was not run in the guide. In the distributed-BMS check, module 3 "
    "was detected as degraded (SOH 85% against 97.3%) yet the degraded-alert count stayed at 0.")

t_bms = tool(
    "bms-battery-management", "3. bms-battery-management: the battery simulator for a single vehicle run",
    ["This is the earliest of the three battery guides. It describes the same package: a two-RC Thevenin cell model, "
     "an Extended Kalman Filter for charge level, a wear model, passive cell balancing, thermal control, power limits "
     "and a supervisor with fault codes. It compares four vehicle classes, from a 48 V 2-wheeler LFP pack to a 409 V "
     "bus pack of 163.8 kWh.",
     "The 2-wheeler run prints a time table of state, charge, pack voltage, current, hottest cell and fan speed. "
     "Charging started at 15.0% and reached 56.8% at 52.2 V and 47.1 C. After discharge the charge was 53.4%, with no "
     "fault and health at 99.99%."],
    "python -m bms.simulation --vehicle 2W",
    "A single 2-wheeler charge and discharge:",
    "The ageing model is a simple linear fade, so it cannot predict the life of a specific real cell, and the "
    "validation numbers come from synthetic data. The guide found README gaps: requirements.txt omits pandas (needed "
    "by --datasets) and matplotlib (needed by --plot), and the README example uses <code>--vehicle two_wheeler</code> "
    "while the command line accepts 2W, 4W_RETRO or BUS. The all-vehicle plot run did not finish within two minutes. "
    "It has not been validated on a physical pack.")

t_h2 = tool(
    "hydrogen-electrolyser-control", "4. hydrogen-electrolyser-control: a simulated electrolyser controller",
    ["This repository holds a control system for three electrolyser types (PEM, AEM and alkaline), an advanced layer "
     "with ramp profiles, data logging and safety interlocks, a Flask REST API with a Python client, and eight "
     "runnable examples. Everything runs against a software model, not a device. It needs Python 3.7 or newer with "
     "Flask, Flask-CORS, numpy and requests.",
     "Example 5 compares the three types and prints efficiencies of 75.0% (PEM), 72.0% (AEM) and 68.0% (alkaline), "
     "which are the model&rsquo;s configured maxima. Example 4 applies a power ramp: voltage saturates at 47.2 V while "
     "power keeps rising to about 4,000 W and efficiency climbs to 72.5%. The menu is interactive, so the guide pipes "
     "the choice in."],
    "echo 5 | python electrolyser_examples.py",
    "The three-type comparison, after <code>pip install -r requirements.txt</code>:",
    "Simulation only, not for operating real electrolysers: the repository&rsquo;s own validation notes say all "
    "testing used synthetic power profiles and no hardware testing was done. The repository is archived, so no fixes "
    "will be merged. In the guide&rsquo;s runs, example 7 crashed with an AttributeError; a 45 V setpoint did not take "
    "effect (example 1 stayed at 30.0 V); and example 8 printed 316 Nm3/h of hydrogen at every power level with 0 V and "
    "0 A, against a 0.95 Nm3/h spec in the same code. Do not quote its production numbers. The README says "
    "&lsquo;Status: Production Ready&rsquo;, which its validation notes contradict, and it names an /api/production "
    "path that the code serves as /api/monitoring/production.")

t_emg = tool(
    "bionic-limb-control", "5. bionic-limb-control: EMG to prosthetic-hand commands",
    ["emg_decoder.py is a single-file reference pipeline for surface EMG from forearm muscles. It filters at "
     "20&ndash;450 Hz with a mains notch, cuts 200 ms windows with a 50 ms step, computes the Hudgins time-domain "
     "features, classifies with StandardScaler plus LDA, smooths with a 5-window majority vote and sets proportional "
     "speed from normalised mean absolute value. It also has a two-electrode direct-control scheme (flexor closes, "
     "extensor opens, co-contraction cycles the grip) and a causal filter for streaming.",
     "It trains on early repetitions and tests on later ones, which avoids the leakage that, per the guide, inflates "
     "accuracy by 10&ndash;20 points in many EMG projects. On its synthetic demo (8 channels, 6 classes) it reached "
     "97.2% window accuracy offline and 88.2% agreement in a causal online replay over 500 decisions; the gap is "
     "smoothing lag at gesture changes. You can also feed it your own CSV recording with --csv."],
    ".venv/bin/python emg_decoder.py --demo",
    "The synthetic demo, after <code>.venv/bin/pip install -r requirements.txt</code> (numpy, scipy, scikit-learn):",
    "Research and teaching code: not a medical device and not clinical advice. The demo data are synthetic, so 97.2% "
    "is optimistic; the README expects 75&ndash;90% on real amputee data and lower across sessions. Never attach it to "
    "a person without firmware-level current limits, end-stops and a watchdog. The README quotes 89% online agreement; "
    "the guide&rsquo;s run gave 88.2%, put down to run-to-run variation. The --csv path was not run.")

worked = '''<p>This example is from the cell-guardian guide, run on 6 November 2026 on a fresh clone in a throwaway virtual environment, with no accounts or downloads. It shows the quickest way to see all four validation sections, and why the numbers need care.</p>
<p><strong>Step 1: get the code and install.</strong> The repo has no requirements.txt, so the packages are named by hand.</p>
''' + code('''
git clone https://github.com/herrrickshaw/cell-guardian.git
cd cell-guardian
pip install numpy pandas matplotlib scipy pytest
''') + '''
<p><strong>Step 2: run the tests.</strong></p>
''' + code('python -m pytest -q tests') + '''
<p>112 passed in about 4 seconds (3.6 s in the guide&rsquo;s stat line).</p>
<p><strong>Step 3: generate synthetic datasets and validate.</strong> This prints the vehicle comparison table, six dataset shapes and a validation report, in about 9 seconds.</p>
''' + code('''
python -m bms.simulation --datasets
1. EKF SOC Estimation  (NASA 18650 discharge cycles)
   Samples       : 200
   RMSE (SOC)    : 0.117 %
   MAE  (SOC)    : 0.113 %
   Max error     : 0.182 %
   EKF final SOC : 94.4 %   (true: 94.5 %)
   Verdict       : PASS  (target RMSE < 3 %)
2. Capacity Fade Model  (Li-Ion Degradation, 300 cycles)
   SOH RMSE      : 0.0504 %
   Fitted fade   : 0.10010 %/cycle
   EOL prediction: cycle 199  (SOH=80 % threshold)
3. 2-RC Voltage Model  (BMS v2.1 telemetry, 600 steps)
   Voltage RMSE  : 1.07 mV
   Max error     : 3.53 mV
4. RUL Estimation  (500 cycles)
   RUL RMSE      : 4.2 cycles
   EOL predicted : cycle 501
''') + '''
<p><strong>How to read it.</strong> The &lsquo;NASA&rsquo; data here are synthetic, produced by the package&rsquo;s own cell model, so a 0.117% charge error is a self-consistency check, not proof of accuracy on real cells. The same figures (0.117% charge error, 1.07 mV voltage error, 4.2 cycles of remaining-life error) appear in the ev-battery-management-sim and bms-battery-management guides. To test against real cells you would download the Kaggle datasets with download_kaggle_datasets.sh, which needs a Kaggle account; the guide did not do this.</p>'''

donot = '''<ul>
<li><strong>None of them is ready to run real hardware.</strong> The battery simulators are not firmware; cell-guardian&rsquo;s guide says it must not manage a real battery, and bms-battery-management has not been validated on a physical pack. The electrolyser code is simulation only, with no hardware testing done. Makers who connect the EMG decoder to a servo hand must add their own safety layer.</li>
<li><strong>Their validation numbers are not real-world accuracy.</strong> All three battery repos validate on synthetic data shaped like the Kaggle files. The EMG decoder&rsquo;s demo data are synthetic too, and its README expects lower accuracy on real people.</li>
<li><strong>Ageing is a straight line.</strong> The battery degradation model fades 0.1% per cycle, and the script itself labels that an accelerated model, not a real LFP rate.</li>
<li><strong>They are not engineering design.</strong> Do not use them to size, cost or certify a battery pack or a hydrogen plant.</li>
<li><strong>The EMG decoder is not a medical device.</strong> It is not clinical advice, and it must not be attached to a person without independent current limits, end-stops and a watchdog in firmware.</li>
<li><strong>Some outputs are wrong.</strong> The electrolyser&rsquo;s production table (example 8) is physically wrong, and that repository is archived, so it will not be fixed.</li>
</ul>'''

body = f"""{stats}

<p>A battery pack, a hydrogen electrolyser and a powered prosthetic hand all depend on control software. It has to estimate what cannot be measured directly, such as how full and how worn a battery is, keep the device inside safe limits, and act on faults. The five repositories here let you run that kind of software against a model on your own computer, before any hardware exists.</p>

<p>Three are battery management system (BMS) simulators for electric scooters, retrofitted cars and buses. They ship a Python package called bms, run with the same command (<code>python -m bms.simulation</code>), pass 112 tests and print the same validation figures. The fourth simulates the controller of a PEM, AEM or alkaline electrolyser. The fifth decodes muscle signals (EMG) into prosthetic-hand commands. The guides write for students, engineers, e-mobility and energy analysts, and makers, and for non-programmers who want an AI assistant to explain each part.</p>

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<h2 class="gb-h2">Which one to start with</h2>
<p>For battery management, start with cell-guardian. Its guide is the newest (6 November 2026), its tests ran fastest of the three, and it documents eight cell chemistries. The three battery repos differ mainly in how they install:</p>
{bms_compare}
<p>Where the battery guides differ, the newest is the better guide. It found that the default all-vehicle run takes about 2 minutes 9 seconds, so begin with a flag such as <code>--datasets</code>. For the electrolyser, read the limitations below before running anything. For EMG, bionic-limb-control is the only option here, and it is one file you can read from top to bottom.</p>

<h2 class="gb-h2">The five tools</h2>
{t_cell}

{t_ev}

{t_bms}

{t_h2}

{t_emg}

<h2 class="gb-h2">Worked example: validating the battery model with cell-guardian</h2>
{worked}

<h2 class="gb-h2">What these tools do not do</h2>
{donot}
"""

links = "; ".join(repo(r) for r in [
    "cell-guardian", "ev-battery-management-sim", "bms-battery-management",
    "hydrogen-electrolyser-control", "bionic-limb-control"])

sources = ("This page replaces the five separate how-to guides this blog wrote for these tools, one per repository. "
           "Everything here is taken from those guides, which drew on each repository&rsquo;s README, source and tests and on "
           "runs in throwaway environments: bms-battery-management on 18 October 2026, ev-battery-management-sim on "
           "19 October 2026, hydrogen-electrolyser-control on 23 October 2026, bionic-limb-control on 5 November 2026 and "
           "cell-guardian on 6 November 2026. Where the battery guides differ, the newest (cell-guardian) is preferred. "
           "All results are from simulation or synthetic data. Repositories: " + links + ".")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/the-battery-passport-was-built-for.html", "The Battery Passport Was Built for Recycling. Now It&#x27;s Also the Fix for Battery Fires."),
    ("https://masaladeutsch.blogspot.com/2026/09/indias-battery-storage-boom-is.html", "India&#x27;s Battery Storage Boom Is Outrunning Both Its Tariffs and Its Factories"),
    ("https://masaladeutsch.blogspot.com/2026/08/the-easiest-ev-conversion-in-india.html", "The Easiest EV Conversion in India Hasn&#x27;t Happened Yet: The Government&#x27;s Own Fleet"),
    ("https://masaladeutsch.blogspot.com/2026/08/the-levelised-cost-of-hydrogen.html", "The Levelised Cost of Hydrogen, Explained: What It Would Actually Take to Hit India&#x27;s $1.50/kg Target"),
    ("https://masaladeutsch.blogspot.com/2026/09/alimco-jaipur-foot-and-bionic-gap-in.html", "ALIMCO, Jaipur Foot, and the Bionic Gap in India&#x27;s Artificial-Limb System"),
]

TITLE = "Five Open-Source Control Simulators for EV Batteries, Hydrogen Electrolysers and Prosthetic Hands, and Which to Start With"
build("Open-Source Tools &middot; 12 November 2026", TITLE,
      "Three free Python projects simulate an electric-vehicle battery management system, one simulates an electrolyser "
      "controller, and one turns muscle signals into prosthetic-hand commands. "
      "Each ran in its guide without hardware, and each says its results come from simulation or synthetic data, not a real device.",
      body, sources, related, OUT)
print("built", OUT)
