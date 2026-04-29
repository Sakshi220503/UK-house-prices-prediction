import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../data/processed/cleaned_data.csv")
yearly = df.groupby("year")["price"].mean().reset_index()

X = yearly[["year"]]
y = yearly["price"]

model = LinearRegression()
model.fit(X, y)

future = pd.DataFrame({"year": range(yearly.year.max(), yearly.year.max()+5)})
preds = model.predict(future)

print(preds)
