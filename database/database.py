import sqlite3
from contextlib import contextmanager
from config import DB_PATH, WATER_TARIFF, ENERGY_TARIFF, EMISSION_FACTOR

@contextmanager
def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()

def fetch(sql, params=()):
    with connect() as con:
        return [dict(r) for r in con.execute(sql, params).fetchall()]

def execute(sql, params=()):
    with connect() as con:
        return con.execute(sql, params).lastrowid

def init_database():
    with connect() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS sensors(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          sensor_uid TEXT UNIQUE NOT NULL,
          deployment_class TEXT NOT NULL,
          sensor_type TEXT NOT NULL,
          manufacturer TEXT, model TEXT, physical_principle TEXT,
          measured_variable TEXT NOT NULL, measurement_range TEXT, accuracy TEXT,
          interface TEXT, supply_voltage TEXT, current_consumption TEXT,
          nominal_output TEXT, protocol TEXT, device_uid TEXT,
          installation_point TEXT, calibration_status TEXT, datasheet_source TEXT,
          selection_reason TEXT, safety_notes TEXT, status TEXT DEFAULT 'PLANNED'
        );
        CREATE TABLE IF NOT EXISTS measurements(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          sensor_uid TEXT NOT NULL, metric TEXT NOT NULL, value REAL NOT NULL,
          unit TEXT NOT NULL, source TEXT NOT NULL, measured_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS alerts(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          sensor_uid TEXT, metric TEXT, severity TEXT, message TEXT, created_at TEXT
        );
        CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """)
        seeds=[
          ("FLOW-001","SENSOR_INTEGRATION","Electromagnetic / Ultrasonic Flow Meter","To be selected","To be selected","Flow measurement","water_flow","To be sized","To be verified","Industrial output","Per instrument","Per instrument","L/min, m³/h, accumulated m³","4–20 mA / pulse / Modbus (examples)","GATEWAY-001","Water inlet / process-water line","Required","Manufacturer datasheet required","Possible instrumentation for water flow and consumption.","Verify process compatibility, pressure, temperature, range, accuracy, calibration and safety.","PLANNED"),
          ("CT-001","SENSOR_INTEGRATION","Current Transformer (CT)","To be selected","To be selected","Electromagnetic induction","electrical_current","To be sized","To be verified","Meter input","Per instrument","Per instrument","Current (A)","Energy meter / gateway","ENERGY-METER-001","Electrical distribution panel","Required","Manufacturer datasheet required","Possible instrumentation for electrical current.","Ratio, burden, insulation and protection require engineering definition.","PLANNED"),
          ("VOLT-001","SENSOR_INTEGRATION","Voltage Transducer","To be selected","To be selected","Electrical transduction","voltage","To be sized","To be verified","Meter input","Per instrument","Per instrument","Voltage (V)","Energy meter / gateway","ENERGY-METER-001","Electrical distribution panel","Required","Manufacturer datasheet required","Possible instrumentation for voltage.","Requires isolation, protection and qualified electrical design.","PLANNED"),
          ("METER-001","SENSOR_INTEGRATION","Multifunction Energy Meter","To be selected","To be selected","Electrical metering","power_energy","To be sized","To be verified","Industrial interface","Per instrument","Per instrument","kW / accumulated kWh","Modbus RTU/TCP (example)","GATEWAY-001","Electrical distribution panel","Required","Manufacturer datasheet required","Possible instrumentation for power and energy.","Metering class, wiring, CT compatibility and certifications depend on installation.","PLANNED")
        ]
        con.executemany("""INSERT OR IGNORE INTO sensors(
          sensor_uid,deployment_class,sensor_type,manufacturer,model,physical_principle,
          measured_variable,measurement_range,accuracy,interface,supply_voltage,current_consumption,
          nominal_output,protocol,device_uid,installation_point,calibration_status,datasheet_source,
          selection_reason,safety_notes,status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",seeds)
        for k,v in [("water_tariff",WATER_TARIFF),("energy_tariff",ENERGY_TARIFF),("emission_factor",EMISSION_FACTOR)]:
            con.execute("INSERT OR IGNORE INTO settings(key,value) VALUES(?,?)",(k,str(v)))
