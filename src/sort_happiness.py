import pandas as pd
import os

df = pd.read_csv("data/raw/happiness_dataset/world-happiness-report-2019.csv")

df = df.rename(columns={
    "Country (region)": "country",
    "Ladder": "happiness_rank"
})

df = df[["country", "happiness_rank"]]
df["year"] = 2019

df.to_csv("data/cleaned/happiness_2019_cleaned.csv", index=False)
print(df.head())
