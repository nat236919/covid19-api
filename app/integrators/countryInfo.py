from typing import List

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
from utils.get_data import (get_data_daily_reports,
                            get_data_daily_reports_us, get_data_lookup_table,
                            get_data_time_series, get_US_time_series)


class AbstractCountryInformation:

    def country_name(self):
        pass

    def total_case_by_country(self):
        pass


class CasesByCountryInformation(AbstractCountryInformation):

    def __init__(self):
        self.df_grp_by_country = self.df.groupby('Country_Region')[concerned_columns].sum()
        self.df = get_data_daily_reports()  # Get base data

    def country_name(self, country_name: str) -> CountryModel:
        """ Get a country data from its name or ISO 2 """
        concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
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

        data = [country_data for country_data in all_country_data if
                country_data.location.lower() in [country_name, country_name_from_code]]
        data = data[0] if data else {}

        return data

    def total_case_by_country(self):
        def get_total(self) -> TotalModel:
            """ Summation of Confirmed, Deaths, Recovered, Active """
            self.df = get_data_daily_reports()  # Get base data
            data = TotalModel(
                confirmed=int(self.df['Confirmed'].sum()),
                deaths=int(self.df['Deaths'].sum()),
                recovered=int(self.df['Recovered'].sum()),
                active=int(self.df['Active'].sum())
            )
            return data

    class CasesInUSAInformation(AbstractCountryInformation):

        def country_name(self):
            return "US"

        def total_case_by_country(self) -> List[CurrentUSModel]:
            """ Get current data for USA's situation """
            self.df_US = get_data_daily_reports_us()  # Get base data

            concerned_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active']
            df = self.df_US.groupby(['Province_State'])[concerned_columns].sum().sort_values(by='Confirmed',
                                                                                             ascending=False)
            df = df[concerned_columns].astype(int)
            df = df.reset_index()
            df.columns = ['Province_State'] + concerned_columns

            data = [CurrentUSModel(**v) for v in df.to_dict('index').values()]

            return data

