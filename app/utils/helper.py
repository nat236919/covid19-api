"""
FILE: helper.py
DESCRIPTION: All functions for helping small tasks
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
import pycountry
import pandas as pd
from typing import List


# Data preprocessing (DataFrame)
def helper_df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """ Fill all empty values with am empty string (e.g., '') """
    return df.fillna('')


# Data preprocessing (DataFrame's columns)
def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: None) -> pd.DataFrame:
    """ Clean certain colomns in a DataFrame """
    df[cols] = df[cols].fillna(0) # Replace empty cells with 0
    df[cols] = df[cols].replace('', 0) # Replace '' with 0

    if ensure_dtype and ensure_dtype in [int, float, str]:
        df[cols] = df[cols].astype(ensure_dtype)

    return df


# Look up a country name from a country code
def lookup_country(country: str) -> str:
    """ Look up a country name from a country code """
    country_name = pycountry.countries.lookup(country).name # Select the first portion of str when , is found
    if ',' in country_name:
        country_name = country_name.split(',')[0]
    elif ' ' in country_name:
        country_name = country_name.split(' ')[-1]
    return country_name
