from pathlib import Path
import pandas as pd

FILE_PATH = Path(__file__)
DIR_PATH = FILE_PATH.parent
DF_PATH = DIR_PATH.joinpath("spotify_songs.csv")

df = pd.read_csv(DF_PATH)


def versatile_func(df, *, head=True, tail=True, describe=True, sample=True):
    if head:
        print("El head del df es:")
        print(df.head())
    if tail:
        print("El tail del df es:")
        print(df.tail())
    if describe:
        print("El describe del df es:")
        print(df.describe())
    if sample:
        print("El sample del df es:")
        print(df.sample())


versatile_func(df, head=True, tail=False, describe=False, sample=True)
versatile_func(df, head=False, tail=False, describe=True, sample=True)
