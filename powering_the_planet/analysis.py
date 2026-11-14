def select_energy_mix(energy):
    """Select energy shares for three countries from 2000 to 2025."""
    countries = ["France", "Germany", "Italy"]

    country_rows = energy[energy["country"].isin(countries)]
    year_rows = country_rows[country_rows["year"].between(2000, 2025)]

    columns = [
        "country",
        "year",
        "fossil_fuels_energy_share_pct",
        "renewables_energy_share_pct",
    ]
    return year_rows[columns].copy()


def energy_share_changes(energy_mix):
    """Calculate the 2000-to-2025 change in energy shares."""
    start = energy_mix[energy_mix["year"] == 2000].set_index("country")
    end = energy_mix[energy_mix["year"] == 2025].set_index("country")

    columns = [
        "fossil_fuels_energy_share_pct",
        "renewables_energy_share_pct",
    ]
    return end[columns] - start[columns]


def select_co2(co2):
    """Select CO₂ data for three countries from 2000 to 2024."""
    countries = ["France", "Germany", "Italy"]

    country_rows = co2[co2["country"].isin(countries)]
    year_rows = country_rows[country_rows["year"].between(2000, 2024)]

    columns = ["country", "year", "co2", "co2_per_capita"]
    return year_rows[columns].copy()


def co2_percent_changes(co2_focus):
    """Calculate each country's CO₂ percentage change, 2000 to 2024."""
    start = co2_focus[co2_focus["year"] == 2000].set_index("country")
    end = co2_focus[co2_focus["year"] == 2024].set_index("country")

    columns = ["co2", "co2_per_capita"]
    return (end[columns] - start[columns]) / start[columns] * 100