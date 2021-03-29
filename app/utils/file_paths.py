"""
FILE: file_paths.py
DESCRIPTION: Keep file paths from the data source
AUTHOR: Nuttaphat Arunoprayoch
DATE: 17-April-2020
"""
# Johns Hopkins CSSE - Datasets (https://github.com/CSSEGISandData/COVID-19)

from abc import ABCMeta, abstractmethod
"""
FILE: file_paths.py
DESCRIPTION: Keep file paths from the data source
AUTHOR: Nuttaphat Arunoprayoch
DATE: 17-April-2020
"""


class Path_IBuilder(metaclass=ABCMeta):
    "The Path Builder Interface"

    @staticmethod
    @abstractmethod
    def build_JHU_CSSE_BASE_PATH():
        "Builds path to the JHU's covid-19 database"

    @staticmethod
    @abstractmethod
    def build_DAILY_REPORT_PATH():
        "extention for the JHU_CSSE_BASE_PATH to get Daily Reports"

    @staticmethod
    @abstractmethod
    def build_DAILY_REPORT_US_PATH():
        "extention for the JHU_CSSE_BASE_PATH to get Daily Reports in US"

    @staticmethod
    @abstractmethod
    def build_TIME_SERIES_PATH():
        "extention for the JHU_CSSE_BASE_PATH to get Time Series"

    @staticmethod
    @abstractmethod
    def build_LOOKUP_TABLE_PATH():
        "extention for the JHU_CSSE_BASE_PATH to get Lookup Table"

    @staticmethod
    @abstractmethod
    def build_CSV_EXTENSTION():
        " '{}.csv' extention for suitable paths"

    @staticmethod
    @abstractmethod
    def build_time_series_global_CSV_EXTENSTION():
        " 'time_series_covid19_{}_global.csv' extention for suitable paths"

    @staticmethod
    @abstractmethod
    def build_time_series_US_CSV_EXTENSTION():
        " 'time_series_covid19_{}_US.csv' extention for suitable paths"

    @staticmethod
    @abstractmethod
    def get_Path():
        " returns the constructed path "


class Path_Builder(Path_IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.path = Path()

    def build_JHU_CSSE_BASE_PATH(self):
        self.path.parts.join(
            'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'
        )
        return self

    def build_DAILY_REPORT_PATH(self):
        self.path.parts.join(
            'csse_covid_19_daily_reports/'
        )
        return self

    def build_DAILY_REPORT_US_PATH(self):
        self.path.parts.join(
            'csse_covid_19_daily_reports_us/'
        )
        return self

    def build_TIME_SERIES_PATH(self):
        self.path.parts.join(
            'csse_covid_19_time_series/'
        )
        return self

    def build_LOOKUP_TABLE_PATH(self):
        self.path.parts.join(
            'UID_ISO_FIPS_LookUp_Table.csv'
        )
        return self

    def build_CSV_EXTENSTION(self):
        self.path.parts.join(
            '{}.csv'
        )
        return self

    def build_time_series_global_CSV_EXTENSTION(self):
        self.path.parts.join(
            'time_series_covid19_{}_global.csv'
        )
        return self

    def build_time_series_US_CSV_EXTENSTION(self):
        self.path.parts.join(
            'time_series_covid19_{}_US.csv'
        )
        return self

    def get_Path(self):
        return self.path


class Path():
    "The Path"

    def __init__(self):
        self.parts = ""


class Director():
    "The Director, building a complex representation of path."

    @staticmethod
    def construct_Daily_Report_Path():
        " Constructs and returns the Daily Reports Path "
        return Path_Builder()\
            .build_JHU_CSSE_BASE_PATH()\
            .build_DAILY_REPORT_PATH()\
            .build_CSV_EXTENSTION()\
            .get_Path()

    @staticmethod
    def construct_Daily_Report_US_Path():
        " Constructs and returns the US's Daily Reports Path "
        return Path_Builder()\
            .build_JHU_CSSE_BASE_PATH()\
            .build_DAILY_REPORT_US_PATH()\
            .build_CSV_EXTENSTION()\
            .get_Path()

    @staticmethod
    def construct_global_TimeSeries_Path():
        " Constructs and returns the global timeseries Path "
        return Path_Builder()\
            .build_JHU_CSSE_BASE_PATH()\
            .build_TIME_SERIES_PATH()\
            .build_time_series_global_CSV_EXTENSTION()\
            .get_Path()

    @staticmethod
    def construct_US_TimeSeries_Path():
        " Constructs and returns the US timeseries Path "
        return Path_Builder()\
            .build_JHU_CSSE_BASE_PATH()\
            .build_TIME_SERIES_PATH()\
            .build_time_series_US_CSV_EXTENSTION()\
            .get_Path()

    @staticmethod
    def construct_LOOKUP_TABLE_path():
        " Constructs and returns the Lookup Table's path "
        return Path_Builder()\
            .build_JHU_CSSE_BASE_PATH()\
            .build_LOOKUP_TABLE_PATH()\
            .get_Path()


JHU_CSSE_CATEGORIES = ['confirmed', 'deaths', 'recovered']

JHU_CSSE_FILE_PATHS = {
    'BASE_URL_LOOKUP_TABLE': Director.construct_LOOKUP_TABLE_path,
    'BASE_URL_DAILY_REPORTS': Director.construct_Daily_Report_Path(),
    'BASE_URL_DAILY_REPORTS_US': Director.construct_Daily_Report_US_Path(),
    'BASE_URL_TIME_SERIES': Director.construct_global_TimeSeries_Path(),
    'BASE_URL_US_TIME_SERIES': Director.construct_US_TimeSeries_Path(),
    'CATEGORIES': JHU_CSSE_CATEGORIES
}
