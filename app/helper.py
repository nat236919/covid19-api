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
from typing import Dict


def get_data() -> Dict[str, pd.DataFrame]:
    """ Get the dataset from https://github.com/CSSEGISandData/2019-nCoV """
    # Download the dataset
    BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/time_series/time_series_2019-ncov-{}.csv'
    CATEGORIES = ['Confirmed', 'Deaths', 'Recovered']
    DATAFRAMES = {}

    # Iterate through all files
    for category in CATEGORIES:
        url = BASE_URL.format(category)
        res = requests.get(url)
        text = res.text

        # Extract data
        data = list(csv.DictReader(text.splitlines()))
        df = pd.DataFrame(data)

        # Data Cleaning
        df = df.iloc[:,[1, -1]] # Select only Country and its last values
        df.columns = ['Country/Region', category]
        pd.to_numeric(df[category])
        df['Country/Region'].replace({'Mainland China': 'China'}, inplace=True)
        df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

        DATAFRAMES[category.lower()] = df

    return DATAFRAMES
