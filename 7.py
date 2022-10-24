import pandas as pd
'''
Найдите средние возраста пассажиров по классам обслуживания.
'''

f = pd.read_csv("train.csv")
df = f.groupby(["Pclass"]).agg({"Age": 'mean'})
print(df)
