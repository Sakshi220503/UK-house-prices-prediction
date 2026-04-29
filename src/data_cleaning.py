import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

input_path = os.path.join(BASE_DIR, "data/raw/uk_house_prices.csv")
output_path = os.path.join(BASE_DIR, "data/processed/cleaned_data.csv")

df = pd.read_csv(input_path)

print("Columns:", df.columns)

# Rename columns (clean names)
df = df.rename(columns={
    "Price (All)": "price_all",
    "Price (New)": "price_new",
    "Price (Modern)": "price_modern",
    "Price (Older)": "price_older"
})

# Convert date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["year"] = df["Date"].dt.year

# Drop rows where main price missing
df = df.dropna(subset=["price_all"])

# Save cleaned file
df.to_csv(output_path, index=False)

print("✅ Cleaned data saved!")