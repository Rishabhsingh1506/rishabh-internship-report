import pandas as pd

INPUT = "data/raw/agriculture_market_dataset.csv"

df = pd.read_csv(INPUT)
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSummary statistics:")
print(df.describe(include="all").T)
