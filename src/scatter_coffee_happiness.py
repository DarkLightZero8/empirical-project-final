import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/coffee_and_happiness_2019.csv")
# Convert to billions
df["value_billion"] = df["value"] / 1_000_000_000

plt.figure(figsize=(8,6))
plt.scatter(df["value_billion"], df["happiness_rank"])
plt.xlabel("Coffee Consumption (Billion Kg, 2019)")
plt.ylabel("Happiness Rank (2019)")
plt.title("Coffee Consumption vs Happiness Rank")
plt.gca().invert_yaxis()  # lower rank = happier
plt.show()
