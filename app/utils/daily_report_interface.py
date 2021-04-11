from abc import ABCMeta, abstractmethod
from typing import Dict
import pandas as pd

class IDailyReports(metaclass=ABCMeta):


    """Get data from daily reports"""
    @staticmethod
    @abstractmethod
    def get_data_daily_reports(self, US: bool = False) -> pd.DataFrame:
        """Extract the data"""