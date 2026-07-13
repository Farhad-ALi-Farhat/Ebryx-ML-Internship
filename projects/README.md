# 🏠 Boston Housing Price Prediction using Linear Regression

This project demonstrates an end-to-end Machine Learning regression workflow using the Boston Housing dataset. The objective is to predict median house prices using multiple housing-related features and evaluate the performance of a Linear Regression model.

---

## 📌 Project Overview

This notebook walks through every major step of a supervised machine learning project:

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Analysis
- Data Visualization
- Data Preprocessing
- Train-Test Split
- Linear Regression Model Training
- Model Evaluation
- Residual Analysis
- Feature Importance Analysis
- Recursive Feature Elimination (RFE)

---

## 📂 Dataset

**Dataset:** Boston Housing Dataset

The dataset contains information about housing in Boston suburbs including:

| Feature | Description |
|---------|-------------|
| CRIM | Crime rate |
| ZN | Residential land zoning |
| INDUS | Industrial area proportion |
| CHAS | Charles River dummy variable |
| NOX | Nitric oxide concentration |
| RM | Average number of rooms |
| AGE | Age of houses |
| DIS | Distance to employment centers |
| RAD | Accessibility to highways |
| TAX | Property tax rate |
| PTRATIO | Pupil-teacher ratio |
| B | Proportion related feature |
| LSTAT | Lower status population (%) |
| MEDV | Median house price (Target) |

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📊 Exploratory Data Analysis

The notebook includes:

- Dataset overview
- Missing value inspection
- Duplicate detection
- Statistical summaries
- Target variable distribution
- Correlation heatmap
- Feature correlation analysis

---

## ⚙️ Machine Learning Pipeline

1. Load dataset
2. Explore and clean data
3. Visualize relationships
4. Scale numerical features using StandardScaler
5. Split data into training and testing sets
6. Train a Linear Regression model
7. Evaluate model performance
8. Analyze residuals
9. Perform Recursive Feature Elimination (RFE)

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| MAE | **3.19** |
| MSE | **24.29** |
| RMSE | **4.93** |
| R² Score | **0.669** |

The Linear Regression model explains approximately **66.9%** of the variance in housing prices.

---

## 📉 Visualizations

The project includes several visualizations:

- Target Distribution
- Correlation Heatmap
- Feature Correlation Bar Chart
- Actual vs Predicted Plot
- Residual Plot
- Residual Distribution

---

## 📌 Key Findings

- Number of rooms (**RM**) has the strongest positive relationship with house prices.
- Lower status population (**LSTAT**) has the strongest negative relationship with house prices.
- Scaling features improves model stability.
- Recursive Feature Elimination (RFE) slightly reduced performance, so the full feature set was retained.

---

## 🚀 Future Improvements

Possible improvements include:

- Polynomial Regression
- Ridge Regression
- Lasso Regression
- Elastic Net
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting (XGBoost / LightGBM)
- Hyperparameter Tuning (GridSearchCV)
- Cross Validation
- Feature Engineering

---

## 📁 Project Structure

```
01_Linear_Regression_Boston_Housing/
│
├── housing.csv
├── 01_Linear_Regression_Boston_Housing.ipynb
├── README.md
└── assets/
    ├── correlation_heatmap.png
    ├── actual_vs_predicted.png
    └── residual_plot.png
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Supervised Machine Learning
- Regression Analysis
- Exploratory Data Analysis
- Feature Scaling
- Feature Selection
- Model Evaluation
- Residual Analysis
- Data Visualization
- End-to-End ML Workflow

---

## 👨‍💻 Author

**Farhad Ali**

This project is part of my Machine Learning learning journey and internship portfolio.
