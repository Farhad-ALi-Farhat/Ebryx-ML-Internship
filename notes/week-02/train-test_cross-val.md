# Train/Test Split and Cross-Validation

Model evaluation is one of the most important steps in Machine Learning. A model should not only perform well on the data it was trained on but also generalize well to unseen data. To achieve this, the dataset is divided into training and testing sets, and techniques like cross-validation are used to obtain more reliable performance estimates.

---

# 1. Train/Test Split

## What is Train/Test Split?

Train/Test Split is the process of dividing a dataset into two parts:

- **Training Set:** Used to train the machine learning model.
- **Testing Set:** Used to evaluate the model's performance on unseen data.

The model learns patterns only from the training data and is evaluated using the testing data.

---

## Why Do We Split the Data?

If we train and test on the same dataset, the model may simply memorize the training examples instead of learning meaningful patterns.

This leads to **overfitting**, where the model performs well on training data but poorly on new, unseen data.

Using a separate test set helps measure how well the model generalizes.

---

## Common Split Ratios

The dataset can be divided using different ratios depending on its size.

| Training | Testing |
|-----------|----------|
| 80% | 20% |
| 75% | 25% |
| 70% | 30% |
| 90% | 10% (Large datasets) |

The **80/20 split** is the most commonly used.

---

## Example

Suppose a dataset contains **1,000 samples**.

Using an 80/20 split:

- Training samples = 800
- Testing samples = 200

The model is trained using the 800 samples and evaluated using the remaining 200 samples.

---

## Random Splitting

Data should be shuffled before splitting to ensure that both training and testing sets represent the overall dataset.

Without shuffling, biased splits may occur.

Example:

If all positive samples appear first and negative samples later, splitting without shuffling may produce an unbalanced training or testing set.

---

## Stratified Splitting

For classification problems, **Stratified Train/Test Split** preserves the proportion of each class in both training and testing datasets.

Example:

Original dataset:

- 90% Cats
- 10% Dogs

After stratified splitting:

Training:

- 90% Cats
- 10% Dogs

Testing:

- 90% Cats
- 10% Dogs

This prevents class imbalance in either split.

---

## Scikit-learn Example

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

### Parameters

- **test_size** → Percentage of data used for testing.
- **random_state** → Makes the split reproducible.
- **stratify** → Maintains class distribution.

---

## Advantages

- Simple and fast.
- Easy to implement.
- Suitable for large datasets.
- Prevents testing on training data.

---

## Disadvantages

- Performance depends on a single split.
- Results may vary if the data is split differently.
- May not fully represent the dataset, especially when data is limited.

---

# 2. Cross-Validation

## What is Cross-Validation?

Cross-Validation is a model evaluation technique where the dataset is divided into multiple subsets (called **folds**) instead of using only one train/test split.

The model is trained and tested multiple times using different portions of the data.

The final performance is obtained by averaging the results across all folds.

---

## Why Use Cross-Validation?

A single train/test split may accidentally produce:

- An easy testing set
- A difficult testing set

This can lead to unreliable performance estimates.

Cross-validation reduces this problem by evaluating the model multiple times.

---

# K-Fold Cross-Validation

The most common type is **K-Fold Cross-Validation**.

The dataset is divided into **K equal parts (folds)**.

For each iteration:

- One fold is used for testing.
- The remaining K−1 folds are used for training.

This process repeats until every fold has been used as the testing set exactly once.

---

## Example: 5-Fold Cross-Validation

Suppose we have 100 samples.

The dataset is divided into five folds:

```
Fold 1
Fold 2
Fold 3
Fold 4
Fold 5
```

Iterations:

| Iteration | Training Folds | Testing Fold |
|-----------|----------------|--------------|
| 1 | 2,3,4,5 | 1 |
| 2 | 1,3,4,5 | 2 |
| 3 | 1,2,4,5 | 3 |
| 4 | 1,2,3,5 | 4 |
| 5 | 1,2,3,4 | 5 |

The average score across all five iterations is reported as the model's performance.

---

## Choosing the Value of K

Common choices include:

| K | Usage |
|---|-------|
| 5 | Most common |
| 10 | Higher reliability |
| Leave-One-Out | Very small datasets |

- **5-Fold** provides a good balance between speed and accuracy.
- **10-Fold** generally produces more reliable estimates but requires more computation.
- **Leave-One-Out Cross-Validation (LOOCV)** trains on all samples except one and repeats for every sample, making it computationally expensive.

---

## Stratified K-Fold

For classification tasks, **Stratified K-Fold** maintains the same class distribution in every fold.

This is especially important when dealing with imbalanced datasets.

---

## Scikit-learn Example

```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print(scores)
print(scores.mean())
```

---

## Cross-Validation Workflow

1. Split the dataset into K folds.
2. Train the model using K−1 folds.
3. Test the model on the remaining fold.
4. Repeat until every fold has been used as the test set.
5. Compute the average performance score.

---

## Advantages

- More reliable evaluation than a single train/test split.
- Reduces bias caused by random data splitting.
- Makes better use of limited data.
- Helps detect overfitting.

---

## Disadvantages

- Computationally more expensive.
- Slower for very large datasets.
- Requires repeated model training.

---

# Train/Test Split vs Cross-Validation

| Feature | Train/Test Split | Cross-Validation |
|----------|------------------|------------------|
| Number of Evaluations | One | Multiple |
| Reliability | Moderate | High |
| Speed | Fast | Slower |
| Suitable for Large Datasets | ✅ Yes | ✅ Yes |
| Suitable for Small Datasets | Limited | Excellent |
| Computational Cost | Low | Higher |
| Risk of Biased Evaluation | Higher | Lower |

---

# Best Practices

- Always split the dataset before training the model.
- Use **Stratified Split** for classification tasks with imbalanced classes.
- Use **Cross-Validation** when comparing multiple models or tuning hyperparameters.
- Keep the **test set untouched** until the final model evaluation.
- Use a fixed **random_state** to make experiments reproducible.

---

# Key Takeaways

- **Train/Test Split** divides the dataset into separate training and testing sets for evaluating model performance.
- **Cross-Validation** evaluates the model multiple times using different data partitions, providing a more reliable estimate of generalization performance.
- **K-Fold Cross-Validation** is the most widely used technique, while **Stratified K-Fold** is recommended for classification problems with imbalanced classes.
- Combining a Train/Test Split with Cross-Validation is a common practice: use cross-validation during model development and reserve the test set for the final evaluation.
