# Hardware Candidate Selection Matrix

> All entries are research candidates. Values are manufacturer-published family/model characteristics and must be re-verified for the exact ordered configuration.

| Domain | Manufacturer / Candidate | Variables | Published range / configuration evidence | Accuracy / class evidence | Communication evidence | Why retained |
|---|---|---|---|---|---|---|
| Water | Endress+Hauser Proline Promag W 400 | Flow, volume | Configuration and nominal diameter dependent; operating documentation covers industrial water-flow configurations | ±0.5% of reading + 1 mm/s; optional ±0.2% of reading ±2 mm/s under stated reference conditions | Modbus RS485 variant documented; other transmitter interfaces exist | Strong industrial flowmeter reference with documented Modbus path |
| Water | Siemens SITRANS FM520 / FMS500 + FMT020 | Flow, volume | FMS500: DN 15–300 coned; DN 350–2000 full bore | Configuration/calibration dependent; verify exact FM520 configuration | HART, PROFINET, Modbus TCP/RTU, PROFIBUS, EtherNet/IP modules documented | Tests modular sensor + transmitter + communication architecture |
| Water | ABB AquaMaster4 | Flow, velocity, volume; pressure on selected tiers | Reduced/full-bore/probe configurations; official family data extends to large water-network sizes | Up to ±0.2% ±0.5 mm/s for published configurations | Pulse, Modbus; selected mobile tiers add 4G/MQTTS or NB-IoT | Tests conventional Modbus and IoT-oriented water-network paths |
| Energy | Schneider Electric PowerLogic PM5560 | V, A, power, energy, frequency, PF | 20–400 V L-N / 20–690 V L-L (Wye) published; 1 A/5 A CT inputs | Active energy Class 0.2S | Modbus RTU/RS485, Modbus TCP/IP, Ethernet; additional protocols documented | High-accuracy multifunction meter and direct software-integration candidate |
| Energy | Siemens SENTRON PAC3220 | V, A, power, energy and related parameters | System/variant and CT dependent | V ±0.2%; A ±0.2%; active power ±0.5%; active energy Class 0.5 | Modbus TCP; RS485 expansion architecture available | Clear Ethernet/Modbus TCP path to higher-level software |
| Energy | ABB M4M 20 | V, A, power, energy, THD | Up to 400 V L-N / 690 V L-L for relevant family configuration; CT-based current input | Active energy Class 0.5S | Variants with Modbus RTU or Modbus TCP/IP | Explicitly validates CT + multifunction-meter architecture |

## Interpretation
The matrix is not a procurement scorecard. `HIGH` integration fit in the application means that a documented communication path can reasonably be mapped to the Eco Data SP architecture. It does not mean that the instrument is the best choice for an unknown installation.
