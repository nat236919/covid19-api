# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict, List

import pandas as pd

from models.base_model import ResponseModel
from models.covid_api_v2_model import (ActiveModel, ConfirmedModel,
                                         CountryModel, CurrentModel,
                                         CurrentUSModel, DeathsModel,
                                         RecoveredModel,
                                         TimeseriesCaseCoordinatesModel,
                                         TimeseriesCaseDataModel,
                                         TimeseriesCaseModel,
                                         TimeseriesGlobalModel,
                                         TimeseriesUSCoordinatesModel,
                                         TimeseriesUSDataModel,
                                         TimeseriesUSInfoModel,
                                         TimeseriesUSModel, TotalModel)
from utils.get_data import (DailyReports, DataTimeSeries,
                              get_data_lookup_table)
import api_v1_interface
from covid_api_v2_integrator import CovidAPIv2

class CovidAPIv2Adapter(APIv1):
    
    def __init__(self, CovidAPIv2: covidapiv2):
        # We get a reference to the object that we are adapting 
        # through the constructor
        self.CovidAPIv2 = covidapiv2
    
    @wrap_data
    def get_deaths(self) -> DeathsModel:
        """ Summation of all deaths """
        self.df = self.CovidAPIv2.daily_reports.get_data_daily_reports() # Get base data
        data = DeathsModel(
            deaths=int(self.df['Deaths'].sum())
        )
        return data

    @wrap_data
    def get_recovered(self) -> RecoveredModel:
        """ Summation of all recovers """
        self.df = self.CovidAPIv2.daily_reports.get_data_daily_reports() # Get base data
        data = RecoveredModel(
            recovered=int(self.df['Recovered'].sum())
        )
        return data

    @wrap_data
    def get_total(self) -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        self.df = self.CovidAPIv2.daily_reports.get_data_daily_reports() # Get base data
        data = TotalModel(
            confirmed=int(self.df['Confirmed'].sum()),
            deaths=int(self.df['Deaths'].sum()),
            recovered=int(self.df['Recovered'].sum()),
            active=int(self.df['Active'].sum())
        )
        return data

    @wrap_data
    def get_time_series(self, case: str) -> List[Any]:
        """ Get time series data from a given case
            1.) global
            2.) confirmed, deaths, recovered
        """
        self.df_time_series = self.CovidAPIv2.time_series.get_data_time_series() # Get base data

        if case not in ['global']:
            raw_data = self.CovidAPIv2.df_time_series[case].T.to_dict()
            data = self.__extract_time_series(raw_data)
        else:
            raw_data = self.df_time_series
            data = self.__extract_time_series_global(raw_data)

        return data
