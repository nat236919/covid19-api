"""
FILE: get_data.py
DESCRIPTION: Read raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import csv
from typing import Dict

import pandas as pd

from .file_paths import JHU_CSSE_FILE_PATHS
from .helper import (helper_df_cleaning, helper_df_cols_cleaning,
                     helper_get_latest_data_url)


# Get Lookup table
def get_data_lookup_table() -> Dict[str, str]:
    """ Get lookup table (country references for iso2) """
    lookup_table_url = JHU_CSSE_FILE_PATHS['BASE_URL_LOOKUP_TABLE']
    lookup_df = pd.read_csv(lookup_table_url)[['iso2', 'Country_Region']]
    
    # Create referral dictionary
    data = lookup_df.to_dict('records')
    data = {v['iso2']: v['Country_Region'] for v in data}

    return data


# Get Daily Reports Data (General and US)
class DailyReports:
    def __init__(self) -> None: 
        self.latest_base_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS'])
        self.latest_base_US_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US'])

    # Get data from daily reports
    def get_data_daily_reports(self, US: bool = False) -> pd.DataFrame:
        """ Get data from BASE_URL_DAILY_REPORTS """
        # Extract the data
        df = pd.read_csv(self.latest_base_US_url) if US else pd.read_csv(self.latest_base_url)

        # Data pre-processing
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = helper_df_cols_cleaning(df, concerned_columns, int)
        
        return df


# Get data from time series
def get_data_time_series() -> Dict[str, pd.DataFrame]:
    """ Get the dataset from JHU CSSE """
    dataframes = {}

    # Iterate through all files
    for category in JHU_CSSE_FILE_PATHS['CATEGORIES']:
        url = JHU_CSSE_FILE_PATHS['BASE_URL_TIME_SERIES'].format(category)

        # Extract data
        df = pd.read_csv(url)
        df = helper_df_cleaning(df)
        dataframes[category] = df

    return dataframes


# Get data from time series (US)
def get_US_time_series() -> Dict[str, pd.DataFrame]:
    """ Get the dataset of time series for USA """
    dataframes = {}

    # Iterate through categories ('confirmed', 'deaths')
    for category in JHU_CSSE_FILE_PATHS['CATEGORIES'][:-1]:
        url = JHU_CSSE_FILE_PATHS['BASE_URL_US_TIME_SERIES'].format(category)
        
        # Extract data
        df = pd.read_csv(url)
        df = helper_df_cleaning(df)
        concerned_columns = ['Lat', 'Long_']
        df = helper_df_cols_cleaning(df, concerned_columns, float)
        dataframes[category] = df

    return dataframes


# API v1
def get_data(time_series: bool = False) -> Dict[str, pd.DataFrame]:
    """ Get the dataset from JHU CSSE """
    dataframes = {}

    # Iterate through all files
    for category in JHU_CSSE_FILE_PATHS['CATEGORIES']:
        url = JHU_CSSE_FILE_PATHS['BASE_URL_TIME_SERIES'].format(category)

        # Extract data
        df = pd.read_csv(url)
        df = df.fillna('')
        df['Country/Region'] = df['Country/Region'].apply(lambda country_name: country_name.strip()) # Eliminate whitespace
        df['Country/Region'] = df['Country/Region'].str.replace(' ', '_')

        # Data Preprocessing
        if time_series:
            df = df.T.to_dict()
        else:
            df = df.iloc[:, [0, 1, -1]] # Select only Region, Country and its last values
            datetime_raw = list(df.columns.values)[-1] # Ex) '2/11/20 20:44'
            df.columns = ['Province/State', 'Country/Region', category]

            df[category].fillna(0, inplace=True) # Replace empty cells with 0
            df[category].replace('', 0, inplace=True) # Replace '' with 0

            df['datetime'] = datetime_raw
            pd.to_numeric(df[category])
            df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

        dataframes[category.lower()] = df

    return dataframes
