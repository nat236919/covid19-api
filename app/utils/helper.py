"""
FILE: helper.py
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
BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'
CATEGORIES = ['Confirmed', 'Deaths', 'Recovered']

# Base URL for Daily Reports
BASE_URL_DAILY_REPORTS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'


# Get data from daily reports
def get_data_daily_reports() -> pd.DataFrame:
    """ Get data from BASE_URL_DAILY_REPORTS """
    current_datetime = datetime.utcnow().strftime('%m-%d-%Y')
    url = BASE_URL_DAILY_REPORTS.format(current_datetime)

    # Check the lastest file
    if requests.get(url).status_code == 404:
        current_datetime = datetime.strftime(datetime.utcnow() - timedelta(1), '%m-%d-%Y')
        url = BASE_URL_DAILY_REPORTS.format(current_datetime)

    res = requests.get(url)
    text = res.text

    # Extract data
    data = list(csv.DictReader(text.splitlines()))
    df = pd.DataFrame(data)
    
    # Data pre-processing
    concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    df[concerned_columns] = df[concerned_columns].fillna(0) # Replace empty cells with 0
    df[concerned_columns] = df[concerned_columns].replace('', 0) # Replace '' with 0
    df[concerned_columns] = df[concerned_columns].astype(int)
    
    return df


# API v1
def get_data(time_series: bool = False) -> Dict[str, pd.DataFrame]:
    """ Get the dataset from https://github.com/CSSEGISandData/COVID-19 """
    dataframes = {}

    # Iterate through all files
    for category in CATEGORIES:
        url = BASE_URL.format(category)
        res = requests.get(url)
        text = res.text

        # Extract data
        data = list(csv.DictReader(text.splitlines()))
        df = pd.DataFrame(data)
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
