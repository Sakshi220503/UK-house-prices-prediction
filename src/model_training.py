import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import os

def train_model():
    print("Loading dataset...")
    
    df = pd.read_csv("data/processed/cleaned_data.csv")
    print("Data loaded:", df.shape)
    print("Columns:", df.columns.tolist())

    # Fix column names
    df = df[["year", "price_all", "price_new", "price_modern", "price_older"]]
    df = df.dropna()
    print("After cleaning:", df.shape)

    # Features & target
    X = df[["year", "price_new", "price_modern", "price_older"]]
    y = df["price_all"]

    # Time based split
    X_train = X[df["year"] < 2015]
    X_test  = X[df["year"] >= 2015]
    y_train = y[df["year"] < 2015]
    y_test  = y[df["year"] >= 2015]

    print(f"Train: {len(X_train)} | Test: {len(X_test)}")

    # Train model
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model trained!")

    # Evaluate
    preds = model.predict(X_test)
    print(f"MAE: £{mean_absolute_error(y_test, preds):,.0f}")
    print(f"R²:  {r2_score(y_test, preds):.4f}")

    # Save model
    os.makedirs("models", exist_ok=True)
    with open("models/price_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved → models/price_model.pkl")

if __name__ == "__main__":
    train_model()