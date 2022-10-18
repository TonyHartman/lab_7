import pandas as pd
import numpy as np

'''
Дан датафрейм в ячейке ниже, состоящий из 4 единиц на диагонали и nan-ов.
Заполнить его так, чтобы в нем было 8 единиц и 8 двоек. Использовать только fillna.
Из полученного датафрейма удалить столбец (или столбцы) с минимальной суммой значений.
'''

df = pd.DataFrame([[1, np.nan, np.nan, np.nan],
                   [np.nan, 1, np.nan, np.nan],
                   [np.nan, np.nan, 1, np.nan],
                   [np.nan, np.nan, np.nan, 1]],
                columns=list("ABCD"))

df = df.fillna(1, limit=1).fillna(2)
drop_columns = df.sum()[df.sum() == df.sum().min()].index
df = df.drop(drop_columns, axis=1)
print(df)

