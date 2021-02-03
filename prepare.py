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
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123, stratify=train_validate.churn)
    return train, validate, test

def prep_telco(df):
    # # drop duplicate values
    df = df.drop_duplicates()

    # add column for tenure in years, rename existing tenure as months
    df = df.rename(columns={'tenure': 'months_tenure'})
    df['years_tenure'] = df.months_tenure / 12    

    drop_list1 = []
 
    # for MVP change No Phone Service and No Internet Service to No
    df.multiple_lines = df.multiple_lines.replace('No phone service', 'No')
    df.online_security = df.online_security.replace('No internet service', 'No')
    df.online_backup = df.online_backup.replace('No internet service', 'No')
    df.device_protection = df.device_protection.replace('No internet service', 'No')
    df.tech_support = df.tech_support.replace('No internet service', 'No')
    df.streaming_tv = df.streaming_tv.replace('No internet service', 'No')
    df.streaming_movies = df.streaming_movies.replace('No internet service', 'No')
    
    # encode columns
    df_dummies = pd.get_dummies(df[['churn', 'multiple_lines', 'online_security', 'online_backup', 'device_protection',
                                      'paperless_billing', 'streaming_movies','streaming_tv', 'tech_support',
                                      'phone_service', 'dependents', 'partner', 'gender']], drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    
    # not working need to debug
    # drop unnecessary columns
    df = df.drop(columns=['churn', 'multiple_lines', 'online_security', 'online_backup', 'device_protection',
                            'paperless_billing', 'streaming_movies', 'streaming_tv', 'tech_support',
                            'phone_service', 'dependents', 'partner', 'gender', 'contract_type', 'payment_type', 'internet_service_type'])

    # rename columns to prefered names
    df = df.rename(columns={'churn_Yes': 'churn', 'multiple_lines_Yes': 'mult_lines', 'online_security_Yes': 'online_sec',
                              'paperless_billing_Yes': 'paperless', 'online_backup_Yes': 'online_backup',
                              'device_protection_Yes': 'device_protect', 'dependents_Yes': 'dependents',
                              'streaming_movies_Yes': 'stream_movies', 'streaming_tv_Yes': 'stream_tv', 
                              'tech_support_Yes': 'tech', 'phone_service_Yes': 'phone', 
                              'partner_Yes': 'partner' , 'gender_Male': 'Male'})
    
    # add column of total "extra services" which is sum of mult_lines, online_sec, online_backup, stream_tv, tech,
    # device_protect, paperless, stream_movies
    df['extra_serv'] = df.mult_lines + df.online_sec + df.online_backup + df.stream_tv + df.tech + df.device_protect + df.paperless + df.stream_movies
    
    # split the data
    train, validate, test = split_dataset(df)
    
    return train, validate, test

