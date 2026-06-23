# Week 2: ML Basics 

##  Goals
- [x] Learn the basics of Machine Learning (theory)
- [x] Get hands-on with **Pandas** for data handling

##  Resources Used
- **ML Playlist** — covered up through **Bagging**
- **Pandas Tutorial** — covered Series, DataFrames, indexing, filtering, and grouping

##  What I Covered

### Machine Learning Theory
- Recap: What is ML, and how it differs from traditional programming
- **Supervised Learning**
  - Linear Regression — predicting continuous values
  - Logistic Regression — binary classification
  - Decision Trees — rule-based splitting for classification/regression
- **Ensemble Learning**
  - Why combine multiple models (reducing variance/overfitting)
  - **Bagging** (Bootstrap Aggregating) — training multiple models on random subsets of data and combining their outputs (e.g., Random Forest as a bagging-based algorithm)

Detailed notes: [`ml_notes.md`](./ml_notes.md)

### Pandas
- Creating Series and DataFrames
- Reading data into a DataFrame
- Indexing & selecting data (`loc`, `iloc`)
- Filtering rows based on conditions
- Adding/modifying columns
- Grouping and aggregating data with `groupby`
- Handling missing values

Code: [`pandas_basics.py`](./pandas_basics.py)

##  Notes to Self
- Decision Trees and Bagging gave a good intuition for why ensemble methods (like Random Forest) tend to perform better than a single model.
- Pandas is going to be essential for every ML project going forward — comfortable with the basics now.
- Next week: continue the ML playlist past Bagging (Boosting, maybe Random Forest in depth) and start applying Pandas to a real dataset.
