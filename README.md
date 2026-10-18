# Eco Data SP 🌱📊

**Eco Data SP — Sustainability Platform** is a Python-based sustainability monitoring platform designed to transform environmental and consumption data into actionable insights.

The project has evolved from a manual/CSV data MVP into an **IoT-ready architecture**, while preserving the original principle: advanced technology should only be added when it improves the usefulness, reliability, or scalability of the system.

## Project goal

Many organizations manage water, energy, cost, and sustainability information across bills, spreadsheets, PDFs, and disconnected systems. Eco Data SP aims to centralize these records, validate them, monitor relevant indicators, identify abnormal conditions, and present clear information to support human decision-making.

## Version 2 — IoT-ready architecture

The V2 architecture follows a layered IoT approach:

**Sensors / Meters → ESP32 / Edge → Wi-Fi or LoRa → MQTT → Eco Data SP → SQLite → Analytics & Alerts → Human Decision**

The platform remains hybrid and can receive data from:

**Manual Input | CSV Import | IoT Telemetry**

Organizations therefore do not need a complete IoT infrastructure to start using the platform.

## First IoT use case: Water Monitoring 💧

The first connected use case focuses on water-flow monitoring.

- Physical quantity: **water flow**
- Unit: **L/min**
- Initial study range: **0–30 L/min**
- Sampling interval: **10 seconds**
- Edge device: **ESP32**
- Communication: **Wi-Fi**, with the architecture prepared for alternatives such as **LoRa**
- Messaging: **MQTT / Mosquitto-compatible**
- Initial configurable warning reference: **20 L/min**

> The 20 L/min value is an initial study threshold, not a universal leak threshold. In a real deployment, alert rules must be configured according to each installation and operating context.

## V2 features

- Sustainability overview dashboard
- Water-flow telemetry
- IoT device registry
- Device connectivity and last-seen tracking
- MQTT telemetry ingestion
- Manual ESP32 reading simulator for validation without physical hardware
- CSV import
- Data-source provenance: `MANUAL`, `CSV`, or `IOT`
- Configurable alert-rule data model
- High-flow warnings
- SQLite persistence
- Architecture prepared for organizations, units, devices, measurements, and alerts
- Human oversight for critical decisions

## Edge and platform responsibilities

### Edge / device
The ESP32 can collect measurements and support local detection of abnormal conditions. This architecture allows essential monitoring logic to remain close to the physical environment and reduces dependence on continuous connectivity.

### Eco Data SP
The platform is responsible for storing historical data, organizing devices and measurements, presenting monitoring information, applying platform-level rules, and supporting analytics, alerts, and reports.

Critical physical actions are **not automatically executed in the current MVP**. The system informs; people decide.

## Scalability principle

A prototype with one sensor does not prove that a system is ready for hundreds of devices.

For that reason, V2 begins separating responsibilities for:

- organizations and units
- device identification
- telemetry
- connectivity status
- measurements
- alert rules
- alerts

This provides a foundation for future fleet management, diagnostics, multi-location deployments, and larger-scale monitoring.

## Technology stack

**Python · CustomTkinter · SQLite · Pandas · MQTT · Paho MQTT**

IoT architecture concepts include **ESP32, edge processing, Wi-Fi/LoRa communication, and Mosquitto-compatible MQTT messaging**.

## Running the V2 prototype

1. Open the project in PyCharm.
2. Use Python 3.10 or newer.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python main.py
```

A running MQTT broker is optional for the first software validation. Without Mosquitto, the GUI can still be tested using the built-in Water Live simulator.

### Example MQTT topic

```text
eco-data/<unit>/<device>/telemetry
```

### Example payload

```json
{
  "device_id": "ESP32-WATER-001",
  "metric": "water_flow",
  "value": 12.4,
  "unit": "L/min"
}
```

## Current validation

The V2 desktop prototype has been executed in PyCharm. The interface includes the Sustainability Overview, Water Live, IoT Devices, Alerts, and CSV import functions.

During the current software validation, simulated water-flow readings above the configured 20 L/min study threshold generated warning records in the Alerts view, validating the basic flow from measurement to persistence, rule evaluation, and visual alert presentation.

## Roadmap

- **v1:** manual/CSV sustainability data flow, validation, SQLite storage, dashboard, indicators, goals, alerts, and reports
- **v2:** IoT-ready architecture, device registry, water telemetry, MQTT integration, edge concepts, connectivity monitoring, and configurable alerts
- **Next:** improve dashboard visualization, configurable alert controls, device-health monitoring, offline synchronization, and broader sustainability telemetry
- **Future:** anomaly detection, adaptive baselines, APIs, forecasting, and AI-assisted recommendations where they provide measurable value

## Design principles

**Environmental Data → Connected Monitoring → Analytics → Insights → Better Sustainability Decisions**

Eco Data SP is designed around modularity, interoperability, scalability, traceability, and human oversight.

## Author

**Raquel Cruz** — ADS student and developer building practical projects in software, data, IoT, and artificial intelligence.
