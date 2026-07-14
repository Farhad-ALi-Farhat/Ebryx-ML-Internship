# K-Means Clustering

## What is K-Means?

K-Means is an **unsupervised machine learning algorithm** used to group similar data points into **K clusters**. Since the data has no labels, the algorithm identifies patterns based on the similarity of the data points.

The goal is to ensure that:
- Data points within the same cluster are as similar as possible.
- Different clusters are as distinct as possible.

---

## Why is it Called "K-Means"?

- **K** represents the number of clusters you want to create.
- **Means** refers to the centroid (mean position) of all data points in a cluster.

For example, if `K = 3`, the algorithm will divide the dataset into three clusters.

---

## How K-Means Works

### Step 1: Choose the Number of Clusters (K)

Decide how many clusters you want to create.

```python
K = 3
```

---

### Step 2: Initialize Centroids

Randomly select **K** points as the initial centroids.

---

### Step 3: Assign Points to the Nearest Centroid

For every data point:

1. Calculate the distance to each centroid.
2. Assign the point to the nearest centroid.

K-Means typically uses **Euclidean Distance**.

---

### Step 4: Update Centroids

Calculate the mean of all points in each cluster.

The centroid moves to this new average position.

---

### Step 5: Repeat

Repeat the assignment and update steps until:
- Centroids stop moving significantly, or
- The maximum number of iterations is reached.

This is called **convergence**.

---

## Distance Measure

K-Means commonly uses **Euclidean Distance**.

For two points:

```
A(x₁, y₁)
B(x₂, y₂)
```

Distance:

\[
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
\]

The point is assigned to the nearest centroid.

---

## Choosing the Right Value of K

Choosing the correct value of **K** is important.

### If K is too small

Different groups may be merged together.

### If K is too large

One natural group may be split into several smaller clusters.

Common methods for choosing K:

- Elbow Method
- Silhouette Score

---

## Advantages

- Simple and easy to understand
- Fast for large datasets
- Easy to implement
- Works well for compact, spherical clusters

---

## Limitations

- Must choose K beforehand
- Sensitive to outliers
- Sensitive to feature scaling
- Doesn't perform well on irregular-shaped clusters
- Different initial centroids can produce different results

---

## Applications

- Customer segmentation
- Recommendation systems
- Image compression
- Document clustering
- Market analysis

---

## Example (Scikit-learn)

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
```

---

## Summary

- K-Means is an unsupervised clustering algorithm.
- It divides data into **K clusters**.
- Each cluster is represented by a centroid.
- The algorithm repeatedly assigns points and updates centroids until convergence.
- It is fast and widely used but requires selecting the number of clusters beforehand.
