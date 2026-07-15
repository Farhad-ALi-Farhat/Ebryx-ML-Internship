"""Model Training Module"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_model(X, y):
    """Train a simple regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    print(f"Model trained. MSE: {mse}")
    return model


def save_model(model, path: str):
    """Save trained model."""
    joblib.dump(model, path)