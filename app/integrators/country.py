import pandas as pd
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


class CountryAbstract:
    def __init__(self, AbstractCountryInformation):
        self.country_information = AbstractCountryInformation

    def country(self):
        pass

    def country_information(self):
        pass


class CountryCasesImplement(CountryAbstract):

    def __init__(self, CountryInformation, objects):
        super().__init__(CountryInformation)
        self.objects = objects

    def country(self):
        self.country_information.country_name(self.objects)

    def country_information(self):
        self.country_information.total_case_by_country(self.objects)


class USACasesImplement(CountryAbstract):
    def __init__(self, CountryInformation, objects):
        super().__init__(CountryInformation)
        self.objects = objects

    def country(self):
        self.country_information.country_name("US")

    def country_information(self):
        self.country_information.total_case_by_country(self.objects)

