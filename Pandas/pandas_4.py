import pandas as pd
import numpy as np


def cal_titanic_survival(data):
    titanic_survival = data
    # print(titanic_survival)
    age = titanic_survival["Age"]
    age_is_null = pd.isnull(age)
    # age_null_true = age[age_is_null]
    # print(age_null_true)
    good_ages = titanic_survival["Age"][age_is_null == False]
    # print(good_ages)
    # correct_mean_age = sum(good_ages)/len(good_ages)
    correct_mean_age = titanic_survival["Age"].mean()
    print(correct_mean_age)


def cal_passenger_class(data):
    titanic_survival = data
    passenger_class = [1, 2, 3]
    fares_by_class = {}
    for this_class in passenger_class:
        pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class]
        pclass_fares = pclass_rows["Fare"]
        fares_for_class = pclass_fares.mean()
        fares_by_class[this_class] = fares_for_class
    print(fares_by_class)


def cal_passenger_class_survival(data):
    titanic_survival = data
    passenger_survival = titanic_survival.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
    print(passenger_survival)


def cal_pclass_age(data):
    titanic_survival = data
    passenger_age = titanic_survival.pivot_table(index="Pclass", values="Age")
    print(passenger_age)


def cal_embark_fare_survival(data):
    titanic_survival = data
    port_stats = titanic_survival.pivot_table(index="Embarked", values=["Fare", "Survived"], aggfunc=np.sum)
    print(port_stats)


def dropna(data):
    titanic_survival = data
    drop_na_colums = titanic_survival.dropna(axis=1)
    # print(drop_na_colums)
    new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age", "Sex"])
    print(new_titanic_survival)


titanic_survival_csv = pd.read_csv("titanic_train.csv")
# cal_titanic_survival(titanic_survival_csv)
# cal_passenger_class(titanic_survival_csv)
# cal_passenger_class_survival(titanic_survival_csv)
# cal_pclass_age(titanic_survival_csv)
# cal_embark_fare_survival(titanic_survival_csv)
dropna(titanic_survival_csv)