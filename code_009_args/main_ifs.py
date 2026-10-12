from pathlib import Path

import pandas as pd

FILE_PATH = Path(__file__)
DIR_PATH = FILE_PATH.parent
DF_PATH = DIR_PATH.joinpath("spotify_songs.csv")

df = pd.read_csv(DF_PATH)
print(df.head().T)

def versatile_func(df, head = True, tail = True, describe = True, shape = True):
    if head:
        print("El head del df es:")
        print(df.head())
    if tail:
        print("El tail del df es:")
        print(df.tail())
    if describe:
        print("El describe del df es:")
        print(df.describe())
    if shape:
        print("El shape del df es:")
        print(df.shape)

versatile_func(df, True, False, False)
versatile_func(df, False, False, True)
