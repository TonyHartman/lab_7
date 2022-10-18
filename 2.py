import pandas as pd
import numpy as np

'''
Дан датафрейм в ячейке ниже, состоящий из 4 единиц на диагонали и nan-ов.
Заполнить его так, чтобы в нем было 8 единиц и 8 двоек. Использовать только fillna.
'''

df = pd.DataFrame([[1, np.nan, np.nan, np.nan],
                   [np.nan, 1, np.nan, np.nan],
                   [np.nan, np.nan, 1, np.nan],
                   [np.nan, np.nan, np.nan, 1]],
                columns=list("ABCD"))

#Способ 1
'''
d = pd.DataFrame([[0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 0, 1], [1, 1, 1, 1]], columns=list("ABCD"))
f = df.fillna(d)
'''
df = df.fillna(1, limit=1).fillna(2)
print(df)
