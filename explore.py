import pandas as pd
df = pd.read_csv("data/mlb_bat_tracking_2024_2025.csv")
print(df.columns)
print(df.head())
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df.describe())