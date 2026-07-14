# Hierarchical Clustering

## What is Hierarchical Clustering?

Hierarchical Clustering is an **unsupervised learning algorithm** that groups similar data points into a hierarchy of clusters.

Unlike K-Means, it does **not require specifying the number of clusters (K) before training**. Instead, it creates a tree-like structure called a **dendrogram**, which helps determine the appropriate number of clusters.

---

## Types of Hierarchical Clustering

### 1. Agglomerative (Bottom-Up)

This is the most commonly used approach.

Steps:

1. Start with each data point as its own cluster.
2. Merge the two closest clusters.
3. Repeat until all points belong to a single cluster.

Example:

```
A  B  C  D

↓

(A B)  C  D

↓

(A B) (C D)

↓

(A B C D)
```

---

### 2. Divisive (Top-Down)

This approach works in reverse.

1. Start with all data points in one cluster.
2. Repeatedly split the cluster into smaller clusters.
3. Continue until each point forms its own cluster.

Divisive clustering is less commonly used because it is more computationally expensive.

---

## How Agglomerative Clustering Works

1. Treat every point as an individual cluster.
2. Compute the distance between all clusters.
3. Merge the closest pair.
4. Recalculate distances.
5. Repeat until only one cluster remains.

---

## Linkage Methods

The distance between clusters can be measured in different ways.

### Single Linkage

Uses the **minimum distance** between two clusters.

- Can create long chain-like clusters.

---

### Complete Linkage

Uses the **maximum distance** between two clusters.

- Produces compact clusters.

---

### Average Linkage

Uses the **average distance** between all pairs of points in two clusters.

- A balance between single and complete linkage.

---

### Ward Linkage

Merges clusters that produce the **smallest increase in variance**.

- Usually creates compact and balanced clusters.
- One of the most commonly used linkage methods.

---

## Dendrogram

A **dendrogram** is a tree diagram that shows how clusters are merged.

Example:

```
|
|        _________
|       |         |
|   ____|___      |
|  |        |     |
|  A        B   C D
|
+-----------------------
```

A horizontal cut through the dendrogram determines the final number of clusters.

- Higher cut → Fewer clusters
- Lower cut → More clusters

---

## Advantages

- No need to specify K initially
- Produces an easy-to-understand dendrogram
- Useful for exploratory data analysis
- Can identify nested clusters

---

## Limitations

- Computationally expensive for large datasets
- High memory usage
- Sensitive to noise and outliers
- Once clusters are merged, they cannot be separated

---

## Applications

- Customer segmentation
- Gene expression analysis
- Biological taxonomy
- Document clustering
- Image analysis

---

## Example (Scikit-learn)

```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

labels = model.fit_predict(X)
```

---

## Summary

- Hierarchical Clustering builds a hierarchy of clusters.
- It produces a dendrogram that visualizes relationships between data points.
- The two main approaches are Agglomerative (bottom-up) and Divisive (top-down).
- Common linkage methods include Single, Complete, Average, and Ward linkage.
- It is useful for smaller datasets and exploratory analysis but is slower than K-Means on large datasets.
