# Machine Learning Basics — Theory Notes

*Notes from the ML playlist, covered up through Bagging.*

## 1. Recap: What is Machine Learning?
Machine Learning is about learning patterns from data rather than relying on hardcoded rules. A model is trained on input data and learns to map inputs to outputs, then generalizes that mapping to new, unseen data.

## 2. Linear Regression
- Used for predicting **continuous** values (e.g., price, temperature).
- Tries to fit a straight line (or hyperplane) that best represents the relationship between input features (`X`) and the target (`y`).
- Line equation: `y = mx + c` (simple case) or `y = w1*x1 + w2*x2 + ... + b` (multiple features).
- The model learns the best `weights` and `bias` by minimizing the error between predicted and actual values (commonly using **Mean Squared Error**).

## 3. Logistic Regression
- Despite the name, it's used for **classification**, not regression — typically binary classification (yes/no, 0/1).
- Instead of fitting a straight line, it fits an **S-shaped curve (sigmoid function)** that outputs a probability between 0 and 1.
- A threshold (commonly 0.5) is used to decide the final class.
- Example use case: predicting whether an email is spam or not.

## 4. Decision Trees
- A tree-like model that splits data based on feature values, asking a series of yes/no questions.
- Each internal node represents a decision rule (e.g., "is age > 30?"), and each leaf node represents an output (class label or value).
- Splits are chosen to maximize "purity" of the resulting groups, using measures like **Gini Impurity** or **Entropy/Information Gain**.
- Easy to interpret, but prone to **overfitting** if grown too deep.

## 5. Ensemble Learning & Bagging
- **Ensemble learning**: combining multiple models to get a better, more stable prediction than any single model alone.
- **Why?** A single Decision Tree can overfit and be sensitive to small changes in data. Combining several models reduces this variance.
- **Bagging (Bootstrap Aggregating)**:
  1. Create multiple random subsets of the training data (sampled *with replacement* — this is "bootstrapping").
  2. Train a separate model (often a Decision Tree) on each subset.
  3. Combine their predictions:
     - **Classification** → majority vote
     - **Regression** → average of predictions
- **Random Forest** is the most common example of bagging — it's essentially a collection of Decision Trees trained on bootstrapped samples, with some extra randomness added in feature selection.
- Key benefit: reduces overfitting and variance compared to a single Decision Tree, while keeping bias roughly the same.

## Key Takeaway
This week built the foundation of core supervised learning algorithms (Linear Regression → Logistic Regression → Decision Trees) and introduced *why* combining models through Bagging leads to more robust predictions. Next step: explore Boosting and dive deeper into Random Forests.
