# lessons/random_forest_duration.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1️⃣ Dataset Load
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# 2️⃣ Duration clean করা (minutes বের করা)
def extract_minutes(x):
    if "min" in str(x):
        return int(x.split(" ")[0])
    else:
        return np.nan

df["duration_minutes"] = df["duration"].apply(extract_minutes)

# 3️⃣ Missing values drop
df = df.dropna(subset=["duration_minutes"])

# Features (X) আর Target (y)
X = pd.get_dummies(df[["release_year"]], drop_first=True)  
y = df["duration_minutes"]

# 4️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# 6️⃣ Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R² Score:", r2)

# 7️⃣ Visualization
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.5, color="blue")
plt.xlabel("Actual Duration (minutes)")
plt.ylabel("Predicted Duration (minutes)")
plt.title("Random Forest Regression - Netflix Duration Prediction")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()
