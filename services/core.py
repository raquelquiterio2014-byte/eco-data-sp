from datetime import datetime, timezone
from database.database import fetch, execute

FIELDS = ["sensor_uid","deployment_class","sensor_type","manufacturer","model","physical_principle","measured_variable","measurement_range","accuracy","interface","supply_voltage","current_consumption","nominal_output","protocol","device_uid","installation_point","calibration_status","datasheet_source","selection_reason","safety_notes","status"]

def list_sensors(deployment=None):
    if deployment:
        return fetch("SELECT * FROM sensors WHERE deployment_class=? ORDER BY sensor_uid",(deployment,))
    return fetch("SELECT * FROM sensors ORDER BY deployment_class,sensor_uid")

def save_sensor(data):
    for k in ("sensor_uid","deployment_class","sensor_type","measured_variable"):
        if not str(data.get(k,"")).strip(): raise ValueError(f"{k} is required.")
    vals=[data.get(k,"") for k in FIELDS]
    q=",".join("?" for _ in FIELDS); updates=",".join(f"{k}=excluded.{k}" for k in FIELDS[1:])
    execute(f"INSERT INTO sensors({','.join(FIELDS)}) VALUES({q}) ON CONFLICT(sensor_uid) DO UPDATE SET {updates}", vals)

def add_measurement(sensor_uid, metric, value, unit, source="IOT", measured_at=None):
    if not fetch("SELECT 1 FROM sensors WHERE sensor_uid=?",(sensor_uid,)): raise ValueError("Sensor must be registered first.")
    value=float(value)
    if value < 0: raise ValueError("Negative values are not accepted in this prototype.")
    ts=measured_at or datetime.now(timezone.utc).isoformat()
    execute("INSERT INTO measurements(sensor_uid,metric,value,unit,source,measured_at) VALUES(?,?,?,?,?,?)",(sensor_uid,metric,value,unit,source,ts))
    limits={"water_flow":20.0,"power":8.0}
    if metric in limits and value > limits[metric]:
        execute("INSERT INTO alerts(sensor_uid,metric,severity,message,created_at) VALUES(?,?,?,?,?)",(sensor_uid,metric,"WARNING",f"{metric} {value:.2f} {unit} exceeded configured study threshold {limits[metric]:.2f} {unit}.",ts))

def latest(metric):
    rows=fetch("SELECT * FROM measurements WHERE metric=? ORDER BY measured_at DESC,id DESC LIMIT 1",(metric,))
    return rows[0] if rows else None

def setting(key): return float(fetch("SELECT value FROM settings WHERE key=?",(key,))[0]["value"])

def sustainability_summary():
    w=latest("water_consumption"); e=latest("energy_consumption")
    water=float(w["value"]) if w else 0.0; energy=float(e["value"]) if e else 0.0
    return water,energy,water*setting("water_tariff")+energy*setting("energy_tariff"),energy*setting("emission_factor")

def list_alerts(): return fetch("SELECT * FROM alerts ORDER BY created_at DESC,id DESC")
def history(): return fetch("SELECT * FROM measurements ORDER BY measured_at DESC,id DESC LIMIT 200")

def list_hardware_candidates(domain=None):
    if domain and domain != "ALL":
        return fetch("SELECT * FROM hardware_candidates WHERE domain=? ORDER BY manufacturer,model",(domain,))
    return fetch("SELECT * FROM hardware_candidates ORDER BY domain,manufacturer,model")

def hardware_study_summary():
    rows=list_hardware_candidates()
    return {"total":len(rows),"water":sum(r["domain"]=="WATER" for r in rows),"energy":sum(r["domain"]=="ENERGY" for r in rows),"high_fit":sum(r["eco_fit"]=="HIGH" for r in rows)}
