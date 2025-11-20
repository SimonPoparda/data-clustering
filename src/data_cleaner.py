from typing import Tuple
import pandas as pd

class DataCleaner:
    """Class to clean a DataFrame and provide access via getter."""

    def __init__(self, df: pd.DataFrame):
        self._df = df            # original DataFrame (private)
        self._numeric_df = None  # cleaned numeric DataFrame (private)

    def clean(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Apply cleaning steps."""
        self._df = self._df.dropna()
        self._numeric_df = self._df.select_dtypes(include=["float64", "int64"])
        return self._df, self._numeric_df

    @property
    def numeric_df(self):
        """Getter for numeric DataFrame."""
        return self._numeric_df

    @property
    def df(self) -> pd.DataFrame:
        """Getter for cleaned full DataFrame."""
        return self._df
