import numpy as np
import pandas as pd

"""""""""
Functions
"""""""""

def lin_regress(bias, w, xi):
    """
    Calculated the linear regression line

    :param float bias: intercept
    :param vector w: features
    :param vector xi: slopes

    :return: predicted y
    :rtype: float
    """
    return bias + xi.dot(w)


def train_linear_regression(X, y, r=0.0):
    """
    Calculated the linear regression line

    :param vector X: Numpy matrix
    :param vector y: vector
    :param float r: number to eliminate errors in code

    :return:
    :rtype:
    """
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
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

def rsme(y, y_pred)->float:
    """
    Calculated root mean square

    :param vector y: actual 
    :param vector y_pred: predicted


    :return: root meas square value
    :rtype: float
    """
    error = y_pred - y
    mse = (error**2).mean()
    return np.sqrt(mse)


def MLB_ch2_prepare_X(input_df, base_columns):
    """
    Create new columns for one-hot encoding categorical data

    :param Pandas Dataframe input_df: input dataframe to alter
    :param vector base_columns: columns of interest

    :return: Altered Dataframe with new columns
    :rtype: Pandas Dataframe
    """
    input_df = input_df.copy()
    features = base_columns.copy()

    input_df['age'] = 2024 - input_df.year
    features.append('age')

    for v in [2,3,4]:
        feature = 'num_doors_%s' % v
        input_df[feature] = (input_df['number_of_doors'] == v).astype(int)
        features.append(feature)

    for v in ['chevrolet','ford','volkswagon','toyota','dodge']:
        feature = 'is_make_%s' % v
        input_df[feature] = (input_df['make'] == v).astype(int)
        features.append(feature)
    
    for v in ['regular_unleaded','premium_unleaded_(required)','premium_unleaded_(recommended)','flex-fuel_(unleaded/e85)']:
        feature = 'is_type_%s' % v
        input_df[feature] = (input_df['engine_fuel_type'] == v).astype(int)
        features.append(feature)

    for v in ['automatic','manual','automated_manual']:
        feature = 'is_transmission_%s' % v
        input_df[feature] = (input_df['transmission_type'] == v).astype(int)
        features.append(feature)
    
    for v in ['front_wheel_drive','rear_wheel_drive','all_wheel_drive','four_wheel_drive']:
        feature = 'is_driven_wheels_%s' % v
        input_df[feature] = (input_df['driven_wheels'] == v).astype(int)
        features.append(feature)

    for v in ['crossover','flex_fuel','luxury','luxury_performance','hatchback']:
        feature = 'is_mc_%s' % v
        input_df[feature] = (input_df['market_category'] == v).astype(int)
        features.append(feature)
    
    for v in ['compact','midsize','large']:
        feature = 'is_size_%s' % v
        input_df[feature] = (input_df['vehicle_size'] == v).astype(int)
        features.append(feature)

    for v in ['sedan','4dr_suv','coupe','convertible','4dr_hatchback', 'regular_cab_pickup']:
        feature = 'is_style_%s' % v
        input_df[feature] = (input_df['vehicle_style'] == v).astype(int)
        features.append(feature)
    
    df_num_prep = input_df[features]
    df_num_prep = df_num_prep.fillna(0)
    X_prep = df_num_prep.values
    return X_prep