# Decision Trees, k-Nearest Neighbors (kNN), and Naive Bayes

This document covers three fundamental supervised machine learning algorithms:

- Decision Trees
- k-Nearest Neighbors (kNN)
- Naive Bayes

These algorithms are widely used for classification tasks, and Decision Trees and kNN can also be used for regression.

---

# 1. Decision Trees

## What is a Decision Tree?

A **Decision Tree** is a supervised learning algorithm that predicts an output by learning a series of decision rules from the training data.

It resembles a flowchart where:

- The **root node** represents the first decision.
- **Internal nodes** represent feature-based decisions.
- **Branches** represent outcomes of those decisions.
- **Leaf nodes** represent the final prediction.

Decision Trees work by repeatedly splitting the dataset into smaller subsets until each subset contains similar target values.

---

## Types of Decision Trees

### Classification Tree

Used when the target variable is categorical.

Examples:

- Spam / Not Spam
- Pass / Fail
- Disease / Healthy

---

### Regression Tree

Used when the target variable is continuous.

Examples:

- House Price Prediction
- Salary Prediction
- Temperature Forecasting

---

## Tree Terminology

### Root Node

The first decision made by the tree.

### Internal Node

A node where another decision is performed.

### Leaf Node

The final prediction.

### Branch

A connection between two nodes.

---

## How Decision Trees Work

Suppose we have the following dataset:

| Age | Income | Buy Laptop |
|------|---------|------------|
|22|High|Yes|
|25|Low|No|
|35|High|Yes|
|45|Low|No|

The algorithm evaluates every feature and chooses the split that best separates the classes.

For example:

```
Age < 30?
```

Then further splits may be performed using Income until the data is well separated.

---

## Splitting Criteria

### Gini Impurity

Measures how mixed the classes are.

- Lower Gini → Better split
- Gini = 0 means perfectly pure.

Used by the CART algorithm.

---

### Entropy

Measures uncertainty within the dataset.

Lower entropy indicates better separation.

Used by the ID3 algorithm.

---

### Information Gain

Measures how much uncertainty decreases after a split.

The feature with the **highest Information Gain** is selected.

---

## Advantages

- Easy to understand and visualize.
- Requires little data preprocessing.
- Works with both numerical and categorical features.
- Handles nonlinear relationships.
- Performs feature selection automatically.

---

## Disadvantages

- Can easily overfit.
- Sensitive to noisy data.
- Small changes in data may produce a completely different tree.

---

## Important Hyperparameters

### max_depth

Maximum depth of the tree.

Smaller values help reduce overfitting.

---

### min_samples_split

Minimum number of samples required before splitting a node.

---

### min_samples_leaf

Minimum samples allowed in each leaf node.

---

### criterion

Determines the split quality.

Classification:

- gini
- entropy

Regression:

- squared_error

---

## Scikit-learn Example

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=4,
    criterion="gini"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

## Applications

- Loan Approval
- Fraud Detection
- Customer Churn Prediction
- Medical Diagnosis
- Credit Risk Analysis

---

# 2. k-Nearest Neighbors (kNN)

## What is kNN?

k-Nearest Neighbors is a supervised learning algorithm that predicts the output based on the **k closest training examples**.

The idea is simple:

> Similar data points tend to belong to the same class.

Unlike most algorithms, kNN performs almost no learning during training. It stores the training data and makes decisions only during prediction.

---

## How kNN Works

1. Choose a value for **k**.
2. Compute the distance between the new sample and every training sample.
3. Select the nearest k neighbors.
4. Perform majority voting (classification) or averaging (regression).

---

## Distance Metrics

### Euclidean Distance

Straight-line distance between two points.

Most commonly used.

---

### Manhattan Distance

Distance measured along horizontal and vertical paths.

Useful in grid-based problems.

---

### Minkowski Distance

A generalized distance metric.

---

## Choosing k

### Small k

Example:

