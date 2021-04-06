from datetime import datetime, timedelta
from typing import List, TypeVar
from abc import ABCMeta, abstractmethod

import pandas as pd
import pycountry
import requests

class IHelperClean(metaclass=ABCMeta):

@staticmethod
@abstractmethod
def helper_df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """ Fill all empty values with am empty string (e.g., '') """


@staticmethod
@abstractmethod
def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
    """ Clean certain colomns in a DataFrame """
