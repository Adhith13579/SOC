"""
Week 5: EDA & Data Cleaning
-----------------------------
A full worked example on a synthetic "student performance" dataset that
has been made intentionally messy. Covers:
  - First look at a dataset
  - Missing value analysis and imputation
  - Duplicate removal
  - Data type fixes
  - Outlier detection (IQR method)
  - Distributions and correlation analysis
  - Exporting a clean, analysis-ready DataFrame
"""

import pandas as pd
import numpy as np

np.random.seed(42)


# ----------------------------
# 1. Create a Synthetic Messy Dataset
# ----------------------------
def create_messy_dataset(n=200):
    """Generates a synthetic student dataset with common data quality issues."""
    data = {
        "student_id": list(range(1, n + 1)),
        "name": [f"Student_{i}" for i in range(1, n + 1)],
        "age": np.random.randint(18, 25, n).astype(float),
        "gender": np.random.choice(["Male", "Female", "male", "female", "M", "F"], n),
        "study_hours_per_day": np.random.uniform(0.5, 10, n).round(1),
        "attendance_pct": np.random.uniform(50, 100, n).round(1),
        "score": np.random.randint(40, 100, n).astype(float),
        "city": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Chennai", None], n),
    }
    df = pd.DataFrame(data)

    # Introduce missing values
    df.loc[np.random.choice(df.index, 20, replace=False), "age"] = np.nan
    df.loc[np.random.choice(df.index, 25, replace=False), "score"] = np.nan
    df.loc[np.random.choice(df.index, 15, replace=False), "attendance_pct"] = np.nan

    # Introduce duplicates
    duplicates = df.sample(10)
    df = pd.concat([df, duplicates], ignore_index=True)

    # Introduce outliers
    df.loc[np.random.choice(df.index, 5, replace=False), "study_hours_per_day"] = 25.0
    df.loc[np.random.choice(df.index, 3, replace=False), "score"] = 200.0

    # Mess up data types
    df["student_id"] = df["student_id"].astype(str)

    return df


# ----------------------------
# 2. First Look
# ----------------------------
print("=" * 50)
print("STEP 1: FIRST LOOK AT THE DATASET")
print("=" * 50)
df = create_messy_dataset()
print(f"Shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)
print(f"\nBasic statistics:")
print(df.describe())


# ----------------------------
# 3. Missing Value Analysis
# ----------------------------
print("\n" + "=" * 50)
print("STEP 2: MISSING VALUE ANALYSIS")
print("=" * 50)
missing_counts = df.isnull().sum()
missing_pct = (df.isnull().mean() * 100).round(2)
missing_summary = pd.DataFrame({"Missing Count": missing_counts, "Missing %": missing_pct})
print(missing_summary[missing_summary["Missing Count"] > 0])


# ----------------------------
# 4. Remove Duplicates
# ----------------------------
print("\n" + "=" * 50)
print("STEP 3: REMOVING DUPLICATES")
print("=" * 50)
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows. ({before} -> {after} rows)")


# ----------------------------
# 5. Fix Data Types
# ----------------------------
print("\n" + "=" * 50)
print("STEP 4: FIXING DATA TYPES")
print("=" * 50)
df["student_id"] = df["student_id"].astype(int)
print("Converted 'student_id' from string to int.")
print(df["student_id"].dtype)


# ----------------------------
# 6. Standardise Categorical Values
# ----------------------------
print("\n" + "=" * 50)
print("STEP 5: STANDARDISING CATEGORICAL COLUMNS")
print("=" * 50)
print("'gender' before:", df["gender"].value_counts().to_dict())
gender_map = {"male": "Male", "m": "Male", "M": "Male", "female": "Female", "f": "Female", "F": "Female"}
df["gender"] = df["gender"].replace(gender_map)
print("'gender' after:", df["gender"].value_counts().to_dict())


# ----------------------------
# 7. Impute Missing Values
# ----------------------------
print("\n" + "=" * 50)
print("STEP 6: IMPUTING MISSING VALUES")
print("=" * 50)

# Impute numeric columns with median (robust to outliers)
for col in ["age", "score", "attendance_pct"]:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)
    print(f"  Filled '{col}' nulls with median: {median_val}")

# Impute categorical column with mode
mode_city = df["city"].mode()[0]
df["city"] = df["city"].fillna(mode_city)
print(f"  Filled 'city' nulls with mode: '{mode_city}'")

print(f"\nMissing values after imputation:\n{df.isnull().sum()}")


# ----------------------------
# 8. Outlier Detection & Removal (IQR Method)
# ----------------------------
print("\n" + "=" * 50)
print("STEP 7: OUTLIER DETECTION (IQR METHOD)")
print("=" * 50)

def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    return outliers, lower, upper

for col in ["study_hours_per_day", "score"]:
    outliers, lower, upper = detect_outliers_iqr(df, col)
    print(f"\n'{col}': {len(outliers)} outliers detected (valid range: {lower:.2f} – {upper:.2f})")
    print(f"  Outlier values: {sorted(outliers[col].unique())}")
    # Remove outliers
    df = df[(df[col] >= lower) & (df[col] <= upper)]
    print(f"  Rows after removing outliers: {len(df)}")


# ----------------------------
# 9. Correlation Analysis
# ----------------------------
print("\n" + "=" * 50)
print("STEP 8: CORRELATION ANALYSIS")
print("=" * 50)
numeric_cols = ["age", "study_hours_per_day", "attendance_pct", "score"]
corr_matrix = df[numeric_cols].corr().round(2)
print(corr_matrix)
print("\nKey insight: Features most correlated with 'score':")
print(corr_matrix["score"].drop("score").sort_values(ascending=False))


# ----------------------------
# 10. Final Clean Dataset Summary
# ----------------------------
print("\n" + "=" * 50)
print("STEP 9: FINAL CLEAN DATASET SUMMARY")
print("=" * 50)
print(f"Final shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"\nSample of clean data:")
print(df.head())
