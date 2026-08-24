import pandas as pd

dummy_data = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(data=dummy_data).T
print(df)

df["Suma"] = df.sum(axis = 1)
print(df)