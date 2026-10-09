"""CSV import helpers for Eco Data SP."""
import pandas as pd

REQUIRED_COLUMNS = {"reference_month", "value"}


def load_consumption_csv(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    return data
