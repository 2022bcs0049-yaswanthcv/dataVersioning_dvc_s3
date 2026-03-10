import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import json

# Load dataset
df = pd.read_csv("data/housing.csv")

# Features and target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Metrics
rmse = mean_squared_error(y_test, predictions, squared=False)
r2 = r2_score(y_test, predictions)

print("Dataset size:", len(df))
print("RMSE:", rmse)
print("R2:", r2)

# Save metrics
metrics = {
    "dataset_size": len(df),
    "rmse": rmse,
    "r2": r2
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)