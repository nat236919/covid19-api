"""
FILE: ihelper.py
DESCRIPTION: All functions for helping small tasks
AUTHOR: Nuttaphat Arunoprayoch
DATE: 04-April-2020
"""
# Import libraries
from datetime import datetime, timedelta
from typing import List, TypeVar

from panda import pd
from abc import ABCMeta, abstractmethod

class IHelper(metaclass=ABCMeta):

    @abstractmethod
    def helper_df_cols_cleaning(df: pd.DataFrame, cols: List[str], ensure_dtype: var_types = None) -> pd.DataFrame:
        "helper function"

    @abstractmethod
    def helper_get_latest_data_url(base_url: str) -> str:
        "helper function"

