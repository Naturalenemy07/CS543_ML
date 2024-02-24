import numpy as np
import pandas as pd

"""""""""""""""
Error messages
"""""""""""""""
errZero = "Cannot divide by zero."
errStr = "String or characters cannot be input to mathematical equation, please use integer only."
errFlt = "Cannot use float number, please use integer only."
errIdx = "Upper bound index must be greater than lower bound index."

"""""""""
Functions
"""""""""
def __checkOne(input):
    if input == 0:
        raise ZeroDivisionError(errZero)
    elif type(input) is float:
        raise ValueError(errFlt)
    elif type(input) is str:
        raise ValueError(errStr)


def exampleTwoOne(input_x:int) -> float:
    """
    Calculate f(x)=(1/x + 3*x) based on input x

    :param int input_x: input to equation

    :return: f(x)
    :rtype: float

    :raises ZeroDivisionError: if input_x is equal to zero
    :raises ValueError: if input_x is a string
    """

def dot(xi, w):
    n = len(w)
    result = 0.0
    for j in range(n):
        result += xi[j]*w[j]
    return result

def lin_regress(bias, w, xi):
    return bias + dot(xi, w)

def train_val_test_split(data, trainP:float, valP:float, testP:float, label:str, const = 1):
    """
    Split dataset into training, validation and testing datasets

    :param Pandas Dataframe data: input data
    :param float trainP: percentage of data to hold for training, between 0 and 1
    :param float valP: percentage of data to hold for validation, between 0 and 1
    :param float testP: percentage of data to hold for testing, between 0 and 1

    :return: training, validation and testing datasets
    :rtype: Pandas Dataframes
    """
    length = len(data)

    n_val = int(valP * length)
    n_test = int(testP * length)
    n_train = int(trainP * length)

    np.random.seed(const)
    idx = np.arange(length)
    np.random.shuffle(idx)

    data_shuffled = data.iloc[idx]

    data_train = data_shuffled.iloc[:n_train].copy()
    data_val = data_shuffled.iloc[n_train:n_train+n_val].copy()
    data_test = data_shuffled.iloc[n_train+n_val:].copy()

    return data_train, data_val, data_test