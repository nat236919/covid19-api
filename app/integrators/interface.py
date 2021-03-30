from abc import ABCMeta, abstractmethod

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
class IIntegrator(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Integrator)"

    @staticmethod
    @abstractmethod
    def wrap_data(func) -> ResponseModel:
        pass
    #######################################################################################
    # GET - Current
    #######################################################################################
    @wrap_data
    def get_current(self) -> List[CurrentModel]:
        pass
    #######################################################################################
    # GET - Current US
    #######################################################################################
    @wrap_data
    def get_current_US(self) -> List[CurrentUSModel]:
        pass
    #######################################################################################
    # GET - Country
    #######################################################################################
    @wrap_data
    def get_country(self, country_name: str) -> CountryModel:
        pass
    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @wrap_data
    def get_confirmed(self) -> ConfirmedModel:
        pass
    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @wrap_data
    def get_deaths(self) -> DeathsModel:
        pass
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @wrap_data
    def get_recovered(self) -> RecoveredModel:
        pass
    #######################################################################################
    # GET - Active
    #######################################################################################
    @wrap_data
    def get_active(self) -> ActiveModel:
        pass
    #######################################################################################
    # GET - Total
    #######################################################################################
    @wrap_data
    def get_total(self) -> TotalModel:
        pass

    #######################################################################################
    # GET - Timeseries
    #######################################################################################
    @wrap_data
    def get_time_series(self, case: str) -> List[Any]:
        pass
    #######################################################################################
    # GET - Timeseries US
    #######################################################################################
    @wrap_data
    def get_US_time_series(self, case: str) -> List[TimeseriesUSModel]:
        pass
