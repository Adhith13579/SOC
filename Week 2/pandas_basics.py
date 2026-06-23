"""
Week 2: Pandas Basics
-----------------------
Practice script covering Series, DataFrames, indexing, filtering,
adding columns, groupby, and handling missing values.
"""

import pandas as pd
import numpy as np

# ----------------------------
# 1. Series
# ----------------------------
print("--- Pandas Series ---")
marks = pd.Series([85, 90, 78, 92, 88], name="Marks")
print(marks)
print("Mean marks:", marks.mean())
print()


# ----------------------------
# 2. Creating a DataFrame
# ----------------------------
print("--- Creating a DataFrame ---")
data = {
    "Name": ["Alex", "Sam", "Priya", "John", "Mira"],
    "Age": [21, 23, 22, 24, 21],
    "Marks": [85, 90, 78, 92, 88],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi"]
}
df = pd.DataFrame(data)
print(df)
print()


# ----------------------------
# 3. Indexing & Selecting Data
# ----------------------------
print("--- Indexing & Selecting Data ---")
print("Using loc (rows where index 0 to 2):")
print(df.loc[0:2])

print("\nUsing iloc (first 2 rows, first 2 columns):")
print(df.iloc[0:2, 0:2])

print("\nSelecting a single column:")
print(df["Name"])
print()


# ----------------------------
# 4. Filtering Data
# ----------------------------
print("--- Filtering Data ---")
high_scorers = df[df["Marks"] > 85]
print("Students with Marks > 85:")
print(high_scorers)

mumbai_students = df[df["City"] == "Mumbai"]
print("\nStudents from Mumbai:")
print(mumbai_students)
print()


# ----------------------------
# 5. Adding / Modifying Columns
# ----------------------------
print("--- Adding/Modifying Columns ---")
df["Grade"] = df["Marks"].apply(lambda x: "A" if x >= 85 else "B")
print(df)
print()


# ----------------------------
# 6. Grouping & Aggregating
# ----------------------------
print("--- Grouping & Aggregating ---")
city_avg = df.groupby("City")["Marks"].mean()
print("Average marks by city:")
print(city_avg)
print()


# ----------------------------
# 7. Handling Missing Values
# ----------------------------
print("--- Handling Missing Values ---")
df_with_nan = df.copy()
df_with_nan.loc[2, "Marks"] = np.nan  # introduce a missing value

print("DataFrame with a missing value:")
print(df_with_nan)

print("\nChecking for missing values:")
print(df_with_nan.isnull().sum())

# Fill missing value with the column's mean
df_filled = df_with_nan.copy()
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

print("\nAfter filling missing value with mean:")
print(df_filled)
