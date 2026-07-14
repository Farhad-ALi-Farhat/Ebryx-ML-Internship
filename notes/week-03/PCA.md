# Principal Component Analysis (PCA)

## What is PCA?

**Principal Component Analysis (PCA)** is an **unsupervised machine learning technique** used for **dimensionality reduction**. It transforms a dataset with many features into a smaller set of new features called **Principal Components**, while preserving as much information (variance) as possible.

PCA is commonly used for:
- **Feature Reduction** – Reduce the number of input features while retaining most of the important information.
- **Data Visualization** – Project high-dimensional data into 2D or 3D so it can be visualized.

---

## Why Do We Need PCA?

Real-world datasets often contain:
- Many features
- Highly correlated features
- Redundant information

Having too many features can:
- Increase training time
- Make models more complex
- Lead to overfitting
- Make visualization difficult or impossible

PCA solves this by creating fewer, uncorrelated features that capture most of the dataset's variation.

---

## What are Principal Components?

Principal Components (PCs) are new features created by combining the original features.

They have two important properties:

- They are **uncorrelated** with each other.
- They are ordered by the amount of variance they explain.

Example:

Original Features:

```
Height
Weight
BMI
Age
```

After PCA:

```
PC1
PC2
PC3
PC4
```

Usually, only the first few principal components are kept because they contain most of the information.

---

## How PCA Works

1. Standardize the data.
2. Compute the covariance matrix.
3. Calculate eigenvalues and eigenvectors.
4. Rank the principal components by explained variance.
5. Select the top principal components.
6. Transform the original data into the new feature space.

---

## Explained Variance

Each principal component explains a certain percentage of the dataset's variance.

Example:

| Principal Component | Explained Variance |
|---------------------|-------------------:|
| PC1 | 65% |
| PC2 | 22% |
| PC3 | 9% |
| PC4 | 4% |

If we keep **PC1** and **PC2**, we preserve:

```
65% + 22% = 87%
```

of the original information while reducing four features to two.

---

# PCA for Visualization

Humans cannot visualize data with many dimensions.

For example:

- 10 features → Impossible to visualize directly.
- 100 features → Even more difficult.

PCA projects the data into **2 principal components (PC1 and PC2)** or **3 principal components (PC1, PC2, and PC3)**, making it possible to plot the data.

### Example

Suppose a dataset has 20 features.

After applying PCA:

```
20 Features

↓

PC1
PC2
```

Now each sample can be represented as a point on a 2D scatter plot.

This helps us:

- Discover natural clusters
- Detect outliers
- Understand relationships between samples
- Explore the data before training a model

---

# PCA for Feature Reduction

PCA can also reduce the number of input features while keeping most of the important information.

Example:

Original dataset:

```
50 Features
```

After PCA:

```
50 Features

↓

12 Principal Components
```

If these 12 components explain **95% of the variance**, we can discard the remaining 38 features with minimal information loss.

Benefits include:

- Faster model training
- Lower memory usage
- Reduced overfitting
- Removal of multicollinearity (highly correlated features)

---

## Choosing the Number of Components

The number of principal components is usually selected based on the **cumulative explained variance**.

A common practice is to retain enough components to explain **90–95%** of the total variance.

---

## Advantages

- Reduces dimensionality
- Speeds up model training
- Removes correlated features
- Helps reduce overfitting
- Makes high-dimensional data easier to visualize

---

## Limitations

- Principal Components are harder to interpret than original features.
- Some information is lost during dimensionality reduction.
- PCA assumes linear relationships between features.
- Feature scaling is required before applying PCA.

---

## Example (Scikit-learn)

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize the data
X_scaled = StandardScaler().fit_transform(X)

# Reduce to 2 principal components
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print(pca.explained_variance_ratio_)
```

---

## Summary

- PCA is an **unsupervised dimensionality reduction** technique.
- It transforms correlated features into a smaller set of **Principal Components**.
- The first principal components capture the most variance in the data.
- PCA is widely used for **feature reduction** and **data visualization**.
- It helps build faster, simpler models while preserving most of the dataset's information.
