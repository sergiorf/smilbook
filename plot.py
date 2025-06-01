import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def compute_correlation(country_timeseries, gdp_timeseries, country):
    """
    Compute Pearson correlation between energy use and GDP per capita for a country.
    """
    energy = dict(country_timeseries.get(country, []))
    gdp = dict(gdp_timeseries.get(country, []))
    years = sorted(set(energy.keys()) & set(gdp.keys()))
    if not years:
        print(f"No overlapping years for {country}")
        return None
    energy_values = [energy[y] for y in years]
    gdp_values = [gdp[y] for y in years]
    if len(energy_values) < 2 or len(gdp_values) < 2:
        print(f"Not enough data for correlation for {country}")
        return None
    corr = np.corrcoef(energy_values, gdp_values)[0, 1]
    return corr

def plot_energy_and_gdp(country_timeseries, gdp_timeseries, countries, gdp_countries=None, interpolate=True):
    """
    Plot energy use (left axis) and GDP per capita (right axis) for one or more countries.
    Prints the correlation coefficient for each country on the plot.
    """
    plt.figure(figsize=(12, 6))
    ax1 = plt.gca()
    ax2 = ax1.twinx()

    # Plot energy use
    for country in countries:
        series = country_timeseries.get(country, [])
        if not series:
            print(f"No energy data for {country}")
            continue
        years, values = zip(*series) if series else ([], [])
        s = pd.Series(values, index=years)
        all_years = range(min(years), max(years) + 1)
        s = s.reindex(all_years)
        if interpolate:
            s = s.interpolate()
        ax1.plot(s.index, s.values, marker='o', label=f"{country} (Energy)")

    # Plot GDP per capita
    if gdp_countries is None:
        gdp_countries = countries
    for country in gdp_countries:
        series = gdp_timeseries.get(country, [])
        if not series:
            print(f"No GDP data for {country}")
            continue
        years, values = zip(*series) if series else ([], [])
        s = pd.Series(values, index=years)
        all_years = range(min(years), max(years) + 1)
        s = s.reindex(all_years)
        if interpolate:
            s = s.interpolate()
        ax2.plot(s.index, s.values, marker='x', linestyle='--', label=f"{country} (GDP)")

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Energy use (kg of oil equivalent per capita)')
    ax2.set_ylabel('GDP per capita, PPP (constant 2021 international $)')
    ax1.grid(True)

    # Compute and print correlation for each country
    corr_texts = []
    for country in countries:
        corr = compute_correlation(country_timeseries, gdp_timeseries, country)
        if corr is not None:
            corr_texts.append(f"{country}: r = {corr:.2f}")
    if corr_texts:
        ax1.text(0.5, 1.05, " | ".join(corr_texts), transform=ax1.transAxes, ha='center', va='bottom', fontsize=12, color='darkred')

    ax1.set_title('Energy use (kg of oil equivalent per capita) and GDP per capita, PPP (constant 2021 international $)')
    # Combine legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')
    plt.tight_layout()
    plt.show()

# --- Load energy use data ---
df_energy = pd.read_csv("API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_88954.csv", skiprows=4)
df_energy = df_energy.dropna(axis=1, how='all')
years = [col for col in df_energy.columns if col.isdigit()]
country_timeseries = {}
for _, row in df_energy.iterrows():
    country = row['Country Name']
    series = []
    for year in years:
        value = row[year]
        if pd.notna(value) and value != '':
            series.append((int(year), float(value)))
    country_timeseries[country] = series

# --- Load GDP per capita data ---
df_gdp = pd.read_csv("API_NY.GDP.PCAP.PP.KD_DS2_en_csv_v2_86973.csv", skiprows=4)
df_gdp = df_gdp.dropna(axis=1, how='all')
gdp_years = [col for col in df_gdp.columns if col.isdigit()]
gdp_timeseries = {}
for _, row in df_gdp.iterrows():
    country = row['Country Name']
    series = []
    for year in gdp_years:
        value = row[year]
        if pd.notna(value) and value != '':
            series.append((int(year), float(value)))
    gdp_timeseries[country] = series

# --- Western European countries (edit this list as needed to match your dataset) ---
western_europe = [
    'Austria', 'Belgium', 'France', 'Germany', 'Netherlands', 'Switzerland',
    'Luxembourg', 'United Kingdom', 'Ireland', 'Denmark', 'Norway', 'Sweden', 'Finland', 'Italy', 'Spain', 'Portugal'
]

# --- Compute average time series for energy use ---
data_energy = []
for country in western_europe:
    series = dict(country_timeseries.get(country, []))
    row = [series.get(int(year), np.nan) for year in years]
    data_energy.append(row)
df_west_energy = pd.DataFrame(data_energy, index=western_europe, columns=[int(y) for y in years])
avg_series_energy = df_west_energy.mean(axis=0, skipna=True)
avg_timeseries_energy = [(year, value) for year, value in avg_series_energy.items() if not np.isnan(value)]
country_timeseries["Western Europe (avg)"] = avg_timeseries_energy

# --- Compute average time series for GDP per capita ---
data_gdp = []
for country in western_europe:
    series = dict(gdp_timeseries.get(country, []))
    row = [series.get(int(year), np.nan) for year in years]
    data_gdp.append(row)
df_west_gdp = pd.DataFrame(data_gdp, index=western_europe, columns=[int(y) for y in years])
avg_series_gdp = df_west_gdp.mean(axis=0, skipna=True)
avg_timeseries_gdp = [(year, value) for year, value in avg_series_gdp.items() if not np.isnan(value)]
gdp_timeseries["Western Europe (avg)"] = avg_timeseries_gdp

plot_energy_and_gdp(
    country_timeseries,
    gdp_timeseries,
   ['India', 'Bangladesh']
 #['United States', 'Western Europe (avg)']
 #['Spain', 'Poland']
 #['Brazil', 'China']
)