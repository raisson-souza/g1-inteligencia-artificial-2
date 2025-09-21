import pandas as pd

def get_only_information_systems_students(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra apenas registros de alunos de sistemas de informação."""
    return df[df["course"] == "Sistemas de Informação"]
