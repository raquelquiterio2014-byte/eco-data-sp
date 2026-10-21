# Electrical Energy Instrumentation Study

## Measurement requirement
Eco Data SP uses the following electrical variables:
- current (A);
- voltage (V);
- power (kW);
- accumulated energy (kWh).

V5.2 research changed an important architecture assumption: these variables do not necessarily require four independent instruments. A multifunction power/energy meter can measure several variables, normally using current transformers where required for current measurement.

## 1. Schneider Electric PowerLogic PM5560
**Why it entered the shortlist**

Official Schneider Electric documentation identifies the PM5560 as a power and energy meter with active-energy Class 0.2S accuracy. Product documentation lists voltage measurement ranges including 20–400 V L-N and 20–690 V L-L for relevant configurations and nominal 1 A / 5 A current inputs associated with CT-based measurement. Communication capabilities include Ethernet, RS485, Modbus TCP/IP and Modbus RTU; product documentation also lists additional building/industrial protocols depending on the interface.

**Why it matters to Eco Data SP**

The PM5560 demonstrates that current, voltage, power and energy can be consolidated at the meter level and delivered digitally to software. This is a more realistic industrial architecture than assuming a dedicated software-facing sensor for every electrical variable.

**Status:** CANDIDATE — wiring topology, CT sizing and installation category require site engineering.

## 2. Siemens SENTRON PAC3220
**Why it entered the shortlist**

Official Siemens technical data lists Modbus TCP communication and measurement performance including ±0.2% for voltage, ±0.2% for current, ±0.5% for active power and Class 0.5 active energy. Siemens documentation also describes Ethernet integration into higher-level systems; RS485/Modbus RTU can be provided through the appropriate expansion architecture.

**Why it matters to Eco Data SP**

The PAC3220 provides a clear Ethernet/Modbus TCP integration case. It is useful for designing a future data-acquisition service that polls registers or receives values through an industrial gateway before normalizing them into Eco Data SP measurement records.

**Status:** CANDIDATE — CT ratio and system configuration are not selected in this portfolio study.

## 3. ABB M4M 20
**Why it entered the shortlist**

ABB states that M4M 20 provides electrical-parameter monitoring including current, voltage, energy and power. The official family information lists active-energy accuracy Class 0.5S for M4M 20 and variants with Modbus RTU or Modbus TCP/IP. ABB also states that standard M4M units require 1 A or 5 A current transformers (except Rogowski-specific variants) and can measure up to 400 V L-N / 690 V L-L without external voltage transformers for those levels.

**Why it matters to Eco Data SP**

M4M 20 directly supports the architectural finding that the current transformer and multifunction meter form a measurement chain rather than two unrelated software sensors. It also provides another Modbus-based candidate for a vendor-neutral acquisition layer.

**Status:** CANDIDATE — exact variant, CTs and communication option remain deployment-specific.

## Electrical-study conclusion
The shortlist deliberately contains multifunction meters from three major industrial manufacturers. The research goal is not brand ranking; it is to validate an architecture pattern:

**Electrical circuit → CT/direct voltage inputs → multifunction meter → Modbus/industrial network → Eco Data SP**

A final selection requires electrical single-line information, nominal voltage, maximum load current, required metering class, CT ratio/burden, panel environment, protection/isolation requirements, communication topology and qualified electrical engineering review.
