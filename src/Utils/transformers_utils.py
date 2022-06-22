import numpy as np
import pandas as pd


def list_element_to_int(my_list: list):
    """
    returns elements of a list as integers
    """
    try:
        res = [int(x) for x in my_list]
        if len(res) > 2:
            return res[0] * 3600 + res[1] * 60 + res[2]
        else:
            return res[0] * 60 + res[1]
    except Exception as e:
        return np.nan


def hms_to_secs(time: pd.Series):
    """
    Converts time in the h:m:s format to seconds using the list_element_to_int fun
    """
    temp = time.apply(lambda x: x.split(".")[0])  # remove decimals (all after .)
    temp2 = temp.str.split(":")
    return temp2.apply(lambda x: list_element_to_int(x))
