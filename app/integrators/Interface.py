"""
FILE: Interface.py
DESCRIPTION: Interface for API v1 and v2
AUTHOR: Manav Batra
DATE: 15-April-2021
"""

import pandas as pd
from typing import Any, Dict, List
from datetime import datetime

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



class Interface:

    def get_total(self):
        pass

    def get_confirmed(self):
        pass    

    def get_deaths(self):
        pass

    def get_recovered(self):
        pass

    def get_active(self):
        pass    

    def get_timeseries(self):
        pass