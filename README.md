# 🏠 UK House Price Analytics (1953–2024)

An end-to-end data analytics and machine learning project analysing UK house price trends using official Land Registry data. Includes data cleaning, SQL analysis, price forecasting, and an interactive Streamlit dashboard.

---

## 📊 Key Findings

- UK average house prices grew from **£1,891 in 1953** to over **£280,000 by 2024** — a 140x increase
- New properties consistently priced **higher** than older ones throughout the entire period
- Significant price slowdown visible around the **2008 financial crisis**
- Rapid post-COVID growth observed from **2020 onwards**
- Gradient Boosting model achieved **R² of 0.99+** predicting average prices from property type data
- Average annual growth rate used to forecast prices up to **2035**

---

## 🤖 Machine Learning

Three models trained to predict average UK house prices:

| Model | Features Used | Goal |
|---|---|---|
| Linear Regression | year, price_new, price_modern, price_older | Baseline |
| Random Forest | year, price_new, price_modern, price_older | Ensemble |
| Gradient Boosting | year, price_new, price_modern, price_older | Best model |

- Time-based train/test split: trained on pre-2015, tested on 2015–2024
- Future price forecasting uses historical average annual growth rate
- Model saved as `models/price_model.pkl`

---

## 🛠️ Tools & Skills Demonstrated

| Area | Tools |
|---|---|
| Data wrangling | Python, pandas |
| Database & SQL | SQLite |
| Machine Learning | scikit-learn (Linear Regression, Random Forest, Gradient Boosting) |
| Dashboard | Streamlit |
| Visualisation | matplotlib |
| Version control | Git, GitHub |

---

## 📁 Project Structure

```
uk-house-pricing/
│
├── data/
│   ├── raw/                  ← original downloaded CSV
│   └── processed/            ← cleaned CSV + SQLite database
│
├── src/
│   ├── download_data.py      ← downloads data from Land Registry
│   ├── data_cleaning.py      ← cleans and processes raw data
│   ├── database.py           ← loads data into SQLite
│   ├── analysis.py           ← SQL analysis + chart exports
│   └── model_training.py     ← trains and saves ML model
│
├── dashboard/
│   └── app.py                ← Streamlit interactive dashboard
│
├── models/
│   └── price_model.pkl       ← saved Gradient Boosting model
│
├── reports/
│   └── figures/              ← exported charts
│
└── README.md
```

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Sakshi220503/uk-house-price-analytics.git
cd uk-house-price-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline in order
python src/download_data.py
python src/data_cleaning.py
python src/database.py
python src/analysis.py
python src/model_training.py

# 4. Launch dashboard
streamlit run dashboard/app.py
```

---

## Dashboard Features

- KPI cards — average, max, min price and total records
- Price trend line chart — all property types over time
- Yearly average bar chart — with year range slider filter
- Price growth % chart — quarter-on-quarter change
- Price Predictor — forecast average UK house price up to 2035

---

## Data Source

**[HM Land Registry — UK House Price Index](https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-march-2024)** — official UK government open data.

*Data: Crown copyright. Contains HM Land Registry data licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).*

