# Water Instrumentation Study

## Measurement requirement
Eco Data SP requires a plausible physical source for:
- water flow rate;
- accumulated water volume.

The V5.2 shortlist focuses on electromagnetic water-flow measurement because all three selected manufacturer families provide documented water applications and digital integration options.

## 1. Endress+Hauser Proline Promag W 400
**Why it entered the shortlist**

The Promag W 400 is an industrial electromagnetic flowmeter family with official documentation for water-oriented measurement and Modbus RS485 variants. Manufacturer operating documentation publishes a maximum measured error of ±0.5% of reading + 1 mm/s under reference conditions, with an optional ±0.2% of reading ±2 mm/s specification.

**Why it matters to Eco Data SP**

It provides a direct example of the V5.1 concept:

**Water flow → industrial flowmeter → Modbus/gateway → software measurement record**

Its inclusion tests whether Eco Data SP can store both measurement provenance and the communication characteristics of a real industrial flowmeter.

**Status:** CANDIDATE — not deployment-selected.

## 2. Siemens SITRANS FM520 / FMS500 + FMT020
**Why it entered the shortlist**

Siemens documents the FMS500 electromagnetic sensor for water and wastewater applications. Official operating information lists coned sensor sizes DN 15–300 and full-bore sizes DN 350–2000. The system supports optional communication modules including HART, PROFINET, Modbus TCP/RTU, PROFIBUS and EtherNet/IP when configured accordingly.

**Why it matters to Eco Data SP**

The Siemens system is useful for evaluating a modular architecture in which the sensor, transmitter and communication module are explicit parts of the data chain. That maps well to Eco Data SP's separation of instrument, device/gateway, connectivity and software ingestion.

**Status:** CANDIDATE — final nominal diameter, transmitter configuration and communication module require deployment-specific definition.

## 3. ABB AquaMaster4
**Why it entered the shortlist**

ABB positions AquaMaster4 for water-distribution applications including district metering, leakage monitoring and revenue metering. Official ABB information lists flow/velocity/volume measurement, sensor sizes across multiple configurations, accuracy up to ±0.2% ±0.5 mm/s, and communication options including pulse and Modbus. Selected mobile-communication tiers add cellular connectivity and MQTTS/NB-IoT options.

**Why it matters to Eco Data SP**

AquaMaster4 is particularly useful to the research because it represents both conventional industrial integration through Modbus and a more IoT-oriented path in selected configurations. It therefore helps evaluate whether the Eco Data SP ingestion layer should remain protocol-agnostic.

**Status:** CANDIDATE — specifications depend on the selected AquaMaster4 tier and sensor configuration.

## Water-study conclusion
No water meter is declared the winner. The three candidates were retained because they demonstrate three credible integration patterns while remaining within the same measurement domain:
- industrial serial communication;
- modular industrial Ethernet/field communication;
- water-network instrumentation with optional IoT connectivity.

A final selection would require real pipe diameter, expected minimum/maximum flow, pressure, water characteristics, installation constraints, required accuracy, power availability, communication infrastructure and regulatory requirements.
