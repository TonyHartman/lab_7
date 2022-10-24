import pandas as pd
'''
Найдите доли выживших по классам обслуживания.
'''
f = pd.read_csv("train.csv")
people_in_class_1 = f[f["Pclass"] == 1].count()[0]
people_in_class_2 = f[f["Pclass"] == 2].count()[0]
people_in_class_3 = f[f["Pclass"] == 3].count()[0]

people_in_class_1_sur = f[f["Pclass"] == 1]["Survived"].sum()
people_in_class_2_sur = f[f["Pclass"] == 2]["Survived"].sum()
people_in_class_3_sur = f[f["Pclass"] == 3]["Survived"].sum()

print("people survived in class 1:", round(people_in_class_1_sur/ people_in_class_1, 2))
print("people survived in class 1:", round(people_in_class_2_sur/ people_in_class_2, 2))
print("people survived in class 1:", round(people_in_class_3_sur/ people_in_class_3, 2))
