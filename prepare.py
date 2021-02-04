import pandas as pd
import numpy as np
import acquire

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

import warnings
warnings.filterwarnings("ignore")

# this function not working, need to debug
# def drop_cols(df, col_list):
#     df = df.drop(columns=[col_list])
#     return df

def split_dataset(df):
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.target)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123, stratify=train_validate.target)
    return train, validate, test

def prep_data(df):
    '''
    prepares the data for EDA (exploritory data analysis)
    '''
    print("Preparing Data...")
    # split the data
    train, validate, test = split_dataset(df)
    print("Prepare Completed")
    print("train shape,", "validate shape,", "test shape")
    print(train.shape, validate.shape, test.shape)
    return train, validate, test

