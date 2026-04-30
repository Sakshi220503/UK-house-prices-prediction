import streamlit as st
import pandas as pd
import os
import pickle

# Page config
st.set_page_config(page_title="UK Housing Dashboard", layout="wide")

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(BASE_DIR, "data/processed/cleaned_data.csv")
df = pd.read_csv(data_path)

df["Date"] = pd.to_datetime(df["Date"])
with open("models/price_model.pkl", "rb") as f:
    model = pickle.load(f)
# =========================
# SIDEBAR (Filters)
# =========================
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)

filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# =========================
# TITLE
# =========================
st.title("UK Housing Market Dashboard")

# =========================
# KPI SECTION
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Price", f"£{int(filtered['price_all'].mean()):,}")
col2.metric("Max Price", f"£{int(filtered['price_all'].max()):,}")
col3.metric("Min Price", f"£{int(filtered['price_all'].min()):,}")
col4.metric("Records", len(filtered))

st.markdown("---")

# =========================
# CHART 1 — PRICE TREND
# =========================
st.subheader("House Price Trends")

st.line_chart(
    filtered.set_index("Date")[[
        "price_all",
        "price_new",
        "price_modern",
        "price_older"
    ]]
)

# =========================
# CHART 2 — YEARLY AVG
# =========================
st.subheader("Average Price by Year")

yearly = filtered.groupby("year")["price_all"].mean()
st.bar_chart(yearly)

# =========================
# CHART 3 — GROWTH
# =========================
st.subheader("Price Growth (%)")

filtered["growth"] = filtered["price_all"].pct_change() * 100
st.line_chart(filtered.set_index("Date")["growth"])

st.markdown("---")

# =========================
# DATA TABLE
# =========================
st.subheader("Filtered Data")
st.dataframe(filtered)

# =========================
# INSIGHTS
# =========================
st.subheader("Key Insights")

st.write("""
- UK house prices show strong long-term upward trends
- Significant slowdown around 2008 financial crisis
- Rapid growth observed post-2020
- New properties generally priced higher than older ones
""")
st.markdown("---")
st.subheader("🤖 Predict Future House Prices")
future_year = st.slider("Select future year", 2025, 2035)

# Calculate average annual growth rate from last 10 years of data
recent = df[df["year"] >= df["year"].max() - 10]
avg_growth = recent["price_all"].pct_change().mean()

# Last known average price and year
last_price = df["price_all"].dropna().iloc[-1]
last_year  = int(df["year"].dropna().iloc[-1])

# Project forward
years_ahead    = future_year - last_year
predicted_price = last_price * ((1 + avg_growth) ** years_ahead)

st.metric(
    f"Predicted Average UK House Price in {future_year}",
    f"£{int(predicted_price):,}",
    delta=f"{((predicted_price - last_price) / last_price * 100):.1f}% from {last_year}"
)

st.caption(f"Based on {avg_growth*100:.2f}% average annual growth rate (last 10 years of data)")