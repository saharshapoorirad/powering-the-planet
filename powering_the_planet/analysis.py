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