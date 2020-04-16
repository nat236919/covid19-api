"""
FILE: get_data.py
DESCRIPTION: Read raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import requests
import csv
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict


# Base URL for timeseries
BASE_URL_TIME_SERIES = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{}_global.csv'
BASE_URL_US_TIME_SERIES = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{}_US.csv'
CATEGORIES = ['confirmed', 'deaths', 'recovered']
NEW_CATEGORIES = ['confirmed', 'deaths', 'recovered'] # Recovered will be deprecated by the source soon

# Base URL for Daily Reports
BASE_URL_DAILY_REPORTS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'

# Base URL for LookUp Table
BASE_URL_LOOKUP_TABLE = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'


# Get Lookup table
def get_data_lookup_table() -> Dict[str, str]:
    """ Get lookup table (country references for iso2) """
    lookup_table_url = BASE_URL_LOOKUP_TABLE
    lookup_df = pd.read_csv(lookup_table_url)[['iso2', 'Country_Region']]
    
    # Create referral dictionary
    data = lookup_df.to_dict('records')
    data = {v['iso2']: v['Country_Region'] for v in data}

    return data


# Get data from daily reports
def get_data_daily_reports() -> pd.DataFrame:
    """ Get data from BASE_URL_DAILY_REPORTS """
    current_datetime = datetime.utcnow().strftime('%m-%d-%Y')
    base_url = BASE_URL_DAILY_REPORTS.format(current_datetime)

    # Check the latest file
    time_delta = 1
    while(requests.get(base_url).status_code == 404):
        current_datetime = datetime.strftime(datetime.utcnow() - timedelta(time_delta), '%m-%d-%Y')
        base_url = BASE_URL_DAILY_REPORTS.format(current_datetime)
        time_delta += 1

    # Extract the data
    df = pd.read_csv(base_url)

    # Data pre-processing
    concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    df[concerned_columns] = df[concerned_columns].fillna(0) # Replace empty cells with 0
    df[concerned_columns] = df[concerned_columns].replace('', 0) # Replace '' with 0
    df[concerned_columns] = df[concerned_columns].astype(int)
    df['Last_Update'] = current_datetime # Replace Last_Update with its file name
    
    return df


# Get data from time series
def get_data_time_series() -> Dict[str, pd.DataFrame]:
    """ Get the dataset from https://github.com/CSSEGISandData/COVID-19 """
    dataframes = {}

    # Iterate through all files
    for category in NEW_CATEGORIES:
        url = BASE_URL_TIME_SERIES.format(category)

        # Extract data
        df = pd.read_csv(url)
        df = df.fillna('')
        dataframes[category] = df

    return dataframes


# Get data from time series (US)
def get_US_time_series() -> Dict[str, pd.DataFrame]:
    """ Get the dataset of time series for USA """
    dataframes = {}

    # Iterate through categories ('confirmed', 'deaths')
    for category in NEW_CATEGORIES[:-1]:
        url = BASE_URL_US_TIME_SERIES.format(category)
        
        # Extract data
        df = pd.read_csv(url)
        df = df.fillna('')
        df[['Lat', 'Long_']] = df[['Lat', 'Long_']].astype(float)
        dataframes[category] = df

    return dataframes


# API v1
def get_data(time_series: bool = False) -> Dict[str, pd.DataFrame]:
    """ Get the dataset from https://github.com/CSSEGISandData/COVID-19 """
    dataframes = {}

    # Iterate through all files
    for category in CATEGORIES:
        url = BASE_URL_TIME_SERIES.format(category)

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
