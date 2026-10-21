import customtkinter as ctk
from tkinter import filedialog, messagebox
from services.core import *
from services.csv_service import import_csv
ctk.set_appearance_mode("light")
class App(ctk.CTk):
    def __init__(self):
        super().__init__(); self.title("Eco Data SP — Sustainability Platform | V5.2"); self.geometry("1580x920"); self.minsize(1250,780)
        self.grid_columnconfigure(1,weight=1); self.grid_rowconfigure(0,weight=1); self.frames={}; self._build(); self.show("dashboard")
    def _base(self,key,title,subtitle):
        f=ctk.CTkFrame(self.content,fg_color="#F4F8FB"); ctk.CTkLabel(f,text=title,font=("Arial",28,"bold"),text_color="#082E46").pack(anchor="w",padx=30,pady=(25,2)); ctk.CTkLabel(f,text=subtitle,text_color="#55717F").pack(anchor="w",padx=30,pady=(0,15)); self.frames[key]=f; return f
    def _info(self,key,title,subtitle,initial=""):
        f=self._base(key,title,subtitle); b=ctk.CTkTextbox(f,font=("Consolas",14)); b.pack(fill="both",expand=True,padx=30,pady=10); b.insert("1.0",initial); setattr(self,key+"_box",b)
    def _build(self):
        s=ctk.CTkFrame(self,width=250,corner_radius=0,fg_color="#082E46"); s.grid(row=0,column=0,sticky="nsew")
        ctk.CTkLabel(s,text="ECO DATA SP",font=("Arial",22,"bold"),text_color="white").pack(pady=(28,2)); ctk.CTkLabel(s,text="V5.2 • Hardware Selection",text_color="#B9D7E8").pack(pady=(0,20))
        self.content=ctk.CTkFrame(self,corner_radius=0,fg_color="#F4F8FB"); self.content.grid(row=0,column=1,sticky="nsew")
        self._dashboard(); self._info("industrial","Sensor Integration Architecture","Possible examples — final hardware depends on deployment requirements.","Physical Variable → Sensor / Meter → Device / Gateway → Connectivity → Measurement → Eco Data SP")
        self._hardware(); self._sensors(); self._live(); self._info("analytics","Costs & CO₂e","Calculated indicators — not physical sensors"); self._info("alerts","Alerts","Threshold events with sensor provenance"); self._info("history","Measurement History","Sensor → measurement traceability")
        for label,key in [("Dashboard","dashboard"),("Sensor Integration","industrial"),("Hardware Selection","hardware"),("Sensors & Meters","sensors"),("Water & Energy","live"),("Costs & CO₂e","analytics"),("Alerts","alerts"),("History","history")]:
            ctk.CTkButton(s,text=label,anchor="w",fg_color="transparent",hover_color="#164B66",command=lambda k=key:self.show(k)).pack(fill="x",padx=15,pady=4)
        ctk.CTkButton(s,text="Import CSV",anchor="w",fg_color="transparent",hover_color="#164B66",command=self.import_file).pack(fill="x",padx=15,pady=4)
    def _dashboard(self):
        f=self._base("dashboard","Sustainability Overview","V5.2 — Hardware Selection Study"); row=ctk.CTkFrame(f,fg_color="transparent"); row.pack(fill="x",padx=25); self.cards=[]
        for label in ["Water Flow\n—","Power\n—","Total Cost\nR$ 0.00","Estimated CO₂e\n0.00 kg","Sensors\n0","Alerts\n0"]:
            c=ctk.CTkLabel(row,text=label,width=180,height=100,fg_color="white",corner_radius=12,font=("Arial",14,"bold")); c.pack(side="left",padx=4); self.cards.append(c)
        self.dashboard_box=ctk.CTkTextbox(f,font=("Consolas",14)); self.dashboard_box.pack(fill="both",expand=True,padx=30,pady=20)
    def _hardware(self):
        f=self._base("hardware","Hardware Selection Study","Official manufacturer references • no prices • candidates, not final selections"); top=ctk.CTkFrame(f,fg_color="transparent"); top.pack(fill="x",padx=30,pady=(0,8))
        ctk.CTkLabel(top,text="Domain",font=("Arial",13,"bold")).pack(side="left",padx=(0,8)); self.hardware_domain=ctk.CTkOptionMenu(top,values=["ALL","WATER","ENERGY"],command=lambda _=None:self.refresh_hardware()); self.hardware_domain.pack(side="left")
        self.hardware_summary=ctk.CTkLabel(top,text="",font=("Arial",13,"bold"),text_color="#082E46"); self.hardware_summary.pack(side="right"); self.hardware_box=ctk.CTkTextbox(f,font=("Consolas",12),wrap="word"); self.hardware_box.pack(fill="both",expand=True,padx=30,pady=(4,12))
    def refresh_hardware(self):
        if not hasattr(self,"hardware_box"): return
        rows=list_hardware_candidates(self.hardware_domain.get()); summary=hardware_study_summary(); self.hardware_summary.configure(text=f"Candidates: {summary['total']} | Water: {summary['water']} | Energy: {summary['energy']}")
        blocks=[f"[{r['domain']}] {r['manufacturer']} — {r['model']}\nType: {r['instrument_type']}\nMeasures: {r['measured_variables']}\nRange: {r['measurement_range']}\nAccuracy: {r['accuracy']}\nCommunication: {r['communication']}\nApplication: {r['application']}\nEco Data SP integration: {r['integration_path']}\nFit: {r['eco_fit']} | Status: {r['status']}\nOfficial source: {r['official_source']}\nEvidence: {r['evidence_note']}" for r in rows]
        self.hardware_box.delete("1.0","end"); self.hardware_box.insert("1.0","CANDIDATE SHORTLIST — NOT FINAL HARDWARE SELECTION\nNo prices. Final selection requires site-specific engineering.\n\n"+"\n\n".join(blocks))
    def _sensors(self):
        f=self._base("sensors","Industrial Sensors","Technical metadata + measurement provenance"); self.sensor_box=ctk.CTkTextbox(f,font=("Consolas",12)); self.sensor_box.pack(fill="both",expand=True,padx=30,pady=10)
    def _live(self):
        f=self._base("live","Water & Energy Measurements","Readings linked to registered sensor/meter examples")
        for suid,metric,label,unit in [("FLOW-IND-001","water_flow","Water flow","L/min"),("FLOW-IND-001","water_consumption","Water consumption","m³"),("CT-IND-001","electrical_current","Electrical current","A"),("VOLT-IND-001","voltage","Voltage","V"),("METER-IND-001","power","Electrical power","kW"),("METER-IND-001","energy_consumption","Energy consumption","kWh")]:
            r=ctk.CTkFrame(f,fg_color="white"); r.pack(fill="x",padx=30,pady=4); ctk.CTkLabel(r,text=f"{label} — {suid}",width=360,anchor="w").pack(side="left",padx=12,pady=13); e=ctk.CTkEntry(r,width=150,placeholder_text="Enter value"); e.pack(side="left"); ctk.CTkButton(r,text="Send reading",command=lambda a=suid,b=metric,c=e,d=unit:self.send(a,b,c,d)).pack(side="left",padx=10)
    def send(self,suid,metric,entry,unit):
        try: add_measurement(suid,metric,entry.get(),unit); entry.delete(0,"end"); self.refresh()
        except Exception as ex: messagebox.showerror("Measurement error",str(ex))
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
        self.dashboard_box.delete("1.0","end"); self.dashboard_box.insert("1.0","V5.2 HARDWARE SELECTION STUDY\n\nPhysical Variable → Industrial Instrument → Modbus / Industrial Ethernet / Gateway → Eco Data SP → SQLite → Analytics → Cost → Estimated CO₂e → Human Decision\n\nResearch candidates are backed by official manufacturer documentation. Final selection remains deployment-specific.")
        self.refresh_hardware(); self.sensor_box.delete("1.0","end"); self.sensor_box.insert("1.0","\n\n".join(f"{s['sensor_uid']} — {s['sensor_type']}\nVariable: {s['measured_variable']} | Range: {s['measurement_range']} | Protocol: {s['protocol']}\nReason: {s['selection_reason']}\nSafety: {s['safety_notes']}" for s in ss))
        self.analytics_box.delete("1.0","end"); self.analytics_box.insert("1.0",f"Water consumption: {water:.2f} m³\nEnergy consumption: {energy:.2f} kWh\nTotal cost: R$ {cost:.2f}\nEstimated CO₂e: {co2:.2f} kg\n\nCost and CO₂e are calculated indicators.")
        self.alerts_box.delete("1.0","end"); self.alerts_box.insert("1.0","\n".join(f"{a['created_at']} | {a['severity']} | {a['sensor_uid']} | {a['message']}" for a in aa) or "No alerts.")
        self.history_box.delete("1.0","end"); self.history_box.insert("1.0","\n".join(f"{r['measured_at']} | {r['sensor_uid']} | {r['metric']} | {r['value']:.2f} {r['unit']} | {r['source']}" for r in history()) or "No measurements.")
