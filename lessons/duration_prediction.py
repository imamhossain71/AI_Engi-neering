import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# CSV load
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# শুধু Movies এবং duration_minute প্রাসঙ্গিক columns রাখছি
df = df[df['type'] == 'Movie']

# duration থেকে ' min' remove & numeric
df['duration_minute'] = df['duration'].str.replace(' min', '')

# Drop rows where duration_minute is NaN or empty
df = df[df['duration_minute'].notna() & (df['duration_minute'] != '')]

# Convert to float
df['duration_minute'] = df['duration_minute'].astype(float)

# Features & Target
X = df[['release_year']]
y = df['duration_minute']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)

# Optional: show few predictions
result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(result.head(10))
