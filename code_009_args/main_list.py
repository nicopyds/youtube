from pathlib import Path
import pandas as pd

FILE_PATH = Path(__file__)
DIR_PATH = FILE_PATH.parent
DF_PATH = DIR_PATH.joinpath("spotify_songs.csv")

df = pd.read_csv(DF_PATH)


def versatile_func(df, attrs):
    for attr in attrs:
        print(attr(df))


versatile_func(df, [pd.DataFrame.head, pd.DataFrame.describe])
