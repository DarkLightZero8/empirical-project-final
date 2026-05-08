import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/coffee_and_happiness_2019.csv")

plt.figure(figsize=(8,6))
plt.scatter(df["value"], df["happiness_rank"])
plt.xlabel("Coffee Consumption (2019)")
plt.ylabel("Happiness Rank (2019)")
plt.title("Coffee Consumption vs Happiness Rank")
plt.gca().invert_yaxis()  # lower rank = happier
plt.show()
