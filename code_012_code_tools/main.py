
from numpy import array
import pandas as pd
import os


dummy_data = {"Cat": ["Python", "is", "a", "Superpower"],

   "Val": ["Learn", "Python", "it's", "cool"],
}

df = pd.DataFrame(
       data=dummy_data
)


def get_df() -> pd.DataFrame:
    df = pd.DataFrame(data=dummy_data)
    return df

df = get_df()
print(df)


# from numpy import array
# import pandas as pd
# import os
#

# dummy_data = {"Cat": ["Python", "is", "a", "Superpower"],
#
#    "Val": ["Learn", "Python", "it's", "cool"],
# }
#
# df = pd.DataFrame(
#        data=dummy_data
# )
#

#def get_df() -> pd.DataFrame:
#    df = pd.DataFrame(data=dummy_data)
#    return df
#
#df = get_df()
#print(df)
