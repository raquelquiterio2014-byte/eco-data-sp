# Eco Data SP — Sustainability Platform

## V5.2 — Hardware Selection Study

V5.2 preserves the V5.1 sensor-integration architecture and adds an **evidence-backed commercial hardware candidate study** for water and electrical monitoring.

The purpose is not to recommend a purchase. It is to show how software requirements can be traced to real industrial instrumentation using official manufacturer documentation.

### New V5.2 module

**Hardware Selection Study** compares:

- manufacturer and model
- instrument type and measured variables
- measurement range
- accuracy / metering class
- communication protocol
- typical application
- possible Eco Data SP integration path
- official manufacturer source
- evidence note and candidate status

No prices are stored or displayed.

### Current candidate matrix

**Water**
- Endress+Hauser Proline Promag W 400
- Siemens SITRANS FM520 (FMS500 + FMT020)
- ABB AquaMaster4

**Electrical monitoring**
- Schneider Electric PowerLogic PM5560
- Siemens SENTRON PAC3220
- ABB M4M 20

The matrix intentionally keeps all products as **CANDIDATE**. A real deployment requires engineering review of process/electrical conditions, measurement range, accuracy, communications, installation, calibration, cybersecurity and safety.

### Architecture

**Physical Variable → Industrial Instrument → Modbus / Industrial Ethernet / Gateway → Eco Data SP → SQLite → Analytics → Cost → Estimated CO₂e → Human Decision**

A key V5.2 finding is that a multifunction electrical meter can consolidate voltage, current, power and energy measurements. Depending on the product and installation, external current transformers may still be required.

### Development journey

**V1 Data Foundation → V2 Water → V3 Energy → V4 Cost → V5 CO₂e → V5.1 Sensor Integration → V5.2 Hardware Selection Study → V6 AI**

### Research documentation

The complete evidence trail is stored under `docs/hardware-selection/`:

- `research-methodology.md` — official-source policy, inclusion/exclusion criteria and study boundaries
- `water-instrumentation-study.md` — rationale for the three water candidates
- `energy-instrumentation-study.md` — rationale for the three electrical candidates
- `selection-matrix.md` — side-by-side technical comparison
- `integration-analysis.md` — vendor-neutral integration architecture
- `references.md` — official manufacturer sources consulted

The documentation distinguishes **candidate shortlist** from **final hardware selection** and records why each commercial family was included.

### Run in PyCharm

```bash
pip install -r requirements.txt
python main.py
```

The database is created locally as `eco_data_sp_v5_2.db`.

### Engineering boundary

The commercial models are research references based on official manufacturer material. They are not endorsements, partnerships, procurement recommendations, or final deployment specifications.

## Author

**Raquel Cruz**
