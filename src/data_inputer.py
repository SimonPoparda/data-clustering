import pandas as pd
import numpy as np
from collections import deque

class Inputer:
    """Class to accept user input"""

    def __init__(self):
        self._number = None

    def get_user_input(self, prompt) -> int:
        while True:
            user_input = input(prompt)
            try:
                number = float(user_input)
            except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
                continue

            if not number.is_integer():
                print("Podaj liczbę całkowitą.")
                continue

            number = int(number)

            if number <= 0:
                print("Liczba musi być większa niż 0. Spróbuj ponownie.")
                continue

            self._number = number
            return self._number

    @property 
    def k(self) -> int:
        if self._number is None:
            raise ValueError("Wartość nie została jeszcze ustawiona")
        return self._number
    

class MockDataGenerator:
    def __init__(self, df: pd.DataFrame):
        self._source_df = df.copy()
        self._mock_df = None

    def generate_and_write_mock_df(self, n_rows: int = 150, path: str = '', random_state = None) -> pd.DataFrame:
        """Generate a mock DataFrame using a queue to cycle columns."""

        rng = np.random.default_rng(random_state)
        numeric_cols = self._source_df.select_dtypes(include='number').columns.tolist()
        if not numeric_cols:
            raise ValueError('Brak numerycznych kolumn w danych')

        col_queue = deque(numeric_cols)
        mock_data = {col: [] for col in numeric_cols}

        for i in range(n_rows):
            col = col_queue.popleft()
            mean = float(self._source_df[col].mean())
            std = float(self._source_df[col].std())
            if std <= 0:
                std = 0.1  # prevent zero std

            # generate a single random value
            value = rng.normal(loc=mean, scale=std, size=1)[0]
            mock_data[col].append(value)
            col_queue.append(col)

        mock_df = pd.DataFrame(mock_data)

        if path:
            mock_df.to_parquet(path, engine='pyarrow', index=False)

        self._mock_df = mock_df
        return mock_df

    @property
    def mock_df(self) -> pd.DataFrame:
        return self._mock_df
