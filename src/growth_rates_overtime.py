import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cooked/coffee_domestic_consumption_cooked.csv")

# Sort
df = df.sort_values(["country", "year"])

# Compute growth
df["yoy_growth"] = df.groupby("country")["value"].pct_change()

# Top 5 all-time consumers
totals = df.groupby("country")["value"].sum().sort_values(ascending=False)
top5 = totals.head(5).index.tolist()

plt.figure(figsize=(12, 7))

for c in top5:
    subset = df[df["country"] == c]
    plt.plot(subset["year"], subset["yoy_growth"], label=c)

plt.title("Year-on-Year Growth Rates for Top 5 Coffee Consumers")
plt.xlabel("Year")
plt.ylabel("Growth Rate")
plt.legend()
plt.tight_layout()
plt.show()
