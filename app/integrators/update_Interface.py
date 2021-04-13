"""
FILE: covid_api_v1_integrator.py
DESCRIPTION: Integrators for API v1
AUTHOR: Elim Lemango
DATE: 12-April-2021
"""
# Import libraries
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd

from models.covid_api_v1_model import (ConfirmedModel, CountriesModel,
                                         CurrentListModel, CurrentModel,
                                         DeathsModel, RecoveredModel,
                                         TimeseriesCoordinatesModel,
                                         TimeseriesDataModel, TimeseriesModel,
                                         TotalModel)
from utils.get_data import get_data
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



class update_Interface:
    def get_deaths(self) -> None:
        pass:

    def get_recovered(self) -> None:
        pass:

    def get_total(self) -> None:
        pass:

    def get_timeseries(self) -> None:
        pass:
