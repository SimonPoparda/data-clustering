import pandas as pd

def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop missing values"""
    return df.dropna()

def select_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return only numeric_columns"""
    return df.select_dtypes(include=["float64", "int64"])

def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Combine all cleaning steps"""
    df = remove_missing_values(df)
    numeric = select_numeric_columns(df)
    return df, numeric

file_path = r"data/IRIS.csv"
df = pd.read_csv(file_path)
df = clean_data(df)[0]

print(df.describe())
