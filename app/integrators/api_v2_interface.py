# Import libraries
from typing import Any, Dict, List

class APIv2:
    # @abstractmethod
    # def get_current(self):
    #     pass

    # @abstractmethod
    # def get_current_US(self):
    #     pass

    # @abstractmethod
    # def get_country(self, country_name: str):
    #     pass

    # @abstractmethod
    # def get_confirmed(self):
    #     pass

    @abstractmethod
    def get_deaths(self):
        pass

    @abstractmethod
    def get_recovered(self):
        pass

    # @abstractmethod
    # def get_active(self):
    #     pass

    @abstractmethod
    def get_total(self):
        pass

    @abstractmethod
    def get_time_series(self):
        pass

    # @abstractmethod
    # def get_US_time_series(self, case: str):
    #     pass