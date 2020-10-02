import numpy as np
import pandas as pd

import pathlib

# In this file, you'll put all the functions for loading data.

_data_dir = pathlib.Path(__file__).parent.joinpath("data")

def read_query_part_X(n: {1, 2, 3}):
    return pd.read_csv(_data_dir.joinpath(f"query_part_{n}.csv"))

def read_query_part_1():
    return read_query_part_X(1)

def read_query_part_2():
    return read_query_part_X(2)

def read_query_part_3():
    return read_query_part_X(3)