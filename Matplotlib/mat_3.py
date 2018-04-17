from StdSuites import rotation

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange


def fun1():
    cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
    norm_reviews = reviews[cols]
    # print(norm_reviews[:1])
    return norm_reviews


def fun2():
    bar_heights = norm_reviews.ix[0, num_cols].values
    print(bar_heights)
    bar_positions = arange(5) + 0.75
    print(bar_positions)
    ax = plt.subplot()
    ax.bar(bar_positions, bar_heights, 0.5)
    plt.show()


def fun3():
    bar_height = norm_reviews.ix[0, num_cols].values
    bar_positions = arange(5) + 1
    tick_position = range(1, 6)
    print(tick_position)
    plt.figure(figsize=(5, 6))
    ax = plt.subplot()

    ax.bar(bar_positions, bar_height, 0.5)
    ax.set_xticks(tick_position)
    ax.set_xticklabels(num_cols, rotation=45)

    ax.set_xlabel('Rating Source')
    ax.set_ylabel('Average Rating')
    ax.set_title('Average User Rating For Avengers: Age of Ultron(2015)')
    plt.show()


def fun4():
    fig = plt.figure(figsize=(5,10))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
    ax1.set_xlabel('Fandango')
    ax1.set_ylabel('Rotten Tomatoes')

    ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
    ax2.set_xlabel('Rotten Tomatoes')
    ax2.set_ylabel('Fandango')
    plt.show()


reviews = pd.read_csv('fandango_score_comparison.csv')
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = fun1()
# fun2()
# fun3()
fun4()
