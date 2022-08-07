import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def str2arr(x):
    return str(x).split(', ') if not x is None else x


def arr2count(arr):
    unique, counts = np.unique(arr, return_counts=True)
    return dict(zip(unique, counts))
