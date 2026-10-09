"""Central configuration for Eco Data SP."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "eco_data.db"
EXPORTS_DIR = BASE_DIR / "exports"
SAMPLE_DATA_DIR = BASE_DIR / "sample_data"
APP_NAME = "Eco Data SP"
APP_VERSION = "0.1.0"
