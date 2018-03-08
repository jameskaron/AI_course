import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("titanic_train.csv")
# print(titanic_survival)
age = titanic_survival["Age"]
age_is_null = ""
