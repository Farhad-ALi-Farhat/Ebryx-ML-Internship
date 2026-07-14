# Titanic Survival Classification

A machine learning classification project that predicts whether a passenger survived the Titanic disaster using three classical machine learning algorithms:

- Decision Tree
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes

The project demonstrates a complete supervised machine learning workflow, including data preprocessing, model training, evaluation, and performance comparison.

---

## Dataset

- **Dataset:** Titanic Dataset
- **Target Variable:** `Survived`
  - `0` = Did Not Survive
  - `1` = Survived

---

## Project Workflow

1. Import required libraries
2. Load and explore the dataset
3. Perform Exploratory Data Analysis (EDA)
4. Handle missing values
5. Remove unnecessary features
6. Encode categorical variables
7. Split the dataset into training and testing sets
8. Build Scikit-learn Pipelines
9. Train three classification models
10. Evaluate model performance
11. Compare model results using metrics and visualizations

---

## Data Preprocessing

### Removed Columns

The following columns were removed because they provided little predictive value or contained excessive missing data:

- `PassengerId`
- `Name`
- `Ticket`
- `Cabin`

### Missing Values

| Column | Strategy |
|---------|----------|
| Age | Filled with Median |
| Embarked | Filled with Mode |

### Encoding

One-Hot Encoding was applied to:

- Sex
- Embarked

---

## Models Used

- Decision Tree Classifier
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes

Pipelines were used to simplify preprocessing and model training.

---

## Evaluation Metrics

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

A final comparison chart was also created to compare the overall performance of all three models.

---

## Results

| Model | Accuracy |
|--------|----------|
| Decision Tree | **82.12%** |
| k-Nearest Neighbors | **81.56%** |
| Gaussian Naive Bayes | **78.21%** |

The Decision Tree model achieved the highest accuracy on the test dataset, with kNN performing closely behind. Gaussian Naive Bayes produced the lowest overall performance among the three classifiers.

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
Titanic-Classification/
│
├── Titanic_Classification.ipynb
├── Titanic.csv
├── README.md
└── assets/
```

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Train-Test Split
- Scikit-learn Pipelines
- Decision Tree Classification
- k-Nearest Neighbors (kNN)
- Gaussian Naive Bayes
- Model Evaluation
- Performance Comparison
