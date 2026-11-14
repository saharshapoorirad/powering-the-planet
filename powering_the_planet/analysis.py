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


def select_gdp_co2(co2):
    """Select GDP and CO₂ for three countries from 2000 to 2022."""
    countries = ["France", "Germany", "Italy"]

    country_rows = co2[co2["country"].isin(countries)]
    year_rows = country_rows[country_rows["year"].between(2000, 2022)]

    columns = ["country", "year", "gdp", "co2"]
    return year_rows[columns].copy()


def gdp_co2_percent_changes(gdp_co2):
    """Calculate GDP and CO₂ percentage changes from 2000 to 2022."""
    start = gdp_co2[gdp_co2["year"] == 2000].set_index("country")
    end = gdp_co2[gdp_co2["year"] == 2022].set_index("country")
    columns = ["gdp", "co2"]
    return (end[columns] - start[columns]) / start[columns] * 100


def years_gdp_up_co2_down(gdp_co2):
    """Find years when GDP rose and CO₂ fell compared with the previous year.

    Args:
        gdp_co2: A table with country, year, GDP, and CO₂ columns.

    Returns:
        A table of matching country-years and their GDP and CO₂
        percentage changes.
    """
    yearly = gdp_co2.sort_values(["country", "year"]).copy()

    yearly["gdp_change_pct"] = (
        yearly.groupby("country")["gdp"].pct_change() * 100
    )
    yearly["co2_change_pct"] = (
        yearly.groupby("country")["co2"].pct_change() * 100
    )

    both = (yearly["gdp_change_pct"] > 0) & (yearly["co2_change_pct"] < 0)
    columns = ["country", "year", "gdp_change_pct", "co2_change_pct"]
    return yearly.loc[both, columns]