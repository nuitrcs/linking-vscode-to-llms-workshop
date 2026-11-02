"""
Summarize the Palmer Penguins data by species.

For each species, print the number of penguins, their mean body mass in
kilograms, and the percentage that are female.
"""

import pandas as pd

# Read the data
df = pd.read_csv("penguins.csv")

# Keep only rows that have a body mass and a sex recorded
df = df.dropna(subset=["body_mass_g", "sex"])

# Convert body mass from grams to kilograms
df["body_mass_kg"] = df["body_mass_g"] / 100

print(f"{'species':<12}{'count':>7}{'mean mass (kg)':>17}{'% female':>11}")

for species, group in df.groupby("species"):
    n = len(group)
    mean_mass = group["body_mass_kg"].mean()
    percent_female = 100 * (group["sex"] == "female").sum() / n
    print(f"{species:<12}{n:>7}{mean_mass:>17.2f}{percent_female:>11.1f}")
