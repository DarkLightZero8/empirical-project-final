import pandas as pd
import os

INPUT_FILES = [
    "coffee_domestic_consumption.csv",
    "coffee_production.csv",
    "coffee_export.csv",
    "coffee_import.csv",
    "coffee_importers_consumption.csv",
    "coffee_re_exports.csv"
]

RAW_DIR = "data/raw/coffee_datasets/"
OUT_DIR = "data/cooked/"
os.makedirs(OUT_DIR, exist_ok=True)

for file in INPUT_FILES:
    df = pd.read_csv(RAW_DIR + file)

    df.columns = [c.strip() for c in df.columns] 
    df = df.rename(columns={
        "Country": "country",
        "Coffee type": "coffee_type"
        })
    
    id_cols = ["country"]
    if "coffee_type" in df.columns:
        id_cols.append("coffee_type")

    year_cols = [
        c for c in df.columns 
        if (
            c not in id_cols 
            and "Total" not in c
            and (c.replace("/", "").isdigit())
            )
            ]

    long_df = df.melt(
        id_vars=id_cols,
        value_vars=year_cols,
        var_name="year_raw",
        value_name="value"
    )

    #Changing year format to make it neater. Some have the form 2012/13.
    #This can introduce inaccuracy in terms of time but it is neater.

    if "/" in year_cols[0]:  
        long_df["year"] = long_df["year_raw"].str.slice(0, 4).astype(int)
    else:  
        long_df["year"] = long_df["year_raw"].astype(int)

    # Drop missing values
    long_df = long_df.dropna(subset=["value"])

    # Save cooked file. Cause the original was raw. Could say roasted cause
    # it's coffee but that seems worse. Latte maybe?
    out_name = file.replace(".csv", "_cooked.csv")
    long_df.to_csv(OUT_DIR + out_name, index=False)

    print(f"Processed: {file} → {out_name}")
