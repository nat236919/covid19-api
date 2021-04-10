#######################################
# CurrentModelRoot
#######################################
import pandas as pd
from datetime import datetime
from functools import wraps
from typing import List, Dict, Any

from models.covid_api_v2_model import (CurrentCountryModel, CurrentUSModel,
                                       TimeseriesBuilder, TimeseriesCaseModel, TimeseriesGlobalModel,
                                       TimeseriesUSInfoBuilder)

from models.covid_api_v2_model import CurrentModel
from pydantic import BaseModel

from models.base_model import ResponseModel

from utils.get_data import get_data_lookup_table, DailyReports, DataTimeSeries

class DataFetcher:
    def get_reports(self, daily_reports: 'DataOrganizer') -> pd.DataFrame:
        raise NotImplemented

    def get_grouped(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplemented

    def cast_to_int(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplemented

    def reorder_df(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplemented

    def get_as_data_model_list(self, df: pd.DataFrame) -> list:
        raise NotImplemented


class DataOrganizer:
    fetcher: DataFetcher

    def __init__(self, fetcher: DataFetcher):
        self.fetcher = fetcher

    def fetch_data(self, daily_reports: DailyReports) -> pd.DataFrame:
        reports = self.fetcher.get_reports(daily_reports)
        reports = self.fetcher.get_grouped(reports)
        reports = self.fetcher.cast_to_int(reports)
        reports = self.fetcher.reorder_df(reports)
        return reports

    def get_as_data_model_list(self, df: pd.DataFrame) -> list:
        return self.fetcher.get_as_data_model_list(df)

class CurrentModelRoot:
    country_models: List[CurrentCountryModel]
    states_models: List[CurrentUSModel]

    def __init__(self, daily_reports: DailyReports):

        self.country_models = []
        self.states_models = []
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports

    def wrap_data(func) -> dict:
        """
        Wrap a result in a schemed data, it keeps the aggregation as all results from functions
        wrapped with this will become dicts
         """

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

            return reponse_model.dict()

        return wrapper

    def update_country_models(self) -> None:
        """ Sets country_models to the current data from all locations (Lastest date) """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        self.df = self.daily_reports.get_data_daily_reports()  # Get base data
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df_grp_by_country[concerned_columns] = self.df_grp_by_country[concerned_columns].astype(int)

        df_grp_by_country = self.df_grp_by_country.sort_values(by='Confirmed', ascending=False)
        df_grp_by_country = df_grp_by_country.reset_index()
        df_grp_by_country.columns = ['location', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentModel(**v) for v in df_grp_by_country.to_dict('index').values()]
        self.country_models = data

    def update_US_models(self) -> None:
        """ Get current data for USA's situation """
        self.df_US = self.daily_reports.get_data_daily_reports(US=True)  # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed',
                                                                                         ascending=False)
        df = df[concerned_columns].astype(int)
        df = df.reset_index()
        df.columns = ['Province_State'] + concerned_columns
        df.columns = ['province_state', 'confirmed', 'deaths', 'recovered', 'active']

        data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]
        self.states_models = data

    @wrap_data
    def get_all_countries(self) -> List[CurrentCountryModel]:
        """ Current data from all locations (Lastest date) """
        self.update_country_models()
        return self.country_models

    @wrap_data
    def get_us(self) -> List[CurrentUSModel]:
        """ Get current data for USA's situation """
        self.update_US_models()
        return self.states_models

    @wrap_data
    def get_country(self, country_name: str) -> CurrentCountryModel:
        """ Get a country data from its name or ISO 2 """
        self.update_country_models()
        # Check input
        if not isinstance(country_name, str) or not country_name.isalpha():
            return {}

        # Search for a given country
        country_name = country_name.lower()
        country_name_from_code = self.lookup_table.get(country_name.upper(), '').lower()

        data = [country_data for country_data in self.country_models if
                country_data.location.lower() in [country_name, country_name_from_code]]
        data = data[0] if data else {}

        return data

    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @wrap_data
    def get_confirmed(self) -> dict:
        """ Summation of all confirmed cases """
        self.update_country_models()
        sum = 0
        for x in self.country_models:
            sum += x.confirmed
        return {'confirmed': sum}

    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @wrap_data
    def get_deaths(self) -> dict:
        """ Summation of all deaths """
        self.update_country_models()
        sum = 0
        for x in self.country_models:
            sum += x.deaths
        return {'deaths': sum}

    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @wrap_data
    def get_recovered(self) -> dict:
        """ Summation of all recovers """
        self.update_country_models()
        sum = 0
        for x in self.country_models:
            sum += x.recovered
        return {'recovered': sum}

    #######################################################################################
    # GET - Active
    #######################################################################################
    @wrap_data
    def get_active(self) -> dict:
        """ Summation of all actives """
        self.update_country_models()
        sum = 0
        for x in self.country_models:
            sum += x.active
        return {'active': sum}

    #######################################################################################
    # GET - Total
    #######################################################################################
    @wrap_data
    def get_total(self) -> dict:
        """ Summation of Confirmed, Deaths, Recovered, Active """
        self.update_country_models()
        data = {
            'active': 0,
            'recovered': 0,
            'deaths': 0,
            'confirmed': 0
        }
        for x in self.country_models:
            data['active'] += x.active
            data['recovered'] += x.recovered
            data['deaths'] += x.deaths
            data['confirmed'] += x.confirmed
        return data


class TimeseriesModelRoot:
    country_timeseries: List[TimeseriesCaseModel]
    us_timeseries: List[TimeseriesCaseModel]

    def __init__(self, time_series: DataTimeSeries):
        self.country_timeseries = []
        self.us_timeseries = []

        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }

        self.time_series = time_series

    def wrap_data(func) -> dict:
        """
        Wrap a result in a schemed data, it keeps the aggregation as all results from functions
        wrapped with this will become dicts
         """

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

            return reponse_model.dict()

        return wrapper

    def _update_time_series(self) -> None:
        """ Update all series
        """
        self.df_time_series = self.time_series.get_data_time_series()  # Get base data

        raw_data = self.df_time_series

        self.global_data = self.__extract_time_series_global(raw_data)

        self.dict_global_data = {}

        for case in ['confirmed', 'deaths', 'recovered']:
            raw_d = raw_data[case].T.to_dict()
            self.dict_global_data[case] = self.__extract_time_series(raw_d)

    def _update_US_time_series(self) -> None:
        self.df_US_time_series = self.time_series.get_data_time_series(US=True)
        self.dict_US_data = {}

        for case in self.df_US_time_series.keys():
            raw_d = self.df_US_time_series[case].T.to_dict()
            self.dict_US_data[case] = self.__extract_US_time_series(raw_d)

    def __extract_time_series(self, time_series: Dict) -> List[TimeseriesCaseModel]:
        """ Extract time series from a given case """

        def __unpack_inner_time_series(time_series: Dict[str, Any]) -> TimeseriesCaseModel:
            for data in time_series.values():
                excluded_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']

                builder: TimeseriesBuilder = TimeseriesBuilder()
                # Coordinates

                builder.set_coordinates(
                    float(data['Lat']) if data['Lat'] else 0,
                    float(data['Long']) if data['Long'] else 0
                )

                # Timeseries Data
                for k, v in data.items():
                    if k not in excluded_cols:
                        v = int(v)
                        builder.add_data(k, v)

                # Main Model
                builder.set_province_state(data['Province/State'])
                builder.set_country_region(data['Country/Region'])

                yield builder.build()

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
            df_temp = pd.DataFrame(
                df.iloc[:, 4:].astype('int32').sum(axis=0))  # Slice to select time series data (exclude country info)
            df_temp.columns = [key]  # A dataframe with one column named by a key (case), rows are time series
            global_df_list.append(df_temp)

        # Combine DataFrames
        global_dict = pd.concat(global_df_list, axis=1, sort=False).T.to_dict()
        data = [{k: TimeseriesGlobalModel(**v)} for k, v in global_dict.items()]

        return data

    def __extract_US_time_series(self, time_series: Dict[str, Any]) -> List[TimeseriesCaseModel]:
        """ Extract USA time series """

        def __unpack_US_inner_time_series(time_series: Dict[str, Any]) -> TimeseriesCaseModel:
            for data in time_series.values():
                excluded_cols = ['UID', 'iso2', 'iso3', 'code3', 'FIPS',
                                 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_',
                                 'Combined_Key', 'Population']

                builder: TimeseriesBuilder = TimeseriesBuilder(is_info_required=True)

                # Info
                us_info_builder: TimeseriesUSInfoBuilder = builder.set_info()
                (
                    us_info_builder
                        .set_UID(data['UID'])
                        .set_iso2(data['iso2'])
                        .set_iso3(data['iso3'])
                        .set_code3(data['code3'])
                        .set_FIPS(data['FIPS'])
                        .set_Admin2(data['Admin2'])
                )

                # Coordinates
                builder.set_coordinates(
                    float(data['Lat']) if data['Lat'] else 0,
                    float(data['Long_']) if data['Long_'] else 0
                )
                # Timeseries
                for k, v in data.items():
                    if k not in excluded_cols:
                        v = int(v)
                        builder.add_data(k, v)

                # Main Model
                builder.set_province_state(data['Province/State'])
                builder.set_country_region(data['Country/Region'])

                yield builder.build()

        # Extract the time series data
        time_series_data = []
        for data in __unpack_US_inner_time_series(time_series):
            time_series_data.append(data)

        return time_series_data

    @wrap_data
    def get_US_time_series(self, case: str) -> List[TimeseriesCaseModel]:
        """ Get USA time series """
        self._update_US_time_series()
        return self.dict_US_data[case]

    @wrap_data
    def get_time_series(self, case: str) -> List[Any]:
        """ Get time series data from a given case
            1.) global
            2.) confirmed, deaths, recovered
        """
        self._update_time_series()
        return self.global_data if case in ['global'] else self.dict_global_data[case]
