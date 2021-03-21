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

 class Deaths:

  def __init__(self) -> None:
     	   self.df_deaths = list_of_dataframes['deaths']

  def get_deaths(self) -> Dict[str, int]:
        """ Summation of all deaths """
        data = {'deaths': sum([int(i) for i in self.df_deaths['deaths']])}
        data = DeathsModel(**self.add_dt_and_ts(data))


 class ConfirmedAndDeathsRatio:

     def __init__(self,deaths, confirmed) 
      self.deaths = deaths
      self.confirmed = confirmed
      self.confirmedDeathRatio confirmed.sum - deaths.sum

      return confirmedDeathRatio

