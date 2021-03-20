


#######################################
# CurrentModelRoot
#######################################
from datetime import datetime
from functools import wraps
from typing import List

from models.covid_api_v2_model import CurrentCountryModel, CurrentUSModel

from models.covid_api_v2_model import CurrentModel
from pydantic import BaseModel

from models.base_model import ResponseModel

from utils.get_data import get_data_lookup_table, DailyReports, DataTimeSeries


class CurrentModelRoot:
    country_models: List[CurrentCountryModel]
    states_models: List[CurrentUSModel]

    def __init__(self,  daily_reports: DailyReports, time_series: DataTimeSeries):

        self.country_models = []
        self.states_models = []
        self.lookup_table = get_data_lookup_table()
        self.scheme = {
            'data': None,
            'dt': None,
            'ts': None
        }
        self.daily_reports = daily_reports
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
        self.df_US = self.daily_reports.get_data_daily_reports(US=True) # Get base data

        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
        df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed', ascending=False)
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

        data = [country_data for country_data in self.country_models if country_data.location.lower() in [country_name, country_name_from_code]]
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



