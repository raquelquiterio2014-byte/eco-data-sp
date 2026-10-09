"""SQLite initialization for the Eco Data SP MVP."""
import sqlite3
from config import DATABASE_DIR, DATABASE_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS organizations (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS units (id INTEGER PRIMARY KEY AUTOINCREMENT, organization_id INTEGER NOT NULL, name TEXT NOT NULL, FOREIGN KEY (organization_id) REFERENCES organizations(id));
CREATE TABLE IF NOT EXISTS water_consumption (id INTEGER PRIMARY KEY AUTOINCREMENT, unit_id INTEGER NOT NULL, reference_month TEXT NOT NULL, consumption_m3 REAL NOT NULL CHECK (consumption_m3 >= 0), cost REAL CHECK (cost >= 0), FOREIGN KEY (unit_id) REFERENCES units(id));
CREATE TABLE IF NOT EXISTS energy_consumption (id INTEGER PRIMARY KEY AUTOINCREMENT, unit_id INTEGER NOT NULL, reference_month TEXT NOT NULL, consumption_kwh REAL NOT NULL CHECK (consumption_kwh >= 0), cost REAL CHECK (cost >= 0), FOREIGN KEY (unit_id) REFERENCES units(id));
CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY AUTOINCREMENT, unit_id INTEGER NOT NULL, metric TEXT NOT NULL, target_value REAL NOT NULL, target_date TEXT, FOREIGN KEY (unit_id) REFERENCES units(id));
CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY AUTOINCREMENT, unit_id INTEGER NOT NULL, metric TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (unit_id) REFERENCES units(id));
"""


def initialize_database() -> None:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(SCHEMA)
