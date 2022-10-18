import pandas as pd

'''
Найдите средний возраст пассажиров
'''

f = pd.read_csv("train.csv")
print(f["Age"].dropna().mean())