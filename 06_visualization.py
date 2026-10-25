import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = "data/processed/agriculture_cleaned.csv"
OUT = Path("outputs/figures")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)
df["date"] = pd.to_datetime(df["date"])

# 1. Production by commodity
commodity = (
    df.groupby("commodity")["production_million_tonnes"]
      .sum()
      .sort_values(ascending=False)
)
plt.figure(figsize=(10,6))
commodity.plot(kind="bar")
plt.title("Total Production by Commodity")
plt.xlabel("Commodity")
plt.ylabel("Production (million tonnes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "01_production_by_commodity.png", dpi=200)
plt.close()

# 2. Monthly modal price trend
monthly = df.groupby("date")["modal_price_rs_quintal"].mean()
plt.figure(figsize=(10,6))
monthly.plot(kind="line", marker="o")
plt.title("Average Monthly Modal Price Trend")
plt.xlabel("Month")
plt.ylabel("Modal Price (Rs/quintal)")
plt.tight_layout()
plt.savefig(OUT / "02_monthly_modal_price_trend.png", dpi=200)
plt.close()

# 3. Yield by state
state_yield = (
    df.groupby("state")["yield_kg_ha"]
      .mean()
      .sort_values(ascending=False)
)
plt.figure(figsize=(10,6))
state_yield.plot(kind="bar")
plt.title("Average Yield by State")
plt.xlabel("State")
plt.ylabel("Yield (kg/ha)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "03_average_yield_by_state.png", dpi=200)
plt.close()

# 4. Production vs yield
plt.figure(figsize=(9,6))
plt.scatter(df["yield_kg_ha"], df["production_million_tonnes"], alpha=0.5)
plt.title("Production vs Yield")
plt.xlabel("Yield (kg/ha)")
plt.ylabel("Production (million tonnes)")
plt.tight_layout()
plt.savefig(OUT / "04_production_vs_yield.png", dpi=200)
plt.close()

# 5. Price distribution
plt.figure(figsize=(9,6))
plt.hist(df["modal_price_rs_quintal"], bins=30)
plt.title("Distribution of Modal Market Price")
plt.xlabel("Modal Price (Rs/quintal)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUT / "05_modal_price_distribution.png", dpi=200)
plt.close()

print("Charts saved to outputs/figures/")
