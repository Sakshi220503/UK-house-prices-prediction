import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/processed/housing.db")
df = pd.read_csv("../data/processed/cleaned_data.csv")
df.to_sql("housing", conn, if_exists="replace", index=False)
conn.close()
