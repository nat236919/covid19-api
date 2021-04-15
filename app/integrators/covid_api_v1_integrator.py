"""
FILE: covid_api_v1_integrator.py
DESCRIPTION: Integrators for API v1
AUTHOR: Nuttaphat Arunoprayoch
DATE: 02-March-2021
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


# Create a model and its methods
class CovidAPIv1:
    """ Model and Its methods """
    def __init__(self) -> None:
        """ Get data from helper -> the source data """
        list_of_dataframes = get_data()
        self.df_confirmed = list_of_dataframes['confirmed']
        self.df_deaths = list_of_dataframes['deaths']
        self.df_recovered = list_of_dataframes['recovered']

        list_of_time_series = get_data(time_series=True)
        self.df_time_series_confirmed = list_of_time_series['confirmed']
        self.df_time_series_deaths = list_of_time_series['deaths']
        self.df_time_series_recovered = list_of_time_series['recovered']

        self.datetime_raw = self.df_confirmed['datetime'].unique().tolist()[0]
        self.timestamp = datetime.strptime(self.datetime_raw, '%m/%d/%y').timestamp()

    def add_dt_and_ts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """ Add datetime and timestamp to Dict data """
        data['dt'] = self.datetime_raw
        data['ts'] = self.timestamp
        return data

    def get_current_status(self, list_required: bool = False) -> Dict[str, Any]:
        """ Current data (Lastest date) """
        # Create a template
        countries = self.df_confirmed['Country/Region'].unique().tolist()
        current_data = {country: {'confirmed': 0, 'deaths': 0, 'recovered': 0} for country in countries}

        # Extractor
        def _extractor(col: str, df: pd.DataFrame) -> None:
            temp_data = df.T.to_dict()
            for data in temp_data.values():
                try:
                    current_data[data['Country/Region']][col] += int(data[col])
                except:
                    pass
            return None

        # Add data to current_data
        df_list = {'confirmed': self.df_confirmed, 'deaths': self.df_deaths, 'recovered': self.df_recovered}
        [_extractor(col, df) for col, df in df_list.items()]

        # Create Models sorted by Confirmed
        current_data = {country_name: CurrentModel(**country_data) for country_name, country_data
                                                    in sorted(current_data.items(), key=lambda data: data[-1]['confirmed'], reverse=True)}

        # Check if a List form is required
        if list_required:
            current_data['countries'] = [{k: v for k, v in current_data.items()}]
            current_data = {k:v for k, v in current_data.items() if k in ['countries']} # Filter out other keys except countries

        # Add datetime and timestamp
        current_data = self.add_dt_and_ts(current_data)

        return current_data

    def get_confirmed_cases(self) -> Dict[str, int]:
        """ Summation of all confirmed cases """
        data = {'confirmed': sum([int(i) for i in self.df_confirmed['confirmed']])}
        data = ConfirmedModel(**self.add_dt_and_ts(data))
        return data

    def get_deaths(self) -> Dict[str, int]:
        """ Summation of all deaths """
        data = {'deaths': sum([int(i) for i in self.df_deaths['deaths']])}
        data = DeathsModel(**self.add_dt_and_ts(data))
        return data

    def get_recovered(self) -> Dict[str, int]:
        """ Summation of all recovers """
        data = {'recovered': sum([int(i) for i in self.df_recovered['recovered']])}
        data = RecoveredModel(**self.add_dt_and_ts(data))
        return data

    def get_total(self) -> Dict[str, Any]:
        """ Summation of Confirmed, Deaths, Recovered """
        data = {
            'confirmed': self.get_confirmed_cases().confirmed,
            'deaths': self.get_deaths().deaths,
            'recovered': self.get_recovered().recovered
            }
        data = TotalModel(**self.add_dt_and_ts(data))
        return data

    def get_affected_countries(self) -> Dict[str, List]:
        """ The affected countries """
        # Sorted alphabetically and exlucde 'Others'
        sort_filter_others = lambda country_list: sorted([country for country in country_list if country not in ['Others']])
        data = {'countries': sort_filter_others(self.df_confirmed['Country/Region'].unique().tolist())}
        data = CountriesModel(**self.add_dt_and_ts(data))
        return data

    def get_time_series(self) -> Dict[str, Dict]:
        """ Raw time series """
        data = {
            'confirmed': [v for v in self.df_time_series_confirmed.values()],
            'deaths': [v for v in self.df_time_series_deaths.values()],
            'recovered':  [v for v in self.df_time_series_recovered.values()],
        }
        data = self.add_dt_and_ts(data)
        return data
