import pandas as pd

#Just combining the two datasets into a single format

coffee = pd.read_csv("data/cooked/coffee_domestic_consumption_cooked.csv")
happiness = pd.read_csv("data/cleaned/happiness_2019_cleaned.csv")

coffee_2019 = coffee[coffee["year"] == 2019]

merged = coffee_2019.merge(happiness, on="country", how="inner")

merged.to_csv("data/cleaned/coffee_and_happiness_2019.csv", index=False)
print(merged.head())
