from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def read_project_csv(filename):
    """Read a CSV from the project's data folder."""
    path = DATA_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Missing project data file: {path}")
    return pd.read_csv(path)


def load_energy():
    """Return the energy CSV as a pandas DataFrame."""
    return read_project_csv("owid_energy.csv")


def load_co2():
    """Return the CO₂ CSV as a pandas DataFrame."""
    return read_project_csv("owid_co2.csv")