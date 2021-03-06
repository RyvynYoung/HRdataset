#### Environment Imports #####
import pandas as pd 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


#### Functions #####

def get_data():
    '''
    This function reads the HRtrain dataset and does initial cleaning.
    '''
    # read in .csv file downloaded from Kaggle
    HRtrain = pd.read_csv('aug_train.csv')
    # Drop unique identifier, column enrollee_id
    HRtrain = HRtrain.drop(columns='enrollee_id')
    # fill nulls with 'not_identified'
    HRtrain = HRtrain.fillna('not_identified')
    # convert target to int
    HRtrain['target'] = pd.Series(HRtrain.target, dtype='int32')
    return HRtrain

def get_test_data():
    '''
    This function reads the HRtest dataset and performs same initial cleaning as on HRtrain
    '''
    # read in .csv file downloaded from Kaggle
    HRtest = pd.read_csv('aug_test.csv')
    # Drop unique identifier, column enrollee_id
    HRtest = HRtest.drop(columns='enrollee_id')
    # fill nulls with 'not_identified'
    HRtest = HRtest.fillna('not_identified')
    return HRtest

def run():
    print("Acquire: compiling raw data files...")
    df = get_data()
    print("Acquire: Completed!")
    return df