```
k = 1
```

Advantages:

- Flexible decision boundary.

Disadvantages:

- Sensitive to noise.
- May overfit.

---

### Large k

Example:

```
k = 25
```

Advantages:

- More stable predictions.

Disadvantages:

- May underfit.

Usually, an odd value of k is chosen for binary classification to avoid ties.

---

## Why Feature Scaling is Important

Distance calculations are affected by feature magnitudes.

Example:

| Height | Salary |
|---------|---------|
|170|40000|

Salary dominates the distance calculation due to its larger scale.

Therefore, feature scaling should be applied before training kNN.

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

## Advantages

- Very simple algorithm.
- No explicit training phase.
- Works well for small datasets.
- Can model complex decision boundaries.

---

## Disadvantages

- Slow prediction on large datasets.
- Sensitive to irrelevant features.
- Requires feature scaling.
- Memory intensive.

---

## Scikit-learn Example

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

## Applications

- Recommendation Systems
- Image Recognition
- Medical Diagnosis
- Pattern Recognition

---

# 3. Naive Bayes

## What is Naive Bayes?

Naive Bayes is a supervised learning algorithm based on **Bayes' Theorem**.

Instead of directly predicting a class, it calculates the probability that a sample belongs to each class and selects the class with the highest probability.

---

## Why is it Called "Naive"?

It assumes that all input features are **independent** of one another.

For example, in spam detection, the words:

- Free
- Winner
- Money

are treated as independent features, even though they often appear together.

Despite this unrealistic assumption, Naive Bayes performs remarkably well in many real-world applications.

---

## Bayes' Theorem

\[
P(A|B)=\frac{P(B|A)\times P(A)}{P(B)}
\]

Where:

- **P(A)** → Prior Probability
- **P(B)** → Evidence Probability
- **P(B|A)** → Likelihood
- **P(A|B)** → Posterior Probability

---

## Types of Naive Bayes

### Gaussian Naive Bayes

Used for continuous numerical data.

Examples:

- Height
- Weight
- Income

---

### Multinomial Naive Bayes

Used for count-based data.

Examples:

- Word frequencies
- Text classification

---

### Bernoulli Naive Bayes

Used for binary features.

Examples:

- Word exists or not.
- Purchased or not.

---

## Advantages

- Extremely fast.
- Works well with high-dimensional datasets.
- Excellent for text classification.
- Performs well even with relatively small datasets.

---

## Disadvantages

- Assumes feature independence.
- Sensitive to highly correlated features.
- Suffers from the Zero Frequency Problem, which is commonly addressed using Laplace Smoothing.

---

## Scikit-learn Example

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

## Applications

- Spam Filtering
- Sentiment Analysis
- News Categorization
- Email Classification
- Medical Diagnosis

---

# Comparison of Algorithms

| Feature | Decision Tree | kNN | Naive Bayes |
|----------|---------------|-----|-------------|
| Learning Type | Supervised | Supervised | Supervised |
| Supports Regression | ✅ | ✅ | ❌ |
| Training Speed | Fast | Very Fast (Lazy Learning) | Very Fast |
| Prediction Speed | Fast | Slow | Fast |
| Feature Scaling Required | ❌ No | ✅ Yes | Usually No |
| Handles Nonlinear Data | ✅ | ✅ | Limited |
| Easy to Interpret | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Works Well with Text Data | ❌ | ❌ | ⭐⭐⭐⭐⭐ |
| Best For | General-purpose classification and regression | Similarity-based problems | Probabilistic classification |

---

# Key Takeaways

- **Decision Trees** create flowchart-like decision rules and are highly interpretable.
- **kNN** predicts using the nearest neighboring data points and requires feature scaling.
- **Naive Bayes** uses Bayes' Theorem to compute class probabilities and performs exceptionally well on text classification tasks.
- Choosing the right algorithm depends on the dataset, problem type, and computational requirements.
