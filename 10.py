import pandas as pd
'''
Найдите доли выживших среди мужчин, среди женщин и среди всех пассажиров.
'''
f = pd.read_csv("train.csv")
male = f[f["Sex"] == 'male'].count()[0]
female = f[f["Sex"] == 'female'].count()[0]

survived_male = f[f["Sex"] == 'male']["Survived"].sum()
survived_female = f[f["Sex"] == 'female']["Survived"].sum()

print("survived male", round(survived_male/male, 3))
print("survived female", round(survived_female/female, 3))
print("survived", round((survived_male + survived_female)/(male + female), 3))