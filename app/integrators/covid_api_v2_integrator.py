"""
FILE: covid_api_v2_integrator.py
DESCRIPTION: Integrators for API v2
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-March-2021
"""
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


class CovidAPIv2Integrator:
    """ Covid-19 API v2 methods
        SCHEMA: {
            "data": Any,
            "dt": str = "{datetime}",
            "ts": int = "{timestamp}
        }
    """
    
    def __init__(self,  daily_reports: DailyReports, time_series: DataTimeSeries) -> None:
        """ Initiate instances """
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
        self.time_series = time_series

    def wrap_data(func) -> ResponseModel:
        """ Wrap a result in a schemed data """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
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
                reponse_model = ResponseModel(**packed_data)
            return reponse_model
        return wrapper
    
    #######################################################################################
    # GET - Current
    #######################################################################################
    @wrap_data
    def get_current(self) -> List[CurrentModel]:
        """ Current data from all locations (Lastest date) """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel.set(((**v) for v in df_grp_by_country.to_dict('index').values()))]

        return data
    
    #######################################################################################
    # GET - Current US
    #######################################################################################
    @wrap_data
    def get_current_US(self) -> List[CurrentUSModel]:
        """ Get current data for USA's situation """
        self.df_US = self.daily_reports.get_data_daily_reports(US=True) # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed', ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns

        data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]

        return data
    
    #######################################################################################
    # GET - Country
    #######################################################################################
    @wrap_data
    def get_country(self, country_name: str) -> CountryModel:
        """ Get a country data from its name or ISO 2 """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        all_country_data = [CountryModel(**v) for v in df_grp_by_country.to_dict('index').values()]


        # Check input
        if not isinstance(country_name, str) or not country_name.isalpha():
            return {}

        # Search for a given country
        country_name = country_name.lower()
        country_name_from_code = self.lookup_table.get(country_name.upper(), '').lower()

        data = [country_data for country_data in all_country_data if country_data.location.lower() in [country_name, country_name_from_code]]
        data = data[0] if data else {}

        return data
    
    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @wrap_data
    def get_confirmed(self) -> ConfirmedModel:
        """ Summation of all confirmed cases """

        self.df = get_data_daily_reports() # Get base data
        data = ConfirmedModel.setConfirmedModel(int(self.df['Confirmed'].sum()))
     

        return data

    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @wrap_data
    def get_deaths(self) -> DeathsModel:
        """ Summation of all deaths """

        self.df = get_data_daily_reports() # Get base data
        data = DeathsModel.setDeathsModel(int(self.df['Deaths'].sum()))
        

        return data
    
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @wrap_data
    def get_recovered(self) -> RecoveredModel:
        """ Summation of all recovers """

        self.df = get_data_daily_reports() # Get base data
        data = RecoveredModel.setRecoveredModel(int(self.df['Recovered'].sum()))
        

    
        return data
    
    #######################################################################################
    # GET - Active
    #######################################################################################
    @wrap_data
    def get_active(self) -> ActiveModel:
        """ Summation of all actives """

        self.df = get_data_daily_reports() # Get base data
        data = ActiveModel.setActiveModel(int(self.df['Active'].sum()))
        

        return data
    
    #######################################################################################
    # GET - Total
    #######################################################################################
    @wrap_data
    def get_total(self) -> TotalModel:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        self.df = self.daily_reports.get_data_daily_reports() # Get base data
        data = TotalModel(
            confirmed=int(self.df['Confirmed'].sum()),
            deaths=int(self.df['Deaths'].sum()),
            recovered=int(self.df['Recovered'].sum()),
            active=int(self.df['Active'].sum())
        )
        return data
    
    #######################################################################################
    # GET - Timeseries
    #######################################################################################
    @wrap_data
    def get_time_series(self, case: str) -> List[Any]:
        """ Get time series data from a given case
            1.) global
            2.) confirmed, deaths, recovered
        """
        self.df_time_series = self.time_series.get_data_time_series() # Get base data

        if case not in ['global']:
            raw_data = self.df_time_series[case].T.to_dict()
            data = self.__extract_time_series(raw_data)
        else:
            raw_data = self.df_time_series
            data = self.__extract_time_series_global(raw_data)

        return data
    
    def __extract_time_series(self, time_series: Dict) -> List[TimeseriesCaseModel]:
        """ Extract time series from a given case """

        def __unpack_inner_time_series(time_series: Dict[str, Any]) -> TimeseriesCaseModel:
            for data in time_series.values():
                excluded_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']
                # Coordinates
                timeseries_coordinates_model = TimeseriesCaseCoordinatesModel(
                    Lat=float(data['Lat']) if data['Lat'] else 0,
                    Long=float(data['Long']) if data['Long'] else 0
                )
                # Timeseries Data
                temp_time_series_dict = {k: int(v) for k, v in data.items() if k not in excluded_cols}
                timeseries_data_model_list = [TimeseriesCaseDataModel(date=k, value=v) for k, v in temp_time_series_dict.items()]

                # Main Model
                timeseries_case_model = TimeseriesCaseModel(
                    Province_State=data['Province/State'],
                    Country_Region=data['Country/Region'],
                    Coordinates=timeseries_coordinates_model,
                    TimeSeries=timeseries_data_model_list
                )
                yield timeseries_case_model

        # Extract the time series data
        time_series_data = []
        for data in __unpack_inner_time_series(time_series):
            time_series_data.append(data) 

        return time_series_data
    
    def __extract_time_series_global(self, dataframe_dict: Dict[str, pd.DataFrame]) -> List[TimeseriesGlobalModel]:
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
        data = [{k: TimeseriesGlobalModel(**v)} for k, v in global_dict.items()]

        return data
    
    #######################################################################################
    # GET - Timeseries US
    #######################################################################################
    @wrap_data
    def get_US_time_series(self, case: str) -> List[TimeseriesUSModel]:
        """ Get USA time series """
        if case not in ['confirmed', 'deaths']:
            data = []
        else:
            self.df_US_time_series = self.time_series.get_data_time_series(US=True) # Get base data
            raw_data = self.df_US_time_series[case].T.to_dict()
            data = self.__extract_US_time_series(raw_data)

        return data

    def __extract_US_time_series(self, time_series: Dict[str, Any]) -> List[TimeseriesUSModel]:
        """ Extract USA time series """

        def __unpack_US_inner_time_series(time_series: Dict[str, Any]) -> TimeseriesUSModel:
            for data in time_series.values():
                excluded_cols = ['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                'Admin2','Province_State', 'Country_Region', 'Lat', 'Long_', 
                                'Combined_Key','Population']
                # Info
                timeseries_US_info_model = TimeseriesUSInfoModel(
                    UID=data['UID'],
                    iso2=data['iso2'],
                    iso3=data['iso3'],
                    code3=data['code3'],
                    FIPS=data['FIPS'],
                    Admin2=data['Admin2'],
                )
                # Coordinates
                timeseries_US_coordinates_model = TimeseriesUSCoordinatesModel(
                    Lat=float(data['Lat']) if data['Lat'] else 0,
                    Long=float(data['Long_']) if data['Long_'] else 0
                )
                # Timeseries
                temp_time_series_dict = {k: int(v) for k, v in data.items() if k not in excluded_cols}
                timeseries_data_model_list = [TimeseriesUSDataModel(date=k, value=v) for k, v in temp_time_series_dict.items()]

                # Main Model
                timeseries_US_model = TimeseriesUSModel(
                    Province_State=data['Province_State'],
                    Country_Region=data['Country_Region'],
                    Info=timeseries_US_info_model,
                    Coordinates=timeseries_US_coordinates_model,
                    TimeSeries=timeseries_data_model_list
                )
                yield timeseries_US_model

        # Extract the time series data
        time_series_data = []
        for data in __unpack_US_inner_time_series(time_series):
            time_series_data.append(data)

        return time_series_data
