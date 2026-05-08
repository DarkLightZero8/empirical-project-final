import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cooked/coffee_domestic_consumption_cooked.csv")

# Compute total consumption across all years, because it's easier
totals = df.groupby("country")["value"].sum().sort_values(ascending=False)

top5_countries = totals.head(5).index.tolist()

df_top5 = df[df["country"].isin(top5_countries)].copy()

# Convert units to billions
df_top5["value_billion"] = df_top5["value"] / 1_000_000_000

plt.figure(figsize=(12, 7))

# Plot top 5
for c in top5_countries:
    subset = df_top5[df_top5["country"] == c]
    plt.plot(subset["year"], subset["value_billion"], label=f"Top: {c}", linewidth=2)

plt.title("Top 5 Coffee Consumers Over Time (In Billions of Kg)")
plt.xlabel("Year")
plt.ylabel("Domestic Consumption (Billion Kg)")
plt.legend()
plt.tight_layout()
plt.show()
