"""
FILE: covid_model_api_v2.py
DESCRIPTION: Covid-19 Model for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 14-March-2020
"""
# Import libraries
from datetime import datetime
from functools import wraps
from typing import Any, Dict, List

import pandas as pd
from utils.get_data import (get_data_daily_reports, get_data_daily_reports_us,
                            get_data_lookup_table, get_data_time_series,
                            get_US_time_series)


class CovidAPIv2:
    """ Covid-19 API v2 model and its methods
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    def __init__(self) -> None:
        """ Initiate DataFrames """
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
    
    def wrap_data(func) -> Dict[str, Any]:
        """ Wrap a result in a schemed data """
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Dict[str, Any]:
            packed_data = self.scheme
            packed_data['data'] = []
            try:
                packed_data['data'] = func(self, *args, **kwargs)
            except Exception as e:
                print(e)
            finally:
                time_format = '%m-%d-%Y'
                packed_data['dt'] = datetime.utcnow().strftime(time_format)
                packed_data['ts'] = datetime.strptime(packed_data['dt'], time_format).timestamp()
            return packed_data
        return wrapper
    
    @wrap_data
    def get_current(self) -> Dict[str, Any]:
        """ Current data from all locations (Lastest date) """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [v for v in df_grp_by_country.to_dict('index').values()]

        return data
    
    @wrap_data
    def get_current_US(self) -> Dict [str, Any]:
        """ Get current data for USA's situation """
        self.df_US = get_data_daily_reports_us() # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'People_Tested', 'People_Hospitalized']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed', ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns

        data = [v for v in df.to_dict('index').values()]

        return data
    
    @wrap_data
    def get_country(self, country_name: str) -> Dict[str, Any]:
        """ Get a country data from its name or ISO 2 """
        all_country_data = self.get_current()['data']

        # Check input
        if not isinstance(country_name, str) or not country_name.isalpha():
            return {}

        # Search for a given country
        country_name = country_name.lower()
        country_name_from_code = self.lookup_table.get(country_name.upper(), '').lower()

        data = [country_data for country_data in all_country_data if country_data['location'].lower() in [country_name, country_name_from_code]]
        data = data[0] if data else {}

        return data

    @wrap_data
    def get_confirmed(self) -> Dict[str, Any]:
        """ Summation of all confirmed cases """
        self.df = get_data_daily_reports() # Get base data
        data = int(self.df['Confirmed'].sum())

        return data

    @wrap_data
    def get_deaths(self) -> Dict[str, Any]:
        """ Summation of all deaths """
        self.df = get_data_daily_reports() # Get base data
        data = int(self.df['Deaths'].sum())

        return data
    
    @wrap_data
    def get_recovered(self) -> Dict[str, Any]:
        """ Summation of all recovers """
        self.df = get_data_daily_reports() # Get base data
        data = int(self.df['Recovered'].sum())

        return data

    @wrap_data
    def get_active(self) -> Dict[str, Any]:
        """ Summation of all actives """
        self.df = get_data_daily_reports() # Get base data
        data = int(self.df['Active'].sum())

        return data
    
    @wrap_data
    def get_total(self) -> Dict[str, Any]:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        self.df = get_data_daily_reports() # Get base data
        data = {
            'confirmed': int(self.df['Confirmed'].sum()),
            'deaths': int(self.df['Deaths'].sum()),
            'recovered': int(self.df['Recovered'].sum()),
            'active': int(self.df['Active'].sum())
        }
        
        return data

    def __extract_time_series(self, time_series: Dict) -> List[Dict]:
        """ Extract time series from a given case """

        def __unpack_inner_time_series(time_series: Dict[str, Any]) -> Dict[str, Any]:
            for data in time_series.values():
                excluded_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']
                temp_dict = {}
                temp_dict['Province/State'] = data['Province/State']
                temp_dict['Country/Region'] = data['Country/Region']
                temp_dict['Coordinates'] = {'Lat': float(data['Lat']), 'Long': float(data['Long'])}

                temp_time_series_dict = {k: int(v) for k, v in data.items() if k not in excluded_cols}
                temp_dict['TimeSeries'] = [{'date': k, 'value': v} for k, v in temp_time_series_dict.items()]

                yield temp_dict

        # Extract the time series data
        time_series_data = []
        for data in __unpack_inner_time_series(time_series):
            time_series_data.append(data) 

        return time_series_data

    def __extract_US_time_series(self, time_series: Dict[str, Any]) -> List[Dict]:
        """ Extract USA time series """

        def __unpack_US_inner_time_series(time_series: Dict[str, Any]) -> Dict[str, Any]:
            for data in time_series.values():
                excluded_cols = ['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                'Admin2','Province_State', 'Country_Region', 'Lat', 'Long_', 
                                'Combined_Key','Population']
                temp_dict = {}
                temp_dict['Province_State'] = data['Province_State']
                temp_dict['Country_Region'] = data['Country_Region']
                temp_dict['Info'] = {
                    'UID': data['UID'],
                    'iso2': data['iso2'],
                    'iso3': data['iso3'],
                    'code3': data['code3'],
                    'FIPS': data['FIPS'],
                    'Admin2': data['Admin2']
                }
                temp_dict['Coordinates'] = {'Lat': float(data['Lat']), 'Long': float(data['Long_'])}

                temp_time_series_dict = {k: int(v) for k, v in data.items() if k not in excluded_cols}
                temp_dict['TimeSeries'] = [{'date': k, 'value': v} for k, v in temp_time_series_dict.items()]

                yield temp_dict

        # Extract the time series data
        time_series_data = []
        for data in __unpack_US_inner_time_series(time_series):
            time_series_data.append(data) 

        return time_series_data

    def __extract_time_series_global(self, dataframe_dict: Dict[str, pd.DataFrame]) -> List[Dict]:
        """ Extract time series for global case
            Iterating all cases from all time series
        """
        global_df_list = []

        for key, df in dataframe_dict.items():
            df_temp = pd.DataFrame(df.iloc[:, 4:].astype('int32').sum(axis=0)) # Slice to select time series data (exclude country info)
            df_temp.columns = [key] # A dataframe with one column named by a key (case), rows are time series
            global_df_list.append(df_temp)

        # Combine DataFrames
        global_dict = pd.concat(global_df_list, axis=1, sort=False).T.to_dict()
        data = [{k: v} for k, v in global_dict.items()]

        return data
    
    @wrap_data
    def get_time_series(self, case: str) -> Dict[str, Any]:
        """ Get time series data from a given case
            1.) global
            2.) confirmed, deaths, recovered
        """
        self.df_time_series = get_data_time_series() # Get base data

        if case not in ['global']:
            raw_data = self.df_time_series[case].T.to_dict()
            data = self.__extract_time_series(raw_data)
        else:
            raw_data = self.df_time_series
            data = self.__extract_time_series_global(raw_data)

        return data
    
    @wrap_data
    def get_US_time_series(self, case: str) -> Dict[str, Any]:
        """ Get USA time series """
        if case not in ['confirmed', 'deaths']:
            data = []
        else:
            self.df_US_time_series = get_US_time_series() # Get base data
            raw_data = self.df_US_time_series[case].T.to_dict()
            data = self.__extract_US_time_series(raw_data)

        return data
