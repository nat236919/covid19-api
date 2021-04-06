from datetime import datetime, timedelta
from typing import List, TypeVar
from helper_clean_interface import IHelperClean

import pandas as pd
import pycountry
import requests

class HelperClean(IHelperClean):

# Data preprocessing (DataFrame)
def helper_df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """ Fill all empty values with am empty string (e.g., '') """
    return df.fillna('')


# Data preprocessing (DataFrame's columns)
var_types = TypeVar('ensure_dtype', int, float, str)

def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
    """ Clean certain colomns in a DataFrame """
    df[cols] = df[cols].fillna(0) # Replace empty cells with 0
    df[cols] = df[cols].replace('', 0) # Replace '' with 0

    if ensure_dtype and ensure_dtype in [int, float, str]:
        df[cols] = df[cols].astype(ensure_dtype)

    return df
