import pandas as pd
import numpy as np

INPUT = "data/raw/agriculture_market_dataset.csv"
OUTPUT = "data/processed/agriculture_cleaned.csv"

df = pd.read_csv(INPUT)
print("Before cleaning:", df.shape)

# Standardise column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]+", "", regex=True)
)

# Parse dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Clean text fields
for col in ["state", "district_apmc", "commodity", "season"]:
    df[col] = df[col].astype("string").str.strip()

# Remove exact duplicates
df = df.drop_duplicates()

# Numeric conversion
numeric_cols = [
    "area_ha", "production_million_tonnes", "yield_kg_ha",
    "min_price_rs_quintal", "modal_price_rs_quintal",
    "max_price_rs_quintal", "arrivals_tonnes"
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill numeric missing values using median by commodity
for col in numeric_cols:
    df[col] = df.groupby("commodity")[col].transform(
        lambda s: s.fillna(s.median())
    )
    df[col] = df[col].fillna(df[col].median())

# Fill missing category values
df["district_apmc"] = df["district_apmc"].fillna("Unknown")

# Logical price correction
df["min_price_rs_quintal"] = np.minimum(
    df["min_price_rs_quintal"], df["modal_price_rs_quintal"]
)
df["max_price_rs_quintal"] = np.maximum(
    df["max_price_rs_quintal"], df["modal_price_rs_quintal"]
)

# Keep only valid non-negative analytical values
for col in numeric_cols:
    df.loc[df[col] < 0, col] = np.nan
    df[col] = df[col].fillna(df[col].median())

df.to_csv(OUTPUT, index=False)

print("After cleaning:", df.shape)
print("Remaining missing values:")
print(df.isna().sum())
print("Saved:", OUTPUT)
