from numpy import array
import pandas as pd
import os


dummy_data = {"Cat": ["Python", "is", "a", "Superpower"], "Val": ["Learn", "Python", "it's", "cool"],

  }

df =\
        pd.DataFrame(
       data=dummy_data
)

import requests


def get_df() -> pd.DataFrame:

   #fmt: off
   df = pd.DataFrame(
        data=dummy_data
    )
   #fmt: on

   return df

df = get_df()
print(df)
