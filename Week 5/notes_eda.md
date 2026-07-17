# Exploratory Data Analysis (EDA) — Notes

*Based on the EDA Python Cheat Sheet.*

## What is EDA and Why Does It Matter?
EDA is the process of examining a dataset to understand its structure, spot problems, and surface patterns — *before* attempting any modelling. It helps you:
- Understand what you're working with (columns, types, size)
- Catch data quality issues early (missing values, wrong types, outliers)
- Form hypotheses about which features might be useful for prediction
- Decide what cleaning and preprocessing steps are needed

Skipping EDA and jumping straight to model training is a common beginner mistake — you end up feeding garbage data into a model and wondering why it performs poorly.

## Step 1: Understanding the Dataset Structure
These are the first things to run on any new dataset:

| Command | What it tells you |
|---|---|
| `df.head()` | First 5 rows — get a feel for the data |
| `df.tail()` | Last 5 rows |
| `df.shape` | Number of rows and columns |
| `df.dtypes` | Data type of each column |
| `df.info()` | Column names, data types, and null counts |
| `df.describe()` | Summary statistics for numeric columns (mean, std, min, max, quartiles) |
| `df.columns` | List of all column names |

## Step 2: Missing Value Analysis
```python
df.isnull().sum()             # Count of nulls per column
df.isnull().mean() * 100      # Percentage of nulls per column
```
Questions to ask:
- Is the data missing randomly, or is there a pattern (e.g., a field that's only missing for a certain category)?
- Is the % of missing values small enough to drop rows, or do you need to impute?

Common imputation strategies:
- **Mean/Median** — for numeric columns (use median when the column is skewed)
- **Mode** — for categorical columns
- **Forward/backward fill** — for time series data

## Step 3: Distributions of Numeric Features
- **Histograms** — show the shape of the distribution (normal, right-skewed, left-skewed, bimodal, etc.)
- **Box plots** — show median, spread (IQR), and potential outliers clearly
- Look out for:
  - Extreme skewness (may need log transformation before modelling)
  - Very tight clustering (low-variance feature, may not be useful)
  - Multimodal distributions (might indicate mixed sub-populations in the data)

## Step 4: Categorical Feature Analysis
```python
df["column"].value_counts()           # Count of each category
df["column"].value_counts(normalize=True)  # As proportions
```
- Bar charts to visualize category frequencies
- Check for too many unique categories (high cardinality), which can be a challenge for ML models
- Check for inconsistent labels (e.g., "Male", "male", "M" all meaning the same thing)

## Step 5: Relationships Between Features
- **Scatter plots** — visualize the relationship between two numeric variables
- **Correlation matrix** — quantify linear relationships between all numeric columns
  ```python
  df.corr()
  ```
  - Values close to 1: strong positive correlation
  - Values close to -1: strong negative correlation
  - Values close to 0: little to no linear relationship
- **Heatmap** — visually represent the correlation matrix (easier to scan than raw numbers)
- **Box plots grouped by category** — compare distributions across different categories

## Step 6: Target Variable Analysis
If working on a supervised ML problem:
- Look at the distribution of the target column
- For classification: is it balanced? (50/50 split vs. 95/5 split changes your approach significantly)
- For regression: is it normally distributed, or skewed?

## Key EDA Takeaway
EDA is detective work. Every plot and summary stat is a clue. The goal isn't to run a fixed list of commands — it's to build enough understanding of the data to make smart decisions about cleaning, feature engineering, and modelling.
