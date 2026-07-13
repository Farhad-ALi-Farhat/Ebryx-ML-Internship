# Gradient Descent

Gradient Descent is an optimization algorithm used to minimize a model's loss function by updating its parameters iteratively.

## Workflow

1. Initialize weights
2. Make predictions
3. Compute loss
4. Calculate gradients
5. Update weights
6. Repeat until convergence

---

## Learning Rate

Controls the step size during updates.

- Too Small → Slow training
- Too Large → May overshoot the minimum
- Proper Value → Stable convergence

---

## Types

### Batch Gradient Descent

Uses the entire dataset for each update.

Pros:

- Stable updates

Cons:

- Slow for large datasets

---

### Stochastic Gradient Descent (SGD)

Updates after every training example.

Pros:

- Fast
- Low memory usage

Cons:

- Noisy convergence

---

### Mini-Batch Gradient Descent

Uses small batches of data.

Pros:

- Faster
- Stable
- Most commonly used

---

## Comparison

| Method | Data Used |
|----------|-----------|
| Batch | Entire Dataset |
| SGD | One Sample |
| Mini-Batch | Small Batch |

---

## Key Takeaway

Mini-Batch Gradient Descent is the standard choice for modern deep learning.
