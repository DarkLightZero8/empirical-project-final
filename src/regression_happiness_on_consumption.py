import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("data/cleaned/coffee_and_happiness_2019.csv")

# X = domestic coffee consumption
X = sm.add_constant(df["value"])

# y = happiness rank
y = df["happiness_rank"]

model = sm.OLS(y, X).fit()
print(model.summary())

corr = df["value"].corr(df["happiness_rank"])
print(f"The correlation between happiness rank and consumption of coffee is ", corr,".")
