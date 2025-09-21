import pandas as pd

def treat_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Colunas não utilizadas serão removidas."""
    return df.drop(columns=["birthdate", "sex", "city", "week_day"])
