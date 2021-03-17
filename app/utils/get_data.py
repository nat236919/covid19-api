"""
FILE: get_data.py
DESCRIPTION: Read raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
from typing import Dict, TypeVar, List
from datetime import datetime, timedelta

import pandas as pd
import requests
import csv


from .file_paths import JHU_CSSE_FILE_PATHS

# Get Lookup table
def get_data_lookup_table() -> Dict[str, str]:
    """ Get lookup table (country references for iso2) """
    lookup_table_url = JHU_CSSE_FILE_PATHS['BASE_URL_LOOKUP_TABLE']
    lookup_df = pd.read_csv(lookup_table_url)[['iso2', 'Country_Region']]
    
    # Create referral dictionary
    data = lookup_df.to_dict('records')
    data = {v['iso2']: v['Country_Region'] for v in data}

    return data


# Get COVID data (API v2)
class COVIDDataForAPIv2:
    # Get data from daily reports
    @staticmethod
    def get_data_daily_reports(US: bool = False) -> pd.DataFrame:
        """ Get data from BASE_URL_DAILY_REPORTS """
        # Extract the data
        df = pd.read_csv(COVIDDataForAPIv2._get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS_US'])) if US else pd.read_csv(COVIDDataForAPIv2._get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS']))

        # Data pre-processing
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = COVIDDataForAPIv2._df_cols_cleaning(df, concerned_columns, int)
        
        return df
    
    # Get data from time series
    @staticmethod
    def get_data_time_series() -> Dict[str, pd.DataFrame]:
        """ Get the dataset from JHU CSSE """
        dataframes = {}

        # Iterate through all files
        for category in JHU_CSSE_FILE_PATHS['CATEGORIES']:
            url = JHU_CSSE_FILE_PATHS['BASE_URL_TIME_SERIES'].format(category)

            # Extract data
            df = pd.read_csv(url)
            df = COVIDDataForAPIv2._df_cleaning(df)
            dataframes[category] = df

        return dataframes


    # Get data from time series (US)
    @staticmethod
    def get_US_time_series() -> Dict[str, pd.DataFrame]:
        """ Get the dataset of time series for USA """
        dataframes = {}

        # Iterate through categories ('confirmed', 'deaths')
        for category in JHU_CSSE_FILE_PATHS['CATEGORIES'][:-1]:
            url = JHU_CSSE_FILE_PATHS['BASE_URL_US_TIME_SERIES'].format(category)
            
            # Extract data
            df = pd.read_csv(url)
            df = COVIDDataForAPIv2._df_cleaning(df)
            concerned_columns = ['Lat', 'Long_']
            df = COVIDDataForAPIv2._df_cols_cleaning(df, concerned_columns, float)
            dataframes[category] = df

        return dataframes

    # Get latest data
    @staticmethod
    def _get_latest_data_url(base_url: str) -> str:
        """ Get the latest base URL """
        time_format = '%m-%d-%Y'
        current_datetime = datetime.utcnow().strftime(time_format)
        latest_base_url = base_url.format(current_datetime)

        # Check the latest file by re-acquiring file
        # If not found, continue
        time_delta = 1
        while requests.get(latest_base_url).status_code == 404:
            current_datetime = datetime.strftime(datetime.utcnow() - timedelta(time_delta), time_format)
            latest_base_url = base_url.format(current_datetime)
            time_delta += 1

        return latest_base_url
    
    # Data preprocessing (DataFrame's columns)
    var_types = TypeVar('ensure_dtype', int, float, str)
    @staticmethod
    def _df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
        """ Clean certain colomns in a DataFrame """
        df[cols] = df[cols].fillna(0) # Replace empty cells with 0
        df[cols] = df[cols].replace('', 0) # Replace '' with 0

        if ensure_dtype and ensure_dtype in [int, float, str]:
            df[cols] = df[cols].astype(ensure_dtype)

        return df
    

    # Data preprocessing (DataFrame)
    @staticmethod
    def _df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
        """ Fill all empty values with am empty string (e.g., '') """
        return df.fillna('')



# Get COVID data (API v1)
class COVIDDataForAPIv1:
    # Get COVID data for API v1
    @staticmethod
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
