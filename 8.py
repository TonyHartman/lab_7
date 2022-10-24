import pandas as pd
'''
Удалите столбец с наибольшим числом пропусков.
'''
f = pd.read_csv("train.csv")
f = f.drop(f.isna().sum()[f.isna().sum() == f.isna().sum().max()].index, axis=1)
print(f.columns)

