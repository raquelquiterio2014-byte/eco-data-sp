# Eco Data SP Integration Analysis

## Architecture principle
V5.2 keeps the application independent from a single hardware vendor.

The preferred conceptual boundary is:

**Physical Variable → Industrial Instrument → Industrial Communication / Gateway → Acquisition Adapter → Normalized Measurement → SQLite → Analytics → Cost → Estimated CO2e → Human Decision**

## Water path
A future water adapter could read flow and totalized volume from:
- Modbus RTU/RS485 through a serial gateway;
- Modbus TCP through an Ethernet gateway/device;
- a manufacturer-supported IoT path that is normalized before entering the application;
- pulse data converted by an edge/gateway device when appropriate.

The application should store the source instrument ID, metric, value, unit, timestamp and data source so that measurement provenance is retained.

## Electrical path
A realistic electrical chain is:

**Circuit → Current Transformer + Voltage Inputs → Multifunction Meter → Modbus RTU/TCP → Acquisition Adapter → Eco Data SP**

This is preferable to assuming that every electrical variable arrives from a separate sensor. The software data model can still expose separate metrics while preserving a shared physical instrument origin.

## Protocol strategy
V5.2 does not hard-code one protocol as the universal solution. Modbus is especially relevant because all three electrical candidate families and several water candidates expose a Modbus path, but the software should treat protocol-specific acquisition as an adapter concern.

Potential future adapters:
- `ModbusRTUAdapter`
- `ModbusTCPAdapter`
- `MQTTAdapter`
- `CSVImportAdapter`
- `ManualInputAdapter`

All should normalize into the same measurement model.

## Traceability requirement
A measurement should eventually be traceable through:

**Measurement → Sensor/Meter ID → Manufacturer/Model → Installation Point → Communication Path → Official Datasheet Reference → Calibration/Status**

This is the core engineering contribution of V5.1/V5.2 before AI is introduced.

## What V5.2 does not implement
The current portfolio version does not:
- connect to physical Modbus devices;
- configure electrical protection;
- size CTs;
- size water meters;
- certify a meter for billing;
- configure industrial cybersecurity;
- perform automatic procurement selection;
- replace qualified instrumentation/electrical engineering.

Those are deployment-stage activities.
