import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def date_time():
    # unrate['DATE'] = pd.to_datetime(unrate['DATE'])
    # print(unrate.head(12))
    first_twelve = unrate[0:12]
    plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
    plt.xticks(rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Unemployment Rate')
    plt.title('Monthly Unemployment Trends, 1948')
    plt.show()


def subplot():
    fig = plt.figure(figsize=(3, 3))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.plot(np.random.random_integers(1, 5, 5), np.arange(5))
    ax2.plot(np.arange(10)*3, np.arange(10))
    plt.show()


def two_line():
    unrate['MONTH'] = pd.to_datetime(unrate['DATE']).dt.month
    fig = plt.figure(figsize=(6, 3))
    plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red', label=str(1948))
    plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue', label=str(1948 + 1))
    plt.legend(loc='best')

    plt.show()

unrate = pd.read_csv("UNRATE.csv")
# date_time()
# subplot()
two_line()