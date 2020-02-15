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
from datetime import datetime
from typing import Dict


# Set global variables
BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'
CATEGORIES = ['Confirmed', 'Deaths', 'Recovered']


def get_data() -> Dict[str, pd.DataFrame]:
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

        # Data Preprocessing
        df = df.iloc[:,[0, 1, -1]] # Select only Region, Country and its last values
        datetime_raw = list(df.columns.values)[-1] # Ex) '2/11/20 20:44'
        df.columns = ['Province/State', 'Country/Region', category]
        df['Country/Region'] = df['Country/Region'].str.replace(' ', '_')
        df['datetime'] = datetime_raw
        pd.to_numeric(df[category])
        df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

        dataframes[category.lower()] = df

    return dataframes


def get_time_series() -> Dict[str, Dict]:
    """ Get the time series data from the source """
    time_series = {}

    # Iterate through all files
    for category in CATEGORIES:
        url = BASE_URL.format(category)
        res = requests.get(url)
        text = res.text

        # Extract data
        data = list(csv.DictReader(text.splitlines()))
        df = pd.DataFrame(data)
        df['Country/Region'] = df['Country/Region'].str.replace(' ', '_')
        time_series[category.lower()] = df.T.to_dict()

    return time_series
