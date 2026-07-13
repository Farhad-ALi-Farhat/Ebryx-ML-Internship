# Overfitting vs Underfitting

## Underfitting

The model is too simple to learn the data.

Characteristics:

- High Bias
- Low Accuracy
- Poor Generalization

Solutions:

- Increase model complexity
- Add features
- Train longer

---

## Overfitting

The model memorizes the training data, including noise.

Characteristics:

- High Variance
- Excellent Training Accuracy
- Poor Test Accuracy

Solutions:

- More data
- Dropout
- Regularization
- Early Stopping

---

## Comparison

| Underfitting | Overfitting |
|--------------|-------------|
| High Bias | High Variance |
| Low Train Accuracy | High Train Accuracy |
| Low Test Accuracy | Low Test Accuracy |

---

## Goal

Build a model that generalizes well to unseen data.
