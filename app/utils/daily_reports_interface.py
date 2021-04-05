"""
FILE: get_data.py
DESCRIPTION: Read raw files from GitHub
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
"""
# Import libraries
import csv

import pandas as pd
from abc import ABCMeta, abstractmethod

class IDailyReports(metaclass=ABCMeta):

    @abstractmethod
    def get_data_daily_reports(self, US: bool = False) -> pd.DataFrame:
        "get data daily reports"