import pandas as pd
import re
import os


def load_data(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File path {file_path} was not found')
    
    if re.search(r"\.csv$", file_path, re.IGNORECASE):
        df = pd.read_csv(file_path)
        return df

load_data(r"data/IRIS.csv")
