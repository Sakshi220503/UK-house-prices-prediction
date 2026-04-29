# UK House Price Analytics

## Live Dashboard
Run locally:
streamlit run dashboard/app.py

## Setup
pip install -r requirements.txt

## Run Pipeline
python src/download_data.py
python src/data_cleaning.py
python src/database.py
python src/analysis.py
