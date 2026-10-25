import pandas as pd

df = pd.read_csv("data/processed/agriculture_cleaned.csv")

top_commodity = (
    df.groupby("commodity")["production_million_tonnes"]
      .sum()
      .sort_values(ascending=False)
      .index[0]
)

top_state = (
    df.groupby("state")["production_million_tonnes"]
      .sum()
      .sort_values(ascending=False)
      .index[0]
)

highest_yield_state = (
    df.groupby("state")["yield_kg_ha"]
      .mean()
      .sort_values(ascending=False)
      .index[0]
)

price = df["modal_price_rs_quintal"]
print("AGRICULTURAL DATA ANALYSIS - KEY INSIGHTS")
print("-" * 50)
print(f"Highest total-production commodity: {top_commodity}")
print(f"Highest total-production state: {top_state}")
print(f"Highest average-yield state: {highest_yield_state}")
print(f"Average modal market price: Rs {price.mean():.2f}/quintal")
print(f"Median modal market price: Rs {price.median():.2f}/quintal")
print(f"Records analysed: {len(df):,}")
print("\nNote: The market dataset is a synthetic demonstration dataset.")
print("The report-aligned annual and rice/wheat files are based on values shown in the internship report.")
