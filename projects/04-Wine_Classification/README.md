# Wine Classification

A multiclass machine learning classification project that classifies wine samples into one of three cultivars using three classical machine learning algorithms:

- Decision Tree
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes

The project demonstrates a complete classification workflow, including exploratory data analysis, model training using Scikit-learn Pipelines, evaluation, and performance comparison.

---

## Dataset

- **Dataset:** Wine Dataset
- **Source:** Scikit-learn (`load_wine`)
- **Target Variable:** `target`

The dataset contains **178 wine samples** with **13 numerical features** describing the chemical composition of different wines.

---

## Project Workflow

1. Import required libraries
2. Load the Wine dataset
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

The dataset contains no missing values and all features are numerical, making preprocessing straightforward.

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
| Decision Tree | 94.44% | 95.14% | 94.44% | 94.50% |
| k-Nearest Neighbors | **97.22%** | **97.47%** | **97.22%** | **97.24%** |
| Gaussian Naive Bayes | **97.22%** | 97.44% | **97.22%** | 97.23% |

Both **k-Nearest Neighbors** and **Gaussian Naive Bayes** achieved the highest accuracy of **97.22%** on the test dataset. Among them, **kNN** produced the highest overall precision and F1-score, making it the best-performing model for this dataset.

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
Wine-Classification/
│
├── Wine_Classification.ipynb
├── README.md
└── assets/
```

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Multiclass Classification
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
