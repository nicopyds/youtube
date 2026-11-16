"""Docu for Pylint"""
import pandas as pd

dummy_data = {
    "Cat": ["Python", "is", "a", "Superpower"],
    "Val": ["Learn", "Python", "it's", "cool"],
}

df = pd.DataFrame(data=dummy_data)


def get_df() -> pd.DataFrame:
    """Docu for Pylint"""
    df = pd.DataFrame(data=dummy_data) # pylint: disable=redefined-outer-name

    return df


df = get_df()
print(df)
