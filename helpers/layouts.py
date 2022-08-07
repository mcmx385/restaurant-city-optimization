import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def tuples2euclidean(tuple1, tuple2):
    return euclidean_distance(tuple1[0], tuple1[1], tuple2[0], tuple2[1])


def get_index(setup, word):
    index = []
    for ind, row in enumerate(setup):
        for item in row:
            if item == word:
                index.append((ind, row.index(item)))
    return index


def get_area_index(setup):
    area_index = []
    for ind, row in enumerate(setup):
        for item in row:
            if item == 'A':
                area_index.append((ind, row.index(item)))
    return area_index


def get_table_index(setup):
    table_index = []
    for ind, row in enumerate(setup):
        for item in row:
            if item == 'T':
                table_index.append((ind, row.index(item)))
    return table_index


def get_stove_index(setup):
    stove_index = []
    for ind, row in enumerate(setup):
        for item in row:
            if item == 'S':
                stove_index.append((ind, row.index(item)))
    return stove_index


def get_all_count(setup):
    stoves = 0
    tables = 0
    areas = 0
    for row in setup:
        for item in row:
            if item == 'T':
                tables += 1
            elif item == 'A':
                areas += 1
            elif item == 'S':
                stoves += 1
    return stoves, tables, areas


def max_area_distance(setup):
    area_indexes = get_area_index(setup)
    return tuples2euclidean(max(area_indexes), min(area_indexes))


def max_stove2table_distance(setup):
    stove_indexes = get_stove_index(setup)
    table_indexes = get_table_index(setup)
    return tuples2euclidean(max(stove_indexes), min(table_indexes))


def avg_stock2table_distance(setup):
    stove_indexes = get_stove_index(setup)
    table_indexes = get_table_index(setup)
    distances = []
    for stove in stove_indexes:
        for table in table_indexes:
            distances.append(tuples2euclidean(stove, table))
    return np.mean(distances)


def add_to_counter(counter, key):
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1
    return counter


def get_max_counter(counter):
    max_count = 0
    max_key = None
    for key, val in counter.items():
        if val > max_count:
            max_count = val
            max_key = key
    return max_key
