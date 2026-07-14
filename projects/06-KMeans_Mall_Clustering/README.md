# K-Means Clustering on Mall Customers Dataset

## Overview

This project demonstrates customer segmentation using the **K-Means Clustering** algorithm. The objective is to group customers with similar purchasing behavior based on their **Annual Income** and **Spending Score**. The project also uses the **Elbow Method**, **Silhouette Score**, and **Principal Component Analysis (PCA)** to evaluate and visualize the clustering results.

---

## Dataset

**Dataset:** Mall Customers Dataset

### Features Used

- Annual Income (k$)
- Spending Score (1–100)

> **Note:** An additional experiment was conducted by including the **Age** feature. However, it reduced the Silhouette Score from **0.55** to **0.45**, indicating poorer cluster separation. Therefore, the final model uses only **Annual Income** and **Spending Score**.

---

## Project Workflow

1. Import libraries
2. Load the dataset
3. Perform Exploratory Data Analysis (EDA)
4. Select relevant features
5. Standardize features using `StandardScaler`
6. Determine the optimal number of clusters using the Elbow Method
7. Validate the clustering using the Silhouette Score
8. Train the K-Means model
9. Visualize customer clusters and cluster centroids
10. Apply PCA for dimensionality reduction and visualization
11. Interpret the resulting customer segments

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## Machine Learning Concepts

- Unsupervised Learning
- K-Means Clustering
- Feature Scaling
- Elbow Method
- Silhouette Score
- Principal Component Analysis (PCA)

---

## Results

- Successfully segmented customers into distinct groups based on spending behavior.
- Identified an appropriate number of clusters using the Elbow Method and Silhouette Score.
- Visualized the clusters in both the original feature space and a PCA-transformed space.
- Evaluated the impact of feature selection on clustering performance.

---

## Key Learnings

- Understanding how K-Means performs unsupervised clustering.
- Selecting the optimal number of clusters using evaluation metrics.
- The importance of feature scaling for distance-based algorithms.
- Using PCA to visualize clustered data in two dimensions.
- Evaluating different feature combinations to improve clustering quality.

---

## Project Structure

```text
01_KMeans_Mall_Clustering/
│
├── KMeans_Mall.ipynb
├── Mall_Customers.csv
├── README.md
└── assets/
    ├── elbow_method.png
    ├── silhouette_score.png
    ├── customer_clusters.png
    └── pca_clusters.png
```
