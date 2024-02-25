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
def __mydot(xi, w):
    n = len(w)
    result = 0.0
    for j in range(n):
        result += xi[j]*w[j]
    return result

def lin_regress(bias, w, xi):
    return bias + __mydot(xi, w)

def train_linear_regression(X, y):
    print('starting regression')

    ones = np.ones(X.shape[0])
    print("made ones column")

    X = np.column_stack([ones,X])
    print("X with ones")

    XTX = X.T.dot(X)
    print('performed dot')

    XTX_inv = np.linalg.inv(XTX)
    print('performed inv')

    w = XTX_inv.dot(X.T).dot(y)
    print('got weights')
    return w[0], w[1:]

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