# Evaluation Metrics

Evaluation metrics measure how well a machine learning model performs.

## Classification Metrics

### Accuracy

Overall percentage of correct predictions.

Best for balanced datasets.

---

### Precision

Measures how many predicted positives are actually positive.

Use when false positives are costly.

---

### Recall

Measures how many actual positives are correctly identified.

Use when false negatives are costly.

---

### F1-Score

Harmonic mean of Precision and Recall.

Best for imbalanced datasets.

---

## Regression Metrics

### Mean Squared Error (MSE)

Average squared difference between predicted and actual values.

Lower is better.

---

### R² Score

Measures how much variance in the target variable is explained by the model.

Range:

- 1 → Perfect prediction
- 0 → Predicting the mean
- <0 → Worse than baseline

---

## Choosing the Right Metric

| Problem | Metric |
|----------|--------|
| Balanced Classification | Accuracy |
| Imbalanced Classification | F1-score |
| Reduce False Positives | Precision |
| Reduce False Negatives | Recall |
| Regression | MSE, R² |

---

## Key Takeaways

- Choose evaluation metrics based on the problem type and business objective.
- Accuracy alone is not always sufficient, especially for imbalanced datasets.
