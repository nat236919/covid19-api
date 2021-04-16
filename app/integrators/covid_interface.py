
# Import libraries

from datetime import datetime
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
from utils.get_data import GetData
import covid_api_v1_integrator
import covid_api_v2_integrator

class covid_interface:
    def current_status(self):
        pass

    def total(self):
        pass

    def confirmed_cases(self):
        pass