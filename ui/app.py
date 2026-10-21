import customtkinter as ctk
from tkinter import filedialog, messagebox
from services.core import *
from services.csv_service import import_csv

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Eco Data SP — Sustainability Platform | V5.1")
        self.geometry("1500x900")
        self.frames={}
        self.grid_columnconfigure(1,weight=1); self.grid_rowconfigure(0,weight=1)
        self._build(); self.show("dashboard")

    def _base(self,key,title,subtitle):
        f=ctk.CTkFrame(self.content,fg_color="#F4F8FB")
        ctk.CTkLabel(f,text=title,font=("Arial",28,"bold"),text_color="#082E46").pack(anchor="w",padx=30,pady=(25,2))
        ctk.CTkLabel(f,text=subtitle,text_color="#55717F").pack(anchor="w",padx=30,pady=(0,15))
        self.frames[key]=f; return f

    def _text(self,key,title,subtitle):
        f=self._base(key,title,subtitle); b=ctk.CTkTextbox(f,font=("Consolas",13))
        b.pack(fill="both",expand=True,padx=30,pady=10); setattr(self,key+"_box",b)

    def _build(self):
        side=ctk.CTkFrame(self,width=240,corner_radius=0,fg_color="#082E46"); side.grid(row=0,column=0,sticky="nsew")
        ctk.CTkLabel(side,text="ECO DATA SP",font=("Arial",22,"bold"),text_color="white").pack(pady=(28,2))
        ctk.CTkLabel(side,text="V5.1 • Sensor Integration",text_color="#B9D7E8").pack(pady=(0,20))
        self.content=ctk.CTkFrame(self,corner_radius=0,fg_color="#F4F8FB"); self.content.grid(row=0,column=1,sticky="nsew")
        self._dashboard(); self._sensors(); self._live()
        self._text("architecture","Sensor Integration Architecture","Possible examples — final hardware depends on deployment requirements.")
        self._text("analytics","Costs & CO₂e","Calculated indicators — not physical sensors")
        self._text("alerts","Alerts","Threshold events with measurement provenance")
        self._text("history","Measurement History","Sensor / meter → measurement traceability")
        for label,key in [("Dashboard","dashboard"),("Sensor Architecture","architecture"),("Sensors & Meters","sensors"),("Water & Energy","live"),("Costs & CO₂e","analytics"),("Alerts","alerts"),("History","history")]:
            ctk.CTkButton(side,text=label,anchor="w",fg_color="transparent",hover_color="#164B66",command=lambda k=key:self.show(k)).pack(fill="x",padx=15,pady=4)
        ctk.CTkButton(side,text="Import CSV",anchor="w",fg_color="transparent",hover_color="#164B66",command=self.import_file).pack(fill="x",padx=15,pady=4)

    def _dashboard(self):
        f=self._base("dashboard","Sustainability Overview","V5.1 — Sensor Integration Architecture")
        row=ctk.CTkFrame(f,fg_color="transparent"); row.pack(fill="x",padx=25)
        self.cards=[]
        for label in ["Water Flow\n—","Power\n—","Total Cost\nR$ 0.00","Estimated CO₂e\n0.00 kg","Sensors\n0","Alerts\n0"]:
            c=ctk.CTkLabel(row,text=label,width=175,height=95,fg_color="white",corner_radius=12,font=("Arial",14,"bold")); c.pack(side="left",padx=4); self.cards.append(c)
        self.dashboard_box=ctk.CTkTextbox(f,font=("Consolas",14)); self.dashboard_box.pack(fill="both",expand=True,padx=30,pady=20)

    def _sensors(self):
        f=self._base("sensors","Sensors & Meters","Technical metadata + measurement provenance")
        form=ctk.CTkScrollableFrame(f,height=350); form.pack(fill="x",padx=30,pady=4)
        self.fields={}
        for i,key in enumerate(FIELDS):
            ctk.CTkLabel(form,text=key.replace("_"," ").title(),width=175,anchor="w").grid(row=i//2,column=(i%2)*2,padx=7,pady=4,sticky="w")
            e=ctk.CTkEntry(form,width=350); e.grid(row=i//2,column=(i%2)*2+1,padx=7,pady=4); self.fields[key]=e
        self.fields["deployment_class"].insert(0,"SENSOR_INTEGRATION"); self.fields["status"].insert(0,"PLANNED")
        ctk.CTkButton(f,text="Save / Update Sensor",command=self.save_sensor_ui).pack(anchor="w",padx=30,pady=8)
        self.sensor_box=ctk.CTkTextbox(f,height=240,font=("Consolas",12)); self.sensor_box.pack(fill="both",expand=True,padx=30,pady=5)

    def _live(self):
        f=self._base("live","Water & Energy Measurements","Readings linked to registered sensor and meter examples")
        for suid,metric,label,unit in [("FLOW-001","water_flow","Water flow","L/min"),("FLOW-001","water_consumption","Water consumption","m³"),("CT-001","electrical_current","Electrical current","A"),("VOLT-001","voltage","Voltage","V"),("METER-001","power","Electrical power","kW"),("METER-001","energy_consumption","Energy consumption","kWh")]:
            r=ctk.CTkFrame(f,fg_color="white"); r.pack(fill="x",padx=30,pady=4)
            ctk.CTkLabel(r,text=f"{label} — {suid}",width=350,anchor="w").pack(side="left",padx=12,pady=12)
            e=ctk.CTkEntry(r,width=150,placeholder_text="Enter value"); e.pack(side="left")
            ctk.CTkButton(r,text="Send reading",command=lambda a=suid,b=metric,c=e,d=unit:self.send(a,b,c,d)).pack(side="left",padx=10)

    def send(self,suid,metric,entry,unit):
        try: add_measurement(suid,metric,entry.get(),unit); entry.delete(0,"end"); self.refresh()
        except Exception as ex: messagebox.showerror("Measurement error",str(ex))

    def save_sensor_ui(self):
        try: save_sensor({k:e.get().strip() for k,e in self.fields.items()}); self.refresh(); messagebox.showinfo("Saved","Sensor/meter registered or updated.")
        except Exception as ex: messagebox.showerror("Sensor error",str(ex))

    def import_file(self):
        path=filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
        if path:
            try: n=import_csv(path); self.refresh(); messagebox.showinfo("Import complete",f"{n} rows imported.")
            except Exception as ex: messagebox.showerror("Import error",str(ex))

    def show(self,key):
        for f in self.frames.values(): f.pack_forget()
        self.frames[key].pack(fill="both",expand=True); self.refresh()

    def refresh(self):
        ss=list_sensors(); aa=list_alerts(); water,energy,cost,co2=sustainability_summary(); wf=latest("water_flow"); power=latest("power")
        vals=[f"Water Flow\n{wf['value']:.2f} {wf['unit']}" if wf else "Water Flow\n—",f"Power\n{power['value']:.2f} {power['unit']}" if power else "Power\n—",f"Total Cost\nR$ {cost:.2f}",f"Estimated CO₂e\n{co2:.2f} kg",f"Sensors\n{len(ss)}",f"Alerts\n{len(aa)}"]
        for c,v in zip(self.cards,vals): c.configure(text=v)
        self.dashboard_box.delete("1.0","end"); self.dashboard_box.insert("1.0","Physical Variable → Sensor / Meter → Device / Gateway → Connectivity → Measurement → SQLite → Analytics → Cost → CO₂e → Human Decision\n\nV5.1 adds sensor-to-measurement traceability without fixing one hardware model.")
        self.architecture_box.delete("1.0","end"); self.architecture_box.insert("1.0","Water Flow & Consumption → Electromagnetic or Ultrasonic Flow Meter\nElectrical Current → Current Transformer (CT)\nVoltage → Voltage Transducer\nPower & Energy → Multifunction Energy Meter\n\nCost = consumption × tariff (no physical sensor)\nEstimated CO₂e = kWh × documented emission factor (no direct sensor in this architecture)\n\nFinal hardware selection depends on range, accuracy, environment, interface, installation, calibration and safety requirements.")
        self.sensor_box.delete("1.0","end"); self.sensor_box.insert("1.0","\n\n".join(f"{s['sensor_uid']} — {s['sensor_type']}\nVariable: {s['measured_variable']} | Range: {s['measurement_range']} | Accuracy: {s['accuracy']}\nProtocol: {s['protocol']} | Installation: {s['installation_point']}\nStatus: {s['status']}" for s in ss))
        self.analytics_box.delete("1.0","end"); self.analytics_box.insert("1.0",f"Water consumption: {water:.2f} m³\nEnergy consumption: {energy:.2f} kWh\nTotal cost: R$ {cost:.2f}\nEstimated CO₂e: {co2:.2f} kg\n\nCost and CO₂e are calculated indicators.")
        self.alerts_box.delete("1.0","end"); self.alerts_box.insert("1.0","\n".join(f"{a['created_at']} | {a['severity']} | {a['sensor_uid']} | {a['message']}" for a in aa) or "No alerts.")
        self.history_box.delete("1.0","end"); self.history_box.insert("1.0","\n".join(f"{r['measured_at']} | {r['sensor_uid']} | {r['metric']} | {r['value']:.2f} {r['unit']} | {r['source']}" for r in history()) or "No measurements.")
