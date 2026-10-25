import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = "data/raw/rice_wheat_comparison.csv"
OUT = Path("outputs/figures")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)

df["Rice_Change_pct"] = (
    (df.loc[1, "Rice_Production_million_tonnes"] /
     df.loc[0, "Rice_Production_million_tonnes"] - 1) * 100
)
df["Wheat_Change_pct"] = (
    (df.loc[1, "Wheat_Production_million_tonnes"] /
     df.loc[0, "Wheat_Production_million_tonnes"] - 1) * 100
)

long = df.melt(
    id_vars="Agricultural_Year",
    value_vars=["Rice_Production_million_tonnes", "Wheat_Production_million_tonnes"],
    var_name="Crop",
    value_name="Production_million_tonnes"
)
long["Crop"] = long["Crop"].str.replace("_Production_million_tonnes", "", regex=False)

plt.figure(figsize=(9,6))
for crop, group in long.groupby("Crop"):
    plt.plot(group["Agricultural_Year"], group["Production_million_tonnes"],
             marker="o", label=crop)
plt.title("Rice and Wheat Production Comparison")
plt.xlabel("Agricultural Year")
plt.ylabel("Production (million tonnes)")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "06_rice_wheat_comparison.png", dpi=200)
plt.close()

print(df)
