from pathlib import Path

import pandas as pd

FILE_PATH = Path(__file__)
DIR_PATH = FILE_PATH.parent
DF_PATH = DIR_PATH.joinpath("spotify_songs.csv")

df = pd.read_csv(DF_PATH)

def versatile_func(df, *args):
    print(args, type(args), len(args))
    for arg in args:
        if hasattr(df, arg):
            print(f"El {arg} del df es:")
            func = getattr(df, arg)
            print(func())


versatile_func(df, "head", "tail")
versatile_func(df, "tail", "describe")

