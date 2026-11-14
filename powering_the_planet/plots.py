def plot_energy_share(energy_mix, column, title):
    """Plot one energy-share measure over time for each country."""
    yearly = energy_mix.pivot(index="year", columns="country", values=column)

    ax = yearly.plot(figsize=(8, 5), title=title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of total energy (%)")
    ax.legend(title="Country")
    ax.grid(alpha=0.3)
    return ax

