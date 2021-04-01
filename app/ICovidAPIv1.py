from abc import ABCMeta, abstractmethod

class ICovidAPIv1(metaclass=ABCMeta):
    "the Builder Interface"

    #######################################################################################
    # GET - Datetime and Timestamp
    #######################################################################################
    @staticmethod
    @abstractmethod
    def add_dt_and_ts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        "A static interface method"
    
    #######################################################################################
    # GET - Current data
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_current_status(self, list_required: bool = False) -> Dict[str, Any]:
        "A static interface method"
    
    #######################################################################################
    # GET - Confirm
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_confirmed_cases(self) -> Dict[str, int]:
        "A static interface method"
    
    #######################################################################################
    # GET - Deaths
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_deaths(self) -> Dict[str, int]:
        "A static interface method"
    
    #######################################################################################
    # GET - Recovered
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_recovered(self) -> Dict[str, int]:
        "A static interface method"
    
    #######################################################################################
    # GET - Total
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_total(self) -> Dict[str, Any]:
        "A static interface method"
    
    #######################################################################################
    # GET - Affected Countries
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_affected_countries(self) -> Dict[str, List]:
        "A static interface method"
    
    #######################################################################################
    # GET - Timeseries
    #######################################################################################
    @staticmethod
    @abstractmethod
    def get_time_series(self) -> Dict[str, Dict]:
        "A static interface method"
