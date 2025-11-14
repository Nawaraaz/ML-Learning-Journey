#creating a dummy datasets for practice
import pandas as pd
import numpy as np
# Set seed for reproducibility
np.random.seed(42)

# Number of rows
n = 150   # change to any number you want

# Create dummy dataset
df = pd.DataFrame({
    "age": np.random.randint(18, 80, n),
    "sex": np.random.choice(["male", "female"], n),
    "cholesterol": np.random.normal(200, 40, n).round(1),
    "blood_pressure": np.random.normal(120, 15, n).round(1),
    "diabetic": np.random.choice(["yes", "no"], n),
    "exercise_level": np.random.choice(["low", "medium", "high"], n),
    "bmi": np.random.normal(25, 4, n).round(1),
    "smoking_years": np.random.randint(0, 40, n),
    "patient_id": np.arange(1, n+1),
})

# Introduce missing values in 10% rows of selected columns
missing_cols = ["cholesterol", "blood_pressure", "bmi"]
for col in missing_cols:
    df.loc[df.sample(frac=0.10).index, col] = np.nan
df.to_csv("dummy_dataset.csv", index=False)
print(df.head())
print("\nDataset Shape:", df.shape)
# this code will drop a dummy dataset.