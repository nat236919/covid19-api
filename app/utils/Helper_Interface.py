"""
FILE: Helper_Interface
DESCRIPTION: Provides an Interface for the helper class
AUTHOR: Faizan Rabbi
DATE: 15-April-2021
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar

import pandas as pd

from abc import ABCMeta, abstractmethod

class HelperInterface(metaclass=ABCMeta):
    var_types = TypeVar('ensure_dtype', int, float, str)

    @abstractmethod
    def helper_df_cleaning(df: pd.DataFrame) -> pd.DataFrame:
        """ Fill all empty values with am empty string (e.g., '') """

    @abstractmethod
    def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
        """ Clean certain columns in a DataFrame """
