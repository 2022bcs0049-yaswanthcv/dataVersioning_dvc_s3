import pandas as pd

# Load dataset
df = pd.read_csv("data/housing.csv")

# Create Version 1 (first 5000 rows)
df_v1 = df.head(5000)

# Replace dataset with Version 1
df_v1.to_csv("data/housing.csv", index=False)

print("Dataset Version 1 created")
print("Shape:", df_v1.shape)