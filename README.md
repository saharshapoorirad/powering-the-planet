# Powering the Planet

An analysis of energy shares, CO₂ emissions, and GDP in France, Germany, and Italy using Our World in Data.

## Questions

1. How did fossil-fuel and renewable-energy shares change from 2000 to 2025?
2. How did total and per-person CO₂ emissions change from 2000 to 2024?
3. When did GDP rise while CO₂ emissions fell from 2000 to 2022?


## Data

The report reads two Our World in Data CSV files from the `data/` folder:

- `owid_energy.csv`: [OWID energy catalog CSV](https://catalog.ourworldindata.org/energy/owid_energy/owid_energy.csv), used for fossil-fuel and renewable-energy shares.
- `owid_co2.csv`: [OWID CO₂ CSV](https://owid-public.owid.io/data/co2/owid-co2-data.csv), used for CO₂ emissions, emissions per person, and GDP.

These large downloaded files are excluded from Git. The setup commands below download them. OWID updates its data, so a later download may give different results.

## Setup and run

Use Python 3.12. From a Terminal opened in this project's top folder, run:

```sh
mkdir -p data
curl --fail --location "https://catalog.ourworldindata.org/energy/owid_energy/owid_energy.csv" --output data/owid_energy.csv
curl --fail --location "https://owid-public.owid.io/data/co2/owid-co2-data.csv" --output data/owid_co2.csv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open `report.ipynb` in VS Code, choose the Python kernel inside `.venv`, then click **Restart** and **Run All**.


## Project files

- `report.ipynb` — the final notebook with calculations, charts, and explanations.
- `powering_the_planet/data.py` — loads the two CSV files.
- `powering_the_planet/analysis.py` — selects countries and years and calculates changes.
- `powering_the_planet/plots.py` — defines the chart functions.
- `powering_the_planet/__init__.py` — marks the folder as a Python package.
- `requirements.txt` — lists the Python packages needed to run the notebook.
- `.gitignore` — tells Git to skip local downloads and generated files.

## Results at a glance

In France, Germany, and Italy, renewable-energy shares rose and fossil-fuel shares fell from 2000 to 2025. Annual CO₂ emissions fell from 2000 to 2024; GDP rose while CO₂ emissions fell from 2000 to 2022.

The GDP data are measured in international dollars at 2011 prices and end in 2022. See [the report](report.ipynb) for the exact results, charts, and limitations.