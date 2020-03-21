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


# API v2
def get_data_api_v2() -> Dict[str, pd.DataFrame]:
    """ Get the dataset from https://github.com/CSSEGISandData/COVID-19 for API v2"""
    dataframes = {}
    
    # Iterate through all files and create dataframes
    for category in CATEGORIES:
        url = BASE_URL.format(category)
        res = requests.get(url)
        text = res.text

        # Extract data
        data = list(csv.DictReader(text.splitlines()))
        df = pd.DataFrame(data)

        # Data pre-processing
        df['Country/Region'] = df['Country/Region'].apply(lambda country_name: country_name.strip()) # delete whitespace
        df = df.iloc[:, [0, 1, -1]] # Select only Region, Country and its last values
        datetime_raw = list(df.columns.values)[-1] # Ex) '2/11/20 20:44'
        df.columns = ['Province/State', 'Country/Region', category]

        df[category].fillna(0, inplace=True) # Replace empty cells with 0
        df[category].replace('', 0, inplace=True) # Replace '' with 0
        pd.to_numeric(df[category])
        df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

        df['datetime'] = datetime_raw

        dataframes[category.lower()] = df

    return dataframes
