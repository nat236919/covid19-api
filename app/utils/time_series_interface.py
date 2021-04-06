from abc import ABCMeta, abstractmethod
from typing import Dict
import pandas as pd

class IDataTimeSeries(metaclass=ABCMeta):

    """ Get the tiemseires dataset from JHU CSSE and Prepare DataFrames """
    @staticmethod
    @abstractmethod
    def get_data_time_series(self, US: bool = False) -> Dict[str, pd.DataFrame]:
        """ Get the dataset from JHU CSSE """

    @staticmethod
    @abstractmethod
    def _clean_timeseries_dataframe(self, df: pd.DataFrame, US: bool = False) -> pd.DataFrame:
        "clean the dataset"
