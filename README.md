# Powering the Planet

An analysis of energy shares, CO₂ emissions, and GDP in France, Germany, and Italy using Our World in Data.

## Questions

1. How did fossil-fuel and renewable-energy shares change from 2000 to 2025?
2. How did total and per-person CO₂ emissions change from 2000 to 2024?
3. When did GDP rise while CO₂ emissions fell from 2000 to 2022?


## Data

The report uses two fixed versions of Our World in Data CSV files:

- `owid_energy.csv`: [energy data, version 2026-09-10](https://catalog.ourworldindata.org/garden/energy/2026-09-10/owid_energy/owid_energy.csv), for fossil-fuel and renewable-energy shares.
- `owid_co2.csv`: [CO₂ data, version 2026-11-10](https://catalog.ourworldindata.org/garden/emissions/2026-11-10/owid_co2/owid_co2.csv), for emissions, emissions per person, and GDP.

When a file is missing, `powering_the_planet/data.py` downloads it into `data/` automatically. Later runs reuse the local copy. These large CSV files are excluded from Git.

## Setup and run

Use Python 3.12. From a Terminal opened in this project's top folder, run:

```sh

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