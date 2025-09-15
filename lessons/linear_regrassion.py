# Linear Regression Example with Netflix Data

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Netflix dataset load
data = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# Suppose আমরা শুধু 'release_year' দিয়ে 'duration' predict করব
# এখানে example purpose এর জন্য numeric values নিতে হবে
# duration কে numeric বানাই (minutes remove করে)
data['duration'] = data['duration'].str.replace(' min', '')
data['duration'] = pd.to_numeric(data['duration'], errors='coerce')

# null values drop
data = data.dropna(subset=['release_year', 'duration'])

X = data[['release_year']]   # feature
y = data['duration']         # target

# dataset split (train 80%, test 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model create
model = LinearRegression()
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# model performance check
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# visualization
plt.scatter(X_test, y_test, color='blue', label="Actual")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Predicted Line")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")
plt.legend()
plt.show()
