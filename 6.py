import pandas as pd

'''
Посчитайте доли пассажиров по классам обслуживания (Pclass)
'''

f = pd.read_csv("train.csv")
people_number = f.shape[0]
f = f.groupby(["Pclass"])["Pclass"].count() / people_number
print(f)