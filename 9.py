import pandas as pd
'''
Удалите столбцы с наибольшим числом уникальных значений.
'''
f = pd.read_csv("train.csv")
f = f.drop(f.nunique()[f.nunique() == f.nunique().max()].index, axis=1)
print(f.columns)
