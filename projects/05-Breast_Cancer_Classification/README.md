# Breast Cancer Classification

A binary machine learning classification project that predicts whether a breast tumor is **malignant** or **benign** using three classical machine learning algorithms:

- Decision Tree
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes

The project demonstrates a complete machine learning workflow, including exploratory data analysis, model training using Scikit-learn Pipelines, evaluation, and performance comparison.

---

## Dataset

- **Dataset:** Breast Cancer Wisconsin Dataset
- **Source:** Scikit-learn (`load_breast_cancer`)
- **Target Variable:** `target`
  - `0` = Malignant
  - `1` = Benign

The dataset contains **569 samples** with **30 numerical features** computed from digitized images of breast cell nuclei.

---

## Project Workflow

1. Import required libraries
2. Load the Breast Cancer dataset
3. Perform Exploratory Data Analysis (EDA)
4. Analyze feature correlations
5. Split the dataset into training and testing sets
6. Build Scikit-learn Pipelines
7. Train three classification models
8. Evaluate each model
9. Compare model performance using metrics and visualizations

---

## Exploratory Data Analysis

The following analyses were performed:

- Dataset overview
- Feature statistics
- Missing value analysis
- Class distribution
- Feature correlation heatmap

The dataset contains no missing values and all features are numerical. Several features exhibit strong positive correlations, which is expected due to the nature of the measurements.

---

## Models Used

- Decision Tree Classifier
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes

Pipelines were used for model training, with feature scaling applied where appropriate.

---

## Evaluation Metrics

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

A comparison chart was generated to visualize the performance of all three classifiers.

---

## Results

| Model | Accuracy | Precision | Recall | F1-Score |
|--------|---------:|----------:|-------:|---------:|
| Decision Tree | 91.23% | 95.59% | 90.28% | 92.86% |
| k-Nearest Neighbors | **95.61%** | **95.89%** | **97.22%** | **96.55%** |
| Gaussian Naive Bayes | 92.98% | 94.44% | 94.44% | 94.44% |

The **k-Nearest Neighbors (kNN)** classifier achieved the best overall performance, obtaining the highest accuracy, recall, and F1-score among the three models. Decision Tree and Gaussian Naive Bayes also performed well, but kNN provided the most reliable predictions on the test dataset.

---

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Project Structure

```
Breast-Cancer-Classification/
│
├── Breast_Cancer_Classification.ipynb
├── README.md
└── assets/
```

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Binary Classification
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Train-Test Split
- Feature Scaling
- Scikit-learn Pipelines
- Decision Tree Classification
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes
- Model Evaluation
- Performance Comparison
```
