# Hyperparameter Tuning with GridSearchCV

## Overview

This project demonstrates how to improve a machine learning model using **GridSearchCV** for hyperparameter tuning. A **Decision Tree Classifier** is trained on the Iris dataset, and its performance is compared before and after tuning. The project also explains the selected hyperparameters and their impact on model performance.

---

## Dataset

**Dataset:** Iris Dataset (built into Scikit-learn)

### Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Setosa
- Versicolor
- Virginica

---

## Project Workflow

1. Import required libraries
2. Load and inspect the dataset
3. Perform basic Exploratory Data Analysis (EDA)
4. Split the data into training and testing sets
5. Train a Decision Tree Classifier with default parameters
6. Evaluate the baseline model
7. Define a hyperparameter search space
8. Apply GridSearchCV with 5-fold Cross-Validation
9. Train the best-performing model
10. Evaluate the tuned model
11. Compare default and tuned models
12. Interpret the selected hyperparameters

---

## Hyperparameters Tuned

The following Decision Tree hyperparameters were optimized:

- `criterion`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

GridSearchCV evaluated multiple combinations using **5-fold Cross-Validation** to determine the best-performing configuration.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## Machine Learning Concepts

- Supervised Learning
- Decision Tree Classifier
- Hyperparameter Tuning
- GridSearchCV
- Cross-Validation
- Model Evaluation
- Confusion Matrix
- Classification Report

---

## Results

- Trained a baseline Decision Tree classifier.
- Applied GridSearchCV to search for the best hyperparameters.
- Identified the optimal parameter combination using cross-validation.
- Compared the default and tuned models on the test set.
- Interpreted the selected hyperparameters and their effect on model complexity.

> **Observation:**  
> Although GridSearchCV achieved the highest average cross-validation accuracy during training, the tuned model achieved the same test accuracy as the default model. This indicates that the default Decision Tree was already well-suited for the Iris dataset, while GridSearchCV validated the optimal parameter selection.

---

## Key Learnings

- Understanding the difference between model parameters and hyperparameters.
- Using GridSearchCV to systematically search for the best hyperparameter combination.
- Applying Cross-Validation to estimate model performance.
- Comparing baseline and tuned models.
- Interpreting tuning results and understanding why tuning does not always improve test accuracy.
- Evaluating model performance using accuracy, classification reports, and confusion matrices.

---

## Project Structure

```text
02_GridSearchCV_Hyperparameter_Tuning/
│
├── GridSearchCV.ipynb
└── README.md
```
