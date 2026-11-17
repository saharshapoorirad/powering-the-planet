from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"

SOURCES = {
    "owid_energy.csv": "https://catalog.ourworldindata.org/garden/energy/2026-09-10/owid_energy/owid_energy.csv",
    "owid_co2.csv": "https://catalog.ourworldindata.org/garden/emissions/2026-11-10/owid_co2/owid_co2.csv",
}


def read_project_csv(filename):
    """Download a missing CSV, then return it as a pandas table."""
    path = DATA_DIR / filename

    if not path.is_file():
        DATA_DIR.mkdir(exist_ok=True)
        temporary = DATA_DIR / f"{filename}.part"

        try:
            print(f"Downloading {filename} from OWID...")
            urlretrieve(SOURCES[filename], temporary)
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)

    return pd.read_csv(path)


def load_energy():
    """Return the energy CSV as a pandas table."""
    return read_project_csv("owid_energy.csv")


def load_co2():
    """Return the CO₂ CSV as a pandas table."""
    return read_project_csv("owid_co2.csv")