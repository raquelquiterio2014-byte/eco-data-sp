# Eco Data SP — Sustainability Platform 🌱📊

## Version 5.1 — Sensor Integration Architecture

Eco Data SP is a Python sustainability monitoring platform that evolves environmental and consumption data into traceable analytics for human decision support.

### Development journey
- **V1 — Data Foundation:** manual/CSV input, validation, SQLite and dashboard
- **V2 — Water Monitoring:** water-flow telemetry, device monitoring and alerts
- **V3 — Energy Monitoring:** electrical power and energy telemetry
- **V4 — Cost Analytics:** water and energy consumption combined with configurable tariffs
- **V5 — CO₂e:** estimated emissions from energy consumption and a documented emission factor
- **V5.1 — Sensor Integration:** registration of sensors/meters and measurement provenance
- **Next V6 — AI Integration:** planned intelligence layer on structured, traceable data

## V5.1 focus
V5.1 prepares the software for physical sensor and meter integration without locking the platform to a specific hardware model.

Possible instrumentation examples:
- Water flow & consumption → electromagnetic or ultrasonic flow meter
- Electrical current → Current Transformer (CT)
- Voltage → voltage transducer
- Power & energy → multifunction energy meter
- Cost → calculated from consumption × tariff; no physical sensor
- Estimated CO₂e → calculated from kWh × documented emission factor; no direct sensor in this architecture

These are architectural examples, not fixed hardware requirements. Final selection depends on measurement range, accuracy, operating environment, communication interface, installation conditions, calibration and applicable safety requirements.

## Architecture
**Physical Variable → Sensor / Meter → Device / Gateway → Connectivity → Measurement → SQLite → Analytics → Cost → CO₂e → Human Decision**

## Sensor metadata
The platform can store Sensor ID, type, manufacturer, model, physical principle, measured variable, measurement range, accuracy, interface, supply voltage, current consumption, nominal output, protocol, device ID, installation point, calibration status, datasheet source, selection reason, safety notes and status.

## Preserved capabilities
V5.1 keeps Water, Energy, Cost, estimated CO₂e, Alerts, CSV import, SQLite persistence and Measurement History while adding sensor-to-measurement traceability.

## Technology stack
**Python · CustomTkinter · SQLite · Pandas · MQTT-ready architecture**

## Run locally
```bash
pip install -r requirements.txt
python main.py
```

## Engineering boundary
Eco Data SP is a monitoring and sustainability decision-support platform. Sensor and meter examples do not replace equipment selection, electrical/process engineering, calibration, industrial safety assessment or manufacturer documentation for a real deployment.

## Author
**Raquel Cruz** — ADS student and developer building practical projects in software, data, IoT and artificial intelligence.
