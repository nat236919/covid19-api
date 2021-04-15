# Import libraries
from typing import Any, Dict, List

class APIv1:
    @abstractmethod
    def add_dt_and_ts(self):
        pass

    @abstractmethod
    def get_current_status(self):
        pass
    
    @abstractmethod
    def get_confirmed_cases(self):
        pass

    @abstractmethod
    def get_deaths(self):
        pass

    @abstractmethod
    def get_recovered(self):
        pass

    @abstractmethod
    def get_total(self):
        pass

    @abstractmethod
    def get_affected_countries(self):
        pass

    @abstractmethod
    def get_time_series(self):
        pass