import pandas as pd
'''
Найдите доли выживших среди возрастных категорий 18-, 18-60, 60+.
'''
f = pd.read_csv("train.csv")
f = f.dropna(axis=0)
age_group_1 = f[f["Age"] < 18].count()[0]
age_group_2 = f[(f["Age"] >= 18) & (f["Age"] < 60)].count()[0]
age_group_3 = f[f["Age"] >= 60].count()[0]

age_group_1_survived = f[f["Age"] < 18]["Survived"].sum()
age_group_2_survived = f[(f["Age"] >= 18) & (f["Age"] < 60)]["Survived"].sum()
age_group_3_survived = f[f["Age"] >= 60]["Survived"].sum()

print("People 18- survived:", round(age_group_1_survived/age_group_1, 2))
print("People 18-60 survived:", round(age_group_2_survived/age_group_2, 2))
print("People 60+ survived:", round(age_group_3_survived/age_group_3, 2))