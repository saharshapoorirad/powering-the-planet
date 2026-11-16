def plot_energy_share(energy_mix, column, title):
    """Plot one energy-share measure over time for each country."""
    yearly = energy_mix.pivot(index="year", columns="country", values=column)

    ax = yearly.plot(figsize=(8, 5), title=title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of total energy (%)")
    ax.legend(title="Country")
    ax.grid(alpha=0.3)
    return ax


def plot_co2(co2_focus, column, title, y_label):
    """Plot a CO₂ measure over time for each country."""
    yearly = co2_focus.pivot(index="year", columns="country", values=column)

    ax = yearly.plot(figsize=(8, 5), title=title)
    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.legend(title="Country")
    ax.grid(alpha=0.3)
    return ax


def plot_gdp_co2_indexed(gdp_co2, country):
    """Plot one country's GDP and CO₂, with both set to 100 in 2000."""
    country_rows = gdp_co2[gdp_co2["country"] == country]
    yearly = country_rows.set_index("year")[["gdp", "co2"]].sort_index()

    indexed = yearly / yearly.loc[2000] * 100
    indexed = indexed.rename(columns={"gdp": "GDP", "co2": "CO₂"})

    ax = indexed.plot(
        figsize=(8, 5),
        title=f"{country}: GDP and CO₂ (2000 = 100)",
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Index (2000 = 100)")
    ax.grid(alpha=0.3)
    return ax


def plot_co2_intensity(intensity):
    """Plot CO₂ per unit of GDP for each country.

    Args:
        intensity: A table with country, year, and intensity_index.

    Returns:
        Matplotlib axes containing the line chart.
    """
    yearly = intensity.pivot(
        index="year", columns="country", values="intensity_index"
    )
    ax = yearly.plot(
        figsize=(8, 5),
        title="CO₂ per unit of GDP, 2000–2022",
    )
    ax.axhline(100, color="gray", linestyle="--", alpha=0.6)
    ax.set_xlabel("Year")
    ax.set_ylabel("Index (2000 = 100)")
    ax.legend(title="Country")
    ax.grid(alpha=0.3)
    return ax