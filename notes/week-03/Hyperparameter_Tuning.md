# Hyperparameter Tuning with GridSearchCV & RandomizedSearchCV

## What is Hyperparameter Tuning?

Hyperparameter tuning is the process of finding the **best combination of hyperparameters** for a machine learning model.

Hyperparameters are settings that are chosen **before training** the model. Unlike model parameters (such as weights in Linear Regression), they are **not learned from the data**.

Examples of hyperparameters:

- Number of neighbors (`n_neighbors`) in KNN
- Maximum depth (`max_depth`) in Decision Trees
- Number of trees (`n_estimators`) in Random Forest
- Learning rate in Gradient Boosting

The goal of hyperparameter tuning is to improve the model's performance on unseen data.

---

# Why is Hyperparameter Tuning Important?

Choosing different hyperparameter values can significantly affect model performance.

For example, in KNN:

- `k = 1` may lead to **overfitting**.
- `k = 50` may lead to **underfitting**.
- `k = 5` or `k = 7` might provide a better balance.

Instead of manually trying different values, Scikit-learn provides automated tools like **GridSearchCV** and **RandomizedSearchCV**.

---

# GridSearchCV

## What is GridSearchCV?

**GridSearchCV** exhaustively searches through **every possible combination** of specified hyperparameter values.

It trains and evaluates the model for each combination using **Cross-Validation (CV)** and selects the one with the best average performance.

---

## How GridSearchCV Works

Suppose we want to tune a KNN classifier.

Parameter grid:

```python
{
    "n_neighbors": [3, 5, 7],
    "weights": ["uniform", "distance"]
}
```

Possible combinations:

| n_neighbors | weights |
|-------------|----------|
| 3 | uniform |
| 3 | distance |
| 5 | uniform |
| 5 | distance |
| 7 | uniform |
| 7 | distance |

GridSearchCV trains and evaluates the model for **all 6 combinations**.

The combination with the highest cross-validation score is selected.

---

## Example

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()

param_grid = {
    "n_neighbors": [3, 5, 7, 9],
    "weights": ["uniform", "distance"]
}

grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
```

---

## Advantages

- Tests every possible combination.
- Finds the best solution within the specified search space.
- Easy to understand and implement.

---

## Limitations

- Can be very slow for large datasets.
- Computationally expensive when many hyperparameters are involved.

---

# RandomizedSearchCV

## What is RandomizedSearchCV?

**RandomizedSearchCV** searches by testing **a random subset of hyperparameter combinations** instead of every possible one.

Instead of trying all combinations, it randomly selects a specified number (`n_iter`) of combinations.

This makes it much faster than GridSearchCV.

---

## How RandomizedSearchCV Works

Suppose there are 100 possible combinations.

GridSearchCV:

```
Tests all 100 combinations
```

RandomizedSearchCV:

```
Randomly tests only 20 combinations
```

Although it may not always find the absolute best combination, it often finds a very good one in much less time.

---

## Example

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

param_dist = {
    "n_estimators": [100, 200, 300, 500],
    "max_depth": [5, 10, 20, None],
    "min_samples_split": [2, 5, 10]
}

random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42
)

random_search.fit(X_train, y_train)

print(random_search.best_params_)
print(random_search.best_score_)
```

---

## Advantages

- Much faster than GridSearchCV.
- Efficient for large search spaces.
- Can discover good hyperparameter combinations with fewer evaluations.

---

## Limitations

- Does not guarantee finding the absolute best combination.
- Results depend on the randomly selected combinations.

---

# GridSearchCV vs RandomizedSearchCV

| Feature | GridSearchCV | RandomizedSearchCV |
|---------|--------------|--------------------|
| Search Method | Tests every combination | Tests random combinations |
| Speed | Slower | Faster |
| Computational Cost | High | Lower |
| Best for | Small search spaces | Large search spaces |
| Guarantees Best Combination | Yes (within the given grid) | No |

---

# Best Practices

- Use **GridSearchCV** when the number of hyperparameter combinations is small.
- Use **RandomizedSearchCV** when the search space is large or training is expensive.
- Always combine hyperparameter tuning with **Cross-Validation** to obtain reliable performance estimates.
- Evaluate the final tuned model on a separate **test set** to measure its real-world performance.

---

# Summary

- Hyperparameter tuning helps improve a model's performance by selecting the best hyperparameter values.
- **GridSearchCV** evaluates every possible combination and is best for smaller search spaces.
- **RandomizedSearchCV** evaluates a random subset of combinations, making it faster and more efficient for larger search spaces.
- Both methods use **Cross-Validation** to estimate model performance and select the best hyperparameters.
