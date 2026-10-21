# Eco Data SP V5.2 — Hardware Selection Study

## Purpose
This documentation records the research basis behind the commercial instrumentation candidate shortlist used in Eco Data SP V5.2.

V5.2 does **not** claim that any listed product has been selected for purchase or deployment. The products are research candidates chosen to test whether the V5.1 sensor-integration architecture maps to real industrial instrumentation documented by official manufacturers.

## Research question
Which commercially available industrial instruments can provide the water and electrical measurements required by Eco Data SP while offering a technically plausible path to software integration and traceable manufacturer evidence?

## Scope
The study covers two domains:
- Water flow and accumulated water volume.
- Electrical current, voltage, power and accumulated energy.

Cost and estimated CO2e are intentionally excluded from physical sensor selection because they are calculated indicators in Eco Data SP.

## Candidate shortlist
### Water
- Endress+Hauser Proline Promag W 400
- Siemens SITRANS FM520 system using FMS500 sensor / FMT020 transmitter
- ABB AquaMaster4

### Electrical energy
- Schneider Electric PowerLogic PM5560
- Siemens SENTRON PAC3220
- ABB M4M 20

## Meaning of "candidate"
`CANDIDATE` means that official manufacturer evidence supports further technical evaluation. It does not mean approved, purchased, certified for a specific site, or recommended independently of installation requirements.

## Documentation set
- `research-methodology.md` — research method and inclusion/exclusion criteria.
- `water-instrumentation-study.md` — water candidate analysis and rationale.
- `energy-instrumentation-study.md` — electrical candidate analysis and rationale.
- `selection-matrix.md` — side-by-side technical shortlist.
- `integration-analysis.md` — how each category could connect to Eco Data SP.
- `references.md` — official manufacturer sources consulted.

## Key engineering finding
V5.1 represented current, voltage, power and energy as separate measurement concepts. V5.2 research shows that a multifunction power/energy meter can consolidate several electrical variables in one instrument, while external current transformers may remain part of the measurement chain. The software architecture therefore separates **measured variable** from **physical instrument count**.

## Research boundary
Final engineering selection requires site-specific information that is not available in this portfolio study, including pipe diameter, expected flow profile, fluid/process conditions, electrical topology, nominal voltage, maximum current, CT ratio, environmental classification, installation category, calibration requirements, local regulations, cybersecurity requirements and final communication infrastructure.
