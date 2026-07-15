"""Data Loading Module"""

import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from given path."""
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()