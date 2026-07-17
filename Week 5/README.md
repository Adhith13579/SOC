# Week 5: EDA (Exploratory Data Analysis) 

## Goals
- [x] Learn the principles and process of Exploratory Data Analysis (EDA)
- [x] Practice Data Cleaning techniques on a real-world-style dataset

##  Resources Used
- **EDA Cheat Sheet (Notion)** — covered the full EDA process in Python: understanding structure, distributions, correlations, and visualizations
- **Data Cleaning Colab Notebook** — hands-on walkthrough of cleaning a messy dataset: handling missing values, duplicates, outliers, and type issues

##  What I Covered

### Exploratory Data Analysis (EDA)
EDA is the process of getting to *know* your dataset before building any model. Rushing into modelling without EDA is one of the most common beginner mistakes.

Key steps covered:
- **Understanding the data**: `.head()`, `.info()`, `.describe()`, `.shape`, `.dtypes`
- **Missing value analysis**: detecting nulls, understanding patterns of missingness
- **Distributions**: histograms, box plots — checking for skew, spread, and outliers
- **Relationships between features**: scatter plots, correlation heatmaps
- **Categorical data**: value counts, bar plots

Detailed notes: [`notes_eda.md`](./notes_eda.md)

### Data Cleaning
Real-world data is always messy. Based on the Colab tutorial:
- Handling **missing values** (dropping vs. filling with mean/median/mode)
- Removing **duplicates**
- Fixing **data type mismatches** (e.g., a column stored as `object` that should be `int`)
- Detecting and dealing with **outliers** (IQR method)
- Renaming columns and standardizing formats

### Hands-on
- Created a synthetic messy dataset and applied a full EDA + cleaning pipeline on it.
- Covers everything from first look to a clean, analysis-ready DataFrame.

Code: [`eda_and_cleaning.py`](./eda_and_cleaning.py)

##  Notes to Self
- EDA is not a one-size-fits-all checklist — the questions you ask depend heavily on the dataset and the problem you're solving.
- Deciding *how* to handle missing values (drop vs. fill) is a judgment call that can significantly affect model performance later.
- Outlier handling is context-dependent too — an outlier in a house price dataset might be a genuine mansion, not a data error.
- Next week: apply EDA + cleaning to a real Kaggle dataset as part of a proper ML project pipeline.
