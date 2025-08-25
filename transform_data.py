import pandas as pd
import glob
import os

data_path = "data/"
all_files = glob.glob(os.path.join(data_path, "daily_sales_data_*.csv"))


df_list = []

for file in all_files:
    df = pd.read_csv(file)
    df = df[df["product"] == "pink morsel"]  
    df["sales"] = df["quantity"] * df["price"]

    df = df[["sales", "date", "region"]]
    
    df_list.append(df)

final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv("data/formatted_sales_data.csv", index=False)

print("✅ Data transformation complete! Output saved to data/formatted_sales_data.csv")
