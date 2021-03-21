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


 class Confirmed:


 def __init__(self) -> None:
     	self.df_confirmed = list_of_dataframes['confirmed']

 def get_confirmed_cases(self) -> Dict[str, int]:
        """ Summation of all confirmed cases """
        data = {'confirmed': sum([int(i) for i in self.df_confirmed['confirmed']])}
        data = ConfirmedModel(**self.add_dt_and_ts(data))
        return data

class Recovered:

   def __init__(self) -> None:
   self.df_recovered = list_of_dataframes['recovered']

   def get_recovered(self) -> Dict[str, int]:
        """ Summation of all recovers """
        data = {'recovered': sum([int(i) for i in self.df_recovered['recovered']])}
        data = RecoveredModel(**self.add_dt_and_ts(data))
        return data

class ConfirmedAndRecoveredDifference:

     def __init__(self,deaths, confirmed) 
      self.recovered = recovered
      self.confirmed = confirmed
      self.confirmedDeathDifference confirmed.sum - recovered.sum

      return confirmedDeathDifference

