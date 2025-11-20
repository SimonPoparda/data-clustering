import pandas as pd
import re
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File path {file_path} was not found")
    
    if not re.search(r"\.csv$", file_path, re.IGNORECASE):
        raise ValueError("Plik nie jest CSV")
    
    df = pd.read_csv(file_path)
    return df