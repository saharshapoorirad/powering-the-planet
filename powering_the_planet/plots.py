def plot_energy_mix_endpoints(energy_mix):
    """Compare five energy-source shares in 2000 and 2025."""
    sources = {
        "coal_energy_share_pct": "Coal",
        "oil_energy_share_pct": "Oil",
        "gas_energy_share_pct": "Gas",
        "nuclear_energy_share_pct": "Nuclear",
        "renewables_energy_share_pct": "Renewables",
    }
    endpoints = energy_mix[energy_mix["year"].isin([2000, 2025])]
    shares = (
        endpoints.sort_values(["country", "year"])
        .set_index(["country", "year"])[list(sources)]
        .rename(columns=sources)
    )

    ax = shares.plot.bar(
        stacked=True,
        figsize=(10, 5),
        color=["#555555", "#a8a8a8", "#ed9b40", "#8064a2", "#4ca564"],
        title="Energy sources in France, Germany, and Italy: 2000 vs 2025",
    )
    ax.set_xticklabels(
        [f"{country}\n{year}" for country, year in shares.index], rotation=0
    )
    ax.set_xlabel("")
    ax.set_ylabel("Share of total energy (%)")
    ax.set_ylim(0, 105)
    ax.legend(title="Energy source", bbox_to_anchor=(1.02, 1), loc="upper left")
    ax.figure.tight_layout()
    return ax


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