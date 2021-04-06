"""
FILE: helper.py
DESCRIPTION: All functions for helping small tasks
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar

import pandas as pd
import pycountry
import requests

# Get latest data
def helper_get_latest_data_url(base_url: str) -> str:
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


# Look up a country name from a country code
def helper_lookup_country(country: str) -> str:
    """ Look up a country name from a country code """
    country_name = pycountry.countries.lookup(country).name # Select the first portion of str when , is found
    if ',' in country_name:
        country_name = country_name.split(',')[0]
    elif ' ' in country_name:
        country_name = country_name.split(' ')[-1]
    return country_name
