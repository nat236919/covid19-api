from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List
from models.covid_api_v1_model import (ConfirmedModel, CountriesModel,
                                         CurrentListModel, CurrentModel,
                                         DeathsModel, RecoveredModel,
                                         TimeseriesCoordinatesModel,
                                         TimeseriesDataModel, TimeseriesModel,
                                         TotalModel)
from utils.get_data import get_data

class ICovidAPIv1(metaclass=ABCMeta):
    "the Builder Interface"

    @staticmethod
    @abstractmethod
    def add_dt_and_ts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_current_status(self, list_required: bool = False) -> Dict[str, Any]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_confirmed_cases(self) -> Dict[str, int]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_deaths(self) -> Dict[str, int]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_recovered(self) -> Dict[str, int]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_total(self) -> Dict[str, Any]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_affected_countries(self) -> Dict[str, List]:
        "A static interface method"
    
    @staticmethod
    @abstractmethod
    def get_time_series(self) -> Dict[str, Dict]:
        "A static interface method"
