import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np


def series_type():
    print(type(series_film))
    # print(series_film[0:5])
    print(series_rt[0:5])


def series_values():
    film_names = series_film.values
    # print(type(film_names))
    rt_scores = series_rt.values
    series_custom_scores = Series(rt_scores, index=film_names)
    # series_custom[['Minions(2015)', 'Leviathan(2014)']]
    series_custom_scores[['The Water Diviner (2015)', 'Irrational Man (2015)']]
    # print(series_custom_scores)
    # fiveten = series_custom_scores[5:10]
    # print(fiveten)
    # original_index = series_custom_scores.index.tolist()
    # sorted_index = sorted(original_index)
    # sorted_by_index = series_custom_scores.reindex(sorted_index)
    # print(sorted_by_index)
    series_custom_films = Series(film_names, index=rt_scores)
    # sorted_scores = sorted(series_custom_films.index.tolist())
    # print(sorted_scores)
    # sorted_by_scores = series_custom_films.reindex(sorted_scores)
    # print(sorted_by_scores)
    max_score = np.max(series_custom_scores)
    series_max = series_custom_films[max_score]
    print(series_max)

    np_sin = np.sin(series_custom_scores)
    result = pd.concat([np_sin, series_custom_scores], axis=1)
    # print(result)
    # np_add = np.add(series_custom_scores, np_sin)
    # print(np_add)


def series_values2():
    series_custom = Series(series_rt.values, index=fandango['FILM'])
    series_greater_than_50 = series_custom[series_custom > 50]
    # print(series_greater_than_50)
    criteria_one = series_custom > 50
    criteria_two = series_custom < 75
    both_criteria = series_custom[criteria_one & criteria_two]
    print(both_criteria)
    print(len(both_criteria))


def series_mean():
    rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
    rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
    rt_mean = (rt_critics + rt_users)/2
    print(rt_mean)


def dataFrame_index():
    fandango_films = fandango.set_index('FILM', drop=False)
    # print(fandango_films.index)
    fandango_films["Avengers: Age of Ultron (2015)": "Hot Tub Time Machine 2 (2015)"]
    print(fandango_films.loc["Avengers: Age of Ultron (2015)": "Hot Tub Time Machine 2 (2015)"].index)


def series_lambda():
    fandango_films = fandango.set_index('FILM', drop=False)
    # print(fandango_films.index)
    types = fandango_films.dtypes
    # print(types)
    float_columns = types[types.values == 'float64'].index
    # print(float_columns)
    float_df = fandango_films[float_columns]
    # print(float_df)
    deviations = float_df.apply(lambda x: np.std(x), axis=1)
    # print(deviations)
    rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
    rt_mt_user.apply(lambda x: np.std(x), axis=1)
    print(rt_mt_user)


fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
series_rt = fandango['RottenTomatoes']
# series_type()
# series_values()
# series_values()
# series_values2()
# series_mean()
# dataFrame_index()
series_lambda()
