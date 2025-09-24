import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")
df = df[df['type']=='Movie'].copy()

# Duration clean & NaN drop
df['duration'] = df['duration'].str.replace(' min', '', regex=False)
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
df = df[df['duration'].notna()]

features = df[['release_year','country','listed_in']].fillna('Unknown')
target = df['duration']

# OneHotEncoding
categorical_cols = ['country','listed_in']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_cat = encoder.fit_transform(features[categorical_cols])
X_num = features[['release_year']].to_numpy()
X = np.hstack([X_num, X_cat])
y = target.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("📌 Random Forest Regression:")
print("R² Score:", r2)
print("RMSE:", rmse)
