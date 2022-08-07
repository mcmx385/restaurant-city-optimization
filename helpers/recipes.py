import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def lookup_time(ingredients, sources, x):
    time = 0
    for key, val in x.items():
        sources_df = ingredients[ingredients['name'] == key]['source']
        sources_df = np.array(sources_df)
        if len(sources_df) < 1:
            time += sources['market'].time*val
        else:
            time += sources[sources_df[0]].time*val
    return time


def lookup_cost(ingredients, sources, x):
    cost = 0
    for key, val in x.items():
        sources_df = ingredients[ingredients['name'] == key]['source']
        sources_df = np.array(sources_df)
        if len(sources_df) < 1:
            cost += sources['market'].cost*val
        else:
            cost += sources[sources_df[0]].cost*val
    return cost


def lookup_difficulty(ingredients, sources, x):
    difficulty = 0
    for key, val in x.items():
        sources_df = ingredients[ingredients['name'] == key]['source']
        sources_df = np.array(sources_df)
        if len(sources_df) < 1:
            difficulty += sources['market'].difficulty*val
        else:
            difficulty += sources[sources_df[0]].difficulty*val
    return difficulty
