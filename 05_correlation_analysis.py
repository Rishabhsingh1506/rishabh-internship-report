import pandas as pd

INPUT = "data/processed/agriculture_cleaned.csv"
OUT = "outputs/tables/correlation_matrix.csv"

df = pd.read_csv(INPUT)

cols = [
    "area_ha", "production_million_tonnes", "yield_kg_ha",
    "modal_price_rs_quintal", "arrivals_tonnes"
]

corr = df[cols].corr(method="pearson")
corr.to_csv(OUT)

print("\nPearson correlation matrix:")
print(corr)
