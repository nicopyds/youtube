import inspect
from pathlib import Path

import pandas as pd

FILE_PATH = Path(__file__)
DIR_PATH = FILE_PATH.parent
DF_PATH = DIR_PATH.joinpath("spotify_songs.csv")

df = pd.read_csv(DF_PATH)


def versatile_func(df, *args, **kwargs):

    print(args, type(args), len(args))
    print(kwargs, type(kwargs), len(kwargs))

    for arg in args:
        if hasattr(df, arg):
            print(f"El {arg} del df es:")

            func = getattr(df, arg)

            signature = inspect.signature(func)
            params = {
                name: value
                for name, value in kwargs.items()
                if name in signature.parameters
            }

            print(f"Los params aceptados por la función son: {params}.")

            print(func(**params))


versatile_func(df, "head", "corr", n=10, method="pearson", numeric_only=True)
