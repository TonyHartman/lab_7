import pandas as pd

'''
Выведите имя самого молодого пассажира.
'''

f = pd.read_csv("train.csv")
print(f[f["Age"] == f["Age"].min()]["Name"])