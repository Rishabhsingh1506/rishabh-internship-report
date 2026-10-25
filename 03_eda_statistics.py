import pandas as pd

INPUT = "data/processed/agriculture_cleaned.csv"
OUT = "outputs/tables"

df = pd.read_csv(INPUT)

# Overall descriptive statistics
df.describe().T.to_csv(f"{OUT}/descriptive_statistics.csv")

# Commodity summary
commodity_summary = (
    df.groupby("commodity")
      .agg(
          records=("commodity","size"),
          avg_area_ha=("area_ha","mean"),
          total_production_mt=("production_million_tonnes","sum"),
          avg_yield_kg_ha=("yield_kg_ha","mean"),
          avg_modal_price=("modal_price_rs_quintal","mean")
      )
      .sort_values("total_production_mt", ascending=False)
)
commodity_summary.to_csv(f"{OUT}/commodity_summary.csv")

# State summary
state_summary = (
    df.groupby("state")
      .agg(
          records=("state","size"),
          total_production_mt=("production_million_tonnes","sum"),
          avg_yield_kg_ha=("yield_kg_ha","mean"),
          avg_modal_price=("modal_price_rs_quintal","mean")
      )
      .sort_values("total_production_mt", ascending=False)
)
state_summary.to_csv(f"{OUT}/state_summary.csv")

print("\nTop commodities by total production:")
print(commodity_summary.head())
print("\nTop states by total production:")
print(state_summary.head())
