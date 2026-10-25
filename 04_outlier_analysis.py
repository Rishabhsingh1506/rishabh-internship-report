import pandas as pd

INPUT = "data/processed/agriculture_cleaned.csv"
OUT = "outputs/tables/outlier_summary.csv"

df = pd.read_csv(INPUT)

cols = [
    "area_ha", "production_million_tonnes", "yield_kg_ha",
    "modal_price_rs_quintal", "arrivals_tonnes"
]

results = []
for col in cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)
    results.append({
        "variable": col,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "lower_bound": lower,
        "upper_bound": upper,
        "outlier_count": int(mask.sum())
    })

result = pd.DataFrame(results)
result.to_csv(OUT, index=False)
print(result)
