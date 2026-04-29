import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../data/processed/housing.db")

query = '''
SELECT town_city, AVG(price) as avg_price
FROM housing
GROUP BY town_city
ORDER BY avg_price DESC
LIMIT 10
'''

df = pd.read_sql(query, conn)

plt.figure()
plt.bar(df['town_city'], df['avg_price'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../reports/figures/top_cities.png")
