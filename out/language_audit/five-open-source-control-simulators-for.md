# Language audit — Five Open-Source Control Simulators for EV Batteries, Hydrogen Electrolysers and Prosthetic Hands, and Which to Start With

*https://blog.vertistratsolution.com/2026/11/five-open-source-control-simulators-for.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...un with the same command (python -m bms.simulation), pass 112 tests and print the same val...
  suggested:  Simulation,  simulation
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...9 seconds in the guide):  python -m bms.simulation --datasets  Main limitation. Its valida...
  suggested:  Simulation,  simulation
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...real battery. The default python -m bms.simulation run is slow (about 2 min 9 s), and its ...
  suggested:  Simulation,  simulation
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...s.  The degradation run:  python -m bms.simulation --degradation  Main limitation. The six...
  suggested:  Simulation,  simulation
- **[GRAMMAR/THE_SUPERLATIVE]** A determiner may be missing.
  context: ...f state, charge, pack voltage, current, hottest cell and fan speed. Charging started at...
  suggested: the hottest
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...er charge and discharge:  python -m bms.simulation --vehicle 2W  Main limitation. The agei...
  suggested:  Simulation,  simulation
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...ort, in about 9 seconds.  python -m bms.simulation --datasets 1. EKF SOC Estimation (NASA ...
  suggested:  Simulation,  simulation
