import pandas as pd
from services.core import add_measurement

def import_csv(path):
    df=pd.read_csv(path)
    required={"sensor_uid","metric","value","unit","measured_at"}
    missing=required-set(df.columns)
    if missing: raise ValueError("Missing CSV columns: "+", ".join(sorted(missing)))
    for _,r in df.iterrows():
        add_measurement(str(r.sensor_uid),str(r.metric),float(r.value),str(r.unit),"CSV",str(r.measured_at))
    return len(df)
